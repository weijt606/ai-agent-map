---
name: "Froge Code"
vendor: "Provisional mapping to Automagik Forge"
category: "automation"
open_source: true
complexity: "medium"
verification: "name-needs-confirmation"
last_reviewed: "2026-04-09"
description: "Provisionally mapped to Automagik Forge, a review-first coding automation platform built around tasks, attempts, and isolated worktrees."
description_zh: "当前暂按 Automagik Forge 进行映射，一套围绕任务、尝试和隔离 worktree 的 review-first coding automation 平台。"
homepage: "https://forge.automag.ik"
repo: "https://github.com/automagik-dev/forge"
---

# Froge Code

中文：
命名核验说明：在首轮公开资料检索中，没有找到一个能明确对应 “Froge Code” 的权威公共项目。因此这个页面当前按最可能的公开匹配项 Automagik Forge 来写，并保留显式说明，等待后续确认。

English:
Name verification note: the initial public research did not find a canonical project that clearly maps to “Froge Code”. This page is therefore written against the most likely public match, Automagik Forge, with the ambiguity kept explicit.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Requested Name | Froge Code |
| Provisional Mapping | Automagik Forge |
| Category | automation |
| Open Source | Yes |
| Complexity | Medium |
| Delivery Model | Self-hosted coding automation platform with UI and MCP |
| Homepage | https://forge.automag.ik |
| Repo | https://github.com/automagik-dev/forge |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Task orchestration | Strong | Built around a persistent kanban workflow with task, attempt, and review states. |
| Code execution | Strong | Work is executed through selected providers and agents inside isolated Git worktrees. |
| Multi-agent / multi-provider control | Strong | Public docs emphasize trying multiple providers and agents in parallel on the same task class. |
| Human oversight | Very strong | The system is explicitly review-first, with compare-and-choose workflows before merge. |
| Memory / persistence | Medium | Strong task persistence through kanban and attempts, but not primarily positioned as a deep autonomous memory system. |
| MCP integration | Strong | Public docs describe built-in MCP support for AI assistant control. |

## 最适合的使用场景 | Best Use Cases

- 想把 coding automation 做成“任务板 + 多次尝试 + 人工挑选结果”的流程。 Good for review-first coding automation built around tasks, multiple attempts, and human selection.
- 想比较不同 provider、不同 agent 在同一类任务上的效果。 Useful when you want to compare providers and agent behaviors on the same task.
- 希望把 AI 产出隔离在 worktree 中，降低直接污染主工作区的风险。 Good when you want isolated worktrees to reduce direct risk to the main workspace.

## 不适合的场景 | Not Suitable For

- 想要一个单独的 agent 自己从 issue 一路做到交付，不想管理任务板和 review。 Not a fit if you want one autonomous agent to take an issue all the way to delivery with minimal workflow overhead.
- 不想处理 provider、agent、attempt、review 这些操作概念。 Weak fit if you do not want to deal with providers, agents, attempts, and review workflow concepts.
- 需要高度自定义的状态机式 orchestration，而不是任务板式 orchestration。 Less suitable if you need highly custom state-machine orchestration rather than task-board orchestration.

## 复杂度判断 | Complexity

中文：
复杂度为 Medium。它不是最省心的选项，但它把“人保持控制权”这件事做得比较明确。你要付出的代价是需要维护任务结构、尝试策略和 review 节奏。

English:
Complexity is Medium. It is not the lowest-effort option, but it is explicit about keeping humans in control. The trade-off is that you must maintain task structure, attempt strategy, and review rhythm.

## 实战备注 | Real-World Usage Notes

- 这个系统的核心优势是流程可见性，不是单个 agent 的“神奇自主性”。 Its core strength is workflow visibility, not magical autonomy from a single agent.
- Git worktree 隔离非常适合多尝试并行和结果对比。 Git worktree isolation is useful for parallel attempts and result comparison.
- 真正的输出质量仍然高度依赖你接入的 provider 和 agent 配置。 Output quality still depends heavily on the provider and agent configuration you attach to it.