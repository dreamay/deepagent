"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 定义子 Agent：字典方式
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent

# 定义一个研究型子 Agent
research_subagent = {
    "name": "researcher",                # 必填：唯一标识符
    "description": "深入研究特定主题，搜索多个信息源并整理成摘要",  # 必填：主 Agent 靠它决定何时委派
    "system_prompt": """你是一位专业的研究员。你的任务是：
1. 把研究问题拆解为多个搜索查询
2. 用 internet_search 搜索相关信息
3. 整理发现，写成简洁摘要
4. 列出关键发现和信息来源

注意：返回结果控制在 500 字以内，只返回核心发现。""",  # 必填：子 Agent 自己的指令
    "tools": [internet_search],          # 可选，默认继承；显式指定后完全替换（不合并）
    "skills": ["/skills/research/"],     # 可选，不继承主 Agent；指定后独立运行 SkillsMiddleware
}

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    skills=["/skills/main/"],            # 主 Agent 和 general-purpose 子 Agent 继承此处
    subagents=[research_subagent],       # researcher 只获得 /skills/research/，不获得 /skills/main/
)
