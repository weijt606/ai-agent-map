# Codex

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/codex.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](codex.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Codex is a strong representative of the “delegate to the cloud, review later” model.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Cloud software engineering agent inside ChatGPT |
| Open source | No, except for Codex CLI |
| Best for | Async tasks, isolated execution, review evidence, and parallel delegation |
| Main cost | Still a cloud-first research preview, with a less immediate rhythm than local agents |
| Official website | https://developers.openai.com/codex |
| GitHub repo | https://github.com/openai/codex |

## When To Pick It

- You have clearly bounded coding tasks to delegate asynchronously.
- You care about logs, tests, and traceable execution evidence.
- Your team already works comfortably through issues, PRs, and review.
- You are comfortable with the main product running in a cloud sandbox rather than fully local execution.

## When Not To Pick It

- You want continuous local back-and-forth inside the editor.
- You require strict self-hosted or offline execution.
- You actually need a broader runtime with messaging or device surfaces.
- You want to treat the open-source Codex CLI as if it were the same thing as the core Codex product.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Isolated execution | Very strong | The isolation model is core |
| Code execution | Strong | Commands, tests, and validation matter here |
| Review evidence | Strong | Well aligned with review-heavy teams |
| Background delegation | Strong | This is the primary mental model |
| GitHub / PR handoff | Strong | Well suited to review-oriented workflows |
| Local companion surfaces | Medium | Codex CLI is related, but its open-source status should not be treated as the product's status |

## Operating Cost

Complexity is Medium. It reduces local ops burden, but it also pushes the team into a more asynchronous delegate-and-review rhythm. The more accurate 2026 framing is: Codex is the proprietary cloud agent product, while Codex CLI is a related local companion surface.

## Model Layer

As of April 23 2026, Codex is powered by [GPT-5.5](gpt-5.5.md) — OpenAI's latest frontier agentic model. The model upgrade brings stronger coding benchmarks (82.7% Terminal-Bench 2.0), a 1M token context window, and better token efficiency. If you are evaluating Codex, the model layer now matters more than before. See the [GPT-5.5 profile](gpt-5.5.md) for the model-level breakdown.

## Bottom Line

The cleanest way to understand Codex is as the cloud agent in ChatGPT, with Codex CLI as a related local entry point rather than the core product itself.