"""
教程《Deep Agents 实战》— pre02-agentseek-skills
原文位置: pre02-agentseek-skills: AgentSeek 准备篇（下）：为 AI 编码助手安装开发技能 / 5. 实操：用 langsmith-trace 定位一次慢调用（5–10 分钟） / 5.3 让编码助手分析瓶颈 (片段 2/3)
语言: typescript

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

langsmith run list --trace-ids <trace-id> --project deepagents-course --run-type llm --include-metadata --limit 100
langsmith run list --trace-ids <trace-id> --project deepagents-course --run-type tool --include-metadata --limit 100
