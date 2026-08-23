"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 3. 第一个修复：先显示“研究助手已启动” / 3.3 path 、 namespace 和 ns 是什么关系 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

def belongs_to_subagent(namespace: list[str] | tuple[str, ...], path: tuple[str, ...]) -> bool:
    return tuple(namespace[: len(path)]) == path
