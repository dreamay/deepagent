"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 3. 创建本地 MCP Server
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Chapter 12 Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers exactly."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers exactly."""
    return a * b


if __name__ == "__main__":
    mcp.run(transport="stdio")
