"""
教程《Deep Agents 实战》— ch02-quickstart
原文位置: ch02-quickstart: 快速上手 — 5 分钟构建你的第一个 Deep Agent / 模型选择 / 方式一：OpenAI 兼容接口（推荐）
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain_openai import ChatOpenAI

# 硅基流动（当前免费模型，适合学习）
model = ChatOpenAI(
    model="Qwen/Qwen2.5-7B-Instruct",
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)
agent = create_deep_agent(model=model)

# 硅基流动（复杂任务推荐模型）
model = ChatOpenAI(
    model="zai-org/GLM-5.2",
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)
agent = create_deep_agent(model=model)
