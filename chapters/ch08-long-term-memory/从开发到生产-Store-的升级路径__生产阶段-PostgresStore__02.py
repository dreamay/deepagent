"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 从开发到生产：Store 的升级路径 / 生产阶段：PostgresStore (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.store.postgres import PostgresStore
import os

with PostgresStore.from_conn_string(os.environ["DATABASE_URL"]) as store:
    # 第一次连接该数据库时调用，用于创建 Store 所需表结构
    store.setup()

    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        context_schema=MemoryContext,
        memory=["/memories/AGENTS.md"],
        store=store,
        backend=CompositeBackend(
            default=StateBackend(),
            routes={
                "/memories/": StoreBackend(
                    namespace=assistant_namespace,
                ),
            },
        ),
    )
