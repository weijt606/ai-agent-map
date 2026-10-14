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

> **最后更新：** 2026-10-14 · **快照窗口：** 2026-10-07 → 2026-10-14（自上次更新以来的增量，**7 天**，上一个窗口也是 7 天，两列原始增量自 09-17 以来第一次可以直接比较）· **star 数：** 更新时点抓取

项目名链接指向上游 GitHub 仓库。本仓库已写入的 profile，在"在本仓库中的状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 在本仓库中的状态 | 应该怎么读 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（=） | [mattpocock/skills](https://github.com/mattpocock/skills) | 290.4k | +11,878 | 候补（Skills 浪潮） | **守住 #1**，是它在 26 个记录窗口里的第 14 个 #1，增量涨 **83%**——是它在任何一个 7 天窗口里的最大增量（此前最高是 06-24 的 11,147）。越过 **29 万**，领先 #2 共 7,315（上期：1,626） |
| #2&#8288;（=） | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 249.4k | +4,563 | 已收录 · [profile](agents/deepseek-harness.md) | 降 6%，自 09-17 峰值以来连续第四次放缓，也是它六个可测窗口里最低的——但仍是 #1 之外唯一一个周增量过 4,000 的项目。越过 **24.5 万**。10 月 9 日的 `v0.2.1-alpha.2` 预发布没有带动增速 |
| #3&#8288;（↑） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 106.4k | +4,172 | 候补（Skills 浪潮） | 涨 **78%**，是 08-12（+4,664）以来最大的增量，连续第二次加速。越过 **10.5 万**。窗口内只有一个修 bug 的版本（0.6.13，10 月 13 日）；原因查不到 |
| #4&#8288;（↑） | [Open Code Review](https://github.com/alibaba/open-code-review) | 47.1k | +2,966 | 已收录 · [profile](agents/open-code-review.md) | 涨 **93%**，是 09-17 Trending 峰值以来第一次加速，结束了连续三次放缓。越过 **4.5 万**；现在约为上 Trending 前约 370/周的 8 倍。**v1.13.0**（10 月 13 日）加了用 ChatGPT 订阅跑评审与 ACP server，但落在窗口最后一天 |
| #5&#8288;（↓） | [Superpowers](https://github.com/obra/superpowers) | 298.9k | +2,756 | 已收录 · [profile](agents/superpowers.md) | 加速一次后降 13%。**距 30 万还差 1,126** |
| #6&#8288;（↓） | [Pi](https://github.com/earendil-works/pi) | 115.1k | +1,992 | 已收录 · [profile](agents/pi.md) | 降 25%——v1.0.0 发布窗口 56% 的跳涨还回了一部分，但增速仍高于发版前约 1,710/周的水平。越过 **11.5 万** |
| #7&#8288;（↓） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 253.6k | +1,857 | 已收录 · [profile](agents/hermes-agent.md) | 涨 8%，是自 09-06 以来连续五次放缓之后的第一次加速。**26 个记录窗口全勤**，仍是唯一一个一次都没缺席的项目 |
| #8&#8288;（↑） | [OpenCode](https://github.com/anomalyco/opencode) | 213.4k | +1,289 | 已收录 · [profile](agents/opencode.md) | 涨 9%，是它进入跟踪以来第一次加速（结束连续四次放缓）。**v1.19.0**（10 月 11 日）加了通往 OpenCode 2 的 `opencode upgrade --major`，并关掉了自动更新 |
| #9&#8288;（新） | [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 51.9k | +1,200 | 候补（Skills 浪潮） | 自 09-06 以来第一个席位——26 个窗口里的第 11 个——连续第二次加速（+47%）。另一个科研集合 K-Dense 也加速了（+40%，第 14），结束连续六次放缓 |
| #10&#8288;（新） | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 111.1k | +1,078 | 候补（金融垂直） | 自 09-17 以来第一个席位，26 个窗口里的第 14 个，增速涨 39%。它以 **10 个 star**（1,078 对 1,068）从 Claude Code 手里拿走了这个席位 |

- 热度适合拿来发现新项目，不适合直接当选型顺序。
- **本窗口 7 天，上一个窗口也是 7 天**，所以两列增量自 09-17 以来第一次可以直接比较；下面不再做周率换算。
- **全榜回暖：55 个可测仓库里 38 个加速、17 个放缓**——正好是上期 17 与 38 的倒转。前十里七个提速（上期六个）。前十席合计增量 33,751，上期 26,421，涨 28%；而 #10 的门槛几乎没动（1,084 → 1,078）。
- **[mattpocock/skills](https://github.com/mattpocock/skills) 创下它有记录以来最大的 7 天增量，+11,878**，涨 83%，连续第二个窗口守住 #1——26 个窗口里的第 14 个。它只有两个窗口的原始增量高于这个数，而且都长于 7 天（08-27 那次 15 天补更窗口，与 8 天的 07-22）；它最快的周*率*仍是 09-06 那个 5 天窗口（约 14,600/周）。它比其他三个通用集合之和（Superpowers +2,756、addyosmani +4,172、anthropics/skills +1,051，合计 7,979）多 **3,899**——上期只多 9 个 star。一个仓库拿走了前十合计增量的 35%。**原因没有任何记录**：窗口内没有发版（最近一版 v1.3.1 在 10 月 4 日，把这套 skills 以原生 Claude Code 插件的形式进了官方 marketplace），10 月 8 日围绕"一条命令安装"重写了 README，Hacker News 上没有帖子。
- **[DeepSeek Harness](agents/deepseek-harness.md) 连续第四个窗口放缓**（−6%，是它六个可测增量里最低的），与 #1 的差距从 1,626 拉大到 7,315。它仍是 #1 之外唯一一个周增量过 4,000 的项目，并越过了 24.5 万。10 月 9 日发了 `dsh-v0.2.1-alpha.2` 预发布（thought-translation 与 Git worktrees 插件、`working_directory` 工具）；在增速里完全看不到。
- **上期两个下滑的项目大幅反转。** [Open Code Review](agents/open-code-review.md) 接近翻倍（+93%）升到 #4，是 09-17 Trending 尖峰以来第一次加速，结束连续三次放缓；越过 4.5 万，现在约为上 Trending 前约 370/周的 8 倍。[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 涨 78% 到 #3，越过 10.5 万。两者都没有可查的原因：Open Code Review 的 v1.13.0（用 ChatGPT 订阅跑评审、Agent Client Protocol server）发在 10 月 13 日，窗口最后一天；addyosmani 的 0.6.13 是修 bug 的版本。
- **尖峰规矩又兑现了一次。** [OpenHuman](agents/openhuman.md)——上期约 12 倍、原因查不到的跳增——还回 **65%**（1,326 → 468），从 #8 掉到第 23，是它第二次在一个窗口内崩掉的尖峰（09-01 那次还回 84%）。[CodeGraph](agents/codegraph.md) 的 +91% 也没扛住（−30%，第 18），[CLI-Anything](agents/cli-anything.md) 连续第二个窗口下滑（−25%，第 22），回到尖峰前约 400/周附近。
- **[Claude Code](agents/claude-code.md) 以 10 个 star 丢掉席位**（1,068 对 TradingAgents 的 1,078，−1%），排第 11——但它**越过了 15 万**（150,741；上期差 327）。本窗口它发了 `v2.1.293`–`v2.1.299`：加入 Haiku 5.5 作为 API 侧默认的 Haiku 模型（10 月 7 日），`v2.1.296`（10 月 9 日）把成本统计里 Sonnet 5.5 的缓存读改为 **$0.10/M，"原为 $0.20"**——见下面模型层那条。它自己的默认模型没有变。
- **skills 浪潮从 3 席升到 4/10**（#1、#3、#5、#9）。第四席是 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)，自 09-06 以来第一个上榜的科研集合；两个科研集合本窗口都加速（K-Dense 在连续六次放缓之后 +40%），所以本榜 10-07 记下的那次"分道扬镳"又合上了。其余六席全是 agent；榜上没有基础设施项目。
- **模型层经历了 9 月 22 日以来最忙的一周，而且本地图记下的一个价格已经在它底下变了。** （1）Anthropic 于 **10 月 7 日**发布 **Claude Haiku 5.5**（`claude-haiku-5-5`）：prompt 不超过 10 万 token 时 $0.10 / $0.50，超过则 $0.50 / $2.50，缓存读 $0.01 / $0.05，1M 上下文。（2）Google 于 **10 月 13 日**把 **Gemini 4 Argon**（`gemini-4-argon`）开放到付费 API——09-30 记下的那道闸门对带防护的版本已经撤掉，无防护版本仍留在 Fairwind 计划里——价格 **$2 / $10 至 11 月 30 日，之后 $4 / $20**，缓存输入便宜 95%，不对免费层和 AI Pro 套餐开放。（3）Anthropic 的价格页现在把 **Sonnet 5.5 的缓存读标为 $0.10/M**，不是本地图从 9 月 28 日 changelog 记下的 $0.20；Claude Code `v2.1.296` 在 10 月 9 日改正了自己的数字。这抹掉了把 Sonnet 5.5 和 GPT-6.1 Sol 分开的唯一一列——两个中间档现在都是 $2 / $10 / $0.10。三件事都已进[成本 & benchmark](comparisons/cost-and-benchmarks.md)与 [market-events](market-events.md)。**连续第二个窗口没有编码 agent 换默认模型**：[Codex CLI](agents/codex.md) `rust-v0.161.0`（10 月 7 日）把 GPT-6.1 Sol 默认带到主发布线，和 `rust-v0.159.1` 在 9 月 29 日回移的是同一处改动；[Gemini CLI](agents/gemini-cli.md) `v0.64.0`（10 月 13 日）与 [OpenCode](agents/opencode.md) `v1.19.0` 都没有换。
- **两个被跟踪的仓库搬了家，本次刷新都已重新编 key。** `trailhq/Graft` 现在是 **`trailhq/Trail-Code`**——README 横幅写着"Trail-code（原 graft）"，在没有变的 `graft` CLI 前面多了一层 Trail 的"learnings"（`.trail/learnings/`、`trail check`）；[profile](agents/graft.md) 已加带日期的说明，仓库**距 1 万还差 11 个**（9,989，+340，涨 42%）。`Hmbown/CodeWhale` 在 10-07 那次抓取之前就已经变成 **`codewhale-hq/Codewhale`**，本地图上期没有注意到；它的 README 现在写"provider 中立……不隶属于任何模型厂商"、40 多条 provider 路线，所以 [CodeWhale](agents/codewhale.md) profile 里"DeepSeek + MiMo 原生"的定位已就地改正。**[ZCode](agents/zcode.md) 的第一个可测周增量是 +317**（7,804）。
- 本窗口的里程碑（按原始整数核过，不看四舍五入那一列）：mattpocock/skills 越过 **29 万**，DeepSeek Harness **24.5 万**，addyosmani/agent-skills **10.5 万**，[anthropics/skills](https://github.com/anthropics/skills) **18 万**（181,024——上期差 27），Pi **11.5 万**，Claude Code **15 万**，[Cline](agents/cline.md) **7 万**，Open Code Review **4.5 万**。三个差一点的：Superpowers **距 30 万还差 1,126**，Trail Code 距 1 万差 11，[anthropics/financial-services](https://github.com/anthropics/financial-services) 距 4 万差 216。
- [OpenClaw](agents/openclaw.md) 仍是绝对总数第一，391.9k star（+404，降 45%）；它已有 profile，但因为这种体量的项目周环比增量噪声太大，不进按增量排名的表。

<details>
<summary>更多窗口笔记：skills 浪潮占比、OpenClaw、以及榜外仍在涨的项目</summary>

- `.claude/skills` 浪潮**拿下前十里的四席**，比上期多一席：#1、#3、#5、#9。三个是通用集合；第四个 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 是自 09-30 的 financial-services 以来第一个上榜的垂直集合，也是 09-06 以来第一个科研集合。[mattpocock/skills](https://github.com/mattpocock/skills) 的 +11,878 比其他通用集合之和（Superpowers +2,756、addyosmani +4,172、anthropics/skills +1,051，合计 7,979）多 3,899——"一个目录就是整波浪潮"这个判断连续第二个窗口成立，而且这次的差距不是四舍五入误差。政策不变：策展型集合按 Skills 浪潮条目跟踪，框架那一端通过 [Superpowers](agents/superpowers.md) 覆盖。
- 刚好卡在榜外：[Claude Code](agents/claude-code.md) 150.7k（+1,068）第 11，比 #10 少 10 个 star；[anthropics/skills](https://github.com/anthropics/skills) 181.0k（+1,051）第 12，涨 7%，越过 18 万；[Codex CLI](agents/codex.md) 129.2k（+1,048）第 13，涨 14%，是连续四次放缓之后的第一次加速；[scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 48.8k（+978）第 14；[LiteLLM](agents/litellm.md) 61.2k（+956）第 15，从 +383 涨 **150%**——是本窗口增量超过 500 的仓库里百分比跳得最大的，原因未查。OpenClaw 不参与本榜，所以这几个榜外名次也按同一口径数。
- **[anthropics/financial-services](https://github.com/anthropics/financial-services) 重新加速**（+896，涨 36%，第 16），结束两个窗口的消退；9 月 21 日之后零提交、没有发版；现在约为旧基线（约 105/周）的 8.5 倍，距 4 万差 216。原因仍然查不到。
- **[AutoGPT](agents/autogpt.md) 少了 116 个 star**，是本榜唯一一个周增量为负的项目，也是原始记录里（自 07-16 起 13 次抓取）第一次出现三位数的下降；此前唯一的负数是上期 Flowise 的 −6。可能的原因包括 GitHub 清理账号，但本地图两边都没有证据。
- 本窗口仍在涨但没进前 10（按增量，7 天原始口径）：[Claude Code](agents/claude-code.md) 150.7k（+1,068）、[anthropics/skills](https://github.com/anthropics/skills) 181.0k（+1,051）、[Codex CLI](agents/codex.md) 129.2k（+1,048）、[scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 48.8k（+978）、[LiteLLM](agents/litellm.md) 61.2k（+956）、[anthropics/financial-services](https://github.com/anthropics/financial-services) 39.8k（+896）、[OpenHands](agents/openhands.md) 90.9k（+718）、[CodeGraph](agents/codegraph.md) 74.0k（+682）、[Browser Use](agents/browser-use.md) 117.9k（+604）、[Ruflo](agents/ruflo.md) 74.6k（+594）、[n8n](agents/n8n.md) 207.3k（+546）、[CLI-Anything](agents/cli-anything.md) 52.1k（+486）、[OpenHuman](agents/openhuman.md) 42.0k（+468）、[LangGraph](agents/langgraph.md) 43.2k（+442）、[jcode](agents/jcode.md) 20.7k（+376）、[Langfuse](agents/langfuse.md) 35.8k（+345）、[Trail Code (Graft)](agents/graft.md) 10.0k（+340）、[Cline](agents/cline.md) 70.3k（+334）、[ZCode](agents/zcode.md) 7.8k（+317）、[LangChain](agents/langchain.md) 147.8k（+313）、[CrewAI](agents/crewai.md) 59.7k（+270）、[Goose](agents/goose.md) 55.3k（+251）、[mini-swe-agent](agents/mini-swe-agent.md) 8.5k（+249）、[agentmemory](https://github.com/rohitg00/agentmemory) 29.4k（+211）、[Omnigent](agents/omnigent.md) 10.8k（+168）、[TrueForge](agents/trueforge.md) 6.2k（+152）、[Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.1k（+144）、[Aider](agents/aider.md) 49.5k（+138）、[Qwen Code](agents/qwen-code.md) 28.5k（+136）、[Grok Build](agents/grok-build.md) 27.4k（+118）、[Gemini CLI](agents/gemini-cli.md) 107.3k（+101）、[12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.7k（+99）、[Kimi Code](agents/kimi-code.md) 7.9k（+81）、[eve](agents/eve.md) 5.6k（+80）、[Continue](agents/continue.md) 36.2k（+76）、[Letta (MemGPT)](agents/memgpt.md) 25.1k（+65）、[OpenHarness](agents/openharness.md) 16.0k（+64）、[LlamaIndex](agents/llamaindex.md) 52.5k（+62）、[Open Interpreter](agents/open-interpreter.md) 68.6k（+54）、[SWE-agent](agents/swe-agent.md) 20.5k（+53）、[MiMoCode](agents/mimocode.md) 13.7k（+52）、[QM](agents/qm.md) 15.4k（+51）、[CodeWhale](agents/codewhale.md) 41.1k（+18）、[Flowise](agents/flowise.md) 55.5k（+11）、[CoStrict](agents/costrict.md) 4.4k（+3）

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
- **[记忆方案对比](comparisons/memory-approaches.md)** —— "有记忆"这句话背后的七种不同含义，从自编辑存储到被动语义召回，以及你要持久化什么就该选哪种。
- **[观测与评估](comparisons/observability-and-evals.md)** —— 上面这一切之下的那一层：agent 一旦无人值守地跑起来，故障就不再长得像崩溃，而是长得像静默的质量漂移。对比 [Langfuse](agents/langfuse.md)、Opik、Phoenix、Helicone、LangSmith 等——并理清这个领域里"开源"的四种不同含义。

## 市场脉搏

当下影响选型的三条结构性主线——完整的日期与来源档案见[市场事件](market-events.md)：

- **`.claude/skills` 浪潮回到四席，而且大半是一个目录撑着**（2026-05 起）：curated skill 合集与 skills 框架五个月来一直占据每周热度前 10 的 2 到 6 席，席位数一直在轮换而不是不动——6/10，然后 2/10、3/10、4/10、5/10、3/10，现在是 **4/10**（2026-10-14）。第四席是一个科研集合 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)，自 09-06 以来第一次回来；核心仍是 [mattpocock/skills](https://github.com/mattpocock/skills)、[Superpowers](agents/superpowers.md) 与 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)。mattpocock 创下它有记录以来最大的 7 天增量（+11,878），比其他三个通用集合之和多 3,899——上期只多 9 个 star——所以本地图自 6 月起就在标记的关键人风险又完整地回来了。本仓库通过 [Superpowers](agents/superpowers.md) 覆盖框架那一端，集合则在 [skill 榜](rankings/skill-verticals.md)上跟踪。
- **模型层变成预算决策——而两家的阶梯现在每一级都有人了**：[Claude Fable 5.1](agents/claude-fable-5.md)（9 月 1 日）与 [GPT-6 Astra](agents/gpt-6-astra.md)（9 月 3 日）仍都标 **$10 / $50**；往下是 **Opus 5.5**（$4 / $20，9 月 22 日）、两个中间档 **Sonnet 5.5** 与 **GPT-6.1 Sol**（都是 $2 / $10，9 月 28–29 日，各是自家编码 agent 的默认），再往下是地板：**GPT-6 Luna**（$0.10 / $0.50，9 月 22 日）与 **Claude Haiku 5.5**（10 月 7 日，prompt 不超过 10 万 token 时 $0.10 / $0.50，超过则 $0.50 / $2.50）。Google 于 **10 月 13 日**加入了有标价的行列：**Gemini 4 Argon** 开放付费 API，$2 / $10 至 11 月 30 日，之后 $4 / $20。本地图此前说把两个中间档分开的那一列已经合上了：Anthropic 的价格页现在把 Sonnet 5.5 的缓存读标为 **$0.10/M**，不是从 9 月 28 日 changelog 记下的 $0.20（Claude Code `v2.1.296` 于 10 月 9 日改正了自己的数字），所以 Sonnet 5.5 与 GPT-6.1 Sol 在标价和缓存上完全相同。还能分开它们的是长上下文的计价形状（OpenAI 输入超 272k token 后对整个请求换价，Anthropic 不这样；Haiku 5.5 则按 prompt 长度分价）。见[成本 & benchmark](comparisons/cost-and-benchmarks.md)。
- **产品边界在向上坍缩**：OpenAI 把 Codex 并入 ChatGPT 应用（7 月 9 日），又在 DevDay（9 月 29 日）用可在任何设备上使用的可复用云端环境，把它进一步搬离笔记本——OpenAI 侧的"选哪个 coding agent"继续在变成"你怎么用 ChatGPT"。打包默认模型一个月里换了两次：`rust-v0.153.4`（9 月 4 日）起是 [GPT-6 Astra](agents/gpt-6-astra.md)，`rust-v0.159.1`（9 月 29 日）起是 **GPT-6.1 Sol**，`rust-v0.161.0`（10 月 7 日）把它带到主发布线。至此已经连续两个窗口没有任何被跟踪的编码 agent 换默认。如果你按默认值跑 Codex，仍然请钉死模型 id；产品不会替你把它固定住。详见 [Codex](agents/codex.md)。

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
| 运行时 & 工具 | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [Trail Code (Graft)](agents/graft.md), [CLI-Anything](agents/cli-anything.md) | 需要工作流自动化、代码执行、LLM 网关、agent 上下文基础设施、agent 驱动 CLI 或可视化构建器的团队 |
| 观测与评估 | [Langfuse](agents/langfuse.md) | agent 已经跑在生产上，需要知道它做了什么、花了多少、质量有没有漂移的人（见[观测与评估](comparisons/observability-and-evals.md)） |
| 浏览器 agent | [Browser Use](agents/browser-use.md) | 任务活在一个没有 API 的网站上的人——这和"agent 怎么改文件"是两个问题，因为它决定的是允许一个 agent 以你的身份在开放互联网上做什么 |
| 自托管 / 本地 runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | 需要端侧隐私、长期运行、本地控制、渠道、设备或个人数据生活集成能力的人 |

## 当前已覆盖的主流项目

已收录 78 个项目，按形态分组。展开任意一组，或到 [agents/](agents/README.md) 浏览完整的路线表与覆盖表。

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
<summary><strong>框架与基础设施</strong>（20 个）</summary>

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
| [Trail Code (Graft)](agents/graft.md) | 运行时 & 工具 | 把代码上下文写成仓库里互相链接的 markdown，一条命令接进八个以上的 agent |
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