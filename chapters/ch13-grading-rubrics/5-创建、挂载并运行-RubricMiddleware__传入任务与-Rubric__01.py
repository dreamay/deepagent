"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 5. 创建、挂载并运行 RubricMiddleware / 传入任务与 Rubric (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.messages import HumanMessage


config = {"configurable": {"thread_id": "ch13-rubric-case"}}
evaluation_start = len(evaluations)

result = agent.invoke(
    {
        "messages": [HumanMessage(content=task)],
        "rubric": rubric,
    },
    config=config,
)

run_evaluations = evaluations[evaluation_start:]
