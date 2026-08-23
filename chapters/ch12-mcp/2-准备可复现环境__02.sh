"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 2. 准备可复现环境 (片段 2/3)
语言: shell

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

python -m venv .venv
source .venv/bin/activate
python -m pip install "deepagents==0.6.12" "langchain-mcp-adapters>=0.3,<0.4" "mcp>=1.28,<2" langchain-openai
