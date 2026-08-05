# Omnigent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](omnigent.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/omnigent.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：Omnigent 是一个开源**元 harness**——在 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi 以及你自己定义的 agent 之上架一层统一编排，让你在同一个会话里混用多个 harness，把这个会话在终端、浏览器、手机和桌面之间搬来搬去，可选地丢进一次性云沙箱里跑，并在这一切前面加上审批和花费策略。

> **它是 alpha，而且自己标了。** 仓库自带 `alpha` 状态徽章。对一个才两个月大的项目来说，它铺的面积大得反常——九家沙箱供应商、六个 harness、一个桌面应用——所以把这种广度理解成"意图"而不是"已经稳定的行为"，并且把版本钉死。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Omnigent（`omnigent-ai/omnigent`，omnigent.ai） |
| 路线 | Agent harness 框架——元 harness / 在其它 harness 之上做编排 |
| 开源 | Apache-2.0 |
| 实现 | Python 3.12+（`uv tool install omnigent`、Homebrew tap，或安装脚本） |
| harness | Claude Code、Codex、Cursor、OpenCode、Hermes、Pi，外加用 YAML 定义的自定义 agent |
| 模型 | 一方 API key、Claude 或 ChatGPT 订阅，或任何兼容网关 |
| 适合 | 想在一个受监督的会话里同时用多个 harness、并且希望随时换设备接手、可选跑在云沙箱里的开发者或小团队 |
| 主要代价 | alpha 状态、一条很重的前置依赖链（uv、Node、tmux，Linux 上还要 `bwrap`），以及你和 agent 之间又多了一层 |
| GitHub 仓库 | https://github.com/omnigent-ai/omnigent |

## 什么时候选它

- 你本来就在用不止一个 harness，受够了它们各自为政。Omnigent 把 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi 放进*同一个*会话，你可以按各自擅长的方向把一个任务拆开——或者让一个 agent 去评审另一个 agent 的产出。
- 你希望单位是会话而不是机器。在终端开始、在浏览器继续、在手机上接手；消息、子 agent、终端和文件保持同步。还有一个原生 macOS 桌面应用。
- 你想让 agent **跑在笔记本之外**，又不想自己造这套东西。会话可以跑在 Modal、Daytona、Islo、E2B、CoreWeave、Kubernetes、OpenShell、Boxlite 或 Databricks 的一次性沙箱里，既能从 CLI 启动，也能由服务端按会话托管分配。
- 你想要一套横跨多个 harness 的治理：策略可以在危险动作前暂停等批准、给花费封顶、限制 agent 能碰哪些工具，作用范围可以是整台服务器、某一个 agent，或某一次对话。
- 你想要对 agent 会话做实时协作——分享出去让同事和你的 agent 对话并围观它干活、在你的机器上一起开车，或者把对话 fork 出去各自往下走。

## 什么时候不选它

- 你就用一个 harness 并且用得挺好。元层只有在你真的要切换或组合时才值回票价，否则它只是一层间接。直接跑 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [Pi](pi.md)。
- 你现在就需要生产级稳定——它是 alpha。
- 你想要一个轻量安装。Omnigent 需要 Python 3.12+、`uv`、git、Node 22+ 带 npm 和 pnpm，原生终端包装层还要 `tmux`；在 Linux 上 `bubblewrap` 是**必需的**，因为那些包装层会把每个 agent 终端塞进一个 `bwrap` 操作系统沙箱，缺了这个二进制就起不来（macOS 用系统内建的 seatbelt 沙箱，不用额外装）。
- 你的问题是"一整家公司共用一套 agent 部署、按人隔离、要 Slack、要管理员设定安全姿态"——那是 [QM](qm.md)。
- 你要的是对 agent 运行做观测和评估，而不是编排它们——见 [Langfuse](langfuse.md) 和[观测与评估对比](../comparisons/observability-and-evals.md)。

## 能力形态

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| harness 编排 | 很强 | 六个具名 harness 加 YAML 自定义 agent，可在一个会话里混用 |
| 跨设备连续性 | 很强 | 终端、浏览器、手机和原生 macOS 应用共享同一份会话状态 |
| 沙箱触达 | 很强 | 九家云沙箱供应商，可从 CLI 启动，也可作为托管主机按会话分配 |
| 策略与审批 | 强 | 审批暂停、花费上限、工具限制，作用域可到服务器 / agent / 单次对话 |
| 协作 | 强 | 分享、实时围观、一起开车，或 fork 会话 |
| 模型自由度 | 强 | API key、消费级订阅、任意兼容网关，都是一等公民 |
| 本地隔离 | 强 | Linux 用 `bwrap`、macOS 用 seatbelt，作用在原生 harness 终端上 |
| 成熟度 | 弱 | 自己声明是 alpha |

## 可选扩展

安装是模块化的，这也挺能代表这个项目的形态：extras 覆盖**模型供应商**（Databricks、Bedrock、Vertex）、**沙箱供应商**（Modal、Daytona、Boxlite、CoreWeave、E2B、OpenShell、Kubernetes）、**SDK harness**（Antigravity、Copilot、Cursor、Agents SDK）以及**存储与记忆**（S3、Hindsight）。你按需装，不用把整个矩阵拉下来。

## 运维成本

中等。日常使用就是一个 CLI 加一个界面，一行安装脚本还会主动提出帮你把缺的前置装上。真正的成本是间接的：你的 agent 工作流中间多了一个 alpha 依赖；前置链横跨三个语言生态；出了问题时，责任可能在 Omnigent、在它拉起的那个 harness、也可能在底下的沙箱供应商。把版本钉死，并且保留一条"直接跑 harness"的退路。

## 结论

Omnigent 回答的是 2026 年一个真问题："指挥"这一层。多数开发者现在装了好几个 harness，却没有一层公共的东西来管审批、花费、沙箱和跨设备的会话连续性。它用不寻常的广度覆盖了这些——六个 harness、九家沙箱供应商、四种表面——并且配了一个策略引擎，正是这一点让它从便利层变成治理层。代价它自己写在包装上：alpha。把它当作你*监督* agent 的地方，还不要当作你依赖的地方。同一个元 harness 思路但面向整个组织而不是单个开发者的版本，见 [QM](qm.md)；想要完全归自己的单 harness 方案，见 [Pi](pi.md)、[jcode](jcode.md) 和 [OpenHarness](openharness.md)。路线级的横向对比见 [agent harness 框架](../comparisons/agent-harness-frameworks.md)。
