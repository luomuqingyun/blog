---
title: python程序运行莫名警告
author: luomuqingyun
comments: true
category:
  - 编程
  - 经验
tags:
  - 编程经验
excerpt:
  - BUG调试记录
date: 2025-05-19 14:42:00
---
占位
## 记一个python程序调试警告
虽然我的主业是电子开发，平时主要用的开发语言是`C/C++`，但由于工作的原因，也会用到其他一些开发语言，所以`python`和`js`都能使用得上。昨天晚上发布的介绍卡尔曼滤波算法的文章因为没有图片说明最后想说的也没法描述，只能草草收场。因为后续还会介绍其他算法问题，肯定都是需要做图说明的，但每一个如果都要做图的话确实比较浪费时间，所以今天空闲时就想着得找个办法把这个问题解决。后面想着用`python`写一个图形生产代码。但在测试出现了一些小警告，所以在这里顺便做个记录方便以后查阅。
警告内容如下：
```
(process:18144): GLib-GIO-WARNING **: 21:51:05.639: Unexpectedly, UWP app `Clipchamp.Clipchamp_2.5.5.0_neutral__yxz26nhyzhsrt' (AUMId `Clipchamp.Clipchamp_yxz26nhyzhsrt!App') supports 41 extensions but has no verbs

(process:18144): GLib-GIO-WARNING **: 21:51:05.683: Unexpectedly, UWP app `microsoft.windowscommunicationsapps_16005.14326.20970.0_x64__8wekyb3d8bbwe' (AUMId `microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail') supports 1 extensions but has no verbs
[21:51:25] INFO     Tips: You are now in the interactive mode. Now you can use the keyboard and the mouse to interact with the scene. 

```
查阅资料发现与`GLib`有关，这是一个跨语言的底层UI图形库，一些比较流行的桌面图形界面都是基于它开发的，比如：`GTK `,`GNOME`等等。字面意思应该是python代码中调用的模块使用到了GLib，并且问题与`GLib-GIO`相关，看了源代码这是GLib的输入，输出功能模块，里面内容太多，并且警告提示也没法定位，确实是让人头大。好在不影响程序功能，但是强迫犯了不得不把它解决。在网上找了相关资料也没有合适的解决办法。
参考了官方代码交流反馈区（https://gitlab.gnome.org/GNOME/glib/-/issues/2640）也没好滴解决办法，可能是软件之间相互影响造成的。

找到一个参考的解决方案是以管理员权限运行命令行输入：`Get-AppXPackage ****.***** -allusers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`，其中`****.*****`替换成自己的问题点`Clipchamp.Clipchamp_2.5.5.0_neutral__yxz26nhyzhsrt`，`microsoft.windowscommunicationsapps_16005.14326.20970.0_x64__8wekyb3d8bbwe`，然而测试结果是并没解决我的问题。

看着问题很无赖，但又不甘心，虽然不影响功能，但还是看着膈应，所以最后又把问题聚焦到了`Clipchamp`上，看打出来是一个系统软件，查证发现是系统自带的视频编辑软件，估计是底层有相互影响了，因为平时也不使用，所以抱着试一试的想法，我把它卸载了，结果奇迹就在这时出现了，一个警告消失，看来确实是个好办法。尝试解决第二个，按提示找到文件位置，结果删不掉，是系统内置文件，也不想暴力，万一暴力之后系统崩溃，那就完蛋了，看来又有点麻烦了，后面想想最后结尾是`mail`那应该是和邮箱有关，平时虽然有有到邮箱，但如果能解决问题那用网页版也OK，所有又把邮箱给卸载了，好果真，奇迹又一次发生。到此警告接触，可以继续往下写功能了。

- [51单片机入门看这一篇就够了](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485523&idx=1&sn=b7fcd1b86e2467d6f03b1a520c39bb06&chksm=ea790022dd0e893452c4994fa16d63111b16d9878c303712f695b58b7af360b7b18c1ed4b201&token=1711068967&lang=zh_CN#rd)
- [怎么快速上手一款新的MCU](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485581&idx=1&sn=b36e6536717774f7931c7aa93d5b237a&chksm=ea7900fcdd0e89ea0db13737720edc996fcb3fdbab3e43b4a92316240ac66d4b5a8bf9a07e78&token=466212876&lang=zh_CN#rd)
- [Keil软件如何高效格式化代码](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485572&idx=1&sn=17cefa35d9d660083d419a7e9b6db6f7&chksm=ea7900f5dd0e89e35b65ba26354cc69ad24f686d8e18abd34e0932567a9345e8c9ed653eee6b&token=1711068967&lang=zh_CN#rd)
- [分享几个windows平台上非常实用的工具](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485420&idx=2&sn=728ca4abbadf7caf51c392e7d7045cbe&chksm=ea790f9ddd0e868b9fa162c80db1876199845f387bbe851c8d38a4e8412329ae635916c13cfb&token=1711068967&lang=zh_CN#rd)
- [实用单片机、电子开发小工具集](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485606&idx=1&sn=2b433faa2e436fc762dc538c9cf3fe14&chksm=ea7900d7dd0e89c169f8948ff3d423016c8f51f1c914eb7b0d20cba8145b9ffa54815915d67b&token=1580674001&lang=zh_CN#rd)
- [零基础电子技术知识集合](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485689&idx=4&sn=211c2d0871a19c5e92cdf0c34f01d96b&chksm=ea790088dd0e899e3042a649a346bc98e94189d1fd18da2b954a7ddb781582dc2d0a82e07f4d&token=970763775&lang=zh_CN#rd)
----

![欢迎添加作者微信，加入交流群](https://files.mdnice.com/user/38598/37e7b97e-a5c7-44d1-9e48-bbe22ab3141d.jpg)

----


