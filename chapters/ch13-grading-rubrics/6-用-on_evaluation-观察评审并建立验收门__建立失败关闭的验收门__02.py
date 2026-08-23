"""
教程《Deep Agents 实战》— ch13-grading-rubrics
原文位置: ch13-grading-rubrics: Grading Rubrics（评分量规） — 让 Agent 按验收标准自我迭代 / 6. 用 on_evaluation 观察评审并建立验收门 / 建立失败关闭的验收门 (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

# 错误：有最终消息不等于验收通过
accepted = bool(result["messages"])
