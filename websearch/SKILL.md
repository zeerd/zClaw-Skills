---
name: websearch
description: "Search web content using Bing search engine. Use when: user asks to search the web, find information online, look up topics, research subjects, or find websites. Searches via https://cn.bing.com/search?q=<keyword> format."
---

# Web Search Skill

Search the web using Bing search engine.

## When to Use

✅ **USE this skill when:**

- "Search for [topic]"
- "Find information about [subject]"
- "What's [news/event]?"
- "Look up [product/service]"
- "Research [topic]"
- "Where can I find [information]?"

## Search Format

### Basic Search

```bash
curl -s "https://cn.bing.com/search?q=<keyword>"
```

### Example Searches

```bash
# Technology news
curl -s "https://cn.bing.com/search?q=AI+latest+news+2024"

# Product research
curl -s "https://cn.bing.com/search?q=best+laptop+for+programming"

# How-to queries
curl -s "https://cn.bing.com/search?q=how+to+install+Python+on+Ubuntu"
```

### Search Tips

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
