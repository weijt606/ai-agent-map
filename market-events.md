# Market Events

[English](market-events.md) | [中文](zh/market-events.md)

Structural events that reshaped agent selection — model releases, product mergers, and waves — newest first. The weekly play-by-play lives in the "Market events" timeline in [agents/README.md](agents/README.md); this page keeps the durable records.

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
