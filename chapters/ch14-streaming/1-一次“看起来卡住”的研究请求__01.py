"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 1. 一次“看起来卡住”的研究请求 (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
print(result["messages"][-1].content)
