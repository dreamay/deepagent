"""
教程《Deep Agents 实战》— ch14-streaming
原文位置: ch14-streaming: Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 2. 先让案例稳定复现
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import os

from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model=os.environ.get("MODEL_NAME", "zai-org/GLM-5.2"),
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ.get("OPENAI_BASE_URL", "https://api.siliconflow.cn/v1"),
)

agent = create_deep_agent(
    model=model,
    system_prompt=(
        "You are a coordinator. Delegate every research request to the "
        "researcher subagent. Do not research the topic yourself. "
        "After the subagent returns, summarize its result in two sentences."
    ),
    subagents=[
        {
            "name": "researcher",
            "description": "Researches a topic and returns a concise summary.",
            "system_prompt": (
                "Research the topic, use available tools when useful, "
                "and return a concise evidence-aware summary."
            ),
        }
    ],
)

request = {
    "messages": [
        {"role": "user", "content": "Research recent Agent streaming patterns"}
    ]
}
