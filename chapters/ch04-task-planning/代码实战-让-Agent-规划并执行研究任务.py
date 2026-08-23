"""
教程《Deep Agents 实战》— ch04-task-planning
原文位置: ch04-task-planning: 任务规划与分解 — 让 Agent 学会拆解复杂任务 / 代码实战：让 Agent 规划并执行研究任务
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import os
from langchain_openai import ChatOpenAI
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent

# 配置模型
model = ChatOpenAI(
    # 多步骤规划任务建议使用能力较强、支持工具调用的模型
    model="zai-org/GLM-5.2",
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

# 搜索工具
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(query: str, max_results: int = 5) -> dict:
    """搜索互联网获取最新信息。"""
    return tavily_client.search(query, max_results=max_results)

# 创建 Agent（write_todos 自动内置）
agent = create_deep_agent(
    model=model,
    tools=[internet_search],
    system_prompt="""你是一位专业的技术研究员。
面对复杂研究任务时，你会：
1. 先用 write_todos 制定研究计划
2. 逐步执行每个步骤，及时更新进度
3. 将搜索结果写入文件系统整理
4. 最终输出完整的研究报告
""",
)

# 发起一个需要规划的复杂任务
result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "请调研 Agent 开发领域的三大 Harness 框架（Deep Agents、Claude Agent SDK、Codex SDK），对比它们的核心能力差异，写一份简要分析报告。"
    }]
})

print(result["messages"][-1].content)
