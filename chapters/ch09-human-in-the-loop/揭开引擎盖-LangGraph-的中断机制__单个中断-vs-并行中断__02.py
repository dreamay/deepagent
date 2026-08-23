"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / 单个中断 vs 并行中断 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.types import Command

# stream.interrupts = (Interrupt(value="question_a", id="..."),
#                      Interrupt(value="question_b", id="..."))
resume_map = {
    intr.id: f"answer for {intr.value}"
    for intr in stream.interrupts
}

graph.invoke(Command(resume=resume_map), config=config)
