#!/home/node/.openclaw/workspace/.venv/bin/python
import argparse
import json
import uuid
import websocket
import urllib.request
import urllib.parse
import os


workflow = {
    "58": {
        "inputs": {
            "value": ""
        },
        "class_type": "PrimitiveStringMultiline",
        "_meta": {
            "title": "Prompt（正）"
        }
    },
    "71": {
        "inputs": {
            "value": ""
        },
        "class_type": "PrimitiveStringMultiline",
        "_meta": {
            "title": "Prompt（负）"
        }
    },
    "83": {
        "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "72:63",
                0
            ]
        },
        "class_type": "SaveImage",
        "_meta": {
            "title": "保存图像"
        }
    },
    "72:65": {
        "inputs": {
            "width": 1024,
            "height": 1024,
            "batch_size": 1
        },
        "class_type": "EmptySD3LatentImage",
        "_meta": {
            "title": "空Latent图像（SD3）"
        }
    },
    "72:62": {
        "inputs": {
            "vae_name": "ae.safetensors"
        },
        "class_type": "VAELoader",
        "_meta": {
            "title": "加载VAE"
        }
    },
    "72:68": {
        "inputs": {
            "text": [
                "58",
                0
            ],
            "clip": [
                "72:69",
                0
            ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
            "title": "CLIP文本编码"
        }
    },
    "72:70": {
        "inputs": {
            "text": [
                "71",
                0
            ],
            "clip": [
                "72:69",
                0
            ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
            "title": "CLIP文本编码"
        }
    },
    "72:63": {
        "inputs": {
            "samples": [
                "72:67",
                0
            ],
            "vae": [
                "72:62",
                0
            ]
        },
        "class_type": "VAEDecode",
        "_meta": {
            "title": "VAE解码"
        }
    },
    "72:69": {
        "inputs": {
            "clip_name": "qwen_3_4b.safetensors",
            "type": "lumina2",
            "device": "default"
        },
        "class_type": "CLIPLoader",
        "_meta": {
            "title": "加载CLIP"
        }
    },
    "72:64": {
        "inputs": {
            "unet_name": "z_image_turbo_bf16.safetensors",
            "weight_dtype": "default"
        },
        "class_type": "UNETLoader",
        "_meta": {
            "title": "UNet加载器"
        }
    },
    "72:67": {
        "inputs": {
            "seed": 383665062760075,
            "steps": 8,
            "cfg": 1,
            "sampler_name": "dpmpp_2m",
            "scheduler": "sgm_uniform",
            "denoise": 1,
            "model": [
                "72:64",
                0
            ],
            "positive": [
                "72:68",
                0
            ],
            "negative": [
                "72:70",
                0
            ],
            "latent_image": [
                "72:65",
                0
            ]
        },
        "class_type": "KSampler",
        "_meta": {
            "title": "K采样器"
        }
    }
}


class ComfyUIClient:
    def __init__(self, server_address="127.0.0.1:8188"):
        self.server_address = server_address
        self.client_id = str(uuid.uuid4())
        print(f"✅ 客户端初始化完成: ID: {self.client_id}")

    def queue_prompt(self, prompt):
        """提交任务到队列"""
        p = {"prompt": prompt, "client_id": self.client_id}
        data = json.dumps(p).encode('utf-8')
        try:
            req = urllib.request.Request(
                f"http://{self.server_address}/prompt", data=data
            )
            return json.loads(urllib.request.urlopen(req).read())
        except Exception as e:
            print(
                f"❌ 提交任务失败: {e}\n"
                "你从`COMFY_UI_IP`和`COMFY_UI_PORT`环境变量中读取到配置了吗？"
            )
            return None

    def get_image(self, output, filename, subfolder, folder_type):
        """下载图片并保存"""
        params = {
            "filename": filename,
            "subfolder": subfolder,
            "type": folder_type
        }
        query = urllib.parse.urlencode(params)
        url = f"http://{self.server_address}/view?{query}"

        os.makedirs(output, exist_ok=True)
        output_path = f"{output}/{filename}"

        try:
            urllib.request.urlretrieve(url, output_path)
            return output_path
        except Exception as e:
            print(f"❌ 下载图片失败: {e}")
            return None

    def get_history(self, prompt_id):
        """获取任务历史"""
        with urllib.request.urlopen(
            f"http://{self.server_address}/history/{prompt_id}"
        ) as response:
            return json.loads(response.read())

    def generate(self, workflow_json, output):
        """
        核心方法：提交 -> 等待 -> 下载
        """
        # 1. 提交
        result = self.queue_prompt(workflow_json)
        if not result:
            return

        prompt_id = result['prompt_id']
        print(f"🚀 任务已提交，ID: {prompt_id}，正在生成中...")

        # 2. 建立 WebSocket 监听
        ws = websocket.WebSocket()
        ws.connect(f"ws://{self.server_address}/ws?clientId={self.client_id}")

        try:
            while True:
                out = ws.recv()
                if isinstance(out, str):
                    message = json.loads(out)
                    # 监听执行完成的消息
                    if message['type'] == 'executing':
                        data = message['data']
                        # 当 node 为 None 且 prompt_id 匹配时，说明整个工作流跑完了
                        if (
                            data['node'] is None and
                            data['prompt_id'] == prompt_id
                        ):
                            print("✨ 生成完成，正在获取图片...")
                            break

        except Exception as e:
            print(f"监听出错: {e}")
        finally:
            ws.close()

        # 3. 获取并保存图片
        history = self.get_history(prompt_id)[prompt_id]
        saved_files = []

        if 'outputs' in history:
            for node_id in history['outputs']:
                node_output = history['outputs'][node_id]
                if 'images' in node_output:
                    for image in node_output['images']:
                        path = self.get_image(
                            output, image['filename'],
                            image['subfolder'], image['type']
                        )
                        if path:
                            saved_files.append(path)

        return saved_files


# ================= 这里是具体的调用代码 =================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ComfyUI Prompt to Image Generator"
    )
    parser.add_argument(
        "prompt", nargs="?", default=(
            "A cartoon image of a cat sitting on a windowsill, in the style "
            "of Studio Ghibli"), help="正向提示词")
    parser.add_argument(
        "output", nargs="?", default=(
            os.path.join(
                os.environ.get("HOME", '/home/node'), '.openclaw/workspace',
                'comfyui_outputs'
            )
        ), help="输出文件夹路径")
    parser.add_argument(
        "negative_prompt", nargs="?", default="blurry, low quality",
        help="反向提示词")
    parser.add_argument(
        "image_name", nargs="?", default=None, help="输出图片文件名（可选）")

    args = parser.parse_args()

    prompt = args.prompt
    output = args.output
    negative_prompt = args.negative_prompt
    image_name = args.image_name

    os.makedirs(output, exist_ok=True)

    # 1. 初始化客户端
    server_ip = os.getenv("COMFY_UI_IP", 'host.docker.internal')
    server_port = os.getenv("COMFY_UI_PORT", "8188")
    client = ComfyUIClient(f"{server_ip}:{server_port}")

    # with open("T2I-Z-Image-API.json", "r") as f:
    #     workflow = json.load(f)

    workflow['58']['inputs']['value'] = prompt  # 替换提示词
    workflow['71']['inputs']['negative'] = negative_prompt  # 替换反向提示词

    # 3. 开始生成
    print("--- 开始任务 ---")
    results = client.generate(workflow, output)

    # 如果指定了图片名称且有生成结果，则重命名为指定名称
    if results and image_name:
        import shutil
        first_img = results[0]
        target_path = os.path.join(output, image_name)
        try:
            shutil.move(first_img, target_path)
            print(f"图片已重命名为: {target_path}")
            results[0] = target_path
        except Exception as e:
            print(f"图片重命名失败: {e}")

    if results:
        print("--- 任务结束 ---")
        print(f"图片已保存到: {results}")
    else:
        print("--- 任务失败或无输出 ---")
