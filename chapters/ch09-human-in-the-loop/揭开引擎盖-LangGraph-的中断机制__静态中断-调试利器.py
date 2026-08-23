"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / 静态中断：调试利器
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 在 node_a 之前暂停，在 node_b 之后暂停
graph = builder.compile(
    interrupt_before=["node_a"],
    interrupt_after=["node_b"],
    checkpointer=checkpointer,
)

config = {"configurable": {"thread_id": "debug-001"}}
graph.invoke(inputs, config=config)   # 执行到 node_a 前暂停
graph.invoke(None, config=config)     # 传入 None 继续执行
