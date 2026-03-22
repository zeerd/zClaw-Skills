---
name: zclaw-web-keywords-searcher
description: >
  Search web content by keywords. When user asks to search the web, find information online, look up topics, research subjects, or find websites.
  基于关键词搜索网络内容。使用场景：用户要求搜索网络、在网上搜索、在网上查找、在线查找信息、查询话题、研究主题或寻找网站。
---

# Web Search Skill

Search the web using Bing search engine.

## 工作流程

1. 从用户提供的文字中提取关键词
    - 如果用户提供的文字已经是关键词，则直接使用这些关键词
    - 如果用户提供的是一个问题或陈述，则需要从中提取关键词。例如：
      - 用户输入："我想了解一下最新的人工智能发展动态"，则提取关键词为 "最新 人工智能 发展动态"
      - 用户输入："帮我找一下关于Python编程的教程"，则提取关键词为 "Python 编程 教程"
2. 将提取的关键词构造成一个搜索 URL，使用 Bing 搜索引擎进行搜索。例如：
    - 搜索 URL 模板：https://cn.bing.com/search?ensearch=1&q=<keywords>
    - 将提取的关键词替换到 URL 中，形成完整的搜索 URL。例如：
      - 如果提取的关键词是 "最新 人工智能 发展动态"，则搜索 URL 为：https://cn.bing.com/search?ensearch=1&q=最新+人工智能+发展动态
      - 如果提取的关键词是 "Python 编程 教程"，则搜索 URL 为：https://cn.bing.com/search?ensearch=1&q=Python+编程+教程
3. 搜索引擎返回的结果也是一个网页，因此我们可以直接提取网页正文内容。
    - 使用 `fetch_web_content` 工具提取搜索结果页面的正文内容，返回干净的 Markdown 格式搜索结果列表，保留标题、链接、图片 URL、列表结构等信息。
    - 注意：搜索结果是网页内容，可能需要用户手动验证其准确性和相关性。

## 能力说明

给一组关键词（keywords），返回干净的 Markdown 格式搜索结果列表，保留：
- 标题层级（# ## ###）
- 超链接（[文字](url)）
- 图片（![alt](url)）

## Search Tips

- Use `+` for spaces in URLs
- Use quotes for exact phrases: `"exact phrase"`
- Use `-` to exclude terms: `python -tutorials`
- Combine operators: `site:example.com keyword`

## Notes

- Uses Bing China search engine (cn.bing.com)
- No API key required
- Results are web search results, may need manual verification
- Rate limit: avoid excessive queries
