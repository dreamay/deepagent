"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 6. 从一个 Server 扩展到多个 Server / HTTP Header 与认证
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import os

from langchain_mcp_adapters.client import MultiServerMCPClient


client = MultiServerMCPClient(
    {
        "orders": {
            "transport": "http",
            "url": "https://mcp.example.com/mcp",
            "headers": {
                "Authorization": f"Bearer {os.environ['MCP_TOKEN']}",
            },
        }
    },
    tool_name_prefix=True,
)
