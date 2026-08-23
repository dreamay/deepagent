"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / Checkpointer：短期记忆的基础
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()

agent = create_deep_agent(
    model=model,
    checkpointer=checkpointer,
)

# 同一个 thread_id 内，Agent 记得之前的对话
config = {"configurable": {"thread_id": "conversation-001"}}
agent.invoke({"messages": [{"role": "user", "content": "我叫张三"}]}, config=config)
agent.invoke({"messages": [{"role": "user", "content": "我叫什么名字？"}]}, config=config)
# Agent 能回答"你叫张三"

# 换一个 thread_id，Agent 不记得了
config2 = {"configurable": {"thread_id": "conversation-002"}}
agent.invoke({"messages": [{"role": "user", "content": "我叫什么名字？"}]}, config=config2)
# Agent 不知道你是谁
