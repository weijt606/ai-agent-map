# Open Code Review

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/open-code-review.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](open-code-review.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Open Code Review (`ocr`) is Alibaba's open-sourced AI code-review CLI — a deliberately *narrow* agent that wraps a deterministic review pipeline around an LLM, trading recall for precision, and that can either run the review itself or hand the reasoning to the coding agent you already use.

> **Narrow on purpose.** This is not a general coding agent that happens to review code. File selection, file bundling, rule matching, and comment positioning are handled by engineering logic; the model is used only where dynamic judgment and context retrieval actually help. That is the whole design argument, and it is the reason to consider it over pointing [Claude Code](claude-code.md) at a diff with a review skill.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Alibaba Group (`alibaba/open-code-review`, open-codereview.ai) |
| Route | Review-first automation — dedicated code-review agent |
| Open source | Apache-2.0 |
| Implementation | Go; distributed via npm (`@alibaba-group/open-code-review`), install script, release binaries, or source |
| Models | Any OpenAI- or Anthropic-compatible endpoint; or none at all in Delegation Mode |
| Surfaces | CLI (`ocr`), CI/CD (GitHub Actions, GitLab CI, GitFlic CI, Gerrit), plugins for Claude Code / Codex / Cursor / OpenCode, and a portable agent skill |
| Best for | Teams that want repeatable, line-accurate review in CI without paying general-agent token costs |
| Main cost | Deliberately lower recall than a general agent, and a rule/config surface to maintain |
| GitHub repo | https://github.com/alibaba/open-code-review |

## Origin

It began as Alibaba Group's internal official AI code-review assistant. The project states it ran for about two years, served tens of thousands of developers, and flagged millions of defects before being open-sourced — which is unusual provenance for this category: most review agents are built as products first and hardened later, and this one is the reverse. The scale claim is the vendor's own and is not independently verifiable, but the shape of the design is consistent with it.

## When To Pick It

- **Your reviews run in CI and must be consistent.** The pitch is aimed squarely at the failure modes of general agents on review: cutting corners on large changesets, drifting line numbers, and quality that swings with small prompt edits.
- **Token cost matters.** The project reports roughly **one-ninth** the tokens of a general-purpose agent doing the same review, and faster wall-clock — significant when review runs on every pull request. (Vendor-run benchmark; see the caveat below.)
- **You want precision over volume.** Recall is *lower* than a general agent by design, on the reasoning that a review bot people learn to ignore is worse than one that says less.
- **You want to keep your existing agent and its model.** In **Delegation Mode**, `ocr` does the file selection and rule resolution and your coding agent performs the review with its own LLM — no separate API key or provider configuration.
- **You need review without a diff.** `ocr scan` reviews whole files across a repository or directory, which is the tool you want for an unfamiliar codebase rather than a changeset.
- You want built-in language rules rather than writing them: the shipped ruleset covers things like null-pointer risks, thread safety, XSS, and SQL injection across multiple languages.

## When Not To Pick It

- You want an agent that also *fixes* what it finds and opens the PR — that is [Cline](cline.md), [CoStrict](costrict.md), [Codex](codex.md), or [Claude Code](claude-code.md). `ocr` reviews.
- You need maximum recall for a security audit. The precision-first trade-off is explicit, so pair it with dedicated security tooling rather than treating it as coverage.
- You want an enterprise platform with private deployment, standardized requirement-to-test workflow, and IDE surfaces — [CoStrict](costrict.md) is the closer fit in that lane.
- Your repository has no meaningful Git history or you are below Git 2.41 — diff generation, code search, and repository operations all lean on Git.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Review precision | Very strong (vendor-reported) | Higher precision and F1 than a general agent on the same model, at ~1/9 the tokens |
| Recall | Deliberately limited | An explicit trade against noise, not an oversight |
| Line-level positioning | Strong | Independent positioning and reflection modules exist specifically to stop location drift |
| Large-changeset stability | Strong | Related files are bundled into units, each reviewed by a sub-agent with isolated context, concurrently |
| CI/CD integration | Strong | GitHub Actions, GitLab CI, GitFlic CI, Gerrit |
| Agent integration | Strong | Plugins for Claude Code, Codex, Cursor, and OpenCode, plus a portable skill for skill-compatible agents |
| Observability | Present | OpenTelemetry integration, plus a browser session viewer for replaying reviews |
| Autonomous fixing | Not the goal | It comments; it does not land changes |

## About That Benchmark

The project publishes a comparison against a general-purpose agent (Claude Code) on the same underlying model, built from 50 popular open-source repositories, 200 real pull requests, 10 languages, and 1,505 annotated ground-truth issues cross-validated by 80+ senior engineers. That is a more serious evaluation design than this category usually offers, and the reported trade — higher precision and F1, much lower token use, lower recall — is at least internally coherent with the architecture.

It is still **vendor-run**, on a benchmark the vendor built, against one competitor. Treat the *direction* as credible and the *magnitudes* as unverified. If review quality is the deciding factor for you, run it on your own recent pull requests before committing; the honest comparison is against whatever you use today, on your code.

## Operating Cost

Low to start, Medium to run well. Install is one npm command, and `ocr config provider` / `ocr config model` walk through provider setup interactively and test connectivity. Sessions are resumable, and `ocr session comments` can print recorded findings filtered by severity or as JSON, which is what you want for wiring it into a gate. The ongoing cost is the review-rule surface — path filtering and targeting are configurable, and a review bot's usefulness lives or dies on how well those rules match your codebase. Delegation Mode removes the model cost entirely at the price of putting your coding agent's tokens on the bill instead.

## Bottom Line

Open Code Review is the strongest current argument that **code review should be a specialized agent, not a prompt you hand a general one**. The hybrid design — deterministic engineering for the steps that must not go wrong, an LLM only for the judgment calls — targets exactly the complaints teams have about agent review, and the two-year internal history behind it shows in the surface: resumable sessions, severity-filtered JSON output, four CI systems, OpenTelemetry, and a delegation mode that works without its own API key. Read the precision-over-recall trade as a real constraint rather than marketing: this tool is built to be believed, not to be thorough. For agents that review *and* act, see [Cline](cline.md) and [CoStrict](costrict.md); for the wider coding lane, see [coding automation](../use-cases/coding-automation.md).
