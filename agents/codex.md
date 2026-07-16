# Codex

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/codex.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](codex.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Codex is the "delegate and review" coding agent that, since July 9 2026, lives inside the ChatGPT app — cloud delegation, desktop Computer Use, and an open-source CLI under one roof.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | OpenAI |
| Route | Coding agent surface inside the ChatGPT app (cloud + desktop), plus the open-source Codex CLI |
| Open source | No, except for Codex CLI |
| Best for | Async tasks, isolated execution, review evidence, and parallel delegation |
| Main cost | A delegate-and-review rhythm that is less immediate than local agents, on a product surface that keeps shifting |
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
| Background delegation | Very strong | Multiple agents can now run on the same machine in parallel after the April 16 update |
| GitHub / PR handoff | Strong | Well suited to review-oriented workflows |
| Computer use | Strong | Background cursor and keyboard control across any macOS app; noticeably faster since the July 9 2026 GPT-5.6 upgrade |
| PR review in-app | Strong (new July 9 2026) | Side-panel pull-request review and inline diff editing in the ChatGPT desktop app |
| Local companion surfaces | Strong (was Medium) | Codex CLI is now a first-class surface, with persisted /goal workflows and MultiAgentV2 in v0.128 |

## Merged Into ChatGPT (July 9 2026)

On July 9 2026, OpenAI merged the standalone Codex app into the ChatGPT desktop app for macOS and Windows. What changed for selection:

- **Codex is now an entry inside ChatGPT**, a dedicated coding experience next to Chat and the new agentic **ChatGPT Work** mode — available on every plan, including Free.
- **Inline diff editing and side-panel pull-request review** move more of the review loop into the app itself.
- **Faster Computer Use, powered by GPT-5.6**, plus **multi-repository projects** for tasks that span codebases.
- **Scale**: 5M+ weekly Codex users, and over 1M of them use it for work outside software development entirely.
- **Codex CLI is unaffected** — it remains the open-source terminal surface at github.com/openai/codex.

## Earlier 2026 Expansion (April 16)

On April 16 2026, OpenAI shipped "Codex for (almost) everything," the largest single update to the Codex product surface before the ChatGPT merge. Key shifts for selection:

- **Background Computer Use:** Codex sees, clicks, and types with its own cursor across any macOS application — closing the gap with general-purpose computer-use agents.
- **Parallel multi-agent execution:** Multiple Codex agents can run on the same Mac in parallel without interfering with foreground work.
- **In-app browser + proactive suggestions:** Frontend iteration without context-switching, plus proposed work pulled from project memory.
- **90+ plugins:** Atlassian Rovo, CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, and more.
- **3M weekly active developers** reported in April 2026 — nearly 2x early-March 2026.

Codex CLI (the open-source terminal companion at github.com/openai/codex) also moved fast: v0.128.0 on April 30 2026 added persisted /goal workflows, MultiAgentV2 controls, plugin marketplace install, and richer permission profiles. The CLI now sits in the same selection conversation as Claude Code and Aider for terminal-first coding agents, with the cloud Codex product as a complementary background path.

## Operating Cost

Complexity is Medium. It reduces local ops burden, but it also pushes the team into a more asynchronous delegate-and-review rhythm. The more accurate 2026 framing is: Codex is the proprietary cloud agent product, while Codex CLI is a related local companion surface.

## Model Layer

As of July 9 2026, Codex is powered by **GPT-5.6** (Sol / Terra / Luna tiers), which succeeded [GPT-5.5](gpt-5.5.md) the same day the product merged into ChatGPT. The upgrade shows up most in Computer Use speed and agentic coding benchmarks. See the [GPT-5.5 profile](gpt-5.5.md) for the model-lineage breakdown and the post-launch landscape (including Anthropic's Mythos-class [Claude Fable 5](claude-fable-5.md)).

## Bottom Line

After the July 9 2026 merge, Codex is best read as the coding surface of the ChatGPT app rather than a separate product: cloud delegation, desktop Computer Use, in-app PR review on every plan — with Codex CLI as the open-source terminal surface that competes head-to-head with Claude Code and Aider.