"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 5. 把 MCP 工具交给 Deep Agent (片段 2/4)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import asyncio
import os
import sys
from pathlib import Path

from deepagents import create_deep_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI


SERVER = Path(__file__).with_name("math_server.py").resolve()


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

    model = ChatOpenAI(
        model=os.environ["MODEL_NAME"],
        api_key=os.environ["SILICONFLOW_API_KEY"],
        base_url="https://api.siliconflow.cn/v1",
    )
    agent = create_deep_agent(
        model=model,
        tools=tools,
        system_prompt=(
            "你是一个严谨的计算助手。数学运算必须使用 MCP 工具完成，"
            "不要直接心算。"
        ),
    )

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "先计算 37 + 58，再把结果乘以 12。",
                }
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
