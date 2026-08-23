"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 7. 页面开始工作后，才需要精确顺序
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

stream = agent.stream_events(request, version="v3")

for event in stream:
    if not isinstance(event, dict):
        continue
    if event.get("method") != "messages":
        continue

    params = event.get("params") or {}
    data = params.get("data")
    if not isinstance(data, (list, tuple)) or not data:
        continue

    payload = data[0]
    if not isinstance(payload, dict):
        continue
    if payload.get("event") != "content-block-delta":
        continue

    block = payload.get("delta") or {}
    if block.get("type") != "text-delta":
        continue

    namespace = params["namespace"]
    source = "subagent" if namespace else "coordinator"
    print(f"#{event['seq']} [{source}] {block['text']}", end="", flush=True)
