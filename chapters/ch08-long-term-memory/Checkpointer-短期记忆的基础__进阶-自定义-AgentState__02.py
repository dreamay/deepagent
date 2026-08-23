"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / Checkpointer：短期记忆的基础 / 进阶：自定义 AgentState (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.tools import tool, ToolRuntime

@tool
def get_user_info(runtime: ToolRuntime) -> str:
    """查询当前用户信息。"""
    user_id = runtime.state["user_id"]  # 从 Agent State 中读取
    # 根据 user_id 查询用户信息
    if user_id == "user_123":
        return "用户：张三，VIP 会员，偏好简洁风格"
    return "未知用户"

@tool
def update_preferences(new_theme: str, runtime: ToolRuntime):
    """更新用户偏好设置。"""
    from langgraph.types import Command
    from langchain.messages import ToolMessage

    current_prefs = runtime.state.get("preferences", {})
    current_prefs["theme"] = new_theme
    # 通过 Command 写回 Agent State
    return Command(update={
        "preferences": current_prefs,
        "messages": [
            ToolMessage("偏好已更新", tool_call_id=runtime.tool_call_id)
        ]
    })
