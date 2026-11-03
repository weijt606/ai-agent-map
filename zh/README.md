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

> **最后更新：** 2026-11-03 · **快照窗口：** 2026-10-28 → 2026-11-03（自上次更新以来的增量，**6 天**，上一个窗口 7 天，增量列不能和上周直接比，下面的比较都按周率）· **star 数：** 更新时点抓取

项目名链接指向上游 GitHub 仓库。本仓库已写入的 profile，在"在本仓库中的状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 在本仓库中的状态 | 应该怎么读 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（=） | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 269.8k | +6,264 | 已收录 · [profile](agents/deepseek-harness.md) | **守住 #1**，这是它第一次连续两个窗口坐榜首（09-30 那次只坐一期），29 个窗口里第三个 #1。约 7,308/周：与上期大致持平，是 09-17 以来最快。越过 **26.5 万**，**差 216 到 27 万**。窗口内只有预发布版（`dsh-v0.2.1-rc.4`、`rc.5`、`v0.2.2-alpha.2`） |
| #2&#8288;（=） | [mattpocock/skills](https://github.com/mattpocock/skills) | 310.3k | +5,633 | 候补（Skills 浪潮） | 周率涨 **20%**，仍是 #2。**越过 31 万**（310,320），距 [Superpowers](agents/superpowers.md) 缩到 967（上期 1,457）。增量比其他三个通用集合之和*少* 3,943。一个补丁版 `v1.3.2`（10 月 29 日） |
| #3&#8288;（↑） | [Superpowers](https://github.com/obra/superpowers) | 311.3k | +5,143 | 已收录 · [profile](agents/superpowers.md) | 周率涨 **81%** 到约 6,000/周，是 07-08 以来最快，名次升一位。**越过 31 万**（311,287），仍以 967 领先成为最大的集合。窗口内默认分支没有发版也没有提交，原因查不到，按尖峰算 |
| #4&#8288;（↓） | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 120.0k | +2,874 | 候补（金融垂直） | 上期尖峰后周率降 28%，但保住席位：只掉一位，没有离榜。**以 1 个 star 越过 12 万**（120,001）。窗口内没有发版 |
| #5&#8288;（↑） | [anthropics/skills](https://github.com/anthropics/skills) | 186.8k | +2,626 | 候补（Skills 浪潮） | 周率涨 **97%**，从 #10 到 #5：06-17 以来最快的周率，09-06 以来最好的名次。越过 **18.5 万**。窗口内一个提交（10 月 28 日更新 `mcp-builder`） |
| #6&#8288;（=） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 259.9k | +2,252 | 已收录 · [profile](agents/hermes-agent.md) | 周率涨 37%，名次不变。**29 个记录窗口全部在榜**。一个版本 `v0.22.6`（11 月 2 日）。**差 96 到 26 万** |
| #7&#8288;（↓） | [OpenCode](https://github.com/anomalyco/opencode) | 224.1k | +1,867 | 已收录 · [profile](agents/opencode.md) | 周率降 23%，2.0 爆发后连续第二次放缓；连续第九次在榜。窗口内发了 `v2.2.1`–`v2.2.5` |
| #8&#8288;（↓） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 112.8k | +1,807 | 候补（Skills 浪潮） | 周率涨 11%，结束连续两次放缓，但名次降一位。两个版本（`0.6.14`、`0.6.15`） |
| #9&#8288;（新） | [Codex CLI](https://github.com/openai/codex) | 132.9k | +1,648 | 已收录 · [profile](agents/codex.md) | 从第 15 升上来：周率涨 **91%**，09-17 以来第一次在榜，09-01 以来最快的周率。`rust-v0.165.0`、`rust-v0.166.0` 把 GPT-6.1 Terra 加进模型目录，默认模型没变 |
| #10&#8288;（新） | [Pi](https://github.com/earendil-works/pi) | 119.6k | +1,392 | 已收录 · [profile](agents/pi.md) | 从第 12 升上来：周率涨 18%，10-14 以来第一次在榜。`v1.5.0` 于 11 月 2 日发布 |

- 热度适合拿来发现新项目，不适合直接当选型顺序。
- **本窗口 6 天，上一个窗口 7 天**，两列增量不能直接比：下面所有"涨/降"都按周率（增量 ÷ 6 × 7）。周率和这张表一直以来一样按整日期计算，所以个位数的变化按持平看。
- **全榜回暖。** 57 个可测仓库里 **34 个加速、23 个放缓**（上期 15 个与 42 个）。前十席 6 天合计增量 31,506，约合每周 36,757，上期 31,952（涨 15%）；#10 的门槛涨约 4%（1,556 → 约 1,624/周）。十个上榜者里八个提速；只有 [TradingAgents](https://github.com/TauricResearch/TradingAgents) 和 [OpenCode](agents/opencode.md) 放缓。
- **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 第一次守住 #1。** 09-30 那次只坐一期，这次已是连续两期，约 7,308/周，是 09-17 以来最快。29 个窗口里它有三个 #1，[mattpocock/skills](https://github.com/mattpocock/skills) 有 15 个。窗口内只有预发布版；越过 26.5 万。
- **集合榜首的差距缩小了，但没有反超。** mattpocock/skills（310,320）和 [Superpowers](agents/superpowers.md)（311,287）都越过 31 万，差距从 1,457 缩到 **967**。mattpocock 本期只多涨 490，更值得看的是 Superpowers：周率涨 **81%**，却没有发版，默认分支没有提交，原因查不到。按本榜的规矩，第二个窗口确认之前都算尖峰。
- **上期的尖峰分了岔。** [TradingAgents](https://github.com/TauricResearch/TradingAgents) 还回 28% 但保住席位（#4），以 1 个 star 越过 12 万。[Gemini CLI](agents/gemini-cli.md) 还回 **88%**（+116，第 38），那次 +665% 只是单窗口事件，原因仍查不到。[Ruflo](agents/ruflo.md)（降 33%，第 11）和 [CLI-Anything](agents/cli-anything.md)（降 44%，第 15）离榜，infra 从两席变成**零席**，是 10-14 以来第一次。
- **浪潮连续第四个窗口占 4/10**（#2、#3、#5、#8），连续第二个窗口全是通用集合。[anthropics/skills](https://github.com/anthropics/skills) 周率接近翻倍，从 #10 到 #5；mattpocock 的增量比其他三个之和**少 3,943**（5,633 对 5,143 + 2,626 + 1,807 = 9,576）。其余六席都是 agent（#1、#4、#6、#7、#9、#10）；[Codex CLI](agents/codex.md)（#9）和 [Pi](agents/pi.md)（#10）回榜。Hermes Agent（29/29）、Superpowers 和 mattpocock/skills（各 24）是仍在继续的长连续；DeepSeek Harness 和 OpenCode 各 9，紧随其后。
- **模型层动的是路由和计费，不是价格或默认模型。** (1) **GitHub 于 10 月 28 日让 Copilot Fusion 正式可用**：选 Fusion，由 Copilot 替你在模型之间路由。GitHub 说 Fusion Max 在 Artificial Analysis Coding Agent Index 上得 60 分，与 Claude Code 配 Opus 5.5 Max 相差不到两分，平均每个任务的 API 成本约为一半；这是 GitHub 自己的说法，本图没有抄进基准表。(2) **Copilot 现在包含在 GitHub Enterprise 里**（面向有客户团队对接的企业），AI 用量"metered from the first request"，让 Copilot 的一部分离开了固定席位。(3) **OpenAI 发布 GPT-6 Rosalind**（10 月 30 日，$15 / $75，生命科学领域的受信访问），不是编码模型，不进 cost 表。(4) **Kimi K3.1 Pro 的权重截至今天还没发布**，距月之暗面承诺的 11 月 4 日还有一天，quickstart 仍是 `[xx.x%]` 占位符，所以继续不进开放权重表。(5) **Google 将在 12 月 1 日把 `gemini-2.5-pro` 路由到 `gemini-3.8-flash`**；这个字符串仍是 [Gemini CLI](agents/gemini-cli.md) 源码里的默认值，值得盯。**连续第五个窗口没有被跟踪的编码 agent 换默认模型**：[Claude Code](agents/claude-code.md) `v2.1.312`–`v2.1.317`、[Codex CLI](agents/codex.md) `rust-v0.166.0`（Terra 进目录，Sol 仍排第一）、Gemini CLI `v0.66.0`、[OpenCode](agents/opencode.md) `v2.2.5`（它的"New Default Model Picker"是界面改动）。[cost 表](comparisons/cost-and-benchmarks.md)每一行都回 Anthropic、OpenAI、Google、Meta 的价格页核过，没有价格变化；两个促销（GPT-5.6 Sol 至少到 11 月 21 日，Gemini 4 Argon 到 11 月 30 日）仍有效。表里三处说明有错或过时，已就地更正。详见[市场事件](market-events.md)。
- **个人 agent 与 skills 两页已刷新。** [Muse](agents/meta-muse.md) 在新加坡开放（10 月 27 日），[ChatGPT dots](agents/chatgpt-dots.md) 为美国 Pro 用户加了短信入口，见[最近变化](comparisons/personal-agents.md#最近变化)。[Agent Skills](comparisons/agent-skills.md) 页改用本期快照，[ECC](agents/ecc.md) 与 [Superpowers](agents/superpowers.md) 已按它们现在的 README 更正。
- **五个仓库进入跟踪**：[Graphify](agents/graphify.md) 141,261、[ECC](agents/ecc.md) 295,725、[Orca](agents/orca.md) 113,699、[claude-mem](agents/claude-mem.md) 110,842、[Paperclip](agents/paperclip.md) 110,458。它们现在已进[分类榜](rankings/README.md)，第一个可测增量在下一期。**本窗口无新 profile。**
- 里程碑（按原始整数核过，不是表里四舍五入的数）：**Superpowers 与 mattpocock/skills 31 万**、DeepSeek Harness **26.5 万**、anthropics/skills **18.5 万**、TradingAgents **12 万**、[Ruflo](agents/ruflo.md) **8 万**、scientific-agent-skills 与 academic-research-skills **5.5 万**、[agentmemory](https://github.com/rohitg00/agentmemory) **3 万**、[Trail Code](agents/graft.md) **1.1 万**、[mini-swe-agent](agents/mini-swe-agent.md) **9k**。差一点：[Aider](agents/aider.md) **差 85 到 5 万**，Hermes Agent 差 96 到 26 万，[Browser Use](agents/browser-use.md) 差 120 到 12 万，DeepSeek Harness 差 216 到 27 万。
- [OpenClaw](agents/openclaw.md) 仍是绝对第一，393.8k star（+559，周率涨 17%）；已写 profile，但不进增量榜，因为这么大的项目周度增量噪声太大。

<details>
<summary>更多窗口笔记：skills 浪潮占比、OpenClaw，以及前 10 之外还在涨的项目</summary>

- `.claude/skills` 浪潮**连续第四个窗口占前十中的四席**：#2、#3、#5、#8，连续第二个窗口全是通用集合。政策不变：curated 集合作为 Skills Wave 条目跟踪，在 [Agent Skills](comparisons/agent-skills.md) 页比较；框架端通过 [Superpowers](agents/superpowers.md) 和 [ECC](agents/ecc.md) 写 profile。
- 刚好卡在榜外：[Ruflo](agents/ruflo.md) 80.7k（+954）第 11，降 33%，越过 8 万；scientific-agent-skills 55.8k（+927）第 12，降 27%；academic-research-skills 55.1k（+903）第 13，涨 19%；[Open Code Review](agents/open-code-review.md) 49.3k（+788）第 14，涨 27%；[CLI-Anything](agents/cli-anything.md) 58.1k（+772）第 15，降 44%，9 月 22 日以来仍无提交；[Claude Code](agents/claude-code.md) 154.3k（+742）第 16，降 5%，四个版本（`v2.1.312`–`v2.1.317`）。OpenClaw 不进榜，所以这些榜外名次也按同样口径算。
- **两个科研集合几乎并列。** academic-research-skills 提速、scientific-agent-skills 放缓，两者都越过 5.5 万；K-Dense 仍更大，55,849 对 55,061。[Gemini CLI](agents/gemini-cli.md) 从第 13 掉到第 38。[anthropics/financial-services](https://github.com/anthropics/financial-services) 继续放缓（+148，降 32%，第 34）。
- 本窗口仍在涨但没进前 10（按增量，6 天原始口径）：[Ruflo](agents/ruflo.md) 80.7k（+954）、[scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 55.8k（+927）、[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 55.1k（+903）、[Open Code Review](agents/open-code-review.md) 49.3k（+788）、[CLI-Anything](agents/cli-anything.md) 58.1k（+772）、[Claude Code](agents/claude-code.md) 154.3k（+742）、[CodeGraph](agents/codegraph.md) 76.3k（+670）、[n8n](agents/n8n.md) 209.4k（+630）、[Browser Use](agents/browser-use.md) 119.9k（+589）、[OpenHands](agents/openhands.md) 92.5k（+528）、[LiteLLM](agents/litellm.md) 62.6k（+422）、[LangGraph](agents/langgraph.md) 44.4k（+360）、[LangChain](agents/langchain.md) 148.9k（+357）、[Goose](agents/goose.md) 56.2k（+335）、[Cline](agents/cline.md) 71.2k（+316）、[Langfuse](agents/langfuse.md) 36.9k（+309）、[CrewAI](agents/crewai.md) 60.4k（+260）、[Trail Code (Graft)](agents/graft.md) 11.0k（+225）、[jcode](agents/jcode.md) 21.4k（+182）、[Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.5k（+160）、[agentmemory](https://github.com/rohitg00/agentmemory) 30.1k（+158）、[mini-swe-agent](agents/mini-swe-agent.md) 9.0k（+155）、[Qwen Code](agents/qwen-code.md) 28.9k（+149）、[anthropics/financial-services](https://github.com/anthropics/financial-services) 41.0k（+148）、[Aider](agents/aider.md) 49.9k（+143）、[OpenHuman](agents/openhuman.md) 42.5k（+134）、[ZCode](agents/zcode.md) 8.4k（+128）、[Gemini CLI](agents/gemini-cli.md) 108.7k（+116）、[Omnigent](agents/omnigent.md) 11.2k（+97）、[AutoGPT](agents/autogpt.md) 187.9k（+96）、[Grok Build](agents/grok-build.md) 27.7k（+92）、[LlamaIndex](agents/llamaindex.md) 52.8k（+90）、[Open Interpreter](agents/open-interpreter.md) 68.8k（+90）、[eve](agents/eve.md) 5.8k（+77）、[Kimi Code](agents/kimi-code.md) 8.1k（+74）、[QM](agents/qm.md) 15.6k（+65）、[12-factor-agents](https://github.com/humanlayer/12-factor-agents) 27.0k（+64）、[SWE-agent](agents/swe-agent.md) 20.7k（+59）、[Letta (MemGPT)](agents/memgpt.md) 25.3k（+55）、[Continue](agents/continue.md) 36.4k（+50）、[OpenHarness](agents/openharness.md) 16.2k（+45）、[TrueForge](agents/trueforge.md) 6.4k（+36）、[CodeWhale](agents/codewhale.md) 41.2k（+33）、[Flowise](agents/flowise.md) 55.5k（+15）、[MiMoCode](agents/mimocode.md) 13.7k（+9）、[CoStrict](agents/costrict.md) 4.5k（+2）

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

热度告诉你该看什么。这六页告诉你该选什么：

- **[能力矩阵](capabilities/matrix.md)** —— 每个项目在九个统一[能力维度](capabilities/README.md)上并排打分（●/◐/○/—），按路线分组。回答"就这项能力而言，谁把它当核心强项"。
- **[成本 & benchmark](comparisons/cost-and-benchmarks.md)** —— 前沿模型能力 vs 每 token 价格，加上每个编码 agent 实际怎么收费。模型层分档按量之后，"这个任务用哪一档"就是选型决策本身。
- **[记忆方案对比](comparisons/memory-approaches.md)** —— "有记忆"这句话背后的七种不同含义，从自编辑存储到被动语义召回，以及你要持久化什么就该选哪种。
- **[消费级个人 agent](comparisons/personal-agents.md)** —— 你把日常交出去的那类 agent——ChatGPT dots、Gemini Task、Claude、Muse、Grok Bot、Cue、豆包、千问、AutoGLM、元宝、Today——按事实和控制力比较，而不是按热度，因为闭源产品没有可供排名的公开数字。
- **[Agent Skills](comparisons/agent-skills.md)** —— skill 是什么、哪些 agent 能加载它，以及最大的五个集合和框架（Superpowers、mattpocock/skills、ECC、anthropics/skills、addyosmani/agent-skills）在类型、体量、维护者和许可证上的对比，外加装别人的 skill 前要查什么。集合在这里比较，不单独写 profile。
- **[观测与评估](comparisons/observability-and-evals.md)** —— 上面这一切之下的那一层：agent 一旦无人值守地跑起来，故障就不再长得像崩溃，而是长得像静默的质量漂移。对比 [Langfuse](agents/langfuse.md)、Opik、Phoenix、Helicone、LangSmith 等——并理清这个领域里"开源"的四种不同含义。

## 市场脉搏

当下影响选型的三条结构性主线——完整的日期与来源档案见[市场事件](market-events.md)：

- **`.claude/skills` 浪潮连续第四个窗口占四席，最大的两个集合都越过 31 万**（2026-05 起）：curated skill 合集与 skills 框架五个月来一直占据每周热度前 10 的 2 到 6 席，席位数一直在轮换而不是不动：6/10，然后 2/10、3/10、4/10、5/10、3/10，接着连续四个窗口 **4/10**（2026-11-03）。四席连续第二个窗口全是通用集合：[mattpocock/skills](https://github.com/mattpocock/skills)、[Superpowers](agents/superpowers.md)、[anthropics/skills](https://github.com/anthropics/skills)、[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)。mattpocock（310,320）距 Superpowers（311,287）967 个 star，增量比其他三个之和少 3,943，本图自 6 月以来提示的单人风险继续缓和。[ECC](agents/ecc.md)（295,725）本窗口进入跟踪，是 [skill 榜](rankings/skill-verticals.md)上第三大的集合。本图通过 Superpowers 和 ECC 写框架端的 profile，集合放在 [Agent Skills](comparisons/agent-skills.md) 页比较。
- **模型层变成预算决策——而两家的阶梯现在每一级都有人了**：[Claude Fable 5.1](agents/claude-fable-5.md)（9 月 1 日）与 [GPT-6 Astra](agents/gpt-6-astra.md)（9 月 3 日）仍都标 **$10 / $50**；往下是 **Opus 5.5**（$4 / $20，9 月 22 日）、两个中间档 **Sonnet 5.5** 与 **GPT-6.1 Sol**（都是 $2 / $10，9 月 28–29 日，各是自家编码 agent 的默认），再往下是地板：**GPT-6 Luna**（$0.10 / $0.50，9 月 22 日）与 **Claude Haiku 5.5**（10 月 7 日，prompt 不超过 10 万 token 时 $0.10 / $0.50，超过则 $0.50 / $2.50）。**10 月 26 日** OpenAI 又用 **GPT-6.1 Terra**（**$1 / $5**，缓存读 $0.05）补上了地板与中间档之间那一级，可在 Codex 里选用，但没有设为默认。Google 于 **10 月 13 日**加入了有标价的行列：**Gemini 4 Argon** 开放付费 API，$2 / $10 至 11 月 30 日，之后 $4 / $20；Meta 的 **Muse Wonder**（10 月 12 日）则落在 **$4 / $20、缓存读 $0.20**——和 Opus 5.5 一模一样，于是 $4 / $20 成了三家共用的价位。本地图此前说把两个中间档分开的那一列已经合上了：Anthropic 的价格页现在把 Sonnet 5.5 的缓存读标为 **$0.10/M**，不是从 9 月 28 日 changelog 记下的 $0.20（Claude Code `v2.1.296` 于 10 月 9 日改正了自己的数字），所以 Sonnet 5.5 与 GPT-6.1 Sol 在标价和缓存上完全相同。还能分开它们的是长上下文的计价形状（OpenAI 输入超 272k token 后对整个请求换价，Anthropic 不这样；Haiku 5.5 则按 prompt 长度分价）。见[成本 & benchmark](comparisons/cost-and-benchmarks.md)。
- **产品边界在向上坍缩**：OpenAI 把 Codex 并入 ChatGPT 应用（7 月 9 日），又在 DevDay（9 月 29 日）用可在任何设备上使用的可复用云端环境，把它进一步搬离笔记本——OpenAI 侧的"选哪个 coding agent"继续在变成"你怎么用 ChatGPT"。打包默认模型一个月里换了两次：`rust-v0.153.4`（9 月 4 日）起是 [GPT-6 Astra](agents/gpt-6-astra.md)，`rust-v0.159.1`（9 月 29 日）起是 **GPT-6.1 Sol**，`rust-v0.161.0`（10 月 7 日）把它带到主发布线。`0.162.0`（10 月 8 日）起 TUI 还会跟随服务端的模型默认，所以实际生效的默认不发版也能变；**10 月 14 日** OpenAI 又让 GPT-5.5 从 Codex 与 ChatGPT 下线（限 ChatGPT 账号登录）。至此已经连续五个窗口没有任何被跟踪的编码 agent 在发版里换默认。如果你按默认值跑 Codex，仍然请钉死模型 id——同时要知道钉死的模型也可能被下线；这两样产品都不会替你固定住。详见 [Codex](agents/codex.md)。

## 先把地图摊开

<p align="center">
  <img src="../assets/route-map-zh.svg" alt="AI Agent 选型地图——16 条路线按五类决策分组" width="100%" />
</p>

| 路线 | 代表项目 | 常见使用者 |
| --- | --- | --- |
| 直接执行型 | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [ZCode](agents/zcode.md), [CodeBuddy](agents/codebuddy.md), [OpenCode](agents/opencode.md), [Gemini CLI](agents/gemini-cli.md), [Qwen Code](agents/qwen-code.md), [Grok Build](agents/grok-build.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | 想把明确 coding 任务交给 agent 的人（见[终端编码 CLI 对比](comparisons/coding-cli-agents.md)） |
| Agent harness 框架 | [DeepSeek Harness](agents/deepseek-harness.md), [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [TrueForge](agents/trueforge.md) | 想自己掌控 agent loop、工具表面和权限，而不是直接接受厂商成品的人——QM 和 Omnigent 把这条推到"在一层之下同时跑*多个* harness"（见 [harness 框架对比](comparisons/agent-harness-frameworks.md)） |
| 前沿 agentic 模型 | [Claude Fable 5.1](agents/claude-fable-5.md), [Claude Opus 5](agents/claude-opus-5.md), [GPT-6 Astra](agents/gpt-6-astra.md), [GPT-5.5](agents/gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 Anthropic / OpenAI 系 agent 能力上限的人——天花板（Fable 5.1、Astra）和你实际会跑的下一档是两个独立决策（Opus 5 曾是 Claude Code 的默认 Opus，9 月 22 日由 Opus 5.5 接替；9 月 28 日默认 Sonnet 也换成了 Sonnet 5.5） |
| 开放权重 agentic 模型 | [Kimi K3](agents/kimi-k3.md), [GLM-5.3](agents/glm-5.md), [DeepSeek V4](agents/deepseek-v4.md), [Qwen3-Coder](agents/qwen3-coder.md) | 想在自己托管、自己承担许可的权重上拿到前沿级能力的人——这和在几个闭源天花板之间做选择是两个不同的决策 |
| Agentic skills 框架 | [Superpowers](agents/superpowers.md), [ECC](agents/ecc.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上的人 |
| 工作流 / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md), [Orca](agents/orca.md), [Paperclip](agents/paperclip.md) | 已经认可 Claude Code 或 Codex，只想在上面补强 orchestration 的人（Ruflo 把这条进一步推到跨机器联邦和 100+ 专用 agent）；Orca 和 Paperclip 同时调度多个不同的 agent |
| 编辑器中心工作流 | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Google Antigravity](agents/antigravity.md), [TRAE](agents/trae.md), [Continue](agents/continue.md) | 想让编辑器本身保持在工作流核心的人 |
| review-first 自动化 | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md), [Open Code Review](agents/open-code-review.md) | 想把 review 和人工控制留在核心的人（CoStrict 加了企业严格流程 + 私有化部署；Open Code Review 只做评审，为 CI 里的准确率调优） |
| 管理式后台路径 | [Claude Managed Agents](agents/claude-managed-agents.md) | 需要 Anthropic 的定时、云端或后台工作流的人 |
| 消费级个人 agent | [ChatGPT dots](agents/chatgpt-dots.md), [Gemini Task](agents/gemini-task.md), [Claude（Cowork）](agents/claude-cowork.md), [Claude Duet](agents/claude-duet.md), [Muse（Meta）](agents/meta-muse.md), [Grok Bot](agents/grok-bot.md), [Cue（Manus）](agents/manus-cue.md), [豆包](agents/doubao.md), [千问 App](agents/qwen-app.md), [AutoGLM](agents/autoglm.md), [元宝](agents/yuanbao.md), [Today](agents/today-ai.md) | 想把跑腿、收件箱、预订或手机交给一个以产品形式出售、而不是自己运行的 agent 的人（见[个人 agent 对比](comparisons/personal-agents.md)） |
| 通用自主 agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md), [WorkBuddy](agents/workbuddy.md), [Kimi Work](agents/kimi-work.md) | 想要通用自主任务执行的人（ml-intern 是 ML 工程取向的特化版本；WorkBuddy 和 Kimi Work 把同一套循环对准桌面知识工作，而不是代码仓库） |
| 自建系统 | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md), [eve](agents/eve.md), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | 想自己搭 agent 平台的团队 |
| 运行时 & 工具 | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [Trail Code (Graft)](agents/graft.md), [CLI-Anything](agents/cli-anything.md), [claude-mem](agents/claude-mem.md), [Graphify](agents/graphify.md) | 需要工作流自动化、代码执行、LLM 网关、agent 上下文基础设施、agent 驱动 CLI 或可视化构建器的团队 |
| 观测与评估 | [Langfuse](agents/langfuse.md) | agent 已经跑在生产上，需要知道它做了什么、花了多少、质量有没有漂移的人（见[观测与评估](comparisons/observability-and-evals.md)） |
| 浏览器 agent | [Browser Use](agents/browser-use.md) | 任务活在一个没有 API 的网站上的人——这和"agent 怎么改文件"是两个问题，因为它决定的是允许一个 agent 以你的身份在开放互联网上做什么 |
| 自托管 / 本地 runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | 需要端侧隐私、长期运行、本地控制、渠道、设备或个人数据生活集成能力的人 |

## 当前已覆盖的主流项目

已收录 98 个项目，按形态分组。展开任意一组，或到 [agents/](agents/README.md) 浏览完整的路线表与覆盖表。

<details>
<summary><strong>编码 agent、编辑器与编排</strong>（36 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Aider](agents/aider.md) | 直接执行 | 终端优先、贴近 git 的 AI 结对编程 |
| [Claude Code](agents/claude-code.md) | 直接执行 | 本地和 IDE 优先的 coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | 管理式后台路径 | Anthropic 管理式 / 云端执行工作流映射 |
| [Codex](agents/codex.md) | 直接执行 | ChatGPT 应用内的 coding agent，支持异步云端委派 |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | 工作流层 | Claude Code 之上的 teams-first orchestration layer |
| [oh-my-codex](agents/oh-my-codex.md) | 工作流层 | 为 Codex CLI 增强工作流、teams 和持久状态 |
| [Orca](agents/orca.md) | 工作流 / orchestration layer | 开源桌面应用：把任意 CLI coding agent 放进各自的 git worktree 并排跑，带评审、浏览器、远程服务器和手机端 |
| [Cursor](agents/cursor.md) | 编辑器中心平台 | 覆盖本地编码、云端 agent 和集成的 AI 编辑器 |
| [GitHub Copilot](agents/github-copilot.md) | 平台 | VS Code + GitHub 里的多表面 agent 平台 |
| [Cline](agents/cline.md) | review-first 执行 | 编辑器内 approval-first coding agent |
| [Windsurf](agents/windsurf.md) | AI 原生 IDE | 以 Cascade 为中心的 AI IDE |
| [Google Antigravity](agents/antigravity.md) | 编辑器中心工作流 | 谷歌的 agent 优先平台：agent 桌面应用、`agy` CLI、独立 IDE 和编辑器扩展共用一套为 Gemini 调优的 harness；免费档按周封顶，闭源 |
| [TRAE](agents/trae.md) | 编辑器中心工作流 | 字节跳动的 AI IDE：VS Code 风格的 IDE 加 AI 主导的 SOLO 模式，另有跑并行、云端和定时任务的 Agent 窗口；国际版与国内版分开；不开隐私模式，对话可能被用于训练 |
| [OpenHands](agents/openhands.md) | 开源执行 | 开源 AI 软件工程 agent |
| [Devin](agents/devin.md) | 托管执行 | 端到端软件工程执行 |
| [Jules](agents/jules.md) | 托管云端执行 | GitHub 连接、PR 回收的 coding delegation |
| [Continue](agents/continue.md) | 编辑器中心 | 支持自选模型的开源 IDE 扩展 |
| [Froge Code](agents/froge-code.md) | review-first 自动化 | 当前按 Automagik Genie 暂定映射 |
| [Pi](agents/pi.md) | Agent harness 框架 | 极简终端 coding agent harness，多 LLM provider 支持 |
| [jcode](agents/jcode.md) | Agent harness 框架 | Rust 多会话 coding harness——启动最快、provider 中立 OAuth、被动语义记忆 |
| [CodeWhale](agents/codewhale.md) | 直接执行 | provider 中立的 Rust 终端 coding agent，40 多条 provider 路线，默认仍是 DeepSeek（原 DeepSeek-TUI） |
| [Kimi Code](agents/kimi-code.md) | 直接执行 | Moonshot AI 官方、Kimi 原生的终端 coding CLI（kimi-cli 继任者） |
| [MiMoCode](agents/mimocode.md) | 直接执行 | 小米官方的 MiMo 终端 coding agent，内置跨会话记忆 |
| [Grok Build](agents/grok-build.md) | 直接执行 | SpaceXAI 官方的 Rust 终端 coding agent——全屏 TUI、headless CI 模式、ACP 编辑器服务 |
| [CoStrict](agents/costrict.md) | review-first 自动化 | Cline 血统的企业 coding agent，含严格标准化流程、AI 代码评审、私有化部署 |
| [SWE-agent](agents/swe-agent.md) | Agent harness 框架 | Princeton + Stanford 的 SWE-bench 原始 harness，single-YAML 配置 |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness 框架 | SWE-agent 的 ~100 行 Python 接班版，SWE-bench Verified 仍 >74% |
| [OpenHarness](agents/openharness.md) | Agent harness 框架 | HKUDS 的 10 子系统开源 agent harness，43+ 工具、兼容 anthropics/skills、支持 MCP |
| [Omnigent](agents/omnigent.md) | Agent harness 框架 | 元 harness——在一个会话里混用 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi，带策略与云沙箱 |
| [OpenCode](agents/opencode.md) | 直接执行型 | 体量最大的厂商中立开源编码 agent，22.2 万 star（2026-10-28），MIT |
| [Gemini CLI](agents/gemini-cli.md) | 直接执行型 | 谷歌的开源终端 agent，内置搜索接地；2026-06-18 起只服务 Code Assist 标准版/企业版与付费 API key，个人用户已转到 Antigravity CLI |
| [Qwen Code](agents/qwen-code.md) | 直接执行型 | 客户端与权重都开放，可在 OpenAI/Anthropic/Gemini/本地之间运行时切换 |
| [DeepSeek Harness](agents/deepseek-harness.md) | Agent harness 框架 | 一切皆插件的 harness——连 agent 循环本身都能从配置里换掉 |
| [ZCode](agents/zcode.md) | 直接执行型 | 智谱的桌面 agentic 开发环境：长周期 "Goal" 任务，可从微信/飞书/Telegram 远程操控 |
| [CodeBuddy](agents/codebuddy.md) | 直接执行型 | 腾讯云的编程产品线（编辑器插件、CodeBuddy IDE、CodeBuddy Code CLI）：Claude Code 式循环，跨厂商模型目录，带私有云版本 |
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
<summary><strong>框架与基础设施</strong>（23 个）</summary>

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
| [Paperclip](agents/paperclip.md) | 工作流 / orchestration layer | 自托管控制平面，像管公司一样管 agent 团队：关联目标的工单、组织架构、预算、审批和定时 routine |
| [CodeGraph](agents/codegraph.md) | 运行时 & 工具 | 为 Claude Code、Cursor、Codex CLI、opencode、Hermes Agent 提供预索引的代码知识图谱 + MCP server |
| [Trail Code (Graft)](agents/graft.md) | 运行时 & 工具 | 把代码上下文写成仓库里互相链接的 markdown，一条命令接进八个以上的 agent |
| [claude-mem](agents/claude-mem.md) | 运行时 & 工具 | 外挂式跨会话记忆：hooks 采集 agent 活动、模型压缩、下次会话注入相关上下文；可选付费托管 observer |
| [Graphify](agents/graphify.md) | 运行时 & 工具 | 把代码库连同文档、PDF 和媒体变成带来源标签的知识图谱，agent 通过 skill、CLI 或本地 MCP server 查询 |
| [Browser Use](agents/browser-use.md) | 浏览器 agent | 把一个真浏览器交给 agent——打开页面、点击、输入、填表单 |
| [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | 自建系统 | AutoGen 的继任者；跨 Python、.NET、Go 的生产级多 agent 工作流 |
| [CLI-Anything](agents/cli-anything.md) | 运行时 & 工具 | 为任意软件自动生成 Click CLI，让 agent 能驱动没有 API 的应用 |

</details>

<details>
<summary><strong>模型与技能</strong>（10 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Claude Fable 5.1](agents/claude-fable-5.md) | 前沿 agentic 模型 | Anthropic 的 Mythos 级天花板——你花额度去买的那个模型，2026-09-01 刷新 |
| [Claude Opus 5](agents/claude-opus-5.md) | 前沿 agentic 模型 | 天花板一半价格的 Opus 档；9 月 22 日之前是 Claude Code 的默认 Opus，此后由 Opus 5.5 接替（9 月 28 日默认 Sonnet 也换成了 Sonnet 5.5） |
| [GPT-6 Astra](agents/gpt-6-astra.md) | 前沿 agentic 模型 | OpenAI 当前的天花板（2026-09-03），面向公众发布的是受限版本 |
| [GPT-5.5](agents/gpt-5.5.md) | 前沿 agentic 模型 | OpenAI 2026 春季的模型，作为 GPT-5.6 到 Astra 的血统参照保留 |
| [Kimi K3](agents/kimi-k3.md) | 开放权重 agentic 模型 | 首个开放的 3T 级模型——2.8T 参数、原生视觉、100 万上下文、自定义许可 |
| [GLM-5.3](agents/glm-5.md) | 开放权重 agentic 模型 | 按厂商数字最强的开放权重编码模型，Apache-2.0——且网安能力不设闸 |
| [DeepSeek V4](agents/deepseek-v4.md) | 开放权重 agentic 模型 | 1.6T 参数下的 MIT；SWE-bench Verified 80.6，且因权重开放而可复现 |
| [Qwen3-Coder](agents/qwen3-coder.md) | 开放权重 agentic 模型 | 塞得进去的那个——80B 里激活约 3B，256K→100 万上下文，跑在你所在的地方 |
| [Superpowers](agents/superpowers.md) | Agentic skills 框架 | 一整套方法论 + 可组合 skills 层，可接到 Claude Code、Codex、Cursor 等 agent 之上 |
| [ECC](agents/ecc.md) | Agentic skills 框架 | 跨 harness 插件：314 个 skill、71 个 subagent、强制 hooks、记忆库和 AgentShield 配置扫描，Claude Code 优先 |

</details>
<details>
<summary><strong>消费级个人 agent</strong>（12 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [ChatGPT dots](agents/chatgpt-dots.md) | 消费级个人 agent | OpenAI 放在 ChatGPT 里的常驻 agent——GPT-6 Astra、自己的云电脑，可在 Slack、Teams 和电话里找到；仅限 Pro，欧洲不可用 |
| [Gemini Task](agents/gemini-task.md) | 消费级个人 agent | Gemini 应用的 agent 模式（原 Spark）——在 Google Workspace 与 Chrome 里定时干活，公开列出确认清单 |
| [Claude（Cowork）](agents/claude-cowork.md) | 消费级个人 agent | Cowork 已并入 Claude 应用——任务可定时、在隔离的云端会话里持续运行，三种命名清楚的审批模式 |
| [Claude Duet](agents/claude-duet.md) | 消费级个人 agent | Anthropic 独立的主动型 agent 应用：早间简报、每隔几小时查一次你的账号、自己的虚拟机，发送、付款、签字、删除前都要你批准；美国候补名单 |
| [Muse（Meta）](agents/meta-muse.md) | 消费级个人 agent | Meta 在自家应用和 WhatsApp 里的跑腿 agent——专属云端虚拟机、一次性卡号付款，美国小范围测试，新加坡已开放 |
| [Grok Bot](agents/grok-bot.md) | 消费级个人 agent | xAI 的一组常驻 Bot，共用 Cursor 云上的一台电脑，可按计划重跑保存的技能 |
| [Cue（Manus）](agents/manus-cue.md) | 消费级个人 agent | Manus 的个人 agent 应用，每个 agent 都有自己的邮箱、电话、钱包和电脑；邀请制抢先体验 |
| [豆包](agents/doubao.md) | 消费级个人 agent | 字节跳动的助手，带工作任务模式，以及在合作手机上操作其他应用的系统级手机助手（Beta） |
| [千问 App](agents/qwen-app.md) | 消费级个人 agent | 阿里的消费级应用变成了跑腿 agent——成品交付、定时任务、外卖、酒店和政务 |
| [AutoGLM](agents/autoglm.md) | 消费级个人 agent | 智谱的手机操作 agent：一个在云手机上干活的免费应用，加上能操作你自己手机的 Apache-2.0 框架 Open-AutoGLM |
| [元宝](agents/yuanbao.md) | 消费级个人 agent | 腾讯的免费助手，Hy3 Agent 功能交付办公文件——WorkBuddy 同一模型家族的消费级那一端 |
| [Today](agents/today-ai.md) | 消费级个人 agent | 主打记忆与主动帮助的个人 AI 助理：早晚间简报、定时任务、云端电脑和 Chrome 插件；中国版数据原则上留在中国大陆，另有国际版 |

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