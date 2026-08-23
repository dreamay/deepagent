"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 批量工具调用的中断处理
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 用户请求："删除 temp.txt 并发邮件通知 admin"
result = agent.invoke(
    {"messages": [{"role": "user", "content": "删除 temp.txt 并发邮件通知 admin@example.com"}]},
    config=config,
    version="v2",
)

if result.interrupts:
    action_requests = result.interrupts[0].value["action_requests"]
    # action_requests[0] = delete_file(path="temp.txt")
    # action_requests[1] = send_email(to="admin@example.com", ...)

    # 按顺序提供决策
    decisions = [
        {"type": "approve"},  # 批准删除
        {
            "type": "reject",
            "message": "用户拒绝发送邮件。不要重试这次发送动作。",
        },
    ]

    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,
        version="v2",
    )
