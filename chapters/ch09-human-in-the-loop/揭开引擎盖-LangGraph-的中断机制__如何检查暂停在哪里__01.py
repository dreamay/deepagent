"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / 如何检查暂停在哪里？ (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

snapshot = graph.get_state(config)

print(snapshot.values)      # 当前状态
print(snapshot.next)        # 下一步节点
print(snapshot.interrupts)  # 待处理的中断
