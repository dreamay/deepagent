"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / Checkpointer：短期记忆的基础 / 短期记忆的管理策略
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langchain.agents import AgentState
from langchain.agents.middleware import before_model
from langgraph.runtime import Runtime

@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict | None:
    """只保留最近几条消息，防止上下文溢出。"""
    messages = state["messages"]
    if len(messages) <= 3:
        return None  # 不需要裁剪

    first_msg = messages[0]  # 保留第一条（通常是系统消息）
    recent = messages[-3:]   # 保留最近 3 条
    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            first_msg,
            *recent,
        ]
    }

# 在 create_agent 或 create_deep_agent 中通过 middleware 参数添加
agent = create_deep_agent(
    model=model,
    middleware=[trim_messages],
)
