# ch14-streaming

**章节标题**：Streaming — 实时观察主 Agent、子 Agent 与工具调用

本页文件由教程 HTML 直接抽取。文件扩展名根据内容启发式确定 (.py / .sh / .toml / .json / .yaml / .md / .txt)。Python 文件已通过 `ast.parse` 语法检查；其余类型仅保证结构与原文一致。

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 1. 一次“看起来卡住”的研究请求

- 片段 1/2 (python): [`1-一次“看起来卡住”的研究请求__01.py`](1-一次“看起来卡住”的研究请求__01.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 1. 一次“看起来卡住”的研究请求

- 片段 2/2 (illustrative): [`1-一次“看起来卡住”的研究请求__02.txt`](1-一次“看起来卡住”的研究请求__02.txt)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 2. 先让案例稳定复现

- 片段 1/1 (python): [`2-先让案例稳定复现.py`](2-先让案例稳定复现.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 3. 第一个修复：先显示“研究助手已启动” / 3.1 不要先从 graph node 猜产品状态

- 片段 1/1 (python): [`3-第一个修复-先显示“研究助手已启动”__31-不要先从-graph-node-猜产品状态.py`](3-第一个修复-先显示“研究助手已启动”__31-不要先从-graph-node-猜产品状态.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 3. 第一个修复：先显示“研究助手已启动” / 3.3 path 、 namespace 和 ns 是什么关系

- 片段 1/2 (illustrative): [`3-第一个修复-先显示“研究助手已启动”__33-path-、-namespace-和-ns-是什么关系__01.txt`](3-第一个修复-先显示“研究助手已启动”__33-path-、-namespace-和-ns-是什么关系__01.txt)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 3. 第一个修复：先显示“研究助手已启动” / 3.3 path 、 namespace 和 ns 是什么关系

- 片段 2/2 (python): [`3-第一个修复-先显示“研究助手已启动”__33-path-、-namespace-和-ns-是什么关系__02.py`](3-第一个修复-先显示“研究助手已启动”__33-path-、-namespace-和-ns-是什么关系__02.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 3. 第一个修复：先显示“研究助手已启动” / 3.4 Projection 是按需打开的

- 片段 1/1 (python): [`3-第一个修复-先显示“研究助手已启动”__34-Projection-是按需打开的.py`](3-第一个修复-先显示“研究助手已启动”__34-Projection-是按需打开的.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 4. 第二个修复：让用户知道它在查什么

- 片段 1/1 (python): [`4-第二个修复-让用户知道它在查什么.py`](4-第二个修复-让用户知道它在查什么.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 4. 第二个修复：让用户知道它在查什么 / 4.1 message 应该读什么

- 片段 1/2 (python): [`4-第二个修复-让用户知道它在查什么__41-message-应该读什么__01.py`](4-第二个修复-让用户知道它在查什么__41-message-应该读什么__01.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 4. 第二个修复：让用户知道它在查什么 / 4.1 message 应该读什么

- 片段 2/2 (illustrative): [`4-第二个修复-让用户知道它在查什么__41-message-应该读什么__02.txt`](4-第二个修复-让用户知道它在查什么__41-message-应该读什么__02.txt)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 5. 第三个修复：工具调用也要能被看见

- 片段 1/1 (python): [`5-第三个修复-工具调用也要能被看见.py`](5-第三个修复-工具调用也要能被看见.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 5. 第三个修复：工具调用也要能被看见 / 5.1 拆解 tool_call

- 片段 1/3 (python): [`5-第三个修复-工具调用也要能被看见__51-拆解-tool_call__01.py`](5-第三个修复-工具调用也要能被看见__51-拆解-tool_call__01.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 5. 第三个修复：工具调用也要能被看见 / 5.1 拆解 tool_call

- 片段 2/3 (text): [`5-第三个修复-工具调用也要能被看见__51-拆解-tool_call__02.txt`](5-第三个修复-工具调用也要能被看见__51-拆解-tool_call__02.txt)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 5. 第三个修复：工具调用也要能被看见 / 5.1 拆解 tool_call

- 片段 3/3 (python): [`5-第三个修复-工具调用也要能被看见__51-拆解-tool_call__03.py`](5-第三个修复-工具调用也要能被看见__51-拆解-tool_call__03.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 6. 顺序乱了：两种方式修复实时消费 / 6.1 异步服务：并发消费

- 片段 1/1 (python): [`6-顺序乱了-两种方式修复实时消费__61-异步服务-并发消费.py`](6-顺序乱了-两种方式修复实时消费__61-异步服务-并发消费.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 6. 顺序乱了：两种方式修复实时消费 / 6.2 同步程序：使用 interleave

- 片段 1/1 (python): [`6-顺序乱了-两种方式修复实时消费__62-同步程序-使用-interleave.py`](6-顺序乱了-两种方式修复实时消费__62-同步程序-使用-interleave.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 7. 页面开始工作后，才需要精确顺序

- 片段 1/1 (python): [`7-页面开始工作后，才需要精确顺序.py`](7-页面开始工作后，才需要精确顺序.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data

- 片段 1/5 (python): [`8-旧代码为什么还在处理-type-ns-data__01.py`](8-旧代码为什么还在处理-type-ns-data__01.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data

- 片段 2/5 (illustrative): [`8-旧代码为什么还在处理-type-ns-data__02.txt`](8-旧代码为什么还在处理-type-ns-data__02.txt)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data

- 片段 3/5 (python): [`8-旧代码为什么还在处理-type-ns-data__03.py`](8-旧代码为什么还在处理-type-ns-data__03.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data

- 片段 4/5 (python): [`8-旧代码为什么还在处理-type-ns-data__04.py`](8-旧代码为什么还在处理-type-ns-data__04.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 8. 旧代码为什么还在处理 type/ns/data

- 片段 5/5 (python): [`8-旧代码为什么还在处理-type-ns-data__05.py`](8-旧代码为什么还在处理-type-ns-data__05.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 9. 需要自定义进度时，先定义自己的事件

- 片段 1/1 (python): [`9-需要自定义进度时，先定义自己的事件.py`](9-需要自定义进度时，先定义自己的事件.py)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 10. 从“能看到”到“能交付”

- 片段 1/1 (illustrative): [`10-从“能看到”到“能交付”.txt`](10-从“能看到”到“能交付”.txt)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 11. 一次最小实验：运行专用 Streaming 应用

- 片段 1/2 (shell): [`11-一次最小实验-运行专用-Streaming-应用__01.sh`](11-一次最小实验-运行专用-Streaming-应用__01.sh)

## Streaming — 实时观察主 Agent、子 Agent 与工具调用 / 11. 一次最小实验：运行专用 Streaming 应用

- 片段 2/2 (shell): [`11-一次最小实验-运行专用-Streaming-应用__02.sh`](11-一次最小实验-运行专用-Streaming-应用__02.sh)

