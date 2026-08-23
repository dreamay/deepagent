"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 按风险等级分层的最佳实践
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

interrupt_on = {
    # === 高风险：审批 + 修改 + 拒绝，不开放 respond ===
    "delete_file": {"allowed_decisions": ["approve", "edit", "reject"]},
    "send_email": {"allowed_decisions": ["approve", "edit", "reject"]},
    "execute_sql": {"allowed_decisions": ["approve", "edit", "reject"]},
    "deploy_to_production": {"allowed_decisions": ["approve", "edit", "reject"]},

    # === 中风险：审批或拒绝（不允许修改参数）===
    "write_file": {"allowed_decisions": ["approve", "reject"]},
    "call_external_api": {"allowed_decisions": ["approve", "reject"]},

    # === 低风险：无需中断 ===
    "read_file": False,
    "ls": False,
    "grep": False,
    "glob": False,

    # === 人工输入型：人类就是工具结果 ===
    "ask_user": {"allowed_decisions": ["respond"]},
}
