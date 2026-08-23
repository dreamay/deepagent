"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 高级用法 / 情景记忆（Episodic Memory）
语言: typescript

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph_sdk import get_client
from langchain.tools import tool, ToolRuntime

client = get_client(url="<DEPLOYMENT_URL>")


def current_user_id(runtime: ToolRuntime) -> str:
    if runtime.server_info and runtime.server_info.user:
        return runtime.server_info.user.identity
    user_id = getattr(runtime.context, "user_id", None)
    if user_id:
        return user_id
    raise ValueError("需要在 server_info 或 runtime.context 中提供 user_id")


@tool
async def search_past_conversations(query: str, runtime: ToolRuntime) -> str:
    """搜索过去的对话以获取相关上下文。"""
    user_id = current_user_id(runtime)
    threads = await client.threads.search(
        metadata={"user_id": user_id},
        limit=5,
    )
    results = []
    for thread in threads:
        history = await client.threads.get_history(thread_id=thread["thread_id"])
        results.append(history)
    return str(results)
