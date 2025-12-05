# 下载并运行

&emsp;&emsp;本篇文章用于讲述如何下载MaaGFL、启动并运行。

## 一、下载

&emsp;&emsp;在[releases](https://github.com/MaaGF1/MaaGF1/releases)中包含了历史发行版本，其中`latest`标签表示该包为最新稳定版；`Pre-release`表示该包为预发行版。

&emsp;&emsp;以[latest](https://github.com/MaaGF1/MaaGF1/releases/latest)为例，在其页面中`Assets`一栏的`MaaGF1-GUI-vA.B.C-ARCH-.zip`即为发行包。其中：

1. `vA.B.C`对应版本编号，例如`v1.2.3`；
2. `ARCH`为运行平台架构，仅支持`aarch64`或`x86-64`。

## 二、运行

&emsp;&emsp;下载`*.zip`压缩包并解压后，运行其中的`MFAAvalonia.exe`，该程序有如下依赖：

1. `.Net Runtime` > 8.0 (1.7版本)
2. `.Net Runtime` > 10.0 (1.8及以后版本)
3. `VC++` > 14.4

> 在`1.8`之后，`MFAAvalonia`在根目录下添加了一键安装依赖的脚本，`DependencySetup_依赖库安装_win.bat`。

&emsp;&emsp;运行`MFAAvalonia`后，会有如下多个提示：

1. 开始查找窗口；
2. 已选择窗口；
3. 软件(MFAAvalonia)已是最新或有新版本可以更新；
4. 该资源不支持Mirror酱。

&emsp;&emsp;在`MFAAvalonia`中存在多个子窗口：

1. **连接**：确保`当前控制器`所选中的窗口是游戏《少女前线》，**注意**：`MaaGF1 1.8`之后的版本需要在“当前控制器”中手动指定窗口；
2. **资源类型**：目前支持国服和美服；
3. **任务列表**：用于选择MaaGF1中的不同脚本；
4. **任务设置**：用于选择**任务列表**中的脚本子选项，例如选择不同打捞人形等；
5. **任务说明**：关于**任务列表**中所选脚本的简要说明；
6. **日志**：用于查看`MaaFw`或`Agent`的日志信息。

## 三、游戏中设置

&emsp;&emsp;MaaGF1要求游戏配置如下：

1. 窗口模式、`1280x720`；
2. 记录上次完成关卡时镜头缩放