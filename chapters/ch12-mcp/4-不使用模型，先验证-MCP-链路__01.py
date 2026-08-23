"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 4. 不使用模型，先验证 MCP 链路 (片段 1/3)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import asyncio
import sys
from pathlib import Path

from langchain_mcp_adapters.client import MultiServerMCPClient


SERVER = Path(__file__).with_name("math_server.py").resolve()


def schema_as_dict(tool) -> dict:
    schema = tool.args_schema
    if isinstance(schema, dict):
        return schema
    return schema.model_json_schema()


def first_text(result: list[dict]) -> str:
    return next(block["text"] for block in result if block["type"] == "text")


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "course_math": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(SERVER)],
            }
        },
        tool_name_prefix=True,
    )

    tools = await client.get_tools()
    print("tools:", [tool.name for tool in tools])

    add_tool = next(tool for tool in tools if tool.name == "course_math_add")
    schema = schema_as_dict(add_tool)
    print("description:", add_tool.description)
    print("required:", schema["required"])

    result = await add_tool.ainvoke({"a": 37, "b": 58})
    print("37 + 58 =", first_text(result))


if __name__ == "__main__":
    asyncio.run(main())
