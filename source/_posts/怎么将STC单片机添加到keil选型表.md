---
title: 怎么将STC单片机添加到keil选型表
date: 2025-05-19 14:42:00
author: luomuqingyun
comments: true
category:
  - 编程
tags:
  - 编程经验
excerpt:
  - 详见完整内容
---
## 使用keil新建工程时怎么没有STC芯片型号
对于很多初学者来说，刚开始接触51单片机时可能是使用proteus等仿真软件进行仿真学习的，在建立keil工程时也是选用课本上对应的51单片机型号进行编程。
而等到自己实际买回单片机开发板回来练习时可能发现板子上使用的芯片是STC89C5x的芯片，这是部分初学者可能会心慌，怎么信号表里都没有找到这个芯片呢？其实这是你完全可以选用其他厂家对应的C5x单片机的，至于芯片的一些额外差异（比如ram,rom等差异）可以在工程或程序中进行一些其他的设置即可。万一下次使用的是STC12X或STC15X型号的芯片呢，不知道选什么型号，又该怎么办？其实更好的办法是把STC的芯片型号添加到keil软件中去。其实STC官方是提供工具和方法给我们了，只是在他们官网上，一般初学者可能没注意到。
下载STC官方工具stc-isp，除了下载程序之外，这个工具现在功能还是挺多的，比如串口助手等等，平时使用可以自己研究使用。
下面直接上图：
打开软件在菜单栏找到`keil仿真设置`菜单，点击`添加xxx`框即可。

![设置](https://files.mdnice.com/user/38598/b487784d-14bf-401c-8efa-8cf042f476ff.png)

在接下的地址选择框中找到你keil安装的路径点击`确认`即可。

![选择keil安装目录](https://files.mdnice.com/user/38598/20e939a5-f46f-4a8a-a005-bbc02e79cbae.png)

设置完就可在keil中进行选择了。

![keil选项界面](https://files.mdnice.com/user/38598/a17f946f-6f58-47d2-afc4-0c6ac532c696.png)


#### 推荐阅读
- [51单片机入门看这一篇就够了](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485523&idx=1&sn=b7fcd1b86e2467d6f03b1a520c39bb06&chksm=ea790022dd0e893452c4994fa16d63111b16d9878c303712f695b58b7af360b7b18c1ed4b201&token=1711068967&lang=zh_CN#rd)
- [怎么快速上手一款新的MCU](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485581&idx=1&sn=b36e6536717774f7931c7aa93d5b237a&chksm=ea7900fcdd0e89ea0db13737720edc996fcb3fdbab3e43b4a92316240ac66d4b5a8bf9a07e78&token=466212876&lang=zh_CN#rd)
- [Keil软件如何高效格式化代码](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485572&idx=1&sn=17cefa35d9d660083d419a7e9b6db6f7&chksm=ea7900f5dd0e89e35b65ba26354cc69ad24f686d8e18abd34e0932567a9345e8c9ed653eee6b&token=1711068967&lang=zh_CN#rd)
- [分享几个windows平台上非常实用的工具](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485420&idx=2&sn=728ca4abbadf7caf51c392e7d7045cbe&chksm=ea790f9ddd0e868b9fa162c80db1876199845f387bbe851c8d38a4e8412329ae635916c13cfb&token=1711068967&lang=zh_CN#rd)
- [实用单片机、电子开发小工具集](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485606&idx=1&sn=2b433faa2e436fc762dc538c9cf3fe14&chksm=ea7900d7dd0e89c169f8948ff3d423016c8f51f1c914eb7b0d20cba8145b9ffa54815915d67b&token=1580674001&lang=zh_CN#rd)
- [零基础电子技术知识集合](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485689&idx=4&sn=211c2d0871a19c5e92cdf0c34f01d96b&chksm=ea790088dd0e899e3042a649a346bc98e94189d1fd18da2b954a7ddb781582dc2d0a82e07f4d&token=970763775&lang=zh_CN#rd)
----

![欢迎添加作者微信，加入交流群](https://files.mdnice.com/user/38598/37e7b97e-a5c7-44d1-9e48-bbe22ab3141d.jpg)

----
