# Haystack

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](haystack.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/haystack.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Haystack 是 deepset 的生产导向 Python 框架，用来搭 RAG pipeline、AI agent 和语义搜索——比 LangChain 更有主张、开销更低。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | deepset |
| 路线 | 生产级 RAG 和 agent 框架 |
| 是否开源 | 是，Apache 2.0 |
| 最适合 | 搭生产 RAG pipeline、搜索和 agent，想要显式 pipeline 控制和更低开销的团队 |
| 主要代价 | 生态比 LangChain 小；代码优先，无可视化构建器 |
| 官网 | https://haystack.deepset.ai |
| GitHub 仓库 | https://github.com/deepset-ai/haystack |

## 什么时候选它

- 你想要模块化、生产导向的 pipeline，支持分支、循环和条件路由。
- 你需要 RAG，支持可插拔 retriever、document store 和内置评估。
- 你在意更低的框架开销（benchmark 中 ~5.9ms vs LangChain ~10ms）。
- 你想要带工具调用和记忆的 agent 工作流，结构清晰。

## 什么时候别选

- 你需要最广的第三方生态——LangChain 的社区集成更多。
- 你想要可视化 no-code 构建器。
- 你的项目很简单，Haystack 的 pipeline 抽象杀鸡用牛刀。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| RAG pipeline | 很强 | 核心优势，可插拔 retriever 和 store |
| Pipeline 架构 | 很强 | 模块化，支持分支、循环、条件路由 |
| Agent 工作流 | 强 | 工具调用和记忆 |
| 评估 | 强 | 内置可观测性和评估 |
| 模型无关 | 很强 | OpenAI、Anthropic、Mistral、Cohere、HuggingFace、Azure、Bedrock、本地 |
| 生态规模 | 中 | 比 LangChain 小 |

## 使用代价

复杂度 Medium。文档完善、生产导向、有主张——这可以是优点。框架免费（Apache 2.0）。deepset 另有 Enterprise Starter 和 Enterprise Platform 提供托管/治理部署。

## 最后一句

Haystack 适合想要 LangChain 级能力但更重视生产纪律和更低开销的团队。代价是更小的生态和社区。
