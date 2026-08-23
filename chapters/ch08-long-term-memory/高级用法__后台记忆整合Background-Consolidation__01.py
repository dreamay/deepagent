"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 高级用法 / 后台记忆整合（Background Consolidation） (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from datetime import datetime, timedelta, timezone
from deepagents import create_deep_agent
from langchain.tools import tool, ToolRuntime
from langgraph_sdk import get_client

sdk_client = get_client(url="<DEPLOYMENT_URL>")


def current_user_id(runtime: ToolRuntime) -> str:
    if runtime.server_info and runtime.server_info.user:
        return runtime.server_info.user.identity
    user_id = getattr(runtime.context, "user_id", None)
    if user_id:
        return user_id
    raise ValueError("需要在 server_info 或 runtime.context 中提供 user_id")


@tool
async def search_recent_conversations(query: str, runtime: ToolRuntime) -> str:
    """搜索过去 6 小时内该用户的对话。"""
    user_id = current_user_id(runtime)
    since = datetime.now(timezone.utc) - timedelta(hours=6)
    threads = await sdk_client.threads.search(
        metadata={"user_id": user_id},
        updated_after=since.isoformat(),
        limit=20,
    )
    conversations = []
    for thread in threads:
        history = await sdk_client.threads.get_history(thread_id=thread["thread_id"])
        conversations.append(history["values"]["messages"])
    return str(conversations)

consolidation_agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="审查最近对话并更新用户记忆文件。合并新事实、移除过期信息、保持简洁。",
    tools=[search_recent_conversations],
)
