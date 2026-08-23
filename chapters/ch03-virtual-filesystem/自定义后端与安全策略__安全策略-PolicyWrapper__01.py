"""
教程《Deep Agents 实战》— ch03-virtual-filesystem
原文位置: ch03-virtual-filesystem: 虚拟文件系统 — Deep Agents 的 Context Engineering 核心 / 自定义后端与安全策略 / 安全策略：PolicyWrapper (片段 1/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents.backends.filesystem import FilesystemBackend
from deepagents.backends.protocol import WriteResult, EditResult

class GuardedBackend(FilesystemBackend):
    def __init__(self, *, deny_prefixes: list[str], **kwargs):
        super().__init__(**kwargs)
        self.deny_prefixes = [p if p.endswith("/") else p + "/" for p in deny_prefixes]

    def write(self, file_path: str, content: str) -> WriteResult:
        if any(file_path.startswith(p) for p in self.deny_prefixes):
            return WriteResult(error=f"写入被拒绝：{file_path}")
        return super().write(file_path, content)

    def edit(self, file_path: str, old_string: str, new_string: str,
             replace_all: bool = False) -> EditResult:
        if any(file_path.startswith(p) for p in self.deny_prefixes):
            return EditResult(error=f"编辑被拒绝：{file_path}")
        return super().edit(file_path, old_string, new_string, replace_all)
