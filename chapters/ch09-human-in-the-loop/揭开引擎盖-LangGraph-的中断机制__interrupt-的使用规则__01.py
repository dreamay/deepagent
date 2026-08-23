"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 揭开引擎盖：LangGraph 的中断机制 / interrupt() 的使用规则 (片段 1/4)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# ❌ 错误：裸 except 会捕获 interrupt 异常
try:
    result = interrupt("请审批")
except Exception as e:
    print(e)  # 这会吞掉 interrupt！

# ✅ 正确：使用具体的异常类型
try:
    result = interrupt("请审批")
    fetch_data()
except NetworkError as e:  # 只捕获特定异常
    print(e)
