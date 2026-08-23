"""
教程《Deep Agents 实战》— ch10-sandboxes
原文位置: ch10-sandboxes: 沙箱执行 — 让 Agent 安全地运行代码 / 9. LangSmith 托管沙箱：不止是一个 Backend / 独立 SDK 使用 (片段 2/2)
语言: typescript

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import { SandboxClient } from "langsmith/sandbox";

const client = new SandboxClient();
const sandbox = await client.createSandbox();
const result = await sandbox.run("node -e 'console.log(2 + 2)'");
console.log(result.stdout);
await sandbox.delete();
