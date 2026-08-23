"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 10. 与 Deep Agents 安全机制组合 / 对副作用工具配置 HITL
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver


agent = create_deep_agent(
    model=model,
    tools=billing_tools,
    interrupt_on={
        "billing_charge_card": {
            "allowed_decisions": ["approve", "reject"],
        }
    },
    checkpointer=InMemorySaver(),
)
