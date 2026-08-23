"""
教程《Deep Agents 实战》— ch06-async-subagents
原文位置: ch06-async-subagents: 异步子 Agent — 让主 Agent 同时驱动多个子任务 / 两种传输：ASGI vs HTTP / HTTP 传输（远程，按需切换）
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

AsyncSubAgent(
    name="researcher",
    description="Research Agent",
    graph_id="researcher",
    url="https://my-research-deployment.langsmith.dev",
)
