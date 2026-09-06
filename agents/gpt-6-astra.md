# GPT-6 Astra

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gpt-6-astra.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gpt-6-astra.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GPT-6 Astra is OpenAI's current frontier model, released September 3–4 2026 — a generational step over the GPT-5.6 family, priced at exactly the same sticker as [Claude Fable 5.1](claude-fable-5.md), and shipped to the public in a deliberately restricted version.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Frontier agentic model — the current ceiling on the OpenAI side |
| Open source | No |
| Best for | Agentic execution, computer and browser use, long-context retrieval, coding workflows |
| Main cost | $10 / $50 per M tokens, doubling to $20 / $75 on long context (threshold reported at 272k input tokens) |
| Public version | Restricted — rejects some cybersecurity prompts; advanced access gated behind Daybreak Blue |
| Official announcement | https://openai.com/index/gpt-6-astra/ |
| API pricing | https://developers.openai.com/api/docs/pricing |

## Why This Entry Exists

This route tracks the model layer because the model sets the capability ceiling of every agent built on it. On the OpenAI side that ceiling moved twice in two months — **GPT-5.6 on July 9**, then **GPT-6 Astra on September 3** — and both moves change what [Codex](codex.md), ChatGPT, GitHub Copilot, and any API-based agent can do.

Astra is also the first release on this map where the *public* version of a frontier model is explicitly a restricted one. That is a selection fact, not a footnote: what you can build depends on which version you have.

## When To Pick It

- You want the strongest OpenAI model for agent work — OpenAI's own framing is state of the art in coding, math, and driving computers and web browsers.
- Your agent's failure mode is **drift**: the launch claims center on staying focused, holding task boundaries, and finishing multi-step workflows rather than on raw benchmark scores.
- You need very long context in one shot — the window is reported at ~1.05M tokens with 128k max output.
- You are already committed to OpenAI surfaces and want the ceiling rather than the tier ladder.

## When Not To Pick It

- **Your work touches offensive security or adjacent research.** The generally available version rejects certain cybersecurity prompts outright. Expanded capability runs through Daybreak Blue approval, the same gate GPT-5.6-Cyber landed behind in August 2026.
- Your prompts routinely exceed **272k input tokens** — past that threshold input doubles to $20/M and output rises to $75/M. A long-context agent loop can cross that line without anyone deciding to.
- You are cost-sensitive: [GPT-5.6 Terra](gpt-5.5.md) at $2/$12 and Luna at $0.20/$1.20 do ordinary agent work at a fraction of the price, and the tier ladder is still the OpenAI-side lever.
- You want open weights, self-hosting, or a model you can pin indefinitely.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic execution | Very strong | Task-boundary adherence and multi-step completion are the headline claims |
| Computer and browser use | Very strong | Called out as a primary axis of improvement over GPT-5.6 |
| Coding | Very strong | 74.1% on DeepSWE v1.1 as of September 2026 |
| Long context | Very strong | ~1.05M tokens — but priced in two bands, see below |
| Cybersecurity (public version) | Restricted | Capability exists; the shipped default refuses part of it |
| Open-source / self-host | None | Fully proprietary |

**Sourcing note.** Two things to flag. OpenAI's launch materials quote **DeepSWE v1.1**, not SWE-bench Verified, so there is no like-for-like SWE-bench comparison against Claude at launch — this map does not manufacture one, and where you see Astra-vs-Fable SWE-bench tables elsewhere, check whether the numbers came from the vendors or from a third-party leaderboard. Separately, `openai.com` was not directly reachable when this profile was written: the **prices and the two-band short/long-context structure below are first-party** (OpenAI's API pricing page), while the **272k threshold, the ~1.05M window, and the 128k max output are from secondary reporting** and are marked as such wherever they appear.

## Price Structure (first-party, September 2026)

| Tier | Short context in / out | Long context in / out | Cached input |
| --- | --- | --- | --- |
| **GPT-6 Astra** | $10 / $50 | $20 / $75 | $1 |
| GPT-5.6 Sol | $4 / $20 | $8 / $30 | — |
| GPT-5.6 Terra | $2 / $12 | $4 / $18 | — |
| GPT-5.6 Luna | $0.20 / $1.20 | $0.40 / $1.80 | — |

Three things worth carrying into a budget:

1. **The long-context surcharge is the trap.** Above the long-context threshold — reported at 272k input tokens — the whole request reprices. Anthropic bills its 1M window at standard rates across the window, so the two vendors now differ in *shape*, not just in level — see the [Opus 5 tier ladder](claude-opus-5.md).
2. **Astra and Fable 5.1 carry the same sticker** ($10/$50). The separation is in caching: Fable 5.1 reads cache at $0.25/M against Astra's $1/M, which for a long-lived agent session is where the bill actually accumulates.
3. **Fast mode is 2x** (output $100/M) and is unavailable with EU data residency. Batch is half price; Flex matches batch on most models.

## Where It Runs

- **ChatGPT** — paid tiers, in the restricted public version.
- **API** — with the pricing structure above.
- **Codex** — see the [Codex profile](codex.md) for the product boundary; the model under it moved to the GPT-5.6 family in July and Astra is the current ceiling above it.
- Staged rollout ran from a limited partner preview (Sept 3) to paid users (Sept 4), then broader API and cloud availability.

## Relationship To GPT-5.6 And GPT-5.5

[GPT-5.5](gpt-5.5.md) remains in this map as the spring 2026 reference point, and its profile carries the model-lineage table. The short version: GPT-5.5 (April) → GPT-5.6 Sol/Terra/Luna (July 9) → GPT-6 Astra (September 3). The tiered family did not go away when Astra shipped — it is still the cost-controlled path, and Sol's promotional $4/$20 runs to at least November 21 2026.

## Bottom Line

Astra restores a clear OpenAI ceiling and pushes the frontier decision back to a two-vendor comparison at an identical headline price. Read the fine print rather than the sticker: the 272k repricing threshold and the 4x gap in cache-read cost will move a real agent bill more than the benchmark table will. And check which version you are entitled to before designing anything security-adjacent on it.
