# Agent 记忆方案对比

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](memory-approaches.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/memory-approaches.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

记忆是把"无状态工具"和"真正懂你项目或你生活的 agent"分开的那根轴。整个 2026 年，它成了本图上最响的差异点之一——[MiMoCode](../agents/mimocode.md) 和 [jcode](../agents/jcode.md) 都拿它打头，[Letta](../agents/memgpt.md) 整个围着它建，自托管运行时也把它当招牌强项。

但"有记忆"这句话，藏起来的比它说出来的多。这些项目说的"记忆"根本不是一回事。本页按它们*怎么*记来分类，好让你把机制对上你真正需要持久化的东西。

## 七种方案一览

| 方案 | 怎么记 | 代表 | 你需要持久化什么时选它 |
| --- | --- | --- | --- |
| 自编辑托管记忆 | agent 在上下文窗口内编辑自己的 core / archival / recall 存储 | [Letta (MemGPT)](../agents/memgpt.md) | 由 agent 自己策展的长期对话状态 |
| 被动语义召回 | 自动采集活动（jcode 每轮嵌入成向量；claude-mem 由 hooks 采集、模型压缩成观察记录），相关历史自动注入 | [jcode](../agents/jcode.md), [claude-mem](../agents/claude-mem.md) | 不用手动调记忆工具的跨会话连续性 |
| 文件 / 关键词项目记忆 | 人类可读文件（`MEMORY.md`、checkpoint），关键词检索取回 | [MiMoCode](../agents/mimocode.md)、Claude Code（`CLAUDE.md`） | 跨运行留存、且可查看的项目理解 |
| 预索引代码知识图谱 | 代码库解析成可查询的图/库，按需查询 | [CodeGraph](../agents/codegraph.md), [Graphify](../agents/graphify.md) | 架构级代码上下文，不是对话 |
| 写成文件的代码图谱 | 代码库解析成互相链接的 markdown，agent 用普通文件工具就能读 | [Graft](../agents/graft.md) | 同一种代码上下文，但产物是人能读、能审的 |
| 个人数据记忆树 | 连接器把你的工具同步进分层摘要存储 | [OpenHuman](../agents/openhuman.md) | agent 关于*你*知道什么——邮件、笔记、日历 |
| 长驻运行时记忆 | 记忆是常驻自托管环境里的一个子系统 | [Hermes Agent](../agents/hermes-agent.md)、[Mercury Agent](../agents/mercury-agent.md) | 跨渠道、跨设备、跨时间的持久状态 |

## 自编辑托管记忆 —— [Letta (MemGPT)](../agents/memgpt.md)

把研究范式（MemGPT）落地：agent 维护 **core memory**、**archival memory**、**recall memory**，用显式工具编辑它们，好在固定上下文窗口里保持有用。这是最有章法、最可移植的设计——它是你拿来建有状态 agent 的框架，不是成品 CLI。代价很实：额外的 LLM 调用和基础设施。如果你 agent 的全部职责就是记住并随时间自我改进，这是认真的开源底座。

## 被动语义召回 —— [jcode](../agents/jcode.md)

jcode 把每一轮嵌入成语义向量，用余弦相似度查一张**记忆图谱**，自动把相关历史注入对话——可选一个校验 side-agent 在注入前检查相关性。重点是召回*不靠模型调记忆工具*，所以它既不遗忘、也不为盯记忆烧 token。你想用时，显式记忆工具和会话检索（对历史会话的传统 RAG）也都在。取舍：如果你想调"召回什么"，它就是多一个要理解的子系统。

**外挂而非内置——[claude-mem](../agents/claude-mem.md)。** 同样是被动召回，只是加装在你已经在用的 agent 上。生命周期 hooks 记录 agent 的动作，由 observer 模型压缩成带类型的观察记录，存进 SQLite（FTS5）和 Chroma，下一次会话开始时注入相关部分；agent 想查更多时，走三步 MCP（`search` → `timeline` → `get_observations`），先拿索引，需要时才取完整内容。取舍在于 observer 跑在哪：用你自己的 key 或套餐，或者用默认安装器首先推荐的付费托管 CMEM Pro。

## 文件 / 关键词项目记忆 —— [MiMoCode](../agents/mimocode.md)、Claude Code

务实、透明的那一端。[MiMoCode](../agents/mimocode.md) 维护项目 `MEMORY.md`、自动会话 checkpoint、scratch 笔记、逐任务进度，恢复时通过 **SQLite FTS5** 关键词检索注回。[Claude Code](../agents/claude-code.md) 的 `CLAUDE.md` 惯例是同一想法的最轻版本。强项是记忆就是一个你能读、能改、能提交的纯文件——没有黑箱。局限是关键词检索：它召回匹配的，不是语义相关的。

## 预索引代码知识图谱 —— [CodeGraph](../agents/codegraph.md)

另一种记忆：不是对话，是**代码库**。CodeGraph 把仓库（Tree-sitter + SQLite + FTS5）解析成本地可查询的知识图谱，通过 MCP 提供，让 Claude Code、Cursor、Codex 这类 agent 用少得多的工具调用和 token 回答架构问题。它是你挂到别的 agent 上的上下文基础设施，在从头扫描代价很高的中大型仓库上回本。

## 写成文件的代码图谱 —— [Graft](../agents/graft.md)

目标和 CodeGraph 一样，存储决定恰好相反。[Graft](../agents/graft.md) 把代码库写成 `graft/*.md`——每个子系统一个节点，各自带一段大白话摘要、真正承载逻辑的那几行、带内容哈希的源引用，以及带类型的 `[[wikilink]]`——agent 用它本来就有的文件工具去读。MCP 也提供，但不是唯一一道门，这就消掉了所有“只能查询”型上下文层共有的失败形态：agent 不主动调就看不见索引。结构那一遍是确定性的 tree-sitter（不调模型、不要 key），所以每次查询都能负担得起先重新核一遍工作区再回答。代价是 `graft/` 被有意 gitignore——每个同事重新生成自己那份，所以这是带共享约定的“每人一份”记忆，不是共享产物。

**第三种存储决定——[Graphify](../agents/graphify.md)。** 它写出一份 `graph.json`（另加一份报告和一个 HTML 视图），agent 通过 skill、CLI 或本地 MCP server 去查；每条边都带置信标签（`EXTRACTED`、`INFERRED` 或 `AMBIGUOUS`）。它和 CodeGraph、Graft 有两点不同：可选的语义那一遍把文档、PDF、图片和转写后的媒体映射进同一张图；它的团队指南写明可以用 pre-commit hook 加 union 合并驱动把 `graph.json` 提交进仓库，让这张图成为共享产物，而不是每人一份的缓存。

**选 CodeGraph 还是 Graft？** 如果提问的不只是 agent、或者你要的就是一份共享数据库，选 CodeGraph。如果你希望这份记忆可审、希望免费那一档连 API key 都不需要，且接受每个开发者各自重建，选 Graft。

## 个人数据记忆树 —— [OpenHuman](../agents/openhuman.md)

指向你生活、而不是你代码的记忆。[OpenHuman](../agents/openhuman.md) 自动把 Gmail、Notion、GitHub、Slack 和 118+ 工具同步进本地**记忆树**——SQLite 里的分层摘要，镜像到一个可浏览可编辑的 Obsidian 兼容 wiki。价值是助手对*你*从不冷启动；代价是它要几周的自动抓取循环才攒得起来，而且你要接受 GPL-3.0 以及把所有东西本地同步带来的数据驻留问题。

## 长驻运行时记忆 —— [Hermes Agent](../agents/hermes-agent.md)、[Mercury Agent](../agents/mercury-agent.md)

这里记忆是常驻、自托管环境里的一个子系统，而不是整个产品。[Hermes Agent](../agents/hermes-agent.md) 把记忆和 skills、delegation、channels 配在一起；[Mercury Agent](../agents/mercury-agent.md) 把持久记忆和权限硬化的常驻守护进程、审批流配在一起。你得到跨渠道跨时间的持久状态，但你也要自己扛守护进程、运维和策展。

## 怎么选

1. **说清什么必须留存。** 对话状态 → [Letta](../agents/memgpt.md) 或 [jcode](../agents/jcode.md)。项目理解 → [MiMoCode](../agents/mimocode.md) 或 `CLAUDE.md` 惯例。代码架构 → [CodeGraph](../agents/codegraph.md) 或 [Graft](../agents/graft.md)。个人数据 → [OpenHuman](../agents/openhuman.md)。长驻多渠道状态 → [Hermes](../agents/hermes-agent.md) / [Mercury](../agents/mercury-agent.md)。
2. **定被动还是显式。** 被动召回（[jcode](../agents/jcode.md)、自编辑的 [Letta](../agents/memgpt.md)）省事但更难审计；文件式记忆（[MiMoCode](../agents/mimocode.md)）完全可查看，但只和它的关键词检索一样好。
3. **盯住隐藏成本。** 每套记忆系统都拿 token、LLM 调用或运维负担换连续性。读 profile 的"使用成本"一节，和[成本 & benchmark](cost-and-benchmarks.md) 一起权衡。

想给"没记忆的 agent"加记忆的团队，可以看已收录的外挂层 [claude-mem](../agents/claude-mem.md)；provider 中立的 [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) 仍在候补名单上追踪。要看能力视角，记忆是[能力矩阵](../capabilities/matrix.md)里的一列。
