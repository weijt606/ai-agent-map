# GenericAgent

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/generic-agent.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](generic-agent.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GenericAgent is a self-evolving autonomous agent — start from a 3.3K-line seed and let it grow a personal skill tree on every task it solves.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | lsdefine (Fudan-affiliated team) |
| Route | Self-evolving autonomous agent |
| Open source | Yes (MIT, Python) |
| Best for | Researchers and operators who want an agent that crystallizes new skills on its own instead of relying on pre-bundled tools |
| Main cost | The "evolve as you go" model means no single static configuration — the agent's effective behavior shifts with usage |
| Official website | https://github.com/lsdefine/GenericAgent |
| GitHub repo | https://github.com/lsdefine/GenericAgent |

## When To Pick It

- You want an autonomous agent that learns new skills from completed tasks instead of being preloaded with a fixed toolset.
- You like minimal seed code (~3,300 lines) you can actually read end-to-end.
- You're interested in token-efficiency — the team reports ~6x lower token consumption than comparable frameworks for full system control.

## When Not To Pick It

- You want a stable, fixed tool surface; the skill tree growing under your agent is the point, not a side-effect.
- You need a turnkey product with a UI, dashboards, or managed cloud runs.
- You need strong audit / review of every action; the design favors autonomy over per-step approval.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| System-level control | Strong | Nine atomic tools cover browser, terminal, filesystem, devices |
| Self-evolution | Strong (defining trait) | Each solved task crystallizes into a reusable skill in the tree |
| Token efficiency | Strong (claimed) | ~6x lower consumption than comparable frameworks per the project's own benchmarks |
| Out-of-the-box features | Light by design | No bundled teams, dashboards, or managed runs |
| Stability | Evolving | January 2026 project, week-2 on this map's watchlist before being added |

## Operating Cost

Complexity is Medium. The seed itself is small enough to read and modify, but operating cost is unusual: because the agent grows its own skills, your second month of use will look different from your first. That's the value proposition, not a bug — but it does mean less predictable behavior than fixed-toolset agents.

## Bottom Line

GenericAgent occupies a niche the rest of this map doesn't really cover: autonomous agents that self-evolve from a small seed, rather than autonomous agents that come preloaded. If you're researching that pattern or want a small codebase you can fully own, GenericAgent is the strongest current candidate. For mainstream production use, AutoGPT or Agent Zero are still safer picks.
