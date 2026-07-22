# Changelog

[English](CHANGELOG.md) | [中文](zh/CHANGELOG.md)

Structural milestones of the map, newest first. The heat tables are refreshed every Wednesday; those routine updates are recorded in the git history and in the "Market events" timeline in [agents/README.md](agents/README.md), not here.

## 2026-07-22 — jcode joins the harness route

- **New [jcode](agents/jcode.md) profile** (EN + zh) — the Rust multi-session coding harness (`1jehuang/jcode`, MIT, 10.6k) graduated from the watchlist to an in-scope profile after entering the weekly gain top 10 at #7. It joins the **agent harness framework** route alongside [Pi](agents/pi.md), the [harness comparison](comparisons/agent-harness-frameworks.md) (now six), the [selection matrix](comparisons/mainstream-agent-landscape.md), and the [coding-automation guide](use-cases/coding-automation.md). Coverage is now 55 profiles; `catalog.json` marks jcode in-scope.

## 2026-07-16 — Home-page slimdown, vendor refresh, and the market-events archive

- **README restructured for density**: the two Market Event sections collapsed into a three-bullet Market Pulse; the 50-row coverage table folded into four collapsible groups; heat-table side notes folded; the harness table moved to [comparisons/agent-harness-frameworks.md](comparisons/agent-harness-frameworks.md); navigation merged with a rankings entry added.
- **Vendor profiles caught up to July 2026**: Codex (merged into the ChatGPT app July 9, GPT-5.6-powered), Claude Code (Fable 5 / Opus 4.8 model arc), Cursor, GitHub Copilot, and GPT-5.5 (post-launch landscape).
- **New [Claude Fable 5](agents/claude-fable-5.md) profile** — Anthropic's Mythos-class tier joins the Frontier agentic model route.
- **New [market-events.md](market-events.md)** (EN + zh): the durable archive of structural events, with refreshed skills-wave numbers.

## 2026-07-16 — Rankings expansion: trend chart, category boards, vertical boards

- **Weekly rank-trend bump chart** (`assets/heat-trend-{en,zh}.svg`), embedded on both home pages and in [rankings/](rankings/README.md). Every weekly top-N window since 2026-04-11 was reconstructed from git history into `scripts/history.json`; the chart re-renders on every publish.
- **New [rankings/](rankings/README.md) section** (EN + zh mirror): Agent, Agent Infra, and Skill boards sorted by current total stars — the stock view that complements the gain-sorted home-page heat table.
- **Vertical rankings**: agents split into coding / general assistant / finance ([agent-verticals](rankings/agent-verticals.md)), skills into curated collections / academic & scientific research / finance / methodology ([skill-verticals](rankings/skill-verticals.md)).
- **Tracked repos 23 → 42**: Claude Code, Aider, Cline, Continue, OpenHands, SWE-agent, mini-swe-agent, OpenHarness, Goose, AutoGPT, LangChain, LangGraph, CrewAI, LlamaIndex, n8n, Letta, Open Interpreter, LiteLLM, Flowise join the weekly star tracking, with per-repo category metadata in `scripts/catalog.json`.
- **Pipeline**: all ranking tables regenerate automatically on publish; `validate.py` now cross-checks the history file against the README heat table and rejects stale charts.

## 2026-06-17 — Automated weekly-update mechanism

`scripts/` gains the weekly toolchain: `fetch-stars.py` (star fetcher + snapshot), `validate.py` (full integrity gate: links, bilingual parity, heat-table lockstep), `weekly-update.sh` (publish gate — nothing is pushed unless validation passes), the Wednesday playbook, and CI validation on every push.

## 2026-06-11 — Terminal coding-CLI comparison

New comparison page [Terminal Coding CLI Agents](comparisons/coding-cli-agents.md); Kimi Code, MiMoCode, and CoStrict profiles added.

## 2026-05-23 — Agent harness framework route

Harness frameworks split out as a first-class route (Pi, OpenHands, SWE-agent, mini-swe-agent, OpenHarness), with a spotlight table on the home page. OpenHuman, CodeGraph, and CLI-Anything profiled the same week.

## 2026-05-19 — The `.claude/skills` wave documented

The skills wave becomes a tracked market event: curated collections tracked as watchlist entries, the framework end profiled through Superpowers.

## 2026-04-24 — Framework batch + pixel-art banner

Continue, CrewAI, AutoGPT, LlamaIndex, n8n, and MemGPT profiled; heat tables gain the update timestamp and snapshot window; new pixel-art banner.

## 2026-04-11 — Heat ranking introduced

First weekly heat snapshot: hot-agent coverage table ranked by star gain.

## 2026-04-09 — Bootstrap

Bilingual (EN + zh) agent map bootstrapped: route taxonomy, first coding-agent profiles, comparisons and use-case scaffolding.
