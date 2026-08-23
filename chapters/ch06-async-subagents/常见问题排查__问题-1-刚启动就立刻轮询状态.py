"""
教程《Deep Agents 实战》— ch06-async-subagents
原文位置: ch06-async-subagents: 异步子 Agent — 让主 Agent 同时驱动多个子任务 / 常见问题排查 / 问题 1：刚启动就立刻轮询状态
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="""...你的指令...

派出异步子 Agent 之后，**必须立刻把控制权交还给用户**；
不要在没有用户提问的情况下主动 check_async_task。""",
    subagents=async_subagents,
)
