"""
教程《Deep Agents 实战》— ch10-sandboxes
原文位置: ch10-sandboxes: 沙箱执行 — 让 Agent 安全地运行代码 / 3. 快速上手：LangSmithSandbox (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from deepagents.backends import LangSmithSandbox
from langchain_anthropic import ChatAnthropic
from langsmith.sandbox import SandboxClient

client = SandboxClient()
ls_sandbox = client.create_sandbox()
backend = LangSmithSandbox(sandbox=ls_sandbox)

agent = create_deep_agent(
    model=ChatAnthropic(model="claude-sonnet-4-6"),
    system_prompt="You are a Python coding assistant with sandbox access.",
    backend=backend,
)

try:
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "Create a small Python package and run pytest",
        }]
    })
    print(result["messages"][-1].content)
finally:
    # 远程资源会持续消耗配额或费用；无论成功失败都清理。
    client.delete_sandbox(ls_sandbox.name)
