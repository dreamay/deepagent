"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / Skill 权限控制 / 只读 Skills（企业知识库场景） (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

agent.invoke(
    {"messages": [{"role": "user", "content": "列出可用 Skills"}]},
    context=TenantContext(org_id="org-acme"),
    config={"configurable": {"thread_id": "1"}},
)
