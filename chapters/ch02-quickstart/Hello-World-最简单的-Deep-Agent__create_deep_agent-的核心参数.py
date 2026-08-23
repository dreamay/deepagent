"""
教程《Deep Agents 实战》— ch02-quickstart
原文位置: ch02-quickstart: 快速上手 — 5 分钟构建你的第一个 Deep Agent / Hello World：最简单的 Deep Agent / create_deep_agent() 的核心参数
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent = create_deep_agent(
    model=model,                           # 模型实例或字符串
    tools=[get_weather],                   # 自定义工具列表
    system_prompt="You are a helpful...",  # 系统提示词
)
