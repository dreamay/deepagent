"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / Progressive Disclosure：渐进式加载 / 匹配流程示例
语言: shell

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

用户："帮我查一下 LangGraph 的 interrupt 机制"

Agent 思考：
  - 扫描 Skills 列表...
  - langgraph-docs: "Use this skill for requests related to LangGraph..." ← 匹配！
  - 读取 /skills/langgraph-docs/SKILL.md 完整内容
  - 按照指令执行：fetch_url → 选择文档 → 阅读 → 回答
