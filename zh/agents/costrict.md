# CoStrict

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](costrict.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/costrict.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：CoStrict（诸葛神码）是一个企业优先的 coding agent，基于 Cline / Roo Code 血统，但围绕那些工具留给你自己做的两件事重建——标准化的"严格"生成流程（需求 → 架构 → 任务计划 → 测试）和仓库级 AI 代码评审——并把私有化、物理隔离部署做成一等公民。

> **血统与厂商：** CoStrict（`zgsm-ai/costrict`，即"诸葛神码 / 神码"项目，由 zgsm-sangfor 团队维护）是 Cline / Roo Code / kilo-code 家族的下游。它保留编辑器 agent 的形态，在上面加了一层企业管控。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | zgsm-ai（CoStrict / 诸葛神码，深信服） |
| 路线 | review-first 自动化——企业、私有化部署 |
| 开源 | 是（Apache-2.0） |
| 实现 | TypeScript |
| 表面 | VS Code、JetBrains、CLI、Cloud（实验性） |
| 模型 | 内置免费模型 + Anthropic、OpenAI、OpenAI 兼容、本地模型 |
| 适合谁 | 需要标准化、可评审的 AI 编码，且要本地/隔离部署的组织 |
| 主要代价 | 企业化框架（严格流程、评审关卡）对单人/快速迭代是负担 |
| GitHub 仓库 | https://github.com/zgsm-ai/costrict |

## 什么时候选它

- 你在企业里，需要**私有化部署**——物理隔离 + 端到端加密——而不是把代码发给托管厂商。
- 你希望代码生成走**标准化流程**（需求分析、架构设计、任务规划、测试生成），而不是自由 prompt，让产出可审计、团队间一致。
- 你想要**仓库级 AI 代码评审**（RAG 索引 + 多模型校验）和写代码的工具接在一起，跑在 VS Code 或 JetBrains 里。

## 什么时候不选

- 你是单人开发或想要最快的循环——严格流程和评审关卡是 [Aider](aider.md) 或 [Claude Code](claude-code.md) 这类终端 CLI 避开的负担。
- 你想要终端原生的单进程 agent——CoStrict 主要是 IDE 插件；CLI 那一档看[终端编码 CLI 对比](../comparisons/coding-cli-agents.md)。
- 你已经标准化在 [Cline](cline.md) 上、不需要这层企业管控——上游血统可能就够了。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 严格 / 标准化生成 | 非常强 | 头号差异点——需求 → 架构 → 任务 → 测试 |
| 仓库级代码评审 | 强 | RAG 索引、多模型校验、接 Git/SCM |
| 私有 / 隔离部署 | 强 | 物理隔离 + 端到端加密；企业卖点 |
| 编辑器覆盖 | 强 | VS Code + JetBrains，外加 CLI 和实验性 cloud |
| 多 provider 支持 | 强 | Anthropic、OpenAI、OpenAI 兼容、本地模型 |
| 单人 / 快速迭代契合度 | 偏弱 | 管控层在团队场景外是负担 |

## 使用成本

复杂度：中。作为 IDE 插件安装很简单，但价值主张——严格流程、评审关卡、私有化部署——是面向有相应流程和基础设施的团队的。自托管隔离部署是实打实的运维工作；对它瞄准的企业来说这正是目的，对个人则是错配。

## 底线

CoStrict 是本仓库 coding agent 集合里"企业管控层"这一档：一个 Cline 血统的 IDE agent，用自由发挥的速度换取标准化、可评审、可私有部署的 AI 开发。如果你的卡点是治理——可审计的生成、循环内代码评审、本地隔离——它是个强力的开源选项。如果你想要快速的个人循环，终端 CLI（[Aider](aider.md)、[Claude Code](claude-code.md)，或[这里](../comparisons/coding-cli-agents.md)对比的厂商 CLI）更合适；如果你想要不带企业脚手架的基础编辑器 agent，[Cline](cline.md) 是上游。
