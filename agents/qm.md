# QM

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/qm.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](qm.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: QM is Y Combinator's multiplayer agent harness for work — a self-hosted agent that lives in Slack and a web app, gives every person *and* every room its own scoped memory, files, keychain, permissions, crons, and durable sandbox, and runs that on a harness you choose (Pi, OpenCode, Codex, or Claude Code) rather than one it ships.

> **Multiplayer is the whole thesis.** Most agents are designed as a personal assistant that you can stretch to cover a company. QM inverts that: the unit is the *scope* — a person, a channel, a group message, a project — and each scope carries its own state and permissions. That is the difference between "one agent with everyone's context in it" and "one deployment, many isolated agents."

> **Contributions are human-written text, not code.** `CONTRIBUTING.md` asks you to describe a proposed change informally as a `.txt` or `.md` file in `adrs/`; if the maintainers agree, *they* implement it. The MIT license is real and you can fork freely, but the upstream tree is not a normal pull-request project. Read that before planning to carry patches.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Y Combinator (`yc-software/qm`, qm.ycombinator.com) |
| Route | Agent harness framework — multiplayer / organization-scoped |
| Open source | MIT |
| Implementation | TypeScript on Node, Fastify HTTP core; Postgres persistence; web UI in Vite + Lit; Slack plugin on Bolt |
| Harnesses | Pluggable — Pi, OpenCode, Codex, and Claude Code all drive the same core |
| Surfaces | Slack and a web app, with one identity and configuration across both |
| Best for | A startup or team that wants one self-hosted agent deployment serving everybody, with per-person isolation and admin-set security posture |
| Main cost | Days old, and it is a deployment to operate — Postgres, sandboxes, connector credentials, and your own cloud account |
| GitHub repo | https://github.com/yc-software/qm |

## When To Pick It

- You want an agent **for a company, not for a laptop**. Employees each get an isolated workspace and work without stepping on each other, and the same agent also participates in shared channels, group messages, and projects.
- You want the agent where the work already happens. QM ships Slack and a web app as first-class surfaces, and identity and configuration carry between them.
- You want to **stay off a single vendor's loop**. The core is harness-agnostic by design — Pi, OpenCode, Codex, and Claude Code are all drivers behind one interface, so a deployment is not tied to whoever wins the harness race. Admins choose which harnesses and models are even available.
- You want scoped, grantable skills rather than a single shared prompt directory: skills are owned by a scope, shareable by grant, promotable org-wide only with admin approval, and importable as skill packs from git repositories.
- You want background work as a built-in, not a bolt-on — crons and watches run while nobody is watching, per scope.
- You want to self-host in your own cloud account. `qm init --org <slug> --target <fly-or-aws>` scaffolds an org-owned deployment repository that depends on the published `@yc-software/qm` package, so you never need a source checkout to run it.

## When Not To Pick It

- You want a terminal coding agent. QM is not that; it is the layer *above* one. Use [Claude Code](claude-code.md), [Codex](codex.md), [Grok Build](grok-build.md), or [jcode](jcode.md) for the loop itself — and note QM can then drive several of them.
- You are one developer. The multiplayer machinery — Postgres, scopes, keychain views, admin posture, per-scope sandboxes — is overhead with no payoff at n=1. [Pi](pi.md) or [OpenHands](openhands.md) are the right size.
- You need something proven. The repo is days old; treat every operational claim as unverified until you have run it.
- You need to upstream your changes. See the contribution note above — [OpenHands](openhands.md), [Pi](pi.md), and [OpenHarness](openharness.md) take code.
- You want a hosted product with a support contract. Every QM deployment runs in the operator's own cloud account, and initialization deliberately does not generate deployment CI.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Multi-tenant scoping | Very strong | Person, channel, group message, and project each own memory, files, keychain view, permissions, crons, web apps, and a durable sandbox |
| Harness neutrality | Very strong | Pi, OpenCode, Codex, and Claude Code behind one interface; admins pick the allowed set |
| Chat-surface reach | Strong | Slack plugin (Bolt) supervised in-process by the core, plus a web app sharing identity and config |
| Approval and policy | Strong | Three org-level security postures that narrower scopes may only tighten, plus a predeclared command policy |
| Skills and sharing | Strong | Scope-owned skills, sharing by grant, admin-gated org promotion, git-imported skill packs |
| Scheduling | Strong | Crons and watches per scope |
| Durable environment | Strong | Each scope's sandbox is a persistent computer — installed tools stay installed |
| Operating maturity | Unproven | Days old at the time of writing |

## Architecture Worth Knowing

Every turn runs through a **headless core** that owns identity, policy, and scheduling; the agent loop is a swappable driver behind it. Postgres holds sessions, memory, and the queue. The agent is given a small, fixed tool surface, and one of those tools is `execute`, which runs commands inside the scope's own sandbox — its durable computer.

The web UI, admin panel, and public portal are **optional plugins** over the core's HTTP API, and Slack is an optional in-process plugin that the core starts and supervises. Everything company-specific — org config, custom tools and skills, sandbox image, infrastructure — lives in a separate **deployment directory** rather than in the core, and every substrate (harness, session store, sandbox, memory) sits behind an interface that production implementations swap in through a single wiring file. That separation is what makes the upgrade story plausible: your customizations are not diffs against the core.

## Security Posture

An organization picks one posture, and narrower scopes can only tighten it:

- **Strict** — every harness tool call pauses for human approval, apart from the two no-effect calls that end a turn.
- **Auto** (default) — a classifier screens provenance-labelled external data and tool results before they reach the model; a deployment can point that at its own screening proxy.
- **Dangerous** — no content screening and no pauses between tool calls.

The **predeclared command policy** — approval rules and hard denials for things like recursive deletes or destructive SQL — applies in every posture, Dangerous included. QM's stated model is the one local coding agents use: the agent acts as the person it works for, with their credentials and permissions, and everything it does is audited. `SECURITY.md` carries the threat model and the known limitations; read it rather than the summary above before deploying.

## Operating Cost

Medium–High, and it is deployment cost rather than learning cost. You are running a Postgres-backed service, per-scope sandboxes, connector credentials, Slack app configuration, and web sign-in, in your own Fly or AWS account. Initialization walks through that and ends with live verification, and the deployment repository never needs a source checkout — but nothing about it is a one-line install. If you want to keep the whole codebase in one place instead, the README documents a **private-fork** pattern (a plain bare clone pushed to a private repo, explicitly *not* GitHub's Fork button, because a fork of a public repo cannot be made private and shares an object network with it).

## Bottom Line

QM is the first entry on this map that treats "many people, one agent deployment" as the design problem rather than an afterthought, and it answers it with scopes: isolated state and permissions per person and per room, one admin-set security posture, and a core that does not care which harness runs the loop. It arrived very loud — roughly 11.4k stars and 1.3k forks in its first week — but it is days old, so the sensible read is *promising architecture, unproven operations*. If you want a single-user loop you own, see [Pi](pi.md), [jcode](jcode.md), or [OpenHands](openhands.md); for the other meta-harness in this map, which optimizes for one developer mixing harnesses in a single session rather than a company sharing one deployment, see [Omnigent](omnigent.md). For the route-level comparison, see [agent harness frameworks](../comparisons/agent-harness-frameworks.md).
