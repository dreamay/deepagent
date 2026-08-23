"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / Skill 权限控制 / 写入需审批（interrupt 模式）
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import FilesystemPermission, create_deep_agent
from langgraph.checkpoint.memory import MemorySaver

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    skills=["/skills/personal/"],
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/skills/**"],
            mode="interrupt",
        ),
    ],
    checkpointer=MemorySaver(),  # interrupt 需要 checkpointer
)
