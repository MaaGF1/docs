# 快速上手 MaaGF1

欢迎来到 MaaGF1！本指南将帮助您快速安装和启动 MaaGF1，从而开始您的自动化之旅。

## 1. 环境准备

在安装 MaaGF1 之前，请确保您的系统满足以下要求：

### 1.1 Python 环境

MaaGF1 需要 Python 3.9 或更高版本。推荐使用 [Python 3.10](https://www.python.org/downloads/)。

您可以访问 [Python 官方网站](https://www.python.org/downloads/) 下载并安装适合您操作系统的 Python 版本。在安装过程中，请务必勾选 "Add Python to PATH" 选项，以便在命令行中直接使用 `python` 和 `pip` 命令。

安装完成后，打开终端或命令提示符，输入以下命令验证 Python 和 pip 是否正确安装：

```bash
python --version
pip --version
```

### 1.2 Git 工具

您需要安装 Git 工具来克隆 MaaGF1 的仓库。

您可以访问 [Git 官方网站](https://git-scm.com/downloads) 下载并安装 Git。安装完成后，在终端或命令提示符中输入以下命令验证 Git 是否正确安装：

```bash
git --version
```

## 2. 安装 MaaGF1

MaaGF1 的安装主要通过克隆仓库和安装依赖完成。

### 2.1 克隆仓库

打开您的终端或命令提示符，选择一个您希望存放 MaaGF1 项目的目录，然后执行以下命令克隆 MaaGF1 仓库：

```bash
git clone https://github.com/MaaGF1/MaaGF1.git
```

这将把 MaaGF1 项目的所有文件下载到当前目录下名为 `MaaGF1` 的文件夹中。

### 2.2 进入项目目录

克隆完成后，进入新创建的 `MaaGF1` 目录：

```bash
cd MaaGF1
```

### 2.3 安装依赖

MaaGF1 依赖于一些第三方库。在项目目录下，执行以下命令安装所有必需的依赖：

```bash
pip install -r requirements.txt
```

如果您遇到网络问题导致安装失败，可以尝试使用国内镜像源：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 3. 运行 MaaGF1

依赖安装成功后，您就可以启动 MaaGF1 了。

在 `MaaGF1` 项目目录下，执行以下命令：

```bash
python main.py
```

MaaGF1 应该会启动，并可能在首次运行时创建一个 `config.json` 文件。

## 4. 初次配置与使用

### 4.1 配置 `config.json`

首次运行后，MaaGF1 会生成一个 `config.json` 文件。您需要根据自己的游戏客户端设置和需求进行一些配置。

-   **ADB 连接**: 如果您使用模拟器或安卓设备，需要配置 ADB 连接信息。确保 ADB 已正确安装并可以连接到您的设备。
-   **虚拟显示器**: 对于无头模式或高性能需求，您可能需要配置虚拟显示器。详细信息请参考 [虚拟显示器配置指南](../advanced/01_virtual_monitor.md)。
-   **游戏路径**: 确保 `config.json` 中配置的游戏路径指向了正确的游戏客户端可执行文件。

### 4.2 连接游戏客户端

MaaGF1 启动后，它会尝试连接到您的游戏客户端。请确保：

-   游戏客户端正在运行。
-   `config.json` 中的设置与您的游戏环境匹配。
-   防火墙或杀毒软件没有阻止 MaaGF1 的连接。

## 5. 遇到问题？

如果在安装或运行过程中遇到任何问题，请：

-   查阅我们的 [常见问题 (FAQ)](../tutorial/FAQ.md)。
-   访问 [MaaGF1 GitHub Issues](https://github.com/MaaGF1/MaaGF1/issues) 寻求帮助或报告问题。

祝您使用愉快！
