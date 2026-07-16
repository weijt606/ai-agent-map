# 市场事件

[English](../market-events.md) | [中文](market-events.md)

重塑 agent 选型格局的结构性事件——模型发布、产品合并、浪潮——新的在前。每周的逐窗口记录在 [agents/README.md](agents/README.md) 的"市场事件"时间线里；本页保存长期有效的档案。

## 2026-07-09 —— Codex 并入 ChatGPT；GPT-5.6 发布

OpenAI 把独立的 Codex 应用并入 ChatGPT 桌面应用（macOS/Windows）：Codex 成为与 Chat 和新的 agentic 模式 **ChatGPT Work** 并列的专属编码入口，所有计划（含免费版）可用。同日，**GPT-5.6** 在 ChatGPT、Codex 和 API 全面接棒 GPT-5.5，分三档——Sol（$5/$30 每百万 token）、Terra（$2.5/$15）、Luna（$1/$6），另有 Ultra 多 agent 模式。Codex 周活超 500 万，其中 100 万以上用于软件开发以外的工作。

**对选型的影响：** OpenAI 侧"选哪个 coding agent"的问题坍缩成"你怎么用 ChatGPT"——移动的是产品边界，不只是能力。GPT-5.6 Sol 以 GPT-5.5 的老价格领跑 Artificial Analysis 编码 agent 指数（80，vs Fable 5 77.2、GPT-5.5 76.4、Opus 4.8 72.5），GPT-5.5 就此成为过渡选择。详见 [Codex](agents/codex.md)、[GPT-5.5](agents/gpt-5.5.md)。

来源：[OpenAI Codex changelog](https://learn.chatgpt.com/docs/changelog)、[GPT-5.6 公告](https://openai.com/index/gpt-5-6/)、[Axios](https://www.axios.com/2026/07/09/ai-openai-gpt-release)。

## 2026-06-09 —— Claude 5 家族：Fable 5 与 Mythos 级

Anthropic 发布 **Claude Fable 5** 和 **Claude Mythos 5**——同一底层模型，Fable 5 面向所有人（附加安全措施），Mythos 5 仅限获批组织。Mythos 是位于 Opus 之上的新等级。Fable 5 成为 Claude Code 中 Pro/Max 的默认模型，6 月 12 日因短暂的美国出口管制全球下架，7 月 1 日在更严格的安全分类器后面恢复（被拦截的请求回退 Opus 4.8），7 月 7 日起改为按量计费的 usage credits。两周前（5 月 28 日），**Opus 4.8** 已修复 Opus 4.7 的 tool-calling 问题并推出 Dynamic workflows。

**对选型的影响：** Anthropic 侧的模型层变成两档预算决策——最难的活花 Fable 5 额度，Opus 4.8 作为可靠默认档。详见 [Claude Fable 5](agents/claude-fable-5.md)、[Claude Code](agents/claude-code.md)。

来源：[Anthropic 公告](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)、[Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)。

## 2026-05（持续中）—— `.claude/skills` 浪潮

5 月中旬冲上 GitHub trending 的浪潮持续复利：curated skill 合集与 skills 框架此后一直占据每周热度前 10 的约一半。Star 数截至 2026-07-16：

| 仓库 | Stars | 形态 |
| --- | --- | --- |
| [Superpowers](agents/superpowers.md) | 255.9k | 完整的 skills 框架 + 方法论，接入 Claude Code、Codex、Cursor、Copilot 等 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 173.8k | Matt Pocock 的个人 `.claude/skills` 精选目录 |
| [anthropics/skills](https://github.com/anthropics/skills) | 161.6k | Anthropic 官方 Agent Skills 参考仓库——模式的上游源头 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.7k | Addy Osmani 面向 coding agent 的生产级工程技能集 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 38.1k | 面向 Claude Code 的学术研究管线 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 31.0k | 覆盖科研/科学/工程/分析/金融/写作的即用型技能 |

**对选型的影响：** `.claude/skills` 模式已经从新鲜事物变成共享基础设施——工程师像当年发布 dotfiles 一样发布自己的技能库，很多任务里技能层和底层 agent 同样重要。本地图通过 [Superpowers](agents/superpowers.md) 覆盖框架端，curated 合集作为候补跟踪（内容资产而非 agent 表面）；浪潮有自己的榜单，见 [rankings/skill-verticals.md](rankings/skill-verticals.md)。

## 2026-04 —— GPT-5.5 与 "Codex for (almost) everything"

相隔一周的两次 OpenAI 发布定下了春季格局。**4 月 16 日**：并入 ChatGPT 之前 Codex 最大的一次产品更新——任意 macOS app 的后台 Computer Use、同机并行多 agent 执行、带主动建议的内置浏览器、90+ plugin、周活 300 万开发者（3 月初的 2 倍）。**4 月 23 日**：**GPT-5.5** 作为 OpenAI 前沿 agentic 模型发布——Terminal-Bench 2.0 得分 82.7%（发布时最高）、1M token 上下文窗口、价格是 GPT-5.4 的 2 倍。

**对选型的影响：** 两者一起抬高了所有 OpenAI 系表面的能力上限，把模型层带进了 agent 选型。两者如今都已被接棒（见 7 月 9 日条目），但仍是"2026 竞赛跑得有多快"的参照点。详见 [GPT-5.5](agents/gpt-5.5.md)、[Codex](agents/codex.md)。
