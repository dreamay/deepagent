"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 9. 需要自定义进度时，先定义自己的事件
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.tools import tool
from langgraph.config import get_stream_writer


@tool
def analyze_data(topic: str) -> str:
    """Analyze a topic and report structured progress."""
    writer = get_stream_writer()
    writer({"status": "starting", "topic": topic, "progress": 0})
    # 执行实际分析
    writer({"status": "complete", "topic": topic, "progress": 100})
    return f"Analysis complete: {topic}"
