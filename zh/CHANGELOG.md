# 更新日志

[English](../CHANGELOG.md) | [中文](CHANGELOG.md)

记录本仓库的结构性里程碑，新的在前。热度表每周三例行刷新，例行更新见 git 历史和 [agents/README.md](agents/README.md) 的"市场事件"时间线，不在此处逐条记录。

## 2026-09-06 —— 第十四条路线：开放权重模型档

本地图的模型层此前只有两家闭源厂商，于是它回答不了自己一半条目底下的那个问题——[CodeWhale](agents/codewhale.md) 跑 DeepSeek 与 MiMo，[ZCode](agents/zcode.md) 跑 GLM，[Kimi Work](agents/kimi-work.md) 跑 Kimi。新增四个 profile（EN + zh）与一条新路线，收录数到 72。

- **新路线：开放权重 agentic 模型。** 有意与"前沿 agentic 模型"分开——"选哪个闭源天花板"和"我能自己托管、自己承担许可的是什么"是两个决策，而后者由许可决定的次数远多于由 benchmark 决定。
- **新增 [Kimi K3](agents/kimi-k3.md)** —— 2.8T 参数，首个开放的 3T 级模型，原生多模态，100 万上下文，自定义许可。按月之暗面自己的对照，其 Terminal-Bench 2.1 为 88.3，对 GPT-5.6 Sol 的 88.8 与 Fable 5 的 88.0。
- **新增 [GLM-5.3](agents/glm-5.md)**（Apache-2.0）—— 按厂商数字最强的开放权重编码模型，也是本地图第一次不得不写下"双用途能力不设闸"这个发现的 profile：智谱称其在 CyberGym 上的漏洞发现是 SOTA，利用链上的增益比 GLM-5.2 翻倍还多，而它带着宽松许可和一个下载链接。
- **新增 [DeepSeek V4](agents/deepseek-v4.md)**（MIT）—— 1.6T/49B，100 万上下文，SWE-bench Verified 80.6，另有 284B/13B 的 Flash 变体。
- **新增 [Qwen3-Coder](agents/qwen3-coder.md)** —— 回答"塞得进什么"的那个条目：Next 在 80B 里激活约 3B，256K 到 100 万上下文，在 Qwen Code、Cline、Claude Code 里都有一等支持。

结构性后果：[成本与基准](comparisons/cost-and-benchmarks.md)新增开放权重一节，算的是**硬件与许可而不是 token**；[market-events](market-events.md) 记录这一档追到前沿，以及它与 [GPT-6 Astra](agents/gpt-6-astra.md)、Mythos 之间在网安能力上的不对称；[主流格局](comparisons/mainstream-agent-landscape.md)加上四行。

工具改动：`render-route-map.py` 现在**自动算出路线数**，不再把"13 条路线"写死在四处字符串里，以后加路线不会再让 SVG 标题过期。

有一处"拒绝做"值得记下来。DeepSeek 报 SWE-bench Verified，Anthropic 报 SWE-bench Pro，OpenAI 报 DeepSWE，智谱报自家 benchmark。本次发布**没有**把这四个数字排进同一列——因为它们不是同一种测量；每家的数字都记在它自己的 benchmark 名下，就停在那里。

## 2026-09-06 —— 四个补漏：没有内核的 harness，以及中国的桌面 agent 品类

一次覆盖面扫描找出的不是"判断结果"而是"漏掉了"的缺口。新增四个 profile（EN + zh），收录数到 68：

- **新增 [DeepSeek Harness](agents/deepseek-harness.md)**（`deepseek-ai/deepseek-harness`，MIT，TypeScript）—— 2026-08-13 发布，三周后 **21.38 万 star / 2.51 万 fork**，是本地图迄今漏掉过的最大一个。它是 [harness 路线](comparisons/agent-harness-frameworks.md)上的第四种形态：不是你 fork 的循环，不是 meta-harness，也不是 HTTP 后面的 harness，而是**一个没有特权内核的 harness**——建在 Cordis 内核上，模型适配层、工具注册表、会话日志与 agent 循环本身全是可从配置替换的插件。按惯例带一个窗口的 `tracked: false`。
- **新增 [ZCode](agents/zcode.md)**（智谱）—— 一个 GLM 优先的开发者真正会打开的那个工具。桌面 agentic 开发环境，主对象是任务而不是文件，带长周期 "Goal" 运行，并可从微信、飞书、Telegram 远程操控。正因如此它进"直接执行"而不是编辑器路线。
- **新增 [WorkBuddy](agents/workbuddy.md)**（腾讯）与 **[Kimi Work](agents/kimi-work.md)**（月之暗面）—— 同一套 agent 循环，指向桌面知识工作。Kimi Work 是本目录里最锋利的例子：厂商明说它的内核是 [Kimi Code](agents/kimi-code.md)，于是一个编码 agent 的循环、长处与失效模式，现在跑在你挂载的文件夹和你已登录的浏览器上。

结构性后果：[market-events](market-events.md) 补两条（DeepSeek 那次发布，以及 3–6 月中国桌面 agent 品类的打开）；[agent harness 框架对比](comparisons/agent-harness-frameworks.md)与[主流格局](comparisons/mainstream-agent-landscape.md)加上新行；路线表里，ZCode 进直接执行，DeepSeek Harness 进 harness 路线，WorkBuddy 与 Kimi Work 进通用自主 agent。

有两件事本条目选择写明而不是藏起来。DeepSeek 那个仓库在本榜外躺了三周，那是扫描环节的失职，在 market-events 里如实记了一笔。以及四个新 profile 里有三个是**带授权本地文件访问的闭源产品**——桌面 agent 这个品类默认闭源，与本地图开放那一侧的惯例正好相反，profile 里都写清楚了。

## 2026-09-06 —— 前沿模型路线一次补齐两代

自本地图上次写下模型层以来，两侧各自又动了两次，而路线表还指着已经被接棒的条目。新增两个 profile（EN + zh），收录数到 64：

- **新增 [Claude Opus 5](agents/claude-opus-5.md)**（2026-07-24）—— 这条路线一直缺的那个条目：不是天花板，而是 Claude 系 agent 真正在跑的模型。价格守在 Opus 档的 $5/$25，CursorBench 3.2 距 Fable 5 峰值 0.5% 以内，1M 上下文既是默认也是上限。它在 Claude Code 里接替 Opus 4.8 成为可靠默认档——而本仓库好几页此前还写着旧的说法。
- **新增 [GPT-6 Astra](agents/gpt-6-astra.md)**（2026-09-03）—— OpenAI 当前的天花板，也是本地图记录到的第一个**公开版本本身就是受限版本**的前沿模型（它会拒绝自己一部分网安能力，进阶访问走 Daybreak Blue）。次日 Codex CLI `rust-v0.153.4` 把它设为打包默认，于是这条限制落到了产品默认之下。
- **[Claude Fable 5](agents/claude-fable-5.md) 更新到 Fable 5.1 / Mythos 5.1**（2026-09-01）—— 标价仍是 $10/$50，缓存读砍 75% 到 $0.25/M。profile 沿用原路径，既有链接不断。
- **[GPT-5.5](agents/gpt-5.5.md) 重新定位为血统参照** —— 其"发布后格局"表现在是 GPT-5.5 → GPT-5.6 → Astra，与 Opus 4.8 → Fable 5 → Sonnet 5 → Opus 5 → Fable 5.1 并列。

结构性后果：[成本与基准](comparisons/cost-and-benchmarks.md) 按一手价格页重建，并新增**缓存读一列**——两家天花板都落在 $10/$50 之后，标价已经不再是区分点；[market-events](market-events.md) 新增三条（Opus 5、Fable 5.1、Astra）；[README](README.md) 与 [agents/](agents/README.md) 的路线表现在把天花板和其下的默认档分开列，因为那是两个不同的决策。

两处刻意保留的来源纪律：Artificial Analysis 编码 agent 指数目前没有本地图愿意照抄的 Astra / Fable 5.1 / Opus 5 数字，因此那些格子留破折号，不用第三方榜单去填；外面流传的 Fable 5.1"SWE-bench Verified 95%"是第三方数字，Anthropic 公布的是 SWE-bench Pro 81.2，本地图记的是后者。

## 2026-08-12 —— 周更不再漂了

只动工具链，没有改任何内容页。此前周更会打两次独立的 GitHub 请求——一次在 `check`（它的数字被手写进热度表），另一次在 `publish`（它 stamp 出的 snapshot 驱动 `rankings/` 和几张 SVG）。两次之间 star 会涨，于是每周结束时热度表和生成的榜单都会差几个 star，必须再做一轮人工对账。

- **`check` 现在会把这次抓取记录到** `scripts/.fetch-cache.json`（已 gitignore），**`publish` 直接复用当天这份结果**而不再打 API。snapshot 和热度表从构造上就是同一批数字。两次调用之间新加进 `tracked-repos.txt` 的 slug——正是 playbook 里"pending pickup"那一步会做的事——会被单独抓取并合并进来；非当天的缓存视为过期忽略。`publish "<msg>" --refetch` 可强制重新抓取。
- **`validate.py` 新增 `[drift]` 检查**，把 README 热度表的增量与真正被 stamp 的那次抓取（`history.json` 最新的 `raw` 条目）对照。原有的 history 交叉校验永远抓不到这类问题，因为它的 window 就是*从* README 抄进去的，天然自洽。这条是为仍会抓两次的路径（`--refetch`，或在 check 之后隔天才 publish）兜底。
- 负增量现在显示成 `-1,234`，不再是 `+-1,234`。

## 2026-08-05 —— 元 harness 这一层，以及一个专职评审 agent

三个新 profile（EN + zh），地图收录数来到 60：

- **新增 [QM](agents/qm.md)**（`yc-software/qm`，MIT）—— Y Combinator 面向 Slack 和 web 的多人协作 agent harness。这是本地图第一个围绕"很多人共用一套部署"来设计的条目：按人、按房间各一个作用域，各自拥有记忆、文件、keychain、权限、cron 和常驻沙箱，底下的 core 可以互换地跑 Pi、OpenCode、Codex 或 Claude Code。
- **新增 [Omnigent](agents/omnigent.md)**（`omnigent-ai/omnigent`，Apache-2.0）—— 同一个元 harness 思路，但收窄到单个开发者：在一个会话里跑多个 harness，跟着你在终端、浏览器、手机和桌面之间走，带策略和九家云沙箱供应商。自标 alpha。
- **新增 [Open Code Review](agents/open-code-review.md)**（`alibaba/open-code-review`，Apache-2.0）—— 阿里跑了两年的内部评审助手，开源版。在模型外面包一条确定性流水线，用召回换准确，还有一个直接跑在你现有 coding agent 大模型上的委派模式。

结构性影响：[agent harness 框架](comparisons/agent-harness-frameworks.md) 新增**元 harness**小节，把"运行 harness 的层"和"harness 本身"分开；[市场事件](../market-events.md) 记录了这个模式的出现；[能力矩阵](capabilities/matrix.md)、[主流格局](comparisons/mainstream-agent-landscape.md)、[编码自动化](use-cases/coding-automation.md) 都补上了新行。同时把 Grok Build 补进主流格局矩阵，并把市场事件按该页声明的"新的在前"重新排序。

## 2026-07-22 —— 路线地图与 Top-10 构成图

两张新的主页可视化（EN + zh），与 bump chart 同一套设计语言：

- **路线生态地图**（`assets/route-map-{en,zh}.svg`，由 `scripts/render-route-map.py` 生成）——把"先摊开"那张表画成真正的地图：12 条路线作为卡片、按四类决策分组，每张卡列出旗舰项目。嵌在两个主页路线区顶部；路线变化时手动重渲（playbook step 5）。
- **Top-10 构成图**（`assets/heat-composition-{en,zh}.svg`，由 `scripts/render-composition.py` 生成）——每周 Top-10 席位按层（agent / infra / skill）的堆叠柱状图，数据来自 `history.json` + `catalog.json`。skills 浪潮故事的量化形态；已接进 `publish` 每周自动刷新，并纳入 `validate.py` 的 SVG 新鲜度闸门。

## 2026-07-22 —— 能力矩阵、成本/benchmark、记忆方案页

三个纯新增的对比面，把地图推过"只看流行度"，且不动现有路线/覆盖结构：

- **新增 [能力矩阵](capabilities/matrix.md)**（EN + zh）——把九个[能力维度](capabilities/README.md)并排应用到约 40 个项目，按核心（●）/ 支持（◐）/ 有限（○）/ 非目标（—）打分，按路线分组。终于用起了此前定义却从未大规模应用的能力词表。
- **新增 [成本 & benchmark](comparisons/cost-and-benchmarks.md)**（EN + zh）——前沿模型能力（Artificial Analysis 编码 agent 指数、SWE-Bench Pro）vs 每 token 价格，加上每个编码 agent 怎么收费（开源自带 / 订阅 / 按量额度 / 托管席位）。复用厂商 profile 里已确立的数字。
- **新增 [记忆方案对比](comparisons/memory-approaches.md)**（EN + zh）——把地图上带记忆的项目按*怎么*记分类（自编辑、被动语义、文件/关键词、代码知识图谱、个人数据树、长驻运行时），串起 jcode、MiMoCode、Letta、CodeGraph、OpenHuman、Hermes、Mercury。

两个对比页从 [comparisons/](comparisons/README.md) 链接；矩阵从 [capabilities/](capabilities/README.md) 链接。

## 2026-07-22 —— jcode 加入 harness 路线

- **新增 [jcode](agents/jcode.md) profile**（EN + zh）——这个 Rust 多会话 coding harness（`1jehuang/jcode`，MIT，10.6k）在进入每周增量前 10（#7）后，从候补转正为已收录 profile。它与 [Pi](agents/pi.md) 一起归入 **agent harness 框架** 路线，并接入 [harness 对比](comparisons/agent-harness-frameworks.md)（现为六个）、[选型矩阵](comparisons/mainstream-agent-landscape.md) 和 [编码自动化指南](use-cases/coding-automation.md)。覆盖数升至 55 个 profile；`catalog.json` 已把 jcode 标为已收录。

## 2026-07-16 —— 主页瘦身、厂商信息刷新、市场事件档案

- **README 重构降密度**：两个市场事件板块收成三条"市场脉搏"要点；50 行覆盖表折叠成四个可展开分组；热榜附注折叠；harness 表迁至 [comparisons/agent-harness-frameworks.md](comparisons/agent-harness-frameworks.md)；导航合并并新增排行入口。
- **厂商 profile 追平 2026 年 7 月**：Codex（7 月 9 日并入 ChatGPT 应用、GPT-5.6 驱动）、Claude Code（Fable 5 / Opus 4.8 模型演进）、Cursor、GitHub Copilot、GPT-5.5（发布后格局）。
- **新增 [Claude Fable 5](agents/claude-fable-5.md) profile**——Anthropic 的 Mythos 级加入前沿 agentic 模型路线。
- **新增 [market-events.md](../market-events.md)**（EN + zh）：结构性事件的长期档案，skills 浪潮数据已刷新。

## 2026-07-16 —— 排行体系扩建：趋势图、分类榜、垂类榜

- **每周排名趋势图（bump chart）**（`assets/heat-trend-{en,zh}.svg`），嵌入两个语言的主页和 [rankings/](rankings/README.md)。2026-04-11 以来的每个每周 top-N 窗口已从 git 历史回溯进 `scripts/history.json`；图表随每次发布自动重绘。
- **新增 [rankings/](rankings/README.md) 板块**（EN + zh 镜像）：Agent 榜、Agent 基础设施榜、Skill 榜，按当前 star 总量排序——存量视角，与主页按增量排序的热榜互补。
- **垂类排行**：agent 分为编程开发 / 通用助理 / 金融（[agent-verticals](rankings/agent-verticals.md)），skill 分为通用技能集 / 学术科研 / 金融 / 方法论（[skill-verticals](rankings/skill-verticals.md)）。
- **追踪仓库 23 → 42**：Claude Code、Aider、Cline、Continue、OpenHands、SWE-agent、mini-swe-agent、OpenHarness、Goose、AutoGPT、LangChain、LangGraph、CrewAI、LlamaIndex、n8n、Letta、Open Interpreter、LiteLLM、Flowise 加入每周 star 追踪，分类元数据在 `scripts/catalog.json`。
- **管线**：所有排行表格随发布自动重新生成；`validate.py` 新增历史文件与 README 热表的交叉校验，并拒绝过期图表。

## 2026-06-17 —— 每周更新自动化机制

`scripts/` 增加每周工具链：`fetch-stars.py`（star 抓取 + 快照）、`validate.py`（完整性闸门：链接、中英对等、热表同步）、`weekly-update.sh`（发布闸门——校验不通过一律不推送）、周三 playbook，以及每次 push 都跑的 CI 校验。

## 2026-06-11 —— 终端 Coding CLI 对比

新增对比页[终端 Coding CLI Agent 对比](comparisons/coding-cli-agents.md)；同期收录 Kimi Code、MiMoCode、CoStrict。

## 2026-05-23 —— Agent harness 框架路线

harness 框架拆为一级路线（Pi、OpenHands、SWE-agent、mini-swe-agent、OpenHarness），主页增加聚焦表。同周收录 OpenHuman、CodeGraph、CLI-Anything。

## 2026-05-19 —— 记录 `.claude/skills` 浪潮

skills 浪潮成为持续追踪的市场事件：curated 合集作为候补跟踪，框架端通过 Superpowers 的 profile 覆盖。

## 2026-04-24 —— 框架批次 + 像素风 banner

收录 Continue、CrewAI、AutoGPT、LlamaIndex、n8n、MemGPT；热度表加上更新时间戳和快照窗口；换上像素风 banner。

## 2026-04-11 —— 引入热度排行

第一份每周热度快照：按 star 增量排名的热门 agent 覆盖表。

## 2026-04-09 —— 项目启动

双语（EN + zh）agent 地图启动：路线分类、第一批 coding agent profile、对比页与用例脚手架。
