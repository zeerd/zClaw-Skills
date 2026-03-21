# 使用

基于提示词生成一张图片

## Comfy UI

基于本地搭建的`Comfy UI`来生成图片。因此，需要配置环境变量来让`Docker`中的脚本访问`Comfy UI`服务。
使用的是经过修改之后的[01_get_started_text_to_image](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/01_get_started_text_to_image.json).

### 配置

手动修改`.openclaw/openclaw.json`文件，或者去配置界面添加：

```jsonl
"skills": {
    "entries": {
        "article-to-cartoon-image": {
            "enabled": true,
            "env": {
                "COMFY_UI_IP": "192.168.1.100",
                "COMFY_UI_PORT": "8188"
            }
        }
    }
},
```
