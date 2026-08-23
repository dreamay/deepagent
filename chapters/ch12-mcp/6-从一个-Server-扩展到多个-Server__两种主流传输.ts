"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 6. 从一个 Server 扩展到多个 Server / 两种主流传输
语言: typescript

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

client = MultiServerMCPClient(
    {
        "course_math": {
            "transport": "stdio",
            "command": sys.executable,
            "args": [str(SERVER)],
        },
        "langchain_docs": {
            "transport": "http",
            "url": "https://docs.langchain.com/mcp",
        },
    },
    tool_name_prefix=True,
)

all_tools = await client.get_tools()
math_tools = await client.get_tools(server_name="course_math")
