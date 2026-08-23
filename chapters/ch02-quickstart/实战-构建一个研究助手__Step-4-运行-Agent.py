"""
教程《Deep Agents 实战》— ch02-quickstart
原文位置: ch02-quickstart: 快速上手 — 5 分钟构建你的第一个 Deep Agent / 实战：构建一个研究助手 / Step 4：运行 Agent
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

result = agent.invoke(
    {"messages": [{"role": "user", "content": "什么是 LangGraph？"}]}
)

print(result["messages"][-1].content)
