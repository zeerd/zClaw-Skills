---
name: zclaw-pdf-reader
description: PDF阅读器技能。用户输入一个PDF文件路径、一些关键字，本技能将会分析PDF文件内容，提取与关键字相关的段落，返回这些段落的文本内容。
---

# PDF Reader Skill


## 🚨 执行前必读

- ✅ **venv**: 使用`~/.openclaw/workspace/.venv/bin/activate`环境执行脚本

## 功能
1. 打开PDF文件
2. 在其中搜索指定的关键字
3. 将找到的关键字所在的章节读取出来
4. 返回PDF名称、这些章节的文本、页码范围
5. 支持读取指定页码范围的所有文本
6. 支持通过 --max-chars 限制返回内容长度

## 脚本用法

```bash
# 按关键字查找章节
python scripts/read-pdf.py search <PDF文件路径> <关键字> [--max-chars 最大字符数]

# 读取指定页码范围
python scripts/read-pdf.py range <PDF文件路径> <起始页码> <结束页码> [--max-chars 最大字符数]
```

不提供“最大字符数”时，将返回完整内容。

## 脚本依赖

```bash
pip install PyPDF2
```

## 示例

```bash
# 查找包含“人工智能”的章节，最多返回300字符
python scripts/read-pdf.py search example.pdf 人工智能 --max-chars 300

# 读取第5到10页全部内容
python scripts/read-pdf.py range example.pdf 5 10

# 读取第1到3页，最多返回500字符
python scripts/read-pdf.py range example.pdf 1 3 --max-chars 500
```
