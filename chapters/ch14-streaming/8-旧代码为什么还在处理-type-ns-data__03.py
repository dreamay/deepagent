"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data (片段 3/5)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

for chunk in agent.stream(
    request,
    stream_mode="updates",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] != "updates":
        continue

    ns = chunk["ns"]
    task_segment = next(
        (segment for segment in ns if segment.startswith("tools:")),
        None,
    )

    if task_segment is None:
        print("Main agent:", chunk["data"])
    else:
        task_id = task_segment.split(":", 1)[1]
        print(f"Subagent {task_id}:", chunk["data"])
