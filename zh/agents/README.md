# Agents

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](README.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/README.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这里不是“agent 名单墙”。

这里更像 shortlist：先帮你看懂路线，再决定要不要点进具体页面。

## 先按路线找

| 路线 | 代表项目 | 适合谁 |
| --- | --- | --- |
| 直接执行 | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md), [CodeWhale](codewhale.md), [Grok Build](grok-build.md), [Devin](devin.md), [Jules](jules.md) | 想直接把 coding 任务交给 agent（在[终端编码 CLI agent](../comparisons/coding-cli-agents.md) 里对比） |
| Agent harness 框架 | [Pi](pi.md), [jcode](jcode.md), [OpenHands](openhands.md), [SWE-agent](swe-agent.md), [mini-swe-agent](mini-swe-agent.md), [OpenHarness](openharness.md), [QM](qm.md), [Omnigent](omnigent.md), [TrueForge](trueforge.md) | 想自己掌控 loop、工具表面和权限，不直接接受厂商成品（QM 和 Omnigent 在一层之下同时跑多个 harness） |
| 前沿 agentic 模型 | [Claude Fable 5](claude-fable-5.md)、[GPT-5.5](gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 Anthropic / OpenAI 系 agent 能力上限 |
| Agentic skills 框架 | [Superpowers](superpowers.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上 |
| 工作流 / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md), [Ruflo](ruflo.md) | 已经在用 Claude Code 或 Codex，只想补强 teams、skills 和持久工作流（Ruflo 进一步推到跨机器联邦） |
| 编辑器中心工作流 | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | 想让编辑器本身成为 agent 主表面 |
| review-first 自动化 | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md), [CoStrict](costrict.md), [Open Code Review](open-code-review.md) | 想把 review 和人工节奏留在核心（CoStrict 瞄准企业严格流程 + 私有化部署；Open Code Review 只做评审，为 CI 里的准确率调优） |
| 通用自主 agent | [AutoGPT](autogpt.md), [Agent Zero](agent-zero.md), [BabyAGI](babyagi.md), [Julep](julep.md), [GenericAgent](generic-agent.md), [ml-intern](ml-intern.md) | 想要通用自主任务执行（ml-intern 是 ML 工程取向的特化版） |
| 自建平台 | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md), [Haystack](haystack.md), [Semantic Kernel](semantic-kernel.md), [DSPy](dspy.md), [Pydantic AI](pydantic-ai.md), [eve](eve.md) | 想自己搭 agent system（eve 是其中唯一自带渠道、定时、沙箱与审批闸门的） |
| 运行时 & 工具 | [n8n](n8n.md), [MemGPT](memgpt.md), [Open Interpreter](open-interpreter.md), [LiteLLM](litellm.md), [Flowise](flowise.md), [CodeGraph](codegraph.md), [CLI-Anything](cli-anything.md) | 需要工作流自动化、代码执行、LLM 网关、agent 上下文基础设施、agent 驱动 CLI 或可视化构建器 |
| 自托管 / 本地 runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md), [Mercury Agent](mercury-agent.md), [OpenHuman](openhuman.md) | 需要端侧隐私、本地控制、扩展、渠道、runtime ownership 或个人数据生活集成 |
| 管理式后台路径 | [Claude Managed Agents](claude-managed-agents.md) | 需要云端、定时、后台执行 |

## 近期热门快照

这不是质量排行榜。

它只是把最近一周 GitHub 快照里特别热的 agent 项目摆出来。顺序按 7 天增量；下面的 star 总数是这次更新目录时重新核对过的当前值。

> **最后更新：** 2026-09-01 · **快照窗口：** 2026-08-27 → 2026-09-01（自上次更新以来的增量，**5 天**——上一次是 8 月 27 日补跑的补更，所以本窗口提前收；估算） · **Star 总数：** 更新时实时核对

项目名链接指向上游 GitHub 仓库。本目录已收录的 profile，在"目录状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 目录状态 | 备注 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（新） | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 41.5k | +6,750 | 候补（Skills 浪潮 · 科研） | 从榜外直接进 #1，**周率跳增 14 倍**——本榜记录以来最大的一次 |
| #2&#8288;（↓） | [mattpocock/skills](https://github.com/mattpocock/skills) | 243.9k | +5,954 | 候补（Skills 浪潮） | **连续九个窗口的 #1 结束**（上一期写成第十个），周率降 24%——越过 243k |
| #3&#8288;（=） | [Pi](https://github.com/earendil-works/pi) | 100.5k | +2,707 | [Profile](pi.md) | **破 10 万**；周率降温 16%，守住 #3 |
| #4&#8288;（=） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 239.5k | +2,595 | [Profile](hermes-agent.md) | 连续第二个窗口持平（+2%）——离 24 万只差约 530 个 star |
| #5&#8288;（=） | [Superpowers](https://github.com/obra/superpowers) | 280.4k | +2,308 | [Profile](superpowers.md) | **越过 280k**，周率持平（−3%）——本榜最稳的一条线 |
| #6&#8288;（↓） | [Codex CLI](https://github.com/openai/codex) | 120.7k | +1,915 | [Profile](codex.md) | 还回 **57% 的周率**，退四位——那波降价拉升是尖峰；越过 120k |
| #7&#8288;（↑） | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 102.2k | +1,455 | 不收录（金融研究垂直） | 周率涨 45% 升一位——连续第三个窗口、累计第十一次，纯靠增量 |
| #8&#8288;（↓） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 91.4k | +1,418 | 候补（Skills 浪潮） | 名次退两位，但周率**涨 17%**——越过 91k |
| #9&#8288;（↓） | [anthropics/skills](https://github.com/anthropics/skills) | 173.0k | +1,173 | 候补（Skills 浪潮源头） | 连续第二个窗口持平（+2%）——距 173k 还差 10 个 star |
| #10&#8288;（新） | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 39.3k | +1,111 | [Profile](openhuman.md) | 拿下上窗口差 259 个 star 错过的位置——这是它第一次上榜，周率热 70% |

历史名次变化的趋势图见 [rankings/](../rankings/README.md)，那里还有按 star 总量排序的分类榜与垂类榜。

**市场事件：**
- **2026-08-27 → 09-01（5 天窗口）—— 科研垂直拿下 #1；连续三个尖峰都没扛住** —— 上一次例更是 8 月 27 日补跑的补更，所以本窗口是 **5 天**，每个原始增量约为正常窗口的 0.71 倍；下面的比较一律按周率讲。**[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 从榜外直接冲到 #1**，+6,750，**周率跳增 14 倍**（约 9,450 对约 670），是本榜记录以来最大的一次——它是 165 个经过验证的 skill 加 100+ 个覆盖生物、化学、医学与药物发现的科学数据库。它不是一个人在动：[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 排在 #11，周率涨 67%；同一窗口内 Anthropic 于 8 月 27 日预览了 **[Model Hardware Standard](../market-events.md)**，一套让 agent 驱动显微镜、移液工作站、机械臂与激光器的开放接口，与 HHMI 共同开发。本地图只记录这个时间上的重合，不断言因果，并且把自己定的规矩用上：**单个窗口在第二个窗口确认之前只是尖峰。** 这条规矩当场就在别处兑现了——**[Codex CLI](codex.md) 还回 57% 的周率**，从 #2 掉到 #6，上窗口那个"本榜记录以来最大的重新加速"只买到一个窗口，没买到基准线；连续三个窗口，三个尖峰全没扛住（jcode、addyosmani、Codex）。**[mattpocock/skills](https://github.com/mattpocock/skills) 在 #1 上连坐九个窗口之后结束**（2026-06-24 → 2026-08-27），是被明确超过，而且自己的周率降了 24%（243.9k）；上一期把最后那次写成"第十个"连续窗口，多算了一个。**[Pi](pi.md) 破 10 万**，[Superpowers](superpowers.md) 越过 280k，[Codex CLI](codex.md) 越过 120k。skills 浪潮从 **4/10 到 5/10**，这是 2026-07-14 以来第一个五席窗口。要分清什么是新的：科研垂直集合从 5 月起就断续占过前十席位，所以新的不是"垂直上榜"，而是这次由一个垂直集合**领跑**，#11 还跟着第二个。榜单整体重新加速（47 个里 27 个周率变高），逆转上窗口的普遍降温。新收录决策：**新增一个 profile —— [TrueForge](trueforge.md)**（`truefoundry/trueforge`，MIT，TypeScript，5.0k，348 fork），[harness 路线](../comparisons/agent-harness-frameworks.md)上的第三种形态：不是你 fork 下来的循环，也不是驱动其他循环的 meta-harness，而是一个你部署起来、用 HTTP 调用的 harness。候补：[trailhq/Graft](https://github.com/trailhq/Graft)（5.4k，MIT，因与 [CodeGraph](codegraph.md) 重叠而按住）、[video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)（7.0k）、[Fuxi](https://github.com/fuxicodex/Fuxi)（3.2k，仍是 `NOASSERTION`）、[Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins)（2.8k）、[sepia](https://github.com/Nanako0129/sepia)（四天 1.4k）。榜外的厂商层动了两次：**Meta 于 8 月 31 日把 [Muse Code](../market-events.md) 转正**，配三档订阅，外加一个用你的 prompt 与 completion 换约 21 倍便宜输出价的 contributor 档；以及 **[Gambit Security 记录到勒索软件团伙用 Cursor Agent](../market-events.md)** 在十家机构内部做实操入侵。细节见 [market-events](../market-events.md)。
- **2026-08-12 → 08-27（补更窗口，漏了两次例更）—— 一次降价挪动了整张榜；eve 补漏收录** —— 8 月 19 日和 8 月 26 日两次例更没有跑，因此本窗口是 **15 天**，所有原始增量约为正常窗口的 2.1 倍；下面的对比一律按周率讲。**[Codex CLI](codex.md) 从 #9 冲到 #2**，+13,321，**周率跳增 4.5 倍**，是本榜记录以来最大的一次重新加速——推动它的不是发布而是价格：OpenAI 于 **8 月 21 日把 GPT-5.6 Sol 从 $5/$30 降到 $4/$20 每百万 token**，为期三个月，覆盖 Codex credits 与符合条件的 ChatGPT Work 计划，同日宣布 **Codex 活跃用户 2000 万**。[mattpocock/skills](https://github.com/mattpocock/skills) 拿下连续第十个 #1、越过 **237k**，并重新加速（+7%），推翻了上窗口标注的减速。**本榜最近两次判断都没站住**：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 那个"记录以来最猛的重新加速"还回 64% 的周率、掉到 #6；[AutoGPT](autogpt.md) 那个"9 倍苏醒"降 77%——单个 4–5 倍窗口在第二个窗口确认之前只算尖峰。[TradingAgents](https://github.com/TauricResearch/TradingAgents) **破 10 万**，仍不收录。榜单中下段普遍降温：[QM](qm.md) −71%、[Open Code Review](open-code-review.md) −53%、[jcode](jcode.md) −50%；相反方向上 [Pi](pi.md)、[n8n](n8n.md)（回到 #10）、[Claude Code](claude-code.md)、[Grok Build](grok-build.md) 都在变好。新收录决策：**新增一个 profile —— [eve](eve.md)**（`vercel/eve`，Apache-2.0，4.8k），补漏收录 Vercel 于 2026 年 6 月 17 日在 Ship London 作为 Agent Stack 一部分发布的文件系统优先 agent 框架；它是"自建"路线上第一个真正带交付面的条目，也是唯一一个生产路径写死在某一家平台上的条目。候补：[truefoundry/trueforge](https://github.com/truefoundry/trueforge)（4.6k，MIT）、[trailhq/Graft](https://github.com/trailhq/Graft)（4.9k，MIT）、[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)（三周 2.1k，卡在 license 不明）。Skills 浪潮维持 4/10 且成员未轮换，但在集中——mattpocock 的增量已超过另外三个之和。详见 [market-events](../market-events.md)。
- **2026-08-05 → 08-12 —— curated skills 那一端重新加速；jcode 反转；本窗口不新增收录** —— [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 从 +945、掉在榜外，直接变成 **+4,664、站上 #2**，4.9 倍的跳增，是本榜记录以来最猛的单窗口重新加速；两个体量最大的 curated `.claude/skills` 目录第一次同时占据增量榜前两席。[mattpocock/skills](https://github.com/mattpocock/skills) 拿下连续第八个 #1、越过 **214k**，但也是三个窗口以来第一次减速（−8%）。上周冻结的前六名裂开了：[Pi](pi.md)、[Superpowers](superpowers.md)、[Hermes Agent](hermes-agent.md) 在增量基本持平的情况下各退一位，[Codex CLI](codex.md) 退三位。**[jcode](jcode.md) 剧烈反转**——上窗口涨得最猛的那个（+3,163）本周降 59% 到 +1,284，从 #5 直接掉出榜单，这更像发布曲线在走平而不是新的基线。[TradingAgents](https://github.com/TauricResearch/TradingAgents) 交出有记录以来最大的窗口（+2,050，2.6 倍），进到 #6 但依然不收录。**[QM](qm.md) 的第一个完整窗口印证了上周的收录**（+1,756，约自身体量的 15%，进到 #8），[Open Code Review](open-code-review.md)（+1,246）、[Omnigent](omnigent.md)（+507）、[Langfuse](langfuse.md)（+390）也都交出了首个增量。[n8n](n8n.md) 在同一个窗口里破了 **20 万**、又丢了席位。新收录决策：**不新增 profile**——扫描里没有达到收录门槛的项目；[QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins)（2.1k，让任意 harness 原生支持多模态）和 [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST)（5.5k，攻防安全元 harness）加入候补。Skills 浪潮维持 4/10，但成员轮换。榜单之外动的是厂商层：**Meta 于 8 月 5 日发布 Muse Code（beta）与 Muse Spark 1.2**——补上一方 coding CLI 阵营的最后一块，但没有公开仓库，因此本地图不跟踪它；**Claude Code 自托管环境**于 8 月 6 日进入公开 beta；**GPT-5.6-Cyber** 于 8 月 10 日发布，需 Daybreak 审批。详见 [market-events](../market-events.md)。
- **2026-07-29 → 08-05 —— QM 以 Y Combinator 的量级首发；榜单重新加速；mattpocock 破 20 万** —— `yc-software/qm`，一个跑在 Slack 和 web 上的**多人协作 agent harness**，头七天拿到约 11.4k star、1.3k fork。新收录决策：**新增三个 profile** —— **[QM](qm.md)**（MIT，TypeScript；按人和按房间分作用域的状态，跑在 harness 无关的 core 上；贡献只收文字提案不收代码）、**[Omnigent](omnigent.md)**（`omnigent-ai/omnigent`，Apache-2.0，8.1k——同一个元 harness 思路但面向单个开发者，自标 alpha）、**[Open Code Review](open-code-review.md)**（`alibaba/open-code-review`，Apache-2.0，19.0k——补漏；阿里跑了两年的内部评审助手，用召回换准确）。榜单上，上窗口的"全面降温"在 7 天对 7 天的干净对比下反转了：前 10 大部分增量回升，[mattpocock/skills](https://github.com/mattpocock/skills) 拿下连续第七个 #1 并冲破 **20 万**，而且 **#1 到 #6 一位没动**。[jcode](jcode.md) 一周长出自身体量的四分之一（+3.2k 到 16.0k）。[Grok Build](grok-build.md) 交出第一个可比增量，**差 24 个 star 没进榜**（+940）——发布尖峰过后的急剧减速。随着 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 回归，Skills 浪潮重新扩面到 4/10。[Langfuse](langfuse.md) 本窗口纳入跟踪，32.6k。
- **2026-07-22 → 07-29 —— Grok Build 登场；榜单全面降温** —— xAI/SpaceXAI 发布 **[Grok Build](grok-build.md)**，厂商官方的 Rust 终端 coding agent，**15 天拿到 23.2k star、4.4k fork**——本地图记录过的最响亮首秀。新收录决策：**Grok Build 作为已收录 profile 加入** coding CLI 路线；注意它的治理——Apache-2.0，但仓库是 monorepo 的周期性导出，且**不接受外部贡献**。因窗口开始时尚未纳入跟踪，本周暂无排名。榜单上前 10 的增量全线回落（部分原因是本窗口 7 天、上次约 8 天）：[mattpocock/skills](https://github.com/mattpocock/skills) 拿下连续第六个 #1 但已离开新高（+11.0k），[Superpowers](superpowers.md) 退到 #3，[Codex CLI](codex.md) 腰斩到 #6，而 [Pi](pi.md) 升到 #2、[jcode](jcode.md) 升到 #5。[n8n](n8n.md) 以 8 个 star 之差从 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 手里拿下 #10，后者掉出榜单。Skills 浪潮连续第三次收窄，到 3/10。
- **2026-07-14 → 07-22 —— jcode 转正写入 profile；mattpocock 暴涨、addyosmani 崩盘** —— [mattpocock/skills](https://github.com/mattpocock/skills) 连续第五次登顶且涨幅创新高（+13.6k，越过 181k），上窗口的 #2 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 增量近乎腰斩、跌到 #9。两个已收录新面孔进入增量榜：**[jcode](jcode.md)** 在 #7、[Kimi Code](kimi-code.md) 在 #10。新收录决策：**[jcode](jcode.md)（`1jehuang/jcode`，Rust，10.6k）自 5 月起持续上涨，本窗口从候补转正为完整 profile**，归入 [agent harness 框架](../comparisons/agent-harness-frameworks.md) 路线。[Codex CLI](codex.md) 越过 10 万。Skills 浪潮收窄到 4/10，[academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 和 [TradingAgents](https://github.com/TauricResearch/TradingAgents) 掉出榜单。
- **2026-07-09 —— Codex 并入 ChatGPT；GPT-5.6 发布** —— OpenAI 把独立 Codex 应用并入 ChatGPT 桌面应用（Codex 成为与 Chat 和新 agentic 模式 ChatGPT Work 并列的入口，全计划含免费版可用），同日 GPT-5.6（Sol/Terra/Luna 三档）在 ChatGPT、Codex 和 API 接棒 GPT-5.5。详见[市场事件](../market-events.md)、[Codex](codex.md)、[GPT-5.5](gpt-5.5.md)。
- **2026-06-09 → 07-07 —— Claude 5 家族登场，一波三折** —— Anthropic 发布 [Claude Fable 5](claude-fable-5.md)，首个 Mythos 级模型（位于 Opus 之上的新等级），成为 Claude Code 默认模型；6 月 12 日因短暂出口管制全球下架，7 月 1 日在更严格安全分类器后恢复（回退 Opus 4.8），7 月 7 日改按额度计费。Opus 4.8 本身 5 月 28 日已发布。详见[市场事件](../market-events.md)。
- **2026 年 7 月 8–14 —— curated skills 轮换、仍无黑马** —— [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 上升一位到 #2（+5.1k，越过 77k），反超滑到 #3 的 [Superpowers](superpowers.md)（越过 253k）。[mattpocock/skills](https://github.com/mattpocock/skills) 连续第四个窗口守住 #1 增量位（+7.7k，越过 168k）。下方唯一真正的重排是 [Pi](pi.md) 跳升两位到 #5、[Codex CLI](codex.md) 跳升两位到 #7，把 [anthropics/skills](https://github.com/anthropics/skills) 和 [codegraph](codegraph.md) 挤下去；[TradingAgents](https://github.com/TauricResearch/TradingAgents) 下滑到 #9。Skills 浪潮仍 5/10。本周新收录扫描没有新的达到收录门槛的 agent 表面；最新且体量最大的新仓库——[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)（7.3k，"loop engineering" 的模式与 CLI 工具集）和 [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)（2.8k，AI 原生的 markdown wiki 编辑器）——加入候补。
- **2026 年 7 月 2–8 —— curated skills 轮换、仍无黑马** —— [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 是本窗口涨幅最大的项目（+4.3k），从 #6 上升三位到 #3，把 curated 那一端重新炒热。[mattpocock/skills](https://github.com/mattpocock/skills) 连续第三个窗口守住 #1 增量位（+6.6k，越过 160k），而 [Hermes Agent](hermes-agent.md) 和 [anthropics/skills](https://github.com/anthropics/skills) 各降温一位。Skills 浪潮仍 5/10；[TradingAgents](https://github.com/TauricResearch/TradingAgents) 下滑到 #8。本周新收录扫描没有新的达到收录门槛的 agent 表面；最新且体量最大的新仓库——[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)（9.6k，一个替 agent 写并维护文档的 CLI）和 [vercel/eve](https://github.com/vercel/eve)（3.3k，Vercel 的 agent 构建框架）——加入候补。
- **2026 年 6 月 24 – 7 月 2 —— 榜首冻结** —— 本窗口没有黑马：[mattpocock/skills](https://github.com/mattpocock/skills) 连续第二个窗口守住 #1 增量位（+9.3k，越过 153k），[Superpowers](superpowers.md) 与 [Hermes Agent](hermes-agent.md) 稳守 #2/#3。Skills 浪潮内部（仍 5/10）：[anthropics/skills](https://github.com/anthropics/skills) 升到 #4，[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 降到 #6；[TradingAgents](https://github.com/TauricResearch/TradingAgents) 以更高的 #7 重回表内。本周新收录扫描没有新的达到收录门槛的 agent 表面；最新的候补——[tigicion/dao-code](https://github.com/tigicion/dao-code)（1.2k，DeepSeek-V4 终端 coding CLI）和 [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)（2.2k，把 Claude Design 打包成 Agent Skill）——加入候补。
- **2026 年 6 月 17–24 —— Skills 浪潮榜首轮换、MiMoCode 降温** —— [mattpocock/skills](https://github.com/mattpocock/skills) 拿到本窗口最大涨幅（+11.1k，越过 144k）夺回 #1 增量位，而上周的黑马 [MiMoCode](mimocode.md) 只涨了约 1.0k（9.6k → 10.6k），跌出增量前 10。[Codex CLI](codex.md) 以 #9 重回表内，[Hermes Agent](hermes-agent.md) 突破 200k。本周新收录扫描没有新的达到收录门槛的 agent 表面；最大的几个新仓库（[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) 4.0k、[ruvnet/agent-harness-generator](https://github.com/ruvnet/agent-harness-generator) 0.3k）留在候补。
- **2026 年 5 月底 —— 更名** —— 本目录以 DeepSeek-TUI 收录的 agent 已改名为 [CodeWhale](codewhale.md)（`Hmbown/CodeWhale`，现 36.6k），并从只支持 DeepSeek 扩展到 **DeepSeek + MiMo**。旧的 `DeepSeek-TUI` 链接会重定向；本目录已统一改用新名。
- **2026 年 5 月底 —— 代码上下文黑马** —— [codegraph](codegraph.md) 单窗口翻倍多（16.4k → 37.5k），是目前最清晰的信号：「agent 上下文基础设施」正在成为独立需求中心。全新的 harness 框架 [jcode](https://github.com/1jehuang/jcode)（1jehuang，Rust，6.8k）加入候补，与 [SWE-agent](swe-agent.md) / [mini-swe-agent](mini-swe-agent.md) 和 [OpenHarness](openharness.md) 并列。
- **2026 年 5 月（降温）** —— `.claude/skills` 浪潮仍在继续，但从前 10 占 6 个收窄到 4 个（[mattpocock/skills](https://github.com/mattpocock/skills)、[Superpowers](superpowers.md)、[academic-research-skills](https://github.com/Imbad0202/academic-research-skills)、[anthropics/skills](https://github.com/anthropics/skills)），因为代码上下文和 harness 基础设施抢走了更多热度。Anthropic 自家的 [skills](https://github.com/anthropics/skills) 仍是整套范式的锚点。
- **2026-04-08** —— Earendil（Armin Ronacher 的公司）从 Mario Zechner 手中收购 [Pi](pi.md) 项目，仓库从 `badlogic/pi-mono` 迁到 `earendil-works/pi`；Earendil 同时启动云端 agent 平台 Lefos。
- **2026-04-16** —— OpenAI 推出 "Codex for (almost) everything"，在 [Codex](codex.md) 产品表面加入后台 Computer Use、并行多 agent 执行、内置浏览器，以及 90+ plugin。同时披露周活 300 万开发者，约为 3 月初的 2 倍。
- **2026-04-23** —— OpenAI 发布 [GPT-5.5](gpt-5.5.md)，是 Codex、ChatGPT 和所有基于 OpenAI API 的 agent 的底层模型。

## 当前已收录

| 项目 | 分类 | 开源 | 一句话定位 | 状态 |
| --- | --- | --- | --- | --- |
| [Aider](aider.md) | execution | 是 | 终端优先、带强 git loop 的 AI 结对编程 | 已核验 |
| [Claude Code](claude-code.md) | execution | 否 | 本地和 IDE 优先的 coding agent | 已核验 |
| [Claude Managed Agents](claude-managed-agents.md) | automation | 否 | Anthropic 管理式 / 云端执行工作流映射 | 已注明映射关系 |
| [Codex](codex.md) | execution | 否 | ChatGPT 内的云端软件工程 agent | 已按当前产品边界核验 |
| [oh-my-claudecode](oh-my-claudecode.md) | multi-agent | 是 | Claude Code 之上的工作流和 orchestration layer | 已核验，附带包名说明 |
| [oh-my-codex](oh-my-codex.md) | multi-agent | 是 | Codex CLI 之上的工作流和 orchestration layer | 已核验 |
| [Cursor](cursor.md) | platform | 否 | 覆盖本地编码、集成和后台 agent 的 AI 编辑器 | 已核验 |
| [GitHub Copilot](github-copilot.md) | platform | 否 | VS Code / GitHub 里的多表面 agent 平台 | 已核验 |
| [Cline](cline.md) | execution | 是 | approval-first 编辑器内 coding agent | 已核验 |
| [Windsurf](windsurf.md) | platform | 否 | 以 Cascade 为中心的 AI 原生 IDE | 已核验 |
| [OpenHands](openhands.md) | execution | 是 | 开源 AI 软件工程 agent | 已核验 |
| [Devin](devin.md) | execution | 否 | 托管式端到端软件工程执行 | 已核验 |
| [Jules](jules.md) | automation | 否 | Google 托管、带 GitHub 和 PR 流程的云端 coding agent | 已按当前文档核验 |
| [AI Edge Gallery](ai-edge-gallery.md) | platform | 是 | 带 agent skills 和 mobile actions 的端侧本地 assistant 沙盒 | 已核验，附带范围说明 |
| [Goose](goose.md) | platform | 是 | 跨 desktop、CLI 和 API 的可扩展本地 agent | 已核验 |
| [Hermes Agent](hermes-agent.md) | multi-agent | 是 | 自托管 memory + skills + subagents 环境 | 已核验 |
| [OpenClaw](openclaw.md) | platform | 是 | 多渠道、多设备、本地优先 runtime | 已核验 |
| [LangChain](langchain.md) | platform | 是 | 快速搭自定义 agent 的高层框架 | 已核验 |
| [LangGraph](langgraph.md) | platform | 是 | 长期运行、有状态 agent workflow 的底层框架 | 已核验 |
| [Continue](continue.md) | platform | 是 | 支持自选模型的开源 IDE 扩展 | 已核验 |
| [Claude Fable 5](claude-fable-5.md) | model / agentic | 否 | Anthropic 的 Mythos 级前沿模型——Claude 系 agent 在 Opus 之上的能力天花板 | 已按发布与恢复公告核验 |
| [GPT-5.5](gpt-5.5.md) | model / agentic | 否 | 驱动 Codex、ChatGPT 和 API 的前沿 agentic 模型（2026-07 已由 GPT-5.6 接棒） | 已按发布材料核验 |
| [AutoGPT](autogpt.md) | autonomous | 是 | 可视化 agent 搭建平台，带工作流和市场 | 已核验 |
| [CrewAI](crewai.md) | multi-agent | 是 | 角色型多 agent 编排框架 | 已核验 |
| [LlamaIndex](llamaindex.md) | platform | 是 | 数据优先的 RAG 与 agent 框架 | 已核验 |
| [n8n](n8n.md) | runtime / tools | Fair-code | 带原生 AI agent 节点的可视化工作流自动化 | 已核验 |
| [MemGPT](memgpt.md) | runtime / tools | 是 | 带持久记忆的有状态 agent（现名 Letta） | 已核验 |
| [Agent Zero](agent-zero.md) | autonomous | 是 | 自构建自主 agent，动态创建工具 | 已核验 |
| [BabyAGI](babyagi.md) | experimental | 是 | 开创性自主 agent 实验——教学用 | 已核验 |
| [Julep](julep.md) | workflow engine | 是 | Temporal 支撑的持久化有状态 agent 工作流引擎 | 已核验 |
| [Haystack](haystack.md) | platform | 是 | deepset 的生产导向 RAG 和 agent 框架 | 已核验 |
| [Semantic Kernel](semantic-kernel.md) | platform | 是 | 微软 AI 编排 SDK，.NET / Python / Java | 已核验 |
| [DSPy](dspy.md) | platform | 是 | 程序化 prompt 优化框架 | 已核验 |
| [Open Interpreter](open-interpreter.md) | runtime / tools | 是 | 自然语言到本地代码执行 | 已核验 |
| [LiteLLM](litellm.md) | infrastructure | 是 | 100+ LLM provider 的统一 API 网关 | 已核验 |
| [Pydantic AI](pydantic-ai.md) | platform | 是 | 类型安全 Python agent 框架，结构化输出 | 已核验 |
| [Flowise](flowise.md) | runtime / tools | 是 | 拖拽式 LLM 应用和 agent 可视化构建器 | 已核验 |
| [Froge Code](froge-code.md) | automation | 是 | 当前映射为 Automagik Genie | 对外命名仍在演进 |
| [Mercury Agent](mercury-agent.md) | multi-channel runtime | 是 | 权限硬化的 CLI + Telegram 自托管 agent，带 token 预算 | 已按当前仓库核验 |
| [Pi](pi.md) | execution / toolkit | 是 | 极简终端 coding agent harness，多 LLM provider 支持 | 2026-04 被 Earendil 收购后已核验 |
| [ml-intern](ml-intern.md) | autonomous（垂直领域） | 是 | 基于 Hugging Face 生态的自主 ML 工程 agent | 已核验 |
| [GenericAgent](generic-agent.md) | autonomous（自演进） | 是 | 从小种子起步、每完成任务长 skill tree 的自主 agent | 候补 2 周后已核验 |
| [Superpowers](superpowers.md) | skills 框架 / 方法论 | 是 | 可组合 agentic skills 框架，集成 Claude Code、Codex、Cursor、Copilot、Gemini | 已按 v5.1（2026-05）核验 |
| [CodeWhale](codewhale.md) | execution（DeepSeek + MiMo） | 是 | DeepSeek + MiMo 终端 coding agent（原 DeepSeek-TUI） | 已在 2026-05 飙升期核验 |
| [Ruflo](ruflo.md) | 多 agent 编排 | 是 | 跨机器联邦的 Claude 编排平台（前身 Claude Flow） | 改名后已核验 |
| [OpenHuman](openhuman.md) | 自托管 / 本地 runtime | 是 | 带 118+ 连接器、本地 Memory Tree、Ollama 支持的开源桌面生活集成 agent | 连续两周热度后已核验 |
| [CodeGraph](codegraph.md) | runtime / agent 上下文 | 是 | 为 Claude Code、Cursor、Codex CLI、opencode、Hermes Agent 服务的预索引代码知识图谱 + MCP server | 2026-05 trending 期间已核验 |
| [CLI-Anything](cli-anything.md) | runtime / agent-native 桥接 | 是 | 为任意软件自动生成 Click CLI，让 agent 能驱动没有 API 的应用 | 已按 v1（2026-05）+ HKUDS 维护核验 |
| [SWE-agent](swe-agent.md) | harness 框架 / 研究参考 | 是 | Princeton + Stanford 的 SWE-bench 原始 harness，single-YAML 配置 | 已按上游核验，团队精力已转移至 mini-swe-agent |
| [mini-swe-agent](mini-swe-agent.md) | harness 框架 / 极简 | 是 | SWE-agent 的 ~100 行 Python 接班版，SWE-bench Verified >74% | 已按上游 README 核验 |
| [OpenHarness](openharness.md) | harness 框架 / 生产级 | 是 | HKUDS 的 10 子系统开源 harness，43+ 工具、anthropics/skills、MCP | 已按 v0.1.9（2026-05）核验 |
| [jcode](jcode.md) | harness 框架 / 编码 | 是 | Rust 多会话 coding harness——启动最快、provider 中立 OAuth、被动语义记忆 | 2026-07 核验（10.6k，从候补转正） |
| [TrueForge](trueforge.md) | harness 框架 / 服务端 | 是 | harness 即服务端：一个循环挂在 HTTP API 后面，带目录化配置、沙箱即工具、审批、subagent，以及公开的成本 benchmark | 对照上游 README 与文档核验（2026-09 收录） |
| [eve](eve.md) | 平台 / agent 框架 | 是 | Vercel 的文件系统优先 agent 框架——持久化执行、每 agent 沙箱、审批、subagent、evals、渠道适配 | 对照上游 README 与发布博文核验（2026-08 补漏收录） |

## 写法标准

统一写法见 [evaluation-framework.md](evaluation-framework.md)。

## 命名说明

如果项目名称、定位或官方公开边界本身就有歧义，这个目录会直接把歧义写出来，而不是假装已经核验清楚。