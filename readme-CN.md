# notion-toc

一个利用Notion第三方API为页面生成目录的工具。

## 安装环境

```
pip install notion
```

## 运行脚本

首先在浏览器页面下按F12打开开发者模式，切换到Network选项卡，地址栏输入`notion.so`打开，打开后选中`www.notion.so`项目，在cookies中复制出`token_v2`的值，并放入`token_v2.txt`文件中。然后运行脚本：

```
python notion_toc.py
```

按照脚本提示进行即可。