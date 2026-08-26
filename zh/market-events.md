# 市场事件

[English](../market-events.md) | [中文](market-events.md)

重塑 agent 选型格局的结构性事件——模型发布、产品合并、浪潮——新的在前。每周的逐窗口记录在 [agents/README.md](agents/README.md) 的"市场事件"时间线里；本页保存长期有效的档案。

## 2026-08-21 —— OpenAI 把 Sol 降价 20% 以上，价格挪动了整张榜

OpenAI 于 **2026 年 8 月 21 日把 GPT-5.6 Sol 从每百万输入/输出 token 的 $5 / $30 降到 $4 / $20**，输入降 20%，**输出降 33%**。这是促销价，为期三个月——至少持续到 2026 年 11 月 21 日——且适用范围不止裸 API：按量付费 API、**Codex credits**、符合条件的 ChatGPT Work 计划都算。这是 GPT-5.6 家族一个月内的第二次降价。同一天，OpenAI 宣布 **Codex 活跃用户 2000 万**。

**对选型的影响：** 这是热度榜第一次由降价而不是发布来解释榜首移动。[Codex CLI](agents/codex.md) 从 #9 到 #2，**周 star 率跳增 4.5 倍**，是本地图记录过最大的一次重新加速，而窗口内并没有可与之匹配的产品事件——这段时间的 release 都是常规增量（Bedrock Runtime 支持、带 MCP 工具的异步 hooks、会话 fork 与恢复、TUI 对话导出）。对选型有两点推论。第一，降得更狠的是输出侧，而这对 agent 负载的意义被低估了：agent 循环的 token 花在生成的 diff、工具调用和推理上，不是花在 prompt 文本上，所以 33% 的输出降价，实际折扣比"20% 以上"这个标题给人的印象大。第二，也更不舒服的一点：**"促销"这两个字是承重的**。三个月的价格不是预算基线；任何按 $4 / $20 做的测算都需要在 11 月复核一次，而按档位算成本的那张表——见[成本与基准](comparisons/cost-and-benchmarks.md)——从此是一份要维护的运营文档，不是一张参考表。本地图一直在跟的那条大趋势没有变：厂商在**访问方式和价格**上竞争，不在循环上。

来源：[OpenAI 下调 GPT-5.6 Sol 价格](https://enterprisedna.co/resources/news/openai-gpt-56-sol-price-cut-20-percent-frontier-model-august-2026/)、[GPT-5.6](https://openai.com/index/gpt-5-6/)、[降价后的 GPT-5.6 定价](https://cellcog.ai/blog/gpt-5-6-pricing/)、[openai/codex releases](https://github.com/openai/codex/releases)。

## 2026-08-05 → 08-10 —— Meta 补上厂商 CLI 的最后一块；Claude Code 支持自托管

一周之内落地了三件事，而它们共同推动的是厂商层，不是开源层。

**Meta 在 8 月 5 日发布了 [Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)（beta）**，一个终端 coding agent，底下是新的 coding 向模型 **Muse Spark 1.2**。它一条命令安装，每个任务可以调度多个常驻子 agent，而真正有辨识度的一点是：每一次模型调用、工具运行、审批和编辑都会追加写入本地事件日志，使运行时**可精确重放、可从崩溃处重启**，因而能扛长任务。内置技能是 `/plan`（把任务变成需要审批的计划）、`/grill`（对该计划做压力测试）和 `/goal`。Muse Spark 1.2 通过 Muse Code、Meta Model API 和 OpenRouter 提供。

**Anthropic 在 8 月 6 日把 [Claude Code 自托管环境](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)推入公开 beta** —— 会话跑在客户自己的基础设施上，在客户自己的网络里、紧挨内部服务，而不是 Anthropic 托管的算力。仅限 Team 和 Enterprise，默认关闭，使用 ZDR 的组织不可用。

**OpenAI 在 8 月 10 日发布 [GPT-5.6-Cyber](https://developers.openai.com/api/docs/models/gpt-5.6-cyber)**，基于 GPT-5.6 Sol 的安全专用模型，需通过 Daybreak 计划审批才能使用。

**对选型的影响：** 本地图 7 月写过"每一家主要模型厂商现在都有自己的一方 coding CLI"，并把这个阵营列为 Anthropic、OpenAI、Moonshot、小米、xAI。Meta 是当时显眼的缺席者，现在不是了——但要注意它是*怎么*来的。Muse Code 是通过 Meta Model API 分发的 beta，**没有公开仓库**，所以它连 Grok Build 那种 source-available 的一端都没够到；本地图的榜单也因此不跟踪它。厂商阵营在不到一个月里合拢，而且合拢时用的多半是你读不到源码的 agent——这才是真正的故事。同时，Claude Code 和 GPT-5.6-Cyber 从另一个角度指向同一件事：厂商现在竞争的差异点是**部署方式与访问控制**——这个 loop 跑在谁的基础设施上、谁被允许跑它——而不是 loop 本身。Muse Code 那个可精确重放的事件日志，是这批发布里唯一一个真正的能力想法，而它对付的正是[观测层](comparisons/observability-and-evals.md)从外部切入的同一个持久性问题。Muse Spark 1.2 的价格与指数位次尚未在本地图记录，因此不会出现在[成本与基准](comparisons/cost-and-benchmarks.md)页。

来源：[Introducing Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)、[developer.meta.com/ai/models/muse-spark](https://developer.meta.com/ai/models/muse-spark/)、[Self-hosted environments for Claude Code](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)、[Claude Code 自托管文档](https://code.claude.com/docs/en/self-hosted-environments)、[GPT-5.6-Cyber](https://developers.openai.com/api/docs/models/gpt-5.6-cyber)。

## 2026-07 → 08 —— "元 harness"出现了

两个项目在相隔几周之内从两端做出了同一件事。**[QM](agents/qm.md)**（`yc-software/qm`，MIT）——Y Combinator 面向 Slack 和 web 的*多人协作* agent——**头七天拿到约 11.4k star、1.3k fork**；**[Omnigent](agents/omnigent.md)**（`omnigent-ai/omnigent`，Apache-2.0）越过 8k。两者都不自带 agent 循环。它们都是把*别人的* harness——Pi、OpenCode、Codex、Claude Code、Cursor、Hermes——收到一个接口背后的层，并补上裸循环缺的东西：身份、审批策略、花费上限、沙箱、调度和会话连续性。

**对选型的影响：** 过去两年，harness 的问题一直是"我 fork 哪一个"。这两个项目假定答案是"好几个，而且这没问题"——这等于押注循环本身正在商品化，持久价值在它上面那层治理里。如果这个押注成立，"选哪个 harness"就变成一个可逆决策，真正重要的选择上移了一层。注意两者在"记账单位"上分得很干净：QM 的单位是**组织**（按人和按房间各一个作用域、一档由管理员设定的安全姿态、自托管在你自己的云里），Omnigent 的单位是**开发者**（一个会话跟着你在终端、浏览器、手机和桌面之间走，可跑在九家云沙箱供应商上）。也要注意成熟度：QM 才几天大，Omnigent 自标 alpha，所以这是一个值得跟踪的形态，还不是一个值得依赖的层。QM 还带着本地图为 Grok Build 标注过的那类治理提醒，只是换了一种形式——许可证是 MIT，但贡献只接受*文字提案*，不收代码。详见 [QM](agents/qm.md)、[Omnigent](agents/omnigent.md)、[agent harness 框架](comparisons/agent-harness-frameworks.md)。

来源：[yc-software/qm](https://github.com/yc-software/qm)、[qm.ycombinator.com](https://qm.ycombinator.com)、[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)、[omnigent.ai](https://omnigent.ai)。

## 2026-07-14 —— xAI 发布 Grok Build，"开源"就此分成两种

SpaceXAI（xAI）发布了 **[Grok Build](agents/grok-build.md)**（`grok`），一个 Claude Code 形态的 Rust 终端 coding agent——全屏 TUI、CI 用的 headless 模式、以及让编辑器驱动它的 Agent Client Protocol server，外加 MCP server、skills、插件、hooks 和沙箱。它**在 15 天内拿到 23.2k star、4.4k fork**，是本地图记录过的最快首秀。至此每家主要模型厂商都有了自己的第一方 coding CLI。

**对选型的影响：** 厂商 CLI 这一格基本填满了（Anthropic、OpenAI、月之暗面、小米、xAI），所以"选哪个 coding CLI"越来越取决于"你在为哪个模型付费"。更耐久的一课是本地图现在必须讲明的治理分叉：Grok Build 是 **Apache-2.0，但不接受贡献**——它是私有 monorepo 的周期性导出，树内还带有 `openai/codex` 和 `sst/opencode` 工具代码的移植。"源码可见"和"社区共建"已经明显分道扬镳，而 LICENSE 文件不再能告诉你拿到的是哪一种。详见 [Grok Build](agents/grok-build.md)、[终端编码 CLI 对比](comparisons/coding-cli-agents.md)。

来源：[xai-org/grok-build](https://github.com/xai-org/grok-build)、[x.ai/cli](https://x.ai/cli)、[docs.x.ai/build/overview](https://docs.x.ai/build/overview)。

## 2026-07-09 —— Codex 并入 ChatGPT；GPT-5.6 发布

OpenAI 把独立的 Codex 应用并入 ChatGPT 桌面应用（macOS/Windows）：Codex 成为与 Chat 和新的 agentic 模式 **ChatGPT Work** 并列的专属编码入口，所有计划（含免费版）可用。同日，**GPT-5.6** 在 ChatGPT、Codex 和 API 全面接棒 GPT-5.5，分三档——Sol（$5/$30 每百万 token）、Terra（$2.5/$15）、Luna（$1/$6），另有 Ultra 多 agent 模式。Codex 周活超 500 万，其中 100 万以上用于软件开发以外的工作。

**对选型的影响：** OpenAI 侧"选哪个 coding agent"的问题坍缩成"你怎么用 ChatGPT"——移动的是产品边界，不只是能力。GPT-5.6 Sol 以 GPT-5.5 的老价格领跑 Artificial Analysis 编码 agent 指数（80，vs Fable 5 77.2、GPT-5.5 76.4、Opus 4.8 72.5），GPT-5.5 就此成为过渡选择。详见 [Codex](agents/codex.md)、[GPT-5.5](agents/gpt-5.5.md)。

来源：[OpenAI Codex changelog](https://learn.chatgpt.com/docs/changelog)、[GPT-5.6 公告](https://openai.com/index/gpt-5-6/)、[Axios](https://www.axios.com/2026/07/09/ai-openai-gpt-release)。

## 2026-06-17 —— Vercel 发布 eve，"自建"路线长出了交付面

Vercel 在伦敦的 Vercel Ship 上发布 **[eve](agents/eve.md)**（`vercel/eve`，Apache-2.0），归在它称为 **Agent Stack** 的一组产品里。它的说法是"agent 的 Next.js"：一个 agent 就是**一个目录**——`instructions.md`、`tools/`、`skills/`、`subagents/`、`channels/`、`schedules/`、`connections/`——而框架负责持久化执行（建立在开源 Workflow SDK 上的检查点会话，能扛住崩溃**和**重新部署）、每个 agent 一个沙箱、能让运行无限期暂停且不耗算力的 `needsApproval` 闸门、带独立上下文窗口的 subagent、`defineEval` 测试集，以及 Slack、Discord、Teams、GitHub、Linear、Telegram、Twilio、HTTP 的渠道适配器。头十周拿到 **4.8k star**。**本地图当时漏了它，现在作为补漏记录在此**，同时补上 profile。

**对选型的影响：** eve 改变的是"自建"这条路线的形态，而不只是把它变长。这条路线上其他框架（[LangChain](agents/langchain.md)、[LangGraph](agents/langgraph.md)、[CrewAI](agents/crewai.md)、[LlamaIndex](agents/llamaindex.md)）在[能力矩阵](capabilities/matrix.md)里的"交付面"一列全是 **—**，因为它们是库，agent 最后**出现在哪里**是你自己的事。eve 是这条路线上第一个把渠道、调度、审批都做成框架原语的条目——这让它在"建"这一侧，最接近[元 harness](agents/qm.md) 在"运维"那一侧做的事。代价在最后一列：它是这条路线上唯一一个生产路径写死在某一家平台上的框架（`vercel deploy`，沙箱与模型访问经 AI Gateway），自托管没有写进文档。Apache-2.0 让代码可以搬走，但不让部署可以搬走。这是一个干净且摆在明面上的取舍——用平台换电池——而它就是全部的决策点。

来源：[Introducing eve](https://vercel.com/blog/introducing-eve)、[vercel/eve](https://github.com/vercel/eve)、[eve.dev](https://eve.dev/)、[Vercel debuts eve](https://www.theregister.com/devops/2026/06/19/vercel-debuts-eve-open-source-agent-framework-tries-to-fix-shadow-ai-with-passport/5258726)。

## 2026-06-09 —— Claude 5 家族：Fable 5 与 Mythos 级

Anthropic 发布 **Claude Fable 5** 和 **Claude Mythos 5**——同一底层模型，Fable 5 面向所有人（附加安全措施），Mythos 5 仅限获批组织。Mythos 是位于 Opus 之上的新等级。Fable 5 成为 Claude Code 中 Pro/Max 的默认模型，6 月 12 日因短暂的美国出口管制全球下架，7 月 1 日在更严格的安全分类器后面恢复（被拦截的请求回退 Opus 4.8），7 月 7 日起改为按量计费的 usage credits。两周前（5 月 28 日），**Opus 4.8** 已修复 Opus 4.7 的 tool-calling 问题并推出 Dynamic workflows。

**对选型的影响：** Anthropic 侧的模型层变成两档预算决策——最难的活花 Fable 5 额度，Opus 4.8 作为可靠默认档。详见 [Claude Fable 5](agents/claude-fable-5.md)、[Claude Code](agents/claude-code.md)。

来源：[Anthropic 公告](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)、[Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)。

## 2026-05（持续中）—— `.claude/skills` 浪潮

5 月中旬冲上 GitHub trending 的浪潮持续复利：curated skill 合集与 skills 框架此后一直占据每周热度前 10 的约一半。Star 数截至 2026-08-12：

| 仓库 | Stars | 形态 |
| --- | --- | --- |
| [Superpowers](agents/superpowers.md) | 270.9k | 完整的 skills 框架 + 方法论，接入 Claude Code、Codex、Cursor、Copilot 等 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 214.3k | Matt Pocock 的个人 `.claude/skills` 精选目录 |
| [anthropics/skills](https://github.com/anthropics/skills) | 168.4k | Anthropic 官方 Agent Skills 参考仓库——模式的上游源头 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 86.4k | Addy Osmani 面向 coding agent 的生产级工程技能集 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 42.1k | 面向 Claude Code 的学术研究管线 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 33.3k | 覆盖科研/科学/工程/分析/金融/写作的即用型技能 |

进入 8 月，这个浪潮不再在*广度*上扩张，而是开始原地轮换：它已连续两个窗口稳定占据每周前 10 的四席，但成员一直在换，而且涨势越来越集中在两个体量最大的 curated 目录上。在 2026-08-05 → 08-12 窗口里，`mattpocock/skills` 和 `addyosmani/agent-skills` 第一次同时拿下增量榜前两席，后者是在整整缺席一个窗口之后以 4.9 倍跳增回来的（+945 → +4,664）。

**对选型的影响：** `.claude/skills` 模式已经从新鲜事物变成共享基础设施——工程师像当年发布 dotfiles 一样发布自己的技能库，很多任务里技能层和底层 agent 同样重要。但这种集中值得留意：如果一个浪潮的增量越来越归拢到两个个人目录上，那它带的是关键人风险，而不是一个正在扩张的生态。本地图通过 [Superpowers](agents/superpowers.md) 覆盖框架端，curated 合集作为候补跟踪（内容资产而非 agent 表面）；浪潮有自己的榜单，见 [rankings/skill-verticals.md](rankings/skill-verticals.md)。

## 2026-04 —— GPT-5.5 与 "Codex for (almost) everything"

相隔一周的两次 OpenAI 发布定下了春季格局。**4 月 16 日**：并入 ChatGPT 之前 Codex 最大的一次产品更新——任意 macOS app 的后台 Computer Use、同机并行多 agent 执行、带主动建议的内置浏览器、90+ plugin、周活 300 万开发者（3 月初的 2 倍）。**4 月 23 日**：**GPT-5.5** 作为 OpenAI 前沿 agentic 模型发布——Terminal-Bench 2.0 得分 82.7%（发布时最高）、1M token 上下文窗口、价格是 GPT-5.4 的 2 倍。

**对选型的影响：** 两者一起抬高了所有 OpenAI 系表面的能力上限，把模型层带进了 agent 选型。两者如今都已被接棒（见 7 月 9 日条目），但仍是"2026 竞赛跑得有多快"的参照点。详见 [GPT-5.5](agents/gpt-5.5.md)、[Codex](agents/codex.md)。

## 2026-01 —— ClickHouse 收购 Langfuse

ClickHouse 收购了 **[Langfuse](agents/langfuse.md)**——star 数最高的开源 LLM/agent 观测平台（截至 2026-07-29 为 32.0k）。Langfuse 以开放内核模式提供追踪、评估、prompt 管理和数据集——核心 MIT，治理类功能在单独的 Enterprise 许可之下——并且自托管仍然免费且不限量。

**对选型的影响：** agent 观测正在被吸收进通用数据基础设施，而不是继续作为独立品类存在；如果你押注某个厂商保持独立，这一点很重要。它同时凸显了本地图现在明确记录的一个区别：在这一层，"开源"横跨四种不同的东西——宽松许可（Opik、Traceloop、Helicone，Apache-2.0）、开放内核（Langfuse）、源码可见但未获 OSI 认可（Arize Phoenix，Elastic 2.0）、以及完全闭源（LangSmith、Braintrust）。Langfuse 表示自己仍然 100% 开源、路线图不变；那是厂商承诺，不是可核实的保证。详见 [Langfuse](agents/langfuse.md)、[观测与评估](comparisons/observability-and-evals.md)。

来源：[Joining ClickHouse](https://langfuse.com/blog/joining-clickhouse)、[ClickHouse 公告](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability)、[langfuse/langfuse](https://github.com/langfuse/langfuse)。
