"""
教程《Deep Agents 实战》— ch06-async-subagents
原文位置: ch06-async-subagents: 异步子 Agent — 让主 Agent 同时驱动多个子任务 / 三种部署拓扑
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

async_subagents = [
    AsyncSubAgent(
        name="researcher",
        description="研究 Agent",
        graph_id="researcher",
        # 不传 url → ASGI（同部署）
    ),
    AsyncSubAgent(
        name="coder",
        description="编码 Agent",
        graph_id="coder",
        url="https://coder-deployment.langsmith.dev",
        # 传了 url → HTTP（远程）
    ),
]
