"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / General-purpose 子 Agent：默认的”万能助手”
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 不传 subagents 参数，也能用子 Agent
agent = create_deep_agent(
    model=model,
    tools=[internet_search],
    system_prompt="你是一位研究助手。",
)

# 主 Agent 可以这样委派：
# task(name="general-purpose", task="搜索量子计算的最新进展")
