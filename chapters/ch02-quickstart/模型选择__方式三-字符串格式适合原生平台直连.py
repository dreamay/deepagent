"""
教程《Deep Agents 实战》— ch02-quickstart
原文位置: ch02-quickstart: 快速上手 — 5 分钟构建你的第一个 Deep Agent / 模型选择 / 方式三：字符串格式（适合原生平台直连）
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 直连 Anthropic 官方 API（需配置 ANTHROPIC_API_KEY）
agent = create_deep_agent(model="anthropic:claude-sonnet-4-6")

# 直连 OpenAI 官方 API（需配置 OPENAI_API_KEY）
agent = create_deep_agent(model="openai:gpt-4.1")
