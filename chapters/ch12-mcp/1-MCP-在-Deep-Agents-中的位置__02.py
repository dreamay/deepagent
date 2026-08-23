"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 1. MCP 在 Deep Agents 中的位置 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

tools = await client.get_tools()
agent = create_deep_agent(model=model, tools=tools)
