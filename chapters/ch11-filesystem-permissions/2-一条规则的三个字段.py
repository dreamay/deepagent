"""
教程《Deep Agents 实战》— ch11-filesystem-permissions
原文位置: ch11-filesystem-permissions: 文件系统权限 — 用声明式规则控制 Agent 的读写边界 / 2. 一条规则的三个字段
语言: python

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

FilesystemPermission(
    operations=["read", "write"],
    paths=["/workspace/**", "/shared/{docs,templates}/**"],
    mode="allow",
)
