"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / CompositeBackend：长期记忆的核心方案 / 运行时身份与 namespace (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent.invoke(
    {"messages": [{"role": "user", "content": "记住我喜欢简洁风格"}]},
    context=MemoryContext(user_id="user-123", org_id="org-acme"),
    config={"configurable": {"thread_id": "1"}},
)
