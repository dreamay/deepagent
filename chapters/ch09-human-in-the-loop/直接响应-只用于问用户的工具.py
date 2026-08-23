"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 直接响应：只用于问用户的工具
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.tools import tool


@tool
def ask_user(question: str) -> str:
    """向用户提问；真实回答由 HITL 的 respond 决策提供。"""
    return "等待用户回答"


agent = create_deep_agent(
    model=model,
    tools=[ask_user],
    interrupt_on={
        "ask_user": {"allowed_decisions": ["respond"]},
    },
    checkpointer=checkpointer,
)

decisions = [{
    "type": "respond",
    "message": "使用季度维度，并排除测试数据。",
}]
