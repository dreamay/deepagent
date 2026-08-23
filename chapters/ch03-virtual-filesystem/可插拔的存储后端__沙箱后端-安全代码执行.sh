"""
教程《Deep Agents 实战》— ch03-virtual-filesystem
原文位置: ch03-virtual-filesystem: 虚拟文件系统 — Deep Agents 的 Context Engineering 核心 / 可插拔的存储后端 / 沙箱后端：安全代码执行
语言: shell

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 沙箱后端自动提供 execute 工具
agent = create_deep_agent(
    model=model,
    backend=sandbox  # 沙箱实例
)
# Agent 现在可以运行: execute("pip install pandas && python analyze.py")
