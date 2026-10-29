# Google Antigravity

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/antigravity.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](antigravity.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Antigravity is Google's agent-first development platform. It started in November 2025 as an IDE with an Agent Manager bolted on, and since May 2026 it is a family of surfaces (a standalone agent app, a terminal CLI, extensions for six editors, the original IDE, and a Python SDK) that all run the same Google agent harness against Gemini models, with Claude available on paid plans.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Google |
| Route | Editor-centric (standalone IDE plus editor extensions), with an agent-manager desktop app and a CLI on the same harness |
| Open source | No. The app and IDE are closed. The [`antigravity-cli`](https://github.com/google-antigravity/antigravity-cli) repo holds a README, changelog and examples, no source and no licence file. The [Python SDK](https://github.com/google-antigravity/antigravity-sdk-python) is Apache-2.0 but needs a compiled runtime binary that ships only in the PyPI wheels |
| Best for | Developers on Gemini who want local agents they can run in parallel and watch, with browser use and plan review built in, and who want a usable free tier |
| Main cost | Quotas are not published as numbers and Google says they can change; no bring-your-own-key; the product spans five surfaces that move at different speeds; terms forbid using your Antigravity login from third-party agents |
| Status (2026-10-30) | Launched as a free public preview on 2025-11-18; the pricing page now labels the subscription plans "Generally Available". The SDK is in preview, and enterprise support in the JetBrains, Zed, Xcode and Eclipse extensions is in preview |
| Current versions (2026-10-30) | App v2.28.1 (2026-10-28) · CLI v1.4.0 (2026-10-16) · standalone IDE v2.6.0 (2026-10-26) · VS Code extension v1.10.0 (2026-10-26) · SDK v0.1.22 (2026-10-12) |
| Platforms | macOS 12+ (Apple Silicon and Intel), Windows 10 64-bit+ (x64 and ARM64), Linux with glibc 2.28+ (x64 and ARM64), Googlebook |
| Official site | https://antigravity.google |

## Why This Entry Exists

The map named Antigravity four times without a page for it. [Gemini CLI](gemini-cli.md) called it "not yet profiled" until this entry, [Gemini Task](gemini-task.md) runs on its harness, and [CodeGraph](codegraph.md), [Omnigent](omnigent.md), [Graphify](graphify.md), [ECC](ecc.md) and [Orca](orca.md) list it as an integration target. On the editor-centric route the map profiled [Cursor](cursor.md) and [Windsurf](windsurf.md) and nothing from Google.

The gap also hid a change that matters for selection. On 2026-05-19 Google's developer blog announced that Gemini CLI is being folded into Antigravity: from 2026-06-18, Gemini CLI and the Gemini Code Assist IDE extensions stopped serving requests for Google AI Pro and Ultra subscribers and for free users of Gemini Code Assist for individuals. Code Assist Standard and Enterprise licences and paid Gemini API keys keep working. Gemini CLI's own quota page now opens with the banner "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." For an individual developer on Google's stack, Antigravity is now the first-party coding product.

## What It Is

Google's docs describe one agent harness and several ways in. All of them share one sign-in.

| Surface | What it is |
| --- | --- |
| Antigravity App (2.0) | Standalone desktop app with no editor, launched 2026-05-19. Google describes it as the Agent Manager grown into its own product. Conversations are grouped by project, and a project can span several folders. It has subagents, hooks, worktrees, Automations (cron-style scheduled runs, renamed from Scheduled Tasks in v2.21.1), `/plan` for a reviewed plan before coding (v2.17.0), `/goal`, `/schedule`, `/browser`, voice transcription, and a built-in browser and PDF viewer since v2.28.0 (2026-10-27) |
| Antigravity CLI (`agy`) | Terminal client written in Go, on the same harness as the app, with shared settings. Installed with `curl -fsSL https://antigravity.google/cli/install.sh \| bash` (macOS, Linux, Googlebook) or a PowerShell or CMD script on Windows, then launched as `agy`; it signs in through the OS keyring or a browser flow. It draws on the same plan quota and model list as the app (the models page lists App, CLI and IDE together), shows remaining AI credits in its status line, and has a `useG1Credits` setting for overage. CLI sessions can be exported into the app. `agy -p` is the headless mode for scripts and CI |
| Antigravity IDE (standalone) | The original product: an Editor view with Tab completion, inline natural-language commands and an agent side panel; an Agent Manager for running several agents across workspaces; Artifacts (task lists, implementation plans, walkthroughs, screenshots, browser recordings) that you comment on to steer the agent. A browser subagent drives local Chrome in a separate profile with allow and deny lists |
| IDE extensions | VS Code, Visual Studio 2026, JetBrains IDEs, Zed, Xcode and Eclipse (Eclipse is a public preview) |
| Antigravity SDK | Python SDK (`pip install google-antigravity`) for building your own agents on the harness; in preview |

Also shipped: a Plugin Marketplace (announced 2026-10-29, rolling out gradually) for bundles of MCP configs, skills, rules, hooks and custom agents, in the app and through `agy plugin install`; and Remote Control (announced 2026-08-21), which lets you drive sessions on your other machines from a web browser, with push notifications when an agent needs input.

Where the IDE stands: when 2.0 shipped, existing IDE users were moved to the app automatically but could keep the IDE, which Google still recommended to developers, and Google said an upcoming release would remove the Agent Manager from the IDE. The IDE went from v2.5.5 (2026-08-13) to v2.6.0 (2026-10-26) with nothing in between, while the app shipped more than ten releases over the same stretch. Enterprise sign-in does not work in the standalone IDE, and Google's enterprise docs say it is not supported for enterprise deployments. The extensions are where Google points organisations that want Antigravity inside an editor.

## Models (as of 2026-10-30)

From Google's "Choose a model" page. Each model has Low, Medium or High thinking levels.

| Model | Free and Google AI Plus | Google AI Pro | Google AI Ultra | Enterprise |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | No | Yes (paid plans, or trial on eligible devices) | Yes | Yes |
| Gemini 3.8 Flash | Yes | Yes | Yes | Yes |
| Gemini 3.7 Flash, 3.6 Flash, 3.1 Pro | No | No | No | Yes |
| Claude Sonnet 5.5 and Opus 5.5 (thinking) | No | Yes (paid, not trial) | Yes | Yes (admin opt-in, billed by token) |
| Claude Sonnet 4.6 and Opus 4.6 (thinking) | Yes, removed 2026-11-02 | Yes, removed 2026-11-02 | No | No |
| GPT-OSS-120b | Yes, removed 2026-11-02 | Yes, removed 2026-11-02 | Yes, removed 2026-11-02 | No |

Reading the table: after 2026-11-02 the free tier's only reasoning model is Gemini 3.8 Flash, and Claude stays only on paid Pro, Ultra and Enterprise. Gemini and the third-party models draw on separate quotas, each with a weekly limit and a five-hour limit. Image generation uses Nano Banana 2 and cannot be changed. Automations default to Flash (v2.24.0). When signed in with Google Cloud Application Default Credentials, the app and CLI can also offer Claude Opus 5.5 and Sonnet 5.5 if your Vertex AI project has access.

## Pricing And Limits (as of 2026-10-30)

| Plan | Price (US, per month) | What Antigravity gets |
| --- | --- | --- |
| Free (Individual) | $0 | A quota refreshed weekly, a weekly rate limit, unlimited Tab completions and Command requests |
| Google AI Pro | $19.99 | A quota refreshed every five hours until a weekly limit is reached |
| Google AI Ultra | $99.99 or $199.99 | Google's plans page puts these at 5x and 20x Pro's limits; third-party models; the highest weekly limits |
| Business via Google Cloud | Gemini Enterprise Standard and Plus from $30 per seat; or pay-as-you-go with no seat fee | App, CLI and IDE extensions; seat credits of $10 (Standard) or $15 (Plus) a month for first-party models; third-party models billed by token |

Details that change the arithmetic:

- Google publishes no request or token numbers for any plan. The plans page says limits track "the amount of work done by the agent", are set mainly by available capacity, and "are subject to modification".
- Pro and Ultra can buy AI credits for overage, charged at Gemini Enterprise consumption prices. A setting controls whether credits are spent automatically (Never or Always).
- No bring-your-own-key or custom endpoint for extra capacity, and no custom-contract organisational tier.
- Sign-in needs a personal Google account aged 18+ in a supported country, or an organisation that has provisioned Antigravity. As of 2026-10-30, mainland China, Hong Kong, Macau and Russia are not on Google's list of supported countries and territories.

## When To Pick It

- You work on Gemini and want Google's own harness. Google says Gemini models are co-optimised with it, and Argon reached Antigravity on 2026-10-13.
- You want to run several local agents at once and supervise them from one place: projects, subagents you can message directly, worktrees, Automations, and Remote Control from a browser.
- Your work needs browser verification. The agent can open and drive a browser, record what it did, and hand back screenshots and recordings as artifacts you comment on.
- You want plan review before code: `/plan` and implementation-plan artifacts are built in.
- You need a free tier for real evaluation. It is weekly-capped and, from 2026-11-02, Gemini-only.
- You are coming from Gemini CLI. `agy` reads `GEMINI.md` and `AGENTS.md`, and `agy plugin import gemini` converts extensions to plugins. Workspace skills have to move from `.gemini/skills/` to `.agents/skills/`, and MCP servers move into `mcp_config.json`. Google says parity is not 1:1.
- Your organisation is already on Gemini Enterprise. App, CLI and extensions inherit its IAM, VPC Service Controls and data-residency controls, and Google says enterprise code and prompts are never used to train its foundation models.

## When Not To Pick It

- You need open source or self-hosting. Nothing here qualifies except the SDK's Python layer, and that still needs Google's compiled runtime.
- You want to plan around a known budget. Without published quota numbers, the only way to know whether Pro is enough is to run your workload on it.
- You want to bring your own model key or use the subscription from other tools. Google's FAQ says using third-party software (it names Claude Code, OpenClaw and OpenCode) with an Antigravity login violates the terms and can get the account suspended, and wrapping `agy` inside third-party agents is not supported on consumer plans. For Gemini inside another agent, Google points to a Gemini Enterprise or AI Studio API key.
- You want the standalone IDE as an enterprise standard. It is not supported for enterprise, and its release pace now trails the app.
- You are in mainland China, Hong Kong, Macau or Russia, or under 18.
- You want one stable surface. Since May 2026 the centre of the product has been the agent app, and a team choosing Antigravity has to decide between app, CLI, IDE and extensions.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Parallel agent supervision | Very strong | Projects, subagents, worktrees, Automations; the app is built around it |
| Editor workflow | Strong | Standalone IDE plus extensions for six editors; the IDE itself is no longer where Google ships first |
| Browser use | Strong | Browser subagent in the IDE, built-in browser in the app since v2.28.0, recordings as artifacts |
| Plan and review | Strong | Implementation plans, walkthroughs, comments on artifacts, `/plan` with a plan review policy setting |
| Remote operation | Strong | Remote Control from a web browser, push notifications |
| Model choice | Medium | Gemini plus Claude 5.5 on paid plans; free is Gemini-only from 2026-11-02; no BYOK |
| Free tier | Medium | Real, but weekly-capped with no published numbers |
| Enterprise | Strong, with a gap | App, CLI and extensions under Gemini Enterprise; standalone IDE excluded; four extensions in enterprise preview |
| Open source | Weak | Closed app and IDE; CLI repo has no source; SDK Apache-2.0 over a compiled binary |

## Relationship To Gemini CLI And Jules

Google appears on this map at four points, and Antigravity now connects most of them.

- [Gemini CLI](gemini-cli.md) was Google's open-source terminal agent. Antigravity CLI took inspiration from its harness and is where consumer users were sent after 2026-06-18. Gemini CLI still runs with Code Assist Standard or Enterprise licences and with paid API keys.
- [Jules](jules.md) is a different shape. Google's Jules page describes an agent that clones a GitHub repo into a cloud VM, plans, shows a diff and opens a PR, and Google's plan page lists Jules limits separately from Antigravity limits. Antigravity's agents run on your own machine (or one you reach through Remote Control). Choose Jules to hand off a task and get a PR back; choose Antigravity to sit with the agent while it works. The 2.0 announcement lists cloud-deployed agents as planned, so this line may move.
- [Gemini Task](gemini-task.md), the consumer agent in the Gemini app, runs on the Antigravity harness, per the I/O announcement cited in that profile.

## Operating Cost

Medium. Install is a download or a one-line script, and sign-in is a Google account. The ongoing cost is in three decisions: which surface your team standardises on, whether the unpublished quota on your plan covers your workload, and how you handle the 2026-11-02 model removals if you depend on Claude 4.6 or GPT-OSS on the free tier. Releases are frequent (the app shipped v2.21 to v2.28 in October 2026 alone) and auto-update by default; Google's releases page notes you can set updates to manual or off.

## Bottom Line

Antigravity is Google's answer on the editor-centric route, and since May 2026 it is also Google's answer for the terminal. Its strengths are parallel local agents you can watch, browser verification and plan review, and a free tier you can actually evaluate with. The costs are a closed product bound to a Google account, quotas you cannot size in advance, no way to bring your own key or reuse the subscription in other tools, and a product line that has moved its centre from the IDE to the agent app. If you want the editor itself to stay the centre, compare it against [Cursor](cursor.md) and [Windsurf](windsurf.md) before committing.

## Sources

All read 2026-10-30.

- Product: [antigravity.google](https://antigravity.google/) · [Antigravity IDE](https://antigravity.google/product/antigravity-ide) · [Download (versions and requirements)](https://antigravity.google/download) · [Releases (update modes)](https://antigravity.google/releases) · [Pricing](https://antigravity.google/pricing)
- Docs: [Overview](https://antigravity.google/docs/overview/) · [Choose a model](https://antigravity.google/docs/models/) · [Plans](https://antigravity.google/docs/plans/) · [FAQ (regions, age, third-party use)](https://antigravity.google/docs/faq/) · [Enterprise](https://antigravity.google/docs/enterprise/) · [Authenticate](https://antigravity.google/docs/install/) · [IDE extensions](https://antigravity.google/docs/ide/extensions/) · [IDE browser](https://antigravity.google/docs/ide/browser/) · [Migrating from Gemini CLI](https://antigravity.google/docs/cli/gcli-migration/) · [Changelog (App v2.28.1, CLI v1.4.0, IDE v2.6.0, extensions v1.10.0, SDK v0.1.22)](https://antigravity.google/docs/changelog/)
- Blog: [Introducing Google Antigravity (2025-11-18)](https://antigravity.google/blog/introducing-google-antigravity) · [Antigravity @ I/O 2026 (2026-05-19)](https://antigravity.google/blog/google-io-2026) · [Introducing Antigravity 2.0 (2026-05-19)](https://antigravity.google/blog/introducing-google-antigravity-2) · [Introducing Antigravity CLI (2026-05-19)](https://antigravity.google/blog/introducing-google-antigravity-cli) · [Changes to Antigravity plans (2026-05-19)](https://antigravity.google/blog/changes-to-antigravity-plans) · [Remote Control (2026-08-21)](https://antigravity.google/blog/remote-control-for-antigravity) · [Gemini 4 Argon in Antigravity (2026-10-13)](https://antigravity.google/blog/gemini-4-argon-in-google-antigravity) · [Plugin Marketplace (2026-10-29)](https://antigravity.google/blog/plugin-marketplace-in-antigravity)
- [Gemini CLI quota and pricing (replacement banner)](https://geminicli.com/docs/resources/quota-and-pricing) · [Antigravity CLI AI credits](https://antigravity.google/docs/cli/credits/)
- [Google Developers Blog: Transitioning Gemini CLI to Antigravity CLI (2026-05-19)](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Google AI plans (US prices)](https://gemini.google/us/subscriptions/?hl=en) · [Jules](https://jules.google/)
- GitHub: [google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli) · [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python)
