"""
教程《Deep Agents 实战》— ch10-sandboxes
原文位置: ch10-sandboxes: 沙箱执行 — 让 Agent 安全地运行代码 / 1. 沙箱 Backend：执行环境，而不是权限开关 / execute() 的返回值
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents.backends.langsmith import LangSmithSandbox
from langsmith.sandbox import SandboxClient

client = SandboxClient()
sandbox = client.create_sandbox(template_name="deepagents-deploy")
backend = LangSmithSandbox(sandbox=sandbox)

try:
    result = backend.execute("python --version")
    print(result.output)
finally:
    client.delete_sandbox(sandbox.name)
