# Julep

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](julep.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/julep.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Julep 是基于 Temporal 的工作流引擎，用来构建有状态、多步 AI agent 工作流——托管云端已关闭，目前仅支持自托管。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Julep AI, Inc. |
| 路线 | 持久化工作流引擎，用于有状态 AI agent |
| 是否开源 | 是，Apache 2.0 |
| 最适合 | 需要带自动重试的持久化多步 agent 工作流、持久记忆、分支循环和错误处理的团队 |
| 主要代价 | 只能自托管（托管云 2025 年 12 月关闭）；小团队，长期维护有风险 |
| 官网 | https://julep.ai |
| GitHub 仓库 | https://github.com/julep-ai/julep |

## 什么时候选它

- 你需要 Temporal 支撑的持久化多步 agent 工作流，带自动重试。
- 你想要带持久长期记忆和自适应上下文管理的有状态 agent。
- 你需要声明式任务定义（YAML 或代码），支持分支、循环、并行和错误处理。
- 你想要内置 RAG pipeline 和 100+ 工具集成。

## 什么时候别选

- 你想要托管云服务。托管后端 2025 年 12 月 31 日已关闭。
- 你需要大型活跃社区。Julep 社区较小（~6.6k stars，团队约 5 人）。
- 你只有简单的单轮任务。Julep 的工作流引擎杀鸡用牛刀。
- 你担心小厂商的长期维护风险。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 持久化工作流 | 很强 | Temporal 支撑，自动重试 |
| 持久记忆 | 强 | 长期记忆 + 自适应上下文 |
| 声明式任务 | 强 | YAML 或代码，支持分支、循环、并行 |
| RAG pipeline | 中 | 内置但深度不如 LlamaIndex |
| 工具集成 | 强 | 100+ 集成 |
| 托管方案 | 无 | 云端已关闭，仅自托管 |
| 社区规模 | 弱 | ~6.6k stars，小团队 |

## 使用代价

复杂度 High。自托管是唯一选项——你需要自己运维 Docker 容器、Temporal 和 PostgreSQL。LLM API 费用为透传。小团队意味着你需要认真评估长期维护风险。

## 最后一句

Julep 是有状态 agent 的认真工作流引擎——如果你愿意自托管并接受小厂商风险的话。对需要 Temporal 级持久化的 agent 工作流，它填补了一个真实缺口。
