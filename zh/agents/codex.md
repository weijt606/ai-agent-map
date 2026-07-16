# Codex

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](codex.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/codex.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Codex 是"丢出去、回来 review"这条路线的代表，2026 年 7 月 9 日起它整体并入 ChatGPT 应用——云端委派、桌面 Computer Use、开源 CLI 都在同一个屋檐下。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | OpenAI |
| 路线 | ChatGPT 应用内的 coding agent 表面（云端 + 桌面），外加开源的 Codex CLI |
| 是否开源 | 否，但 Codex CLI 开源 |
| 最适合 | 异步任务、隔离环境、日志证据、并行委派 |
| 主要代价 | 委派-review 的节奏不如本地 agent 即时，且产品表面仍在快速变化 |
| 官网 | https://developers.openai.com/codex |
| GitHub 仓库 | https://github.com/openai/codex |

## 什么时候选它

- 你有很多边界清晰的 coding task，想丢给 agent 并行跑。
- 你很看重测试输出、终端日志和可追踪执行证据。
- 你的团队本来就习惯 issue、PR、review 这种异步工作方式。
- 你接受主产品运行在 ChatGPT / 云端隔离环境里，而不是完全本地执行。

## 什么时候别选

- 你要的是持续、本地、对话式的结对编程体验。
- 你要求严格自托管或离线运行。
- 你真正需要的是带消息渠道和设备能力的 runtime 系统。
- 你想把开源的 Codex CLI 直接当成这个主产品本身来理解。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Isolated execution | 很强 | 每个任务独立运行是核心卖点 |
| Code execution | 强 | 能跑命令、测试、类型检查 |
| Review evidence | 强 | 很适合 review-first 团队 |
| Background delegation | 很强 | 4 月 16 日更新后多 agent 可并行在同一台机器跑 |
| GitHub / PR handoff | 强 | 适合把结果带回 review 流程 |
| Computer use | 强 | 在任意 macOS app 内后台鼠键操作；7 月 9 日换用 GPT-5.6 后明显更快 |
| PR review in-app | 强（2026-07-09 新增） | ChatGPT 桌面应用内的侧栏 PR review 和 diff 内联编辑 |
| Local companion surfaces | 强（原"中"） | Codex CLI 已成为一线表面，v0.128 加入持久化 /goal workflow 和 MultiAgentV2 |

## 并入 ChatGPT（2026 年 7 月 9 日）

2026 年 7 月 9 日，OpenAI 把独立的 Codex 应用并入 macOS / Windows 的 ChatGPT 桌面应用。对选型来说重要的变化：

- **Codex 成为 ChatGPT 内的一个入口**，与 Chat 和新发布的 agentic 模式 **ChatGPT Work** 并列——所有计划可用，包括免费版。
- **diff 内联编辑 + 侧栏 PR review**，把更多 review 环节搬进应用内部。
- **更快的 Computer Use（由 GPT-5.6 驱动）**，以及跨代码库任务用的**多仓库项目**。
- **规模**：Codex 周活超 500 万，其中 100 万以上的用户完全用它做软件开发以外的工作。
- **Codex CLI 不受影响**——仍是 github.com/openai/codex 的开源终端表面。

## 更早的 2026 扩展（4 月 16 日）

2026 年 4 月 16 日，OpenAI 推出 "Codex for (almost) everything"，是并入 ChatGPT 之前 Codex 产品表面的最大单次更新。对选型来说重要的变化：

- **后台 Computer Use：** Codex 用自己的鼠标和键盘操作任意 macOS app——与通用 computer-use agent 的差距被拉平。
- **并行多 agent 执行：** 多个 Codex agent 可以在同一台 Mac 并行运行，不干扰前台工作。
- **内置浏览器 + 主动建议：** 前端迭代不用切上下文，并基于项目记忆主动提议工作。
- **90+ plugin：** Atlassian Rovo、CircleCI、CodeRabbit、GitLab Issues、Microsoft Suite 等。
- **周活 300 万开发者**（2026 年 4 月数据），约为 3 月初的 2 倍。

Codex CLI（开源终端伴侣，github.com/openai/codex）也走得很快：2026-04-30 的 v0.128.0 引入持久化 /goal workflow、MultiAgentV2 控制、plugin marketplace 安装和更细的权限 profile。现在 CLI 与 Claude Code、Aider 在同一个选型对话里讨论，云端 Codex 产品则作为互补的后台路径。

## 使用代价

复杂度是 Medium。它帮你减轻本地运维负担，但也会把团队带进“远程委派 + 回来看结果”的异步节奏。当前更准确的理解方式是：主产品是闭源云端 agent，Codex CLI 是相关但独立的本地 companion surface。

## 模型层

截至 2026 年 7 月 9 日，Codex 底层已换成 **GPT-5.6**（Sol / Terra / Luna 三档）——与产品并入 ChatGPT 同日接棒 [GPT-5.5](gpt-5.5.md)。升级最直观的体现是 Computer Use 速度和 agentic 编码 benchmark。模型谱系与发布后格局（包括 Anthropic 的 Mythos 级 [Claude Fable 5](claude-fable-5.md)）详见 [GPT-5.5 profile](gpt-5.5.md)。

## 最后一句

经过 2026 年 7 月 9 日的合并，Codex 更适合理解成 ChatGPT 应用的 coding 表面，而不是一个独立产品：云端委派、桌面 Computer Use、应用内 PR review 全计划可用——外加已经能与 Claude Code、Aider 正面比较的开源终端 CLI。