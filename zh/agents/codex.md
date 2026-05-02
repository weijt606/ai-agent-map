# Codex

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](codex.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/codex.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：如果你喜欢“把任务丢出去，在云端隔离环境里跑完，再回来 review”，Codex 很有代表性。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | OpenAI |
| 路线 | ChatGPT 内的云端软件工程 agent |
| 是否开源 | 否，但 Codex CLI 开源 |
| 最适合 | 异步任务、隔离环境、日志证据、并行委派 |
| 主要代价 | 仍偏云端 research preview，远程节奏不如本地 agent 即时 |
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
| Computer use | 强（2026-04-16 新增） | 在任意 macOS app 内后台鼠键操作，包括没有 API 的 app |
| Local companion surfaces | 强（原"中"） | Codex CLI 已成为一线表面，v0.128 加入持久化 /goal workflow 和 MultiAgentV2 |

## 近期能力扩展

2026 年 4 月 16 日，OpenAI 推出 "Codex for (almost) everything"，是 2026 年 Codex 产品表面的最大单次更新。对选型来说重要的变化：

- **后台 Computer Use：** Codex 用自己的鼠标和键盘操作任意 macOS app——与通用 computer-use agent 的差距被拉平。
- **并行多 agent 执行：** 多个 Codex agent 可以在同一台 Mac 并行运行，不干扰前台工作。
- **内置浏览器 + 主动建议：** 前端迭代不用切上下文，并基于项目记忆主动提议工作。
- **90+ plugin：** Atlassian Rovo、CircleCI、CodeRabbit、GitLab Issues、Microsoft Suite 等。
- **周活 300 万开发者**（2026 年 4 月数据），约为 3 月初的 2 倍。

Codex CLI（开源终端伴侣，github.com/openai/codex）也走得很快：2026-04-30 的 v0.128.0 引入持久化 /goal workflow、MultiAgentV2 控制、plugin marketplace 安装和更细的权限 profile。现在 CLI 与 Claude Code、Aider 在同一个选型对话里讨论，云端 Codex 产品则作为互补的后台路径。

## 使用代价

复杂度是 Medium。它帮你减轻本地运维负担，但也会把团队带进“远程委派 + 回来看结果”的异步节奏。当前更准确的理解方式是：主产品是闭源云端 agent，Codex CLI 是相关但独立的本地 companion surface。

## 模型层

截至 2026 年 4 月 23 日，Codex 底层已升级为 [GPT-5.5](gpt-5.5.md)——OpenAI 最新的前沿 agentic 模型。模型升级带来了更强的编码 benchmark（Terminal-Bench 2.0 得分 82.7%）、百万 token 上下文窗口和更高的 token 效率。如果你在评估 Codex，模型层现在比以往更重要。详见 [GPT-5.5 profile](gpt-5.5.md)。

## 最后一句

经过 2026 年 4 月 16 日更新，Codex 更适合理解成一个多表面 coding agent：ChatGPT 里的云端 agent、带 Computer Use 和并行后台执行的桌面 app，再加上已经能与 Claude Code、Aider 正面比较的开源终端 CLI。