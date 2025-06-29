---
title: PID算法（八）之遗传算法
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
## 遗传算法

![遗传算法关系图](https://files.mdnice.com/user/38598/2fb4337b-7a92-4639-8e5c-697fd96bb87f.png)

遗传算法（Genetic Algorithm，GA）是进化算法的一种。进化算法最初是借鉴了进化生物学中的一些现象而发展起来的，它是遗传算法、进化策略、进化规划的统称。进化计算起源于20世纪50年代末，成熟于20世纪80年代，目前主要被应用于智能控制工程、机器学习、应用数学等领域。

在计算机科学和运筹学中，遗传算法是一种受自然选择过程启发的元启发式算法（又称万能启发式演算法或万用启发式演算法），属于更大类别的进化算法(EA)。是一种模拟自然进化过程的搜索算法，它通过模拟遗传，自然选择、交叉（杂交）和变异（突变）等过程，从候选解中寻找最优解。遗传算法通常用于通过依赖生物学启发的算子（例如变异、交叉和选择）来生成优化和搜索问题的高质量解决方案。

## 遗传算法执行原理

![遗传算法执行步骤](https://files.mdnice.com/user/38598/032623eb-66d7-48c4-acb8-915b3a0b9c96.png)

在遗传算法里，优化问题的解被称为个体，它表示为一个变量序列，叫做染色体或者基因串。染色体一般被表达为简单的字符串或数字串，不过也有其他的依赖于特殊问题的表示方法，这一过程称为编码。

首先，算法随机生成一定数量的个体，当然，操作者也可以干预这个随机产生过程，以提高初始种群的质量。在每一代中，都会评价每一个体，并通过计算适应度函数得到适应度数值。按照适应度排序种群个体，适应度高的在前面。

接下来是产生下一代个体并组成种群，这个过程是通过选择和繁殖完成，其中繁殖包括杂交（crossover，在算法研究领域中称之为交叉操作）和突变（mutation）。选择是根据新个体的适应度进行筛选，但它不意味着完全以适应度高低为导向，因为单纯选择适应度高的个体将可能导致算法快速收敛到局部最优解而非全局最优解，这种情况称之为早熟。作为折中，遗传算法依据原则：适应度越高，被选择的机会越高，而适应度低的，被选择的机会就低。初始的数据可以通过这样的选择过程组成一个相对优化的群体。之后，被选择的个体进入交配过程。

一般的遗传算法都有一个交配概率（又称为交叉概率），范围一般是0.6~1，这个交配概率反映两个被选中的个体进行交配的概率。例如，交配概率为0.8，则80%的“夫妻”会生育后代。每两个个体通过交配产生两个新个体，代替原来的“老”个体，而不交配的个体则保持不变。交配父母的染色体相互交换，从而产生两个新的染色体，第一个个体前半段是父亲的染色体，后半段是母亲的，第二个个体则正好相反。不过这里的半段并不是真正的一半，这个位置叫做交配点，也是随机产生的，可以是染色体的任意位置。

再接下来就是突变，可以通过突变产生新的“子”个体。一般遗传算法都有一个固定的突变常数（又称为变异概率），通常是0.1或者更小，这代表变异发生的概率。根据这个概率，新个体的染色体随机的突变，通常就是改变染色体的一个字节（0变到1，或者1变到0）。

经过这一系列的过程（选择、交配和突变），产生的新一代个体不同于初始的一代，并一代一代向增加整体适应度的方向发展。
![遗传算法模型演化](https://files.mdnice.com/user/38598/48f5f9c4-905b-4616-a937-2057d65e3e3b.png)

整个过程应该理解起来还是没有压力的吧，我们都是学过高中生物的了，简单描述它就是适者生存的自然进化法则。

## 遗传算法常见术语
遗传算法由自然界的遗传规律发展而来，所以很多关键术语都是非常好理解的。简单的讲将这些术语通过一定规律的数据序列演绎出来就形成了遗传算法。

![遗传算法术语关系](https://files.mdnice.com/user/38598/4422ed04-6f5c-4716-9b8a-40aed8419e69.png)

- 种群（population）：个体的集合，该集合内个体数称为种群；

- 个体（individual）：指染色体带有特征的实体；

- 染色体（Chromosome）：携带遗传基因的序列；

- 基因型(genotype)：性状染色体的内部表现；

- 表现型(phenotype)：染色体决定的性状的外部表现，及显性性状；

- 进化(evolution)：种群逐渐适应生存环境，品质不断得到改良。生物的进化是以种群的形式进行的；

- 适应度(fitness)：度量某个物种对于生存环境的适应程度；

- 选择(selection)：以一定的概率从种群中选择若干个个体。一般，选择过程是一种基于适应度的优胜劣汰的过程；

- 复制(reproduction)：细胞分裂时，遗传物质DNA通过复制而转移到新产生的细胞中，新细胞就继承了旧细胞的基因；

- 交叉(crossover)：两个染色体的某一相同位置处DNA被切断，前后两串分别交叉组合形成两个新的染色体。也称基因重组或杂交；

- 变异(mutation)：复制时可能（很小的概率）产生某些复制差错，变异产生新的染色体，表现出新的性状；

- 编码(coding)：DNA中遗传信息在一个长链上按一定的模式排列。遗传编码可看作从表现型到基因型的映射；

- 解码(decoding)：基因型到表现型的映射。


## 基于遗传算法的PID控制

![基于遗传算法的PID控制图](https://files.mdnice.com/user/38598/2518cd4d-702d-479e-a3cc-77d4073026e7.png)

基于遗传算法的方法是通过遗传算法搜索最优的PID参数。将遗传算法应用于PID控制的步骤和上文描述步骤一样，简化其行为主要可以分为以下内容：
- 初始化种群

首先，需要根据控制系统的特点和要求，进行编码设计，（可随机）初始化种群。种群中的每个个体表示一个PID参数组合。PID参数组合可以采用多种表示方式，如列表、向量或矩阵等。

- 适应度评估

根据控制系统的性能指标，计算每个个体的适应度。适应度函数的设计是自整定PID算法的重要环节，它决定了算法搜索到的结果。

- 选择

根据个体的适应度进行选择，选择出一定数量的个体作为父代。常用方法有轮盘赌选择、锦标赛选择等。

- 交叉

将父代个体的参数进行交叉，生成新的子代个体。交叉算法可以采用多种方式，如单点交叉、多点交叉和均匀交叉等。

- 变异

对子代个体进行变异，增加种群的多样性。变异算法可以采用多种方式，如点变异、位变异和染色体变异等。

- 生成新一代种群

将父代个体和子代个体合并，形成新的种群。

- 终止与重复

如果达到预定的迭代代数或种群适应度收敛,则终止运算,输出最优参数;否则返回到第二步骤直到达到预定的终止条件。

----

占位

>>>文章内容为作者个人观点，难免有疏忽或错误，若有不同见解可以交流评论，若发现错误还请指正，若认同文章观点，欢迎关注，分享。

>>如学习需要或项目合作可以扫码添加微信交流。
>>![](https://files.mdnice.com/user/38598/6fbcd253-edc6-4175-ba0c-44e24ad33b21.jpg)
>>
>>建有交流群，以方便大家平时交流、学习，如果要进群，加好友时记得备注信息`进群`。
>>
>>**注意：加好友的人比较多，为提高交流效率，节约大家时间，未备注则默认不邀请进群。**

`温馨提示：部分文章中附有分享文件，若需要获取，进入公众号后台发送对应关键字，可自动获取，此举也是为了提高效率，节约时间。不要在留言或个人微信聊天界面发送关键字，一是留言区没有机器人，二是个人聊天默认不回复此类信息，请悉知！`

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

