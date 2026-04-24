# Pydantic AI

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](pydantic-ai.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/pydantic-ai.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Pydantic AI 是类型安全的 Python agent 框架——结构化输出、依赖注入、IDE 自动补全，为生产级 AI 应用设计。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Pydantic Inc.（Samuel Colvin） |
| 路线 | 类型安全 agent 框架 |
| 是否开源 | 是，MIT |
| 最适合 | 想要类型安全、结构化输出和可测试 agent 架构的 Python 团队 |
| 主要代价 | 集成生态比 LangChain 小；仅支持 Python |
| 官网 | https://ai.pydantic.dev |
| GitHub 仓库 | https://github.com/pydantic/pydantic-ai |

## 什么时候选它

- 你想要完整的类型安全——IDE 自动补全、静态类型检查、写代码时就能发现错误。
- 你需要通过 Pydantic model 做结构化输出，响应经过验证、符合 schema。
- 你看重依赖注入，想要干净、可测试的 agent 架构。
- 你需要 MCP 支持、human-in-the-loop 工具审批和持久化执行。
- 你用 FastAPI，想要自然配合的 agent 框架。

## 什么时候别选

- 你需要大量预建集成。LangChain 的连接器更多。
- 你需要复杂的多 agent 有状态编排。LangGraph 在这方面更强。
- 你不在 Python 生态里。
- 你想要可视化构建器或 no-code 体验。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 类型安全 | 很强 | 核心设计——完整 IDE 支持和静态检查 |
| 结构化输出 | 很强 | Pydantic model 验证 |
| 依赖注入 | 很强 | 干净可测试的 agent 设计 |
| 模型支持 | 强 | OpenAI、Anthropic、Gemini、Mistral、Bedrock、Ollama 等 |
| MCP 支持 | 强 | 内置 |
| 持久化执行 | 中 | 能扛住 API 故障和重启 |
| 集成生态 | 中 | 在增长但比 LangChain 小 |
| 多 agent 编排 | 弱 | 不是主要设计方向 |

## 使用代价

复杂度 Low 到 Medium。如果你已经会 Pydantic 和 FastAPI，学习曲线很小。框架比 LangChain 更精简、更显式（等效应用约 160 行 vs 170 行）。可观测性通过 Pydantic Logfire（基于 OpenTelemetry）。

## 最后一句

Pydantic AI 是用类型思考的团队的 agent 框架。生态不如 LangChain 广，但架构更干净，生产环境里意外更少。
