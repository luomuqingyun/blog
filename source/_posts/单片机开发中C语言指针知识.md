---
title: 单片机开发中C语言指针知识
author: luomuqingyun
comments: true
category:
  - 编程
  - 经验
tags:
  - 编程经验
excerpt:
  - C语言指针知识
date: 2025-05-19 14:42:00
---
哈
## 指针，初学者的梦魇
对于初学者，在学习C语言的过程中每每提到指针都会让无数人闻风散胆吧。因为在我们学C语言的时候很多人（包括学长或老师）可能都会告诉我们指针是C语言中最难的一部分，所以导致还没开始接触就劝退了一批人。确实，C语言的精华也在于此，这也是它之所以长盛不衰的原因。很多时候初学者之所以害怕使用指针是因为害怕去尝试，其实如果在初学阶段愿意去尝试，敢于去修改bug，这时你就会发现指针学起来也简单多了。你是不是因为害怕搞混`*(p+1)`与`*p+1`,`const int *p`与`int *const p`,`**p`,`&p`等看起来就让人蒙圈的变量、符号，并且怎么记都似乎记不住？那就应该多去练习！在之前的内容中我也一直没有写这部分知识点，因为我自己觉得指针只要去使用它确实是没难度的，另外一个原因是，这种没难度似乎又只可意会不可言传，自己总结出来的话总是没有书籍中写的清晰，每个人基础不一样同样的话对不同人理解的程度又不同，所以这里还是希望初学者自己主动把这块硬骨头啃下去，我就提点我自己认证之内的技巧供大家参考。
## 从定义出发去理解指针
这里对于指针的官方定义我就不做搬运了，所有讲解C语言的书本都少不了对指针的定义。如果需要权威的说明可以查看`《C Primer Plus》`这本经典书籍，其中还包含很多细节说明和举例应用，把它作为参考书再好不过了，我想我能描述出来的文字绝对比不上他书中写的专业详细。指针最简单的概念就是：它是程序运行过程中的一个`内存地址`。至于一些针对指针变量衍生出来的奇奇怪怪的的表达式实质上就是运算符优先级与结合规律的基础内容。如果区分不出来可以先复习运算符部分知识。我们都知道所有程序要跑起来都需要先加载到内存中，程序运行所需的数据都会根据程序指令进行动态分配。很多朋友平时可能会说，哎呀，我的电脑（手机）又卡死啦，这时候很大可能性就是你的电脑或手机内存被占满了，而不是硬盘（存储器）没有足够空间。当然如果你的磁盘空间不够，然后运行内存也消耗过多那活该你的机器被卡。
## 学习时该怎么样避免踩坑
还是哪句话，多练习把坑踩平自然而就不会再踩坑了，这肯定是一句废话，学啥技术都可以这么说。我的建议就是善用编译器的`调试功能`和`printf()`函数，现在的编译器功能都是越来越完善的，在初学阶段使用程序调试功能可以让你少走很多弯路，结合打断点调试程序，单步执行，观察变量信息，哪里对点哪里，调多了你编程都会越来越有手感。当然，等你有一定经验之后，在项目开发过程中还是希望你不要过多的依赖调试功能。希望你对程序能够熟练到通过看代码就能发现逻辑是否正确。至于初学者嘛，此时不用你还想啥时候用呢！另外一个很关键的的技巧就是多打印信息，当然也是要你到处都打印，一个变量都不落下的打印，如果你不想时不时的调试代码，那就选择这种方式，选择在关键的地方对关键的数据进行输出，这样你直接在控制或者串口助手中就能及时发现问题。当然采用这种方式在开发阶段还是比较实用的，如果在巧妙的结合一些宏定义语句进入功能调试的差不多之后就整体关闭输出就好了，即使日后出现bug需要再调试处理起来也是非常方便。所以以上两种方法用于练习指针操作对初学者来说也是再好不过了，总之我曾经就是这么练习的。
## Keil中怎么了解指针
Keil和常用的C语言编译器VS一样具备调试功能，所以在你不会的时候也是可以采用调试的办法仿真程序运行结果来达到学习指针的目的。下面举一个简单的例子来说明。

随便写一个逻辑上跑得通的例子程序，编译没问题之后点击debug即可。
```
#include <reg52.h> 
#include <intrins.h> 

unsigned int var1 = 0;
unsigned int idata var2[] = {1,2,3,4};
unsigned int data var3[] = {5,6,7};
unsigned int var4[] = {8,9};
unsigned int code var5[] = {10,11,12};

unsigned int data *var6;
unsigned int *var7;
unsigned int *var8;
unsigned int *var9;
unsigned int *var10;
//unsigned int *var11;

void main(void)
{
    var1 = 100;
    var2[0] = 101;   
    var3[0] = 102;
    var4[0] = 103;
//    va5[0] = 104;//这是一条错误语句，存放于flash中的数据为只读
    
    var6 = &var1;
    var7 = &var2;
    var8 = &var3;
    var9 = &var4;
    var10 = &var5;
}
```
在接下来弹出的窗口中就可以查看，哪些是指针的地址，以及其对应的值，都可以看的一目了然。

![汇编中内存信息](https://files.mdnice.com/user/38598/12869435-8941-4f68-af37-67f47925b3ce.png)

这个办法学起来难度不比单纯的敲代码更有意义吗，即可以从底层了解单片机执行原理又可以了解代码的执行过程，我感觉这应该不会那么无聊吧。单片机只是一种微型的计算机放大到开发计算机程序也是一样的道理吧。

如果底层代码理解起来有一定的难度也可以添加变量到观察窗口进行单步测试，这样也一样直观明了。

![变量观察窗口](https://files.mdnice.com/user/38598/0ca47657-d1d3-438f-80d4-8c3ef0b4fe30.png)

当然还有很多方法进行查看指针变量的变化过程，这里只是举了一个非常简单的例子，初学者完全可以充分发挥自己的动手能力探索自己的方法。如果有自己想法欢迎留言或私信交流。

#### 推荐阅读
- [51单片机入门看这一篇就够了](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485523&idx=1&sn=b7fcd1b86e2467d6f03b1a520c39bb06&chksm=ea790022dd0e893452c4994fa16d63111b16d9878c303712f695b58b7af360b7b18c1ed4b201&token=1711068967&lang=zh_CN#rd)
- [怎么快速上手一款新的MCU](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485581&idx=1&sn=b36e6536717774f7931c7aa93d5b237a&chksm=ea7900fcdd0e89ea0db13737720edc996fcb3fdbab3e43b4a92316240ac66d4b5a8bf9a07e78&token=466212876&lang=zh_CN#rd)
- [Keil软件如何高效格式化代码](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485572&idx=1&sn=17cefa35d9d660083d419a7e9b6db6f7&chksm=ea7900f5dd0e89e35b65ba26354cc69ad24f686d8e18abd34e0932567a9345e8c9ed653eee6b&token=1711068967&lang=zh_CN#rd)
- [分享几个windows平台上非常实用的工具](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485420&idx=2&sn=728ca4abbadf7caf51c392e7d7045cbe&chksm=ea790f9ddd0e868b9fa162c80db1876199845f387bbe851c8d38a4e8412329ae635916c13cfb&token=1711068967&lang=zh_CN#rd)


----
![欢迎扫码关注公众号](https://files.mdnice.com/user/38598/659b642c-fcce-4f9c-becc-038eadd2c655.jpg)

----
![欢迎添加作者微信](https://files.mdnice.com/user/38598/37e7b97e-a5c7-44d1-9e48-bbe22ab3141d.jpg)

----