"""
教程《Deep Agents 实战》— ch10-sandboxes
原文位置: ch10-sandboxes: 沙箱执行 — 让 Agent 安全地运行代码 / 9. LangSmith 托管沙箱：不止是一个 Backend / 独立 SDK 使用 (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sandbox:
    result = sandbox.run("python -c 'print(2 + 2)'")
    print(result.stdout)
