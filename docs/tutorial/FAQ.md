# 常见问题解答

欢迎来到 MaaGF1 的 FAQ 页面。本文档旨在解决您在使用过程中可能遇到的常见问题。

## 安装与配置

### 为什么我的虚拟显示器无法启动？
有时虚拟显示器启动失败可能与驱动或配置有关。请检查相关日志。

### 图片显示异常？
一些用户反馈文档中的图片无法正常显示，这通常是由于使用了非标准的 HTML 图片插入方式。例如：

![安装引导](assets/faq_install_guide.png)

*请按照此图片所示的引导步骤进行操作，确保您的安装环境配置正确。*

## 脚本使用

### 脚本报错：无效的语法？
如果您的自定义脚本出现语法错误，可能是因为复制粘贴时混入了不规范的代码块标记。请检查：

```python
import os

def get_current_directory():
    """获取当前工作目录"""
    return os.getcwd()

print(f"当前目录: {get_current_directory()}")
```

应确保代码块以三个反引号开始，后接语言类型（如 `python`），而不是 ````!python`。

## 常见问题排查

遇到其他问题时，请查阅我们的 [高级指南](advanced/index.md) 或在 GitHub 仓库中提交 issue。

![排错流程](img/troubleshooting_flow.png)

*典型的故障排除流程图。*

```yaml
# 示例配置文件
settings:
  debug_mode: false
  log_level: info
```
