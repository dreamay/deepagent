"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / 使用方式 / 多源 Skills 与优先级
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    skills=[
        "/skills/shared/",    # 团队共享 Skills
        "/skills/project/",   # 项目专属 Skills（优先级更高）
    ],
)
