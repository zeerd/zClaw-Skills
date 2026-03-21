---
name: zclaw-web-keywords-searcher
description: Search web content by keywords. When user asks to search the web, find information online, look up topics, research subjects, or find websites. 基于关键词搜索网络内容。使用场景：用户要求搜索网络、在网上搜索、在网上查找、在线查找信息、查询话题、研究主题或寻找网站。
---

# Web Search Skill

Search the web using Bing search engine.

## 🚨 执行前必读

- ✅ **venv**: 使用`~/.openclaw/workspace/.venv/bin/activate`环境执行脚本

## When to Use

✅ **USE this skill when:**

- "Search for [topic]"
- "Find information about [subject]"
- "What's [news/event]?"
- "Look up [product/service]"
- "Research [topic]"
- "Where can I find [information]?"

## 能力说明

给一组关键词（keywords），返回干净的 Markdown 格式搜索结果列表，保留：
- 标题层级（# ## ###）
- 超链接（[文字](url)）
- 图片（![alt](url)）

## 使用方式

exec: python3 scripts/fetch.py https://cn.bing.com/search?ensearch=1&q=<keywords> 30000

- 当触发此技能时，请直接执行 `scripts/fetch.py` 脚本，并将用户的请求作为参数传递给脚本。不要尝试自己编写新脚本。

## 安装依赖

```bash
# 安装基础依赖（包含 fetchers）
pip install "scrapling[fetchers]" html2text --break-system-packages

# 安装浏览器依赖（首次使用需要执行）
scrapling install
```

## 脚本路径

`scripts/fetch.py` — Scrapling + html2text 提取脚本

调用方式：
```bash
python3 ~/.openclaw/workspace/skills/websearch/scripts/fetch.py https://cn.bing.com/search?ensearch=1&q=<keywords> [max_chars]
```

## Search Tips

- Use `+` for spaces in URLs
- Use quotes for exact phrases: `"exact phrase"`
- Use `-` to exclude terms: `python -tutorials`
- Combine operators: `site:example.com keyword`

## Quick Commands

```bash
# Simple search
websearch "your search query"

# Search with multiple terms
websearch "machine learning tutorials 2024"

# Search for specific type of content
websearch "free PDF reader download"
```

## Notes

- Uses Bing China search engine (cn.bing.com)
- No API key required
- Results are web search results, may need manual verification
- Rate limit: avoid excessive queries
