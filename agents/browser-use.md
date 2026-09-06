# Browser Use

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/browser-use.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](browser-use.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Browser Use gives an agent a real browser — it opens pages, clicks, types, and fills forms the way a person does — and at 113k stars under MIT it is the default answer for the one capability this map had no route for.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Browser Use (open-source project, with a hosted cloud) |
| Route | **Browser agent** — the first entry on a new route |
| Repository | [`browser-use/browser-use`](https://github.com/browser-use/browser-use) — MIT, Python, **113k stars** |
| Open source | Yes (MIT); a hosted Browser Use Cloud also exists |
| Best for | Tasks that live on websites rather than in repositories |
| Main cost | An agent driving a real browser is a real security surface — scope it deliberately |
| Requirements | Python 3.11+ |
| Docs | https://docs.browser-use.com |

## Why This Entry Exists

This map covered agents that edit code, run terminals, orchestrate other agents, and write documents. It had **no route** for the capability that most non-engineering automation actually needs: driving a website that has no API.

The gap became untenable once the map recorded [Kimi Work](kimi-work.md) shipping browser automation as a headline feature and [Claude in Chrome](../market-events.md) going generally available with per-action approval removed. Browser Use is the open, self-hostable member of that category, and it is the one the others get compared against.

## When To Pick It

- **The task is on a website and there is no API.** Filling applications, extracting structured data from pages, multi-step flows across forms — the project's own examples.
- You want it **inside an agent you already run**: it registers as a skill (`browser-use skill install`) and the README documents setup for Claude Code, Codex, Cursor, [Hermes Agent](hermes-agent.md), and [OpenClaw](openclaw.md) — three of which this map already profiles.
- You want **any LLM**, from your own code: the Python library is model-agnostic by design.
- You want the option of a hosted path later without changing tools — Browser Use Cloud exists alongside the library.
- You want MIT rather than a copyleft or source-available licence; among browser agents, Skyvern is AGPL-3.0 and that difference decides deployments.

## When Not To Pick It

- **You have not thought about what the browser is logged into.** This is the central risk of the category, not a footnote: an autonomous loop with your live sessions can act as you. Scope the profile, the credentials, and the approval gate before the first run.
- You want deterministic automation. If the flow is stable and scriptable, Playwright is cheaper, faster, and more predictable than a model deciding what to click.
- You want a coding agent — this is a capability to give one, not a replacement for one.
- You need a Node-native SDK rather than Python — Stagehand (MIT, TypeScript) is the neighbour to compare, and it is on this map's watchlist rather than profiled.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Web task completion | Very strong | The category-defining implementation: opens, clicks, types, fills, extracts |
| Harness integration | Very strong | Ships as a skill; documented for Claude Code, Codex, Cursor, Hermes, OpenClaw |
| Model freedom | Very strong | Works with any LLM from your own code |
| Deployment options | Strong | Self-hosted library or hosted cloud |
| Licence | Strong | MIT, against AGPL-3.0 for the nearest alternative |
| Security surface | **Handle with care** | A live browser session is the thing being automated |

## The Route This Opens

"Browser agent" is a separate route on this map rather than a feature bullet, because the selection question is genuinely different: you are not choosing how an agent edits files, you are choosing **what an agent is allowed to do as you, on the open web**. The neighbours worth knowing while this route fills out: **Stagehand** (`browserbase/stagehand`, MIT, TypeScript, 24k) as the SDK-shaped alternative, and **Skyvern** (`Skyvern-AI/skyvern`, AGPL-3.0, 23k) as the workflow-shaped one. Both are on the watchlist.

## Bottom Line

If an agent has to use the web the way a person does, this is where to start: biggest, MIT, model-agnostic, and already wired into harnesses this map covers. Spend the time you save on the approval design — the capability that makes it useful is the same one that makes it dangerous.
