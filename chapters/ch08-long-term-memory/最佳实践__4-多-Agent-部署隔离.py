"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 最佳实践 / 4. 多 Agent 部署隔离
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

StoreBackend(
    namespace=lambda rt: (
        assistant_namespace(rt)[0],
        user_namespace(rt)[0],
    ),
)
