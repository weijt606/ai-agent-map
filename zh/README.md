# AI Agent Map

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](README.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../README.md)
[![License](https://img.shields.io/badge/LICENSE-MIT-16a34a?style=for-the-badge&labelColor=166534)](../LICENSE)
[![Agent](https://img.shields.io/badge/AGENT-MAP-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md)

<p align="center">
	<img src="../assets/ai-agent-map-pixel-zh.png" alt="像素风格的 AI Agent Map 主视觉，展示四大区域——日常编程 Agent、通用自主任务 Agent、框架与平台、运行时与工具——agent 图标分布在宝藏地图风格的插画场景中" width="100%" />
</p>

AI Agent Map 是一个更偏实用、偏可视化的仓库，用来横向比较主流 AI agent、agent 平台、runtime 和 orchestration 工具。

目标很简单：帮读者更快得到一个靠谱的 shortlist。

## 这个仓库想解决什么

- agent 世界很热闹，但真正帮助选型的内容不多。
- 很多资料会讲理念，却不讲适合什么、不适合什么、代价是什么。
- 大多数人需要的是比较层，不是链接堆。

这个仓库只关注选型：它擅长什么、边界在哪、使用成本是什么。

## 从哪里开始

| 你现在的问题更像什么 | 先看哪里 |
| --- | --- |
| 我要先得到一个候选 shortlist | [![进入 Agents](https://img.shields.io/badge/%E8%BF%9B%E5%85%A5-Agents-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md) |
| 我的问题是"代码自动化怎么选" | [![阅读 代码自动化](https://img.shields.io/badge/%E9%98%85%E8%AF%BB-%E4%BB%A3%E7%A0%81%E8%87%AA%E5%8A%A8%E5%8C%96-2563eb?style=for-the-badge&labelColor=1d4ed8)](use-cases/coding-automation.md) |
| 我已经有候选，想做横向对比 | [![查看 主流矩阵](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E4%B8%BB%E6%B5%81%E7%9F%A9%E9%98%B5-dc2626?style=for-the-badge&labelColor=991b1b)](comparisons/mainstream-agent-landscape.md) |
| 我在意审批、记忆、调度、部署这类能力维度 | [![浏览 能力维度](https://img.shields.io/badge/%E6%B5%8F%E8%A7%88-%E8%83%BD%E5%8A%9B%E7%BB%B4%E5%BA%A6-16a34a?style=for-the-badge&labelColor=166534)](capabilities/README.md) |
| 我想看每个项目在这些维度上并排打分 | [![查看 能力矩阵](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E8%83%BD%E5%8A%9B%E7%9F%A9%E9%98%B5-059669?style=for-the-badge&labelColor=047857)](capabilities/matrix.md) |
| 我想知道跑起来到底多少钱、哪一档模型值得 | [![查看 成本与基准](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E6%88%90%E6%9C%AC%E4%B8%8E%E5%9F%BA%E5%87%86-0891b2?style=for-the-badge&labelColor=0e7490)](comparisons/cost-and-benchmarks.md) [![查看 记忆方案](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E8%AE%B0%E5%BF%86%E6%96%B9%E6%A1%88-0d9488?style=for-the-badge&labelColor=0f766e)](comparisons/memory-approaches.md) |
| agent 已经在跑了——我需要知道它是不是还正常 | [![查看 观测与评估](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E8%A7%82%E6%B5%8B%E4%B8%8E%E8%AF%84%E4%BC%B0-4f46e5?style=for-the-badge&labelColor=3730a3)](comparisons/observability-and-evals.md) |
| 我想看存量排行和每周趋势图 | [![查看 排行](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E6%8E%92%E8%A1%8C-7c3aed?style=for-the-badge&labelColor=5b21b6)](rankings/README.md) |
| 我想看问题导向的指南或全部对比页 | [![浏览 用例](https://img.shields.io/badge/%E6%B5%8F%E8%A7%88-%E7%94%A8%E4%BE%8B-ea580c?style=for-the-badge&labelColor=9a3412)](use-cases/README.md) [![浏览 对比](https://img.shields.io/badge/%E6%B5%8F%E8%A7%88-%E5%AF%B9%E6%AF%94-475569?style=for-the-badge&labelColor=334155)](comparisons/README.md) |

## 近期热门榜

热度不等于适合度。

这张表记录的是最近一周 GitHub 快照里特别热的 agent 项目。排名按 7 天增量。下面的总 star 数是这次更新仓库时重新核对过的当前值。

> **最后更新：** 2026-09-09 · **快照窗口：** 2026-09-06 → 2026-09-09（自上次更新以来的增量，**3 天**——周日那次是计划外补刷，周三的例行节奏从这里恢复，所以窗口偏短、噪声偏大；原始增量约为正常窗口的 0.43 倍，下面所有判断一律按**周率**讲） · **star 数：** 更新时点抓取

项目名链接指向上游 GitHub 仓库。本仓库已写入的 profile，在"在本仓库中的状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 在本仓库中的状态 | 应该怎么读 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（=） | [mattpocock/skills](https://github.com/mattpocock/skills) | 257.6k | +3,237 | 候补（Skills 浪潮） | **靠 11 个 star 守住 #1**，而它自己的周率降了 48%（约 14,600/周 到约 7,550）。越过 **25.7 万**，但这是本榜记录到的最窄领先 |
| #2&#8288;（新） | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 217.2k | +3,226 | 已收录 · [profile](agents/deepseek-harness.md) | **第一个可测增量就落在 #2**，约 7,530/周，与第一名差不到 1%。上窗口才纳入跟踪，这是它第一次能进榜 |
| #3&#8288;（=） | [Superpowers](https://github.com/obra/superpowers) | 283.8k | +1,414 | 已收录 · [profile](agents/superpowers.md) | 周率涨 19%，是本窗口唯一加速的 skills 条目。连坐两个窗口的 #3 |
| #4&#8288;（↓） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 243.7k | +1,232 | 已收录 · [profile](agents/hermes-agent.md) | 破 24 万之后的第一个窗口降 32%、退两位。仍是 20 个记录窗口里每期都在的那个 |
| #5&#8288;（新） | [Browser Use](https://github.com/browser-use/browser-use) | 113.9k | +1,228 | 已收录 · [profile](agents/browser-use.md) | **第一个可测增量**，直接到 #5，约 2,870/周。浏览器 agent 路线上目前唯一的条目，三天前才写进 profile |
| #6&#8288;（↓） | [Pi](https://github.com/earendil-works/pi) | 103.4k | +1,028 | 已收录 · [profile](agents/pi.md) | 再降 10%，越过 **10.3 万**。破 10 万之后连续两个窗口温和下滑 |
| #7&#8288;（新） | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 103.6k | +924 | 不收录（金融研究垂直） | 周率涨 **189%**，掉榜一期后回来，越过 **10.3 万**。单个短窗口，本榜不把它读成趋势 |
| #8&#8288;（新） | [OpenCode](https://github.com/anomalyco/opencode) | 206.1k | +916 | 已收录 · [profile](agents/opencode.md) | **第一个可测增量**约 2,140/周，越过 **20.6 万**。上窗口三个新纳入里第三个立刻拿到前十席位的 |
| #9&#8288;（↑） | [Ruflo](https://github.com/ruvnet/ruflo) | 71.8k | +824 | 已收录 · [profile](agents/ruflo.md) | 上榜后的第二个窗口周率涨 **71%**，是确认而不是反转 |
| #10&#8288;（↓） | [Codex CLI](https://github.com/openai/codex) | 122.8k | +814 | 已收录 · [profile](agents/codex.md) | 周率涨 7% 却退两位，因为上面挤进来三个新仓库 |

- 热度适合拿来发现新项目，不适合直接当选型顺序。
- **本窗口是 3 天。** 周日那次是计划外补刷，周三的例行节奏从这里恢复，所以跨度短，原始增量约为正常一周的 0.43 倍。下面每一条判断都按**周率**讲（增量 ÷ 3 × 7），对上一期的周率（增量 ÷ 5 × 7）。三天是本榜发布过的最短窗口，看方向就好，别抠小数。
- **上窗口才纳入跟踪的三个仓库，第一个可测增量就拿走了前十里的三席。** [DeepSeek Harness](agents/deepseek-harness.md) 到 #2、[Browser Use](agents/browser-use.md) 到 #5、[OpenCode](agents/opencode.md) 到 #8。它们此前根本没法进榜，因为上一个窗口开始时还没被跟踪。这与其说是三个同时爆发，不如说是那次扫描失职终于落到了榜面上：三个都体量巨大、活跃了好几周，而本榜一直没有它们的行。
- **#1 是靠 11 个 star 定下来的。** [mattpocock/skills](https://github.com/mattpocock/skills) 拿 +3,237，DeepSeek Harness +3,226。而且第一名自己的周率比上期的历史高点降了 48%，它守住席位靠的是减速比别人慢一点，不是拉开距离。
- **skills 浪潮掉到 2/10，是这波浪潮开始以来的最低。** 上一期还是追平纪录的 6/10。掉下来有两个原因，两个都成立：三个非 skills 仓库挤到了它们上面，而这些集合本身也确实在降温——[anthropics/skills](https://github.com/anthropics/skills) 周率 −52%、[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) −37%、[K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills) −27%、[addyosmani](https://github.com/addyosmani/agent-skills) −12%。唯一的例外是 [Superpowers](agents/superpowers.md)，涨 19%。2026-05-23 以来，这波浪潮的地板一直是 3/10，只在 2026-07-29 出现过一次。
- **[Ruflo](agents/ruflo.md) 是唯一一个确认而不是反转的。** 它上期首次上榜，本可能只是一次尖峰；结果第二个窗口周率涨了 71%。按本榜自己的规矩，这是五个窗口以来第一个扛过下一期的爆发。
- **两处加速，本榜明确暂不称之为趋势**：[TradingAgents](https://github.com/TauricResearch/TradingAgents) 涨 189% 回到榜上，[OpenHands](agents/openhands.md) 涨 129% 排在 #12。单个短窗口在第二个窗口确认前只是尖峰，而最近五个里有四个没通过这项检验。
- 本窗口的里程碑：[OpenCode](agents/opencode.md) 越过 **20.6 万**，[DeepSeek Harness](agents/deepseek-harness.md) **21.7 万**，[Pi](agents/pi.md) 与 [TradingAgents](https://github.com/TauricResearch/TradingAgents) 双双越过 **10.3 万**，mattpocock/skills 越过 **25.7 万**。
- [OpenClaw](agents/openclaw.md) 仍是绝对总数第一，389.3k star（+241）；它已有 profile，但因为这种体量的项目周环比增量噪声太大，不进按增量排名的表。

<details>
<summary>更多窗口笔记：skills 浪潮占比、OpenClaw、以及榜外仍在涨的项目</summary>

- `.claude/skills` 浪潮**占到前十的 5 个**，这是 2026-07-14 以来第一个五席窗口——而新进来的那个是 [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)，一个科研集合，紧随其后的 #11 是 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)。上窗口标出的集中化仍然成立——[mattpocock/skills](https://github.com/mattpocock/skills) 的增量仍超过其他通用集合之和（5,954 对 4,899）。真正新的不是"有垂直集合上榜"（那从 5 月起就断断续续成立），而是这次有一个垂直集合**领跑**。策略不变：精选集合按 Skills 浪潮条目跟踪，框架那一端通过 [Superpowers](agents/superpowers.md) 覆盖。
- 刚好卡在榜外：[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 44.8k（+975，周率涨 67%）、[CodeGraph](agents/codegraph.md) 69.1k（+814，周率涨 9%，从 #9 掉出）、[OpenClaw](agents/openclaw.md)（+792）。[n8n](agents/n8n.md) 又丢了位置，在参与排名的项目里按增量排第 16，周率降温 29%（203.1k，+527）——最近四个窗口里它坐稳过两个。
- [OpenClaw](agents/openclaw.md) 仍是绝对总数第一，388.5k star（+792，周率涨 40%）；它已有 profile，但因为这种体量的项目周环比增量噪声太大，不进按增量排名的表。
- **上窗口"新收录后的第一个窗口通常就是峰值"这个判断，只对了一半。** [QM](agents/qm.md) 连续第二次减速（−47%，14.4k）、[Open Code Review](agents/open-code-review.md) 连续第二次减速（−25%，21.8k），但 [Omnigent](agents/omnigent.md) 反转向上（+25%，9.6k），[Langfuse](agents/langfuse.md) 又一次基本持平（+4%，34.1k）。四个里只有两个继续掉，比本地图当时给的说法要弱——记在这里当作一次部分落空，而不是一次验证。
- **[eve](agents/eve.md) 第一次被 stamp 进快照，4,902**（`vercel/eve`），从本窗口起纳入跟踪；因为窗口开始时它还没被跟踪，所以暂时没有增量。本窗口新增的 [TrueForge](agents/trueforge.md)（5,038）已写入 profile 但还没开始抓取——按惯例新 profile 先带一个窗口的 `tracked: false`，下次刷新才进榜。
- **[Grok Build](agents/grok-build.md) 重新开始减速**：+235 到 26.3k，周率约 329 对上窗口的 640——上窗口那次回升没有延续，发布后的衰减又回来了。
- 本窗口仍在涨但没进前 10（按增量，5 天原始口径）：[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 44.8k（+975）、[CodeGraph](agents/codegraph.md) 69.1k（+814）、[OpenHands](agents/openhands.md) 85.9k（+681）、[Ruflo](agents/ruflo.md) 70.1k（+646）、[Claude Code](agents/claude-code.md) 143.7k（+593）、[n8n](agents/n8n.md) 203.1k（+527）、[CLI-Anything](agents/cli-anything.md) 48.8k（+502）、[LiteLLM](agents/litellm.md) 57.8k（+430）、[Cline](agents/cline.md) 67.3k（+381）、[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) 27.9k（+378）、[LangChain](agents/langchain.md) 145.4k（+373）、[LangGraph](agents/langgraph.md) 40.9k（+368）、[jcode](agents/jcode.md) 19.0k（+322）、[Open Code Review](agents/open-code-review.md) 21.8k（+315）、[CrewAI](agents/crewai.md) 58.0k（+312）、[Langfuse](agents/langfuse.md) 34.1k（+285）、[Goose](agents/goose.md) 53.8k（+275）、[Omnigent](agents/omnigent.md) 9.6k（+275）、[Grok Build](agents/grok-build.md) 26.3k（+235）、[QM](agents/qm.md) 14.4k（+188）、[AutoGPT](agents/autogpt.md) 187.1k（+162）、[Aider](agents/aider.md) 48.7k（+139）、[humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) 25.6k（+129）、[mini-swe-agent](agents/mini-swe-agent.md) 6.9k（+123）、[Kimi Code](agents/kimi-code.md) 7.2k（+115）、[anthropics/financial-services](https://github.com/anthropics/financial-services) 34.6k（+93）、[LlamaIndex](agents/llamaindex.md) 52.0k（+87）、[Letta（MemGPT)](agents/memgpt.md) 24.5k（+86）、[Continue](agents/continue.md) 35.7k（+81）、[OpenHarness](agents/openharness.md) 15.6k（+65）、[Open Interpreter](agents/open-interpreter.md) 68.2k（+60）、[MiMoCode](agents/mimocode.md) 12.9k（+42）、[SWE-agent](agents/swe-agent.md) 20.2k（+41）、[CodeWhale](agents/codewhale.md) 40.9k（+24）、[CoStrict](agents/costrict.md) 4.4k（+7）、[Flowise](agents/flowise.md) 55.4k（+5)）。

</details>

### 排名趋势

每周 Top 10 自开始追踪以来的名次变化——一条折线一个项目，折线中断表示该周掉出榜单：

<p align="center">
  <img src="../assets/heat-trend-zh.svg" alt="每周热度排行趋势图（bump chart）" width="100%" />
</p>

同样的窗口按"每层占几席"来读——就是每周叙事里那条 skills 浪潮故事的量化版：

<p align="center">
  <img src="../assets/heat-composition-zh.svg" alt="每周 Top 10 按层构成（堆叠柱状图）" width="100%" />
</p>

按类别的完整存量排行——Agent 榜、Agent 基础设施榜、Skill 榜及各自的垂类榜，按 star 总量排序——见 [rankings/](rankings/README.md)。

## 榜单之外

热度告诉你该看什么。这四页告诉你该选什么：

- **[能力矩阵](capabilities/matrix.md)** —— 每个项目在九个统一[能力维度](capabilities/README.md)上并排打分（●/◐/○/—），按路线分组。回答"就这项能力而言，谁把它当核心强项"。
- **[成本 & benchmark](comparisons/cost-and-benchmarks.md)** —— 前沿模型能力 vs 每 token 价格，加上每个编码 agent 实际怎么收费。模型层分档按量之后，"这个任务用哪一档"就是选型决策本身。
- **[记忆方案对比](comparisons/memory-approaches.md)** —— "有记忆"这句话背后的六种不同含义，从自编辑存储到被动语义召回，以及你要持久化什么就该选哪种。
- **[观测与评估](comparisons/observability-and-evals.md)** —— 上面这一切之下的那一层：agent 一旦无人值守地跑起来，故障就不再长得像崩溃，而是长得像静默的质量漂移。对比 [Langfuse](agents/langfuse.md)、Opik、Phoenix、Helicone、LangSmith 等——并理清这个领域里"开源"的四种不同含义。

## 市场脉搏

当下影响选型的三条结构性主线——完整的日期与来源档案见[市场事件](market-events.md)：

- **`.claude/skills` 浪潮持续复利——而且正在向一个目录集中**（2026-05 起）：curated skill 合集和 skills 框架已连续三个月占据每周热度前 10 的约一半，进入 8 月后席位数完全不动——连续三个窗口都是 4/10，最后一个窗口连成员都没轮换。还在动的是浪潮内部的结构：[mattpocock/skills](https://github.com/mattpocock/skills) 的增量现在超过另外三个之和，而一个月前它和它们持平。很多任务里技能层已经和底层 agent 同样重要；这种集中该读成关键人风险，而不是生态在扩张。本仓库通过 [Superpowers](agents/superpowers.md) 覆盖框架端，合集则在 [Skill 垂类榜](rankings/skill-verticals.md)里追踪。
- **模型层变成预算决策——而 9 月第一周，两家的天花板落到了同一个价位**：[Claude Fable 5.1](agents/claude-fable-5.md)（9 月 1 日）与 [GPT-6 Astra](agents/gpt-6-astra.md)（9 月 3 日）都标 **$10 / $50**，前沿对比因此不再是标价之争，而是**缓存读**（$0.25 对 $1）与**长上下文的计价形状**之争——Anthropic 的 1M 窗口整窗按标准价，OpenAI 输入超 272k token 后翻倍。往下看，大多数活其实该跑在档位阶梯上：一侧是 [Opus 5](agents/claude-opus-5.md)（$5/$25，7 月 24 日起是 Claude Code 的默认）与 Sonnet 5（$2/$10），另一侧是 GPT-5.6 的 Sol/Terra/Luna，其中 Sol 的促销价 $4/$20 至少到 11 月 21 日。完整表见[成本与基准](comparisons/cost-and-benchmarks.md)，血统见 [GPT-5.5](agents/gpt-5.5.md)。
- **产品边界在向上坍缩**：OpenAI 把 Codex 并入 ChatGPT 应用（7 月 9 日）——OpenAI 侧的"选哪个 coding agent"正在变成"你怎么用 ChatGPT"。而自 Codex CLI `rust-v0.153.4`（9 月 4 日）起，那里打包的默认模型已是 [GPT-6 Astra](agents/gpt-6-astra.md)，也就是说产品默认继承了 Astra 在网安上的受限行为。详见 [Codex](agents/codex.md)。

## 先把地图摊开

<p align="center">
  <img src="../assets/route-map-zh.svg" alt="AI Agent 选型地图——15 条路线按四类决策分组" width="100%" />
</p>

| 路线 | 代表项目 | 常见使用者 |
| --- | --- | --- |
| 直接执行型 | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [ZCode](agents/zcode.md), [OpenCode](agents/opencode.md), [Gemini CLI](agents/gemini-cli.md), [Qwen Code](agents/qwen-code.md), [Grok Build](agents/grok-build.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | 想把明确 coding 任务交给 agent 的人（见[终端编码 CLI 对比](comparisons/coding-cli-agents.md)） |
| Agent harness 框架 | [DeepSeek Harness](agents/deepseek-harness.md), [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [TrueForge](agents/trueforge.md) | 想自己掌控 agent loop、工具表面和权限，而不是直接接受厂商成品的人——QM 和 Omnigent 把这条推到"在一层之下同时跑*多个* harness"（见 [harness 框架对比](comparisons/agent-harness-frameworks.md)） |
| 前沿 agentic 模型 | [Claude Fable 5.1](agents/claude-fable-5.md), [Claude Opus 5](agents/claude-opus-5.md), [GPT-6 Astra](agents/gpt-6-astra.md), [GPT-5.5](agents/gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 Anthropic / OpenAI 系 agent 能力上限的人——天花板（Fable 5.1、Astra）和你实际会跑的默认档（Opus 5）是两个独立决策 |
| 开放权重 agentic 模型 | [Kimi K3](agents/kimi-k3.md), [GLM-5.3](agents/glm-5.md), [DeepSeek V4](agents/deepseek-v4.md), [Qwen3-Coder](agents/qwen3-coder.md) | 想在自己托管、自己承担许可的权重上拿到前沿级能力的人——这和在几个闭源天花板之间做选择是两个不同的决策 |
| Agentic skills 框架 | [Superpowers](agents/superpowers.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上的人 |
| 工作流 / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | 已经认可 Claude Code 或 Codex，只想在上面补强 orchestration 的人（Ruflo 把这条进一步推到跨机器联邦和 100+ 专用 agent） |
| 编辑器中心工作流 | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | 想让编辑器本身保持在工作流核心的人 |
| review-first 自动化 | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md), [Open Code Review](agents/open-code-review.md) | 想把 review 和人工控制留在核心的人（CoStrict 加了企业严格流程 + 私有化部署；Open Code Review 只做评审，为 CI 里的准确率调优） |
| 管理式后台路径 | [Claude Managed Agents](agents/claude-managed-agents.md) | 需要 Anthropic 的定时、云端或后台工作流的人 |
| 通用自主 agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md), [WorkBuddy](agents/workbuddy.md), [Kimi Work](agents/kimi-work.md) | 想要通用自主任务执行的人（ml-intern 是 ML 工程取向的特化版本） |
| 自建系统 | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | 想自己搭 agent 平台的团队 |
| 运行时 & 工具 | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [CLI-Anything](agents/cli-anything.md) | 需要工作流自动化、代码执行、LLM 网关、agent 上下文基础设施、agent 驱动 CLI 或可视化构建器的团队 |
| 观测与评估 | [Langfuse](agents/langfuse.md) | agent 已经跑在生产上，需要知道它做了什么、花了多少、质量有没有漂移的人（见[观测与评估](comparisons/observability-and-evals.md)） |
| 浏览器 agent | [Browser Use](agents/browser-use.md) | 任务活在一个没有 API 的网站上的人——这和"agent 怎么改文件"是两个问题，因为它决定的是允许一个 agent 以你的身份在开放互联网上做什么 |
| 自托管 / 本地 runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | 需要端侧隐私、长期运行、本地控制、渠道、设备或个人数据生活集成能力的人 |

## 当前已覆盖的主流项目

已收录 77 个项目，按形态分组。展开任意一组，或到 [agents/](agents/README.md) 浏览完整的路线表与覆盖表。

<details>
<summary><strong>编码 agent、编辑器与编排</strong>（32 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Aider](agents/aider.md) | 直接执行 | 终端优先、贴近 git 的 AI 结对编程 |
| [Claude Code](agents/claude-code.md) | 直接执行 | 本地和 IDE 优先的 coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | 管理式后台路径 | Anthropic 管理式 / 云端执行工作流映射 |
| [Codex](agents/codex.md) | 直接执行 | ChatGPT 应用内的 coding agent，支持异步云端委派 |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | 工作流层 | Claude Code 之上的 teams-first orchestration layer |
| [oh-my-codex](agents/oh-my-codex.md) | 工作流层 | 为 Codex CLI 增强工作流、teams 和持久状态 |
| [Cursor](agents/cursor.md) | 编辑器中心平台 | 覆盖本地编码、云端 agent 和集成的 AI 编辑器 |
| [GitHub Copilot](agents/github-copilot.md) | 平台 | VS Code + GitHub 里的多表面 agent 平台 |
| [Cline](agents/cline.md) | review-first 执行 | 编辑器内 approval-first coding agent |
| [Windsurf](agents/windsurf.md) | AI 原生 IDE | 以 Cascade 为中心的 AI IDE |
| [OpenHands](agents/openhands.md) | 开源执行 | 开源 AI 软件工程 agent |
| [Devin](agents/devin.md) | 托管执行 | 端到端软件工程执行 |
| [Jules](agents/jules.md) | 托管云端执行 | GitHub 连接、PR 回收的 coding delegation |
| [Continue](agents/continue.md) | 编辑器中心 | 支持自选模型的开源 IDE 扩展 |
| [Froge Code](agents/froge-code.md) | review-first 自动化 | 当前按 Automagik Genie 暂定映射 |
| [Pi](agents/pi.md) | 直接执行 | 极简终端 coding agent harness，多 LLM provider 支持 |
| [jcode](agents/jcode.md) | Agent harness 框架 | Rust 多会话 coding harness——启动最快、provider 中立 OAuth、被动语义记忆 |
| [CodeWhale](agents/codewhale.md) | 直接执行 | DeepSeek + MiMo 终端 coding agent（原 DeepSeek-TUI） |
| [Kimi Code](agents/kimi-code.md) | 直接执行 | Moonshot AI 官方、Kimi 原生的终端 coding CLI（kimi-cli 继任者） |
| [MiMoCode](agents/mimocode.md) | 直接执行 | 小米官方的 MiMo 终端 coding agent，内置跨会话记忆 |
| [Grok Build](agents/grok-build.md) | 直接执行 | SpaceXAI 官方的 Rust 终端 coding agent——全屏 TUI、headless CI 模式、ACP 编辑器服务 |
| [CoStrict](agents/costrict.md) | review-first 自动化 | Cline 血统的企业 coding agent，含严格标准化流程、AI 代码评审、私有化部署 |
| [SWE-agent](agents/swe-agent.md) | Agent harness 框架 | Princeton + Stanford 的 SWE-bench 原始 harness，single-YAML 配置 |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness 框架 | SWE-agent 的 ~100 行 Python 接班版，SWE-bench Verified 仍 >74% |
| [OpenHarness](agents/openharness.md) | Agent harness 框架 | HKUDS 的 10 子系统开源 agent harness，43+ 工具、兼容 anthropics/skills、支持 MCP |
| [Omnigent](agents/omnigent.md) | Agent harness 框架 | 元 harness——在一个会话里混用 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi，带策略与云沙箱 |
| [OpenCode](agents/opencode.md) | 直接执行型 | 体量最大的厂商中立开源编码 agent——20.5 万 star，MIT |
| [Gemini CLI](agents/gemini-cli.md) | 直接执行型 | 谷歌的终端 agent；每天 1,000 次免费请求，内置搜索接地 |
| [Qwen Code](agents/qwen-code.md) | 直接执行型 | 客户端与权重都开放，可在 OpenAI/Anthropic/Gemini/本地之间运行时切换 |
| [DeepSeek Harness](agents/deepseek-harness.md) | Agent harness 框架 | 一切皆插件的 harness——连 agent 循环本身都能从配置里换掉 |
| [ZCode](agents/zcode.md) | 直接执行型 | 智谱的桌面 agentic 开发环境：长周期 "Goal" 任务，可从微信/飞书/Telegram 远程操控 |
| [Open Code Review](agents/open-code-review.md) | review-first 自动化 | 阿里的准确率优先代码评审 CLI——模型外面包确定性流水线，带 CI 与 agent 插件表面 |

</details>

<details>
<summary><strong>自主与自托管 agent</strong>（17 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [AI Edge Gallery](agents/ai-edge-gallery.md) | 端侧本地 runtime | 带 agent skills 的移动端本地 assistant 沙盒 |
| [Goose](agents/goose.md) | 开源本地平台 | 跨 desktop、CLI、API 的可扩展本地 agent |
| [Hermes Agent](agents/hermes-agent.md) | 多 agent / 自托管 | 带 memory、skills、gateway 的长期工作环境 |
| [OpenClaw](agents/openclaw.md) | runtime | 多渠道、多设备、本地优先运行层 |
| [AutoGPT](agents/autogpt.md) | 自主 agent 平台 | 可视化 agent 构建器，带工作流、市场和多模型支持 |
| [Agent Zero](agents/agent-zero.md) | 自主 agent | 自构建自主 agent，动态创建工具 |
| [BabyAGI](agents/babyagi.md) | 实验性 | 开创性自主 agent 实验——教学用，非生产 |
| [Open Interpreter](agents/open-interpreter.md) | 运行时 | 自然语言到本地代码执行，无沙盒 |
| [Mercury Agent](agents/mercury-agent.md) | 自托管多通道 | 主打 CLI + Telegram 的权限硬化 agent，带 token 预算 |
| [ml-intern](agents/ml-intern.md) | 垂直领域自主 agent | Hugging Face 的自主 ML 工程师——基于 HF 生态做研究、写代码、发布 ML 成果 |
| [GenericAgent](agents/generic-agent.md) | 自演进自主 agent | 从小种子起步、每完成任务长出 skill tree 的自主 agent |
| [OpenHuman](agents/openhuman.md) | 自托管 / 本地 runtime | 桌面生活集成 agent，118+ 连接器、本地 Memory Tree、支持 Ollama |
| [Julep](agents/julep.md) | 工作流引擎 | Temporal 支撑的持久化有状态 AI agent 工作流引擎 |
| [QM](agents/qm.md) | Agent harness 框架 | Y Combinator 的多人协作 agent，跑在 Slack 和 web——按人和按房间分作用域、自托管、harness 无关 |
| [WorkBuddy](agents/workbuddy.md) | 通用自主 agent | 腾讯的桌面办公 agent——同一套循环，指向文档、幻灯片与表格 |
| [Kimi Work](agents/kimi-work.md) | 通用自主 agent | 月之暗面的桌面知识工作 agent：挂载文件夹、浏览器自动化、内置 cron |
| [TrueForge](agents/trueforge.md) | Agent harness 框架 | harness 即服务端——一个循环挂在 HTTP API 后面，带聊天 UI、TypeScript SDK 与可嵌入 UI |

</details>

<details>
<summary><strong>框架与基础设施</strong>（19 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [eve](agents/eve.md) | 自建平台 | Vercel 的文件系统优先 agent 框架——持久化执行、沙箱、审批、渠道、evals |
| [LangChain](agents/langchain.md) | 平台 | 快速搭自定义 agent 的高层框架 |
| [LangGraph](agents/langgraph.md) | 平台 | 搭持久化、有状态 agent workflow 的底层框架 |
| [CrewAI](agents/crewai.md) | 多 agent 框架 | 角色型 agent 协作，快速搭原型 |
| [LlamaIndex](agents/llamaindex.md) | 数据优先框架 | 基于文档和数据的 RAG 与 agentic 应用 |
| [n8n](agents/n8n.md) | 工作流自动化 | 带原生 AI agent 节点和 400+ 集成的可视化工作流平台 |
| [MemGPT](agents/memgpt.md) | 有状态 agent 平台 | 跨会话学习的持久记忆 agent（现名 Letta） |
| [Haystack](agents/haystack.md) | 框架 | deepset 的生产导向 RAG 和 agent 框架 |
| [Semantic Kernel](agents/semantic-kernel.md) | 框架 | 微软的 AI 编排 SDK，支持 .NET、Python、Java |
| [DSPy](agents/dspy.md) | 框架 | 程序化 prompt 优化——编程而非手调 LM |
| [LiteLLM](agents/litellm.md) | 基础设施 | 100+ LLM provider 的统一 API 网关 |
| [Langfuse](agents/langfuse.md) | 基础设施 | 开源的 agent 观测、评估与 prompt 管理（观察 agent，不运行 agent） |
| [Pydantic AI](agents/pydantic-ai.md) | 框架 | 类型安全 Python agent 框架，结构化输出 |
| [Flowise](agents/flowise.md) | 可视化构建器 | 基于 LangChain 的拖拽式 LLM 应用和 agent 构建器 |
| [Ruflo](agents/ruflo.md) | 工作流 / orchestration layer | 面向 Claude 的多 agent 编排平台，支持跨机器联邦、神经记忆和 100+ 专用 agent |
| [CodeGraph](agents/codegraph.md) | 运行时 & 工具 | 为 Claude Code、Cursor、Codex CLI、opencode、Hermes Agent 提供预索引的代码知识图谱 + MCP server |
| [Browser Use](agents/browser-use.md) | 浏览器 agent | 把一个真浏览器交给 agent——打开页面、点击、输入、填表单 |
| [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | 自建系统 | AutoGen 的继任者；跨 Python、.NET、Go 的生产级多 agent 工作流 |
| [CLI-Anything](agents/cli-anything.md) | 运行时 & 工具 | 为任意软件自动生成 Click CLI，让 agent 能驱动没有 API 的应用 |

</details>

<details>
<summary><strong>模型与技能</strong>（9 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Claude Fable 5.1](agents/claude-fable-5.md) | 前沿 agentic 模型 | Anthropic 的 Mythos 级天花板——你花额度去买的那个模型，2026-09-01 刷新 |
| [Claude Opus 5](agents/claude-opus-5.md) | 前沿 agentic 模型 | 天花板一半价格的 Opus 档——大多数 Claude 系 agent 真正在跑的模型 |
| [GPT-6 Astra](agents/gpt-6-astra.md) | 前沿 agentic 模型 | OpenAI 当前的天花板（2026-09-03），面向公众发布的是受限版本 |
| [GPT-5.5](agents/gpt-5.5.md) | 前沿 agentic 模型 | OpenAI 2026 春季的模型，作为 GPT-5.6 到 Astra 的血统参照保留 |
| [Kimi K3](agents/kimi-k3.md) | 开放权重 agentic 模型 | 首个开放的 3T 级模型——2.8T 参数、原生视觉、100 万上下文、自定义许可 |
| [GLM-5.3](agents/glm-5.md) | 开放权重 agentic 模型 | 按厂商数字最强的开放权重编码模型，Apache-2.0——且网安能力不设闸 |
| [DeepSeek V4](agents/deepseek-v4.md) | 开放权重 agentic 模型 | 1.6T 参数下的 MIT；SWE-bench Verified 80.6，且因权重开放而可复现 |
| [Qwen3-Coder](agents/qwen3-coder.md) | 开放权重 agentic 模型 | 塞得进去的那个——80B 里激活约 3B，256K→100 万上下文，跑在你所在的地方 |
| [Superpowers](agents/superpowers.md) | Agentic skills 框架 | 一整套方法论 + 可组合 skills 层，可接到 Claude Code、Codex、Cursor 等 agent 之上 |

</details>

## 可以这样开始

如果还不确定从哪里切入，可以先按这些示意路径读一轮，再按自己的场景分支出去。

| 如果你更像这样 | 推荐阅读路径 | 这条路径会帮你回答什么 |
| --- | --- | --- |
| 我想找一个日常 coding agent，但还没想清楚终端还是编辑器 | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [终端编码 CLI 对比](comparisons/coding-cli-agents.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [use-cases/coding-automation.md](use-cases/coding-automation.md) | 哪个厂商 CLI 配你的模型、终端优先 vs 编辑器中心 vs 强审批控制怎么取舍 |
| 我已经喜欢 Claude Code 或 Codex，但想补强 orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 底层 agent 够不够用，什么时候值得再加一层工作流 |
| 我想搞清楚 2026 模型竞赛怎么改变 agent 选型 | [Claude Fable 5.1](agents/claude-fable-5.md) → [Claude Opus 5](agents/claude-opus-5.md) → [GPT-6 Astra](agents/gpt-6-astra.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [市场事件](market-events.md) | 前沿档与其下的默认档怎样抬高能力天花板，又怎样影响产品选型 |
| 我想要专用 AI IDE，而不是继续拼装工具 | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | AI 原生编辑器和生态型平台怎么区分 |
| 我想把 ticket 交出去，过一会儿再回来验收 | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 异步云端委派和管理式后台自动化有什么差别 |
| 我需要开源、自托管或者更强本地控制面 | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | 终端控制、开源执行和本地运行控制面的取舍 |
| 我不是买产品，而是要搭自己的 agent 体系 | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | framework、runtime、product 三者边界怎么分 |

## 免责声明

表格里的 star 数和 7 天增量，都是仓库更新时点抓取的 GitHub 快照；不同周次之间会出现波动，少量取整误差也是正常的。每个项目的描述、厂商和能力总结，反映的是写作时点的公开信息，可能因项目演进、被收购、转型而过时。本仓库提供的是**选型参考**，不是背书、不是投资建议、也不是生产可用性保证。最终决策前请以各项目自己的官方文档为准。