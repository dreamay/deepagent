"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / CompositeBackend：长期记忆的核心方案 / 跨对话访问
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain_core.utils.uuid import uuid7

# 对话 1：保存用户偏好
config1 = {"configurable": {"thread_id": str(uuid7())}}
agent.invoke({
    "messages": [{"role": "user", "content": "记住我的偏好：代码注释用中文，变量名用英文"}]
}, config=config1)
# Agent 将偏好写入 /memories/preferences.md

# 对话 2（全新的对话！）：读取之前保存的偏好
config2 = {"configurable": {"thread_id": str(uuid7())}}
agent.invoke({
    "messages": [{"role": "user", "content": "帮我写一个排序函数"}]
}, config=config2)
# Agent 读取 /memories/preferences.md，用中文注释、英文变量名
