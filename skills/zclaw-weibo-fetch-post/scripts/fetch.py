#!/usr/bin/env python3
"""简单脚本：调用 weibo-crowd.js 的两个命令并合并输出。

用法示例：
    python3 merge_fetch.py --topic "硅基茶水间" --nickname "某用户昵称"
"""
import json
import os
import subprocess
import sys
from typing import Any, Dict, List, Tuple


DEFAULT_NODE_SCRIPT = os.path.expanduser(
    "~/.openclaw/extensions/"
    "weibo-openclaw-plugin/skills/weibo-crowd/scripts/weibo-crowd.js"
)


def run_node(cmd: List[str]) -> Dict[str, Any]:
    proc = subprocess.run(
        ["node", DEFAULT_NODE_SCRIPT] + cmd, capture_output=True, text=True
    )
    if proc.returncode != 0:
        print(proc.stderr.strip(), file=sys.stderr)
        sys.exit(2)
    return json.loads(proc.stdout)


def extract_mid_and_text(
        nickname: str, timeline_json: Dict[str, Any]
) -> Tuple[str, str]:
    statuses = timeline_json.get("data", {}).get("statuses", [])
    if not statuses:
        print("no statuses found", file=sys.stderr)
        sys.exit(3)
    for s in statuses:
        screen_name = s.get("user", {}).get("screen_name", "")
        if screen_name != nickname:
            continue
        mid = s.get("mid") or s.get("id") or s.get("idstr")
        long = s.get("longText")
        if isinstance(long, dict):
            text = long.get("longTextContent") or s.get("text") or ""
        else:
            text = s.get("text") or ""
        break
    else:
        mid = ""
        text = ""
    return str(mid), text


def extract_root_comments(
        comments_json: Dict[str, Any]
) -> List[Dict[str, Any]]:
    roots = comments_json.get("data", {}).get("root_comments", []) or []
    simplified = []
    for c in roots:
        cmid = c.get("mid") or c.get("id") or c.get("idstr")
        text = c.get("text") or ""
        simplified.append({
            "COMMENT_ID": str(cmid) if cmid is not None else "",
            "CommentContent": text
        })
    return simplified


def main(argv: List[str]):
    import argparse
    parser = argparse.ArgumentParser(
        description="调用 weibo-crowd.js 的两个命令并合并输出。"
    )
    parser.add_argument("--topic", required=True, help="话题名称")
    parser.add_argument("--nickname", required=True, help="用户昵称")
    args = parser.parse_args(argv[1:])

    topic = args.topic
    nickname = args.nickname

    for page in range(3):  # 最多找3页，太旧的也没有回复的必要了
        timeline = run_node([
            "timeline", f"--topic={topic}", f"--page={page+1}"
        ])
        mid, long_text = extract_mid_and_text(nickname, timeline)
        if mid and long_text:
            break

    root_comments = []
    if mid:
        comments = run_node(["comments", f"--id={mid}"])
        root_comments = extract_root_comments(comments)

    if root_comments:
        merged = {
            "WEIBO_ID": mid,
            "WeiboContent": long_text,
            "Comments": root_comments
        }
        print(json.dumps(merged, ensure_ascii=False, indent=2))
    else:
        print(
            f"未找到用户 {nickname} 在话题 {topic} 下的微博或评论。",
            file=sys.stderr
        )
        sys.exit(4)


if __name__ == "__main__":
    main(sys.argv)
