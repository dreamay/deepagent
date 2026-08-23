"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / 如何检查暂停在哪里？ (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

thread_state = client.threads.get_state(thread_id="thread-1")
print(thread_state["values"])
print(thread_state["next"])
