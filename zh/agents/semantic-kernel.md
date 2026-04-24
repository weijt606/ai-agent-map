# Semantic Kernel

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](semantic-kernel.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/semantic-kernel.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Semantic Kernel 是微软的开源 SDK，用来搭 AI 编排应用——.NET 和 Azure 生态团队的自然选择。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Microsoft |
| 路线 | 企业级 AI 编排 SDK |
| 是否开源 | 是，MIT |
| 最适合 | .NET、Python 或 Java 团队，想要类型安全、企业级 AI 编排，且和 Azure 对齐 |
| 主要代价 | 在微软生态里最强；Python 社区和第三方集成不如 LangChain 广 |
| 官网 | https://learn.microsoft.com/semantic-kernel |
| GitHub 仓库 | https://github.com/microsoft/semantic-kernel |

## 什么时候选它

- 你的技术栈是 .NET、C# 或 Java，想要自己语言的一等公民 AI 编排。
- 你在 Azure OpenAI 上构建，想要原生、维护良好的连接器。
- 你需要插件系统——模块化的函数组（prompt 型或 native code），可组合、可复用。
- 你想从用户目标自动生成多步执行计划（Planners）。
- 你需要内置 agent 框架，支持多 agent 模式、工具调用和对话管理。

## 什么时候别选

- 你的技术栈以 Python 为主，需要最广的社区生态。LangChain 在那边更大。
- 你需要非微软模型 provider 的深度原生支持。
- 你想要可视化 no-code 构建器。
- 你要的是成品 coding agent，不是编排 SDK。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| AI 编排 | 很强 | 核心能力——LLM 调用和 native code 无缝串联 |
| 插件系统 | 很强 | 模块化、可组合、可复用的函数组 |
| Planners | 强 | 从目标自动生成多步计划 |
| Agent 框架 | 强 | 多 agent、工具调用、对话管理 |
| Memory / RAG | 中 | 向量存储连接器支持 Azure AI Search、Qdrant、Chroma |
| 语言支持 | 很强 | C#/.NET（最成熟）、Python、Java |
| Azure 对齐 | 很强 | 原生 Azure OpenAI 集成 |
| 非微软 provider | 中 | 支持但不如 LangChain 深 |

## 使用代价

复杂度 Medium。文档完善、企业级、强类型。SDK 免费（MIT）。如果你已经在微软生态里，集成很顺滑。如果不在，LangChain 更广的社区和第三方集成可能更实用。

## 最后一句

Semantic Kernel 是微软世界里的 LangChain——类型安全、企业级、Azure 原生。如果你的团队写 C# 或 Java，它是 AI 编排的第一选择。
