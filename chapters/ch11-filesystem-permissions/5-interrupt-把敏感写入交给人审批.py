"""
教程《Deep Agents 实战》— ch11-filesystem-permissions
原文位置: ch11-filesystem-permissions: 文件系统权限 — 用声明式规则控制 Agent 的读写边界 / 5. interrupt ：把敏感写入交给人审批
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import FilesystemPermission, create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command


agent = create_deep_agent(
    model=model,
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/secrets/**"],
            mode="interrupt",
        ),
    ],
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": "permission-review-1"}}

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "把临时凭证写入 /secrets/token.txt",
            }
        ]
    },
    config=config,
    version="v2",
)

if result.interrupts:
    request = result.interrupts[0].value["action_requests"][0]
    print(request["name"], request["args"])

    result = agent.invoke(
        Command(resume={"decisions": [{"type": "approve"}]}),
        config=config,
        version="v2",
    )
