"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 多子 Agent 协作模式
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import os
from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent

model = ChatOpenAI(
    # 主 Agent 负责协调多个子 Agent，建议使用能力较强、支持工具调用的模型
    model="zai-org/GLM-5.2",
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

subagents = [
    {
        "name": "data-collector",
        "description": "从多个来源收集原始数据，包括网络搜索和 API 调用",
        "system_prompt": "你是数据收集专家。搜索并整理相关数据，返回结构化的数据摘要。",
        "tools": [internet_search, api_call],
    },
    {
        "name": "data-analyzer",
        "description": "对收集到的数据进行统计分析，提取关键洞察",
        "system_prompt": "你是数据分析专家。分析数据并提取 3-5 个关键发现，控制在 300 字以内。",
        "tools": [statistical_analysis],
    },
    {
        "name": "report-writer",
        "description": "根据分析结果撰写专业报告",
        "system_prompt": "你是技术写作专家。根据提供的分析结果撰写清晰、专业的报告。",
        "tools": [format_document],
    },
]

agent = create_deep_agent(
    model=model,
    system_prompt="""你是一位项目协调者。面对复杂任务时：
1. 先用 write_todos 制定计划
2. 将数据收集委派给 data-collector
3. 将分析工作委派给 data-analyzer
4. 将报告撰写委派给 report-writer
5. 整合各子 Agent 的输出，形成最终结果""",
    subagents=subagents,
)
