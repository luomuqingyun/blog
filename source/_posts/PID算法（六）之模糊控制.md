---
title: PID算法（六）之模糊控制
date: 2025-05-19 14:42:00
author: luomuqingyun
comments: true
mathjax: true
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
---
## 模糊控制理论
模糊控制是一种基于模糊逻辑的控制方法，所谓的“模糊”是指所涉及的逻辑不能表达为“真”或“假”，而是“部分真”。它是以模糊集合论，模糊语言变量及模糊逻辑推理为基础的计算机智能控制。该控制机制的输入是透过模糊化将原本为0或1的数字逻辑信息变成0到1之间的任意数值，相对于原本数字逻辑的非零即一的二分法更接近人类的逻辑思维。在推论的过程中资料为模糊的，但透过解模糊化的步骤，可使得输出为精确值。总体来说，模糊控制在概念上是非常简单，比较容易理解的，但它的实现过程却相对比较难。简单理解就是我们要把数字化的控制系统，通过特定经验的公式计算实现为模拟化的控制系统，输入经验值不一样，对应的公式也不一样，控制结果肯定也不太一样。当然经过科学家和前线工程师们的几十年的经验积累，模糊控制也取得了非常多的成就，目前它常被用于智能运算、建构专家控制系统、和类神经网络等应用，在整个儿智能化控制领域有着举足轻重的意义。

![模糊控制理论简图](https://files.mdnice.com/user/38598/392b63ec-138f-4d88-8dfe-da23128ec931.png)

## 模糊控制实现过程
- 确定输入变量和输出变量

根据实际控制系统和控制要求,确定模糊控制器的输入变量和输出变量。输入变量通常是系统状态,输出变量是控制指令。

- 定义输入输出变量的语言词及隶属函数
为每个输入输出变量定义适当的语言词,比如“误差”的语言词可以定为“负大”“负小”“零”“正小”“正大”。并为每个语言词确定隶属函数,如三角函数或梯形函数等。

- 建立模糊控制规则

根据对系统的控制经验,建立输入变量和输出变量之间的如果-则形式的模糊控制规则。如“如果误差是正大,则输出是增大”。

- 进行模糊推理

对当前的输入变量值,根据控制规则进行模糊推理,得到语言形式的输出值,常用Mamdani推理方法。

![Mamdani模型“形象”](https://files.mdnice.com/user/38598/83b9e7c1-beb5-4e67-abc2-f2adbfd81cb1.png)

- 输出值的清晰化

采用（离散）质心法等清晰化（也称作解模糊化或反模糊化）方法,将语言输出转化为确切的数值输出。

- 转换控制输出

将清晰化后的控制输出传递给执行机构,完成对过程的控制。

- 闭环控制

构建闭环控制系统,以实现对过程的持续稳定控制。

## 模糊PID控制
模糊PID控制就是将模糊控制理论方法融入到PID控制当中去，可以让控制系统实现动态调节参数，从而实现系统的智能化控制。这种做法在一定程度上可以使得原本的PID控制适应范围更广，抗噪能力更强。当然设计复杂度也相对更高。

![模糊PID模型](https://files.mdnice.com/user/38598/1fe60ff7-5987-4b9f-9cf9-03cfa6b39aa0.png)


模糊PID控制过程：
1. 确定系统输入和输出变量

输入变量:误差e和误差变化率ec
输出变量:PID三个参数Kp、Ki、Kd的调整量。

2. 定义语言变量及隶属函数

对输入输出变量定义适当的语言词,如误差的“负大”“负小”等,并确定隶属函数形状。

3. 建立模糊控制规则库

根据PID参数调节经验,建立输入和输出之间的如果-则形式模糊控制规则。

4. 选择模糊推理方法

通常选择Mamdani推理方法,进行规则模糊推理。

5. 输出值的清晰化

采用质心法等方法,得到PID参数的数值输出。

6. PID控制器

将调整后的Kp、Ki、Kd参数输入传统PID控制器,实时控制过程。

7. 闭环控制系统

构建闭环控制系统,持续获取反馈,实现过程变量的稳定控制。

8. 优化和维护

根据控制效果,优化和维护规则库、隶属函数等,改进控制性能。

## 模糊控制特点
相较于传统的控制方法，模糊控制具有非常多的优势。
- 不需要建立精确数学模型

模糊控制基于对专家知识的模拟,不需要建立被控对象的精确数学模型。

- 可以处理非线性系统

传统控制方法对非线性系统效果不佳,而模糊控制可以很好地应用于非线性系统。

- 具有一定的鲁棒性

规则表达带有模糊性,不会因局部参数变化而完全失效。

- 设计方便、易实现

控制策略用语言规则表达,减少复杂的数学计算,软件较易实现。

- 控制效果好

模糊控制的控制质量通常优于传统PID控制。

- 可以利用专家经验

控制规则来源于专家的控制经验,能反映人的控制思维。

- 适应性强

基于反馈调整控制规则,系统可在线进行自适应、自学习、自组织实现自身的优化。

- 用途广泛

可广泛用于工业过程控制、家电、消费电子、汽车等领域。

当然每种控制理论都有优缺点，模糊控制也是一样，它有多少优点相反方向它就会有多少缺点。

相较于传统控制，模糊控制更难进行理论化，系统化的表达与分析，需要更多的数据经验。所以这也容易导致其系统可能不如传统控制稳定，更依赖于设计者的经验或提供的数据丰富程度。可以类比现在流行的各种AI产品，简单来说它们可以看做是一种概率分析，所以性能完美的AI要都有一个庞大的数据模型供它自主学习。

## 模糊控制程序举例
参考代码源自著名开源仓库中的`/shuoyueqishi/fuzzy-PID-controller`，访问不稳定朋友的查看以下内容。

参数及变量声明fuzzy_PID.h文件：
```C
#ifndef FUZZY_PID_H_
#define FUZZY_PID_H_
#include<iostream>
#include<string>
using std::string;
using std::cout;
using std::cin;
using std::endl;
class FuzzyPID
{
public:
	const static int N=7;
private:
	float target;  //系统的控制目标
	float actual;  //采样获得的实际值
	float e;       //误差
	float e_pre_1; //上一次的误差
	float e_pre_2; //上上次的误差
	float de;      //误差的变化率
	float emax;    //误差基本论域上限
	float demax;   //误差辩化率基本论域的上限
	float delta_Kp_max;   //delta_kp输出的上限
	float delta_Ki_max;   //delta_ki输出上限
	float delta_Kd_max;   //delta_kd输出上限
	float Ke;      //Ke=n/emax,量化论域为[-3,-2,-1,0,1,2,3]
	float Kde;     //Kde=n/demax,量化论域为[-3,-2,-1,0,1,2,3]
	float Ku_p;    //Ku_p=Kpmax/n,量化论域为[-3,-2,-1,0,1,2,3]
	float Ku_i;    //Ku_i=Kimax/n,量化论域为[-3,-2,-1,0,1,2,3]
	float Ku_d;    //Ku_d=Kdmax/n,量化论域为[-3,-2,-1,0,1,2,3]
	int Kp_rule_matrix[N][N];//Kp模糊规则矩阵
	int Ki_rule_matrix[N][N];//Ki模糊规则矩阵
	int Kd_rule_matrix[N][N];//Kd模糊规则矩阵
	string mf_t_e;       //e的隶属度函数类型
	string mf_t_de;      //de的隶属度函数类型
	string mf_t_Kp;      //kp的隶属度函数类型
	string mf_t_Ki;      //ki的隶属度函数类型
	string mf_t_Kd;      //kd的隶属度函数类型
	float *e_mf_paras; //误差的隶属度函数的参数
	float *de_mf_paras;//误差的偏差隶属度函数的参数
	float *Kp_mf_paras; //kp的隶属度函数的参数
	float *Ki_mf_paras; //ki的隶属度函数的参数
	float *Kd_mf_paras; //kd的隶属度函数的参数
	float Kp;
	float Ki;
	float Kd;
	float A;
	float B;
	float C;
	void showMf(const string & type,float *mf_paras);      //显示隶属度函数的信息
	void setMf_sub(const string & type,float *paras,int n);//设置模糊隶属度函数的子函数
public:
	FuzzyPID(float e_max,float de_max,float kp_max,float ki_max,float kd_max,float Kp0,float Ki0,float Kd0);
	FuzzyPID(float *fuzzyLimit,float *pidInitVal);
	~FuzzyPID();
	float trimf(float x,float a,float b,float c);          //三角隶属度函数
	float gaussmf(float x,float ave,float sigma);          //正态隶属度函数
	float trapmf(float x,float a,float b,float c,float d); //梯形隶属度函数
	void setMf(const string & mf_type_e,float *e_mf,
			   const string & mf_type_de,float *de_mf,
			   const string & mf_type_Kp,float *Kp_mf,
		       const string & mf_type_Ki,float *Ki_mf,
			   const string & mf_type_Kd,float *Kd_mf);	//设置模糊隶属度函数的参数
	void setRuleMatrix(int kp_m[N][N],int ki_m[N][N],int kd_m[N][N]);  //设置模糊规则
	float realize(float t,float a);              //实现模糊控制
	void showInfo();                                      //显示该模糊控制器的信息


};

#endif
```

控制实现fuzzy_PID.cpp文件：
```C

#include"fuzzy_PID.h"


FuzzyPID::FuzzyPID(float e_max,float de_max,float kp_max,float ki_max,float kd_max,float Kp0,float Ki0,float Kd0):
target(0),actual(0),emax(e_max),demax(de_max),delta_Kp_max(kp_max),delta_Ki_max(ki_max),delta_Kd_max(kd_max),e_mf_paras(NULL),de_mf_paras(NULL),
Kp_mf_paras(NULL),Ki_mf_paras(NULL),Kd_mf_paras(NULL)
{
   e=target-actual;
   e_pre_1=0;
   e_pre_2=0;
   de=e-e_pre_1;
   Ke=(N/2)/emax;
   Kde=(N/2)/demax;
   Ku_p=delta_Kp_max/(N/2);
   Ku_i=delta_Ki_max/(N/2);
   Ku_d=delta_Kd_max/(N/2);
   mf_t_e="No type";
   mf_t_de="No type";
   mf_t_Kp="No type";
   mf_t_Ki="No type";
   mf_t_Kd="No type";
   Kp=Kp0;
   Ki=Ki0;
   Kd=Kd0;
   A=Kp+Ki+Kd;
   B=-2*Kd-Kp;
   C=Kd;
}

FuzzyPID::FuzzyPID(float *fuzzyLimit,float *pidInitVal)
{
	target=0;
	actual=0;
	e=0;
	e_pre_1=0;
    e_pre_2=0;
    de=e-e_pre_1;
	emax=fuzzyLimit[0];
	demax=fuzzyLimit[1];
	delta_Kp_max=fuzzyLimit[2];
	delta_Ki_max=fuzzyLimit[3];
	delta_Kd_max=fuzzyLimit[4];
	Ke=(N/2)/emax;
    Kde=(N/2)/demax;
    Ku_p=delta_Kp_max/(N/2);
    Ku_i=delta_Ki_max/(N/2);
    Ku_d=delta_Kd_max/(N/2);
    mf_t_e="No type";
    mf_t_de="No type";
    mf_t_Kp="No type";
    mf_t_Ki="No type";
    mf_t_Kd="No type";
	e_mf_paras=NULL;
	de_mf_paras=NULL;
	Kp_mf_paras=NULL;
	Ki_mf_paras=NULL;
	Kd_mf_paras=NULL;

    Kp=pidInitVal[0];
    Ki=pidInitVal[1];
    Kd=pidInitVal[2];
    A=Kp+Ki+Kd;
    B=-2*Kd-Kp;
    C=Kd;
}

FuzzyPID::~FuzzyPID()
{
  delete [] e_mf_paras;
  delete [] de_mf_paras;
  delete [] Kp_mf_paras;
  delete [] Ki_mf_paras;
  delete [] Kd_mf_paras;
}
//三角隶属度函数
float FuzzyPID::trimf(float x,float a,float b,float c)
{
   float u;
   if(x>=a&&x<=b)
	   u=(x-a)/(b-a);
   else if(x>b&&x<=c)
	   u=(c-x)/(c-b);
   else
	   u=0.0;
   return u;

}
//正态隶属度函数
float FuzzyPID::gaussmf(float x,float ave,float sigma) 
{
	float u;
	if(sigma<0)
	{
	   cout<<"In gaussmf, sigma must larger than 0"<<endl;
	}
	u=exp(-pow(((x-ave)/sigma),2));
	return u;
}
//梯形隶属度函数
float FuzzyPID::trapmf(float x,float a,float b,float c,float d)
{
    float u;
	if(x>=a&&x<b)
		u=(x-a)/(b-a);
	else if(x>=b&&x<c)
        u=1;
	else if(x>=c&&x<=d)
		u=(d-x)/(d-c);
	else
		u=0;
	return u;
}
//设置模糊规则Matrix
void FuzzyPID::setRuleMatrix(int kp_m[N][N],int ki_m[N][N],int kd_m[N][N])
{
	for(int i=0;i<N;i++)
	   for(int j=0;j<N;j++)
	   {
		   Kp_rule_matrix[i][j]=kp_m[i][j];
		   Ki_rule_matrix[i][j]=ki_m[i][j];
		   Kd_rule_matrix[i][j]=kd_m[i][j];
	   }
}
//设置模糊隶属度函数的子函数
void FuzzyPID::setMf_sub(const string & type,float *paras,int n)
{
	int N_mf_e,N_mf_de,N_mf_Kp,N_mf_Ki,N_mf_Kd;
  switch(n)
  {
  case 0:
	  if(type=="trimf"||type=="gaussmf"||type=="trapmf")
	    mf_t_e=type;
	  else
		cout<<"Type of membership function must be \"trimf\" or \"gaussmf\" or \"trapmf\""<<endl;
      if(mf_t_e=="trimf")
        N_mf_e=3;
	  else if(mf_t_e=="gaussmf")
		N_mf_e=2;
	  else if(mf_t_e=="trapmf")
		N_mf_e=4;
       
	  e_mf_paras=new float [N*N_mf_e];
	  for(int i=0;i<N*N_mf_e;i++)
		e_mf_paras[i]=paras[i];
	  break;

  case 1:
	  if(type=="trimf"||type=="gaussmf"||type=="trapmf")
	    mf_t_de=type;
	  else
		cout<<"Type of membership function must be \"trimf\" or \"gaussmf\" or \"trapmf\""<<endl;
      if(mf_t_de=="trimf")
        N_mf_de=3;
	  else if(mf_t_de=="gaussmf")
		N_mf_de=2;
	  else if(mf_t_de=="trapmf")
		N_mf_de=4;
        de_mf_paras=new float [N*N_mf_de];
	  for(int i=0;i<N*N_mf_de;i++)
		de_mf_paras[i]=paras[i];
	  break;

   case 2:
	  if(type=="trimf"||type=="gaussmf"||type=="trapmf")
	    mf_t_Kp=type;
	  else
		cout<<"Type of membership function must be \"trimf\" or \"gaussmf\" or \"trapmf\""<<endl;
      if(mf_t_Kp=="trimf")
        N_mf_Kp=3;
	  else if(mf_t_Kp=="gaussmf")
		N_mf_Kp=2;
	  else if(mf_t_Kp=="trapmf")
		N_mf_Kp=4;
        Kp_mf_paras=new float [N*N_mf_Kp];
	  for(int i=0;i<N*N_mf_Kp;i++)
		Kp_mf_paras[i]=paras[i];
	  break;

   case 3:
	  if(type=="trimf"||type=="gaussmf"||type=="trapmf")
	    mf_t_Ki=type;
	  else
		cout<<"Type of membership function must be \"trimf\" or \"gaussmf\" or \"trapmf\""<<endl;
      if(mf_t_Ki=="trimf")
        N_mf_Ki=3;
	  else if(mf_t_Ki=="gaussmf")
		N_mf_Ki=2;
	  else if(mf_t_Ki=="trapmf")
		N_mf_Ki=4;
        Ki_mf_paras=new float [N*N_mf_Ki];
	  for(int i=0;i<N*N_mf_Ki;i++)
		Ki_mf_paras[i]=paras[i];
	  break;

   case 4:
	  if(type=="trimf"||type=="gaussmf"||type=="trapmf")
	    mf_t_Kd=type;
	  else
		cout<<"Type of membership function must be \"trimf\" or \"gaussmf\" or \"trapmf\""<<endl;
      if(mf_t_Kd=="trimf")
        N_mf_Kd=3;
	  else if(mf_t_Kd=="gaussmf")
		N_mf_Kd=2;
	  else if(mf_t_Kd=="trapmf")
		N_mf_Kd=4;
        Kd_mf_paras=new float [N*N_mf_Kd];
	  for(int i=0;i<N*N_mf_Kd;i++)
		Kd_mf_paras[i]=paras[i];
	  break;

   default: break;
  }
}
//设置模糊隶属度函数的类型和参数
void FuzzyPID::setMf(const string & mf_type_e,float *e_mf,
			const string & mf_type_de,float *de_mf,
			const string & mf_type_Kp,float *Kp_mf,
		    const string & mf_type_Ki,float *Ki_mf,
			const string & mf_type_Kd,float *Kd_mf)
{
	setMf_sub(mf_type_e,e_mf,0);
	setMf_sub(mf_type_de,de_mf,1);
	setMf_sub(mf_type_Kp,Kp_mf,2);
	setMf_sub(mf_type_Ki,Ki_mf,3);
	setMf_sub(mf_type_Kd,Kd_mf,4);
}
//实现模糊控制
float FuzzyPID::realize(float t,float a)   
{
	float u_e[N],u_de[N],u_u[N];
	int u_e_index[3],u_de_index[3];//假设一个输入最多激活3个模糊子集
	float delta_Kp,delta_Ki,delta_Kd;
	float delta_u;
	target=t;
	actual=a;
    e=target-actual;
	de=e-e_pre_1;
	e=Ke*e;
	de=Kde*de;
  /* 将误差e模糊化*/
	int j=0;
	for(int i=0;i<N;i++)
	{
		if(mf_t_e=="trimf")
		  u_e[i]=trimf(e,e_mf_paras[i*3],e_mf_paras[i*3+1],e_mf_paras[i*3+2]);//e模糊化，计算它的隶属度
		else if(mf_t_e=="gaussmf")
		  u_e[i]=gaussmf(e,e_mf_paras[i*2],e_mf_paras[i*2+1]);//e模糊化，计算它的隶属度
		else if(mf_t_e=="trapmf")
		  u_e[i]=trapmf(e,e_mf_paras[i*4],e_mf_paras[i*4+1],e_mf_paras[i*4+2],e_mf_paras[i*4+3]);//e模糊化，计算它的隶属度

		if(u_e[i]!=0)
            u_e_index[j++]=i;                //存储被激活的模糊子集的下标，可以减小计算量
  	}
	for(;j<3;j++)u_e_index[j]=0;             //富余的空间填0

	/*将误差变化率de模糊化*/
	j=0;
	for(int i=0;i<N;i++)
	{
		if(mf_t_de=="trimf")
		   u_de[i]=trimf(de,de_mf_paras[i*3],de_mf_paras[i*3+1],de_mf_paras[i*3+2]);//de模糊化，计算它的隶属度
		else if(mf_t_de=="gaussmf")
		   u_de[i]=gaussmf(de,de_mf_paras[i*2],de_mf_paras[i*2+1]);//de模糊化，计算它的隶属度
		else if(mf_t_de=="trapmf")
		   u_de[i]=trapmf(de,de_mf_paras[i*4],de_mf_paras[i*4+1],de_mf_paras[i*4+2],de_mf_paras[i*4+3]);//de模糊化，计算它的隶属度

		if(u_de[i]!=0)
			u_de_index[j++]=i;            //存储被激活的模糊子集的下标，可以减小计算量
	}
	for(;j<3;j++)u_de_index[j]=0;          //富余的空间填0

	float den=0,num=0;
	/*计算delta_Kp和Kp*/
	for(int m=0;m<3;m++)
		for(int n=0;n<3;n++)
		{
		   num+=u_e[u_e_index[m]]*u_de[u_de_index[n]]*Kp_rule_matrix[u_e_index[m]][u_de_index[n]];
		   den+=u_e[u_e_index[m]]*u_de[u_de_index[n]];
		}
	delta_Kp=num/den;
	delta_Kp=Ku_p*delta_Kp;
	if(delta_Kp>=delta_Kp_max)   delta_Kp=delta_Kp_max;
	else if(delta_Kp<=-delta_Kp_max) delta_Kp=-delta_Kp_max;
	Kp+=delta_Kp;
	if(Kp<0)Kp=0;
	/*计算delta_Ki和Ki*/
	den=0;num=0;
	for(int m=0;m<3;m++)
		for(int n=0;n<3;n++)
		{
		   num+=u_e[u_e_index[m]]*u_de[u_de_index[n]]*Ki_rule_matrix[u_e_index[m]][u_de_index[n]];
		   den+=u_e[u_e_index[m]]*u_de[u_de_index[n]];
		}

	delta_Ki=num/den;
	delta_Ki=Ku_i*delta_Ki;
	if(delta_Ki>=delta_Ki_max)   delta_Ki=delta_Ki_max;
	else if(delta_Ki<=-delta_Ki_max)  delta_Ki=-delta_Ki_max;
	Ki+=delta_Ki;
	if(Ki<0)Ki=0;
	/*计算delta_Kd和Kd*/
	den=0;num=0;
	for(int m=0;m<3;m++)
		for(int n=0;n<3;n++)
		{
		   num+=u_e[u_e_index[m]]*u_de[u_de_index[n]]*Kd_rule_matrix[u_e_index[m]][u_de_index[n]];
		   den+=u_e[u_e_index[m]]*u_de[u_de_index[n]];
		}
	delta_Kd=num/den;
	delta_Kd=Ku_d*delta_Kd;
	if(delta_Kd>=delta_Kd_max)   delta_Kd=delta_Kd_max;
	else if(delta_Kd<=-delta_Kd_max) delta_Kd=-delta_Kd_max;
	Kd+=delta_Kd;
	if(Kd<0)Kd=0;

	A=Kp+Ki+Kd;
    B=-2*Kd-Kp;
    C=Kd;
	delta_u=A*e+B*e_pre_1+C*e_pre_2;

	delta_u=delta_u/Ke;
  
	if(delta_u>=0.95*target)delta_u=0.95*target;
	else if(delta_u<=-0.95*target)delta_u=-0.95*target;

	e_pre_2=e_pre_1;
    e_pre_1=e;

	return delta_u;
}
void FuzzyPID::showMf(const string & type,float *mf_paras)
{
    int tab;
	if(type=="trimf")
		tab=2;
	else if(type=="gaussmf")
		tab==1;
	else if(type=="trapmf")
		tab=3;
	cout<<"函数类型："<<mf_t_e<<endl;
	cout<<"函数参数列表："<<endl;
	float *p=mf_paras;
	for(int i=0;i<N*(tab+1);i++)
	  {
		  cout.width(3);
	      cout<<p[i]<<"  ";
		  if(i%(tab+1)==tab)
			  cout<<endl;
	  }
}
void FuzzyPID::showInfo()
{
   cout<<"Info of this fuzzy controller is as following:"<<endl;
   cout<<"基本论域e：["<<-emax<<","<<emax<<"]"<<endl;
   cout<<"基本论域de：["<<-demax<<","<<demax<<"]"<<endl;
   cout<<"基本论域delta_Kp：["<<-delta_Kp_max<<","<<delta_Kp_max<<"]"<<endl;
   cout<<"基本论域delta_Ki：["<<-delta_Ki_max<<","<<delta_Ki_max<<"]"<<endl;
   cout<<"基本论域delta_Kd：["<<-delta_Kd_max<<","<<delta_Kd_max<<"]"<<endl;
   cout<<"误差e的模糊隶属度函数参数："<<endl;
   showMf(mf_t_e,e_mf_paras);
   cout<<"误差变化率de的模糊隶属度函数参数："<<endl;
   showMf(mf_t_de,de_mf_paras);
   cout<<"delta_Kp的模糊隶属度函数参数："<<endl;
   showMf(mf_t_Kp,Kp_mf_paras);
   cout<<"delta_Ki的模糊隶属度函数参数："<<endl;
   showMf(mf_t_Ki,Ki_mf_paras);
   cout<<"delta_Kd的模糊隶属度函数参数："<<endl;
   showMf(mf_t_Kd,Kd_mf_paras);
   cout<<"模糊规则表："<<endl;
   cout<<"delta_Kp的模糊规则矩阵"<<endl;
   for(int i=0;i<N;i++)
   {
	 for(int j=0;j<N;j++)
	   {
		 cout.width(3);
		 cout<<Kp_rule_matrix[i][j]<<"  ";
	    }
	   cout<<endl;
   }
   cout<<"delta_Ki的模糊规则矩阵"<<endl;
   for(int i=0;i<N;i++)
   {
	 for(int j=0;j<N;j++)
	   {
		 cout.width(3);
		 cout<<Ki_rule_matrix[i][j]<<"  ";
	    }
	   cout<<endl;
   }
   cout<<"delta_Kd的模糊规则矩阵"<<endl;
   for(int i=0;i<N;i++)
   {
	 for(int j=0;j<N;j++)
	   {
		 cout.width(3);
		 cout<<Kd_rule_matrix[i][j]<<"  ";
	    }
	   cout<<endl;
   }
   cout<<endl;
   cout<<"误差的量化比例因子Ke="<<Ke<<endl;
   cout<<"误差变化率的量化比例因子Kde="<<Kde<<endl;
   cout<<"输出的量化比例因子Ku_p="<<Ku_p<<endl;
   cout<<"输出的量化比例因子Ku_i="<<Ku_i<<endl;
   cout<<"输出的量化比例因子Ku_d="<<Ku_d<<endl;
   cout<<"设定目标target="<<target<<endl;
   cout<<"误差e="<<e<<endl;
   cout<<"Kp="<<Kp<<endl;
   cout<<"Ki="<<Ki<<endl;
   cout<<"Kd="<<Kd<<endl;
   cout<<endl;
}
```
举例应用main.c文件：
```C
#include<iostream>
#include"fuzzy_PID.h"

#define NB -3
#define NM -2
#define NS -1
#define ZO 0
#define PS 1
#define PM 2
#define PB 3

int main()
{
	float target=600;
	float actual=0;
	float u=0;
	int deltaKpMatrix[7][7]={{PB,PB,PM,PM,PS,ZO,ZO},
	                         {PB,PB,PM,PS,PS,ZO,NS},
						     {PM,PM,PM,PS,ZO,NS,NS},
	                         {PM,PM,PS,ZO,NS,NM,NM},
	                         {PS,PS,ZO,NS,NS,NM,NM},
	                         {PS,ZO,NS,NM,NM,NM,NB},
	                         {ZO,ZO,NM,NM,NM,NB,NB}};
	int deltaKiMatrix[7][7]={{NB,NB,NM,NM,NS,ZO,ZO},
	                         {NB,NB,NM,NS,NS,ZO,ZO},
						     {NB,NM,NS,NS,ZO,PS,PS},
	                         {NM,NM,NS,ZO,PS,PM,PM},
	                         {NM,NS,ZO,PS,PS,PM,PB},
	                         {ZO,ZO,PS,PS,PM,PB,PB},
	                         {ZO,ZO,PS,PM,PM,PB,PB}};
	int deltaKdMatrix[7][7]={{PS,NS,NB,NB,NB,NM,PS},
	                         {PS,NS,NB,NM,NM,NS,ZO},
						     {ZO,NS,NM,NM,NS,NS,ZO},
	                         {ZO,NS,NS,NS,NS,NS,ZO},
	                         {ZO,ZO,ZO,ZO,ZO,ZO,ZO},
	                         {PB,NS,PS,PS,PS,PS,PB},
	                         {PB,PM,PM,PM,PS,PS,PB}};
	float e_mf_paras[]={-3,-3,-2,-3,-2,-1,-2,-1,0,-1,0,1,0,1,2,1,2,3,2,3,3};
	float de_mf_paras[]={-3,-3,-2,-3,-2,-1,-2,-1,0,-1,0,1,0,1,2,1,2,3,2,3,3};
	float Kp_mf_paras[]={-3,-3,-2,-3,-2,-1,-2,-1,0,-1,0,1,0,1,2,1,2,3,2,3,3};
	float Ki_mf_paras[]={-3,-3,-2,-3,-2,-1,-2,-1,0,-1,0,1,0,1,2,1,2,3,2,3,3};
	float Kd_mf_paras[]={-3,-3,-2,-3,-2,-1,-2,-1,0,-1,0,1,0,1,2,1,2,3,2,3,3};
    FuzzyPID fuzzypid(1500,650,0.3,0.4,0.2,0.02,0.65,0.005);
	fuzzypid.setMf("trimf",e_mf_paras,"trimf",de_mf_paras,"trimf",Kp_mf_paras,"trimf",Ki_mf_paras,"trimf",Kd_mf_paras);
	fuzzypid.setRuleMatrix(deltaKpMatrix,deltaKiMatrix,deltaKdMatrix);
	cout<<"num target    actual"<<endl;
	/*fuzzy.showInfo();*/
	for(int i=0;i<200;i++)
	{
		u=fuzzypid.realize(target,actual);
		actual+=u;
		cout<<i<<"   "<<target<<"    "<<actual<<endl;
	}
	fuzzypid.showInfo();
	system("pause");
	return 0;
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
