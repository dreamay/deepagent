"""
教程《Deep Agents 实战》— ch03-virtual-filesystem
原文位置: ch03-virtual-filesystem: 虚拟文件系统 — Deep Agents 的 Context Engineering 核心 / 可插拔的存储后端 / FilesystemBackend：本地磁盘
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents.backends import FilesystemBackend

agent = create_deep_agent(
    model=model,
    backend=FilesystemBackend(root_dir=".", virtual_mode=True)
)
