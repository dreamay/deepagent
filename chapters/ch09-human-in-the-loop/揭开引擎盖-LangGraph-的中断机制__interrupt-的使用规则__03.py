"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / interrupt() 的使用规则 (片段 3/4)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# ✅ 正确：每次执行顺序一致
def node(state):
    name = interrupt("你叫什么名字？")
    age = interrupt("你多大了？")
    return {"name": name, "age": age}

# ❌ 错误：条件跳过会导致索引错位
def node(state):
    name = interrupt("你叫什么名字？")
    if state.get("need_age"):     # 这个条件可能在恢复时变化！
        age = interrupt("你多大了？")
    city = interrupt("你在哪个城市？")  # 索引错位
