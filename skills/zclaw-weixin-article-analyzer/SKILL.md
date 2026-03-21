---
name: zclaw-weixin-article-analyzer
description: 专业的微信公众号内容分析师，对微信公众号（https://mp.weixin.qq.com/*）文章进行深度分析。并将结果保存到飞书云文档。
---

# Weixin Article Analyzer

专业的微信公众号内容分析技能，帮助深度解读文章的核心价值。

**工作流程**：
1. 用户提供链接 → 我使用 `fetch_web_content` **工具**获取内容
   - 对于微信公众号文章，`fetch_web_content` 会使用 Scrapling 绕过反爬
   - ✗ 禁止使用浏览器自动化工具（如 Playwright）抓取微信公众号文章，因为这会触发反爬机制，导致抓取失败。
   - 注意：这是一个工具，不是技能！直接告诉`fetch_web_content`要读取的 URL，例如：
     - ✓ **正确用法**： "使用`fetch_web_content` **工具**读取这篇文章：https://mp.weixin.qq.com/s/xxx"
     - ✗ **错误用法**： "调用 web_fetch 工具抓取内容..."
2. 获取内容后，调用`zclaw-article-analyzer`技能按五层框架进行分析
3. 将分析结果保存到飞书云文档，并通知用户结果和飞书云文档的链接。
