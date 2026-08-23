"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data (片段 4/5)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.messages import AIMessageChunk, ToolMessage


for chunk in agent.stream(
    request,
    stream_mode="messages",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] != "messages":
        continue

    token, metadata = chunk["data"]
    source = "subagent" if chunk["ns"] else "main"

    if isinstance(token, AIMessageChunk) and token.tool_call_chunks:
        for tool_chunk in token.tool_call_chunks:
            print(source, "tool:", tool_chunk.get("name"), tool_chunk.get("args"))
    elif isinstance(token, ToolMessage):
        print(source, "tool result:", token.name, token.content)
    elif token.content:
        print(source, token.content, end="", flush=True)
