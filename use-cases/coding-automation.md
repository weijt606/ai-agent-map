# How to Choose an Agent for Coding Automation

中文：
这个指南面向的不是“想试试看 agent 写代码”的读者，而是已经确定自己要把一部分软件工程流程交给 agent 的读者。问题不是“能不能写代码”，而是“该用什么 operating model 来写代码”。

English:
This guide is for readers who have already decided to hand part of their software engineering workflow to agents. The real question is not whether an agent can write code, but which operating model fits the job.

## 先看结论 | Quick Recommendations

| Your real need | Start with | Why |
| --- | --- | --- |
| 我想在本地终端或 IDE 里和 agent 紧密协作 | [Claude Code](../agents/claude-code.md) | Strong local agent loop with tools, MCP, instructions, and subagents |
| 我想把明确 coding 任务异步丢到云端 agent 去跑 | [Codex](../agents/codex.md) | Cloud sandboxes, isolated tasks, reviewable logs and test evidence |
| 我想用 Anthropic 的管理式 / 后台运行工作流 | [Claude Managed Agents](../agents/claude-managed-agents.md) | Better fit for detached or scheduled Claude workflows than interactive local work |
| 我想在编辑器里强审批、强控制地用 agent | [Cline](../agents/cline.md) | Editor-native, approval-first, browser + terminal + MCP capable |
| 我想在 VS Code / GitHub 工作流里本地和云端切换 | [GitHub Copilot](../agents/github-copilot.md) | Local, CLI, and cloud agent targets in one workflow |
| 我想要一个开源、自托管、接近 Devin 式的软件工程 agent | [OpenHands](../agents/openhands.md) | CLI, local GUI, cloud, and enterprise deployment paths |
| 我想直接把明确任务交给 agent 执行 | [Devin](../agents/devin.md) | Execution-first, issue-to-PR style workflow |
| 我想保留人工控制、任务板、对比多个 agent 输出 | [Froge Code](../agents/froge-code.md) | Review-first automation with multiple attempts and isolated worktrees |
| 我想自托管一个长期使用的 coding assistant，还需要 memory、skills、messaging | [Hermes Agent](../agents/hermes-agent.md) | Self-hosted agent environment with delegation, memory, and toolsets |
| 我想把 coding automation 接到多渠道、多设备和更强的 runtime 控制面 | [OpenClaw](../agents/openclaw.md) | Runtime and gateway model with channels, tools, and routing |
| 我不是要买现成 agent，我是要快速搭一个自定义 agent | [LangChain](../agents/langchain.md) | Prebuilt agent abstractions and integrations |
| 我不是要买现成 agent，我是要自己搭 stateful agent workflow | [LangGraph](../agents/langgraph.md) | Build your own stateful orchestration system |

## 决策逻辑 | Decision Logic

1. 如果你想要“一个 agent 直接干活”，优先看 [Devin](../agents/devin.md)。如果你想要“一个系统管理多个 agent 和多次尝试”，优先看 [Froge Code](../agents/froge-code.md) 或 [LangGraph](../agents/langgraph.md)。

2. 如果你想在本地工作流里强交互、强控制，优先看 [Claude Code](../agents/claude-code.md) 或 [Cline](../agents/cline.md)。如果你想异步后台执行，优先看 [Codex](../agents/codex.md) 或 [GitHub Copilot](../agents/github-copilot.md) 的 cloud path。

3. 如果你想要尽量少运维、快速验证价值，优先看托管型执行 agent，例如 [Devin](../agents/devin.md)、[Claude Code](../agents/claude-code.md) 或 [Codex](../agents/codex.md)。

4. 如果你需要自托管、模型可替换、toolsets 可控、长期运行，优先看 [OpenHands](../agents/openhands.md)、[Hermes Agent](../agents/hermes-agent.md)、[OpenClaw](../agents/openclaw.md) 或 [LangGraph](../agents/langgraph.md)。

5. 如果你的核心要求是“人必须 review 后再 merge”，优先看 [Froge Code](../agents/froge-code.md)、[Codex](../agents/codex.md)、[GitHub Copilot](../agents/github-copilot.md) 或 [Cline](../agents/cline.md)。如果你更关心“agent 自己从头做到尾”，优先看 [Devin](../agents/devin.md)。

6. 如果你真正需要的是长期状态、失败恢复、审批流和复杂 workflow，而不是单次代码生成，优先看 [LangGraph](../agents/langgraph.md)。

7. 如果你除了 coding 之外，还想接消息渠道、设备控制、定时任务或日常助手能力，优先看 [Hermes Agent](../agents/hermes-agent.md) 或 [OpenClaw](../agents/openclaw.md)。

## 推荐 Agent 说明 | Recommended Agents

### Claude Code

- 适合什么：本地终端和 IDE 中的高频 coding 协作。 Best for interactive local coding workflows in the terminal and IDE.
- 为什么选它：MCP、CLAUDE.md、subagents、scheduled tasks 和跨表面工作流组合得比较完整。 It combines instructions, MCP, subagents, and cross-surface workflows in a unified agent loop.
- 代价是什么：仍然需要你管理权限、环境和操作节奏。 The trade-off is that you still own permissions, environment, and operating rhythm.

### Claude Managed Agents

- 适合什么：后台、定时、管理式 Claude 工作流。 Best for detached, scheduled, or managed Claude execution workflows.
- 为什么选它：相比纯本地交互，更适合把任务交给云端或管理式执行路径。 It is better suited to managed or cloud execution than tight local interaction.
- 代价是什么：名称和产品边界目前分散在 Anthropic 多个文档概念里，需要读者理解其映射关系。 The trade-off is that Anthropic currently describes this through multiple concepts rather than one simple product page.

### Codex

- 适合什么：异步丢任务、独立云端环境执行、回来看结果和日志。 Best for asynchronous task delegation into isolated cloud environments.
- 为什么选它：任务隔离、日志和测试引用、PR 导向 review 很清晰。 It offers clear isolation, review evidence, and PR-oriented results.
- 代价是什么：本地即时配合感弱于编辑器内 agent。 The trade-off is less immediacy than editor-native agents.

### GitHub Copilot

- 适合什么：以 VS Code 和 GitHub 为中心的本地到云端 handoff。 Best for VS Code and GitHub-centric local-to-cloud agent workflows.
- 为什么选它：本地 agent、CLI、cloud agent 和自定义 agent 放在同一套工作流里。 It unifies local, CLI, cloud, and custom agent workflows.
- 代价是什么：在非 VS Code / GitHub 场景下吸引力会下降。 The trade-off is weaker value outside the GitHub and VS Code ecosystem.

### Cline

- 适合什么：想要 agent 很强，但每一步都保留人工批准。 Best for powerful agent workflows with explicit human approval.
- 为什么选它：终端、浏览器、编辑器和 MCP 结合得强，同时保持 approval-first。 It combines terminal, browser, editor, and MCP access while staying approval-first.
- 代价是什么：高频审批会带来摩擦。 The trade-off is approval friction.

### OpenHands

- 适合什么：想用开源方式获得较完整的软件工程 agent。 Best for teams wanting a more complete open-source software engineering agent.
- 为什么选它：CLI、GUI、Cloud、Enterprise 和 SDK 路线比较完整。 It spans CLI, GUI, cloud, enterprise, and SDK deployment modes.
- 代价是什么：本地运行通常依赖 Docker 和较重的环境准备。 The trade-off is heavier setup and runtime requirements.

### Devin

- 适合什么：明确 issue、缺陷修复、功能小步交付。 Best for well-scoped engineering execution.
- 为什么选它：你买的是“直接执行能力”，不是框架自由度。 You are buying direct execution, not framework flexibility.
- 代价是什么：闭源、托管、控制边界较少。 The trade-off is less control and a managed, closed model.

### Froge Code

- 适合什么：任务板式 coding automation、多人协作、对比不同 provider / agent 的结果。 Best for task-board-driven coding automation with review and comparison.
- 为什么选它：它把“多尝试 + worktree 隔离 + 人工挑选”做成了一等工作流。 It makes multiple attempts, worktree isolation, and human selection first-class.
- 代价是什么：流程更重，真正产出依赖接入的 provider。 The trade-off is a heavier workflow and dependence on attached providers.

### Hermes Agent

- 适合什么：长期使用的自托管 coding / research / ops assistant。 Best for a long-lived self-hosted coding, research, or ops assistant.
- 为什么选它：memory、skills、toolsets、gateway 和 subagents 组合得比较完整。 It combines memory, skills, toolsets, gateway integrations, and subagents in one environment.
- 代价是什么：需要持续管理权限、记忆和技能。 The trade-off is ongoing operational curation.

### OpenClaw

- 适合什么：不仅要写代码，还要接消息渠道、浏览器、设备节点和定时任务。 Best when coding automation is only one part of a broader assistant runtime.
- 为什么选它：runtime、gateway、channels、nodes 和 tools 是它的强项。 Its strength is the runtime plus gateway, channels, nodes, and tool model.
- 代价是什么：对纯代码任务可能偏重。 It can be too heavy for code-only workflows.

### LangGraph

- 适合什么：自己搭长期运行的 coding agent system 或内部 agent platform。 Best for building your own long-running coding agent system.
- 为什么选它：checkpoint、state、approval 和 recovery 是框架级能力。 Checkpointing, state, approval, and recovery are framework-level strengths.
- 代价是什么：你要自己承担系统设计和运维。 The trade-off is that you own system design and operations.

### LangChain

- 适合什么：快速搭出自定义 agent，而不是从更低层 orchestration 开始。 Best for quickly building custom agents without starting from lower-level orchestration.
- 为什么选它：提供高层 agent 抽象、模型集成和快速起步路径。 It gives you higher-level agent abstractions, integrations, and a fast start path.
- 代价是什么：如果你需要非常精细的状态机和长期执行控制，通常还是要落到 LangGraph。 The trade-off is that advanced stateful orchestration still points you back to LangGraph.

## 关键取舍 | Trade-Offs

| Agent | Main advantage | Main trade-off |
| --- | --- | --- |
| Claude Code | Strong local-first agent loop with instructions and MCP | Still interactive and permissions-heavy |
| Claude Managed Agents | Better fit for managed or scheduled Anthropic workflows | Product boundary is less simple than a single local tool |
| Codex | Strong cloud isolation and review evidence | Less editor-native and more asynchronous |
| GitHub Copilot | One workflow across local, CLI, and cloud agents | Best inside the VS Code and GitHub ecosystem |
| Cline | Approval-first power inside the editor | Higher interaction overhead |
| OpenHands | Broad open-source software engineering surface | Heavier setup and runtime requirements |
| Devin | Fast path to direct execution | Less control, closed-source, managed boundary |
| Froge Code | Human-controlled review workflow | Heavier process and dependency on attached providers |
| Hermes Agent | Strong self-hosted environment with memory and delegation | More curation and permissions management |
| OpenClaw | Rich runtime with channels, tools, and device integrations | Can be heavier than needed for pure coding work |
| LangChain | Fastest path to custom agent assembly | Less precise control than lower-level orchestration |
| LangGraph | Maximum flexibility for custom workflows | Highest engineering and ops burden |

## 常见误判 | Common Mistakes

- 你需要的是现成 agent，却选了 framework。 Choosing a framework when you really need a ready-to-run agent.
- 你需要的是 review-first 流程，却选了 autonomy-first 执行器。 Choosing an autonomy-first executor when your real requirement is review-first control.
- 你需要的只是代码自动化，却选了带大量外部渠道和 runtime 能力的系统。 Choosing a broad runtime platform when you only need coding automation.
- 忽略了权限、密钥、代码暴露和测试责任。 Ignoring permissions, secrets, code exposure, and validation responsibilities.

## 一个简单的选型原则 | One Simple Rule

中文：
尽量选择“能解决你当前问题的最小 agent surface”，不要为了未来可能用到的能力，一开始就把 runtime、platform 和 orchestration 全部背上。

English:
Choose the smallest agent surface that solves your current problem. Do not adopt a full runtime, platform, and orchestration stack on day one for capabilities you might never need.