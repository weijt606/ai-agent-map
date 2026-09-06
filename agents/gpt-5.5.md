# GPT-5.5

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gpt-5.5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gpt-5.5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GPT-5.5 was OpenAI's frontier agentic model of spring 2026 — designed to carry multi-step tasks through to completion with tool use and self-checking — and has since been succeeded twice, by GPT-5.6 on July 9 2026 and by [GPT-6 Astra](gpt-6-astra.md) on September 3 2026. This profile is kept as the lineage reference (see Post-Launch Landscape below).

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Frontier agentic model powering Codex, ChatGPT, and API surfaces (legacy — succeeded by GPT-5.6 in July and [GPT-6 Astra](gpt-6-astra.md) in September 2026) |
| Open source | No |
| Best for | High-autonomy coding, research, multi-step agent workflows, and long-context tasks |
| Main cost | 2x the API price of GPT-5.4, and the model boundary blurs with the Codex product boundary |
| Official website | https://openai.com/index/introducing-gpt-5-5/ |
| API reference | https://developers.openai.com |

## Why This Entry Exists

Most entries in this directory are products or tools. GPT-5.5 is a model. It is included because OpenAI explicitly positions it as "a new class of intelligence for real work and powering agents," and because its release reshapes the capability ceiling across multiple existing agent surfaces — Codex, ChatGPT, GitHub Copilot, and any API-based agent builder.

When a model release changes what agents built on top of it can do, the model itself becomes part of the selection landscape.

## When To Pick It

- You want the strongest available OpenAI model for agentic coding tasks through Codex or the API.
- You need a 1-million-token context window for large codebases or long research workflows.
- You care about fewer tokens per task — GPT-5.5 completes the same Codex tasks with significantly fewer tokens than GPT-5.4.
- You are building your own agent system on the OpenAI API and want native tool calling, self-checking, and multi-step planning.
- Your workflow already runs through ChatGPT, Codex, or GitHub Copilot and you want the latest model upgrade.

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

GPT-5.5 is not a standalone runtime. It is available through:

- **ChatGPT** — Plus, Pro, Business, Enterprise tiers
- **Codex** — OpenAI's agentic coding product with sandboxed cloud execution
- **API** — Responses and Chat Completions (rolling out)
- **GitHub Copilot** — available in the model picker for ask, edit, and agent modes

## Operating Cost

Complexity is Medium to High. The model itself is straightforward to use through ChatGPT or Codex, but API-based agent builders face a meaningful cost jump: $5/$30 per million tokens (input/output), exactly 2x GPT-5.4. OpenAI argues the per-task cost may still drop because GPT-5.5 uses fewer tokens to finish the same work, but teams should benchmark this claim against their own workloads.

## Relationship To Codex

This profile covers GPT-5.5 as a model. The [Codex](codex.md) profile covers the product — the cloud execution environment, isolation model, and review workflow. GPT-5.5 powers Codex but is not the same thing. If you are choosing between agent products, start with Codex. If you are choosing which model to wire into your own agent system, this profile is the right one.

## Post-Launch Landscape (as of September 2026)

The frontier moved fast after GPT-5.5's April launch, and has now moved through two more generations on each side:

| Release | Date | What it changed |
| --- | --- | --- |
| **Claude Opus 4.8** (Anthropic) | May 28 2026 | Fixed Opus 4.7's verbosity and tool-calling issues; added Dynamic workflows (hundreds of parallel subagents in Claude Code); $5/$25 per M tokens |
| **[Claude Fable 5](claude-fable-5.md)** (Anthropic) | June 9 2026 | First Mythos-class model — a tier above Opus; $10/$50 per M tokens, metered credits in Claude subscriptions since July 7 |
| **Claude Sonnet 5** (Anthropic) | June 30 2026 | Mid tier at $2/$10 per M tokens, positioned close to Opus 4.8; the introductory price was made permanent in August |
| **GPT-5.6** (OpenAI) | July 9 2026 | Succeeded GPT-5.5 across ChatGPT/Codex/API in three tiers — Sol, Terra, Luna — with an Ultra multi-agent setting; led the Artificial Analysis Coding Agent Index at launch (Sol 80 vs Fable 5 77.2, GPT-5.5 76.4, Opus 4.8 72.5) |
| **[Claude Opus 5](claude-opus-5.md)** (Anthropic) | July 24 2026 | Held the Opus price ($5/$25) while closing most of the gap to Fable 5; 1M context as default *and* maximum; became the default model on Claude Max |
| **[Claude Fable 5.1](claude-fable-5.md)** (Anthropic) | September 1 2026 | Same $10/$50 sticker, cache reads cut 75% to $0.25/M; SWE-bench Pro 81.2; ~60% fewer cybersecurity false positives in Claude Code |
| **[GPT-6 Astra](gpt-6-astra.md)** (OpenAI) | September 3 2026 | Current OpenAI ceiling; $10/$50, doubling past 272k input tokens; public version restricted on cybersecurity prompts |

Practical read: GPT-5.5 is a legacy choice for new work. The September 2026 model-layer decision is **[GPT-6 Astra](gpt-6-astra.md) versus [Fable 5.1](claude-fable-5.md) at an identical $10/$50 headline** — separated by cache-read cost and long-context pricing shape rather than by sticker — with the cost-controlled path being GPT-5.6's tiers on one side and [Opus 5](claude-opus-5.md) / Sonnet 5 on the other.

## Bottom Line

GPT-5.5 was a genuine capability jump for OpenAI's agent ecosystem — strongest agentic coding benchmarks at its April launch, 1M context, and better token efficiency. Two generations later it is a legacy choice; this profile stays in the map as the reference point for how the spring 2026 model race reshaped agent selection, and as the place the OpenAI model lineage is written down.
