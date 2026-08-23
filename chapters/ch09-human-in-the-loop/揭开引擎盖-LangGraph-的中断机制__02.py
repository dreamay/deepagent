"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 审批通过
result = agent.invoke(
    Command(resume={"approved": True}),
    config=config,
    version="v2",
)

# 审批拒绝
result = agent.invoke(
    Command(resume={"approved": False, "reason": "时机不对，延后执行"}),
    config=config,
    version="v2",
)
