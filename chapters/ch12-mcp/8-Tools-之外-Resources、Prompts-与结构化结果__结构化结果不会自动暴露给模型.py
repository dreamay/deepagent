"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 8. Tools 之外：Resources、Prompts 与结构化结果 / 结构化结果不会自动暴露给模型
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.messages import ToolMessage


for message in result["messages"]:
    artifact = message.artifact if isinstance(message, ToolMessage) else None
    if isinstance(artifact, dict):
        data = artifact.get("structured_content")
        if data is not None:
            print(data)
