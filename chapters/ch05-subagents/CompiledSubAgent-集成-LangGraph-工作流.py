"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / CompiledSubAgent：集成 LangGraph 工作流
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent, CompiledSubAgent
from langchain.agents import create_agent

# 用 LangChain 创建一个自定义 Agent 图
custom_graph = create_agent(
    model=model,
    tools=[statistical_analysis, generate_chart],
    system_prompt="你是数据分析专家，擅长统计分析和可视化。",
)

# 包装为 CompiledSubAgent
data_subagent = CompiledSubAgent(
    name="data-analyzer",
    description="执行复杂的数据分析任务，包括统计分析和图表生成",
    runnable=custom_graph,  # 传入编译好的 LangGraph 图
)

agent = create_deep_agent(
    model=model,
    subagents=[data_subagent],
)
