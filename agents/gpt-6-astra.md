# GPT-6 Astra

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gpt-6-astra.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gpt-6-astra.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GPT-6 Astra is OpenAI's current frontier model, released September 3–4 2026 — a generational step over the GPT-5.6 family, and shipped to the public in a deliberately restricted version.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Frontier agentic model — the current ceiling on the OpenAI side |
| Open source | No |
| Best for | Agentic execution, computer and browser use, long-context retrieval, coding workflows |
| Public version | Restricted — rejects some cybersecurity prompts; advanced access gated behind Daybreak Blue |
| Official announcement | https://openai.com/index/gpt-6-astra/ |

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
- You want open weights, self-hosting, or a model you can pin indefinitely.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic execution | Very strong | Task-boundary adherence and multi-step completion are the headline claims |
| Computer and browser use | Very strong | Called out as a primary axis of improvement over GPT-5.6 |
| Coding | Very strong | 74.1% on DeepSWE v1.1 as of September 2026 |
| Long context | Very strong | ~1.05M tokens |
| Cybersecurity (public version) | Restricted | Capability exists; the shipped default refuses part of it |
| Open-source / self-host | None | Fully proprietary |

**Sourcing note.** Two things to flag. OpenAI's launch materials quote **DeepSWE v1.1**, not SWE-bench Verified, so there is no like-for-like SWE-bench comparison against Claude at launch — this map does not manufacture one, and where you see Astra-vs-Fable SWE-bench tables elsewhere, check whether the numbers came from the vendors or from a third-party leaderboard. Separately, `openai.com` was not directly reachable when this profile was written: the **~1.05M window and the 128k max output are from secondary reporting** and are marked as such wherever they appear.

## Where It Runs

- **ChatGPT** — paid tiers, in the restricted public version.
- **API**.
- **Codex** — see the [Codex profile](codex.md) for the product boundary. Astra was Codex CLI's bundled default from Sept 4 (`rust-v0.153.4`) until `rust-v0.159.1` (Sept 29) switched the default to GPT-6.1 Sol.
- Staged rollout ran from a limited partner preview (Sept 3) to paid users (Sept 4), then broader API and cloud availability.

## Relationship To GPT-5.6 And GPT-5.5

[GPT-5.5](gpt-5.5.md) remains in this map as the spring 2026 reference point, and its profile carries the model-lineage table. The short version: GPT-5.5 (April) → GPT-5.6 Sol/Terra/Luna (July 9) → GPT-6 Astra (September 3) → GPT-6 Sol and Luna (September 22) → GPT-6.1 Sol (September 29) → GPT-6.1 Terra (October 26). The tiered family did not go away when Astra shipped.

## Bottom Line

Astra restores a clear OpenAI ceiling and pushes the frontier decision back to a two-vendor comparison. Check which version you are entitled to before designing anything security-adjacent on it.
