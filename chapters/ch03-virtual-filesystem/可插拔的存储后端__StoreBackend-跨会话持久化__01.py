"""
教程《Deep Agents 实战》— ch03-virtual-filesystem
原文位置: ch03-virtual-filesystem: 虚拟文件系统 — Deep Agents 的 Context Engineering 核心 / 可插拔的存储后端 / StoreBackend：跨会话持久化 (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.store.memory import InMemoryStore
from deepagents.backends import StoreBackend

agent = create_deep_agent(
    model=model,
    backend=StoreBackend(
        namespace=lambda rt: (rt.server_info.user.identity,),  # 按用户隔离数据
    ),
    store=InMemoryStore()  # 开发用；部署到 LangSmith 时可省略，平台自动提供
)
