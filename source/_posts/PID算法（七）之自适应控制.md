---
title: PID算法（七）之自适应控制
author: luomuqingyun
comments: true
math: true
mermaid: true
category:
  - 编程
  - 算法
tags:
  - 编程经验
  - 算法应用
excerpt:
  - PID算法
date: 2025-05-19 14:42:00
---
## 参数自整定

![PID参数自整定控制](https://files.mdnice.com/user/38598/fc5aa8d0-ea59-4dac-9622-0e54e903408f.png)

在控制理论中，自整定（self-tuning）可以在满足目标函数最大化或是最小化的情形下，将其内部运行参数进行最佳化，一般会是进行效率的最大化，或是错误的最小化。

自整定及自动整定（auto-tuning）有时会指同一个概念，许多软体研究群体认为auto-tuning是较正确的名词。不过在变频器领域中，自动整定（auto-tuning）有时只是马达参数自学习，利用测试信号及演算法量测马达参数，不一定包括内部运行参数的最佳化。

自整定系统一般会包括非线性自适应控制。数十年以来，自整定系统已经是航太产业中的标志，这类的反馈在非线性过程的多目标最佳控制非常重要。在电信产业中，常使用自适应通信，其中会动态的调整系统参数，让效率及鲁棒性都可以最大化。

## 智能控制
上一篇文章简单介绍了模糊PID控制算法的一些基础知识。它属于一种智能控制方法，在控制过程中实现了参数的自整定，这种复杂的控制方法在复杂的控制系统中才会被使用，简单的控制系统中使用普通算法能实现控制就不需要构建复杂算法增加成本了。在PID控制领域还有其他各种类型智能控制算法，比如自适应PID控制，基于神经网络的PID控制，基于遗传算法的PID控制等等。

我们应用时可以根据系统复杂程度选择合适的控制算法，并且也会根据实际情况进行组合使用，通常情况下都会涉及到自适应调节过程。甚至结合其他控制算法使用，比如最常见的卡尔曼滤波。

当然，智能控制领域一直在发展，只要人类社会还要“偷懒”，还需要追求低碳节能，那控制算法就还会不断更新或产生新的应用算法。如果你有兴趣并且又有这方面的潜质那往算法领域深入发展肯定会有很不错的职业前景。

再次贴出这张脑图，很多专业技能可以依循它展开学习。图中涵盖内容广泛并不是所有人都需要成为这个领域的专家，所以在自己的领域内选择需要用到的版块进行学习，当然，信号系统分析还是推荐最好要掌握的，另外值得一提的是，python或matlab都是很重要的一种分析工具。更多理论可以详细阅读相关的研究书籍，当然平时可以多看些外文书籍或论文，一些复杂的概念他们可能写得更清晰易懂。

## 自适应控制

自适应控制（Adaptive control）也称为适应控制，是一种对系统参数的变化具有适应能力的控制方法。在一些系统中，系统的参数具有较大的不确定性，并可能在系统运行期间发生较大改变。比如说，客机在作越洋飞行时，随着时间的流逝，其重量和重心会由于燃油的消耗而发生改变。虽然传统控制方法（即基于时不变假设Non-Time-Variant Assumption的控制方法）具有一定的对抗系统参数变化的能力，但是当系统参数发生较大变化时，传统控制方法的性能就会出现显著的下降，甚至产生发散。

自适应控制通常可以分为两种类型，一种叫做直接自适应控制（Direct Adptive Control），另一种叫做间接自适应控制（Indirect Adaptive Control）实际系统中一般采用直接自适应控制方法。

直接自适应控制直接对控制器的参数进行在线调整，其目的是使得系统的跟踪误差趋于零。通过简单的Lyapunov稳定性(李雅普诺夫稳定性)推导，可以得到直接自适应控制的控制律。而通过充分利用实际系统的时延，可以运用上一采样时刻的参数值更新控制律，从而大大减小了直接自适应控制的在线计算量。

间接自适应控制是通过对系统模型某个或某些未知参数进行在线估计，然后将这些参数的最新估计值代入并更新所设计的控制器的增益[1]。间接自适应控制的目的是使得该参数的估计误差趋于零。所以，间接自适应控制一般要求对系统模型结构有清晰的了解。然而要想获得实际系统的精确模型几乎是不可能的。


自适应控制主要是根据系统过程的变化实时调整PID参数,使系统适应变化，实现对部分未知或时变系统的控制，常用方法有增益调节、模型参考自适应等。自适应PID控制的实现过程：

- 构建初始PID控制器,选取合适的PID参数。

- 在线实时收集控制系统的状态数据,如过程变量、控制变量、误差等。

- 根据收集到的新数据,评估当前PID参数的控制效果。

- 使用参数自适应调节算法,根据控制效果评估结果,调整PID的控制参数。

- 重复步骤2-4,使PID参数不断适应过程的变化,实现自适应优化控制。

## 神经网络

人工神经网络（英语：Artificial Neural Network，ANN），简称神经网络（Neural Network，NN）或类神经网络，在机器学习和认知科学领域，是一种模仿生物神经网络（动物的中枢神经系统，特别是大脑）的结构和功能的数学模型或计算模型，用于对函数进行估计或近似。神经网络由大量的人工神经元联结进行计算。

大多数情况下人工神经网络能在外界信息的基础上改变内部结构，是一种自适应系统，通俗地讲就是具备学习功能。现代神经网络是一种非线性统计性数据建模工具，神经网络通常是通过一个基于数学统计学类型的学习方法（Learning Method）得以优化，所以也是数学统计学方法的一种实际应用，通过统计学的标准数学方法我们能够得到大量的可以用函数来表达的局部结构空间

另一方面，在人工智能学的人工感知领域，我们通过数学统计学的应用可以来做人工感知方面的决定问题（也就是说通过统计学的方法，人工神经网络能够类似人一样具有简单的决定能力和简单的判断能力），这种方法比起正式的逻辑学推理演算更具有优势。

![神经网络PID控制](https://files.mdnice.com/user/38598/1ebe8608-6fb7-4b88-b2fc-df6cbd1dc4a1.png)

基于神经网络的PID控制是指使用神经网络来代替传统PID控制器中的比例、积分和微分参数。通过大量神经网络训练数据构成一个控制系统的适应性机制，它可近似任意非线性函数，通过学习调整网络权值实现控制。它可以通过学习来发现复杂的控制关系，在实际应用中得到了广泛的应用。建立基于神经网络的PID控制算法包含以下几个步骤：
- 建立神经网络模型

首先，需要根据控制系统的特点和要求，建立神经网络模型。神经网络模型的输入包括控制系统的状态和输入，输出为控制系统的控制量。

- 训练神经网络模型

使用控制系统的实际数据训练神经网络模型。

- 使用神经网络模型控制系统

将神经网络模型部署到控制系统中，使用神经网络模型生成控制量作用于控制系统。

----
>>>文章内容为作者个人观点，难免有疏忽或错误，若有不同见解可以交流评论，若发现错误还请指正，若认同文章观点，欢迎关注，分享。

>>>如学习需要或项目合作可以扫码添加微信。
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
