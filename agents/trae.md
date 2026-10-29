# TRAE

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/trae.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](trae.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: TRAE is ByteDance's AI IDE, sold as two editions with separate accounts, models and prices: TRAE international (trae.ai, billed in dollars against model token prices, with GPT, Gemini, Kimi and others, plus Claude and Grok for US users) and TRAE China (trae.cn, billed in credits, Chinese models only). Since October 2026 one desktop app holds a VS Code-style IDE window with an AI-led SOLO mode and a separate Agent window for parallel, cloud and scheduled tasks, with web and mobile clients on the same account.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | ByteDance. The international service outside the US is provided by SPRING (SG) PTE. LTD., Singapore (privacy policy) |
| Route | Editor-centric: an IDE window (IDE mode and SOLO mode) plus an Agent window for multi-agent, cloud and scheduled tasks |
| Editions | International: [trae.ai](https://www.trae.ai), [docs.trae.ai](https://docs.trae.ai). China: trae.cn, [docs.trae.cn](https://docs.trae.cn). Different model lists, plans and currencies; the China edition is versioned separately (v3.4.x against v3.6.x on the same date) |
| Surfaces | TRAE Desktop (Agent window and IDE window), TRAE Web, TRAE Mobile; TRAE Plugin for VS Code and JetBrains IDEs; TRAE CLI 2.0 only on the China edition's enterprise flagship plan |
| Open source | The product is closed. [`bytedance/trae-agent`](https://github.com/bytedance/trae-agent) is a separate MIT-licensed research CLI agent (`trae-cli`, bring your own API key); last commit 2026-02-05. `Trae-AI/TRAE` holds only a two-line README |
| Best for | Developers who want a VS Code-compatible IDE with a low-cost entry tier, a wide built-in model list and a mobile client that dispatches tasks to the desktop or cloud; teams in China who want domestic models in an IDE |
| Main cost | Chat data can be used for analytics and model training unless you turn on Privacy Mode; the two editions differ enough to be two products; the free tier has no SOLO mode and its allowance is not published as a number; Claude is only on the US model list |
| Status (2026-10-30) | Shipping. TraeCode and TraeWork were merged into "the all-new TRAE" in October 2026 (v3.6.0, 2026-10-08, launched the Agent window) |
| Current versions (2026-10-30) | International v3.6.4 (changelog entry 2026-10-15, "v3.6.1 ~ 3.6.4"). China v3.4.4 (same date) |
| Platforms | macOS 12+ (Apple Silicon and Intel); Windows 10 and 11 (x64); Linux x64 and ARM64 (.deb for Ubuntu 20.04+ and Debian 10+, .rpm for Fedora 42 and RHEL 9.x). Up to 3 signed-in devices per account |
| Official site | https://www.trae.ai |

## Why This Entry Exists

The map listed TRAE only as an integration target in [Graphify](graphify.md). On the editor-centric route it profiled [Cursor](cursor.md), [Windsurf](windsurf.md) and [Google Antigravity](antigravity.md), and nothing from ByteDance, which also appears here through [Doubao](doubao.md). TRAE is the editor-centric product of the Chinese vendors on this map; Tencent's [CodeBuddy](codebuddy.md) is filed under direct execution because its terminal CLI is where it competes.

Two changes in 2026 also make older descriptions of TRAE wrong. On 2026-05-08 (v3.5.56) the separate Builder agents were merged into one built-in "Agent" and SOLO Coder was renamed SOLO Agent. In October, TraeCode (the IDE) and TraeWork (the agent workspace with web, desktop and mobile apps) were merged into one product, and the old TraeWork desktop app migrates its data and can uninstall itself.

## What It Is

The docs describe three clients, two desktop windows and two modes inside the IDE window.

| Part | What it is |
| --- | --- |
| IDE window, IDE mode | A code-editor workspace with VS Code extension support, split editing, terminal, debugger and Git. Setup can import configuration from VS Code or Cursor. Chat, inline chat, CUE completion (multi-line edits, next-edit prediction, smart import and rename in Python, TypeScript and Go), and agents that search the codebase, plan and run tools |
| IDE window, SOLO mode | "AI takes the lead." The built-in Agent writes a plan, waits for you to confirm it, then works through code, tests, preview and a change summary. Tool panels for editor, browser and doc viewer; parallel tasks inside one project; Figma to code; built-in Supabase, Vercel deployment, AI service and Stripe payment integrations; DiffView for the change set |
| Agent window | Added in v3.6.0 (2026-10-08). A task workspace that runs several agent tasks across projects and runtimes: local folders, several paths mounted into one project, a directory on a remote host over SSH, worktrees, or a cloud environment built from TRAE's base container image. Also holds Automation (scheduled tasks), the plugin Marketplace (plugins and skills, launched 2026-09-20) and My Artifacts (code changes, HTML, slides, documents, images, videos) |
| TRAE Web | Cloud-only. Cloud tasks sync between Web, Mobile and the Agent window |
| TRAE Mobile | Dispatches and monitors tasks on the cloud or on your own computers. Linking to the desktop lasts 180 days and can only reach projects open in TRAE Desktop; when a device is offline the task moves to the cloud |
| TRAE Plugin | Completion, chat, code explanation, review and fixes inside VS Code and JetBrains IDEs (Android Studio included) |

Under all of these: MCP servers, custom agents with their own prompts and toolsets, skills, rules, slash commands, hooks (v3.5.66, 2026-06-10), subagent definitions loaded from `.trae/agents` (beta switch, v3.5.67), global and project memories, browser use, and connectors for GitHub and Lark or Feishu. Max mode, per model, raises the context window to up to 1M tokens and allows up to 200 tool-call rounds in one task; the docs warn it "will significantly increase costs".

## Is There A CLI?

Not on the international edition, as of 2026-10-30. The TRAE Enterprise page on trae.ai lists "CLI (coming soon)".

On the China edition, docs.trae.cn documents **TRAE CLI 2.0** (`traecli`), a terminal coding agent for macOS, Linux and Windows (WSL2 recommended) with an interactive TUI, a non-interactive `traecli exec` for scripts and CI, plugins, skills, MCP, an Agent Client Protocol server mode for editors, directory trust, and three permission modes (Workspace Edit, Auto-Review, Full Access). Its own page states the limit: it is available only to customers on the TRAE Enterprise flagship plan (旗舰版). TRAE CLI 1.0 is in "weak maintenance". Its migration prompt can import Claude Code subagents and sessions and convert `CLAUDE.md` to `AGENTS.md`.

So this entry does not put TRAE in [terminal coding CLI agents](../comparisons/coding-cli-agents.md): an individual developer cannot install a TRAE CLI on either edition. The open-source [`bytedance/trae-agent`](https://github.com/bytedance/trae-agent) does have a CLI (`trae-cli run`, `trae-cli interactive`), but its README describes it as a research-friendly agent for "studying AI agent architectures", it runs on your own provider keys, nothing in TRAE's docs says the IDE uses it, and the repo's last commit is 2026-02-05.

## Models (as of 2026-10-30)

International edition, from the "Built-in models & custom models" page (updated 2026-10-26). The list depends on where you are:

| Region | Built-in models |
| --- | --- |
| Outside the US | GPT-6-Astra, GPT-6-Sol, GPT-6-Luna, GPT-5.6-Sol, GPT-5.6-Terra, GPT-5.6-Luna, GPT-5.5, GPT-5.4, GPT-5.2; Gemini-3.1-Pro-Preview, Gemini-3-Flash-Preview; Seed-2.1-Turbo; GLM-5.2; DeepSeek-V4-Flash; Kimi-K3, Kimi-K2.7-Code, Kimi-K2.5; MiniMax-M3, MiniMax-M2.7. No Claude |
| US | GPT-6.1-Sol, GPT-6-Sol, GPT-6-Luna, GPT-6-Astra, GPT-5.6-Sol, GPT-5.6-Terra, GPT-5.6-Luna, GPT-5.5; Grok-4.7, Grok-4.6; Claude Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 5, Sonnet 5, Opus 4.8, Opus 4.7, Sonnet 4.6, Haiku 4.5; Gemini-3.1-Pro-Preview, Gemini-3.1-Flash-Preview, Gemini-2.5-Pro, Gemini-2.5-Flash; Kimi-K2-0905 |

Each model has a published per-million-token price for input, cache read, cache write and output, and that is what your plan allowance is charged at. Two examples from the US table: Claude Opus 5.5 at $4.00 input and $20.00 output; GPT-6-Astra at $10.00 input and $50.00 output up to 272k context. The newest models (GPT-6.x, GPT-5.6, GPT-5.5, GLM-5.2, DeepSeek-V4-Flash, Kimi-K2.7-Code, Kimi-K3) are available only on the plans introduced in autumn 2026; legacy subscribers get them after upgrading.

Free users get Auto mode only, where TRAE picks a built-in model. Paid plans can also pick a model by hand. Any plan can add custom models: from a preset provider with your API key (including a provider's Coding Plan or Agent Plan quota), or any endpoint that speaks OpenAI Chat Completions or Anthropic Messages, with a custom base URL. Auto mode never uses your custom models.

China edition, from docs.trae.cn: Seed-Evolving (Pro and above), Seed-2.1-Pro-0915, Seed-2.1-Turbo, Seed-Code, MiMo-V2.6-Flash and -Pro, Step-5-Preview, GLM-5.3-FlashX, GLM-5.3-Flash, GLM-5.3, GLM-5.2, DeepSeek-V4.1-Flash, DeepSeek-V4-Flash, DeepSeek-V4-Pro, Kimi-K3, Kimi-K2.8-Preview, MiniMax-M3, Qwen3.8-Flash, Qwen3.8-Max and Qwen3.7-Plus. No GPT, Claude, Gemini or Grok. Custom models do not consume credits on this edition.

## Pricing And Limits (as of 2026-10-30)

International edition, from the pricing page and the "Plans & billing" doc (updated 2026-10-26):

| Plan | Monthly | Annual | Usage included per month | Concurrent cloud tasks | Notes |
| --- | --- | --- | --- | --- | --- |
| Free | $0 | $0 | "Limited" (no number published) | 2 | Auto mode only; standard queue; autocompletion limited (5,000 a month on the pricing page); no SOLO mode |
| Lite | $8 | $80 | $8 | 2 | Only in Thailand, Indonesia, Vietnam, the Philippines, India, Pakistan, Turkey, Malaysia, Brazil, Colombia, Peru and Nigeria |
| Pro | $20 | $200 | $20 | 10 | Manual model choice, fast queue, unlimited autocompletion, SOLO mode |
| Pro+ | $60 | $600 | $60 | 15 | As Pro |
| Ultra | $200 | $2,000 | $200 | 20 | Early access to new models |

How it is charged:

- Each model request is metered on its own: cost = tokens used × that model's list price. It comes out of the monthly dollar allowance first.
- After the allowance, On-Demand Usage (paid plans only, off until you switch it on) bills further tokens "according to the official standard API pricing of the model provider", charged each time $3 accrues. Without it, AI chat stops until the next cycle; free users wait for next month.
- Enterprise is sold separately (BytePlus on trae.ai). Refunds only within 24 hours of purchase and only if nothing was used. No student discount.
- Legacy subscribers who keep an unbroken monthly subscription keep their old price after moving to the new plans (the docs' example: Pro renewing at $10 a month); their allowance changes to the new plan's.

China edition, from docs.trae.cn "套餐与计费说明": billing is in credits, and only built-in models consume them.

| Plan | Single month | Auto-renew monthly | Credits a month | Concurrent cloud tasks |
| --- | --- | --- | --- | --- |
| Lite | ¥49 | ¥45 | 2,000 | 2 |
| Pro | ¥99 | ¥89 | 4,000 | 10 |
| Pro+ | ¥239 | ¥219 | 12,000 | 10 |
| Ultra | ¥699 | ¥629 | 40,000 | 20 |

Free users on the China edition get 500 credits a month for signing in, 2,000 once on sign-up, and 100 a day for checking in. Extra credits cost ¥50 per 1,000. Seed-2.1-Turbo and Seed-Code are charged at 25% of their normal rate for members, and a time-limited off-peak discount (22:00 to 08:00) halves DeepSeek V4 usage for free users. Payment is Douyin Pay, Alipay or WeChat Pay.

## Privacy And Data (as of 2026-10-30)

Read this before choosing TRAE. The terms are spread across four official pages.

- **Training on chats is the default unless you switch it off.** The Privacy mode doc (international and China, same text): "your information like your chat interactions, including related code snippets and AI-generated outputs, may be used for analytics, product improvement, and model training." Privacy Mode is a switch under Settings > Account; it only works while you are signed in, and stops when you sign out.
- **Codebase files are treated differently.** With or without Privacy Mode, TRAE says it does not use codebase files for analytics, product improvement or training. For codebase indexing it uploads the files temporarily to compute embeddings and then "permanently" deletes the plaintext.
- **Cloud tasks store your code.** The cloud-agent data policy says repository content you authorise, plus MCP, rules, memory, hooks and context, is stored in the cloud for the session and "will never be used for any model training". Chat and code for a cloud session are kept until you delete the session.
- **Who gets the data.** The international privacy policy (last updated 2026-05-20, covering use outside the US) names SPRING (SG) PTE. LTD. in Singapore as data controller; says data is stored on servers in Singapore and Malaysia and may be transferred elsewhere, including the United States; says AI chat inputs are shared with third-party model developers, naming Gemini (Google) and GPT (Microsoft); and says entities in ByteDance's corporate group process user data for functions that include "training and improving our Corporate Group's technologies". Retention is "as long as necessary", with account information and user content generally kept while you have an account.
- **US users are under a different policy.** The policy above excludes the US, and the docs give a separate US support address (`ussupport@mail.traeai.us`). This entry did not read a US-specific policy.
- **Enterprise is a different deal.** The trae.ai Enterprise page claims zero retention ("Code is encrypted in transit and never stored on our servers"), no training on your code, and SOC 2 Type 2. The China enterprise docs claim ISO/IEC 27001 and 27701 alignment through Volcano Engine and offer private deployment. These are vendor claims; this entry did not see the audit reports.

## Regional Availability (as of 2026-10-30)

- The international "Supported countries and regions" page lists most of Asia, Europe, the Americas, Oceania and Africa. It does **not** list mainland China, Hong Kong, Macao, Taiwan, Russia, Belarus, Iran, Cuba, Syria, Venezuela, Egypt or Canada.
- Paid international plans are sold in a shorter list of 59 countries and regions. That list does include Hong Kong, Macao and Egypt, which the availability page leaves out; the two pages disagree, so check both from your location.
- Mainland China users are served by the separate trae.cn edition, with its own account system, Chinese models and CNY prices. trae.cn itself returned HTTP 403 from outside China when this entry was written; the China facts here come from docs.trae.cn.

## When To Pick It

- You want a VS Code-compatible IDE that can import your VS Code or Cursor setup and keep your extensions, with agents, CUE completion and SOLO mode added.
- You want a cheap way in: $8 Lite in twelve countries, $20 Pro, and usage priced per token against published model prices, so a cheap model stretches the allowance.
- You want many models behind one subscription: OpenAI's current line, Gemini, Kimi, GLM, DeepSeek, MiniMax and Seed outside the US, plus Claude and Grok in the US, and your own keys on top.
- You want to dispatch work from your phone to your desktop or to a cloud environment, and see it on any of the three clients.
- You build small web apps end to end: SOLO's Figma, Supabase, Vercel and Stripe integrations cover the path from design to a deployed link.
- You are in mainland China and want an IDE with domestic models (Seed, GLM, DeepSeek, Kimi, Qwen, MiniMax, MiMo, Step) and CNY billing.

## When Not To Pick It

- Your code or chats must never be used for training and you cannot rely on every user turning on Privacy Mode while signed in. Use the enterprise edition, which states no training and zero retention, or a different tool.
- Your policy rules out sending code and prompts to a ByteDance group company, or storing them in Singapore and Malaysia with onward transfer.
- You need open source or self-hosting. The product is closed; `trae-agent` is a separate research project, not the IDE.
- You need a terminal agent. There is no TRAE CLI for individuals on either edition; look at [terminal coding CLI agents](../comparisons/coding-cli-agents.md).
- You want Claude outside the US. It is not on the non-US model list; you would need your own Anthropic key.
- You are in Canada, Russia, Taiwan or another region missing from the international list.
- You want to know in advance what the free tier covers. Its allowance is "limited" with no number, and SOLO mode is paid-only.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Editor workflow | Strong | VS Code-style IDE window with extensions, debugger, Git, CUE completion; imports VS Code or Cursor settings |
| Autonomous build mode | Strong | SOLO mode plans, waits for confirmation, then codes, tests, previews and deploys; paid plans only |
| Parallel and cloud tasks | Strong | Agent window across projects, SSH hosts, worktrees and cloud containers; 2 to 20 concurrent cloud tasks by plan |
| Scheduling | Strong | Automation runs tasks at a fixed time, on an interval, or from a natural-language schedule |
| Cross-device | Strong | Desktop, web and mobile share tasks; mobile can drive the desktop |
| Model choice | Strong, by region | Wide built-in list plus OpenAI- or Anthropic-format custom endpoints; Claude and Grok only in the US; China edition is domestic-only |
| Privacy defaults | Weak | Chat data may be used for training until Privacy Mode is on; corporate-group processing; enterprise terms are stricter |
| Terminal / CLI | Weak | Only on the China enterprise flagship plan |
| Open source | Weak | Closed product; `trae-agent` (MIT) is a separate research CLI |

## Relationship To Other Entries

- [Cursor](cursor.md) and [Windsurf](windsurf.md) are the closest shapes: VS Code-derived editors with agents. TRAE's differences are the separate Agent window, the mobile client, token-priced plans starting at $8, and the region-split model list.
- [Google Antigravity](antigravity.md) is the other editor-plus-agent-manager design on this route. Antigravity has a public CLI and a free tier with Gemini; TRAE has a wider multi-vendor model list and SOLO's app-building integrations, but no public CLI.
- [CodeBuddy](codebuddy.md) is Tencent's equivalent product line, also split into international and China editions. CodeBuddy offers its terminal CLI to individuals; TRAE does not.
- [Doubao](doubao.md) is ByteDance's consumer assistant; the Seed models in TRAE's lists are ByteDance's own.

## Operating Cost

Low to install, medium to run. The download is a standard installer and setup imports VS Code or Cursor settings. The ongoing cost is in three choices: which edition you can use from where you are, whether every team member turns on Privacy Mode (or whether you buy enterprise), and how much model choice and Max mode eat the dollar allowance. Releases come often (four point releases on 2026-10-15 alone), and a feature you read about may have been renamed: Builder became part of Agent, SOLO Coder became SOLO Agent, and TraeCode and TraeWork became TRAE.

## Bottom Line

TRAE is a capable editor-centric product with more surfaces than most on this route: IDE, AI-led SOLO mode, a multi-agent Agent window, web, mobile and scheduled tasks, on a broad and cheap token-priced model menu. Read the data terms before picking it. Chat content can be used for training until Privacy Mode is on, ByteDance group companies process the data, and the strict no-training, no-retention terms come with the enterprise edition. It is also two products: the international edition outside China and the US, a US variant with Claude and Grok, and a China edition with domestic models and CNY credits. If you need a terminal agent or open source, look elsewhere on this map.

## Sources

All read 2026-10-30.

- Site: [trae.ai](https://www.trae.ai/) · [Pricing](https://www.trae.ai/pricing) · [Download Center](https://www.trae.ai/download) · [Enterprise ("CLI (coming soon)", zero retention, SOC 2 Type 2)](https://www.trae.ai/enterprise) · [Privacy Policy (last updated 2026-05-20)](https://www.trae.ai/privacy-policy)
- International docs, get started: [About TRAE](https://docs.trae.ai/ide/what-is-trae) · [TraeCode and TraeWork merged into the all-new TRAE](https://docs.trae.ai/ide/traework-to-traecode-data-migration) · [Desktop, web and mobile](https://docs.trae.ai/ide/trae-across-desktop-web-and-mobile) · [Get started with TRAE Desktop (system requirements)](https://docs.trae.ai/ide/get-started-with-trae-desktop) · [Supported countries and regions](https://docs.trae.ai/ide/supported-countries-and-regions) · [Device limit](https://docs.trae.ai/ide/device-limit) · [Changelog (v3.6.4, 2026-10-15)](https://docs.trae.ai/ide/changelog)
- International docs, features: [SOLO mode](https://docs.trae.ai/ide/solo-mode) · [Agent overview](https://docs.trae.ai/ide/agent-overview) · [Auto-run & security](https://docs.trae.ai/ide/auto-run-and-security) · [Sandbox](https://docs.trae.ai/ide/sandbox) · [Automated tasks](https://docs.trae.ai/ide/automated-tasks) · [Cloud environment setup](https://docs.trae.ai/ide/set-up-your-cloud-environment) · [Memories](https://docs.trae.ai/ide/memories) · [Max mode](https://docs.trae.ai/ide/max-mode) · [TRAE Plugin](https://docs.trae.ai/plugin/what-is-trae-plugin)
- International docs, models and billing: [Built-in models & custom models](https://docs.trae.ai/ide/models) · [Auto mode](https://docs.trae.ai/ide/auto-mode) · [Plans & billing](https://docs.trae.ai/ide/new-plans-and-billing) · [On-Demand Usage](https://docs.trae.ai/ide/on-demand-usage) · [Plans & billing FAQs](https://docs.trae.ai/ide/plans-and-billing-faqs)
- International docs, data: [Privacy mode](https://docs.trae.ai/ide/privacy-mode) · [Data storage policy for cloud agents](https://docs.trae.ai/ide/data-storage-policy-for-remote-agents)
- China docs: [关于 TRAE](https://docs.trae.cn/ide_what-is-trae-code) · [套餐与计费说明](https://docs.trae.cn/ide_plans-and-billing) · [内置模型 & 自定义模型](https://docs.trae.cn/ide_models) · [内置模型限时折扣](https://docs.trae.cn/ide_limited-time-discount-for-builtin-models) · [隐私模式](https://docs.trae.cn/ide_privacy-mode) · [更新日志 (v3.4.4)](https://docs.trae.cn/ide_changelog) · [TRAE CLI 2.0 简介 (flagship-only)](https://docs.trae.cn/cli_about-trae-code-cli-2) · [TRAE CLI 2.0 快速开始](https://docs.trae.cn/cli_get-started-with-trae-cli-2) · [升级到 TRAE CLI 2.0](https://docs.trae.cn/cli_get-started-with-trae-cli) · [权限与沙箱](https://docs.trae.cn/cli_permission-and-sandbox) · [企业版概览](https://docs.trae.cn/enterprise_trae-enterprise-edition-overview) · [企业版安全合规](https://docs.trae.cn/enterprise_security-compliance-and-governance)
- GitHub: [bytedance/trae-agent](https://github.com/bytedance/trae-agent) (MIT) · [Trae-AI/TRAE](https://github.com/Trae-AI/TRAE)
