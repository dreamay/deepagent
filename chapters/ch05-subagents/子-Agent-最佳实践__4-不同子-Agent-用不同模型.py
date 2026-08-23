"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 子 Agent 最佳实践 / 4. 不同子 Agent 用不同模型
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

subagents = [
    {
        "name": "quick-lookup",
        "description": "快速查询简单事实",
        "tools": [internet_search],
        "model": ChatOpenAI(  # 轻量快速模型
            model="Qwen/Qwen2.5-7B-Instruct",
            api_key=os.environ["SILICONFLOW_API_KEY"],
            base_url="https://api.siliconflow.cn/v1",
        ),
        "system_prompt": "快速查找并返回简洁答案。",
    },
    {
        "name": "deep-analyst",
        "description": "执行需要深入推理的复杂分析任务",
        "tools": [internet_search, statistical_analysis],
        "model": ChatOpenAI(  # 强推理模型
            model="zai-org/GLM-5.2",
            api_key=os.environ["SILICONFLOW_API_KEY"],
            base_url="https://api.siliconflow.cn/v1",
        ),
        "system_prompt": "深入分析并提供详细的推理过程。",
    },
]
