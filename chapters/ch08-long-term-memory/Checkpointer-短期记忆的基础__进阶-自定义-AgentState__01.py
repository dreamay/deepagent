"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / Checkpointer：短期记忆的基础 / 进阶：自定义 AgentState (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.agents import create_agent, AgentState

class CustomAgentState(AgentState):
    user_id: str          # 用户 ID
    preferences: dict     # 用户偏好

agent = create_agent(
    model=model,
    tools=[get_user_info],
    state_schema=CustomAgentState,
    checkpointer=checkpointer,
)

# 自定义状态可以在 invoke 时传入
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "你好"}],
        "user_id": "user_123",
        "preferences": {"theme": "dark"},
    },
    {"configurable": {"thread_id": "1"}},
)
