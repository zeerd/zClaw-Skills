#!/home/node/.openclaw/workspace/.venv/bin/python
"""
通用网页正文提取脚本（基于 Scrapling + html2text）
返回 Markdown 格式。

用法：
  python3 fetch.py <url> [max_chars]

示例：
  python3 fetch.py https://example.com/article 12000
  python3 fetch.py https://mp.weixin.qq.com/s/xxx 30000

输出：
  Markdown 格式正文，截断至 max_chars（默认 30000）
  图片使用原始 URL 内嵌在 Markdown 中（data-src 懒加载已自动处理）
"""

import sys
import re
import html2text
from scrapling.fetchers import Fetcher
from playwright.sync_api import sync_playwright


def fix_lazy_images(html_raw):
    """
    微信公众号等平台用 data-src 懒加载图片，src 为占位符。
    将 data-src 的值提升为 src，确保 html2text 能正确渲染图片。
    """
    # 先把 data-src 提升为 src（如果 src 不存在或是占位）
    html_raw = re.sub(
        r'<img([^>]*?)\sdata-src="([^"]+)"([^>]*?)>',
        lambda m: f'<img{m.group(1)} src="{m.group(2)}"{m.group(3)}>',
        html_raw
    )
    return html_raw


def html_to_markdown(html_raw, max_chars=30000):
    """
    把 HTML 转为 Markdown：处理懒加载图片、使用 html2text，并压缩多空行。
    返回截断后的 Markdown 字符串。
    """
    if not html_raw:
        return ''
    try:
        html_raw = fix_lazy_images(html_raw)
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0

        md = h.handle(html_raw)
        md = re.sub(r'\n{3,}', '\n\n', md).strip()
        return md[:max_chars]
    except Exception as e:
        print(f"HTML->Markdown 转换失败: {e}", file=sys.stderr)
        return ''


def weibo_fetch(url, max_chars=30000):
    content = ''
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_load_state("networkidle")

        try:
            # 优先查找 class 包含 "_body_" 的 div；其次回退到 "_full_" 或 data-testid
            content_elem = page.query_selector('div[class*="_body_"]')
            if not content_elem:
                content_elem = page.query_selector('div[class*="_full_"]')
            if not content_elem:
                content_elem = page.query_selector('[data-testid="text"]')

            if content_elem:
                # 获取完整 HTML 内容，保留图片与格式
                content = content_elem.inner_html()
            else:
                content = ""
        except Exception as e:
            print(f"抓取正文失败: {e}", file=sys.stderr)
            content = ""

        # 将 HTML 转为 Markdown（使用封装函数）
        content = html_to_markdown(content, max_chars)
        browser.close()
    return content


def scrapling_fetch(url, max_chars=30000):
    page = Fetcher(auto_match=False).get(
        url,
        headers={
            "Referer": "https://www.google.com/search?q=site",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
        }
    )

    # 微信公众号专用选择器
    if "mp.weixin.qq.com" in url:
        selectors = ["div#js_content", "div.rich_media_content"]
    else:
        selectors = [
            'article',
            'main',
            '.post-content',
            '.entry-content',
            '.article-body',
            '[class*="body"]',
            '[class*="content"]',
            '[class*="article"]',
        ]

    for selector in selectors:
        els = page.css(selector)
        if els:
            md = html_to_markdown(els[0].html_content, max_chars)
            if len(md) > 300:
                return md[:max_chars], selector

    # fallback：全页转 Markdown
    md = html_to_markdown(page.html_content, max_chars)
    return md[:max_chars], 'body(fallback)'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 fetch.py <url> [max_chars]", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    max_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 30000

    text = None
    try:
        if (
            url.startswith("https://weibo.com/") or
            url.startswith("https://www.weibo.com/")
        ):
            text = weibo_fetch(url)
        else:
            text, selector = scrapling_fetch(url, max_chars)
    except Exception as e:
        print(f"Scrapling 提取失败: {e}", file=sys.stderr)
        text = ''

    print(text)
