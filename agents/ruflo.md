# Ruflo

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/ruflo.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](ruflo.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Ruflo is a multi-agent orchestration platform for Claude Code — it takes the orchestration layer up to multi-machine federation, neural memory, and 100+ specialized agents.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | RuvNet (open source, rebranded from "Claude Flow") |
| Route | Workflow / orchestration layer for Claude Code |
| Open source | Yes (MIT) |
| Best for | Teams that need to run many specialized agents across machines with persistent memory and federated communication |
| Main cost | Significantly more surface area than [oh-my-claudecode](oh-my-claudecode.md) — federation, vector memory, web UI, neural architecture all live in the same project |
| GitHub repo | https://github.com/ruvnet/ruflo |

## When To Pick It

- You already use Claude Code and want to scale up to coordinated swarms across teams or machines.
- You want vector memory with HNSW indexing, federated agent communication, and a self-learning skill pipeline as one package.
- You want a web UI (flo.ruv.io) and a separate goal-planning interface (goal.ruv.io) alongside the CLI experience.

## When Not To Pick It

- You only need single-developer orchestration — [oh-my-claudecode](oh-my-claudecode.md) is lighter and matches that scope better.
- You want a vendor-managed platform; Ruflo is open source and self-hosted.
- You want a minimal, opinionated skill layer — Superpowers is the framework end, oh-my-claudecode is the curated end, and Ruflo is the federation/enterprise end of the same broader space.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Multi-agent coordination | Very strong | 100+ specialized agents, swarm coordination |
| Cross-machine federation | Very strong | Secure agent federation across machines and trust boundaries |
| Memory and retrieval | Strong | Vector memory with HNSW indexing, plus "SONA" neural architecture for self-learning patterns |
| Plugin integration | Strong | 32 Claude Code plugins; integrates with multiple LLM providers |
| Lightweight single-user use | Medium | Possible, but overkill compared to simpler workflow layers |

## Operating Cost

Complexity is High. Ruflo bundles federation, vector memory, neural-pattern learning, and a separate web UI into one project. The payoff scales with team and machine count — for a single developer, it is more apparatus than the task usually justifies.

## Bottom Line

Ruflo (formerly Claude Flow) is what an orchestration layer looks like when it grows toward the enterprise end: multi-machine federation, vector memory, a web UI, and 100+ specialized agents. Compared to [oh-my-claudecode](oh-my-claudecode.md), it is the heavier and more ambitious option in the same route. If you have a single developer running Claude Code locally, oh-my-claudecode is probably the right fit. If you have a team of developers running Claude Code across machines and need cross-machine coordination plus persistent memory, Ruflo is where to start looking.
