"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 从开发到生产：Store 的升级路径 / LangSmith 部署
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# LangSmith 部署时，省略 store 参数
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    context_schema=MemoryContext,
    memory=["/memories/AGENTS.md"],
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=assistant_namespace,
            ),
        },
    ),
    # store 由平台自动提供
)
