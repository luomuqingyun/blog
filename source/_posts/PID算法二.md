---
title: PID算法二
date: 2025-05-19 14:42:00
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
---
## PID算法应用公式演化
上一片文章内容介绍了PID算法的概况和调参说明以及一些动图演示，这篇文章我们一起来来了解一下两种常用的简单PID算法结构——位置式PID与增量式PID。熟悉这两种算法结构后，后面的文章再介绍一些更为复杂的改进算法。

正如之前介绍的，PID算法控制系统的函数表达式为：
$$
u(t) = Kp*e(t) + Ki*∫e(t)dt + Kd*\frac{de(t)}{dt}
$$
以上公式被称为理想公式，它或者可以写为更为“标准”的表达式法：
$$
u(t) = Kp*\Big(e(t) + \frac{1}{Ti}∫e(t)dt + Td*\frac{de(t)}{dt}\Big)
$$

其中：

$Ti$为积分时间，

$Td$为微分时间。

实际上两表达式的转化关系也就是：

$$
Ki = \frac{Kp}{Ti}
$$
     
    
$$
Kd = \frac{Kp}{Td}
$$

当然,无论以上哪个公式都是基于连续时间系统而推倒出来的公式。也就是这是一个模拟系统公式，因为PID算法的应用远早于数字信号的应用，最开始是用来进行机械控制的，比如控制航行方向。但是设计的控制器是实实在在根据系统响应设计的模拟控制仪器，有点类似收音机调频器。

![原始的PID控制器](https://files.mdnice.com/user/38598/f541128b-9eca-43eb-ad56-9bb75e5f6f33.png)

从信号与系统的角度来看，PID控制算法可以当做为一种频域系统的滤波器，当然它与传统的几种滤波器还是有所区别，这可以从它的传递函数中略窥一二，其系统的拉普拉斯变换公式可以写成：

$$
L(s) = Kp + \frac{Ki}{s} + Kd*s
$$

或者
$$
L(s) = \frac{Kp*s^2 + Kd*s+ Ki}{s+C}
$$

这个拉普拉斯公式也就是系统的传递函数，这些公式涉及一些比较复杂的理论知识，仅作了解，写多了肯定很多人都会失去兴趣，所以就不做详细介绍了，有兴趣的朋友可以查阅相关教材或论文进行详细学习。

随着数字信号与计算机的应用，科学家们将PID算法应用在了电子控制的方方面面。现在我们平时应用的pid控制理论算法都是基于信号采样的离散信号系统。在离散信号中，可以使用求和代替积分，差分代替微分，所以PID算法公式就可以转化为以下表达式：
$$
u(t) = Kp*e(t)+Ki*\sum_{n=0}^{t}{e(n)}+Kd*(e(t)-e(t-1))
$$

这就是标准的数字PID表达式，也就是经典位置式PID算法。从公式中可以看出，整个算法过程中积分项都不停的累加误差值，这对于资源有限的单片机系统来说并不太友好，虽然从程序实现上来说每次运算都只需实现一次累加即可，但同样还是会引发一些问题，比如：积分饱和问题。

>积分饱和是理想PID算法实现时常见的问题。若设定值有大的变动，其积分量会有大幅的变化，大到输出值被上下限限制而饱和，因此系统会有过冲，而且即使误差量符号改变，积分量变小，但输出值仍被上下限限制，维持在上限（或下限），因此输出看似没有变化，系统仍会持续的过冲，一直要到输出值落在上下限的范围内，系统的振荡才会开始下降。
>
>改善措施：
>
> - 在程序输出参数偏离可控制范围时，暂停积分项的计算。
> - 把积分项计算结果限制在一个较小的上下限范围内。
> - 也可以根据实际情况重新计算积分项，使控制器输出维持在上下限之间的范围内。

如果将以上公式中的两次计算结果相减会得到什么呢？
$$
u(t)-u(t-1) = Kp*\Big(e(t)-e(t-1))+Ki*(e(t))+Kd*(e(t)-2*e(t-1)+e(t-2)\Big)
$$

上式中可以看成求和积分部分已经抵消了，现在转换思路，PID算法都是根据之前的误差来计算下一步的输出值，从而减低误差与实际值之间差距。上式就是前后两个状态值之差值，如果进行小学数学运算将$u(t-1)$移到等式右侧。这就意味着，本次输入值是上一时刻输入值与最近两次误差之间的计算量之和，依次类推，下一次控制的输入结果就是本次输入结果与本次误差及上次误差的计算值之和，从以上公式可以看出只需参考最近两次的误差值，再将它们的计算结果与前一次输入结果求和就可以得到下一次的控制值了。这种应用反向思维，即根据一个初始值通过最近的两次误差进行计算然后推导下一时刻控制值的算法就称之为增量式PID算法。与位置式PID算法公式先比，增量式明显解决了积分的问题，简化了计算方法，对单片机应用来说还是很有优势的。

当然这两种算法本质都是一个娘胎出来的，所以理论上它们没有啥大的区别，都是为了方便实际使用而进行相应的优化，所以至于哪种适合你的控制系统需要你自己根据实际情况而定，没有绝对的优劣之分。并且你若需要实现一个效果良好的控制系统肯定不仅仅只需掌握这两公式就能完美实现的，实际使用还有其他的一些更现实的问题需要我们去解决。不过如果你的控制系统要求不高，那就简单多了，你甚至可以简化很多控制步骤。这里先稍作了解，日后再写文特做说明吧。当然还是那句话有兴趣的朋友可以继续做更深层次的学习。

## 位置式PID参考代码
```c
//注意：代码仅做参考，没有具体实现目标，可以视为伪代码，看你使用硬件平台是否支持浮点运算，不支持请转换浮点，仅有框架，其他功能需要自行添砖加瓦！

// PID参数
float kp = 0.01f, ki = 0.005f, kd = 0.001f;

// 目标位置和当前位置
float target_pos = 0.0f;
float current_pos = 0.0f; 

// PID计算中间变量
float pid_error = 0.0f;
float pid_integral = 0.0f;
float pid_derivative = 0.0f;
float pid_output = 0.0f;

// PID控制函数
float PID_control(float target, float curr_pos) {

  // 计算位置误差
  pid_error = target - curr_pos; 
  
  // 积分项
  pid_integral += pid_error;

  // 微分项 
  pid_derivative = pid_error - pre_pid_error;

  // PID输出
  pid_output = kp*pid_error + ki*pid_integral + kd*pid_derivative;
  
  // 返回输出值
  return pid_output;

}

int main(void) {

  // 初始化系统时钟等

  // 设置目标位置
  target_pos = 20.0f;
  
  // 获取当前位置
  current_pos = read_xxx();
  //current_pos = 10.0f; // 也可酌情设置某初值

  // 调用PID控制
  pid_output = PID_control(target_pos, current_pos);
  
  // 输出控制量 
  set_xxx(pid_output);
  
  while(1) {
    //更新周期
    if(xx){
      // 读取实际值获取当前位置量
      current_pos = read_xxx();  

      // 调用PID计算输出
      pid_output = PID_control(target_pos, current_pos);

      // 设置输出结果
      set_xxx(pid_output);
    }
  }
}
```

## 增量式PID参考代码
```c
//注意：代码仅做参考，没有具体实现目标，可以视为伪代码，看你使用硬件平台是否支持浮点运算，不支持请转换浮点，仅有框架，其他功能需要自行添砖加瓦！
// PID参数
float kp = 0.5, ki = 0.01, kd = 0.1;

float setpoint = 0.0; //目标值
float meas_value = 0.0; //设测量值 
float output = 0.0;

// PID计算中间变量
float pid_error = 0; 
float pid_pre_error = 0;
float pid_integral = 0;
float pid_derivative = 0;
float pid_output = 0;
float pid_prev_output = 0;

// 增量式PID算法
float PID_incremental(float setpoint, float measured_value) {

  // 计算当前误差
  pid_error = setpoint - measured_value;

  // 积分项
  pid_integral += pid_error;

  // 微分项
  pid_derivative = pid_error - pid_pre_error;

  // 当前输出  
  pid_output = pid_prev_output + kp*(pid_error - pid_pre_error) + ki*pid_integral + kd*pid_derivative;
  
  // 更新上一次误差 
  pid_pre_error = pid_error;

  // 更新上一次输出
  pid_prev_output = pid_output;

  return pid_output;

}

int main(void) {

  setpoint = 100.0; //目标值
  meas_value = 50.0; //设置某初值或进行测量值 

  // 调用增量式PID算法
  output = PID_incremental(setpoint, meas_value);

  // 设置输出结果
  set_xxx(output); 
  while(1) {
    //到达测试周期后
    if(xx){
      // 获取测量值 
      meas_value = get_measured_value();

      // 调用增量PID算法
      output = PID_incremental(setpoint, meas_value);

      // 控制执行器
      set_xxx(output); 
    }
  }
}
```
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
