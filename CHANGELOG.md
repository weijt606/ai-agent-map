# Changelog

[English](CHANGELOG.md) | [中文](zh/CHANGELOG.md)

Structural milestones of the map, newest first. The heat tables are refreshed every Wednesday; those routine updates are recorded in the git history and in the "Market events" timeline in [agents/README.md](agents/README.md), not here.

## 2026-09-06 — Four backfills: the harness with no core, and China's desktop agent category

A coverage scan found gaps that were not judgment calls but misses. Four new profiles (EN + zh), taking the map to 68:

- **New [DeepSeek Harness](agents/deepseek-harness.md)** (`deepseek-ai/deepseek-harness`, MIT, TypeScript) — published August 13 2026 and at **213.8k stars / 25.1k forks three weeks later**, which makes it the largest thing this map has ever failed to notice. It is a fourth shape on the [harness route](comparisons/agent-harness-frameworks.md): not a loop you fork, not a meta-harness, not a harness behind HTTP, but **a harness with no privileged core** — the model adapter, tool registry, session log and the agent loop itself are all plugins replaceable from configuration, on the Cordis kernel. Carries `tracked: false` for one window.
- **New [ZCode](agents/zcode.md)** (Zhipu) — the tool a GLM-first developer actually opens. A desktop agentic development environment whose primary object is a task rather than a file, with long-horizon "Goal" runs and remote control from WeChat, Feishu, or Telegram. Placed on direct execution rather than the editor route for that reason.
- **New [WorkBuddy](agents/workbuddy.md)** (Tencent) and **[Kimi Work](agents/kimi-work.md)** (Moonshot) — the same agent loop aimed at desktop knowledge work. Kimi Work is the sharpest case in this directory: the vendor states its core is [Kimi Code](agents/kimi-code.md), so a coding agent's loop, strengths, and failure modes now run over your mounted folders and the browser you are logged into.

Structural consequences: [market-events](market-events.md) gains two backfilled entries (the DeepSeek release, and the March–June opening of China's desktop agent category); [agent harness frameworks](comparisons/agent-harness-frameworks.md) and [mainstream landscape](comparisons/mainstream-agent-landscape.md) carry the new rows; the route tables gain ZCode on direct execution, DeepSeek Harness on the harness route, and WorkBuddy and Kimi Work on general-purpose autonomous.

Two things this entry states rather than hides. The DeepSeek repository sat off these boards for three weeks, which is a scanning failure and is recorded as one in the market-events entry. And three of the four new profiles are **closed source with authorized access to local files** — the desktop agent category is closed by default, which is the opposite of the norm on the open side of this map, and the profiles say so.

## 2026-09-06 — The frontier model route catches up, two generations at once

The model layer had moved twice on each side since this map last wrote it down, and the route was pointing at superseded entries. Two new profiles (EN + zh), taking the map to 64:

- **New [Claude Opus 5](agents/claude-opus-5.md)** (July 24 2026) — the entry this route was missing: not the ceiling, but the model Claude-based agents actually run on. Holds the Opus price ($5/$25) while landing within 0.5% of Fable 5 on CursorBench 3.2, with 1M context as both default *and* maximum. It replaced Opus 4.8 as Claude Code's dependable default, which several pages here still described incorrectly.
- **New [GPT-6 Astra](agents/gpt-6-astra.md)** (September 3 2026) — OpenAI's current ceiling, and the first frontier model this map has recorded whose *public* version is deliberately restricted (it refuses part of its own cybersecurity capability, with advanced access behind Daybreak Blue). Codex CLI `rust-v0.153.4` made it the bundled default the next day, so the restriction now sits under a product default.
- **[Claude Fable 5](agents/claude-fable-5.md) updated to Fable 5.1 / Mythos 5.1** (September 1 2026) — same $10/$50 sticker, cache reads cut 75% to $0.25/M. The profile keeps its original path so existing links hold.
- **[GPT-5.5](agents/gpt-5.5.md) reframed as the lineage reference** — its post-launch table now runs GPT-5.5 → GPT-5.6 → Astra alongside Opus 4.8 → Fable 5 → Sonnet 5 → Opus 5 → Fable 5.1.

Structural consequences: [cost & benchmarks](comparisons/cost-and-benchmarks.md) is rebuilt on first-party price pages and gains a **cache-read column**, because with both ceilings at an identical $10/$50 the sticker stopped being the differentiator; [market-events](market-events.md) records three new entries (Opus 5, Fable 5.1, Astra); the route tables in [README](README.md) and [agents/](agents/README.md) now separate the ceiling from the default tier under it, since those are two different decisions.

Two sourcing notes the map is deliberately holding: the Artificial Analysis Coding Agent Index has no figure this map will copy for Astra, Fable 5.1, or Opus 5, so those cells stay dashed rather than filled from third-party leaderboards; and the "95% SWE-bench Verified" figure circulating for Fable 5.1 is a third-party number — Anthropic published SWE-bench Pro 81.2, which is what is recorded here.

## 2026-08-12 — The weekly refresh stops drifting

Tooling only; no content surfaces changed. The weekly flow ran two independent GitHub fetches — one in `check` (whose numbers get hand-written into the heat tables) and another in `publish` (which stamps the snapshot that drives `rankings/` and the SVGs). Stars moved between them, so every refresh ended with the tables and the generated boards disagreeing by a few stars, and a manual reconciliation pass afterwards.

- **`check` now records its fetch** to `scripts/.fetch-cache.json` (gitignored), and **`publish` reuses that same-day fetch** instead of calling the API again. The stamped snapshot and the heat tables are the same numbers by construction. Slugs added to `tracked-repos.txt` between the two calls — exactly what the playbook's pending-pickup step does — are fetched individually and merged in; a cache from an earlier date is ignored as stale. `publish "<msg>" --refetch` forces a fresh fetch.
- **`validate.py` gained a `[drift]` check** comparing the README heat gains against the fetch that was actually stamped (`history.json`'s newest `raw` entry). The existing history cross-check could never catch this, because its window is copied *from* the README and so agrees with it by construction. This is the backstop for the paths that still fetch twice (`--refetch`, or publishing on a later day than the check).
- Negative weekly gains now print as `-1,234` rather than `+-1,234`.

## 2026-08-05 — The meta-harness layer, and a dedicated review agent

Three new profiles (EN + zh), taking the map to 60:

- **New [QM](agents/qm.md)** (`yc-software/qm`, MIT) — Y Combinator's multiplayer agent harness for Slack and the web. The map's first entry designed around *many people sharing one deployment*: a scope per person and per room, each with its own memory, files, keychain, permissions, crons, and durable sandbox, over a core that runs Pi, OpenCode, Codex, or Claude Code interchangeably.
- **New [Omnigent](agents/omnigent.md)** (`omnigent-ai/omnigent`, Apache-2.0) — the same meta-harness idea scoped to one developer: several harnesses inside a single session, following you across terminal, browser, phone, and desktop, with policy and nine cloud sandbox providers. Self-declared alpha.
- **New [Open Code Review](agents/open-code-review.md)** (`alibaba/open-code-review`, Apache-2.0) — Alibaba's two-year internal review assistant, open-sourced. A deterministic pipeline wrapped around the model, trading recall for precision, with a delegation mode that runs on your existing coding agent's LLM.

Structural consequences: [agent harness frameworks](comparisons/agent-harness-frameworks.md) gains a **meta-harness** section separating layers that *run* harnesses from harnesses themselves; [market-events](market-events.md) records the pattern's arrival; the [capability matrix](capabilities/matrix.md), [mainstream landscape](comparisons/mainstream-agent-landscape.md), and [coding automation](use-cases/coding-automation.md) all carry the new rows. Grok Build was also backfilled into the mainstream landscape matrix, and the market-events entries were re-sorted into the newest-first order the page claims.

## 2026-07-22 — Route map and top-10 composition charts

Two new home-page visuals (EN + zh), same design language as the bump chart:

- **Route ecosystem map** (`assets/route-map-{en,zh}.svg`, from `scripts/render-route-map.py`) — the "First Cut" table drawn as an actual map: 12 routes as cards grouped into four decisions, each naming its flagships. Embedded at the top of the route section on both home pages; regenerated manually when routes change (playbook step 5).
- **Top-10 composition chart** (`assets/heat-composition-{en,zh}.svg`, from `scripts/render-composition.py`) — stacked bars of weekly top-10 seats by layer (agent / infra / skill), computed from `history.json` + `catalog.json`. The quantitative form of the skills-wave story; wired into `publish` so it refreshes weekly, and into `validate.py`'s SVG freshness gate.

## 2026-07-22 — Capability matrix, cost/benchmark, and memory-approaches pages

Three additive comparison surfaces that move the map beyond popularity, without touching the existing route/coverage structure:

- **New [capability matrix](capabilities/matrix.md)** (EN + zh) — applies the nine [capability dimensions](capabilities/README.md) to ~40 projects side by side, scored core (●) / support (◐) / limited (○) / not-a-goal (—), grouped by route. Finally uses the capabilities vocabulary that had been defined but never applied at scale.
- **New [cost & benchmarks](comparisons/cost-and-benchmarks.md)** (EN + zh) — frontier-model capability (Artificial Analysis Coding Agent Index, SWE-Bench Pro) vs per-token price, plus how each coding agent bills (open-source BYO / subscription / metered credits / managed seat). Reuses the numbers already established in the vendor profiles.
- **New [memory approaches](comparisons/memory-approaches.md)** (EN + zh) — sorts the map's memory-carrying projects by *how* they remember (self-editing, passive semantic, file/keyword, code knowledge graph, personal-data tree, long-lived runtime), tying together jcode, MiMoCode, Letta, CodeGraph, OpenHuman, Hermes, and Mercury.

Both comparison pages are linked from [comparisons/](comparisons/README.md); the matrix from [capabilities/](capabilities/README.md).

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
