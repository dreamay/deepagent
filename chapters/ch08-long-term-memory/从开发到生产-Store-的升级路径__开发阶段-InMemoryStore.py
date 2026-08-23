"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 从开发到生产：Store 的升级路径 / 开发阶段：InMemoryStore
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.store.memory import InMemoryStore

store = InMemoryStore()  # 数据在内存中，重启丢失
