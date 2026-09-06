# OpenCode

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/opencode.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](opencode.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: OpenCode is the largest vendor-neutral open-source coding agent — 205k stars under MIT — and this map has been quietly referencing it as an integration target in five other profiles without ever writing one for it.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anomaly Co (community project) |
| Route | Direct execution |
| Repository | [`anomalyco/opencode`](https://github.com/anomalyco/opencode) — MIT, TypeScript, **205k stars** |
| Open source | Yes (MIT) |
| Best for | A terminal coding agent that belongs to no model vendor |
| Main cost | You choose and pay for the model; no vendor is optimizing the loop for their own weights |
| Surfaces | Terminal, plus a **desktop app in beta** (macOS, Windows, Linux) |
| Official site | https://opencode.ai |

> **Naming note.** The repository moved from `sst/opencode` to **`anomalyco/opencode`**; the old path still redirects, and the Homebrew tap and Nix flake reference the new org. Same project, same star count, same history since April 2025.

## Why This Entry Exists

Because it was already here. [QM](qm.md) lists OpenCode among the harnesses it runs, [Omnigent](omnigent.md) ships an adapter for it, [Superpowers](superpowers.md) has a plugin for it, [CodeGraph](codegraph.md) has an MCP integration for it, and [Open Code Review](open-code-review.md) ships a plugin for it. Five profiles treat it as infrastructure. None of them could link to a page explaining what it is — until this one.

That is worth naming as a failure mode: a project can become load-bearing in a map's own text without ever clearing its inclusion process.

## When To Pick It

- **You want vendor neutrality at the loop level.** [Claude Code](claude-code.md), [Codex](codex.md), [Gemini CLI](gemini-cli.md), [Kimi Code](kimi-code.md), and [Qwen Code](qwen-code.md) are all first-party tools whose defaults follow their vendor's model. OpenCode's incentive is different because its authors do not sell a model.
- You want a **large, actively developed** open-source agent rather than a lean one — at 205k stars it is one of the biggest agent repositories in existence, and it was still shipping the day this profile was written.
- You want **installation to be someone else's problem**: curl script, npm, Homebrew, Scoop, Chocolatey, pacman/AUR, mise, and Nix are all first-class.
- You want a **GUI option without leaving the project** — the desktop app ships as `.dmg`, `.exe`, `.deb`, `.rpm`, and `.AppImage`, though it is explicitly beta.
- You are building something on top of it: the integrations listed above mean the ecosystem already expects it.

## When Not To Pick It

- **You want a vendor's tuned defaults.** If you have committed to one model family, the first-party CLI is usually better tuned for it — see the [terminal coding CLI comparison](../comparisons/coding-cli-agents.md).
- You want a small, auditable loop you can read in a sitting — that is [mini-swe-agent](mini-swe-agent.md), and OpenCode is the opposite end of that spectrum.
- You want the desktop experience to be stable today: it is labelled beta.
- You need a support contract or a company to escalate to.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Model freedom | Very strong | The core proposition: no vendor's model is privileged |
| Ecosystem pull | Very strong | Treated as a first-class target by harnesses, skill layers, and review tools alike |
| Install and distribution | Very strong | Eight-plus package managers plus a desktop build |
| Delivery surfaces | Strong | Terminal first; desktop app in beta |
| Governance | Medium | Community project under MIT, recently moved organizations |
| Auditability | Medium | Open, but large — this is not a loop you read in one sitting |

## Relationship To The Rest Of This Map

On the [harness route](../comparisons/agent-harness-frameworks.md), OpenCode is usually the thing being *driven* rather than the driver: [QM](qm.md) and [Omnigent](omnigent.md) both run it alongside Claude Code and Codex. That is the clearest signal of what it actually is — a dependable, vendor-neutral loop that other layers are comfortable building on.

## Bottom Line

If your requirement is "a serious coding agent that no model vendor controls", this is the default answer and has been for a while. Its absence from this map until now was an oversight, not a judgment — and the fact that five other profiles already depended on it is the evidence.
