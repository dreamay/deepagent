"""
教程《Deep Agents 实战》— ch12-mcp
原文位置: ch12-mcp: MCP — 用标准协议扩展 Deep Agents 工具生态 / 9. 错误语义与 Interceptor / Client Interceptor 不是 Agent Middleware
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langchain.messages import ToolMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.interceptors import MCPToolCallRequest


async def require_authentication(
    request: MCPToolCallRequest,
    handler,
):
    is_authenticated = request.runtime.state.get("authenticated", False)
    if (
        request.server_name == "orders"
        and request.name == "cancel"
        and not is_authenticated
    ):
        return ToolMessage(
            content="Authentication required.",
            tool_call_id=request.runtime.tool_call_id,
            status="error",
        )
    return await handler(request)


client = MultiServerMCPClient(
    connections,
    tool_interceptors=[require_authentication],
)
