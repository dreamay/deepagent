"""
教程《Deep Agents 实战》— ch04-task-planning
原文位置: ch04-task-planning: 任务规划与分解 — 让 Agent 学会拆解复杂任务 / 任务规划与上下文管理的协同 / 在 LangChain 中手动组合
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from deepagents.middleware import FilesystemMiddleware, SummarizationMiddleware

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        TodoListMiddleware(),
        FilesystemMiddleware(),   # read_file / write_file 通过中间件注入
        SummarizationMiddleware(
            model="zai-org/GLM-5.2",  # 总结压缩影响后续推理质量，建议使用能力较强的模型
            trigger=("tokens", 4000),  # 可自定义：("ratio", 0.85) 或 ("tokens", N)
            keep=("messages", 20),
        ),
    ],
)
