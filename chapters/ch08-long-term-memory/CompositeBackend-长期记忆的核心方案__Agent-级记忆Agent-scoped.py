"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / CompositeBackend：长期记忆的核心方案 / Agent 级记忆（Agent-scoped）
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    context_schema=MemoryContext,
    memory=["/memories/AGENTS.md"],          # 启动时自动加载的记忆文件
    skills=["/skills/"],                      # 程序性记忆（Skills）
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=assistant_namespace,
            ),
            "/skills/": StoreBackend(
                namespace=assistant_namespace,
            ),
        },
    ),
)
