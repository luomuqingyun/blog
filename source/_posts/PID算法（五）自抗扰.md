---
title: PID算法（五）自抗扰
date: 2025-05-19 14:42:00
---

>***幸福的家庭都是相似的，不幸的家庭各有各的不幸。***
>
>如果列夫·托尔斯泰是名理科生，或许他会说，`线性控制系统都是相似的，非线性控制系统各有各的不同。`

## 线性控制系统
**线性控制系统（Linear Control System）** 是指系统的数学模型是线性微分方程或线性差分方程控制的系统。这类系统的特点是符合线性`叠加原理`，即系统对输入的响应是输入的线性叠加。

根据定义和图解可知PID控制算法的系统输入，输出关系是符合线性关系的，所以他是最常见的线性控制器设计方法之一。

![PID算法框架](https://files.mdnice.com/user/38598/c13fcb0f-fd82-4432-b096-57127879cbce.png)

- 线性控制系统通常可以用传递函数或状态空间模型来描述。

- 线性系统满足叠加原理,即系统对两个输入信号叠加后的响应等于对两个输入的响应叠加。这一特点简化了线性系统的分析。

- 线性系统的参数不随状态或输入改变而改变,系统特性保持不变。这称为时不变性,使系统行为稳定可预测。线性时不变系统可用简单的频域分析方法,如频率响应、根轨迹等。频域方法直观而有效。

- 线性方程组的解通常存在并且唯一,理论上能得到系统的精确数学模型。这使线性系统的稳定性分析简单化。

- 线性控制系统的分析方法有根轨迹法、频率响应方法、状态空间方法等。这些方法可以用来分析系统的时域和频域特性,稳定性等。

- 线性控制理论是经典控制理论的重要组成部分,在工程控制系统的设计中应用非常广泛。

## 非线性控制系统
**非线性控制系统（Nonlinear Control System）** 顾名思义它正好与线性控制系统相对。非线性控制系统的数学模型包含非线性项,通常为非线性微分方程或者非线性差分方程。这类方程中会出现乘幂、指数、三角函数等非线性表达式。常见的非线性方程有:
- 带有乘幂项的多项式方程
- 正弦/余弦函数的三角方程 
- 指数函数方程
- 含有反函数的隐函数方程

这使得非线性系统行为复杂多变,难以建立精确的数学模型。

- 非线性叠加原理不成立：

非线性系统的输入和输出不满足线性叠加原理。多个输入叠加后产生的输出不等于对应输出的叠加。这意味着系统特性依赖于工作状态变化。

- 参数变化系统：

非线性系统的参数往往会随状态变量变化而变化,产生参数变化的特性。这导致系统动态特性随工作条件改变。

- 存在复杂动态特性：

非线性系统可能出现线性系统没有的复杂动态,如多稳态、混沌、奇异性等。这给系统分析和控制带来难度。

- 全局性与局部性：
非线性系统难以求得全局解,往往只能在某工作区域求局部近似解。这也是非线性系统分析和设计的困难之处。

非线性系统拟合效果好,但设计复杂，并且非线性系统具有复杂变化的动力学特性,给控制系统设计带来挑战。需要使用特定方法分析其非线性行为,才能设计出满足控制要求的非线性控制器。

线性系统理论成熟,有一系列成熟分析工具,这使其在工程控制中应用广泛。但线性系统也存在一定局限,无法描述复杂非线性过程。两者优劣各有侧重,需要根据实际选择合适的系统描述方法。

## 自抗扰控制
**自抗扰控制（Active Disturbance Rejection Control，简称ADRC）**
是由中国科学院的韩京清教授（1937年11月1日—2008年4月21日）基于PID控制理论提出的一种应对非线性，时变，不确定性和扰动的独立于复杂数学模型的现代控制方法。自抗扰控制继承了传统PID控制的优势：误差反馈控制，并且改进了PID控制中的缺点：误差提取法和加权误差。当然，经过几十年的发展，现在ADRC控制理论新的继承者们已经实现了线性ADRC控制理论，所以给人感觉上似乎ADRC控制理论又回到PID控制理论了。以后再细写吧，有意愿的朋友可以读读韩京清教授的书籍和论文。`温馨提示：MATLAB上都有现成的PID和ADRC仿真模型，有安装软件的朋友可去探索，仿真实现后可以生成C语言试试`。

![ADRC控制模型](https://files.mdnice.com/user/38598/32ac6dea-0ad3-4701-bbc2-f9c472415199.png)


![ADRC控制模型英文描述](https://files.mdnice.com/user/38598/19b4cb9e-dd2e-4b67-8722-5820957b3113.png)


ADRC主要思想和特点包括:

- 扩张状态观测器(ESO):

利用扩张状态观测器在线实时估计系统的全部状态变量和外部扰动。不依赖对象模型。

- 状态错误反馈(状态反馈)

将ESO估计的状态反馈进行控制,抑制系统对扰动的敏感性。

- 自抗扰控制律

设计一个鲁棒的PD控制律来抵抗系统的内部参数变化。

- 串级补偿(滤波补偿)

串级加入一个滤波器补偿时滞,提高系统的动态特性。

- 无需精确模型

ADRC不依赖对象模型,对参数变化和外部扰动都具有很强的适应性。

- （相对）简单实用

ADRC算法简单,易于工程实现,适用于各类非线性反应迟缓过程的控制。

ADRC已经成功应用于各种复杂工业过程的控制,显示出良好的抗扰性、适应性和鲁棒性,是一种非常有效的现代控制方法。它为复杂非线性过程的控制问题提供了一个较好的解决方案。

## ADRC调试
ADRC算法调试主要涉及以下几个方面:

- ESO参数调试

ESO的带宽选择应大于控制对象的主要动态过程的频率。初值可取较大,再逐步减小,直到得到满意的状态估计响应。

2. 反馈控制参数调试

选择合适的反馈控制参数,如PID控制中KP、KI、KD的取值,以获得所需的控制效果。

3. 滤波补偿参数调试

调整滤波补偿器参数,补偿系统的时滞特性,提高系统动态响应速度。

4. 整定和测试

整定控制参数,进行步响应测试,观察调整过程,直到获得满意的速度响应、稳定性和抗扰动性。

5. 在线调整

由于ADRC对对象参数变化不敏感,可建立在线调节机制,在运行过程中实时调整参数,适应参数变化。

总体来说,ADRC算法调试注重ESO、控制器和补偿器的参数协调整定,既要保证稳定性,又要获得满意的动态特性。多次测试和参数调整是获得最佳控制效果的关键。

## 参考控制程序
附一个可以借鉴的ADRC控制无人机程序,源于github开源仓库，程序调试的不错，值得参考，链接：
`https://github.com/wustflywithdream/ADRC`
```
#include "Headfile.h"
#include "ADRC.h"
/*----------------------------------------------------------------------------------------------------------------------/
        *               本程序只供购买者学习使用，版权著作权属于无名科创团队，
        *               无名科创团队将飞控程序源码提供给购买者，
        *               购买者要为无名科创团队提供保护，
        *               未经作者许可，不得将源代码提供给他人
        *               不得将源代码放到网上供他人免费下载，
        *               更不能以此销售牟利，如发现上述行为，
        *               无名科创团队将诉之以法律解决！！！
-----------------------------------------------------------------------------------------------------------------------/
        *               生命不息、奋斗不止；前人栽树，后人乘凉！！！
        *               开源不易，且学且珍惜，祝早日逆袭、进阶成功！！！
-----------------------------------------------------------------------------------------------------------------------/
	*		无名科创开源飞控 V1.1	武汉科技大学  By.YuYi
	*		CSDN博客: http://blog.csdn.net/u011992534
	*               优酷ID：NamelessCotrun无名小哥
	*               无名科创开源飞控QQ群：540707961
        *               https://shop348646912.taobao.com/?spm=2013.1.1000126.2.5ce78a88ht1sO2
        *               百度贴吧:无名科创开源飞控
        *               修改日期:2017/10/30
        *               版本：V1.1
        *               版权所有，盗版必究。
        *               Copyright(C) 武汉科技大学无名科创团队 2017-2019
        *               All rights reserved
----------------------------------------------------------------------------------------------------------------------*/
Fhan_Data ADRC_Pitch_Controller;
Fhan_Data ADRC_Roll_Controller;
const float ADRC_Unit[3][16]=
{
/*TD跟踪微分器   改进最速TD,h0=N*h      扩张状态观测器ESO           扰动补偿     非线性组合*/
/*  r     h      N                  beta_01   beta_02    beta_03     b0     beta_0  beta_1     beta_2     N1     C    alpha1  alpha2  zeta  b*/
 {300000 ,0.005 , 3,               300,      4000,      10000,     0.001,    0.002,   2.0,      0.0010,    5,    5,    0.8,   1.5,    50,    0},
 {300000 ,0.005 , 3,               300,      4000,      10000,     0.001,    0.002,   2.0,      0.0010,    5,    5,    0.8,   1.5,    50,    0},
 {300000 ,0.005 , 3,               300,      4000,      10000,     0.001,    0.002,   1.2,      0.0005,    5,    5,    0.8,   1.5,    50,    0},
};


float Constrain_Float(float amt, float low, float high){
  return ((amt)<(low)?(low):((amt)>(high)?(high):(amt)));
}

int16_t Sign_ADRC(float Input)
{
    int16_t output=0;
    if(Input>1E-6) output=1;
    else if(Input<-1E-6) output=-1;
    else output=0;
    return output;
}

int16_t Fsg_ADRC(float x,float d)
{
  int16_t output=0;
  output=(Sign_ADRC(x+d)-Sign_ADRC(x-d))/2;
  return output;
}


void ADRC_Init(Fhan_Data *fhan_Input1,Fhan_Data *fhan_Input2)
{
  fhan_Input1->r=ADRC_Unit[0][0];
  fhan_Input1->h=ADRC_Unit[0][1];
  fhan_Input1->N0=(uint16)(ADRC_Unit[0][2]);
  fhan_Input1->beta_01=ADRC_Unit[0][3];
  fhan_Input1->beta_02=ADRC_Unit[0][4];
  fhan_Input1->beta_03=ADRC_Unit[0][5];
  fhan_Input1->b0=ADRC_Unit[0][6];
  fhan_Input1->beta_0=ADRC_Unit[0][7];
  fhan_Input1->beta_1=ADRC_Unit[0][8];
  fhan_Input1->beta_2=ADRC_Unit[0][9];
  fhan_Input1->N1=(uint16)(ADRC_Unit[0][10]);
  fhan_Input1->c=ADRC_Unit[0][11];

  fhan_Input1->alpha1=ADRC_Unit[0][12];
  fhan_Input1->alpha2=ADRC_Unit[0][13];
  fhan_Input1->zeta=ADRC_Unit[0][14];
  fhan_Input1->b=ADRC_Unit[0][15];

  fhan_Input2->r=ADRC_Unit[1][0];
  fhan_Input2->h=ADRC_Unit[1][1];
  fhan_Input2->N0=(uint16)(ADRC_Unit[1][2]);
  fhan_Input2->beta_01=ADRC_Unit[1][3];
  fhan_Input2->beta_02=ADRC_Unit[1][4];
  fhan_Input2->beta_03=ADRC_Unit[1][5];
  fhan_Input2->b0=ADRC_Unit[1][6];
  fhan_Input2->beta_0=ADRC_Unit[1][7];
  fhan_Input2->beta_1=ADRC_Unit[1][8];
  fhan_Input2->beta_2=ADRC_Unit[1][9];
  fhan_Input2->N1=(uint16)(ADRC_Unit[1][10]);
  fhan_Input2->c=ADRC_Unit[1][11];

  fhan_Input2->alpha1=ADRC_Unit[1][12];
  fhan_Input2->alpha2=ADRC_Unit[1][13];
  fhan_Input2->zeta=ADRC_Unit[1][14];
  fhan_Input2->b=ADRC_Unit[1][15];
}



//ADRC最速跟踪微分器TD，改进的算法fhan
void Fhan_ADRC(Fhan_Data *fhan_Input,float expect_ADRC)//安排ADRC过度过程
{
  float d=0,a0=0,y=0,a1=0,a2=0,a=0;
  float x1_delta=0;//ADRC状态跟踪误差项
  x1_delta=fhan_Input->x1-expect_ADRC;//用x1-v(k)替代x1得到离散更新公式
  fhan_Input->h0=fhan_Input->N0*fhan_Input->h;//用h0替代h，解决最速跟踪微分器速度超调问题
  d=fhan_Input->r*fhan_Input->h0*fhan_Input->h0;//d=rh^2;
  a0=fhan_Input->h0*fhan_Input->x2;//a0=h*x2
  y=x1_delta+a0;//y=x1+a0
  a1=sqrt(d*(d+8*ABS(y)));//a1=sqrt(d*(d+8*ABS(y))])
  a2=a0+Sign_ADRC(y)*(a1-d)/2;//a2=a0+sign(y)*(a1-d)/2;
  a=(a0+y)*Fsg_ADRC(y,d)+a2*(1-Fsg_ADRC(y,d));
  fhan_Input->fh=-fhan_Input->r*(a/d)*Fsg_ADRC(a,d)
                  -fhan_Input->r*Sign_ADRC(a)*(1-Fsg_ADRC(a,d));//得到最速微分加速度跟踪量
  fhan_Input->x1+=fhan_Input->h*fhan_Input->x2;//跟新最速跟踪状态量x1
  fhan_Input->x2+=fhan_Input->h*fhan_Input->fh;//跟新最速跟踪状态量微分x2
}


//原点附近有连线性段的连续幂次函数
float Fal_ADRC(float e,float alpha,float zeta)
{
    int16 s=0;
    float fal_output=0;
    s=(Sign_ADRC(e+zeta)-Sign_ADRC(e-zeta))/2;
    fal_output=e*s/(powf(zeta,1-alpha))+powf(ABS(e),alpha)*Sign_ADRC(e)*(1-s);
    return fal_output;
}




/************扩张状态观测器********************/
//状态观测器参数beta01=1/h  beta02=1/(3*h^2)  beta03=2/(8^2*h^3) ...
void ESO_ADRC(Fhan_Data *fhan_Input)
{
  fhan_Input->e=fhan_Input->z1-fhan_Input->y;//状态误差

  fhan_Input->fe=Fal_ADRC(fhan_Input->e,0.5,fhan_Input->h);//非线性函数，提取跟踪状态与当前状态误差
  fhan_Input->fe1=Fal_ADRC(fhan_Input->e,0.25,fhan_Input->h);

  /*************扩展状态量更新**********/
  fhan_Input->z1+=fhan_Input->h*(fhan_Input->z2-fhan_Input->beta_01*fhan_Input->e);
  fhan_Input->z2+=fhan_Input->h*(fhan_Input->z3
                                 -fhan_Input->beta_02*fhan_Input->fe
                                   +fhan_Input->b*fhan_Input->u);
 //ESO估计状态加速度信号，进行扰动补偿，传统MEMS陀螺仪漂移较大，估计会产生漂移
  fhan_Input->z3+=fhan_Input->h*(-fhan_Input->beta_03*fhan_Input->fe1);
}


/************非线性组合****************/
/*
void Nolinear_Conbination_ADRC(Fhan_Data *fhan_Input)
{
  float d=0,a0=0,y=0,a1=0,a2=0,a=0;
  float Sy=0,Sa=0;//ADRC状态跟踪误差项

  fhan_Input->h1=fhan_Input->N1*fhan_Input->h;

  d=fhan_Input->r*fhan_Input->h1*fhan_Input->h1;
  a0=fhan_Input->h1*fhan_Input->c*fhan_Input->e2;
  y=fhan_Input->e1+a0;
  a1=sqrt(d*(d+8*ABS(y)));
  a2=a0+Sign_ADRC(y)*(a1-d)/2;

  Sy=Fsg_ADRC(y,d);
  a=(a0+y-a2)*Sy+a2;
  Sa=Fsg_ADRC(a,d);
  fhan_Input->u0=-fhan_Input->r*((a/d)-Sign_ADRC(a))*Sa-fhan_Input->r*Sign_ADRC(a);

  //a=(a0+y)*Fsg_ADRC(y,d)+a2*(1-Fsg_ADRC(y,d));

  //fhan_Input->fh=-fhan_Input->r*(a/d)*Fsg_ADRC(a,d)
  //                -fhan_Input->r*Sign_ADRC(a)*(1-Fsg_ADRC(a,d));//得到最速微分加速度跟踪量
}
*/
void Nolinear_Conbination_ADRC(Fhan_Data *fhan_Input)
{
  float temp_e2=0;
  temp_e2=Constrain_Float(fhan_Input->e2,-3000,3000);
  fhan_Input->u0=fhan_Input->beta_1*Fal_ADRC(fhan_Input->e1,fhan_Input->alpha1,fhan_Input->zeta)
                +fhan_Input->beta_2*Fal_ADRC(temp_e2,fhan_Input->alpha2,fhan_Input->zeta);

}


void ADRC_Control(Fhan_Data *fhan_Input,float expect_ADRC,float feedback_ADRC)
{
    /*自抗扰控制器第1步*/
    /********
        **
        **
        **
        **
        **
     ********/
      /*****
      安排过度过程，输入为期望给定，
      由TD跟踪微分器得到：
      过度期望信号x1，过度期望微分信号x2
      ******/
      Fhan_ADRC(fhan_Input,expect_ADRC);

    /*自抗扰控制器第2步*/
    /********
            *
            *
       ****
     *
     *
     ********/
      /************系统输出值为反馈量，状态反馈，ESO扩张状态观测器的输入*********/
      fhan_Input->y=feedback_ADRC;
      /*****
      扩张状态观测器，得到反馈信号的扩张状态：
      1、状态信号z1；
      2、状态速度信号z2；
      3、状态加速度信号z3。
      其中z1、z2用于作为状态反馈与TD微分跟踪器得到的x1,x2做差后，
      经过非线性函数映射，乘以beta系数后，
      组合得到未加入状态加速度估计扰动补偿的原始控制量u
      *********/
      ESO_ADRC(fhan_Input);//低成本MEMS会产生漂移，扩展出来的z3此项会漂移，目前暂时未想到办法解决，未用到z3
    /*自抗扰控制器第3步*/
    /********
           **
         **
       **
         **
           **
     ********/
      /********状态误差反馈率***/
      fhan_Input->e0+=fhan_Input->e1*fhan_Input->h;//状态积分项
      fhan_Input->e1=fhan_Input->x1-fhan_Input->z1;//状态偏差项
      fhan_Input->e2=fhan_Input->x2-fhan_Input->z2;//状态微分项，
      /********线性组合*******/
     /*
      fhan_Input->u0=//fhan_Input->beta_0*fhan_Input->e0
                    +fhan_Input->beta_1*fhan_Input->e1
                    +fhan_Input->beta_2*fhan_Input->e2;
     */
      Nolinear_Conbination_ADRC(fhan_Input);
      /**********扰动补偿*******/
      //fhan_Input->u=fhan_Input->u0
      //             -fhan_Input->z3/fhan_Input->b0;
      //由于MEMS传感器漂移比较严重，当beta_03取值比较大时，长时间z3漂移比较大，目前不加入扰动补偿控制量
      fhan_Input->u=Constrain_Float(fhan_Input->u0,-200,200);
}

```


## 号外消息
今天交流群被暂时停用了，大家都还能发消息，但相互看不见，目前新建了交流群，旧群可能还能恢复。又被击到了，太闹腾，不想一个个去拉人进群了，看到消息的朋友可以加入到新群。

![旧群被停用无法加人](https://files.mdnice.com/user/38598/9bed3313-82b5-4c4e-9212-05e76ab6c8a8.jpg)

![新群二维码](https://files.mdnice.com/user/38598/a9ecf00f-4fd0-4da7-9a94-a4ac6f19a41e.jpg)

注意：交流群用于大家日常工作、学习嵌入式，单片机技术交流。请勿发不相关广告，并且不得讨论政治问题，也不得发布违反国家禁令的言论，违者将赠送飞机票一张！


----
>>>文章内容为作者个人观点，难免有疏忽或错误，若有不同见解可以交流评论，若发现错误还请指正，若认同文章观点，欢迎关注，分享。

>>>如学习需要或项目合作可以扫码添加微信。
~~建有交流群，以方便大家平时交流、学习，如果要进群，加好友时记得备注信息`进群`~~ 目前进群开发可直接扫码进群。
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
