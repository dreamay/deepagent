"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 常见问题排查 / 调用了错误的子 Agent
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

subagents = [
    {
        "name": "quick-researcher",
        "description": "用于简单、快速的查询，只需 1-2 次搜索。适合查找基本事实或定义。",
    },
    {
        "name": "deep-researcher",
        "description": "用于复杂、深入的研究，需要多次搜索、综合和分析。适合生成全面报告。",
    },
]
