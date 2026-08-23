"""
教程《Deep Agents 实战》— ch03-virtual-filesystem
原文位置: ch03-virtual-filesystem: 虚拟文件系统 — Deep Agents 的 Context Engineering 核心 / 自定义后端与安全策略 / 安全策略：PolicyWrapper (片段 2/2)
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

from deepagents.backends.protocol import BackendProtocol, WriteResult, EditResult

class PolicyWrapper(BackendProtocol):
    def __init__(self, inner: BackendProtocol, deny_prefixes: list[str]):
        self.inner = inner
        self.deny_prefixes = [p if p.endswith("/") else p + "/" for p in deny_prefixes]

    def _deny(self, path: str) -> bool:
        return any(path.startswith(p) for p in self.deny_prefixes)

    def ls(self, path): return self.inner.ls(path)
    def read(self, file_path, offset=0, limit=2000): return self.inner.read(file_path, offset=offset, limit=limit)
    def grep(self, pattern, path=None, glob=None): return self.inner.grep(pattern, path, glob)
    def glob(self, pattern, path="/"): return self.inner.glob(pattern, path)

    def write(self, file_path: str, content: str) -> WriteResult:
        if self._deny(file_path):
            return WriteResult(error=f"写入被拒绝：{file_path}")
        return self.inner.write(file_path, content)

    def edit(self, file_path: str, old_string: str, new_string: str,
             replace_all: bool = False) -> EditResult:
        if self._deny(file_path):
            return EditResult(error=f"编辑被拒绝：{file_path}")
        return self.inner.edit(file_path, old_string, new_string, replace_all)
