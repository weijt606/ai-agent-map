# Omnigent

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/omnigent.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](omnigent.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Omnigent is an open-source **meta-harness** — one orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and agents you define yourself, so you can mix several harnesses inside a single session, move that session between terminal, browser, phone, and desktop, run it in a disposable cloud sandbox, and put approval and spend policies in front of all of it.

> **Alpha, and it says so.** The repository badges its own status as `alpha`. The surface area is unusually large for a project two months old — nine sandbox providers, half a dozen harnesses, a desktop app — so treat breadth as intent rather than as settled behavior, and pin versions.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Omnigent (`omnigent-ai/omnigent`, omnigent.ai) |
| Route | Agent harness framework — meta-harness / orchestration over other harnesses |
| Open source | Apache-2.0 |
| Implementation | Python 3.12+ (`uv tool install omnigent`, Homebrew tap, or install script) |
| Harnesses | Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, plus custom agents defined in YAML |
| Models | First-party API keys, a Claude or ChatGPT subscription, or any compatible gateway |
| Best for | A developer or small team who wants several harnesses in one supervised session, reachable from any device and optionally running in a cloud sandbox |
| Main cost | Alpha status, a heavy prerequisite chain (uv, Node, tmux, `bwrap` on Linux), and one more layer between you and the agent |
| GitHub repo | https://github.com/omnigent-ai/omnigent |

## When To Pick It

- You already use more than one harness and are tired of them being separate worlds. Omnigent puts Claude Code, Codex, Cursor, OpenCode, Hermes, and Pi in the *same* session, so you can split a task across the ones that are good at different things — or ask one agent to review another's work.
- You want the session, not the machine, to be the unit. Start in the terminal, continue in the browser, pick it up on your phone; messages, sub-agents, terminals, and files stay in sync. There is a native macOS desktop app.
- You want to run agents **off your laptop** without building that yourself. Sessions can run in disposable sandboxes on Modal, Daytona, Islo, E2B, CoreWeave, Kubernetes, OpenShell, Boxlite, or Databricks, launched from the CLI or provisioned per session by the server.
- You want governance that spans harnesses: policies pause for approval before risky actions, cap spend, or restrict which tools an agent can reach, and they attach to the whole server, one agent, or a single chat.
- You want live collaboration on an agent session — share it so teammates can chat with your agent and watch it work, co-drive it on your machine, or fork the conversation and continue separately.

## When Not To Pick It

- You use exactly one harness and are happy. The meta-layer earns its keep only when you are genuinely switching or combining; otherwise it is indirection. Run [Claude Code](claude-code.md), [Codex](codex.md), or [Pi](pi.md) directly.
- You need production stability now — it is alpha.
- You want a thin install. Omnigent needs Python 3.12+, `uv`, git, Node 22+ with npm and pnpm, and `tmux` for the native terminal wrappers; on Linux `bubblewrap` is **mandatory**, because those wrappers put each agent terminal in a `bwrap` OS sandbox and the harness fails to start without it (macOS uses the built-in seatbelt sandbox).
- Your problem is a whole company sharing one agent deployment with per-person isolation, Slack presence, and an admin-set security posture — that is [QM](qm.md).
- You want observability and evaluation of agent runs rather than orchestration of them — see [Langfuse](langfuse.md) and the [observability & evaluation comparison](../comparisons/observability-and-evals.md).

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Harness orchestration | Very strong | Six named harnesses plus YAML-defined custom agents, mixable within one session |
| Cross-device continuity | Very strong | Terminal, browser, phone, and a native macOS app share one session state |
| Sandbox reach | Very strong | Nine cloud sandbox providers, from the CLI or provisioned per session as managed hosts |
| Policy and approval | Strong | Approval pauses, spend caps, and tool restrictions scoped to server, agent, or chat |
| Collaboration | Strong | Share, watch live, co-drive, or fork a session |
| Model freedom | Strong | API key, consumer subscription, or any compatible gateway, all first-class |
| Local isolation | Strong | `bwrap` on Linux, seatbelt on macOS, applied to native harness terminals |
| Maturity | Weak | Self-declared alpha |

## Optional Extras

Installation is modular, which is a fair proxy for the project's shape: extras cover **model providers** (Databricks, Bedrock, Vertex), **sandbox providers** (Modal, Daytona, Boxlite, CoreWeave, E2B, OpenShell, Kubernetes), **SDK harnesses** (Antigravity, Copilot, Cursor, Agents SDK), and **storage and memory** (S3, Hindsight). You install the ones you need rather than pulling the full matrix.

## Operating Cost

Medium. Day-to-day use is a CLI plus a UI, and the one-line installer will offer to set up the missing prerequisites for you. The real costs are indirect: an alpha dependency in the middle of your agent workflow, a prerequisite chain that spans three language ecosystems, and a debugging story where a failure could belong to Omnigent, to the harness it launched, or to the sandbox provider underneath. Version-pin, and keep a path back to running the harness directly.

## Bottom Line

Omnigent is the "conductor" answer to a real 2026 problem: most developers now have several harnesses installed and no common layer for approval, spend, sandboxing, or session continuity across them. It covers that with unusual breadth — six harnesses, nine sandbox providers, four surfaces — and pairs it with a policy engine, which is the part that turns a convenience layer into a governance one. The catch is stated plainly on the tin: it is alpha. Adopt it as the place you *supervise* agents from, not yet as the place you depend on. For the same meta-harness idea aimed at a whole organization instead of one developer, see [QM](qm.md); for single-harness alternatives you own outright, see [Pi](pi.md), [jcode](jcode.md), and [OpenHarness](openharness.md). For the route-level comparison, see [agent harness frameworks](../comparisons/agent-harness-frameworks.md).
