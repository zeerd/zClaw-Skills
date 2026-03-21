---
name: zclaw-prompt-to-image
description: 文生图。基于文本生成图片。基于提示词生成图片。调用 Comfy UI 将输入的提示词转换成一张图片。
---

# 文生图

## 🚨 执行前必读

- ✅ **venv**: 使用`~/.openclaw/workspace/.venv/bin/activate`环境执行脚本

## 功能说明

将任意输入内容输出成一张图片。

**确定内容**
    - 用户提供链接 → 我会提取网页正文内容
    - 用户提供了文字 → 我会直接使用这些文字内容

## 使用流程

1. **确定命名**：将提示词总结成一个简短的“名称前缀”或者直接使用用户指定的“名称前缀”。
2. **输出图片**: 调用`scripts/generate.py`，使用提示词生成图片，保存在指定输出文件夹中。文件名为：名称前缀.png，如“如何学习Python.png”。
  - 当触发此技能时，请直接执行 `scripts/generate.py` 脚本，并将用户的请求作为参数传递给脚本。不要尝试自己编写新脚本。

不要停下来询问，直接输出图片，除非用户特别要求分步展示或需要调整提示词细节。

## 输出路径

工作区下的`comfyui_outputs`路径，即`$WORKSPACE/comfyui_outputs`。

如： `~/.openclaw/workspace/comfyui_outputs`

## 使用方式

`scripts/generate.py` — 调用  Comfy UI API 生成图片的脚本

调用方式：
```bash
python3 ~/.openclaw/workspace/skills/zclaw-prompt-to-image/scripts/generate.py --prompt <提示词> --output <输出文件夹> --negative_prompt <负面提示词> --image_name <图片名称.png>
```

注意：先确认`COMFY_UI_IP`和`COMFY_UI_PORT`环境变量已经正确配置，脚本才能成功调用 Comfy UI API 生成图片。
