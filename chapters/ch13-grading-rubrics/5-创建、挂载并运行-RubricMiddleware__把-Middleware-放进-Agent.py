"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 5. 创建、挂载并运行 RubricMiddleware / 把 Middleware 放进 Agent
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver


agent = create_deep_agent(
    model=working_model,
    system_prompt=(
        "You are a careful Python engineer. Return only executable Python "
        "source code, without Markdown fences. When the rubric grader reports "
        "a gap, revise the latest implementation to address that exact gap."
    ),
    middleware=[rubric_middleware],
    checkpointer=InMemorySaver(),
)
