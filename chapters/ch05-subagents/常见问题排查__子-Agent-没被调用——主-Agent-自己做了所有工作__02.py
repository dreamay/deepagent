"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 常见问题排查 / 子 Agent 没被调用——主 Agent 自己做了所有工作 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent = create_deep_agent(
    ...,
    system_prompt="""...你的指令...

重要：面对复杂任务时，使用 task() 工具委派给对应的子 Agent，保持自身上下文干净。""",
)
