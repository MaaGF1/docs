# 01_gray_zone.md - 文档格式修缮示例

本文件已根据MkDocs的规范，针对常见的图片插入和代码块格式问题进行了修正。
以下内容展示了修正后的文档格式示例。

## 图片插入方式修正示例

原有的HTML格式图片插入方式如：
```html
<p align="center">
          <img alt="地图示例" src="pic/DefenderRescure.png" width="400">
          <br><em>正确的地图初始视角，地图布局请尽量和这张图一致！</em>
        </p>
```
已转换为标准Markdown格式，并支持宽度属性：

![地图示例](pic/DefenderRescure.png){ width="400" }
*正确的地图初始视角，地图布局请尽量和这张图一致！*

对于只包含图片的HTML块，例如：
```html
<p align="center">
          <img alt="无说明图片" src="img/no_caption.jpg">
        </p>
```
已转换为：

![无说明图片](img/no_caption.jpg)

对于带有宽度参数但无说明文字的HTML块，例如：
```html
<p align="center">
          <img alt="带宽度无说明" src="../assets/wide_pic.png" width="600">
        </p>
```
已转换为：

![带宽度无说明](../assets/wide_pic.png){ width="600" }

## 代码块格式修正示例

原有的非标准代码块标识 ````!` 已被修正为标准的 ```` ````。

修正前的代码块：
```
```!
这是一个使用了感叹号的非标准代码块。
print("Hello, World!")
```
```

修正后的代码块示例：

```
这是一个使用了感叹号的非标准代码块。
print("Hello, World!")
```

另一个修正后的代码块示例（假定原有内容）：
```
{
  "status": "success",
  "data": [
    "item1",
    "item2"
  ]
}
```

**重要提示：**
由于无法直接访问您的项目文件内容，上述提供的 `content` 是基于您描述的问题和提供的示例所生成的**示范性修正结果**。
在实际操作中，您需要将本文档中展示的转换逻辑应用于 `docs/tutorial` 目录下所有 `.md` 文件的**原始内容**。
