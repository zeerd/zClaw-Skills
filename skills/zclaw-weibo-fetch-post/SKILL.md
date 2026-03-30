---
name: zclaw-weibo-fetch-post
description: >
  Fetch Weibo posts and comments by topic and user nickname. When user asks to fetch Weibo content, find posts and comments related to a specific topic and user.
  基于超话话题和用户昵称获取微博内容。使用场景：用户要求获取微博内容、查找特定话题下的微博、获取用户的微博和评论。
---

# Weibo Fetch Post and Comments

## 🚨 执行前必读

- ✅ **venv**: 使用`~/.openclaw/workspace/.venv/bin/activate`环境执行脚本

## 能力说明
给定一个话题名称和用户昵称，返回该用户在该话题下的微博内容和根评论。输出格式为 JSON，包含以下字段：
- `WEIBO_ID`: 微博 ID
- `longTextContent`: 微博正文内容
- `root_comments`: 根评论列表，每条评论包含 `COMMENT_ID` 和 `text`

## 使用方式

1. 直接告诉我要获取的用户昵称和话题名称，我会自动调用 weibo-crowd.js 的两个命令并合并输出。例如：
> 获取用户 "张三" 在话题 "硅基茶水间" 下的微博内容和评论。

## 脚本路径

`scripts/merge_fetch.py` — 调用 weibo-crowd.js 的两个命令并合并输出的脚本

调用方式：

```bash
python3 ~/.openclaw/workspace/skills/zclaw-weibo-fetch-post/scripts/merge_fetch.py --topic <话题名称> --nickname <用户昵称>
```

注意：请确保已经正确安装了 `weibo-openclaw-plugin`，并且 `DEFAULT_NODE_SCRIPT` 路径指向正确的脚本文件。
安装命令`openclaw plugins install @wecode-ai/weibo-openclaw-plugin`
