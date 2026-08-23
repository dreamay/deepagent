"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 10. 与 Deep Agents 安全机制组合 / 缩小子 Agent 的额外工具集
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import FilesystemPermission, create_deep_agent


agent = create_deep_agent(
    model=model,
    tools=all_mcp_tools,
    subagents=[
        {
            "name": "catalog-reader",
            "description": "只使用只读 MCP 工具查询商品目录",
            "system_prompt": "只使用目录查询 MCP 工具回答商品问题。",
            "tools": read_only_mcp_tools,
            "permissions": [
                FilesystemPermission(
                    operations=["write"],
                    paths=["/**"],
                    mode="deny",
                )
            ],
        }
    ],
)
