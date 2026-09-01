# Agent Harness 框架对比

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](agent-harness-frameworks.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/agent-harness-frameworks.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

"harness" 是把 LLM 变成 agent 的最小脚手架——循环、工具表面、权限模型、skills 挂载点。这些项目你可以 fork、审计、端到端拥有，而不是照单全收的厂商产品。

九个项目的当前 star 总量见[分类排行](../rankings/README.md)；本页比的是形态，不是体量。

这条路线下现在有三种形态。**单循环 harness** 本身*就是*那个循环——你 fork 一个然后完全拥有它。**元 harness** 把好几个这样的循环收拢到一层之下，是当"用哪个 harness"不再只有一个答案时你会去找的东西。**harness 即服务端**只跑一个循环，但把它放在一条 API 后面，是当这个 agent 属于你的产品而不是属于你的终端时你会去找的东西。

## 一览

| 项目 | 许可证 | 甜点区 | 体量 |
| --- | --- | --- | --- |
| [Pi](../agents/pi.md) | MIT（TS） | 终端优先的 coding harness，LLM 提供商覆盖面广 | 小核心 + 按需 skills/扩展 |
| [jcode](../agents/jcode.md) | MIT（Rust） | 快、占用小、面向多会话工作流的终端 harness，带被动语义记忆 | 精简 Rust 二进制——同类中启动最快、RAM 最低 |
| [OpenHands](../agents/openhands.md) | 开源 | 完整的开源 SWE agent（CLI + GUI + 云选项） | 最重——更接近产品 |
| [SWE-agent](../agents/swe-agent.md) | MIT（Py） | SWE-bench 背后的研究参考实现，单 YAML 配置 | 中等；上游重心转向 mini-swe-agent |
| [mini-swe-agent](../agents/mini-swe-agent.md) | MIT（Py） | ~100 行的接班版；SWE-bench Verified >74% | 极小——一次就能读完 |
| [OpenHarness](../agents/openharness.md) | MIT（Py） | 10 子系统开放 harness，带 anthropics/skills + MCP + 43 工具 | 中等；生产形态，与 [CLI-Anything](../agents/cli-anything.md) 同门 |

## 元 harness

这两个不自带循环。它们把上面那些 harness（以及 [Claude Code](../agents/claude-code.md)、[Codex](../agents/codex.md) 这类厂商产品）收到一个接口背后，并补上裸循环缺的那些东西：身份、审批策略、沙箱、调度，以及一个别人能围观的地方。

| 项目 | 许可证 | 能跑 | 它优化的"单位" | 注意 |
| --- | --- | --- | --- | --- |
| [QM](../agents/qm.md) | MIT（TS） | Pi、OpenCode、Codex、Claude Code | **一家公司。** 作用域 = 一个人、频道、群聊或项目，各自拥有记忆、文件、keychain、权限、cron 和常驻沙箱 | 才几天大；是一套真要运维的部署（Postgres、沙箱、你自己的云账号）；贡献只收文字提案不收代码 |
| [Omnigent](../agents/omnigent.md) | Apache-2.0（Py） | Claude Code、Codex、Cursor、OpenCode、Hermes、Pi、YAML 自定义 agent | **一个开发者。** 会话是单位；它跟着你在终端、浏览器、手机和桌面之间走，还能跑在九家云沙箱供应商之一上 | 自标 **alpha**；前置依赖链横跨三个语言生态（`uv`、Node、tmux，Linux 上还要 `bwrap`） |

在这两个之间做选择时真正关键的区别：QM 假设的是**很多人共用一套部署**，它给每个人隔离；Omnigent 假设的是**一个人驱动很多 agent**，它给这些 agent 连续性和策略。两者不能互相替代。

## harness 即服务端

一个循环，当成服务来跑。你不 fork 它，也不用它去指挥别的 harness——你把它部署起来，一次性接好各个 provider，然后从自己的产品里用 HTTP 调它。

| 项目 | 许可证 | 前门 | 它优化的"单位" | 注意 |
| --- | --- | --- | --- | --- |
| [TrueForge](../agents/trueforge.md) | MIT（TS） | 自带聊天 UI、HTTP API + TypeScript SDK、可嵌入 UI SDK | **你产品的后端。** 模型、MCP server、skill、沙箱都从目录一次性接好；agent 只能从运维批准过的东西里挑 | 公开六周，版本还是 0.x 的 release candidate；贡献者几乎全来自一家公司；沙箱目前只有 Daytona；没有定时，也没有渠道适配器 |

它之所以是一种独立形态而不是单循环那张表的一个脚注：把循环放到 API 边界后面，会逼出可 fork 的那些 harness 根本不用做的选择。会话状态必须持久化而不能留在进程里，工具面必须集中声明而不能每次调用传进来，审批必须能渲染给正拿着客户端的那个人看——这也是为什么它的审批是 Generative UI 而不是终端提示。TrueForge 还是这条路线上唯一一个用**可复现的成本对比**立论的条目（14 个跨系统任务，对 [Claude Managed Agents](../agents/claude-managed-agents.md) 和 deepagents，同模型同 MCP server，脚手架在 `benchmark/` 里），而不是靠功能清单。把它当厂商自测来读——然后还是要读。

## 怎么选

- 按体量选，不按 star 选。合适的 harness 是那个你愿意长期维护其表面积的。
- 想要最小可信的 fork 底座：[mini-swe-agent](../agents/mini-swe-agent.md)。
- 想要生产形态、可自托管的开放 runtime：[OpenHarness](../agents/openharness.md)。
- 想发表 SWE-bench 成绩：[SWE-agent](../agents/swe-agent.md) 是规范参考，mini-swe-agent 是实际接班者。
- 想要终端优先的日常 coding harness：[Pi](../agents/pi.md)；如果优先要速度、多会话下的低 RAM、以及内置被动记忆，选 [jcode](../agents/jcode.md)。
- 想要更完整但仍开源的 SWE agent 产品：[OpenHands](../agents/openhands.md)。
- 如果问题已经不是"选哪个 harness"，而是"好几个 harness 怎么在同一套策略下运行"：单个开发者跨设备用 [Omnigent](../agents/omnigent.md)，整个团队在 Slack 和 web 上用 [QM](../agents/qm.md)。两者都会在你的 agent 循环中间加一个依赖——真的同时在跑多个 harness 时再上，不要提前上。
- 如果这个 agent 是**你产品的一个功能**而不是你机器上的一个工具——它需要 API、需要登录、需要一个你的用户看得见的审批界面：[TrueForge](../agents/trueforge.md)。代价是你从此要运维 Postgres、Redis 和一个沙箱 provider；换来的是循环这部分你不用再运维。
