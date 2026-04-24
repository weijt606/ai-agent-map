# Flowise

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](flowise.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/flowise.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Flowise 是开源的拖拽式可视化构建器，用来搭 LLM 应用和 AI agent——本质上是 LangChain 的 no-code UI。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | FlowiseAI（Y Combinator S23） |
| 路线 | 可视化 LLM 应用和 agent 构建器 |
| 是否开源 | 是，Apache 2.0 |
| 最适合 | 想不写代码就搭 RAG chatbot 和 agent 流程的团队 |
| 主要代价 | 复杂流程变脆弱、难调试；控制力不如代码优先框架 |
| 官网 | https://flowiseai.com |
| GitHub 仓库 | https://github.com/FlowiseAI/Flowise |

## 什么时候选它

- 你想用可视化拖拽画布搭 chatflow（RAG pipeline、chatbot）和 agentflow（多步、带工具的 agent）。
- 你想把 flow 暴露为 REST API，不用写后端代码。
- 你需要原生向量数据库支持——Pinecone、Qdrant、Chroma 等。
- 你想从市场里的预建模板快速开始。

## 什么时候别选

- 你需要生产级、大规模编排。复杂可视化流程会变脆弱。
- 你是代码优先团队，想要细粒度控制。直接用 LangChain 或 LangGraph。
- 你需要通用工作流自动化（邮件、数据库、Webhook）。n8n 在那方面更强。
- 你需要严格安全——2026 年初披露了一个 CVSS 10.0 RCE 漏洞。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 可视化构建器 | 很强 | chatflow 和 agentflow 的拖拽画布 |
| RAG / chatbot | 强 | 原生向量 DB 支持，预建模板 |
| API 暴露 | 强 | 把 flow 暴露为 REST API |
| Agent flow | 中 | 多步带工具的 agent，但控制力不如代码 |
| LLM 支持 | 强 | 所有主流 provider |
| 生产规模 | 弱 | 复杂 flow 变脆弱 |
| 非 AI 工作流 | 弱 | AI 优先；LLM 场景之外能力很有限 |

## 使用代价

复杂度 Low 到 Medium。用 Docker 或 Node.js 自托管，或用 Flowise Cloud。可视化构建器对非开发者友好。真正的限制在规模上——flow 复杂度增长时，调试和可靠性比代码优先框架更难。

## 最后一句

Flowise 是从零到可用 LLM 应用最快的路径，不用写代码。它是可视化版的 LangChain。代价是：你得到了可访问性，但失去了代码优先团队在规模化时需要的控制力。
