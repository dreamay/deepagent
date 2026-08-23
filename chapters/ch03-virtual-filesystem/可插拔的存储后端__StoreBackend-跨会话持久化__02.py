"""
教程《Deep Agents 实战》— ch03-virtual-filesystem
原文位置: ch03-virtual-filesystem: 虚拟文件系统 — Deep Agents 的 Context Engineering 核心 / 可插拔的存储后端 / StoreBackend：跨会话持久化 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

namespace=lambda rt: (
    (rt.server_info.user.identity,)
    if rt.server_info else
    ("local-user",)
),
