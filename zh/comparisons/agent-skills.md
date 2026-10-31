# Agent Skills

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](agent-skills.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/agent-skills.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

skill（技能）就是一个装着说明、有时还带脚本的文件夹，agent 在任务需要时才把它加载进来。5 月 [`.claude/skills` 浪潮](../market-events.md#2026-05持续中-claudeskills-浪潮)开始以来，skill 集合一直是本地图跟踪的仓库里 star 最多的一批。本地图不给精选集合写 profile，因为它们是内容资产，不是 agent 本身；这一页就是比较它们的地方。本页讲四件事：skill 是什么，哪些 agent 能加载它，最大的五个集合和框架，以及装别人的 skill 之前要查什么。

> **最近复核：** 2026-11-01 · 下面每条事实都来自厂商自己的文档、仓库自己的 README 和文件，或维护者自己的网站。star 数是本地图 2026-10-28 的快照。厂商自报的数字都注明了出处。

## skill 是什么

开放规范 [agentskills.io](https://agentskills.io) 的定义是"a folder containing a `SKILL.md` file"（一个含有 `SKILL.md` 文件的文件夹）。这个文件里有元数据（至少要有 `name` 和 `description`）和说明。skill 还可以附带 `scripts/`、`references/`、`assets/` 等其他文件。

```
my-skill/
├── SKILL.md      # 必需：name + description，然后是说明
├── scripts/      # 可选：agent 可以运行的代码
├── references/   # 可选：需要时才读的文档
└── assets/       # 可选：模板、素材
```

skill 是分阶段加载的，规范和 Anthropic 文档都把这叫作**渐进式披露**（progressive disclosure）。Anthropic 文档给出了每个阶段的开销：

| 阶段 | 何时加载 | 上下文开销（Anthropic 文档） |
| --- | --- | --- |
| 元数据（`name`、`description`） | 始终，启动时 | 每个 skill 约 100 token |
| `SKILL.md` 正文 | 请求与描述匹配时 | 5k token 以内 |
| 附带的文件和脚本 | 只有说明里引用到时 | 读之前为零；脚本代码本身不进上下文，只有输出进 |

所以决定 skill 什么时候触发的是 `description`。Anthropic 文档说它"must say both what the Skill does and when to use it"（必须同时写清做什么、什么时候用）。

**skill 和几个容易混淆的东西有什么不同**，各用其官方说法：

- **提示词**是"conversation-level instructions for one-off tasks"（针对一次性任务的对话级说明）；skill "load on demand"（按需加载），不用每次对话都重复同样的指导（Anthropic 文档）。自定义指令"apply broadly to all your conversations"（作用于所有对话）；skill 是"task-specific and only load when relevant"（针对特定任务、相关时才加载）（Claude 帮助中心）。
- **MCP** "is an open-source standard for connecting AI applications to external systems"（把 AI 应用连到外部系统的开源标准）（modelcontextprotocol.io）。Claude 帮助中心把两者分开说：MCP 把 Claude 接到外部服务和数据，skill 装的是做事的流程。两者可以一起用，让 Claude 知道怎么用 MCP 提供的工具。
- **插件**（plugin）在 Claude Code 里是"a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit"（一个由 skill、agent、hook、MCP server 等组件构成、整体安装加载的目录）。skill 是插件可以装的东西之一。下面的集合大多以插件形式发布。
- **Claude 的 Project** 提供"static background knowledge that's always loaded"（始终加载的静态背景知识）；skill 则"activate dynamically when needed"（需要时动态激活）（Claude 帮助中心）。

## skill 在哪里能用

只列官方文档里写明支持 Agent Skills 的 agent。预置的文档类 skill（Word、Excel、PowerPoint、PDF）是 Anthropic 的产品功能，不属于标准本身。Anthropic 文档说它们在 claude.ai 和 Claude API 上可用，在 Claude Code 里不可用。

| Agent | skill 放在哪里 | 怎么用 | 文档里值得注意的 |
| --- | --- | --- | --- |
| **Claude 应用**（claude.ai） | 自定义 → Skills → "+" → 上传 skill（把文件夹打成 ZIP） | 相关时 Claude 自己调用；每个 skill 可单独开关 | 需要先打开代码执行。自定义 skill 只属于个人，不是全组织共享 |
| **[Claude Code](../agents/claude-code.md)** | `~/.claude/skills/<名字>/SKILL.md`（个人）、`.claude/skills/<名字>/SKILL.md`（项目），或放在插件里 | 自动调用，或输入 `/skill-name` | 自定义命令"have been merged into skills"（已并入 skill） |
| **Claude Agent SDK** | `.claude/skills/` 和 `~/.claude/skills/`，通过 `settingSources` 加载 | 模型自行调用，或发送 `/<名字>`；用 `skills` 选项限定范围 | 没有编程注册接口，skill 就是磁盘上的文件 |
| **Claude API / Managed Agents** | 通过 `/v1/skills` 上传，或用预置的 `pptx` / `xlsx` / `docx` / `pdf` | 在 `container` 参数里列出 `skill_ids`，并带上代码执行工具 | 在沙箱里运行，不能联网 |
| **[Codex](../agents/codex.md) 与 ChatGPT** | `.agents/skills/`（仓库）、`~/.agents/skills/`（用户）；`$skill-installer` 可装精选 skill | 自动调用，或在 Codex 里用 `$` / `/skills`，在 ChatGPT 里用 `@` | 独立 skill 可用于 ChatGPT 桌面版、Codex CLI 和 IDE 扩展；插件里打包的 skill 在网页版和手机端也能用 |
| **[Cursor](../agents/cursor.md)** | `.agents/skills/`、`.cursor/skills/`（及 `~/` 下对应目录）；也读 `.claude/skills/` | 自动调用，或在 Agent 对话里输入 `/` | 来自 GitHub 仓库的 skill 要以插件形式导入 |
| **VS Code 里的 [GitHub Copilot](../agents/github-copilot.md)** | `.github/skills/`、`~/.copilot/skills/`；也列出 `.claude/skills/` 和 `.agents/skills/` | skill 适用时加载；对话里输入 `/skills` | 文档提醒只复用可信的 skill |
| **[Gemini CLI](../agents/gemini-cli.md)** | `.gemini/skills/` 或 `.agents/skills/`（及 `~/` 下对应目录）；`gemini skills install <git 地址>` | Gemini 调用 `activate_skill`，你在同意提示里批准 | 免费用户和 Google One 用户已于 2026-06-18 转到 Antigravity CLI |
| **[OpenCode](../agents/opencode.md)** | `.opencode/skills/`、`.claude/skills/`、`.agents/skills/`（及全局对应目录） | 内置 `skill` 工具按需加载 | 可在 `opencode.json` 里把每个 skill 设成允许、拒绝或询问 |

从这张表能看出两件事。第一，`.agents/skills/` 是这些 agent 共用最多的文件夹：Codex、Cursor、VS Code 里的 Copilot、Gemini CLI 和 OpenCode 都读它，Claude Code 的文档没有列它；而 Claude Code、Agent SDK、Cursor、VS Code 里的 Copilot 和 OpenCode 读 `.claude/skills/`。第二，自定义 skill 在 Claude 自家各个入口之间不同步。上传到 claude.ai 的 skill 要另外上传到 API，Claude Code 则在磁盘上另存一份。

Anthropic 自己的页面有一处不一致：帮助中心说 Free、Pro、Max、Ultra、Team、Enterprise 各档都能用 skill，平台文档则说自定义 skill 上传从 Pro 档起。以你自己账户的设置页为准。

## 标准现在归基金会了

**2026-10-22**，Anthropic [把 Agent Skills 捐给了 Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)（AAIF）。AAIF 是 Anthropic 与 Block、OpenAI 共同发起的 Linux 基金会项目，这次捐赠也包括 agentskills.io 域名。Anthropic 称"more than 70 agent platforms, including ChatGPT, Cursor, GitHub Copilot, and VS Code"（70 多个 agent 平台，包括 ChatGPT、Cursor、GitHub Copilot 和 VS Code）已接入这个标准，并称"1 million skills have been published and nearly 280 million installed"（已发布 100 万个 skill，安装近 2.8 亿次）。这些是 Anthropic 自报的数字，本地图没有独立统计，公告里点名的也只有这四个平台。对写 skill 的人来说，眼下什么都没变：格式还是那个格式，变的是它归谁管。这件事记在[市场事件](../market-events.md)里。

## 集合对比

按 2026-10-28 的 star 数排序。"skill 数"是 2026-11-01 各仓库里 `SKILL.md` 文件的个数；ECC 例外，它的目录树里有翻译副本，所以用它 README 里的数字。

| 项目 | 类型 | 对你来说改变了什么 | skill 数 | README 覆盖的 agent | 体量 | 维护者 | 许可证 | Star（2026-10-28） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Superpowers](../agents/superpowers.md) | 框架 + 方法论 | 一套自动触发、必须遵守的流程：头脑风暴 → git worktree → 计划 → 子 agent 或当前会话执行 → TDD → 代码评审 → 收尾分支 | 15 | 16 个安装目标，包括 Claude Code、Codex 应用与 CLI、Cursor、Gemini CLI、GitHub Copilot CLI、OpenCode、Antigravity、Kimi Code、Qwen Code、Pi、Hermes Agent | 每个 harness 装一个插件；会话开始时注入引导 | Jesse Vincent 与 Prime Radiant | MIT | 306.1k |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 个人集合 | 一组小 skill，你手动调用或 agent 自己挑：`/grill-me`、`/tdd`、`/to-spec`、`/diagnosing-bugs` 等，分成用户调用和模型调用两类 | 39（README 列出的工程与效率两组共 27） | Claude Code、Codex、GitHub Copilot（CLI 和 VS Code）、Gemini CLI；其他 agent 用 `npx skills` | 插件（自动更新）或可编辑的副本，二选一 | Matt Pocock | MIT | 304.7k |
| [ECC](../agents/ecc.md) | 框架 + 运行时层 | 一整套工程体系：子 agent、拦截命令的 hook、本地记忆库、AgentShield 配置扫描 | 314 个 skill、71 个 agent（README） | Claude Code 稳定；Codex 与 Qoder 原生；Cursor、OpenCode、Copilot CLI 为 beta；其余实验性 | 体量大；README 建议在意上下文时用 `--profile minimal` | Affaan Mustafa（README 自称"a single maintainer"） | MIT（托管的 Pro 档收费） | 290.6k¹ |
| [anthropics/skills](https://github.com/anthropics/skills) | 官方参考示例 | 演示这种模式：创意与设计、开发、企业沟通，以及 Claude 文件生成背后的文档类 skill | 20（含一个模板） | Claude Code（插件市场）、claude.ai、Claude API | 按插件挑（`document-skills`、`example-skills`） | Anthropic | 多数 Apache-2.0；`docx` / `pdf` / `pptx` / `xlsx` 是源码可见（source-available），不是开源 | 184.2k |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 按开发生命周期组织的集合 | 从 `/spec` 到 `/ship` 的九个命令（定义 → 计划 → 构建 → 验证 → 评审 → 上线），skill 也会自己触发 | 25 | Claude Code（推荐）、Codex、Cursor、Antigravity CLI、Gemini CLI、OpenCode、GitHub Copilot、Windsurf、Kiro、Command Code | 整包安装，或用 `npx skills` 一次装一个 | Addy Osmani | MIT | 111.0k |

¹ ECC 不在本地图的 star 快照里，这个数字是[它的 profile](../agents/ecc.md) 记录的 2026-10-28 数据。

维护者各自怎么介绍自己：**Matt Pocock** 说自己是"an educator, content creator and engineer"（教育者、内容创作者和工程师），现在全职教 AI 工程，并运营 Total TypeScript。**Addy Osmani** 的个人网站说他是"a Member of Technical Staff at Anthropic"，参与 Claude Code；此前在 Google 工作 14 年以上，最近的职位是 Google Cloud AI 的 Director。**Jesse Vincent** 和 Prime Radiant 一起开发 Superpowers，Prime Radiant 提供商业支持。**Affaan Mustafa** 按 README 的说法是 ECC 的唯一维护者。

怎么读这张表：Superpowers 和 ECC 改变的是*你的 agent 怎么干活*，用它们就是接受它们的流程。mattpocock/skills 和 addyosmani/agent-skills 是可以一个一个拿的库。anthropics/skills 自己说它的 skill "for demonstration and educational purposes only"（仅供演示和学习）：拿它学格式，别把它当产品用。

科研、金融、方法论等领域集合见 [skill 垂类](../rankings/skill-verticals.md)榜单。

## 装别人的 skill 之前

1. **skill 能跑代码。** Anthropic 文档原话："Use Skills only from trusted sources: those you created yourself or obtained from Anthropic"（只用可信来源的 skill：你自己写的，或来自 Anthropic 的）；如果非用不明来源的不可，要"thoroughly audit it before use"（使用前彻底审查），也就是检查 `SKILL.md`、脚本、图片和其他附带文件，留意意外的网络请求或文件访问。文档还说要"treat like installing software"（当成安装软件来对待）。Claude Code 另外写了两点：项目 skill 的 `allowed-tools` 即使在你从没信任过的文件夹里也会生效，所以要先看仓库里提交的 skill；`` !`command` `` 行会在 Claude 看到 skill 之前执行 shell 命令，设置 `"disableSkillShellExecution": true` 可以关掉。VS Code 文档也提醒只复用可信的 skill。Gemini CLI 激活 skill 前会征求你的同意，OpenCode 可以把 skill 设成"询问"。
2. **skill 闲着也占上下文。** 每个装上的 skill，描述每一轮都在上下文里：按 Anthropic 文档约 100 token 一个，Claude Code 每条列表最多截到 1,536 个字符。插件里的 skill 和 agent 也会加进来，"even in sessions where nothing from the plugin runs"（即使这次会话插件什么都没用上）。Claude Code 官方插件市场在安装前会显示上下文开销估算。同一套包用两种方式装，开销就翻倍；mattpocock/skills 提醒，插件和复制文件都装"gives you every skill twice"（每个 skill 都会有两份）。
3. **看清谁在维护。** 8 月 5–12 日那个窗口，浪潮里增量最大的两个席位都是个人目录，[市场事件](../market-events.md#2026-05持续中-claudeskills-浪潮)当时就指出了关键人风险。ECC 的 README 说它只有一位维护者。按某个 agent 的行为调好的 skill，在那个 agent 改版后可能失灵；anthropics/skills 也提醒"always test skills thoroughly in your own environment"（一定要在你自己的环境里充分测试）。
4. **留意数据条款。** Superpowers 的可选可视化组件会从 Prime Radiant 网站加载一个 logo，请求里带 Superpowers 的版本号。README 说不含任何项目信息，设置环境变量 `SUPERPOWERS_DISABLE_TELEMETRY` 即可关闭。

## 从哪里开始

1. **你只想让 Claude 做文档。** claude.ai 上已经有预置的 Word、Excel、PowerPoint、PDF skill，不用装任何东西。
2. **你想搞懂这个格式。** 读 [anthropics/skills](https://github.com/anthropics/skills) 里的一个 skill 和 agentskills.io 的规范，然后在 `~/.claude/skills/` 或 `.agents/skills/` 里自己写一个 `SKILL.md`。自己写的十行 skill，比装一个 300 个 skill 的包学到的多。
3. **你用编码 agent，想要一整套方法。** 想要流程、不想多一层运行时，选 [Superpowers](../agents/superpowers.md)；主要用 Claude Code，还想要 hook、记忆和配置扫描，选 [ECC](../agents/ecc.md)。两者只装一个：各自都会强加自己的开发循环。
4. **你只想借几个好习惯。** 从 [mattpocock/skills](https://github.com/mattpocock/skills)（对齐需求、TDD）或 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)（从定义到上线的生命周期）里挑单个 skill。先装在项目范围，不触发的就删掉。

不管选哪个，上限还是由宿主 agent 决定。skill 告诉一个有能力的 agent 该怎么做，但不会让一个能力弱的 agent 变强。agent 本身的比较见[终端编码 CLI 对比](coding-cli-agents.md)。

## 最近变化

- **2026-11-01** —— 本页建立，起因是 Anthropic 10 月 22 日把标准捐了出去。顺带记下：ECC 的 README 现在写的是 314 个 skill、98 个命令（它 10 月 28 日的 profile 写的是 311 和 97）；Superpowers 的 README 现在列了 16 个安装目标，比它的 profile 列得多。

## 来源

- 标准：[agentskills.io 概览](https://agentskills.io) · [规范](https://agentskills.io/specification) · [Donating Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)（Anthropic，2026-10-22）
- Anthropic：[Agent Skills 概览](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Claude Code 中的 skill](https://code.claude.com/docs/en/skills) · [插件概览](https://code.claude.com/docs/en/plugins) · [Agent SDK 中的 skill](https://code.claude.com/docs/en/agent-sdk/skills) · [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) · [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- 其他 agent：[Codex / ChatGPT skill](https://learn.chatgpt.com/docs/build-skills) · [Cursor skill](https://cursor.com/docs/context/skills) · [VS Code agent skill](https://code.visualstudio.com/docs/copilot/customization/agent-skills) · [Gemini CLI skill](https://geminicli.com/docs/cli/skills/) · [OpenCode skill](https://opencode.ai/docs/skills/) · [What is MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- 集合：[Superpowers README](https://github.com/obra/superpowers#readme) · [mattpocock/skills README](https://github.com/mattpocock/skills#readme) · [ECC README](https://github.com/affaan-m/ECC#readme) · [anthropics/skills README](https://github.com/anthropics/skills#readme) · [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills#readme)
- 维护者：[mattpocock.com](https://www.mattpocock.com/) · [totaltypescript.com](https://www.totaltypescript.com/) · [addyosmani.com](https://addyosmani.com/)
