"""
教程《Deep Agents 实战》— ch07-skills
原文位置: ch07-skills: Skills — 可复用的 Agent 能力包 / 用 Skills 执行代码 / 解释器技能（Interpreter Skills） (片段 2/4)
语言: markdown

本文件直接从教程 HTML 中提取,代码与原文一致;仅调整了缩进/换行以保证语法合法。
"""

---
name: order-helpers
description: Helper functions for normalizing and grouping order records.
metadata:
  entrypoint: scripts/index.ts
---

# order-helpers

Use this skill when order records need deterministic cleanup or aggregation.

Import these utilities into the REPL:

```typescript
const { groupByStatus } = await import("@/skills/order-helpers");
groupByStatus(...);
```
