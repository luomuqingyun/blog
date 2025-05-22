---
title: 关于TI官网注册和网页版Filter Pro使用的问题
author: luomuqingyun
comments: true
category:
  - 工具
tags:
  - 开发工具
excerpt:
  - Filter Pro软件说明
date: 2025-05-19 14:42:00
---
占位
## 关于Filter Pro软件电路参数问题
前段时间小破站上有留言说TI的滤波器电路设计软件`Filter Pro`使用时出问题，设计参数与`TI-TINA`的仿真相差很大。但我在自己电脑上设计了一个简单电路，软件生成的电路参数与计算结果是没问题的。因为电脑上没安装TI-TINA了，也没看到他的实际电路和TI-TINA软件设置情况，所以也不知道那位朋友具体是哪里出了意外。我个人猜测如果是软件问题的话可能因为当前的Filter Pro软件包是十多年前的版本了（TI公司推出网页版之后就没怎么更新安装软件了），软件设置的某些参数的是当时的芯片参数，而网友的仿真电路中的芯片参数已经更新很多版本了。综上原因如果需要进行电路设计不妨可以试试网页版工具。
## 关于TI官网注册问题
TI网页版的滤波器电路设计工具在TI官网的设计资源库中，名称为`Filter designer`,里面还有许多TI官方的其他支持应用软件，各位空闲的时候可以按需尝试。但是TI官网的所有工具都是需要登录才能使用。前面那位网友反馈注册不了TI官网账号，他当时怀疑是否是因为某些原因TI官方对国内用户的支持做了相关限制，我当时也觉得可能有一定的关联，但TI在国内业务那么广应该不会这么折腾自己吧？后面我本着求真原则重新注册了一个新的账号，我当时是在谷歌浏览器上操作的，一路信息填下去也没遇到网友所说的注册不了的情况。所以TI官方应该没有限制国内用户使用的权限，不过注册时其官网时推荐使用企业邮箱进行注册的，这大概率和他们的业务推广有关，可能也是为了更直接的提供技术支持服务吧，总之，你使用有效的个人邮箱注册都是可以的。当然一般国外网站因为主服务器不在国内的原因我们访问速度会相对慢一点，网站也可能没那么稳定，一般遇到这种情况建议使用无痕窗口进行操作。

![网友留言信息](https://files.mdnice.com/user/38598/46c37866-acfe-4744-85bb-337da97a1ceb.png)

今天又收到另一位网友在后面留言说他怎么都注册不上，希望我做一个注册视频，我当时是非常疑惑的，是真的注册不了了，难道TI真的搞事情了？或许还有很多经验不多的网友会也遇到类似问题，正好就再注册一个账号验证一下，再加上很久没更新小破站的视频内容了，都快被平台埋了，所以就想着录一个注册全过程的的视频，供大家参考。

为了确定是否与浏览器相关我这次特意使用国内应用比较广的微软Edge浏览器进行操作。最终验证结果是注册没问题，同时为了验证在无痕模式下进行操作更稳定，我这一次性注册了2个账号。所以到目前为止我就有了4个账号~

![一堆尴尬的账号](https://files.mdnice.com/user/38598/ca6b9431-0605-46f0-b773-f289277d1641.png)

## 完整注册视频
下面是完整视频，需要的朋友可以查看：

占位

#### 推荐阅读
- [51单片机入门看这一篇就够了](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485523&idx=1&sn=b7fcd1b86e2467d6f03b1a520c39bb06&chksm=ea790022dd0e893452c4994fa16d63111b16d9878c303712f695b58b7af360b7b18c1ed4b201&token=1711068967&lang=zh_CN#rd)
- [怎么快速上手一款新的MCU](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485581&idx=1&sn=b36e6536717774f7931c7aa93d5b237a&chksm=ea7900fcdd0e89ea0db13737720edc996fcb3fdbab3e43b4a92316240ac66d4b5a8bf9a07e78&token=466212876&lang=zh_CN#rd)
- [Keil软件如何高效格式化代码](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485572&idx=1&sn=17cefa35d9d660083d419a7e9b6db6f7&chksm=ea7900f5dd0e89e35b65ba26354cc69ad24f686d8e18abd34e0932567a9345e8c9ed653eee6b&token=1711068967&lang=zh_CN#rd)
- [分享几个windows平台上非常实用的工具](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485420&idx=2&sn=728ca4abbadf7caf51c392e7d7045cbe&chksm=ea790f9ddd0e868b9fa162c80db1876199845f387bbe851c8d38a4e8412329ae635916c13cfb&token=1711068967&lang=zh_CN#rd)
- [实用单片机、电子开发小工具集](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485606&idx=1&sn=2b433faa2e436fc762dc538c9cf3fe14&chksm=ea7900d7dd0e89c169f8948ff3d423016c8f51f1c914eb7b0d20cba8145b9ffa54815915d67b&token=1580674001&lang=zh_CN#rd)
- [滤波器设计软件FilterPro](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247484080&idx=1&sn=72ceac0e9c7a2601201431ca847c82f9&chksm=ea790ac1dd0e83d7630ec80d2e28acc9b99d88812d9bff7aa6b957a2352b2231d2bbf27e6d65&token=1854026269&lang=zh_CN#rd)
----
![欢迎添加作者微信](https://files.mdnice.com/user/38598/37e7b97e-a5c7-44d1-9e48-bbe22ab3141d.jpg)

----
