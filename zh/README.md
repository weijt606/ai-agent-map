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

> **最后更新：** 2026-10-21 · **快照窗口：** 2026-10-14 → 2026-10-21（自上次更新以来的增量，**7 天**，上一个窗口也是 7 天，两列原始增量连续第二周可以直接比较）· **star 数：** 更新时点抓取

项目名链接指向上游 GitHub 仓库。本仓库已写入的 profile，在"在本仓库中的状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 在本仓库中的状态 | 应该怎么读 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（=） | [mattpocock/skills](https://github.com/mattpocock/skills) | 299.2k | +8,787 | 候补（Skills 浪潮） | **连续第三个窗口守住 #1**，是它在 27 个窗口里的第 15 个 #1；增量比上期的 7 天纪录降了 26%。**距 30 万差 796**；领先 #2 共 1,673（上期：7,315）。窗口内没有发版 |
| #2&#8288;（=） | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 256.5k | +7,114 | 已收录 · [profile](agents/deepseek-harness.md) | 涨 **56%**，结束连续四次放缓，也是它有记录以来最大的 7 天增量。越过 **25 万**与 **25.5 万**，**总 star 反超 Hermes Agent**（256,509 对 255,734）。窗口内五个预发布，最后是 `rc.2`（10 月 17 日），加上了对 DeepSeek 新模型 V4.1-Flash-1017 的支持 |
| #3&#8288;（↑） | [OpenCode](https://github.com/anomalyco/opencode) | 219.4k | +6,043 | 已收录 · [profile](agents/opencode.md) | 涨 **369%**，是它此前最好成绩（09-17 的 1,920）的三倍多，也是它第一次进前三。**OpenCode 2.0** 于 10 月 12 日发布公告，Hacker News 发布帖（887 分）在 10 月 14 日；2.x 走单独分支发布，不是 GitHub Release。越过 **21.5 万** |
| #4&#8288;（新） | [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 53.4k | +4,627 | 候补（Skills 浪潮） | 涨 **373%**，09-06 以来第一次上榜，27 个窗口里的第 4 席。越过 **5 万**，总量也超过了 academic-research-skills。没有发版，原因查不到：按尖峰处理 |
| #5&#8288;（=） | [Superpowers](https://github.com/obra/superpowers) | 302.8k | +3,960 | 已收录 · [profile](agents/superpowers.md) | 涨 44%。**越过 30 万**（302,834），是本地图跟踪的仓库里继 OpenClaw 之后第二个过 30 万的 |
| #6&#8288;（新） | [CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 55.8k | +3,631 | 已收录 · [profile](agents/cli-anything.md) | 涨 **647%**，本窗口跳得最猛的一个，而它自 9 月 22 日起没有提交、6 月以来没有发版：**原因查不到**。05-23 以来第一次上榜，也是它唯一的上一次。越过 **5.5 万** |
| #7&#8288;（新） | [Ruflo](https://github.com/ruvnet/ruflo) | 78.1k | +3,445 | 已收录 · [profile](agents/ruflo.md) | 涨 **480%**，是它在本地图原始记录（自 07-16 起）里最大的增量，09-09 以来第一次上榜。窗口开始前一天（10 月 13 日）厂商发了新闻稿，窗口内发了 14 个版本。越过 **7.5 万** |
| #8&#8288;（↓） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 109.1k | +2,704 | 候补（Skills 浪潮） | 连续两次加速之后降 35%。**距 11 万差 872** |
| #9&#8288;（↓） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 255.7k | +2,105 | 已收录 · [profile](agents/hermes-agent.md) | 涨 13%，连续第二次加速。**27 个记录窗口全部在榜**；越过 **25.5 万**，但总 star 被 DeepSeek Harness 反超 |
| #10&#8288;（新） | [Claude Code](https://github.com/anthropics/claude-code) | 152.7k | +1,920 | 已收录 · [profile](agents/claude-code.md) | 涨 **80%**：它的第三席（此前是 09-24 与 10-07），也是它有记录以来第二大的 7 天增量，仅次于 09-24 的 2,108。七个版本（`v2.1.300`–`v2.1.306`），没有换默认模型 |

- 热度适合拿来发现新项目，不适合直接当选型顺序。
- **本窗口 7 天，上一个窗口也是 7 天**，两列原始增量连续第二周可以直接比较；下面不做周率换算。
- **提速的仓库比上期少，但榜首一带热得厉害。** 57 个可测仓库里 31 个加速、24 个放缓、2 个持平（上期是 55 个里 38 个加速）。前十席合计增量 **44,336**，上期 33,751，涨 31%；#10 的门槛涨了 **78%**（1,078 → 1,920）。四个仓库的增量是上期的 4.7 到 7.5 倍——[OpenCode](agents/opencode.md)、[scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)、[CLI-Anything](agents/cli-anything.md)、[Ruflo](agents/ruflo.md)——其中只有 OpenCode 有查得到的触发事件。
- **[mattpocock/skills](https://github.com/mattpocock/skills) 连续第三个窗口守住 #1**，27 个窗口里的第 15 个；+8,787 比上期的 7 天纪录降了 26%，但仍是全榜最大。它对 #2 的领先从 7,315 缩到 **1,673**，对其他三个通用集合之和的领先从 3,899 缩到 **530**。它**距 30 万差 796**，落后 [Superpowers](agents/superpowers.md) 3,630（上期 8,457）；按本窗口的速度，这个差距一周之内就会被追平。窗口内没有发版，唯一的提交是 10 月 19 日合并的一个 PR。
- **[DeepSeek Harness](agents/deepseek-harness.md) 重新加速，总 star 反超 [Hermes Agent](agents/hermes-agent.md)。** +7,114（涨 56%）结束了连续四次放缓，是它有记录以来最大的 7 天增量（周率峰值仍是 8 天的 09-17 窗口，约 8,800/周）。256,509 对 255,734，它现在是本地图跟踪的 agent 里仅次于 OpenClaw 的第二大；上期还是 Hermes 以 253,629 对 249,395 领先。窗口内五个预发布，最后是 `dsh-v0.2.1-rc.2`（10 月 17 日），在 DeepSeek 发布 V4.1-Flash-1017 的当天就加上了支持——而 DeepSeek 的发布说明点名推荐用这个 harness。两者都在涨，只是 Hermes 涨得少（+2,105，仍涨 13%）。
- **[OpenCode](agents/opencode.md) 是唯一一个有据可查的爆发：+6,043，涨 369%**，从 #8 升到 #3，是它此前最好成绩的三倍多。**OpenCode 2.0** 于 10 月 12 日发布公告，Hacker News 发布帖（887 分）在窗口第一天 10 月 14 日；已有安装用 `opencode upgrade --major`（v1.19.0 加入）升级，2.x 走单独分支发布，不是 GitHub Release。另外，**10 月 17 日** OpenCode 的 X 账号发了一条报告凭证泄露的帖子，被以"OpenCode Hacked: User credentials leaked"为题提交到 Hacker News（973 分），第二天仓库里的一个 issue 也提到"the Console breach"。本地图没能直接读到厂商声明，也不转述二手帖子里的影响范围数字——如果你用 OpenCode 托管的 Console，去看厂商公告并轮换密钥。
- **三个原因查不到的尖峰，其中两个是 infra。** [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)（涨 373%，#4）没有发版；[CLI-Anything](agents/cli-anything.md)（涨 647%，#6）自 9 月 22 日起没有提交；[Ruflo](agents/ruflo.md)（涨 480%，#7）在窗口前一天发了厂商新闻稿、窗口内发了 14 个版本，但两者都没法和增量挂上钩。CLI-Anything 与 Ruflo 让 infra 层**自 08-27 以来第一次拿到两席**，也是 09-09 以来 infra 第一次有任何席位。按本榜规矩，在第二个窗口确认之前它们都算尖峰——而 CLI-Anything 上一次在 09-30 的跳增，下一期就还回了 49%。
- **[Pi](agents/pi.md) 连续 20 个窗口在榜就此结束——这是本榜有史以来结束的最长连续在榜。** 它从 #6 掉到第 11，增量只降了 9%（+1,810），是被抬高的门槛挤出去的，不是崩了。此前结束的最长纪录是 [anthropics/skills](https://github.com/anthropics/skills) 的 15 个（09-09 结束）。还在跑的长连续有三条：Hermes Agent 27（每个记录窗口都在）、Superpowers 22、mattpocock/skills 22；其次是 DeepSeek Harness 与 OpenCode，都是 7。
- **skills 浪潮仍占十席中的四席**（#1、#4、#5、#8），但第四席换了人：K-Dense 取代 academic-research-skills，总量也反超了它。其余六席是四个 agent（#2、#3、#9、#10）和两个 infra 项目（#6、#7）。
- **模型层动的是价格和下线，不是默认模型。** (1) **Meta 的 Muse Wonder**（10 月 12 日，落在上一个窗口里，本地图当时漏了）上了 Meta Model API，**$4 / $20，缓存输入 $0.20**——和 Opus 5.5 的标价、缓存读完全一样；更大的 Muse Wonder Full 只走订阅。(2) **OpenAI 于 10 月 14 日让 GPT-5.5 从 Codex 与 ChatGPT 下线**（限 ChatGPT 账号登录），让用户改用 GPT-6.1 Sol；API 不受影响。(3) 两个开放权重发布：**Meta 的 Muse Spark Open**（10 月 15 日；816B / 激活 42B，100 万上下文，Muse Model License，"有限商用条款"）与 **DeepSeek-V4.1-Flash-1017**（10 月 17 日）。(4) Anthropic 的 **Code Review** 于 10 月 15 日对 Team 与 Enterprise 正式开放。**被跟踪的编码 agent 连续第三个窗口没有换默认模型**：[Gemini CLI](agents/gemini-cli.md) `v0.65.0` 没有改用 Gemini 4 Argon，[Codex CLI](agents/codex.md) `rust-v0.163.0` 仍是 GPT-6.1 Sol。Codex `0.162.0`（10 月 8 日）改的是默认值*怎么取*——新的 TUI 会话跟随 app server 的模型默认，除非启动时显式覆盖——这意味着 OpenAI 不发版也能改掉实际生效的默认。[成本表](comparisons/cost-and-benchmarks.md)新增 Muse Wonder 与 Muse Spark Open，按 OpenAI 价格页补上 GPT-5.5 的价格和 GPT-5.6 三档的缓存读，并把 Muse Spark 两行改名为 1.3（9 月 2 日以同样价格发布）。详见 [market-events](market-events.md)。
- **一处上期欠下的更正：** 10-14 那次刷新把 [CodeWhale](agents/codewhale.md) 的 profile 改成了 provider 中立，但本页和 [agents/README](agents/README.md) 目录行里那句"DeepSeek + MiMo"的一句话定位没改。这几行现已就地改正。
- 里程碑按原始数字核对，不看四舍五入那一列：**Superpowers 30 万**、DeepSeek Harness **25 万**与 **25.5 万**、Hermes Agent **25.5 万**、mattpocock/skills **29.5 万**、OpenCode **21.5 万**、scientific-agent-skills **5 万**、CLI-Anything **5.5 万**、Ruflo **7.5 万**、Codex CLI **13 万**、[anthropics/financial-services](https://github.com/anthropics/financial-services) **4 万**、Trail Code **1 万**（10,563）。差一点的：mattpocock/skills **距 30 万差 796**，[CrewAI](agents/crewai.md) 距 6 万差 53，[agentmemory](https://github.com/rohitg00/agentmemory) 距 3 万差 263，[Aider](agents/aider.md) 距 5 万差 319，[CodeGraph](agents/codegraph.md) 距 7.5 万差 425，OpenCode 距 22 万差 573。
- [OpenClaw](agents/openclaw.md) 仍以 392.6k star 稳居绝对第一（+705，涨 75%）；它有 profile，但不进增量榜，因为这么大的项目逐周增量噪声太大。

<details>
<summary>更多窗口笔记：skills 浪潮占比、OpenClaw、以及榜外仍在涨的项目</summary>

- `.claude/skills` 浪潮**连续第二个窗口拿下前十里的四席**：#1、#4、#5、#8。三个是通用集合；第四席现在是 [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)（K-Dense），它从 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 手里接过科研席位，总 star 也以 53,434 对 53,269 反超，成为两个科研集合里更大的那个。[mattpocock/skills](https://github.com/mattpocock/skills) 的 +8,787 比其他三个通用集合之和（Superpowers +3,960、addyosmani +2,704、anthropics/skills +1,593，合计 8,257）多 **530**——"一个目录就是整波浪潮"这个判断连续第三个窗口成立，但差距从 3,899 缩到了 530。政策不变：策展型集合按 Skills 浪潮条目跟踪，框架那一端通过 [Superpowers](agents/superpowers.md) 覆盖。
- 刚好卡在榜外：[Pi](agents/pi.md) 116.9k（+1,810）第 11，跌 9%，连续 20 个窗口在榜就此结束（见上）；[anthropics/skills](https://github.com/anthropics/skills) 182.6k（+1,593）第 12，涨 52%；[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 53.3k（+1,354）第 13、[TradingAgents](https://github.com/TauricResearch/TradingAgents) 112.5k（+1,336）第 14——**两者都在加速（+13%、+24%），却仍然丢了席位**，因为 #10 的门槛涨了 78%（1,078 → 1,920）；[Codex CLI](agents/codex.md) 130.2k（+1,089）第 15，涨 4%，越过 13 万。OpenClaw 不参与本榜，所以这几个榜外名次也按同一口径数。
- **上期的两个反转没有都扛住。** [Open Code Review](agents/open-code-review.md) 还回 **76%**（2,966 → 716），从 #4 掉到第 19，连续五个窗口在榜就此结束；现在约为 Trending 之前（约 370/周）的 2 倍。[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 放缓 35%，但仍以 #8 留在榜上。上期原因不明、涨了 150% 的 [LiteLLM](agents/litellm.md) 还回 49%（+490，第 23），[OpenHuman](agents/openhuman.md) 又腰斩一次（+234）。
- **[anthropics/financial-services](https://github.com/anthropics/financial-services) 越过 4 万**（40,597，+813，跌 9%，第 17）。[AutoGPT](agents/autogpt.md) 在上期 −116 之后回到 +123。
- 本窗口仍在涨但没进前 10（按增量，7 天原始口径）：[Pi](agents/pi.md) 116.9k（+1,810）、[anthropics/skills](https://github.com/anthropics/skills) 182.6k（+1,593）、[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 53.3k（+1,354）、[TradingAgents](https://github.com/TauricResearch/TradingAgents) 112.5k（+1,336）、[Codex CLI](agents/codex.md) 130.2k（+1,089）、[n8n](agents/n8n.md) 208.2k（+868）、[anthropics/financial-services](https://github.com/anthropics/financial-services) 40.6k（+813）、[Browser Use](agents/browser-use.md) 118.7k（+802）、[Open Code Review](agents/open-code-review.md) 47.8k（+716）、[OpenHands](agents/openhands.md) 91.5k（+594）、[Trail Code (Graft)](agents/graft.md) 10.6k（+574）、[CodeGraph](agents/codegraph.md) 74.6k（+535）、[LiteLLM](agents/litellm.md) 61.7k（+490）、[Cline](agents/cline.md) 70.7k（+402）、[LangGraph](agents/langgraph.md) 43.6k（+391）、[jcode](agents/jcode.md) 21.1k（+382）、[LangChain](agents/langchain.md) 148.2k（+354）、[agentmemory](https://github.com/rohitg00/agentmemory) 29.7k（+333）、[Langfuse](agents/langfuse.md) 36.1k（+321）、[CrewAI](agents/crewai.md) 59.9k（+270）、[ZCode](agents/zcode.md) 8.1k（+261）、[OpenHuman](agents/openhuman.md) 42.2k（+234）、[Goose](agents/goose.md) 55.5k（+204）、[mini-swe-agent](agents/mini-swe-agent.md) 8.7k（+192）、[Qwen Code](agents/qwen-code.md) 28.6k（+148）、[Omnigent](agents/omnigent.md) 10.9k（+142）、[Gemini CLI](agents/gemini-cli.md) 107.5k（+142）、[12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.8k（+139）、[Aider](agents/aider.md) 49.7k（+139）、[AutoGPT](agents/autogpt.md) 187.7k（+123）、[Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.2k（+123）、[Grok Build](agents/grok-build.md) 27.5k（+114）、[LlamaIndex](agents/llamaindex.md) 52.6k（+105）、[TrueForge](agents/trueforge.md) 6.3k（+97）、[Letta (MemGPT)](agents/memgpt.md) 25.2k（+86）、[Kimi Code](agents/kimi-code.md) 7.9k（+83）、[eve](agents/eve.md) 5.6k（+75）、[QM](agents/qm.md) 15.5k（+67）、[Continue](agents/continue.md) 36.3k（+61）、[SWE-agent](agents/swe-agent.md) 20.6k（+56）、[Open Interpreter](agents/open-interpreter.md) 68.6k（+51）、[MiMoCode](agents/mimocode.md) 13.7k（+43）、[OpenHarness](agents/openharness.md) 16.0k（+39）、[CodeWhale](agents/codewhale.md) 41.1k（+14）、[Flowise](agents/flowise.md) 55.5k（+14）、[CoStrict](agents/costrict.md) 4.5k（+3）

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

- **`.claude/skills` 浪潮仍占四席，而且大半是一个目录撑着**（2026-05 起）：curated skill 合集与 skills 框架五个月来一直占据每周热度前 10 的 2 到 6 席，席位数一直在轮换而不是不动——6/10，然后 2/10、3/10、4/10、5/10、3/10，4/10，现在仍是 **4/10**（2026-10-21）。第四席还是科研集合，但换了一个：[scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)（K-Dense）以原因不明的 +373% 取代了 academic-research-skills。核心仍是 [mattpocock/skills](https://github.com/mattpocock/skills)、[Superpowers](agents/superpowers.md) 与 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)；Superpowers 越过 **30 万**，mattpocock 距 30 万差 796。mattpocock 连续第三个窗口守住 #1，仍比其他三个通用集合之和多，但只多 530，上期是 3,899——本地图自 6 月起标记的关键人风险还在，只是没有上期那么一边倒。本仓库通过 [Superpowers](agents/superpowers.md) 覆盖框架那一端，集合则在 [skill 榜](rankings/skill-verticals.md)上跟踪。
- **模型层变成预算决策——而两家的阶梯现在每一级都有人了**：[Claude Fable 5.1](agents/claude-fable-5.md)（9 月 1 日）与 [GPT-6 Astra](agents/gpt-6-astra.md)（9 月 3 日）仍都标 **$10 / $50**；往下是 **Opus 5.5**（$4 / $20，9 月 22 日）、两个中间档 **Sonnet 5.5** 与 **GPT-6.1 Sol**（都是 $2 / $10，9 月 28–29 日，各是自家编码 agent 的默认），再往下是地板：**GPT-6 Luna**（$0.10 / $0.50，9 月 22 日）与 **Claude Haiku 5.5**（10 月 7 日，prompt 不超过 10 万 token 时 $0.10 / $0.50，超过则 $0.50 / $2.50）。Google 于 **10 月 13 日**加入了有标价的行列：**Gemini 4 Argon** 开放付费 API，$2 / $10 至 11 月 30 日，之后 $4 / $20；Meta 的 **Muse Wonder**（10 月 12 日）则落在 **$4 / $20、缓存读 $0.20**——和 Opus 5.5 一模一样，于是 $4 / $20 成了三家共用的价位。本地图此前说把两个中间档分开的那一列已经合上了：Anthropic 的价格页现在把 Sonnet 5.5 的缓存读标为 **$0.10/M**，不是从 9 月 28 日 changelog 记下的 $0.20（Claude Code `v2.1.296` 于 10 月 9 日改正了自己的数字），所以 Sonnet 5.5 与 GPT-6.1 Sol 在标价和缓存上完全相同。还能分开它们的是长上下文的计价形状（OpenAI 输入超 272k token 后对整个请求换价，Anthropic 不这样；Haiku 5.5 则按 prompt 长度分价）。见[成本 & benchmark](comparisons/cost-and-benchmarks.md)。
- **产品边界在向上坍缩**：OpenAI 把 Codex 并入 ChatGPT 应用（7 月 9 日），又在 DevDay（9 月 29 日）用可在任何设备上使用的可复用云端环境，把它进一步搬离笔记本——OpenAI 侧的"选哪个 coding agent"继续在变成"你怎么用 ChatGPT"。打包默认模型一个月里换了两次：`rust-v0.153.4`（9 月 4 日）起是 [GPT-6 Astra](agents/gpt-6-astra.md)，`rust-v0.159.1`（9 月 29 日）起是 **GPT-6.1 Sol**，`rust-v0.161.0`（10 月 7 日）把它带到主发布线。`0.162.0`（10 月 8 日）起 TUI 还会跟随服务端的模型默认，所以实际生效的默认不发版也能变；**10 月 14 日** OpenAI 又让 GPT-5.5 从 Codex 与 ChatGPT 下线（限 ChatGPT 账号登录）。至此已经连续三个窗口没有任何被跟踪的编码 agent 在发版里换默认。如果你按默认值跑 Codex，仍然请钉死模型 id——同时要知道钉死的模型也可能被下线；这两样产品都不会替你固定住。详见 [Codex](agents/codex.md)。

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
| [CodeWhale](agents/codewhale.md) | 直接执行 | provider 中立的 Rust 终端 coding agent，40 多条 provider 路线，默认仍是 DeepSeek（原 DeepSeek-TUI） |
| [Kimi Code](agents/kimi-code.md) | 直接执行 | Moonshot AI 官方、Kimi 原生的终端 coding CLI（kimi-cli 继任者） |
| [MiMoCode](agents/mimocode.md) | 直接执行 | 小米官方的 MiMo 终端 coding agent，内置跨会话记忆 |
| [Grok Build](agents/grok-build.md) | 直接执行 | SpaceXAI 官方的 Rust 终端 coding agent——全屏 TUI、headless CI 模式、ACP 编辑器服务 |
| [CoStrict](agents/costrict.md) | review-first 自动化 | Cline 血统的企业 coding agent，含严格标准化流程、AI 代码评审、私有化部署 |
| [SWE-agent](agents/swe-agent.md) | Agent harness 框架 | Princeton + Stanford 的 SWE-bench 原始 harness，single-YAML 配置 |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness 框架 | SWE-agent 的 ~100 行 Python 接班版，SWE-bench Verified 仍 >74% |
| [OpenHarness](agents/openharness.md) | Agent harness 框架 | HKUDS 的 10 子系统开源 agent harness，43+ 工具、兼容 anthropics/skills、支持 MCP |
| [Omnigent](agents/omnigent.md) | Agent harness 框架 | 元 harness——在一个会话里混用 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi，带策略与云沙箱 |
| [OpenCode](agents/opencode.md) | 直接执行型 | 体量最大的厂商中立开源编码 agent——21.9 万 star，MIT |
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