import type { OpenClawPluginApi } from "openclaw/plugin-sdk";
import { emptyPluginConfigSchema } from "openclaw/plugin-sdk";
import { Type } from "@sinclair/typebox";
import { spawn } from "child_process"; // 改用 spawn 以便更好地控制参数和路径
import path from "path";
import { fileURLToPath } from "url";

// 辅助函数：将 spawn 包装为 Promise
function runPythonScript(pythonPath: string, scriptPath: string, args: string[]): Promise<{ stdout: string; stderr: string }> {
    return new Promise((resolve, reject) => {
        const pyProcess = spawn(pythonPath, [scriptPath, ...args], {
            // 可选：确保环境变量干净，或者继承当前进程环境变量
            env: process.env,
            cwd: path.dirname(scriptPath) // 可选：设置工作目录为脚本所在目录
        });

        let stdoutData = "";
        let stderrData = "";

        pyProcess.stdout.on("data", (data) => {
            stdoutData += data.toString();
        });

        pyProcess.stderr.on("data", (data) => {
            stderrData += data.toString();
        });

        pyProcess.on("close", (code) => {
            if (code === 0) {
                resolve({ stdout: stdoutData, stderr: stderrData });
            } else {
                // 即使退出码非零，也返回内容供上层处理，或者直接在这里 reject
                reject(new Error(`Python 脚本退出码: ${code}. 错误输出: ${stderrData}`));
            }
        });

        pyProcess.on("error", (err) => {
            reject(err);
        });
    });
}

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// 【配置项】虚拟环境目录名称 (根据你的实际项目结构调整)
// 假设 .venv 在 plugin 根目录，即当前文件的上两级目录 (skills/web-content-fetcher/scripts -> ../../..)
// 请根据实际情况调整这个相对路径
const VENV_RELATIVE_PATH = "/home/node/.openclaw/workspace/.venv";

const plugin = {
    id: "zclaw-skills",
    name: "zClaw Skills",
    description: "zClaw Skills plugin",
    configSchema: emptyPluginConfigSchema(),
    register(api: OpenClawPluginApi) {
        api.registerTool({
            id: "fetch_web_content",
            name: "fetch_web_content",
            label: 'zClaw: Fetch Web Content',
            description: "提取网页正文内容。支持 Scrapling+html2text / playwright / web_fetch 三级降级策略，"
            + "自动返回干净的 Markdown 格式正文，保留标题、链接、图片 URL、列表结构。"
            + "能读取微信公众号文章、微博博文。"
            + "触发条件：用户要抓取某个 URL 的正文内容、读取某篇文章、提取网页内容等。",
            parameters: Type.Object({
                url: Type.String({ description: "要抓取的完整 URL 地址" }),
                max_chars: Type.Optional(Type.Number(
                    { description: "可选参数，限制返回内容的最大字符数，默认为 30000" }
                )),
            }),
            async execute(_toolCallId: any, params: any) {
                try {
                    const scriptPath = path.join(
                        __dirname, "skills", "zclaw-web-content-fetcher",
                        "scripts", "fetch.py"
                    );

                    // 1. 确定 Python 解释器路径
                    let pythonExecutable: string;
                    if (process.platform === "win32") {
                        pythonExecutable = path.join(VENV_RELATIVE_PATH, "Scripts", "python.exe");
                    } else {
                        pythonExecutable = path.join(VENV_RELATIVE_PATH, "bin", "python");
                    }

                    api.logger.info(`[zClaw]Using Python interpreter: ${pythonExecutable}`);
                    api.logger.info(`[zClaw]Executing fetch_web_content with URL: ${params.url}`);

                    // 准备参数
                    const scriptArgs = [
                        params.url,
                        (params.max_chars || 30000).toString()
                    ];

                    // 2. 使用自定义的 runPythonScript 运行
                    const { stdout, stderr } = await runPythonScript(pythonExecutable, scriptPath, scriptArgs);

                    api.logger.info(`[zClaw]fetch_web_content stdout length: ${stdout.length}`);
                    if (stderr) {
                        api.logger.warn(`[zClaw]fetch_web_content stderr: ${stderr}`);
                    }

                    // 注意：有些脚本可能将错误信息打印到 stderr 但仍然返回了部分结果
                    // 这里逻辑根据你的需求调整，如果只要有 stderr 就视为失败，保留原逻辑
                    if (stderr && !stdout) {
                        return {
                            content: [
                                { type: "text", text: `抓取失败: ${stderr}` }
                            ]
                        };
                    }

                    return {
                        content: [{ type: "text", text: stdout }]
                    };
                } catch (error: any) {
                    api.logger.error(`[zClaw]Execution error: ${error.message}`);
                    return {
                        content: [
                            { type: "text", text: `执行出错: ${error.message}` }
                        ]
                    };
                }
            },
        }, { name: 'fetch_web_content' });
    },
};

export default plugin;
