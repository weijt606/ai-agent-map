# Mercury Agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](mercury-agent.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/mercury-agent.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Mercury Agent 是一个走"权限硬化 + 长期常驻"路线的自托管多通道 agent，不是只跑一次的 coding 工具。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | cosmicstack-labs |
| 路线 | 自托管多通道 agent，主打权限守卫 |
| 是否开源 | 是（MIT，TypeScript） |
| 最适合 | 想常驻运行、又需要审批、token 预算和持久记忆的个人或小团队 |
| 主要代价 | 你自己负责 daemon、权限策略和通道表面 |
| 官网 | https://mercury.cosmicstack.org |
| GitHub 仓库 | https://github.com/cosmicstack-labs/mercury-agent |

## 什么时候选它

- 你想要一个能从终端和 Telegram 两边都触达的长期 assistant，状态共享。
- 你要的是显式审批工作流、shell 黑名单、文件夹级作用域，而不是默认放权。
- 你需要每日 token 预算和"超过 70% 自动收紧"机制，避免账单失控。
- 你希望 agent 的人格层（`soul.md`、`persona.md`）是你能直接编辑和版本控制的。

## 什么时候别选

- 你只想丢一次 coding 任务、跑完就结束。
- 你不想常驻一个 daemon，也不想长期维护 SQLite 存储和权限策略。
- 你想要一个有厂商 SLA 的托管产品。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Tool use | 强 | 31 个内置工具，覆盖文件系统、shell、git、web、调度和消息 |
| 权限 | 非常强 | shell 黑名单、文件夹作用域和审批工作流都是核心能力 |
| Memory | 强 | SQLite 支撑的"Second Brain"，10 种记忆类型 + 全文搜索 |
| Scheduling | 强 | 持久化调度器 + daemon 模式自动重启 |
| 多通道访问 | 强 | CLI 流式输出 + Telegram（admin / member 角色） |
| Provider 自由度 | 强 | 支持 DeepSeek、OpenAI、Anthropic、Grok、Ollama Cloud、本地 Ollama，可回退 |

## 使用代价

复杂度是 Medium。安装本身不算难，但 Mercury 是一个需要长期维护的 daemon——权限策略、记忆整理和通道访问都要持续打理。Token 预算能控住花费上限，但运营面没有因此消失。

## 在自托管 / 本地 runtime 这条线上的取舍

- 对比 [Hermes Agent](hermes-agent.md)：Hermes 把 memory、skills 和 subagent delegation 作为主路径。Mercury 主路径是权限硬化 + token 预算 + Telegram 通道。
- 对比 [OpenClaw](openclaw.md)：OpenClaw 的 runtime / gateway 横跨更多渠道和设备。Mercury 更收敛——只到 CLI + Telegram，但审批纪律更严格。
- 对比 [Goose](goose.md)：Goose 强调 desktop / CLI / API 三面 + extensions 生态。Mercury 把审批和预算护栏放在更前面，扩展面相对窄。

## 最后一句

如果你要的是一个"长期常驻、严格权限、有 token 预算、能从 Telegram 调用"的自托管 agent，Mercury 值得排进 shortlist。如果你只想要一个纯 coding 执行器或托管产品，先看别的。
