---
title: STM32位带操作（修改）
author: luomuqingyun
comments: true
category:
  - 编程
  - 单片机
tags:
  - 编程经验
  - STM32
excerpt:
  - STM32位带操作
date: 2025-05-19 14:42:00
---
## 修改声明
之前写的文章后半部分关于位带示例说明的内容没有详细考究，给出了错误的介绍，为了不造成更多的误导已将该文删除现修改后半部分。希望看完该篇文章内容的朋友重新查看这篇内容，以免形成错误认知。同时也在这里给大家道歉，还希望后续的文章中若有发现错误的内容大家能够积极提出质疑，我们一起交流，共同改进。`文章中主要错误描述是：标准库和HAL中对GPIO等大多数外设的处理是对直接寄存器操作方式的封装，涉及到的更多的是位操作，而不是使用位带操作，此文会将正确的做法列出。当然两种官方库中对位带操作都有应用，只是官方应用的范围比较少，如果想在一般外设中使用还是需要自己添加一些代码去实现。`

## 让STM32像51一样编程
在以前的文章中我都提到过很多次，单片机控制程序实质上大部分都是在操作寄存器。
举例一段51代码：
```c
void main()
{
	for(;;)
	{
		P1^0 = 0;
		delay(300);
		P1^0 = 1;
		delay(300);
	}
}
```
在51单片机程序中我们都是直接通过寄存器的设置来实现代码功能，并且使用位操作运算符非常容易的就可以实现各种寄存器设置操作，想设置功能也是非常直接，再比如`EA = 1;`设置总中断使能。因为51单片机的内存地址和寄存器都差不多数得过来，并且寄存器都是8位的，所以编程时对于这点数量的位运算可以说是“指哪打哪”。

现在再一起来回顾一下主要的位运算符：

- '|' :位或运算符,可以设置寄存器的某几位

- '&' :位与运算符,可以清除寄存器的某几位

- '^' :位异或运算符,可以翻转寄存器的某几位

- '<<':左移运算符,可以访问某个位位置

- '>>':右移运算符,可以访问某个位位置

![51单片机寄存器地址定义](https://files.mdnice.com/user/38598/312c3d33-7d15-41a3-bb78-6a5479653035.png)

![51单片机寄存器位定义](https://files.mdnice.com/user/38598/660e4dab-7dd2-4c37-b15f-07afb6fcb3ad.png)

虽然单片机的位操作很方便了，但当单片机外设，寄存器数量及位数很大的时候，使用位运算进行编程时还是需要仔细推倒一下逻辑关系，不然还是很容易出错的。对于STM32，它内部的寄存器和内存空间都很多，并且寄存器是32位的，编程时程序该怎么对应寄存器，内存地址才会比较方便呢？并且使用Cortex-M3内核制造芯片的厂家那么多，要怎么统一规划？arm公司就对这些情况进行了一些设置，这个问题就是通过我上一篇文章写的STM32单片机存储器映射解决的，没看的朋友可以点击链接跳转查看：[浅析STM32存储器映射](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486100&idx=1&sn=a177c25048f591ea29a489070361bb16&chksm=ea7902e5dd0e8bf3ecfa9bd88eee25b2f328d168f473a08467e9a806438c3de46cb23896fd17&token=1626842862&lang=zh_CN#rd)。

再贴一下Cortex-M3内核单片机存储器映射结构：

![Cortex-M3存储器映射](https://files.mdnice.com/user/38598/48a6bcd7-269f-48f2-baa4-5deb87a8c435.png)

在STM32中使用的方法就是:`Bit-band`,也就是通常说的`位带`操作。

STM32系列MCU具有强大的位带操作能力,通过对某地址字的读写操作实现对某bit的读写操作。这样做可以高效地像51单片机那样对单个或多个位进行读写或控制，从而简化了直接寄存器操作时的“读-改-写”这一个过程。

## 位带操作的底层原理
单片机支持位带操作后，就可以使用普通的加载/存储指令来对单一的比特进行读写。在 Cortex-M3内核中，有两个区中实现了位带。其中一个是 SRAM 区的最低1MB范围，第二个则是片内外设区的最低1MB范围。这两个区中的地址除了可以像普通的RAM一样使用外，它们还都有自己的“位带别名区”，位带别名区把每个比特膨胀成一个32位的字，简单的说就是，这些bit-band区域将存储器别名区的一个字映射为bit-band区的一个位。就如你的本名叫张三，别人叫你三崽同一个道理，你听到后就知道都是在叫你。当你通过位带别名区访问这些字时，就可以达到访问原始bit位的目的。

其中内容具体对应关系如下：
- 对 32MB SRAM 别名区的访问映射为对1MB SRAMbit-band 区的访问。
- 对 32MB 外设别名区的访问映射为对1MB 外设bit-band 区的访问。

位带区与位带别名区的地址的通用映射计算公式如下：
```c
bit_word_offset = (byte_offset×32) + (bit_number×4)

bit_word_addr = bit_band_base + bit_word_offset
```
- Bit_word_offset 为bit-band 存储区中的目标位的位置。
- Bit_word_addr 为别名存储区中映射为目标位的字的地址。
- Bit_band_base 是别名区的开始地址。
- Bit_offset 为bit-band 区中包含目标位的字节的编号。
- Bit_number 为目标位的位位置（0-7）。

具体到SRAM区某字节地址为A的第n bit其位带别名区地址计算公式如下：
```c
AliasAddr=0x22000000+((A-0x20000000)*8+n)*4 =0x22000000+(A-0x20000000)*32+n*4
```
外设区某字节地址为A的第n bit其位带别名区地址计算公式如下：
```c
AliasAddr=0x42000000+((A-0x40000000)*8+n)*4 =0x42000000+(A-0x40000000)*32+n*4
```

![位带储存区地址对应图示](https://files.mdnice.com/user/38598/4b57b42b-51d4-4770-806a-32745dc7832a.png)

**位带别名区的字只有最低位（LSB）有效，即对该字进行写1或写零就是对其对应的位带区所在的bit位进行置位或清零，这样就实现了类似51中EA = 0这种操作了，而不用先读取该寄存器所有值，再进行对其中某一位处理，最后再进行寄存器整体赋值。如果用过STM8或16位机，或者cortex-M0系列等功能相对复杂却没位带操作的芯片的朋友应该能过感受这种复杂的操作**

## 代码中实现位带操作
我们编程时要实现位带操作可以将一些常用外设位带区与位带别名区，当然通常情况下都是对GPIO的使用，所以代码量也不会太大。并且一般情况下这些代码也不用我们自己去实现一遍，如果你有购买某些开发板学习那在开发板配套的资料里都会有涉及，如果你没使用过开发板那可以在原子，野火等官网下载相关资料获取，在项目中使用时可以直接调用该文件。当然你也可以根据自己的需求定义一些适合你自己使用的内容。

比如定义一个这样的头文件：
```c
#ifndef __SYS_H
#define __SYS_H

#include <main.h>

#define BITBAND(addr, bitnum) ((addr & 0xF0000000)+0x2000000+((addr &0xFFFFF)<<5)+(bitnum<<2)) 
#define MEM_ADDR(addr)  *((volatile unsigned long  *)(addr)) 
#define BIT_ADDR(addr, bitnum)   MEM_ADDR(BITBAND(addr, bitnum)) 
#define bit_read_write(data, bit) BIT_ADDR((unsigned long)(&data), bit)

#ifdef USE_STM32F1xx	

#define PA_L8_MODE(n)   BIT_ADDR(&(GPIOA->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PB_L8_MODE(n)   BIT_ADDR(&(GPIOB->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PC_L8_MODE(n)   BIT_ADDR(&(GPIOC->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PD_L8_MODE(n)   BIT_ADDR(&(GPIOD->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PE_L8_MODE(n)   BIT_ADDR(&(GPIOE->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PF_L8_MODE(n)   BIT_ADDR(&(GPIOF->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PH_L8_MODE(n)   BIT_ADDR(&(GPIOH->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PI_L8_MODE(n)   BIT_ADDR(&(GPIOI->CRL),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 

#define PA_H8_MODE(n)   BIT_ADDR(&(GPIOA->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PB_H8_MODE(n)   BIT_ADDR(&(GPIOB->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PC_H8_MODE(n)   BIT_ADDR(&(GPIOC->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PD_H8_MODE(n)   BIT_ADDR(&(GPIOD->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PE_H8_MODE(n)   BIT_ADDR(&(GPIOE->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PF_H8_MODE(n)   BIT_ADDR(&(GPIOF->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PH_H8_MODE(n)   BIT_ADDR(&(GPIOH->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PI_H8_MODE(n)   BIT_ADDR(&(GPIOI->CRH),n*4)  //1:OUTPUT MODE;0:INTPUT MODE 

#elif USE_STM32F4xx

#define PAMODE(n)   BIT_ADDR(&(GPIOA->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PBMODE(n)   BIT_ADDR(&(GPIOB->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PCMODE(n)   BIT_ADDR(&(GPIOC->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PDMODE(n)   BIT_ADDR(&(GPIOD->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PEMODE(n)   BIT_ADDR(&(GPIOE->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PFMODE(n)   BIT_ADDR(&(GPIOF->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PHMODE(n)   BIT_ADDR(&(GPIOH->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 
#define PIMODE(n)   BIT_ADDR(&(GPIOI->MODER),n*2)  //1:OUTPUT MODE;0:INTPUT MODE 

#endif
/**
 * [PAout description]
 * @param  n [0-15]
 * @return   [none]
 * EG:  PAout(1) = 1;//set PA1 to HIGH
 * 		PAout(1) = 0;//set PA1 to LOW
 */
#define PAout(n)   BIT_ADDR(&(GPIOA->ODR),n)  //OUTPUT 
#define PBout(n)   BIT_ADDR(&(GPIOB->ODR),n)  //OUTPUT 
#define PCout(n)   BIT_ADDR(&(GPIOC->ODR),n)  //OUTPUT 
#define PDout(n)   BIT_ADDR(&(GPIOD->ODR),n)  //OUTPUT 
#define PEout(n)   BIT_ADDR(&(GPIOE->ODR),n)  //OUTPUT 
#define PFout(n)   BIT_ADDR(&(GPIOF->ODR),n)  //OUTPUT 
#define PGout(n)   BIT_ADDR(&(GPIOG->ODR),n)  //OUTPUT 
#define PHout(n)   BIT_ADDR(&(GPIOH->ODR),n)  //OUTPUT 
#define PIout(n)   BIT_ADDR(&(GPIOI->ODR),n)  //OUTPUT

/**
 * [PAin description]
 * @param  n [0-15]
 * @return   [none]
 * EG:  a = PAin(1);//get PA1 bit to value a
 */
#define PAin(n)    BIT_ADDR(&(GPIOA->IDR),n)  //输入 
#define PBin(n)    BIT_ADDR(&(GPIOB->IDR),n)  //输入 
#define PCin(n)    BIT_ADDR(&(GPIOC->IDR),n)  //输入 
#define PDin(n)    BIT_ADDR(&(GPIOD->IDR),n)  //输入 
#define PEin(n)    BIT_ADDR(&(GPIOE->IDR),n)  //输入
#define PFin(n)    BIT_ADDR(&(GPIOF->IDR),n)  //输入
#define PGin(n)    BIT_ADDR(&(GPIOG->IDR),n)  //输入
#define PHin(n)    BIT_ADDR(&(GPIOH->IDR),n)  //输入
#define PIin(n)    BIT_ADDR(&(GPIOI->IDR),n)  //输入


#define HIGH 0x1
#define LOW  0x0

#define PI 3.1415926535897932384626433832795
#define HALF_PI 1.5707963267948966192313216916398
#define TWO_PI 6.283185307179586476925286766559
#define DEG_TO_RAD 0.017453292519943295769236907684886
#define RAD_TO_DEG 57.295779513082320876798154814105
#define EULER 2.718281828459045235360287471352

//#define SERIAL  0x0
#define DISPLAY 0x1

#define LSBFIRST 0
#define MSBFIRST 1

#define CHANGE 1
#define FALLING 2
#define RISING 3


#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
// #define abs(x) ((x)>0?(x):-(x))
#define constrain(amt,low,high) ((amt)<=(low)?(low):((amt)>(high)?(high):(amt)))
#define round(x)     ((x)>=0?(long)((x)+0.5):(long)((x)-0.5))
#define radians(deg) ((deg)*DEG_TO_RAD)
#define degrees(rad) ((rad)*RAD_TO_DEG)
#define sq(x) ((x)*(x))

#define low8Byte(w) ((uint8_t) ((w) & 0xff))
#define high8Byte(w) ((uint8_t) ((w) >> 8))

#define bitRead(value, bit) (((value) >> (bit)) & 0x01)
#define bitSet(value, bit) ((value) |= (1UL << (bit)))
#define bitClear(value, bit) ((value) &= ~(1UL << (bit)))
#define bitWrite(value, bit, bitvalue) (bitvalue ? bitSet(value, bit) : bitClear(value, bit))
#define bitToggle(value, bit) bitWrite(value, bit, !bitRead(value, bit))

#define swap(a, b) { uint32_t t = a; a = b; b = t; }
#define bit(b) (1UL << (b))


#define map(x, in_min, in_max, out_min, out_max) \
  ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#define cycle_increase(a, b) a=(a+1)%(b)

/* 向上取整 */
#define CEIL_DIV(a, b) (((a)+(b)-1)/(b))

#endif

```

将以上头文件添加到工程中后我们代码中就可以使用如
`PAout(0) 
PAin(1) 
`
这样简洁的代码实现对单片机端口的控制。

如果平时喜欢使用寄存器操作的编程方式就可以将更多外设对应的操作定义列举出来。如果使用官方标准库或HAL库，也可以在工程中混合使用。如果你在编程时不想要现成的，或者想和库函数实现代码保持一致，那标准库和HAL库中也给出了一些使用的例子可以作为参考。

可以参考的标准库位带功能使用案例：
![标准库中对位带别名区基地址的定义](https://files.mdnice.com/user/38598/a0c3e65e-791c-4a6f-8f46-2178803da8e1.png)

![标准库中对特定外设的别名区地址定义](https://files.mdnice.com/user/38598/81a8c9d8-7dca-430e-9e85-09dbf529bfcc.png)

![标准库中特定位带功能实现函数](https://files.mdnice.com/user/38598/48d91759-0c80-4d18-92ae-85866421a162.png)

相关使用方式在HAL也差不多类似的：

![HAL中同样的不别名区基地址定义](https://files.mdnice.com/user/38598/9e62d4e7-d0b3-4e61-8ea3-9d5a9821a26f.png)

![HAL库中对一些特定外设的别名区地址定义](https://files.mdnice.com/user/38598/9a56b85f-c942-40a4-b766-25110784d5a0.png)

![HAL库中一些特定位带功能实现函数](https://files.mdnice.com/user/38598/6460138b-d6d2-4228-81dd-c6380e0a5dd4.png)

从这些代码中我们可以很容易看出来，使用位带功能编程一旦你将基础的功能定义好了，在实现操作时都可以用等式定义就能达到目的，在一些特定场景下使用位带操作还是很方便。不管你平时使用哪种库或者直接寄存器的方法都可以与之相互结合使用，互不冲突。

## 总结
位带操作是STM32编程中非常重要的一种技术,可以对MCU的IO口、外设状态位进行高效的访问。平时编程的过程中根据应用的复杂程度和资源情况,适当使用位带操作可以充分发挥STM32的性能优势,编写出高效可靠的应用程序。

----
>>>文章内容为作者个人观点，难免有疏忽或错误，若有不同见解可以交流评论，若发现错误还请指正，若认同文章观点，欢迎关注，分享。

>>>如学习需要或技术合作可以扫码添加微信。
建有交流群，以方便大家平时交流、学习，如果要进群，加好友时记得备注信息`进群`。
![](https://files.mdnice.com/user/38598/6fbcd253-edc6-4175-ba0c-44e24ad33b21.jpg)


占位

`温馨提示：若需要获取分享的资料，进入公众号后台发送关键字内容即可自动获取，而不是在留言或个人微信聊天界面发送！！！`

#### 推荐阅读
- [怎么快速上手一款新的MCU](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485581&idx=1&sn=b36e6536717774f7931c7aa93d5b237a&chksm=ea7900fcdd0e89ea0db13737720edc996fcb3fdbab3e43b4a92316240ac66d4b5a8bf9a07e78&token=466212876&lang=zh_CN#rd)
- [初学者看得懂代码却写不出怎么办](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485862&idx=1&sn=830ede5ac467c8d396adfbea141f0526&chksm=ea7901d7dd0e88c1e8e5396305ab83c6fbd884cf356ad64c54463230364e865a1659f193dd1f&token=63320980&lang=zh_CN#rd)
- [51单片机入门看这一篇就够了](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485523&idx=1&sn=b7fcd1b86e2467d6f03b1a520c39bb06&chksm=ea790022dd0e893452c4994fa16d63111b16d9878c303712f695b58b7af360b7b18c1ed4b201&token=1711068967&lang=zh_CN#rd)
- [实用单片机、电子开发小工具集](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485606&idx=1&sn=2b433faa2e436fc762dc538c9cf3fe14&chksm=ea7900d7dd0e89c169f8948ff3d423016c8f51f1c914eb7b0d20cba8145b9ffa54815915d67b&token=1580674001&lang=zh_CN#rd)
- [Keil软件如何高效格式化代码](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485572&idx=1&sn=17cefa35d9d660083d419a7e9b6db6f7&chksm=ea7900f5dd0e89e35b65ba26354cc69ad24f686d8e18abd34e0932567a9345e8c9ed653eee6b&token=1711068967&lang=zh_CN#rd)
- [两个电子开发初学者用得上的工具](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485987&idx=1&sn=106e52add61999ae4bddd8b28c7ed2b1&chksm=ea790252dd0e8b44e36e26f20153b1bd73a0fff98ef3c50330358435a9dfac2d97e04a30d59e&token=63320980&lang=zh_CN#rd)
- [windows平台上非常实用的小工具](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485420&idx=2&sn=728ca4abbadf7caf51c392e7d7045cbe&chksm=ea790f9ddd0e868b9fa162c80db1876199845f387bbe851c8d38a4e8412329ae635916c13cfb&token=1711068967&lang=zh_CN#rd)
- [51单片机入门学习推荐书单](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485689&idx=3&sn=d4c0d26781f307ffd26defdc4022c928&chksm=ea790088dd0e899e2872692b9568309e779acfc515e82c28a853d4228de2e2b8f7ee7149913f&token=63320980&lang=zh_CN#rd)
- [零基础电子技术知识集合](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485689&idx=4&sn=211c2d0871a19c5e92cdf0c34f01d96b&chksm=ea790088dd0e899e3042a649a346bc98e94189d1fd18da2b954a7ddb781582dc2d0a82e07f4d&token=970763775&lang=zh_CN#rd)
----
