"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / Skill 权限控制 / 共享 + 个人 Skills 分层
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from dataclasses import dataclass

from deepagents import FilesystemPermission, create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend


@dataclass(frozen=True)
class TenantContext:
    org_id: str
    user_id: str


def shared_skill_namespace(rt):
    org_id = getattr(rt.context, "org_id", "default-org")
    return ("curated-skills", org_id)


def personal_skill_namespace(rt):
    if rt.server_info and rt.server_info.user:
        return ("user-skills", rt.server_info.user.identity)
    user_id = getattr(rt.context, "user_id", "local-user")
    return ("user-skills", user_id)


agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    context_schema=TenantContext,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/skills/shared/": StoreBackend(
                namespace=shared_skill_namespace,
            ),
            "/skills/personal/": StoreBackend(
                namespace=personal_skill_namespace,
            ),
        },
    ),
    skills=["/skills/shared/", "/skills/personal/"],
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/skills/shared/**"],
            mode="deny",
        ),
    ],
)
