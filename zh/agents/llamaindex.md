# LlamaIndex

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](llamaindex.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/llamaindex.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：LlamaIndex 是构建 RAG 和 agentic 应用的数据框架——当你的 agent 需要基于自己的文档和数据推理时，它最强。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | LlamaIndex, Inc. |
| 路线 | 数据优先的 agent 和 RAG 框架 |
| 是否开源 | 是，MIT |
| 最适合 | 需要对文档、数据库、API 做摄取、索引、推理的应用 |
| 主要代价 | 为生产环境调优 chunking、索引和检索质量需要投入精力 |
| 官网 | https://www.llamaindex.ai |
| GitHub 仓库 | https://github.com/run-llama/llama_index |

## 什么时候选它

- 你的 agent 需要基于自己的数据推理——文档、PDF、SQL、API。
- 你需要生产级 RAG，带高级索引、chunking 和 re-ranking。
- 你需要开箱 300+ 数据连接器。
- 你想在强检索基础上构建 agent 能力（ReAct agent、tool calling）。
- 你需要事件驱动的 Workflows 做多步 agent 编排，支持分支和并行执行。

## 什么时候别选

- 你需要复杂的有状态多 agent 编排，带条件逻辑和 human-in-the-loop。LangGraph 在这方面更强。
- 你没有检索需求，只想做简单的 prompt chain。
- 你想要可视化的 no-code agent 构建器。看 n8n 或 AutoGPT。
- 你想要一个成品 coding agent，不是框架。看 Claude Code 或 Cursor。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| RAG / 检索 | 很强 | 核心优势——高级索引、chunking、re-ranking |
| 数据连接器 | 很强 | 300+ 集成，覆盖文档、数据库、API |
| Agent 框架 | 强 | ReAct agent、tool calling、Agent Workflows |
| 工作流编排 | 中 | 事件驱动 Workflows 引擎，但控制力不如 LangGraph |
| MCP 支持 | 中 | 2026 年新增 MCP server 支持 |
| 多 agent 编排 | 弱 | 不是主要设计方向 |
| 可视化构建器 | 无 | 代码优先框架 |

## 使用代价

复杂度 Medium。框架本身免费（MIT）。成本来自 LLM API 调用（embedding + 推理）。真正的精力在调优检索质量——为你的数据选择合适的 chunking 策略、索引类型和 re-ranker。很多生产系统会把 LlamaIndex 做检索和 LangGraph 做编排配合使用。

## 最后一句

如果你的 agent 需要真正了解你的数据，LlamaIndex 是最强的检索基座。它不是通用 agent 编排器——它是让其他 agent 变得更聪明的检索层。
