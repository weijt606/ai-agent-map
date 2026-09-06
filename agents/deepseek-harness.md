# DeepSeek Harness

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/deepseek-harness.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](deepseek-harness.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: DeepSeek Harness (`dsh`) is an agent harness with **no privileged core** — the model adapter, the tool registry, the session log, and the agent loop itself are all plugins you can replace from configuration — and it reached 213k stars in three weeks while still labelled a developer preview.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | DeepSeek AI |
| Route | Agent harness framework |
| Repository | [`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) — MIT, TypeScript |
| Open source | Yes (MIT) |
| Best for | Teams that want to own the loop and swap parts of it without forking |
| Main cost | **Developer preview** — the README warns of compatibility-breaking changes |
| Start command | `npx @deepseek-ai/dsh web` (Web UI on `127.0.0.1:3080`) |
| Docs | https://deepseek-harness.github.io/deepseek-harness/ |

## Why This Entry Exists

This map's [harness route](../comparisons/agent-harness-frameworks.md) already had three shapes: a loop you fork and own ([Pi](pi.md), [jcode](jcode.md)), a meta-harness that drives other loops ([QM](qm.md), [Omnigent](omnigent.md)), and a harness you deploy and call over HTTP ([TrueForge](trueforge.md)). `dsh` is a fourth: **a harness with no core to fork.**

The architecture is built on [Cordis](https://github.com/cordiverse/cordis), a plugin kernel where plugins contribute services, typed events, and reversible effects to a shared context. The project's own architecture doc states it plainly: *"Every part of the product is a plugin, including the model adapter, the tool registry, the session log, and the agent loop itself, so each is replaceable from configuration. There is no privileged core to patch."*

## When To Pick It

- You want to replace **one part** of an agent — the loop, the sandbox policy, the tool registry — without maintaining a fork of the whole thing. Registrations are effects that unwind when their plugin unloads, so removal is as clean as addition.
- You need several delivery shapes from one codebase. Shipped profiles are `web` (browser app), `headless` (one-shot runner, no server), `sdk` (JSON-RPC server, TypeScript and Python clients), `sdk-minimal`, and `acp` (automation-only [Agent Client Protocol](https://agentclientprotocol.com) server).
- You want to read the composition before trusting it: `dsh --profile web --dump-config` prints the actual plugin tree your machine boots, and any row it prints can be replaced by a patch of your own.
- You want a permissive licence on a vendor-official harness — MIT, with third-party licences disclosed separately.

## When Not To Pick It

- **You need API stability.** The README's own words: *"DeepSeek Harness is in developer preview and iterating rapidly. THERE WILL BE COMPATIBILITY-BREAKING CHANGES."* Plugin contracts are explicitly not frozen.
- You want to start today and not think about architecture. The layered profile/bundle/patch model is genuinely more to learn than a single-file loop, and its own docs recommend using an agent to explore the codebase.
- You want a managed product with a support contract — this is a repository, not a service.
- You want the vendor's own model to be the only path. It is not, but the surrounding ecosystem (docs, plugin topic, Discord) is DeepSeek-run.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Extensibility | Very strong | The differentiating property: everything, including the agent loop, is a replaceable plugin |
| Delivery surfaces | Very strong | Web UI, headless one-shot, JSON-RPC SDK (TS + Python), ACP server |
| Approval and sandboxing | Strong | Sandbox and approval policy ship in the shared `dsh-base` layer, not bolted on per-profile |
| Session durability | Strong | Append-only `SessionEvent` log with a live store; session events are the facts that survive a reload |
| Observability | Strong | Telemetry is a base-layer seam; capability events (`fs/*`, `tools/*`, `telemetry/*`) attach policy without importing the loop |
| Stability | **Weak** | Developer preview by the project's own label |
| Governance | Medium | MIT and open to contributions, but vendor-run and moving fast |

## How Composition Works

Three nouns do the work, and they are worth learning before you evaluate anything else:

- A **bundle** is a distribution format for config rows plus the code they mount. `dsh-base` is the shared first layer — model adapters, tools, persistence, sandbox and approval policy, settings, credentials, telemetry.
- A **profile** is a named composition that stacks bundles, holds out-of-tree plugins, and keeps your own `cordis.patch.yml`.
- **Patches** apply in a defined order — each bundle, then the profile's patch, then the home-level one, then any `--patch` overlay — and target a row by id to replace its config or insert new rows.

Custom profiles default to live patch reload; `headless`, `sdk`, `sdk-minimal`, and `acp` apply layers once at startup, because swapping a one-shot or stdio application's dependencies mid-lifecycle would invalidate it.

## Relationship To The Rest Of This Map

Against [Pi](pi.md) and [jcode](jcode.md), the difference is ownership model: those are loops you fork and own; `dsh` is a tree you compose and patch. Against [QM](qm.md) and [Omnigent](omnigent.md), `dsh` is not a meta-harness — it does not drive Claude Code or Codex, it is the thing being driven. Against [TrueForge](trueforge.md), both expose an SDK and a server, but TrueForge's unit is a deployed service you call over HTTP, while `dsh`'s is a plugin tree you recompose locally.

## Bottom Line

The plugin-kernel idea is not new; applying it to the *agent loop itself*, in a vendor-official MIT repository, is. The adoption curve (213k stars, 25k forks in three weeks) says the pitch landed. Weigh that against the label the project puts on itself: developer preview, contracts not frozen. Good fit if you are building something you expect to keep changing; bad fit if you need to pin an interface and walk away.
