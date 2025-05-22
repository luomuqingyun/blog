---
title: PID算法基础汇总
author: luomuqingyun
comments: true
category:
  - 编程
  - 算法
tags:
  - 编程经验
  - 算法应用
excerpt:
  - PID算法
categories: []
date: 2025-05-19 14:42:00
---
## PID算法基础汇总

前段时间把PID算法的基础内容做了一些介绍，总的来说，PID算法原理是简单的，但具体应用绝对是复杂的，因为现实使用场景并不是理想的，线性的，它不可能像1+1这样的运算那么确定。大多数情况下都不是单纯的唯一解，并且它的结果还会受人的主观影响。比如同样的控制系统不同的人会调试出不同的参数组合。所以更多的知识还需要平时使用调试时做经验积累，想做更专业的应用更需要对调试的产品做更多知识储备，积累过程多参考相关专业书籍或应用案例。也是因为它通常没有绝对的标准结果，所以若是刚接触它也完全不要被它的概念吓唬了，按一定的规则放心去调试就好了。

PID算法已有百年历史之久，足以见得它在控制领域有着举足轻重的地位，国内外已有非常多的领域专家为它著书立作，不过在一些细分场景里国外可能有更多参考书籍，比如设计温控器，在国外书籍库中你或许可以找到一些专门针对温控器设计与应用的书籍，运气好的话还能找到和你想使用的控制器一样的设计案例。参考这些资料或许能发现一些可能出现在你设计过程中的坑他们早为你找到避开的方案了，相较而言国内的书籍如果涉及讲解温控设备更多可能只是在部分章节用较少的内容做一些概念性的介绍。并且由于这些应用书籍可能在国内受众比较少而没人愿意翻译，更别提电子文档，所以通常情况想要深入学习这些知识获取途径比较少，部分书籍在学校图书馆可能能够查找得到。另外，国外视频平台也有很多优秀视频可以学习，比如matlab官方发布的视频,现在他们在B站上也有中文账号，可以去了解一下，虽然他们B站的视频并没有那么多但内容是丰满的。这里也不是打给他们广告，只是单纯觉得他们做的挺好的（一个好的视频真的需要投入很多精力，并且在短视频泛滥的时代，形成的过眼即忘的“快餐式”学习方式，长视频内容创作更不易），有条件的朋友完全可以去学习更多的内容。

![](https://files.mdnice.com/user/38598/bb6a051d-c814-45dc-93c2-765a695315e8.png)

当然，现在国内的各种应用场景中也绝对不缺人才，有很多公开的大学课程也都很好，我们现在还缺的是时间的积累。毕竟过去国外发达国家的工业化进程比我们要早至少几十年，他们前期积累的大量内容我们也不可能一下就能消化。我们一直在追赶，没有时间给落队的人，这个过程浮躁也在所难免，所以很多时候都在负和博弈，或许再等十年，在新工业化发展逐渐成熟的进程中，在各项细分领域，国内应该也会有越来越多的可借鉴的经验和资料做参考。届时开发者在各自擅长的领域研究，有积才厚，把脚步放慢，我想未来的开发者也就肯定不用像现在那么卷了吧。

这篇文章主要是把前面一个系列的文章和资料做个汇总，方便需要的朋友统一查看。顺便再分享一些可参考借鉴的代码资料，老规矩需要资料的朋友在公众号后台回复关键字`231011A`获取网盘链接。

今后的文章将开始另一个主题系列，当然控制领域相关的文章也会在适当的时候继续更新，毕竟它是一个跨学科的，涉及面很广的领域，工业控制产品开发都可能用到。

- [PID算法（一）之原理解析](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486314&idx=1&sn=320c7d88c90604a8af80f472771246bb&chksm=ea79031bdd0e8a0d2b77c9450c39eb002805efb3c34bc44477feb56059b46f0dc71999cc8f73&token=2119834800&lang=zh_CN#rd)
- [PID算法（二）之位置与增量](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486361&idx=1&sn=632673e9fb92b49b3cfd8b52c6e483ea&chksm=ea7903e8dd0e8afeee8db64e97b44d5b7a72e1a1e775a70a70aa3a9e4ebee6d834257466ac04&token=2119834800&lang=zh_CN#rd)
- [PID算法（三）之串级控制](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486375&idx=1&sn=4c0d39a4f31b37fafef555235584e384&chksm=ea7903d6dd0e8ac0513d91640a9157466602dc7ebc3036aa97531b186b54b1edfeccaf6706d1&token=2119834800&lang=zh_CN#rd)
- [PID算法（四）之鲁棒性](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486383&idx=1&sn=a0bf54c7aa31041602b3f24ad418a3d3&chksm=ea7903dedd0e8ac81a79d9e491727a7298e11014fdba31b0b3e44e0739ef0ff7f965bfa02096&token=2119834800&lang=zh_CN#rd)
- [PID算法（五）之自抗扰](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486421&idx=1&sn=723513a1cebb3cf3310d8e2b6105930b&chksm=ea7903a4dd0e8ab24e1a98e20e6dd7365b01f473e3ffd80b1f63284dd8a66b484da34140ae74&token=2119834800&lang=zh_CN#rd)
- [PID算法（六）之模糊控制](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486434&idx=1&sn=db72c05c209b5696ca0990c7a7001ee9&chksm=ea790393dd0e8a85aca906b3aab95bab208df5b683440e3bdb232fe5aeb22c6567463110b426&token=2119834800&lang=zh_CN#rd)
- [PID算法（七）之自适应控制](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486451&idx=1&sn=2e20314ad6de5ae1836dcff428059036&chksm=ea790382dd0e8a94f943af6d1f9d9680ffa1dba3f9f5305b41eeac56cb279fb1655df080a18e&token=2119834800&lang=zh_CN&poc_token=HKVnJmWjkUt2yx4GZVc5AMOF9QXnAYQL5cF9pf31)
- [PID算法（八）之遗传算法](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486511&idx=1&sn=5c7582635b2490a698bc8467a4bc04b4&chksm=ea79045edd0e8d488e1d05be8df4dd873bba7e50212c21dad5b2080e156c7d61d3013f97b25a&token=2119834800&lang=zh_CN#rd)
- [几本实用的控制理论书籍](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486478&idx=1&sn=6bae6ef87e4bb5acd0e095f8adfbb6a7&chksm=ea79047fdd0e8d69c07d3e1fc13cc1ca1153905533827f4fd65905bf7e2d2d4bcc99b272006d&token=2119834800&lang=zh_CN#rd)
- [控制理论思维导图](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247486407&idx=1&sn=f2c4d7cd4ae591e07f0d344a0203ab58&chksm=ea7903b6dd0e8aa0b24f8de306139c385beacc60f8bd0bfe1bf0236b865d458a31e2d11a237c&token=2119834800&lang=zh_CN#rd)

其他推荐的资料：

- matlab是之前的文章说明几次的了，做算法，控制都可以去学习使用。上面的工具非常丰富，数学功能也很强大，并且与它相关学习书籍和资料都非常完善了，搭配他们的官网和国内的中文论坛使用完全可以快速上手。
- python，以前也提到过了，当然C/C++也是可以，只是python中现成的库实现数学运算或做个仿真测试还是比较方便的。平时使用搭配jupyter lab使用则编译都省了，完全可以边学习边做记录边看程序结果，随写随用。

- 以上两者都可以看做是工具，也可以重点掌握一个，另一个当做参考使用。你若已经有其他习惯的工具或编程语言也可以不使用二者。如果是还没毕业的学生或是工作过程使用算法不多的朋友则做个了解即可，你有时间精力学习那更好。你也完全可以在使用到时再强化学习，这样目的性更强，学起来也就更快。

- 关于PID控制的书籍就不推荐了，市面上优秀的书籍也非常多，可以看目录选择自己需要的。有条件又刚好需要的可以看些外文版的。

- 一些可参考的代码：

![开源参考代码](https://files.mdnice.com/user/38598/e8eeca4b-5cec-4d9c-a4c9-07a821ab4953.png)

很多只简单了解过PID算法的人都会说它是普通人难以理解，但业内开发者又不得不学习应用。其实所有算法（或技术）都是这样，不从事相关应用就不会去深入学习这些东西。生活中也一样，就像很多开发者都可能遇到过的被亲戚或朋友叫去修电脑或电器一样，一般人并不会关心电器或软件运行的原理，等到功能失常了才会第一时间想到身边哪个是做开发的。

----

占位

>>>文章内容为作者个人观点，难免有疏忽或错误，若有不同见解可以交流评论，若发现错误还请指正，若认同文章观点，欢迎关注，分享。

>>如学习需要或项目合作可以扫码添加微信交流。
>>![](https://files.mdnice.com/user/38598/6fbcd253-edc6-4175-ba0c-44e24ad33b21.jpg)
>>
>>建有交流群，以方便大家平时交流、学习，如果要进群，加好友时记得备注信息`进群`。
>>
>>**注意：加好友的人比较多，为提高交流效率，节约大家时间，未备注则默认不邀请进群。**

`温馨提示：部分文章中附有分享文件，若需要获取，进入公众号后台发送对应关键字，可自动获取，此举也是为了提高效率，节约时间。不要在留言或个人微信聊天界面发送关键字，一是留言区没有机器人，二是个人聊天默认不回复此类信息，请悉知！！！`

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
