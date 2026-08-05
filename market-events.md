# Market Events

[English](market-events.md) | [中文](zh/market-events.md)

Structural events that reshaped agent selection — model releases, product mergers, and waves — newest first. The weekly play-by-play lives in the "Market events" timeline in [agents/README.md](agents/README.md); this page keeps the durable records.

## July–August 2026 — The Meta-Harness Appears

Two projects landed the same idea from opposite ends within weeks of each other. **[QM](agents/qm.md)** (`yc-software/qm`, MIT) — Y Combinator's *multiplayer* agent for Slack and the web — reached **~11.4k stars and 1.3k forks in its first seven days**, and **[Omnigent](agents/omnigent.md)** (`omnigent-ai/omnigent`, Apache-2.0) passed 8k. Neither ships an agent loop. Both are layers that run *other* harnesses — Pi, OpenCode, Codex, Claude Code, Cursor, Hermes — behind one interface, and add what a bare loop leaves out: identity, approval policy, spend caps, sandboxing, scheduling, and session continuity.

**Impact on selection:** for two years the harness question was "which one do I fork." These projects assume the answer is "several, and that is fine" — which is a bet that the loop itself is commoditizing and the durable value sits in the governance layer above it. If that bet is right, "which harness" becomes a reversible decision and the important choice moves up a level. Note the two split cleanly on unit of account: QM's is an **organization** (a scope per person and per room, one admin-set security posture, self-hosted in your own cloud), Omnigent's is a **developer** (one session following you across terminal, browser, phone, and desktop, across nine cloud sandbox providers). Also note the maturity: QM is days old and Omnigent is self-declared alpha, so this is a shape worth tracking, not yet a layer worth depending on. QM carries the same governance caveat the map flagged for Grok Build in a different form — the license is MIT, but contributions are accepted as *written proposals*, not code. Details: [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [agent harness frameworks](comparisons/agent-harness-frameworks.md).

Sources: [yc-software/qm](https://github.com/yc-software/qm), [qm.ycombinator.com](https://qm.ycombinator.com), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [omnigent.ai](https://omnigent.ai).

## July 14 2026 — xAI Ships Grok Build, And Open Source Splits In Two

SpaceXAI (xAI) released **[Grok Build](agents/grok-build.md)** (`grok`), a Rust terminal coding agent in the Claude Code mold — full-screen TUI, headless mode for CI, and an Agent Client Protocol server so editors can drive it, plus MCP servers, skills, plugins, hooks, and sandboxing. It reached **23.2k stars and 4.4k forks within 15 days**, the fastest debut this map has recorded. Every major model vendor now ships a first-party coding CLI.

**Impact on selection:** the vendor-CLI field is now essentially complete (Anthropic, OpenAI, Moonshot, Xiaomi, xAI), so "which coding CLI" is increasingly downstream of "which model do you pay for." The more durable lesson is a governance split the map now has to make explicit: Grok Build is **Apache-2.0 but closed to contributions** — a periodic export from a private monorepo, with in-tree ports of `openai/codex` and `sst/opencode` tool code. Source-available and community-built have visibly diverged, and the LICENSE file no longer tells you which one you are getting. Details: [Grok Build](agents/grok-build.md), [terminal coding CLI comparison](comparisons/coding-cli-agents.md).

Sources: [xai-org/grok-build](https://github.com/xai-org/grok-build), [x.ai/cli](https://x.ai/cli), [docs.x.ai/build/overview](https://docs.x.ai/build/overview).

## July 9 2026 — Codex Merges Into ChatGPT; GPT-5.6 Ships

OpenAI merged the standalone Codex app into the ChatGPT desktop app (macOS/Windows): Codex is now a dedicated coding entry next to Chat and the new agentic **ChatGPT Work** mode, available on every plan including Free. The same day, **GPT-5.6** replaced GPT-5.5 across ChatGPT, Codex, and the API in three tiers — Sol ($5/$30 per M tokens), Terra ($2.5/$15), Luna ($1/$6) — plus an Ultra multi-agent setting. Codex reports 5M+ weekly users, over 1M of them working outside software development.

**Impact on selection:** the "which coding agent" question on the OpenAI side collapsed into "how do you use ChatGPT" — the product boundary moved, not just the capability. GPT-5.6 Sol leads the Artificial Analysis Coding Agent Index (80, vs Fable 5 77.2, GPT-5.5 76.4, Opus 4.8 72.5) at GPT-5.5's old price, making GPT-5.5 a legacy choice. Details: [Codex](agents/codex.md), [GPT-5.5](agents/gpt-5.5.md).

Sources: [OpenAI Codex changelog](https://learn.chatgpt.com/docs/changelog), [GPT-5.6 announcement](https://openai.com/index/gpt-5-6/), [Axios](https://www.axios.com/2026/07/09/ai-openai-gpt-release).

## June 9 2026 — Claude 5 Family: Fable 5 And The Mythos Tier

Anthropic released **Claude Fable 5** and **Claude Mythos 5** — the same underlying model, with Fable 5 generally available (with added safety measures) and Mythos 5 restricted to approved organizations. Mythos is a new tier above Opus. Fable 5 became the default Claude Code model for Pro/Max, was pulled worldwide June 12 under short-lived US export controls, returned July 1 behind stricter safety classifiers (blocked requests fall back to Opus 4.8), and moved to metered usage credits on July 7. Two weeks earlier (May 28), **Opus 4.8** had already fixed Opus 4.7's tool-calling issues and shipped Dynamic workflows.

**Impact on selection:** the Anthropic model layer became a two-tier budget decision — Fable 5 credits for the hardest work, Opus 4.8 as the dependable default. Details: [Claude Fable 5](agents/claude-fable-5.md), [Claude Code](agents/claude-code.md).

Sources: [Anthropic announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5), [Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5), [Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8).

## May 2026 (ongoing) — The `.claude/skills` Wave

The wave that broke into GitHub trending in mid-May keeps compounding: curated skill collections and skills frameworks have held roughly half of the weekly heat top 10 ever since. Star counts as of 2026-07-16:

| Repo | Stars | Shape |
| --- | --- | --- |
| [Superpowers](agents/superpowers.md) | 255.9k | Complete skills framework + methodology, plugging into Claude Code, Codex, Cursor, Copilot, and more |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 173.8k | Matt Pocock's curated personal `.claude/skills` directory |
| [anthropics/skills](https://github.com/anthropics/skills) | 161.6k | Anthropic's canonical Agent Skills reference — the upstream source of the pattern |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 78.7k | Addy Osmani's production-grade engineering skill set for coding agents |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 38.1k | Curated academic research pipeline for Claude Code |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 31.0k | Ready-to-use skills for research, science, engineering, analysis, finance, writing |

**Impact on selection:** the `.claude/skills` pattern crossed from curiosity into shared infrastructure — engineers publish skill libraries the way they used to publish dotfiles, and for many tasks the skill layer matters as much as the underlying agent. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks curated collections as watchlist entries (content assets, not agent surfaces); the wave has its own boards in [rankings/skill-verticals.md](rankings/skill-verticals.md).

## April 2026 — GPT-5.5 And "Codex For (Almost) Everything"

Two OpenAI releases a week apart set up the spring landscape. **April 16**: the largest Codex product update before the ChatGPT merge — background Computer Use across any macOS app, parallel multi-agent execution on one machine, an in-app browser with proactive suggestions, 90+ plugins, and 3M weekly developers (2x early March). **April 23**: **GPT-5.5** shipped as OpenAI's frontier agentic model — 82.7% on Terminal-Bench 2.0 (highest at launch), a 1M-token context window, at 2x GPT-5.4's price.

**Impact on selection:** together they raised the ceiling for every OpenAI-based surface and made the model layer part of agent selection. Both have since been superseded (see the July 9 entry) but remain the reference point for how fast the 2026 race moved. Details: [GPT-5.5](agents/gpt-5.5.md), [Codex](agents/codex.md).

## January 2026 — ClickHouse Acquires Langfuse

ClickHouse acquired **[Langfuse](agents/langfuse.md)**, the most-starred open-source LLM/agent observability platform (32.0k stars as of 2026-07-29). Langfuse offers tracing, evaluation, prompt management, and datasets under an open-core model — MIT core, with governance features under a separate Enterprise license — and remains free to self-host without limits.

**Impact on selection:** agent observability is being absorbed into general data infrastructure rather than remaining a standalone category, which matters if you are betting on a vendor staying independent. It also sharpens a distinction this map now documents explicitly: in this layer "open source" spans four different things — permissive (Opik, Traceloop, Helicone under Apache-2.0), open core (Langfuse), source-available but not OSI-approved (Arize Phoenix under Elastic 2.0), and fully closed (LangSmith, Braintrust). Langfuse states it remains 100% open source with an unchanged roadmap; that is a vendor commitment, not a verifiable guarantee. Details: [Langfuse](agents/langfuse.md), [observability & evaluation](comparisons/observability-and-evals.md).

Sources: [Joining ClickHouse](https://langfuse.com/blog/joining-clickhouse), [ClickHouse announcement](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), [langfuse/langfuse](https://github.com/langfuse/langfuse).
