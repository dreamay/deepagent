"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 5. 第三个修复：工具调用也要能被看见 / 5.1 拆解 tool_call (片段 3/3)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

stream = agent.stream_events(request, version="v3")

for subagent in stream.subagents:
    print(f"subagent {subagent.name}: {subagent.status}")

    for tool_call in subagent.tool_calls:
        print(f"{tool_call.tool_name}({tool_call.input})")
        for delta in tool_call.output_deltas:
            print(delta, end="", flush=True)

    for nested in subagent.subagents:
        print(f"nested subagent {nested.name}: {nested.status}")
