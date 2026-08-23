"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 3. 准备案例、环境与 Rubric / 准备环境与模型 (片段 2/3)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

import os

from langchain.chat_models import init_chat_model


working_model = init_chat_model(os.environ["WORKING_MODEL"])
grader_model = init_chat_model(
    os.environ.get("GRADER_MODEL", os.environ["WORKING_MODEL"])
)
