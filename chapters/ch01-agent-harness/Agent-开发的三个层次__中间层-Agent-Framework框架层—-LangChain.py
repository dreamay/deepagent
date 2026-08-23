"""
教程《Deep Agents 实战》— ch01-agent-harness
原文位置: ch01-agent-harness: 从 Agent Framework 到 Agent Harness — Deep Agents 的诞生逻辑 / Agent 开发的三个层次 / 中间层：Agent Framework（框架层）— LangChain
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.agents import create_agent

agent = create_agent(
    model="gpt-4.1",
    tools=[web_search, calculator],
    system_prompt="You are a helpful assistant."
)
