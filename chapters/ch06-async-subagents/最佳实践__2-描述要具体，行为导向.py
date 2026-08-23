"""
教程《Deep Agents 实战》— ch06-async-subagents
原文位置: ch06-async-subagents: 异步子 Agent — 让主 Agent 同时驱动多个子任务 / 最佳实践 / 2. 描述要具体，行为导向
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# ✅ 好
AsyncSubAgent(
    name="researcher",
    description="深度网络调研，需要多次搜索 + 信息综合时使用",
    graph_id="researcher",
)

# ❌ 差
AsyncSubAgent(
    name="helper",
    description="帮你处理事情",
    graph_id="helper",
)
