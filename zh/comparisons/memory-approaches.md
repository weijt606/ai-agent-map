# Agent 记忆方案对比

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](memory-approaches.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/memory-approaches.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

记忆是把"无状态工具"和"真正懂你项目或你生活的 agent"分开的那根轴。整个 2026 年，它成了本图上最响的差异点之一——[MiMoCode](../agents/mimocode.md) 和 [jcode](../agents/jcode.md) 都拿它打头，[Letta](../agents/memgpt.md) 整个围着它建，自托管运行时也把它当招牌强项。

但"有记忆"这句话，藏起来的比它说出来的多。这些项目说的"记忆"根本不是一回事。本页按它们*怎么*记来分类，好让你把机制对上你真正需要持久化的东西。

## 六种方案一览

| 方案 | 怎么记 | 代表 | 你需要持久化什么时选它 |
| --- | --- | --- | --- |
| 自编辑托管记忆 | agent 在上下文窗口内编辑自己的 core / archival / recall 存储 | [Letta (MemGPT)](../agents/memgpt.md) | 由 agent 自己策展的长期对话状态 |
| 被动语义召回 | 每一轮嵌入成向量；记忆图谱自动注入相关历史 | [jcode](../agents/jcode.md) | 不用手动调记忆工具的跨会话连续性 |
| 文件 / 关键词项目记忆 | 人类可读文件（`MEMORY.md`、checkpoint），关键词检索取回 | [MiMoCode](../agents/mimocode.md)、Claude Code（`CLAUDE.md`） | 跨运行留存、且可查看的项目理解 |
| 预索引代码知识图谱 | 代码库解析成可查询的图/库，按需查询 | [CodeGraph](../agents/codegraph.md) | 架构级代码上下文，不是对话 |
| 个人数据记忆树 | 连接器把你的工具同步进分层摘要存储 | [OpenHuman](../agents/openhuman.md) | agent 关于*你*知道什么——邮件、笔记、日历 |
| 长驻运行时记忆 | 记忆是常驻自托管环境里的一个子系统 | [Hermes Agent](../agents/hermes-agent.md)、[Mercury Agent](../agents/mercury-agent.md) | 跨渠道、跨设备、跨时间的持久状态 |

## 自编辑托管记忆 —— [Letta (MemGPT)](../agents/memgpt.md)

把研究范式（MemGPT）落地：agent 维护 **core memory**、**archival memory**、**recall memory**，用显式工具编辑它们，好在固定上下文窗口里保持有用。这是最有章法、最可移植的设计——它是你拿来建有状态 agent 的框架，不是成品 CLI。代价很实：额外的 LLM 调用和基础设施。如果你 agent 的全部职责就是记住并随时间自我改进，这是认真的开源底座。

## 被动语义召回 —— [jcode](../agents/jcode.md)

jcode 把每一轮嵌入成语义向量，用余弦相似度查一张**记忆图谱**，自动把相关历史注入对话——可选一个校验 side-agent 在注入前检查相关性。重点是召回*不靠模型调记忆工具*，所以它既不遗忘、也不为盯记忆烧 token。你想用时，显式记忆工具和会话检索（对历史会话的传统 RAG）也都在。取舍：如果你想调"召回什么"，它就是多一个要理解的子系统。

## 文件 / 关键词项目记忆 —— [MiMoCode](../agents/mimocode.md)、Claude Code

务实、透明的那一端。[MiMoCode](../agents/mimocode.md) 维护项目 `MEMORY.md`、自动会话 checkpoint、scratch 笔记、逐任务进度，恢复时通过 **SQLite FTS5** 关键词检索注回。[Claude Code](../agents/claude-code.md) 的 `CLAUDE.md` 惯例是同一想法的最轻版本。强项是记忆就是一个你能读、能改、能提交的纯文件——没有黑箱。局限是关键词检索：它召回匹配的，不是语义相关的。

## 预索引代码知识图谱 —— [CodeGraph](../agents/codegraph.md)

另一种记忆：不是对话，是**代码库**。CodeGraph 把仓库（Tree-sitter + SQLite + FTS5）解析成本地可查询的知识图谱，通过 MCP 提供，让 Claude Code、Cursor、Codex 这类 agent 用少得多的工具调用和 token 回答架构问题。它是你挂到别的 agent 上的上下文基础设施，在从头扫描代价很高的中大型仓库上回本。

## 个人数据记忆树 —— [OpenHuman](../agents/openhuman.md)

指向你生活、而不是你代码的记忆。[OpenHuman](../agents/openhuman.md) 自动把 Gmail、Notion、GitHub、Slack 和 118+ 工具同步进本地**记忆树**——SQLite 里的分层摘要，镜像到一个可浏览可编辑的 Obsidian 兼容 wiki。价值是助手对*你*从不冷启动；代价是它要几周的自动抓取循环才攒得起来，而且你要接受 GPL-3.0 以及把所有东西本地同步带来的数据驻留问题。

## 长驻运行时记忆 —— [Hermes Agent](../agents/hermes-agent.md)、[Mercury Agent](../agents/mercury-agent.md)

这里记忆是常驻、自托管环境里的一个子系统，而不是整个产品。[Hermes Agent](../agents/hermes-agent.md) 把记忆和 skills、delegation、channels 配在一起；[Mercury Agent](../agents/mercury-agent.md) 把持久记忆和权限硬化的常驻守护进程、审批流配在一起。你得到跨渠道跨时间的持久状态，但你也要自己扛守护进程、运维和策展。

## 怎么选

1. **说清什么必须留存。** 对话状态 → [Letta](../agents/memgpt.md) 或 [jcode](../agents/jcode.md)。项目理解 → [MiMoCode](../agents/mimocode.md) 或 `CLAUDE.md` 惯例。代码架构 → [CodeGraph](../agents/codegraph.md)。个人数据 → [OpenHuman](../agents/openhuman.md)。长驻多渠道状态 → [Hermes](../agents/hermes-agent.md) / [Mercury](../agents/mercury-agent.md)。
2. **定被动还是显式。** 被动召回（[jcode](../agents/jcode.md)、自编辑的 [Letta](../agents/memgpt.md)）省事但更难审计；文件式记忆（[MiMoCode](../agents/mimocode.md)）完全可查看，但只和它的关键词检索一样好。
3. **盯住隐藏成本。** 每套记忆系统都拿 token、LLM 调用或运维负担换连续性。读 profile 的"使用成本"一节，和[成本 & benchmark](cost-and-benchmarks.md) 一起权衡。

一个 provider 中立的外挂层，[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)，在候补名单上追踪，供想给"没记忆的 agent"加记忆的团队。要看能力视角，记忆是[能力矩阵](../capabilities/matrix.md)里的一列。
