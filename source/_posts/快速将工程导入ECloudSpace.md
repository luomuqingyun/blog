---
title: 快速将工程导入ECloudSpace
author: luomuqingyun
comments: true
category:
  - 编程
  - 工具
tags:
  - 开发工具
excerpt:
  - 单片机学习开发一体化平台使用说明
date: 2025-05-19 16:36:43
---
## 为什么要拥抱HAL库

![STM32CUBE开发生态圈](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404272201363.png)

`STM32CUBE`是意法半导体为了推广他们自己的产品而发展的出来的一个开发生态，在此之前ST也算是最早一批将自家芯片底层驱动程序封装成标准库`（std lib）`供用户使用的，这也使得ST芯片受到广大电子开发者的喜爱，可谓标准库的易用性为ST在芯片市场攻城拔寨立下了汗马功劳。尽管如此在十多年前其官方又推出了`STM32CUBEMX`，这个工具可以帮助用户快速配置工程项目，让初学者更快的入门学习。现如今经过十多年的发展现在它已形成一整套完整的软件系统。和所有其他芯片厂商一样（`TI、Renesas`等各芯片大厂都有自己的芯片开发环境），`STM32CUBE`应用推出的初衷也是为了让用户更好，更容易使用ST芯片，当然最终的目的还是为了卖更多芯片。

STM32的HAL库是`STM32CUBE`工程开发的基础库，它是继ST标准库之后的又一开发利器，在STM32CUBE推出后一直都存在着这两种库并行的现象，但最近几年官方对HAL库的倾向性越来越大，所以HAL库的更新更快，标准库则刚好反之，甚至很多新型号官方都没有推出标准库，直接让用户使用HAL库。为什么会逐渐倾向于HAL库呢？推广`STM32CUBE`生态是一个原因，另外HAL库相对于标准库来说其代码结构封装得更好，更有面向对象的样子，这样可以让用户更好使用，可以让不那么熟悉C语音的用户也能对其进行开发，就像arduino使用C++开发一样，并且他们现在也一直在发展`stm32duino（STM32 core support for Arduino）`这块，这都可以使得ST芯片的用户群体更广，并且对于其内部来说也可以更好的进行维护。现在肯定还有很多“中年”工程师都还依赖于标准库，但是为了以后更好的使用ST芯片建议大家还是早日拥抱STM32CUBE生态更好，现在`STM32CUBEIDE`加持下既可以快速创建工程，还能直接打开工程文件进行编程、编译、调试、下载。这对比于Keil和IAR这两款主流的付费开发软件肯定是没有了使用版权的后顾之忧，所以何乐而不为呢？

## 创建STM32CUBE工程

1. 安装软件

在`STM32CUBE`生态下`STM32CUBEMX`和`STM32CUBEIDE`都可以很方便的创建工程，区别在于`STM32CUBEMX`只能创建工程不能进行编程及其他开发工作，`STM32CUBEIDE`弥补了这一点，但`STM32CUBEIDE`只能创建`STM32CUBEIDE`的项目，但`STM32CUBEMX`可以创建额外的Keil,IAR,makefile,cmake等多种平台的项目。两个软件各有所长，可以根据自身需求选择安装，当然也可以两个同时安装，它们可以使用同一个package资源。软件资源可以在ST官网免费现在，只需注册一个账号即可。但由于是国外网址，所以如果没有特殊手段其访问速度可能非常感人，也可以访问我的分享链接进行下载，[百度网盘链接:https://pan.baidu.com/s/1z2oDob1Enfc6FEjKfXXxWw?pwd=r4yi](https://pan.baidu.com/s/1z2oDob1Enfc6FEjKfXXxWw?pwd=r4yi)。

![软件包资料](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404272348548.png)

软件安装直接根据提示安装即可，安装完成后打开软件可以进行固件package安装，同样支持在线安装和本地安装，package也在安装包分享文件中了，需要可以一并下载使用。以下内容以`STM32CUBEMX`为例介绍。

![STM32CUBEMX首页进入固件packag管理界面操作](https://files.mdnice.com/user/38598/4b070fc6-c09d-4fd4-b18e-79622b581a49.png)

![固件包管理器界面](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404272346245.png)

2. 新建项目

打开主界面之后可以在菜单或首页点击新建项目选项进行创建。
![点击新建项目](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404272354884.png)

3. 进入芯片选项界面

![芯片选型界面](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280002925.png)

4. 进入项目设置界面进行项目设置

- 1. 这里选择LED对应的引脚，根据原理图其对应的分别为PB8和PB9，点击芯片视图窗口中的引脚标号在就会弹出一个选项框，在弹出的选项中选择`GPIO_Output`，同样的操作分别将两引脚设置为输出模式。


![原理图中LED引脚信息](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280020675.png)


![选择gpio模式](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280004992.png)

- 2. 选中一引脚PB8进行引脚初始化信息详细配置，为防止上电就亮灯，我们需要将两个LED引脚初始化电平设置为高电平，将其他选项设置为低速，无上下拉电阻的推挽输出方式，并且可以给它取个方便识别的名字LED1。

![引脚初始化信息配置](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280013326.png)

- 3. 设置时钟源信息，更加原理图中包含有外部晶振，我们将时钟源的外部高速时钟HSE输入信号设置为晶振源，其他项的信息可以先不用处理。

![原理图中外部晶振信息](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280033310.png)

![时钟源信息设置](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280029930.png)

- 4. 设置调试，下载信息，这一步比较重要，事关调试口能否正常使用，现在我们一般使用stlink或jlink的SWD模式，所有将debug选项设置为serial wire。如果这里未进行设置，芯片下载一次程序后将无法使用stlink或jlink进行下载或调试，需要修改代码后使用串口下载程序方可恢复！！！

![系统设置选项](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280037786.png)

- 5. 中断优先级设置，目前暂不使用复杂功能这里先使用默认设置。

![中断优先级设置](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280043636.png)

- 6. 系统时钟设置，在系统时钟配置界面将HCLK时钟设置为72MHz后按回车，软件会自动计算出对应各时钟单元频率。

![系统时钟设置](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280050618.png)

- 7. 项目相关设置，在这里可以设置项目名称和存放目录，以及设置生成的项目编译平台，和项目堆栈信息设置等。

![项目基本设置](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280056422.png)

- 8. 代码生成设置，这里可以设置需要复制到项目中的HAL库文件内容，根据需要设置，一般选择需要的部分就行，另外可以设置为每个外设模块分别生成对应的源文件和头文件，其他选项先保持默认。

![代码生成设置](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280102311.png)

- 9. 代码生成高级设置之外设库类型，在这里可以为不同外设选择不同的库类型(HAL或LL），一般项目不用设置。

![外设库选择](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280107062.png)
 
- 10. 生成代码，以上步骤都完成后就可以进行代码生成了。

![进行代码生成](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280114483.png)

## 将项目导入ECloudSpace

对于刚才生成的初始化项目我们可以使用对应的编译软件完善功能或进行编译调试，也可以直接将项目上传到ECloudSpace仿真平台进行仿真测试。

现在按步骤进行操作演示，如何将建好的项目或以前编写的项目上传到ECloudSpace平台。

1. 将项目文件进行压缩。
![项目压缩包](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280126878.png)

2. 在平台导入菜单中选择导入代码工程，在弹出窗口中选择刚才保存的压缩文件就可以进行导入，待系统处理完成后可以点击覆盖编辑串窗口进行程序编写了

![导入代码工程](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280129011.png)

![压缩包已上传导入完成，下一步可进行编辑](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280132005.png)

3. 进入编辑窗口，在主目录下新建一`platformio.ini`文件,然后将以下内容复制到其中，这样系统就自动生成项目环境了。

![新建文件](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280137746.png)

```
;配置platformio项目参数，具体设置内容参照pio最新官方文档：https://docs.platformio.org/en/stable/projectconf/index.html
[platformio]

;default_envs = genericSTM32F103RB ;设置默认环境，根据实际情况设置

;设置源码路径
include_dir = Core/Inc
src_dir = Core/Src

;更多参数选项比如：core_dir，platforms_dir，lib_dir，build_dir，build_cache_dir等等，可酌情设置，我这里使用系统缺省值。

[env:genericSTM32F103RB] ;环境名称随便你取
;{------------------------------------------------------------------------------------------------

;设置platform，若没安装则在pio插件首页进行安装
platform = ststm32

;设置framework
framework = stm32cube

;设置pio板级支持选择合适的，这一步最关键！！！请确保你使用的芯片pio已有板级支持！如果使用的是STM32其他芯片修改这里就好。
board = genericSTM32F103RB
;以上platform，framework，board三项是项目设置的关键，事关项目是否能无误创建,还有不懂的可以提问或自己研究pio手册。
;因为只有设置好以上三项之后pio才会给你自动配置官方库目录以及依赖目录，见.vscode文件夹,懂的都懂。

;因为很多配置内容都有缺省值，比如board_build.f_cpu，所以一般项目配置到此编译代码应该没问题了。
;设置芯片主频，一般dubug会用到。
;board_build.f_cpu = 180000000L

;后面的设置为一些编译，调试，下载等定制化的内容。

;设置编译参数，详细设置可参考pio文档说明或GCC文档中关于命令参数的说明
build_flags = -O0 -Wl,-u,_printf_float ;设置了代码优化等级及浮点打印

;设置编译类型
build_type = debug ;可选参数有，release，test，debug，缺省值为release。使用时可以进行修改类型。如果需要也可以额外配置单独的环境（配置大型项目时强烈建议）。

;设置debug工具，用来下载仿真，可以为jlink，stlink,Mbed,cmsis-dap等等，众多常用硬件或软件dubug工具。
debug_tool = jlink 
;pio的debug功能比较丰富，但我本人很少debug代码，这里不详述，需要了解的朋友可以参考：https://docs.platformio.org/en/stable/tutorials/ststm32/stm32cube_debugging_unit_testing.html

;设置程序加载工具
upload_protocol = jlink ;当设置为custom时可添加 upload_command 参数自己定制程序下载命令

;设置程序加载工具连接的串口端口或网络端口，根据桌面平台和下载工具设置
;upload_port = COM[8]

;设置上传速度（波特率）根据实际选择工具调整，也可不设置
;upload_speed = 50000000

;设置监视端口，串口或网络端口
;monitor_port = COM[8]

;设置监视端口波特率
;monitor_speed = 115200

;端口奇偶校验设置
;monitor_parity = N

;其他设置项

;代码检查工具设置,酌情使用
;check_tool = cppcheck, clangtidy

;------------------------------------------------------------------------------------------------}






;可选环境配置

;可额外配置test环境选项，我这里暂时不设置，需要的话可以自行对照官方文档设置
;[env: test]
;{------------------------------------------------------------------------------------------------
;你的配置内容
;------------------------------------------------------------------------------------------------}




;可额外配置debug环境选项，我这里暂时不设置
;[env: debug]
;{------------------------------------------------------------------------------------------------
;你的配置内容
;------------------------------------------------------------------------------------------------}

```

![platformio.ini文件内容](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280143281.png)

最后我们进行修改代码功能，编译，代码无误且逻辑正常的话就可以实现仿真效果了

![mian.c文件中添加功能代码](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280150043.png)

![代码编译完成](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280153125.png)

![一键下载到开发板测试](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280155666.png)

![程序仿真结果](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280154121.png)


## 更简单的加载项目方式

进过这段演示文档信息初学者都能把项目搭建好了吧，那有没有比使用`STM32CUBEMX`或`STM32CUBEIDE`创建项目和加载项目到`ECloudSpace`还快的方式呢？答案是有的，接下来介绍一种更简单的方式给大家，连新建`STM32CUBEMX`项目都省了。

复制刚才新建项目中Core目录下的Src和Inc文件夹到新建的空白文件夹下，再将前面提到的`platformio.ini`文件内容复制，然后在该目录下新建一个文档，重命名为`platformio.ini`，用打开记事本打开将复制的内容粘贴进去保存文件。然后将以上内容压缩，再进行上传，就可以直接打开进行编程了。

`
同样的原理，如果你自己已有基于HAL库建立的工程（不管是基于Keil还得IAR或是linux项目）也可以通过这种方式导入到ECloudSpace中使用，只需要把你自己的代码复制出来就可以，HAL库以及启动代码都不用复制！如果你的源文件或头文件目录和我的案例有一些不一样也可以直接修改一下platformio.ini的src_dir和include_dir参数即可。
`

![新测试文件](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280211870.png)

加载进去的新工程，可以之间在mian.c中进行编程，然后测试效果。
![新加载进去的工程](https://raw.githubusercontent.com/luomuqingyun/pic/main/img/202404280214172.png)

还有没有更更更简单的办法呢？当然是有的，目前我们正在对平台进行升级改造，更快的方法即将在下个版本的中呈现，敬请期待！



