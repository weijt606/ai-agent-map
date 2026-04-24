# MemGPT (Letta)

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](memgpt.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/memgpt.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：MemGPT（现名 Letta）是一个构建有状态 AI agent 的平台，带持久记忆，能跨会话学习和自我改进。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Letta, Inc. |
| 路线 | 带持久记忆的有状态 agent 平台 |
| 是否开源 | 是，Apache 2.0 |
| 最适合 | 需要跨会话记住上下文的 agent——长期运行的助手、个性化工作流、随时间积累的上下文 |
| 主要代价 | 记忆管理会增加额外 LLM 调用；自托管需要 Docker 和 PostgreSQL |
| 官网 | https://www.letta.com |
| GitHub 仓库 | https://github.com/letta-ai/letta |

## 命名说明

MemGPT 是论文中的设计模式（LLM 自编辑记忆）。Letta 是基于这个模式构建的框架、公司和产品。原始的 `cpacker/MemGPT` 仓库现已跳转到 `letta-ai/letta`。

## 什么时候选它

- 你需要 agent 跨会话记住信息——不只是一次对话内，而是跨越几天甚至几周。
- 你想让 agent 在固定上下文窗口内自动管理记忆，通过自编辑工具实现。
- 你需要维护 core memory、archival memory 和 recall memory 的有状态 agent。
- 你想要能从过去经验中学习并不断改进的 agent（Skill Learning）。
- 你需要基于 git 的 agent 记忆版本管理（Context Repositories）。

## 什么时候别选

- 你已经在用 LangGraph、CrewAI 或 AutoGen，想加一层记忆。Letta 会替换你的 agent 栈，不是插在旁边。
- 你需要开箱即用的多 agent 编排或可视化调试器。
- 你的任务是无状态、短周期的——所有内容都能放进单个上下文窗口。
- 你想要最简单的记忆方案。Mem0 更轻量。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 持久记忆 | 很强 | core memory + archival memory + recall memory |
| 上下文管理 | 很强 | 自编辑记忆工具，在上下文窗口内工作 |
| 有状态 | 很强 | 状态跨会话持久化 |
| 技能学习 | 强 | Agent 从过去经验中改进 |
| 记忆版本管理 | 中 | Context Repositories，基于 git |
| 多 agent 编排 | 弱 | 不是主要关注点 |
| 可视化调试器 | 弱 | 工具支持有限 |

## 使用代价

复杂度 Medium 到 High。自托管需要 Docker 和 PostgreSQL。MemGPT 架构会为记忆管理操作（读、写、搜索记忆）增加额外 LLM 调用，token 花费比无状态方案更高。基础托管成本在 Railway 上大约 $5–10/月，加上 LLM API 费用。

## 最后一句

如果你的 agent 需要"记住"，Letta 是最认真的开源选择。代价很清楚：你得到了真正的持久记忆和自我改进 agent，但要为额外的 LLM 调用和基础设施复杂度买单。
