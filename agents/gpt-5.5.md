# GPT-5.5

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gpt-5.5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gpt-5.5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GPT-5.5 is OpenAI's frontier agentic model, designed from the ground up to carry multi-step tasks through to completion with tool use and self-checking.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Frontier agentic model powering Codex, ChatGPT, and API surfaces |
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
- You need the best tool-use and SWE-bench performance — Claude Opus 4.7 currently leads on SWE-Bench Pro (64.3% vs 58.6%).
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

## Bottom Line

GPT-5.5 is a genuine capability jump for OpenAI's agent ecosystem — strongest agentic coding benchmarks at launch, 1M context, and better token efficiency. The trade-off is clear: it is the most expensive OpenAI model to date, it is fully proprietary, and it trails Claude on some tool-use benchmarks. Its biggest impact is raising the ceiling for everything built on the OpenAI API.
