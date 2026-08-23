"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 文件存储格式与外部写入 (片段 2/2)
语言: shell

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents.backends.utils import create_file_data
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()

# 预填 Agent 记忆
store.put(
    ("my-agent",),                          # namespace
    "/memories/AGENTS.md",                  # 文件路径
    create_file_data("""## Response style
- Keep responses concise
- Use code examples where possible
"""),
)

# 预填一个 Skill
store.put(
    ("my-agent",),
    "/skills/langgraph-docs/SKILL.md",
    create_file_data("""---
name: langgraph-docs
description: Fetch relevant LangGraph documentation to provide accurate guidance.
---

# langgraph-docs

Use the fetch_url tool to read https://docs.langchain.com/llms.txt, then fetch relevant pages.
"""),
)
