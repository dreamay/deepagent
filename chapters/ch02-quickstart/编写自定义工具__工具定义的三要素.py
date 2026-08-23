"""
教程《Deep Agents 实战》— ch02-quickstart
原文位置: ch02-quickstart: 快速上手 — 5 分钟构建你的第一个 Deep Agent / 编写自定义工具 / 工具定义的三要素
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

def internet_search(
    query: str,                          # 1. 参数名 + 类型标注
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
) -> dict:                               # 2. 返回类型
    """Run a web search for the given query."""  # 3. Docstring
    # 实际的工具逻辑
    return tavily_client.search(query, max_results=max_results, topic=topic)
