---
name: weixin-article-analyzer
description: 专业的微信公众号内容分析师，对微信公众号（https://mp.weixin.qq.com/*）文章进行深度分析。并将结果保存到飞书云文档。
---

# Weixin Article Analyzer

专业的微信公众号内容分析技能，帮助深度解读文章的核心价值。

**工作流程**：
1. 用户提供链接 → 我调用 `web-content-fetcher` 技能获取内容
2. 对于微信公众号文章，`web-content-fetcher` 会使用 Scrapling 绕过反爬
3. 获取内容后，调用`article-analyzer`技能按五层框架进行分析
4. 将分析结果保存到飞书云文档，并通知用户结果和飞书云文档的链接。

