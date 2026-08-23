"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / interrupt() 的使用规则 (片段 2/4)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# ❌ 错误：interrupt 前创建记录，恢复时会创建重复记录
def node(state):
    db.create_log("操作开始")  # 每次恢复都会再创建一条！
    approved = interrupt("请审批")
    return {"approved": approved}

# ✅ 正确：用 upsert（幂等操作），或把副作用放到 interrupt 之后
def node(state):
    approved = interrupt("请审批")
    if approved:
        db.create_log("操作已审批")  # 只在审批后执行一次
    return {"approved": approved}
