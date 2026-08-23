"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 5. 第三个修复：工具调用也要能被看见
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

stream = agent.stream_events(request, version="v3")

for call in stream.tool_calls:
    print("[coordinator tool]", call.tool_name, call.input)
    print("completed:", call.completed, "error:", call.error)

for subagent in stream.subagents:
    for call in subagent.tool_calls:
        print(f"[{subagent.name} tool]", call.tool_name, call.input)

        for delta in call.output_deltas:
            print(delta, end="", flush=True)

        if call.completed and call.error is None:
            print("\nresult:", call.output)
        elif call.error is not None:
            print("\nerror:", call.error)
