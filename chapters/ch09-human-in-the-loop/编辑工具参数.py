"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 编辑工具参数
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

if result.interrupts:
    interrupt_value = result.interrupts[0].value
    action_request = interrupt_value["action_requests"][0]

    # Agent 原始参数
    original_args = action_request.get("arguments", action_request.get("args", {}))
    print(original_args)
    # {"to": "all@example.com", "subject": "通知", "body": "..."}

    # 用户决定修改收件人
    decisions = [{
        "type": "edit",
        "edited_action": {
            "name": action_request["name"],  # 必须包含工具名
            "args": {
                "to": "team@example.com",    # 修改后的收件人
                "subject": "通知",
                "body": "...",
            }
        }
    }]

    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,
        version="v2",
    )
