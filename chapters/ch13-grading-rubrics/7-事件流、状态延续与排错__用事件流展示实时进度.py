"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 7. 事件流、状态延续与排错 / 用事件流展示实时进度
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.stream import CustomTransformer


stream = agent.stream_events(
    {
        "messages": [HumanMessage(content=task)],
        "rubric": rubric,
    },
    config={"configurable": {"thread_id": "ch13-rubric-stream"}},
    version="v3",
    transformers=[CustomTransformer],
)

for event in stream.custom:
    if event.get("type") == "rubric_evaluation_start":
        print(f"grading iteration {event['iteration']} started")
    elif event.get("type") == "rubric_evaluation_end":
        print(f"grading iteration {event['iteration']}: {event['result']}")
