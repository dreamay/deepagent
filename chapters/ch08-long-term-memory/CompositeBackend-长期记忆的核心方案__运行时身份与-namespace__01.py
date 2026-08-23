"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / CompositeBackend：长期记忆的核心方案 / 运行时身份与 namespace (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryContext:
    user_id: str = "local-user"
    org_id: str = "default-org"


def assistant_namespace(rt):
    if rt.server_info:
        return (rt.server_info.assistant_id,)
    return ("local-agent",)


def user_namespace(rt):
    if rt.server_info and rt.server_info.user:
        return (rt.server_info.user.identity,)
    user_id = getattr(rt.context, "user_id", "local-user")
    return (user_id,)


def org_namespace(rt):
    org_id = getattr(rt.context, "org_id", "default-org")
    return (org_id,)
