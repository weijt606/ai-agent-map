# GPT-5.5

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gpt-5.5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gpt-5.5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GPT-5.5 was OpenAI's frontier agentic model of spring 2026 — designed to carry multi-step tasks through to completion with tool use and self-checking — and has since been succeeded twice, by GPT-5.6 on July 9 2026 and by [GPT-6 Astra](gpt-6-astra.md) on September 3 2026. This profile is kept as the lineage reference (see Post-Launch Landscape below).

> **Retired from Codex and ChatGPT (2026-10-14):** effective October 14 2026 at 19:00 UTC, GPT-5.5 is no longer available in Codex or ChatGPT for users signed in with a ChatGPT account; OpenAI points them to GPT-6.1 Sol (`gpt-6.1-sol`) and asks that workspace defaults, saved settings, custom agents and scripts that still select `gpt-5.5` be updated. The OpenAI API and Codex sessions authenticated with an API key are unaffected, and the API still lists it at $5 / $30 per M tokens ($0.50 cached). Source: [Codex changelog](https://learn.chatgpt.com/docs/changelog).

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Frontier agentic model that powered Codex, ChatGPT, and API surfaces (legacy — succeeded by GPT-5.6 in July and [GPT-6 Astra](gpt-6-astra.md) in September 2026; retired from Codex and ChatGPT for ChatGPT sign-in on 2026-10-14, so now API and API-key Codex only) |
| Open source | No |
| Best for | High-autonomy coding, research, multi-step agent workflows, and long-context tasks |
| Main cost | 2x the API price of GPT-5.4, and the model boundary blurs with the Codex product boundary |
| Official website | https://openai.com/index/introducing-gpt-5-5/ |
| API reference | https://developers.openai.com |

## Why This Entry Exists

Most entries in this directory are products or tools. GPT-5.5 is a model. It is included because OpenAI explicitly positions it as "a new class of intelligence for real work and powering agents," and because its release reshapes the capability ceiling across multiple existing agent surfaces — Codex, ChatGPT, GitHub Copilot, and any API-based agent builder.

When a model release changes what agents built on top of it can do, the model itself becomes part of the selection landscape.

## When To Pick It

- You want the model that was OpenAI's strongest for agentic coding at its April launch, and you reach it through the API or an API-key Codex session (ChatGPT sign-in lost it on 2026-10-14).
- You need a 1-million-token context window for large codebases or long research workflows.
- You care about fewer tokens per task — GPT-5.5 completes the same Codex tasks with significantly fewer tokens than GPT-5.4.
- You are building your own agent system on the OpenAI API and want native tool calling, self-checking, and multi-step planning.
- Your workflow ran through ChatGPT, Codex, or GitHub Copilot and you wanted the latest model upgrade at the time. For ChatGPT-signed-in Codex and ChatGPT that path closed on 2026-10-14.

## When Not To Pick It

- You want an open-source or self-hosted model. GPT-5.5 is fully proprietary.
- You are cost-sensitive — input is $5/M tokens, output is $30/M tokens (2x GPT-5.4).
- You need the current frontier — the landscape has moved twice on both sides since spring 2026 ([GPT-6 Astra](gpt-6-astra.md), [Claude Fable 5.1](claude-fable-5.md), [Opus 5](claude-opus-5.md)); see Post-Launch Landscape below.
- You want a finished agent product, not a model. In that case, look at [Codex](codex.md) (the product) instead.
- You want local execution without cloud dependency.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic coding | Very strong | 82.7% on Terminal-Bench 2.0, highest among public benchmarks at launch |
| Long context | Very strong | 1M token context window in API |
| Tool calling | Strong | Native tool use for code execution, browsing, file ops |
| Self-checking | Strong | Verifies its own output before delivering |
| Multi-step planning | Strong | Handles multi-part tasks requiring planning, tool use, and verification |
| Token efficiency | Strong | Fewer tokens per task compared to GPT-5.4 |
| SWE-Bench Pro | Medium | 58.6% — trails Claude Opus 4.7 at 64.3% |
| Open-source / self-host | None | Fully proprietary, API and product access only |

## Where It Runs

GPT-5.5 is not a standalone runtime. It was available through the surfaces below; since 2026-10-14 it is gone from ChatGPT and from Codex signed in with a ChatGPT account, and remains on the API and API-key Codex sessions:

- **ChatGPT** — Plus, Pro, Business, Enterprise tiers (retired 2026-10-14)
- **Codex** — OpenAI's agentic coding product with sandboxed cloud execution (retired for ChatGPT sign-in 2026-10-14; API-key sessions unaffected)
- **API** — Responses and Chat Completions (rolling out)
- **GitHub Copilot** — available in the model picker for ask, edit, and agent modes

## Operating Cost

Complexity is Medium to High. The model itself is straightforward to use through ChatGPT or Codex, but API-based agent builders face a meaningful cost jump: $5/$30 per million tokens (input/output), exactly 2x GPT-5.4. OpenAI argues the per-task cost may still drop because GPT-5.5 uses fewer tokens to finish the same work, but teams should benchmark this claim against their own workloads.

## Relationship To Codex

This profile covers GPT-5.5 as a model. The [Codex](codex.md) profile covers the product — the cloud execution environment, isolation model, and review workflow. GPT-5.5 powered Codex (the bundled default moved to GPT-6 Astra on Sept 4 and to GPT-6.1 Sol on Sept 29, and ChatGPT-signed-in Codex dropped GPT-5.5 on 2026-10-14), but it was never the same thing. If you are choosing between agent products, start with Codex. If you are choosing which model to wire into your own agent system, this profile is the right one.

## Post-Launch Landscape (as of October 2026)

The frontier moved fast after GPT-5.5's April launch, and has now moved through two more generations on each side:

| Release | Date | What it changed |
| --- | --- | --- |
| **Claude Opus 4.8** (Anthropic) | May 28 2026 | Fixed Opus 4.7's verbosity and tool-calling issues; added Dynamic workflows (hundreds of parallel subagents in Claude Code); $5/$25 per M tokens |
| **[Claude Fable 5](claude-fable-5.md)** (Anthropic) | June 9 2026 | First Mythos-class model — a tier above Opus; $10/$50 per M tokens, metered credits in Claude subscriptions since July 7 |
| **Claude Sonnet 5** (Anthropic) | June 30 2026 | Mid tier at $2/$10 per M tokens, positioned close to Opus 4.8; the introductory price was made permanent in August |
| **GPT-5.6** (OpenAI) | July 9 2026 | Succeeded GPT-5.5 across ChatGPT/Codex/API in three tiers — Sol, Terra, Luna — with an Ultra multi-agent setting; led the Artificial Analysis Coding Agent Index at launch (Sol 80 vs Fable 5 77.2, GPT-5.5 76.4, Opus 4.8 72.5) |
| **[Claude Opus 5](claude-opus-5.md)** (Anthropic) | July 24 2026 | Held the Opus price ($5/$25) while closing most of the gap to Fable 5; 1M context as default *and* maximum; became the default model on Claude Max |
| **[Claude Fable 5.1](claude-fable-5.md)** (Anthropic) | September 1 2026 | Same $10/$50 sticker, cache reads cut 75% to $0.25/M; SWE-bench Pro 81.2; ~60% fewer cybersecurity false positives in Claude Code |
| **[GPT-6 Astra](gpt-6-astra.md)** (OpenAI) | September 3 2026 | Current OpenAI ceiling; $10/$50, repricing to $20/$75 past 272k input tokens; public version restricted on cybersecurity prompts |
| **Claude Opus 5.5** (Anthropic) | September 22 2026 | $4/$20, cache reads $0.20/M; Anthropic says Fable 5.1-level on most work at 40% less to run than Opus 5; default Opus in Claude Code `v2.1.280` |
| **GPT-6 Sol and GPT-6 Luna** (OpenAI) | September 22 2026 | Sol $2/$10 (cache $0.20), Luna $0.10/$0.50 (cache $0.01), each roughly half its GPT-5.6 namesake; not the same models as GPT-5.6 Sol and Luna |
| **Claude Sonnet 5.5** (Anthropic) | September 28 2026 | $2/$10, cache reads $0.10/M; Terminal-Bench 4.0 70.6%; default Sonnet in Claude Code `2.1.284` |
| **GPT-6.1 Sol** (OpenAI) | September 29 2026 | $2/$10, cache reads $0.10/M; bundled Codex default since `rust-v0.159.1`, replacing Astra; the model OpenAI points GPT-5.5 users to |
| **Claude Haiku 5.5** (Anthropic) | October 7 2026 | $0.10/$0.50 on prompts up to 100K tokens ($0.50/$2.50 above), cache reads $0.01/M; the Anthropic floor |
| **GPT-6.1 Terra** (OpenAI) | October 26 2026 | $1/$5, cache reads $0.05/M; selectable in Codex, not a default |

Practical read: GPT-5.5 is a legacy choice for new work, and since 2026-10-14 it is API-only for anyone signed in with ChatGPT. At the ceiling the decision is still **[GPT-6 Astra](gpt-6-astra.md) versus [Fable 5.1](claude-fable-5.md) at an identical $10/$50 headline** — separated by cache-read cost and long-context pricing shape rather than by sticker. The cost-controlled path is now GPT-6.1 Sol ($2/$10), GPT-6.1 Terra ($1/$5) and GPT-6 Luna on one side, and Opus 5.5 ($4/$20), Sonnet 5.5 ($2/$10) and Haiku 5.5 on the other; both vendors' coding agents default to that middle layer. Prices: [cost & benchmarks](../comparisons/cost-and-benchmarks.md).

## Bottom Line

GPT-5.5 was a genuine capability jump for OpenAI's agent ecosystem — strongest agentic coding benchmarks at its April launch, 1M context, and better token efficiency. Two generations later it is a legacy choice; this profile stays in the map as the reference point for how the spring 2026 model race reshaped agent selection, and as the place the OpenAI model lineage is written down.
