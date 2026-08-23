"""
教程《Deep Agents 实战》— ch04-task-planning
原文位置: ch04-task-planning: 任务规划与分解 — 让 Agent 学会拆解复杂任务 / write_todos 工具详解 / Agent 怎么用 write_todos？ (片段 2/3)
语言: shell

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

Agent 更新任务 1 状态为 in_progress
Agent 调用 internet_search("LangGraph architecture")
Agent 调用 write_file("/workspace/langgraph_notes.md", ...)
Agent 更新任务 1 状态为 completed

Agent 更新任务 2 状态为 in_progress
Agent 调用 internet_search("Temporal vs LangGraph")
...
