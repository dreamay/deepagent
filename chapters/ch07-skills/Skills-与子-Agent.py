"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / Skills 与子 Agent
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent

research_subagent = {
    "name": "researcher",
    "description": "Research assistant with specialized skills",
    "system_prompt": "You are a researcher.",
    "tools": [web_search],
    "skills": ["/skills/research/", "/skills/web-search/"],  # 子 Agent 专属 Skills
}

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    skills=["/skills/main/"],              # 主 Agent 和 GP 子 Agent 使用
    subagents=[research_subagent],          # researcher 只有自己的 Skills
)
