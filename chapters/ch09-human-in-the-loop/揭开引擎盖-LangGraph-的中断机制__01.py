"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph.types import interrupt

@tool
def request_approval(action_description: str) -> str:
    """请求人工审批。"""
    # interrupt() 暂停执行，返回值是 Command(resume=...) 传入的数据
    approval = interrupt({
        "type": "approval_request",
        "action": action_description,
        "message": f"请审批：{action_description}",
    })

    if approval.get("approved"):
        return f"操作 '{action_description}' 已获批准，继续执行..."
    else:
        reason = approval.get("reason", "未提供原因")
        return f"操作 '{action_description}' 被拒绝，原因：{reason}"
