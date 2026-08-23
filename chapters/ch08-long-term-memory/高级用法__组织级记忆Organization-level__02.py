"""
教程《Deep Agents 实战》— ch08-long-term-memory
原文位置: ch08-long-term-memory: 长期记忆 — 让 Agent 拥有跨对话的记忆 / 高级用法 / 组织级记忆（Organization-level） (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from langgraph_sdk import get_client
from deepagents.backends.utils import create_file_data

client = get_client(url="<DEPLOYMENT_URL>")

await client.store.put_item(
    (org_id,),
    "/compliance.md",
    create_file_data("""## 合规政策
- 不得披露内部定价
- 金融建议必须附加免责声明
"""),
)
