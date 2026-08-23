"""
教程《Deep Agents 实战》— ch10-sandboxes
原文位置: ch10-sandboxes: 沙箱执行 — 让 Agent 安全地运行代码 / 7. 生命周期与作用域 / Thread-scoped：按对话复用
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from deepagents.backends.langsmith import LangSmithSandbox
from langchain_core.runnables import RunnableConfig
from langsmith.sandbox import SandboxClient

client = SandboxClient()

async def thread_agent(config: RunnableConfig):
    thread_id = config["configurable"]["thread_id"]
    sandbox_name = f"thread-{thread_id}"
    existing = [
        sb for sb in client.list_sandboxes()
        if getattr(sb, "name", None) == sandbox_name
    ]
    ls_sandbox = existing[0] if existing else client.create_sandbox(
        name=sandbox_name,
        idle_ttl_seconds=3600,
    )
    return create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        backend=LangSmithSandbox(sandbox=ls_sandbox),
    )
