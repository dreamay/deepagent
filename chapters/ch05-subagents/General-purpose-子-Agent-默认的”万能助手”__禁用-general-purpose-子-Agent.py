"""
教程《Deep Agents 实战》— ch05-subagents
原文位置: ch05-subagents: 子 Agent 与上下文隔离 — 让 Agent 学会委派 / General-purpose 子 Agent：默认的”万能助手” / 禁用 general-purpose 子 Agent
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents import create_deep_agent
from deepagents.profiles import GeneralPurposeSubagentProfile, HarnessProfile, register_harness_profile

# 两步缺一不可
# 为指定模型注册 Harness Profile。
register_harness_profile(
    key="openai:zai-org/GLM-5.2",
    profile=HarnessProfile(
        general_purpose_subagent=GeneralPurposeSubagentProfile(
            enabled=False
        )
    ),
)

agent = create_deep_agent(
    model=model,
    subagents=[],  # 不传任何同步子 Agent
)
