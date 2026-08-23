"""
教程《Deep Agents 实战》— ch11-filesystem-permissions
原文位置: ch11-filesystem-permissions: 文件系统权限 — 用声明式规则控制 Agent 的读写边界 / 7. CompositeBackend 与沙箱的特殊边界 / CompositeBackend：权限路径必须落在可控制的路由上
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends import CompositeBackend


composite = CompositeBackend(
    default=sandbox,
    routes={"/memories/": memories_backend},
)

agent = create_deep_agent(
    model=model,
    backend=composite,
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/memories/**"],
            mode="deny",
        ),
    ],
)
