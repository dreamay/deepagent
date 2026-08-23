"""
教程《Deep Agents 实战》— ch09-human-in-the-loop
原文位置: ch09-human-in-the-loop: Human-in-the-Loop — 构建安全的人机协作流程 / 中断与恢复：完整流程
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import uuid
from langgraph.types import Command

# 创建一个 thread_id（恢复时必须使用同一个）
config = {"configurable": {"thread_id": str(uuid.uuid4())}}

# Step 1: 发起请求
result = agent.invoke(
    {"messages": [{"role": "user", "content": "删除 temp.txt 文件"}]},
    config=config,
    version="v2",
)

# Step 2: 检查是否中断
if result.interrupts:
    interrupt_value = result.interrupts[0].value
    action_requests = interrupt_value["action_requests"]
    review_configs = interrupt_value["review_configs"]
    config_map = {cfg["action_name"]: cfg for cfg in review_configs}

    # 展示给用户
    for action in action_requests:
        review_config = config_map[action["name"]]
        args = action.get("arguments", action.get("args", {}))
        print(f"工具: {action['name']}")
        print(f"参数: {args}")
        print(f"可选决策: {review_config['allowed_decisions']}")

    # Step 3: 用户做出决策
    decisions = [
        {"type": "approve"}  # 用户批准删除
    ]

    # Step 4: 恢复执行（必须用相同的 config！）
    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,     # 同一个 thread_id
        version="v2",
    )

# 获取最终结果
print(result.value["messages"][-1].content)
