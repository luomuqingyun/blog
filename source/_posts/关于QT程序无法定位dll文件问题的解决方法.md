---
title: 关于QT程序无法定位dll文件问题问题解决方法
author: luomuqingyun
comments: true
category:
  - 编程
  - 经验
tags:
  - 编程经验
excerpt:
  - bug调试记录
categories: []
date: 2025-05-19 14:51:09
---
## 引言
`本文主要介绍运行使用QT编译好的程序报无法定位动态链接库错误的几种常用解决方案，以及本次特殊遇到的libpng16-16.dll中调用inflateReset2函数引发的问题解决思路。希望能够帮助遇到类似问题的朋友。`

## QT程序报错无法定位*.dll

QT是作为一个夸平台的图形界开发工具，由于其具有开源和友好的用户操作界面，相对于其他一些跨平台图形开发工具来说更容易使用，所以他成为了Windows端跨平台开发的得力工具。当然它的更新速度也比较快，这就造成了我们日常开发过程中可能不得不安装多个版本的qmake来适应不同需求的问题。如果的是在Windows系统下开发，涉及到msvc与gcc两种编译器问题可能就更甚了，并且在Windows系统和开发软件完美的封装让我们省去了搭建编译环境的过程，可以傻瓜式的使用，有时对于自己使用的动态库及其所依赖库是否存在以及其版本是否匹配也没有明显的提示，然后项目编译可能没问题，但运行时会因匹配不到库而出错。如下：

![运行QT编译的程序报错](https://files.mdnice.com/user/38598/c92955e7-feb1-4bf9-a7ac-d971af6d0699.png)
```
---------------------------
xx.exe - 无法找到入口
---------------------------
无法定位程序输入点 inflateReset2 于动态链接库 
xx\libpng16-16.dll 上。 
---------------------------
确定   
---------------------------
```
## 常规解决办法

这种错误提示想必对于刚开始使用QT开发的朋友来说应该不陌生。网上也有很多解决方案了。如果已安装对应版本的*.dll，这时一般通过修改Path环境变量，调整一下QT版本路径顺序或复制动态链接库到程序所在路径基本可以解决问题。如果是系统中缺失对应的*.dll也可以通过下载，安装该库来实现（如果没有现成的则可以自行下载源码编译后复制该库）。

## 非常解决方法

我这次遇到libpng16-16.dll调用inflateReset2函数这个错误，所编译的程序我在其他电脑上运行是没问题的，我想应该也是动态库版本问题造成的。所以，自然而然就想着通过修改PATH路径顺序来解决，然而这次并没起作用。通过查询系统上存在的libpng16-16.dll，是存在有几个不同的版本：

![我系统中的libpng16-16.dll](https://files.mdnice.com/user/38598/3e451ff6-cd9b-47a4-a0b4-89ee7aa853f3.png)

但经确认，我电脑系统环境里面只有目前使用的一个libpng16-16.dll：

![系统环境下的libpng16-16.dll](https://files.mdnice.com/user/38598/166fa56e-241e-4b50-9671-bb3a47b1e23d.png)

这就有点不应该了，但直觉告诉我这次的问题应该不在于libpng16-16.dll本身上，应该是与它相关联的动态库出问题了。遇到这种情况最直接的方法是在源码中查找答案。所以在libpng源码中找出了所有关于inflateReset2的描述：

![libpng源码中关于inflateReset2的使用及描述](https://files.mdnice.com/user/38598/caa84047-2018-457c-a7bf-5ba9985351eb.png)

这个函数确实是它调用的其他库函数，从注释描述中可以确认是zlib库，关于代码内容现在不是我们需要特意去关注的，所以要解决问题我们需要找出zlib相关的问题。所以又在libpng源码Issues中找到了一些其他的蛛丝马迹，[参考资料1(链接见文后)：libpng Make Failed #173](https://github.com/pnggroup/libpng/issues/173)，查看对应的解决方案也提到了zlib.dll的问题。然后，顺藤摸瓜又在msys2源码仓库的Issues下找到的了类似问题，[参考资料2：libpng16 throwing entry point inflateReset2 could not be located #813](https://github.com/msys2/MINGW-packages/issues/813)，可以确认是zlib1.dll这个库引发的问题（在Windows系统上zlib.dll是zlib1.dll的旧版）。所以接下的问题就是调整电脑中zlib1.dll的路径顺序。

![命令行查询系统环境变量下zlib1.dll路径](https://files.mdnice.com/user/38598/45e28e07-9764-432d-ad38-4be739d6b0a9.png)

但通过命令行查询后，目前使用的zlib1.dll库早已经确定是在系统环境变量的最优先位置了，默认调用也确实是它了：

![系统默认调用zlib1.dll文件](https://files.mdnice.com/user/38598/a983f34f-6688-44ba-bc7c-fe3fea454ac7.png)

按理程序应该完全能够跑得起来了。但问题还一直存在，真是让人脑壳大，催人掉头发呀，没办法。于是又尝试把所有zlib1.dll文件都找出查看是否有其他干扰的可能，发现文件虽多但还是都不影响所在工程的执行调用：

![查询系统中的zlib1.dll](https://files.mdnice.com/user/38598/39e8ada3-37db-4bd4-ac4c-72c7d9adbb72.png)

所以最后只能对环境变量中列出的另外3个逐一进行路径排除。经过最后的折腾，最终发现是`C:\Windows\System32`目录下的zlib1.dll引发的问题，由于不能将该目录在环境变量中删除所以保守的办法就是将该zlib1.dll文件备份后删除。问题是解决了，但需要思考的是在Win11系统下`C:\Windows\System32`系统路径之下的可执行文件或库文件是否具有全局优先权？

![命令行确认修改后的zlib1.dll](https://files.mdnice.com/user/38598/005d3dbd-6b27-42f5-b58a-66490fa5cf3f.png)

----

占位

>>>文章内容为作者个人观点，难免有疏忽或错误，若有不同见解可以交流评论，若发现错误还请指正，若认同文章观点，欢迎关注，分享。

>>如学习需要或项目开发合作可以扫码添加微信。
>>![](https://files.mdnice.com/user/38598/6fbcd253-edc6-4175-ba0c-44e24ad33b21.jpg)
>>
>>有电子开发交流群，供平时交流、学习，如果要进群，加好友时记得备注信息`进群`，未备注则默认不邀请进群。
>>

`温馨提示：部分文章中附有分享文件，若需要获取，进入公众号后台发送文提示的关键词，即可自动获取。不要在文章留言区或微信聊天时发送关键词,望悉知！！！`

#### 推荐阅读
- [PID算法基础汇总](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486549&idx=1&sn=aa7a3ea1c22bd5b797986314e4aa0e2c&chksm=ea790424dd0e8d32da20a9219be731e7691ce1711f2e6b42fc144e3586fe53ff41c3070df904&token=241279816&lang=zh_CN#rd)
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
