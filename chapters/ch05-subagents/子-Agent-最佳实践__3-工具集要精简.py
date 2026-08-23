"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 子 Agent 最佳实践 / 3. 工具集要精简
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# ✅ 精简：只给研究相关的工具
research_agent = {"tools": [internet_search]}

# ❌ 冗余：给了不需要的工具
research_agent = {"tools": [internet_search, send_email, delete_file, execute_code]}
