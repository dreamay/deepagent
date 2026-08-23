"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / 结构化输出：让子 Agent 返回 JSON
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from pydantic import BaseModel, Field
from deepagents import create_deep_agent

class ResearchFindings(BaseModel):
    summary: str = Field(description="研究摘要")
    confidence: float = Field(description="置信度 0-1")
    sources: list[str] = Field(description="信息来源 URL 列表")

research_subagent = {
    "name": "researcher",
    "description": "研究特定主题并返回结构化发现",
    "system_prompt": "深入研究给定主题，返回你的发现。",
    "tools": [internet_search],
    "response_format": ResearchFindings,  # 需要 deepagents>=0.5.3
}

agent = create_deep_agent(model=model, subagents=[research_subagent])
# 主 Agent 的 ToolMessage 将收到：
# '{"summary": "...", "confidence": 0.87, "sources": ["https://..."]}'
