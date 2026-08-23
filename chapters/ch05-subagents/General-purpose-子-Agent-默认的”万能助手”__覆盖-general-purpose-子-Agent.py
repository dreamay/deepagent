"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / General-purpose 子 Agent：默认的”万能助手” / 覆盖 general-purpose 子 Agent
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent = create_deep_agent(
    model=model,  # 主 Agent 复用应用的默认模型
    tools=[internet_search],
    subagents=[
        {
            "name": "general-purpose",  # 覆盖默认
            "description": "通用助手，处理各种委派任务",
            "system_prompt": "你是一个通用助手。",
            "tools": [internet_search],
            "model": ChatOpenAI(  # 子 Agent 用更强的模型
                model="zai-org/GLM-5.2",
                api_key=os.environ["SILICONFLOW_API_KEY"],
                base_url="https://api.siliconflow.cn/v1",
            ),
        },
    ],
)
