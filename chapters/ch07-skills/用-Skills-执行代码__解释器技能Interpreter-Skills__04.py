"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / 用 Skills 执行代码 / 解释器技能（Interpreter Skills） (片段 4/4)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from deepagents.backends import StateBackend
from langchain_quickjs import CodeInterpreterMiddleware

backend = StateBackend()

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    backend=backend,
    skills=["/skills/"],
    middleware=[CodeInterpreterMiddleware(skills_backend=backend)],
)
