# Graft

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](graft.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/graft.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：Graft 是一层代码上下文，它把代码库的结构写成**一组互相链接的 markdown 文件，agent 用读普通文件的方式就能读**——没有 embedding、没有数据库、没有常驻索引进程——并且一条 `init` 就把自己接进 Claude Code、Codex、Cursor、Gemini CLI 等八个以上的 agent。

> **真正的分野在存储形态，不在检索。** [CodeGraph](codegraph.md) 把仓库索引进一个可查询的 SQLite 数据库，通过 MCP 交给 agent；agent 必须**主动调工具**才看得见任何东西。Graft 写的是 `graft/*.md`——每个子系统一个节点，节点之间用 `[[wikilink]]` 相连——agent 用它本来就有的文件工具去打开、grep、跟着链接走。MCP 也提供，但那是第二道门，不是唯一一道。

> **它给出了第三方评分的基准，这在这条路线上很少见。** 多数上下文层只报自家 harness 的数字。Graft 既报了自家的，也报了 **SWE-bench Verified 的 50 个实例**，由官方 `swebench` 4.1.0 评分——真实仓库、维护者自己的测试。请把它当作厂商自己跑的一个 50 实例子集来读，但要读：它记录的失败形态（基线只补一个文件、漏掉同属那几个）是一个具体可核的断言，而不是一个省 token 的百分比。

## 快速判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Trail（`trailhq/Graft`，trailhq.com）——`trailhq` 组织建于 2026-08-24；仓库徽章与 npm scope 仍留着此前 NanoNets 的名字 |
| 路线 | 运行时 & 工具——给别的 agent 用的代码上下文层 |
| 开源 | MIT；npm `@nanonets/graft`，CLI 为 `graft` |
| 实现 | Node 上的 TypeScript；结构层用 tree-sitter |
| 核心思想 | 图谱是你仓库里一堆互相链接的 markdown 文件，不是查询 API 背后的数据库 |
| 模型 | 自带——OpenAI 兼容、Anthropic 原生、OpenRouter、Fireworks、Groq、LiteLLM 代理，或本地模型。结构那一遍完全不调模型 |
| 已接入的 agent | Claude Code（skill 文件 + hooks + statusline + MCP）、Codex、OpenCode 等读 `AGENTS.md` 的 CLI、Cursor、Gemini CLI、Copilot、Kiro、Windsurf、Grok、AdaL |
| 语言 | 23 种——九种全保真（TS/JS、Python、Go、Java、Kotlin、PHP、Swift、R），十四种到「符号 + 调用边」精度；另有可选 LSP 层拿编译器级精度的边 |
| 最适合 | 仓库够大、agent 每次任务的开销主要花在重新认路、又希望产物本身可读的团队 |
| 主要代价 | 0.x 且迭代很快；图谱是每个人各自重建的本地缓存；`init` 可能写入机器级的 Codex 配置 |
| GitHub 仓库 | https://github.com/trailhq/Graft |

## 什么时候选它

- **你的 agent 开销在探索，不在生成。** Graft 点出的问题正是本地图在 [coding CLI 路线](../comparisons/coding-cli-agents.md)上反复看到的那个：每个任务都重新 grep、重新打开、重新顺着 import 走一遍一小时前刚摸清的仓库，然后丢掉。如果你的 token 账单是被读而不是被改撑起来的，这就是对症的那一层。
- **你希望产物对人也可读。** 一个节点就是一个 markdown 文件：一段大白话摘要、真正承载逻辑的那几行、构建它所用的源文件（带内容哈希），以及带类型的链接（`depends_on`、`part_of`、`uses`、`implements`、`produces`）。你能读它、审它，还能在下面写自己的笔记——笔记在重新生成时会保留。
- **你不想再养一个索引。** 每次查询都会拿工作区和上次构建的指纹重新比对（约 3ms），只重建动过的部分，所以回答描述的是此刻的代码，包括还没提交的改动。没有守护进程，也没有要预热的索引。
- **你希望免费的那一档是真免费。** `graft build` 与 `graft check` 是确定性的 tree-sitter——不调模型、不要 key、不联网。写摘要和概念节点的那遍 LLM（`--deep`）是可选的，且跑在你自己的 provider key 下。
- **你同时用不止一个 agent。** 一条 `init` 给每个 agent 写它自己的原生指令文件，而不是一份最小公约数；`--dry-run` 会先把所有将要动的路径打出来再动手。
- **你想看到机制，不只看到省了多少。** 公布的 SWE-bench 那一臂是 33/50，对冷启动 Claude Sonnet 5 基线的 27/50，同时少用 23% 的 token；而且文章逐条讲清每次赢在哪，没有把它们平均掉。

## 什么时候不要选

- **仓库太小。** agent 几次工具调用就能读完的东西，给它一张地图没有收益，你只是多了一个构建步骤。
- **你要的是一个别的工具也能 join 的可查询存储。** 如果提问的不止是 agent，[CodeGraph](codegraph.md) 的 SQLite 是更合适的形态。
- **你需要一份提交进仓库、大家共享的产物。** `graft build` 会特意把 `graft/` 加进 `.gitignore`——你提交的是接线，每个同事各自重新生成自己的图谱（也各自付自己的富化成本）才能拿到同一张图。
- **机器级写入对你是问题。** 选了 Codex 这个宿主，它同时会改 `~/.codex/config.toml`、`~/.codex/hooks.json` 并放一个 hook shim——这些是用户级的，对你用 Codex 打开的**每一个**仓库都生效。选择器里有标注、`--no-global` 可以跳过，但默认并不是只作用于本仓库。
- **你需要稳定的接口。** npm 停在 `0.19.0`，GitHub 上一个 release tag 都没有；而且项目中途换过东家：组织是 `trailhq`，npm scope 还是 `@nanonets`，README 自己的徽章两边都指。
- **你要厂商中立的治理。** 绝大多数提交来自两个账号，README 反复把人引向托管产品（Trail Brain）。MIT 且可 fork，不等于社区治理——本地图对 [TrueForge](trueforge.md) 画的是同一条线。
- **默认开启的遥测是硬阻断。** 默认会发一条批量的匿名使用统计。它有文档、能用 `graft telemetry debug` 查看、在 CI 和源码构建里默认关闭、`DO_NOT_TRACK=1` 也能关——但它是 opt-out，不是 opt-in。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 工具使用 | 强 | 六个 MCP 工具（找代码、文件 API、追调用、全量查找、仓库地图、新鲜度），外加一条完全不需要 MCP 的纯文件路径 |
| 代码执行 | 无 | Graft 不跑你的代码，只解析 |
| 记忆 | 强 | 这就是产品本体——持久的项目理解，靠重新生成而不是靠记住，跨每一次会话存活 |
| 编排 | 无 | 没有循环、没有回合；它是别人循环下面的一层 |
| 多 agent | 中 | 一条命令接八个以上 agent，但各自独立读图谱，没有任何东西在协调它们 |
| 人工审批 | — | 不适用；`--dry-run` 与文件选择器是最接近的东西 |
| 调度 | 无 | 重建由查询和编辑后的 hook 触发，不由时钟触发 |
| 交付面 | 中 | CLI（`grep`、`map`、`ask`、`viz`）、MCP server，以及它写进每个 agent 的指令文件 |
| 部署控制 | 很强 | MIT、默认纯本地、用你自己的 key；唯一一个你没要求的网络调用有文档也能关 |

## 值得了解的架构

其余一切都由**「图谱是文件而不是数据库」**这个决定推出来。节点一旦是工作区里的 markdown，检索就不再是一种特殊能力：agent 用读源码的同一套工具去 grep、去打开、去顺着 `[[wikilink]]` 走。这消掉了所有基于 embedding 的上下文层共有的失败形态——agent 不主动调就看不见索引；同时也意味着产物是人可以审的，而一张 embedding 表永远做不到。

第二个想法是**两档之间划了一条硬线**。第一档是 tree-sitter：每个函数、类、调用边，确定性、不调模型、不要 key、零成本。第二档（`--deep`）才是写大白话摘要、把文件归并成概念节点的那遍 LLM。把两者分开，是新鲜度那套说法能成立的原因——每次查询都敢重新核一遍工作区，正因为这次核对从不调模型。这也让项目在你还没决定用哪家 provider 之前就能用。

第三，节点格式在一个文件里装了**三层深度**：摘要说代码做什么；**crux**——真正的那个 guard、跳过条件或状态变更，按文本而不是按行号区间存，所以上面无关代码挪动时它不会漂——说它怎么做；带内容哈希的源引用指向其余部分。它的主张是把通常的两步（先找到地址、再读文件）压成一步，这也是整个设计里最直接解释基准里工具调用下降的那一环。

## 运行成本

钱上低，习惯上真实。结构图谱免费且即时；富化那遍是每个仓库一次性的 LLM 开销，按内容哈希缓存，重跑只碰改过的文件（项目自己给的 124 文件仓库数字：冷跑 0.74s，改一个文件后 0.18s）。真正要算的成本是组织上的：`graft/` 被 gitignore，所以图谱是每人一份，每个同事各自付自己的富化成本。要预算的是这条约定而不是算力——你得维持住的，是「大家都会跑一次 `graft build`」这件事。

## 结论

对 coding agent 路线一直绕着走的一个问题——**为什么每个任务都要从重新认识仓库开始？**——Graft 给了目前最清楚的答案：把理解写成 agent 本来就会读的文件。这个答案比一个索引更简单，而且难得地是用第三方评分的基准、而不是一个省钱百分比来论证的。要把它和它的年纪放在一起掂量：`0.19.0`、换名换到一半、核心只有两个作者，而且图谱是每人一份的缓存而不是共享产物。想要仓库里可读、且零基础设施，就选它而不是 [CodeGraph](codegraph.md)；想要 MCP 背后一个可查询的存储，就选 CodeGraph。路线层面的视角见[记忆方案对比](../comparisons/memory-approaches.md)与[主流格局表](../comparisons/mainstream-agent-landscape.md)。
