"""
教程《Deep Agents 实战》— ch04-task-planning
原文位置: ch04-task-planning: 任务规划与分解 — 让 Agent 学会拆解复杂任务 / 揭开引擎盖：LangChain 中间件 / TodoListMiddleware：write_todos 的真身
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from deepagents.middleware import FilesystemMiddleware

model = ChatOpenAI(
    # 任务规划属于复杂推理场景，建议使用能力较强、支持工具调用的模型
    model="zai-org/GLM-5.2",
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        TodoListMiddleware(),
        FilesystemMiddleware(),   # 自动注入 read_file / write_file 等文件工具
    ],
)
