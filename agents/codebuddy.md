# CodeBuddy (Tencent)

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/codebuddy.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](codebuddy.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CodeBuddy is Tencent Cloud's coding product line, sold in three forms (editor plugin, standalone CodeBuddy IDE, and the terminal agent CodeBuddy Code). This map files it on the direct-execution route because the terminal CLI is where it competes with the vendor CLIs here. It is a Claude-Code-shaped loop with a multi-vendor model catalog and Tencent's enterprise deployment options.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Tencent Cloud (same "Buddy AI" family as [WorkBuddy](workbuddy.md)) |
| Route | Direct execution (terminal CLI, CodeBuddy Code). The plugin and the IDE are editor-centric surfaces of the same account |
| Surfaces | Plugin for VS Code, JetBrains IDEs, Visual Studio, Xcode and WeChat DevTools; CodeBuddy IDE (Windows 10+, macOS 11+); CodeBuddy Code CLI (macOS, Linux, Windows) |
| Editions | International ([codebuddy.ai](https://www.codebuddy.ai)) and China ([copilot.tencent.com](https://copilot.tencent.com)); the CLI also routes to iOA, dedicated-cloud and self-hosted enterprise deployments |
| Open source | **No public source.** The npm package carries an MIT license file but ships a minified bundle; the public repo on Tencent's CNB holds docs, samples, the changelog and issues. On GitHub the only repo is `Tencent-CodeBuddy/homebrew-tap` (the Homebrew formula) |
| Models | Built-in catalog served by Tencent per edition (docs name Hunyuan and DeepSeek; Hy3 preview added to the China edition in CLI v2.93.4, 2026-04-23); any OpenAI-format endpoint through `models.json` or `CODEBUDDY_BASE_URL` |
| Best for | Teams on Tencent Cloud or in the Chinese enterprise stack who want one vendor for plugin, IDE and CLI, with private-cloud options |
| Main cost | Credit-metered plans; the source is closed; no fixed published model list |
| Current version | CodeBuddy Code 2.178.1 (2026-10-29); CodeBuddy IDE 4.12.2 on the China release notes (2026-10-14) |
| Install | `npm install -g @tencent-ai/codebuddy-code` (Node.js 18.20+), `brew install Tencent-CodeBuddy/tap/codebuddy-code`, or the native binary (beta) |

## Why This Entry Exists

The map already profiles Tencent's office agent [WorkBuddy](workbuddy.md) and its consumer assistant [Yuanbao](yuanbao.md), and both pages point at CodeBuddy as the Tencent tool for repositories without profiling it. This page closes that gap.

**WorkBuddy vs CodeBuddy.** Tencent's China pricing page uses "Buddy AI" as the umbrella name for WorkBuddy, CodeBuddy and related products, and states that CodeBuddy and WorkBuddy **share one account and one credit balance**, so you do not subscribe twice. The split is by object of work: WorkBuddy acts on documents, decks and spreadsheets; CodeBuddy acts on a code repository. The two are also closer under the hood than the product pages suggest: CodeBuddy Code's own v2.176.0 release notes list fixes under "Resident service (WorkBuddy)". That points to WorkBuddy running on the CodeBuddy Code engine, but Tencent has not published an architecture description, so treat it as an inference from the changelog. Tencent's Hy3 announcement (2026-07-06) lists WorkBuddy/CodeBuddy together among the products the model is wired into.

## The Three Surfaces

| Surface | Who Tencent aims it at | Shape |
| --- | --- | --- |
| CodeBuddy plugin | "Everyday coding developers / users of a specific IDE" | Completion, chat and agent inside your existing editor. Minimum versions listed: VS Code 1.82, JetBrains IDEs 2022.2, Android Studio Flamingo, Visual Studio 2022, Xcode 14.0, WeChat DevTools 1.06.2409140 |
| CodeBuddy IDE | "Product managers / designers / full-stack developers / programming beginners" | Standalone editor sold as "conversation as programming": PRD generation, Figma-to-code, built-in Supabase and Tencent CloudBase, one-click deploy to CloudStudio or EdgeOne Pages |
| CodeBuddy Code | "DevOps / operations / SRE / senior developers" | Terminal agent with shell, file and network tools, headless mode, SDKs and IDE bridges |

The IDE is the vibe-coding end and overlaps with [Cursor](cursor.md) and [Windsurf](windsurf.md). The CLI is the part that belongs in the [terminal coding CLI comparison](../comparisons/coding-cli-agents.md), which is why the route above is direct execution.

## How CodeBuddy Code Compares To The Vendor CLIs

The loop is the Claude Code shape, and the docs make that obvious: `CODEBUDDY.md` and `AGENTS.md` instruction files, Shift+Tab into plan mode, permission modes named `default`, `acceptEdits`, `plan`, `bypassPermissions` and `auto`, plus hooks, skills, plugins and marketplaces, sub-agents, checkpoints with `/rewind`, and `-p` headless runs. If you know [Claude Code](claude-code.md), there is little to relearn. What differs:

- **Model catalog.** [Claude Code](claude-code.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md) and [Grok Build](grok-build.md) are tuned around their vendor's own model. CodeBuddy's built-in list is multi-vendor and served from Tencent's backend per edition; Tencent's own Hunyuan/Hy3 is one option, not the whole point. It also routes `lite` and `reasoning` sub-tasks to cheaper or stronger models automatically.
- **Deployment editions.** One CLI switches between international, China, iOA, dedicated-cloud and self-hosted backends (`CODEBUDDY_INTERNET_ENVIRONMENT`, plus an enterprise `endpoint`). Enterprises get OAuth client credentials through `apiKeyHelper`.
- **Chinese messaging reach.** Channels (beta) push WeChat, Telegram and Discord events into a live session, and there is a WeCom bot setup guide. Remote Control (beta) exposes the local session to a phone or browser.
- **IDE reach.** `codebuddy --acp` runs it as an ACP agent server for Zed; `--ide` attaches it to the VS Code, Cursor, Windsurf and JetBrains plugins over a local MCP connection.
- **SDKs.** `@tencent-ai/agent-sdk` (npm, MIT) and `codebuddy-agent-sdk` (PyPI) ship in lockstep with the CLI.
- **Openness.** [Kimi Code](kimi-code.md) and [MiMoCode](mimocode.md) are open-source MIT projects; [Qwen Code](qwen-code.md) and [Gemini CLI](gemini-cli.md) are Apache-2.0. CodeBuddy Code is a closed bundle with an MIT license file, closer to [Claude Code](claude-code.md) in practice.
- **Release cadence.** The release notes show near-daily versions (2.161.0 on 2026-10-01 to 2.178.1 on 2026-10-29).

## When To Pick It

- You are on **Tencent Cloud** or in the Chinese enterprise stack (WeChat, WeCom, Tencent unified identity) and want plugin, IDE and CLI under one vendor and one bill.
- You need a **dedicated-cloud or self-hosted** edition of the same CLI your developers use, with OAuth-based enterprise sign-in.
- You want a Claude-Code-style terminal loop but **not tied to one model vendor**: the built-in catalog spans vendors, and `models.json` accepts any OpenAI-format endpoint (the docs show DeepSeek and OpenRouter examples).
- Your team mixes roles: product and design people on CodeBuddy IDE, engineers on the plugin or CLI, all sharing one account. If the same people also do office work, the credits are shared with [WorkBuddy](workbuddy.md) on the China edition.

## When Not To Pick It

- **You want to read or patch the agent.** There is no public source; the MIT file covers a minified bundle. For an open terminal loop from a Chinese vendor, pick [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md) or [Qwen Code](qwen-code.md).
- **You want to know exactly which model runs.** The built-in list is served per account and edition and is not published as a fixed list; plan on checking `/model` in your own install.
- **You want the deepest tuning for one model.** If you have already settled on Claude, GPT or Kimi, that vendor's own CLI is the better-tuned path (see [How To Choose](../comparisons/coding-cli-agents.md#how-to-choose)).
- **You need a stable surface.** Near-daily releases and several beta features (native binary, Channels, Remote Control) mean the details move under you. The international IDE release-notes page also lags the China one (4.10.4 on 2026-07-22 vs 4.12.2 on 2026-10-14 when read), so check the edition you use.
- **Name collision.** Several unrelated VS Code extensions are also called "CodeBuddy". Tencent's plugin is published by `Tencent-Cloud` (`Tencent-Cloud.coding-copilot`).

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Strong | Claude-Code-shaped loop: plan mode, permission modes, hooks, skills, plugins, sub-agents, checkpoints |
| Surface coverage | Very strong | Plugin for VS Code, JetBrains, Visual Studio, Xcode and WeChat DevTools, a standalone IDE, and a CLI on one account |
| Model freedom | Strong | Multi-vendor built-in catalog plus any OpenAI-format endpoint; built-in list not published |
| Enterprise deployment | Very strong | International, China, iOA, dedicated-cloud and self-hosted editions; OAuth via `apiKeyHelper` |
| IDE / ACP integration | Strong | `--acp` for Zed; `--ide` bridge to VS Code, Cursor, Windsurf and JetBrains plugins |
| Remote / messaging | Medium | Channels and Remote Control are both beta; WeChat, WeCom, Telegram, Discord |
| Headless / automation | Strong | `-p` mode, GitLab CI/CD guide, scheduled tasks, JS and Python SDKs |
| Open source / auditability | Low | MIT license file on a minified bundle; no public source repository |

## Pricing (read 2026-10-30)

Credits are the unit for both editions; different models consume different amounts. Promotional bonuses below are Tencent's own "limited-time" figures and will change.

| Edition | Plan | Price | Credits / month |
| --- | --- | --- | --- |
| International | Free | $0 | 100 (plus a limited-time daily bonus) |
| International | Pro | $10 / month or $96 / year | 1,000 base + 1,000 bonus |
| International | Team | $40 / seat / month or $480 / seat / year | 1,000 per seat, pooled |
| China | 体验版 (trial) | Free | 500 |
| China | 标准版 / 高级版 / 旗舰版 | ¥99 / ¥199 / ¥999 per month (lower on auto-renew or annual) | 2,000 / 4,000 / 20,000 base, plus limited-time bonus |
| China | Enterprise SaaS (旗舰版) | ¥198 / seat / month, from 1 seat | 2,000 per seat, pooled |
| China | Enterprise private cloud (专享版) | ¥316 / seat / month, from 100 seats | 2,000 per seat, pooled |

The China tiers took effect on 2026-07-01, when the single paid plan was split into three. On the China edition the same credits cover WorkBuddy.

## Bottom Line

CodeBuddy covers more surfaces from one vendor than most entries here: a plugin, a vibe-coding IDE and a Claude-Code-shaped CLI under one account, with editions that reach into private clouds. Pick it if Tencent Cloud or the Chinese enterprise stack is already your environment, or if you need a CLI your company can host itself. Skip it if you want to read the agent's source or tie the loop to one model; [Kimi Code](kimi-code.md), [Qwen Code](qwen-code.md) and the vendor CLIs serve those better. For Tencent's office-work sibling on the same credits, see [WorkBuddy](workbuddy.md).

## Sources

All read 2026-10-30.

- Tencent Cloud product docs: [CodeBuddy product introduction](https://cloud.tencent.com/document/product/1831/134343) (last updated 2026-08-14)
- CodeBuddy docs (international): [IDE introduction](https://www.codebuddy.ai/docs/ide/Introduction) · [IDE installation](https://www.codebuddy.ai/docs/ide/Getting-Started/Installation) · [IDE models.json](https://www.codebuddy.ai/docs/ide/Features/models) · [Pricing](https://www.codebuddy.ai/docs/ide/Account/pricing) · [Credits](https://www.codebuddy.ai/docs/ide/Account/credits) · [IDE release notes](https://www.codebuddy.ai/docs/ide/release-notes/release-notes)
- CodeBuddy docs (China): [IDE introduction (three forms, plugin minimum versions)](https://copilot.tencent.com/docs/ide/Introduction) · [IDE installation](https://copilot.tencent.com/docs/ide/Getting-Started/Installation) · [定价 / pricing](https://copilot.tencent.com/docs/ide/Account/pricing) · [IDE release notes](https://copilot.tencent.com/docs/ide/release-notes/release-notes)
- CodeBuddy Code docs: [Overview](https://www.codebuddy.ai/docs/cli/overview) · [Installation](https://www.codebuddy.ai/docs/cli/installation) · [Identity and access management](https://www.codebuddy.ai/docs/cli/iam) · [Models](https://www.codebuddy.ai/docs/cli/models) · [Costs](https://www.codebuddy.ai/docs/cli/costs) · [IDE integrations](https://www.codebuddy.ai/docs/cli/ide-integrations) · [ACP](https://www.codebuddy.ai/docs/cli/acp) · [Permission modes](https://www.codebuddy.ai/docs/cli/permission-modes) · [Headless](https://www.codebuddy.ai/docs/cli/headless) · [Channels](https://www.codebuddy.ai/docs/cli/channels) · [SDK](https://www.codebuddy.ai/docs/cli/sdk)
- CodeBuddy Code release notes: [v2.178.1 (2026-10-29)](https://www.codebuddy.ai/docs/cli/release-notes/v2.178.1) · [v2.176.0 ("Resident service (WorkBuddy)" fixes)](https://www.codebuddy.ai/docs/cli/release-notes/v2.176.0) · [v2.93.4 (Hy3 preview, 2026-04-23)](https://www.codebuddy.ai/docs/cli/release-notes/v2.93.4)
- Packages: [`@tencent-ai/codebuddy-code` on npm](https://www.npmjs.com/package/@tencent-ai/codebuddy-code) (2.178.1, LICENSE.txt is MIT text) · [`@tencent-ai/agent-sdk` on npm](https://www.npmjs.com/package/@tencent-ai/agent-sdk) · [`codebuddy-agent-sdk` on PyPI](https://pypi.org/project/codebuddy-agent-sdk/) · [`Tencent-Cloud.coding-copilot` on the VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Tencent-Cloud.coding-copilot)
- Repositories: [cnb.cool/codebuddy/codebuddy-code](https://cnb.cool/codebuddy/codebuddy-code) (docs, samples, changelog, issues) · [Tencent-CodeBuddy/homebrew-tap](https://github.com/Tencent-CodeBuddy/homebrew-tap)
- [Tencent Hunyuan officially releases Hy3 (Tencent newsroom, 2026-07-06)](https://www.tencent.com/zh-hk/tencent-hunyuan-officially-releases-hy3-advancing-agent-capabilities-and-deeper-product-integration/)
