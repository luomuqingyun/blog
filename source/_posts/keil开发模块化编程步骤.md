---
title: keil开发模块化编程步骤
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
占位
## 搭建keil模块化编程工程
在[单片机开发模块化编程实例详解](https://mp.weixin.qq.com/s?__biz=MzI1OTQ4MTg4Ng==&mid=2247485647&idx=1&sn=694e1bf1034df905d770d49915efaeb4&chksm=ea7900bedd0e89a81a2471ee82be5f73ca3ba5c8afc94fe16b839e1832e64a6184c17f1ad230&token=765272341&lang=zh_CN#rd)这篇文章中介绍了使用C语言进行模块化编程的原理，但没有讲解怎么使用keil软件进行搭建工程，部分初学者尝试时可能会遇到了一些问题，导致工程创建失败，这篇文章我就来讲解一下整个工程搭建的完整步骤。
## 搭建步骤

> 1. 新建工程

这一步很简单，搭建过工程的可以直接跳过。

![1.1点击新建工程](https://files.mdnice.com/user/38598/77be1f50-bdbd-454d-bd97-e762cfcb92ff.png)

![1.2选择工程编程目录和名称](https://files.mdnice.com/user/38598/6bb29f01-b1ac-4d41-b9dc-4e8bfa6ffcbd.png)


![1.3选择单片机型号](https://files.mdnice.com/user/38598/0cbee5d5-7fda-44a0-890e-4b6021ea47eb.png)

![1.4新建空白工程完成](https://files.mdnice.com/user/38598/1aea7471-790f-4579-bdd8-4c1b506f4560.png)


> 2. 新建文件

这一步也挺简单，搭建过工程的可以直接跳过。

![2.1点击新建文件进行新建](https://files.mdnice.com/user/38598/15d3398a-93a9-43a7-b1dd-6b0e7ef00179.png)

![2.2保存文件](https://files.mdnice.com/user/38598/5ab06927-353a-4425-be55-18dae56efa2e.png)

把新建的文件保存到工程目录下，并按同样的步骤新建其他文件。
> 3. 讲文件添加到工程

新建的文件虽然是保存在工程目录下的，但并不会被工程自动包含进去，这里需要手动将新文件添加到工程中去。这里有很多初学者想很容易忽略，所以后面的步骤容易出问题

![3.1将文件添加到工程](https://files.mdnice.com/user/38598/43b4eaca-8f5e-4c24-8fd9-f2ed7054a68c.png)
`注意：只需要add一次即可，多个文件可以框选一起放添加进去`

> 4. 编程

文件添加进工程之后，即可开始进行编程，为了方便演示，我们就不进行编程了，这里直接将上一篇文章的代码文件复制过来进行操作了。

> 5. 编译与调试

程序代码实现之后即可进行编译，调试了。如果编译有问题则根据错误原因进行修改代码，如果没报错则基本大功告成了，当然要生成HEX文件则在工程设置中还需要勾选output项中的create hex file选项。

![5.1勾选create hex file](https://files.mdnice.com/user/38598/562c94ca-318d-4b27-94b9-fe48626d3c71.png)

> 6. 下载程序到单片机中运行
将最终的hex文件下载都单片机中查看实验现象是否一致。

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