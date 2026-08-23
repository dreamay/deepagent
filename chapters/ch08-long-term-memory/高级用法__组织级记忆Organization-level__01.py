"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 高级用法 / 组织级记忆（Organization-level） (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    context_schema=MemoryContext,
    memory=[
        "/memories/preferences.md",
        "/policies/compliance.md",
    ],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=user_namespace,
            ),
            "/policies/": StoreBackend(
                namespace=org_namespace,
            ),
        },
    ),
)
