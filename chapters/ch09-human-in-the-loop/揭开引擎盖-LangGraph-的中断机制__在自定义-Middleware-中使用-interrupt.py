"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / 在自定义 Middleware 中使用 interrupt()
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from typing import Any

from deepagents import create_deep_agent
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain.messages import AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.runtime import Runtime
from langgraph.types import Command, interrupt


class DraftApprovalMiddleware(AgentMiddleware):
    def after_model(
        self,
        state: AgentState,
        runtime: Runtime,
    ) -> dict[str, Any] | None:
        last_message = state["messages"][-1]

        # 有工具调用时让 Agent 继续执行；这里只审查最终草稿。
        if not isinstance(last_message, AIMessage) or last_message.tool_calls:
            return None

        decision = interrupt({
            "type": "draft_review",
            "draft": last_message.content,
            "message": "是否批准向用户发布这份草稿？",
        })

        if decision.get("approved"):
            return None

        reason = decision.get("reason", "审批未通过")
        return {
            "messages": [AIMessage(content=f"草稿未发布：{reason}")],
        }


agent = create_deep_agent(
    model=model,
    middleware=[DraftApprovalMiddleware()],
    checkpointer=MemorySaver(),
)

config = {"configurable": {"thread_id": "draft-review-001"}}

paused = agent.invoke(
    {"messages": [{"role": "user", "content": "起草一份上线公告"}]},
    config=config,
    version="v2",
)

final = agent.invoke(
    Command(resume={"approved": True}),
    config=config,
    version="v2",
)
