# CrewAI

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](crewai.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/crewai.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：CrewAI 是一个 Python 框架，用来编排基于角色的 AI agent 团队协作完成复杂任务。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | CrewAI Inc. |
| 路线 | 多 agent 编排框架 |
| 是否开源 | 是，MIT |
| 最适合 | 想让多个 agent 按角色分工协作——研究员、写手、审稿人——快速搭原型 |
| 主要代价 | agent 数量越多 token 花费越高；复杂条件逻辑需要转向 LangGraph |
| 官网 | https://crewai.com |
| GitHub 仓库 | https://github.com/crewAIInc/crewAI |

## 什么时候选它

- 你想按角色、目标和背景定义 agent，然后让它们作为 crew 协作。
- 你需要顺序、层级或并行的任务管线，agent 之间可以互相委派。
- 你想快速搭多 agent 原型，不想一上来就面对陡峭学习曲线。
- 你需要 MCP 和 A2A 协议支持。
- 你想自由选模型——OpenAI、Anthropic、本地 LLM 都行。

## 什么时候别选

- 你需要复杂分支、循环和条件状态机。LangGraph 在这方面更强。
- 你需要对执行图和 human-in-the-loop 审批有精细控制。
- 你需要开箱即用的生产级可观测性（需要付费 Enterprise）。
- 你要的是一个成品 agent 产品，不是搭建用的框架。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 角色型 agent | 很强 | 核心设计模式——每个 agent 有 role、goal、backstory |
| 任务管线 | 强 | 支持顺序、层级、并行 |
| Agent 委派 | 强 | Agent 可以将任务委派给其他 agent |
| 记忆 | 中 | 内置短期和长期记忆 |
| 工具调用 | 强 | Agent 可调用工具和 API |
| MCP / A2A | 中 | 2026 年已支持 |
| 可视化构建器 | 中 | 付费 Enterprise 平台提供 |
| 状态机控制 | 弱 | 不是为图式条件逻辑设计的 |

## 使用代价

复杂度 Medium。开源核心免费，上手快——定义角色、组建 crew、运行。真实成本在 LLM API token 上：每次 agent 调用就是一次模型调用，多 agent crew 的花费成倍增长。付费云计划从 $99/月到 $120K/年（Enterprise）。

## 最后一句

CrewAI 是角色协作型多 agent 原型的最快路径。常见模式：先在 CrewAI 里快速搭建，如果需要更深的状态控制再迁移到 LangGraph。
