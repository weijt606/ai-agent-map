# Ruflo

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](ruflo.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/ruflo.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Ruflo 是 Claude Code 的多 agent 编排平台——把 orchestration layer 推到跨机器联邦、神经记忆和 100+ 专用 agent 的规模。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | RuvNet（开源，前身 "Claude Flow"） |
| 路线 | Claude Code 的工作流 / orchestration layer |
| 开源 | 是（MIT） |
| 适合谁 | 需要在多台机器上跑多种专用 agent、要持久记忆和联邦通信的团队 |
| 主要代价 | 表面积明显比 [oh-my-claudecode](oh-my-claudecode.md) 大——联邦、向量记忆、Web UI、神经架构都在同一个项目里 |
| GitHub 仓库 | https://github.com/ruvnet/ruflo |

## 什么时候选它

- 你已经在用 Claude Code，想往团队 / 跨机器协同 swarm 的方向扩。
- 你想一次拿到 HNSW 索引的向量记忆、联邦式 agent 通信、自学习 skill 管道。
- 你想要 Web UI（flo.ruv.io）和独立的 goal 规划界面（goal.ruv.io）配合 CLI 用。

## 什么时候不选

- 你只需要单开发者的 orchestration——[oh-my-claudecode](oh-my-claudecode.md) 更轻、更合适。
- 你想要厂商托管的平台；Ruflo 是开源自托管。
- 你想要极简、有意见的 skill 层——Superpowers 是框架那一端，oh-my-claudecode 是策展那一端，Ruflo 是同一空间里联邦 / 企业那一端。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 多 agent 协同 | 非常强 | 100+ 专用 agent，swarm 协调 |
| 跨机器联邦 | 非常强 | 在不同机器和信任边界之间安全联邦 |
| 记忆与检索 | 强 | HNSW 索引的向量记忆，加上 "SONA" 神经架构做自学习 |
| 插件集成 | 强 | 32 个 Claude Code 插件；支持多种 LLM provider |
| 单用户轻量使用 | 中 | 能用，但相对简单工作流层是大材小用 |

## 使用成本

复杂度：高。Ruflo 把联邦、向量记忆、神经模式学习、独立 Web UI 都打包在一个项目里。收益跟团队和机器数量正相关——单开发者用一般不太划算，apparatus 多于任务本身。

## 底线

Ruflo（前身 Claude Flow）是 orchestration layer 朝企业端长出来的样子：跨机器联邦、向量记忆、Web UI、100+ 专用 agent。和 [oh-my-claudecode](oh-my-claudecode.md) 比，它是同一条路线上更重、更野心大的那一端。如果你是单开发者在本地用 Claude Code，oh-my-claudecode 大概率更合适。如果你是团队多人跨机器用 Claude Code，需要跨机协调和持久记忆，那从 Ruflo 开始看。
