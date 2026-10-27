# ECC

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](ecc.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/ecc.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：ECC 是一个装进现有 coding agent 的插件，装进去的是一整套工程体系——71 个 subagent、311 个 skill、hooks、rules、本地记忆库和 AgentShield 配置扫描器——围绕 plan → test → implement → review → verify → remember → improve 这条循环组织。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Affaan Mustafa（README 自述为单人维护）和贡献者 |
| 路线 | Agentic skills 框架——跑在宿主 agent 里的 skills、hooks 与记忆层 |
| 仓库 | [`affaan-m/ECC`](https://github.com/affaan-m/ECC)——MIT，JavaScript；截至 2026-10-28 有 29.06 万 star |
| 开源 | 是（MIT）。托管的 ECC Tools GitHub App：免费档仅限公开仓库（每月 10 次分析）；**ECC Pro** $19/席位/月，覆盖私有仓库；Enterprise 联系销售 |
| 适配哪些 agent | [Claude Code](claude-code.md)（稳定、首要）；[Codex](codex.md) 和 Qoder（原生插件）；[Cursor](cursor.md)、[OpenCode](opencode.md)、GitHub Copilot CLI（beta）；Gemini、Zed、Antigravity、Qwen、[Hermes](hermes-agent.md)、[OpenClaw](openclaw.md)、Kimi 等（实验性适配）；[GitHub Copilot](github-copilot.md) Chat（仅指令文件） |
| 适合谁 | 想一次装好规划、TDD、新上下文评审、hook 强制检查和 agent 配置安全扫描的 Claude Code 用户 |
| 主要代价 | 要安装、要占上下文的面很大；README 自己就提醒不要叠装多种安装方式，并建议在意上下文占用时用选择性或 minimal profile |
| 当前版本 | 2.2.3（2026-10-01）；安装命令 `npx ecc-universal@2.2.3 setup` |
| 官网 | https://ecc.tools |

## 它怎么运作

ECC 把工作拆给五类组件，每类的上下文成本不同。**Skills**（311 个）是 TDD、安全评审、深度调研这类工作流，只在任务需要时加载。**Agents**（71 个）是有独立上下文和工具权限的 subagent，用来把规划、实现和评审隔开。**Rules** 是始终加载的规范，按语言选装。**Hooks** 在宿主事件上运行，不占模型上下文：会话摘要、持续学习，以及 GateGuard——它会在 `rm`、强制 `git checkout` 这类破坏性命令执行前先拦下来。**Instincts** 是从过往会话里学到的模式，带置信度存储，相关时调回。

核心之外还有两块。**Memory Vault**（`ecc memory`，2.2 系列加入）把长期上下文和跨 harness 的交接以本地 Markdown 存在 `.ecc/memory/` 下；README 明确说记忆是未经审核的上下文，不是可执行的策略。**AgentShield** 也以 `ecc-agentshield` npm 包单独发布，扫描 `CLAUDE.md`、settings、MCP 配置、hooks、agent 定义和 skills，查密钥泄露、权限问题、hook 注入和有风险的 MCP server。

**和 [Superpowers](superpowers.md) 的区别。** 两者都跑在宿主 agent 里，都带一套分阶段的开发流程。Superpowers 的基本工作流是 brainstorming → git worktree → 写计划 → 由 subagent 按 TDD 执行 → 代码评审 → 收尾分支，它的 README 里 hooks 只用来在会话开始时引导加载 skills。ECC 多出了 Superpowers README 没有描述的运行时部件：用于强制检查的 hooks、Memory Vault 与 instincts 构成的记忆、安全扫描器，以及一个收费的托管 GitHub App。代价是覆盖面换占用：ECC 的 README 专门有一节讲上下文窗口管理。

## 什么时候选它

- 你主要用 [Claude Code](claude-code.md)（README 标注的稳定首要 harness），想要一套现成体系，而不是自己拼 skills。
- 你希望检查由 prompt 之外的 hooks 强制执行（GateGuard、会话摘要），而不是靠模型可能会忘的提醒。
- 你想用 AgentShield 审计自己的 agent 配置（hooks、MCP server、权限、密钥）。
- 你在多个 harness 之间切换，想用一种本地、可检查的 Markdown 格式在它们之间交接。

## 什么时候不选

- 你想要一个独立 agent。ECC 自己不跑循环，它改变的是已装 harness 的行为。
- 你依赖 Cursor、OpenCode、Gemini 等非 Claude 适配并期待功能对齐。README 把它们标为 beta、实验性或仅指令，并说明不承诺与 Claude 功能完全对齐。
- 你想要一个精简的 skill 集。默认安装很大；在意上下文占用就用 `--profile minimal` 或选择性安装。
- 你在原生 Windows 上且需要持续学习或 Memory Vault 写入。README 列出这两项在原生 Windows 上都有未修复缺陷（#2489、#2626），并说依赖 shell 的功能需要 Git Bash 或 WSL。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| Skill 与 agent 目录 | 非常强 | 71 个 agent、311 个 skill、97 个命令 shim；skills 按需加载 |
| Hook 强制 | 强 | GateGuard 拦截破坏性命令；hooks 在模型上下文之外运行 |
| 记忆 | 中等 | Memory Vault（本地 Markdown，可选 MCP server）加学到的 instincts；调回内容按未审核上下文处理 |
| Agent 配置安全 | 强 | AgentShield 扫描 prompt、hooks、MCP 配置、权限、密钥和 agent 文件 |
| 跨 harness 对齐 | 不均衡 | Claude Code 稳定，Codex 和 Qoder 原生，其余为 beta 或实验性 |
| 独立运行时 | 不是目标 | 跑在宿主 agent 里 |

## 使用成本

复杂度：中到高。安装只要一条引导命令，但你引入的是一个大目录加运行时 hooks，README 用了整节篇幅讲不要重复安装、裁剪 rules、关掉不用的 MCP server 来控制上下文。开源层是 MIT；私有仓库要用托管 GitHub App 分析，价格是每席位每月 $19。

## 底线

ECC 把方法论、subagent、hooks、记忆和安全扫描器打包进了一个插件。如果你常驻 Claude Code、想要现成体系，选它；如果你只要方法论、不要运行时那一层，选 [Superpowers](superpowers.md)。无论哪个，上限仍由宿主 agent 的能力决定。

## 来源

- [ECC README](https://github.com/affaan-m/ECC#readme) · [Releases](https://github.com/affaan-m/ECC/releases) · [2.0.0 发布说明](https://github.com/affaan-m/ECC/blob/main/docs/releases/2.0.0/release-notes.md) · [LICENSE（MIT）](https://github.com/affaan-m/ECC/blob/main/LICENSE) · [ECC Tools 定价](https://ecc.tools/pricing) · [Superpowers README](https://github.com/obra/superpowers#readme)
