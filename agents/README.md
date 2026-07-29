# Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/README.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](README.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This is not a wall of names.

Think of it as a shortlist directory: understand the route first, then decide which profile is worth opening.

## Browse By Route

| Route | Representative projects | Best for |
| --- | --- | --- |
| Direct execution | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md), [CodeWhale](codewhale.md), [Grok Build](grok-build.md), [Devin](devin.md), [Jules](jules.md) | People who want to hand a coding task directly to an agent (compared in [terminal coding CLI agents](../comparisons/coding-cli-agents.md)) |
| Agent harness framework | [Pi](pi.md), [jcode](jcode.md), [OpenHands](openhands.md), [SWE-agent](swe-agent.md), [mini-swe-agent](mini-swe-agent.md), [OpenHarness](openharness.md) | People who want to own the loop, tool surface, and permissions instead of inheriting a vendor product |
| Frontier agentic model | [Claude Fable 5](claude-fable-5.md), [GPT-5.5](gpt-5.5.md) | People choosing which model to wire into their agent system, or evaluating the capability ceiling of Anthropic / OpenAI surfaces |
| Agentic skills framework | [Superpowers](superpowers.md) | Users who want a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and other agents |
| Workflow / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md), [Ruflo](ruflo.md) | Users who already like Claude Code or Codex and want stronger teams, skills, and persistent workflow (Ruflo extends this to multi-machine federation) |
| Editor-centric AI workflow | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | Users who want the editor itself to be the main agent surface |
| Review-first automation | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md), [CoStrict](costrict.md) | People who want review and human pacing to stay central (CoStrict targets enterprise strict-workflow + private deployment) |
| General-purpose autonomous agent | [AutoGPT](autogpt.md), [Agent Zero](agent-zero.md), [BabyAGI](babyagi.md), [Julep](julep.md), [GenericAgent](generic-agent.md), [ml-intern](ml-intern.md) | People who want autonomous general-purpose task execution (ml-intern is the ML-specialized variant) |
| Build-your-own platform | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md), [Haystack](haystack.md), [Semantic Kernel](semantic-kernel.md), [DSPy](dspy.md), [Pydantic AI](pydantic-ai.md) | Teams building their own agent system |
| Runtime and tools | [n8n](n8n.md), [MemGPT](memgpt.md), [Open Interpreter](open-interpreter.md), [LiteLLM](litellm.md), [Flowise](flowise.md), [CodeGraph](codegraph.md), [CLI-Anything](cli-anything.md) | Teams needing workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Self-hosted / local runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md), [Mercury Agent](mercury-agent.md), [OpenHuman](openhuman.md) | Users who need local control, on-device privacy, extensions, channels, runtime ownership, or personal-data life integration |
| Managed background path | [Claude Managed Agents](claude-managed-agents.md) | Users who need scheduled, cloud, or detached execution |

## Recent Heat Snapshot

This is not a ranking of quality.

It is a quick view of projects that appeared especially hot in the latest weekly GitHub snapshot. The order follows the 7-day gain, while the star totals below reflect the current counts checked during this repo update.

> **Last updated:** 2026-07-29 · **Snapshot window:** 2026-07-22 → 2026-07-29 (gain since last update, 7 days, approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When a profile exists in this directory, it is linked separately in the "Directory status" column.

| Rank | Project | Current stars | Snapshot gain | Directory status | Note |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 192.9k | +11,033 | Watchlist (Skills Wave) | Sixth straight window at the gain lead — curated `.claude/skills` directory cleared 192k, though off last window's record |
| #2&nbsp;(↑) | [Pi](https://github.com/earendil-works/pi) | 79.7k | +4,286 | [Profile](pi.md) | Climbed to #2 and neared 80k — the steadiest gainer in the top five |
| #3&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 262.7k | +3,409 | [Profile](superpowers.md) | Slipped to #3 as its gain fell by a third, but crossed 262k |
| #4&nbsp;(=) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 221.9k | +3,057 | [Profile](hermes-agent.md) | Steady at #4 for a third straight window — cleared 221k |
| #5&nbsp;(↑) | [jcode](https://github.com/1jehuang/jcode) | 12.8k | +2,156 | [Profile](jcode.md) | Rose two spots in its first full window as a profile — the Rust multi-session harness cleared 12.7k |
| #6&nbsp;(↓) | [Codex CLI](https://github.com/openai/codex) | 102.1k | +1,498 | [Profile](codex.md) | Eased to #6 as its gain halved post-100k — cleared 102k |
| #7&nbsp;(↑) | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 63.1k | +1,464 | [Profile](codegraph.md) | Up one to #7 — pre-indexed code knowledge graph cleared 63k |
| #8&nbsp;(↓) | [anthropics/skills](https://github.com/anthropics/skills) | 164.8k | +1,439 | Watchlist (Skills Wave canonical) | Slipped two spots as its gain nearly halved — cleared 164k |
| #9&nbsp;(↑) | [Kimi Code](https://github.com/MoonshotAI/kimi-code) | 5.5k | +997 | [Profile](kimi-code.md) | Up one to #9 — Moonshot's vendor-official Kimi-native CLI cleared 5.5k |
| #10&nbsp;(new) | [n8n](https://github.com/n8n-io/n8n) | 198.4k | +973 | [Profile](n8n.md) | First appearance on this table — the workflow-automation runtime took the last seat by 8 stars |

Rank history over time is charted in [rankings/](../rankings/README.md), alongside category and vertical boards sorted by total stars.

**Market events:**
- **July 22–29 2026 — Grok Build lands; the board cools broadly** — xAI/SpaceXAI shipped **[Grok Build](grok-build.md)**, a vendor-official Rust terminal coding agent, reaching **23.2k stars and 4.4k forks in 15 days** — the loudest debut this map has recorded. New-inclusion decision: **Grok Build is added as an in-scope profile** on the coding-CLI route; note its governance — Apache-2.0 but a periodic monorepo export that **does not accept external contributions**. It carries no rank yet because it was untracked when the window opened. On the table, every top-10 gain fell (partly a 7-day window against ~8 last time): [mattpocock/skills](https://github.com/mattpocock/skills) took a sixth straight #1 off its record (+11.0k), [Superpowers](superpowers.md) slipped to #3, [Codex CLI](codex.md) halved to #6, while [Pi](pi.md) rose to #2 and [jcode](jcode.md) to #5. [n8n](n8n.md) entered at #10 by 8 stars over [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), which fell off. Skills wave narrowed a third straight time, to 3/10.
- **July 14–22 2026 — jcode promoted to a profile; mattpocock surges, addyosmani collapses** — [mattpocock/skills](https://github.com/mattpocock/skills) took a fifth straight #1 with its biggest gain yet (+13.6k, past 181k), while last window's #2 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) fell to #9 as its gain roughly halved. Two in-scope newcomers entered the gain table: **[jcode](jcode.md)** at #7 and [Kimi Code](kimi-code.md) at #10. New-inclusion decision: **[jcode](jcode.md) (`1jehuang/jcode`, Rust, 10.6k) graduated from the watchlist to a full profile** in the [agent harness framework](../comparisons/agent-harness-frameworks.md) route, after climbing steadily since May. [Codex CLI](codex.md) crossed 100k. Skills wave narrowed to 4/10 as [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) and [TradingAgents](https://github.com/TauricResearch/TradingAgents) fell off the table.
- **July 9 2026 — Codex merges into ChatGPT; GPT-5.6 ships** — OpenAI folded the standalone Codex app into the ChatGPT desktop app (Codex is now an entry next to Chat and the new agentic ChatGPT Work mode, on every plan including Free), and GPT-5.6 (Sol/Terra/Luna tiers) replaced GPT-5.5 across ChatGPT, Codex, and the API. Details in [market-events](../market-events.md), [Codex](codex.md), [GPT-5.5](gpt-5.5.md).
- **June 9 – July 7 2026 — Claude 5 family arrives, with turbulence** — Anthropic released [Claude Fable 5](claude-fable-5.md), the first Mythos-class model (a tier above Opus), as the default Claude Code model; it was pulled worldwide June 12 under short-lived export controls, returned July 1 behind stricter safety classifiers (Opus 4.8 fallback), and moved to metered credits July 7. Opus 4.8 itself had shipped May 28. Details in [market-events](../market-events.md).
- **July 8–14 2026 — curated-skills rotation, still no breakout** — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) climbed one spot to #2 (+5.1k, past 77k), overtaking [Superpowers](superpowers.md), which slipped to #3 (past 253k). [mattpocock/skills](https://github.com/mattpocock/skills) held the #1 gain spot for a fourth straight window (+7.7k, past 168k). The only real reshuffle below was [Pi](pi.md) jumping two spots to #5 and [Codex CLI](codex.md) two spots to #7, pushing [anthropics/skills](https://github.com/anthropics/skills) and [codegraph](codegraph.md) down; [TradingAgents](https://github.com/TauricResearch/TradingAgents) slipped to #9. Skills wave still 5/10. New-inclusion scan found no new in-scope surface; the freshest and largest new repos — [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) (7.3k, patterns and CLI tooling for "loop engineering") and [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge) (2.8k, an AI-native markdown wiki editor) — join the watchlist.
- **July 2–8 2026 — curated-skills rotation, still no breakout** — [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) was the biggest riser (+4.3k), climbing three spots from #6 to #3 and re-heating the curated end. [mattpocock/skills](https://github.com/mattpocock/skills) held the #1 gain spot for a third straight window (+6.6k, past 160k), while [Hermes Agent](hermes-agent.md) and [anthropics/skills](https://github.com/anthropics/skills) each cooled a step. Skills wave still 5/10; [TradingAgents](https://github.com/TauricResearch/TradingAgents) slipped to #8. New-inclusion scan found no new in-scope surface; the freshest and largest new repos — [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) (9.6k, a CLI that writes and maintains agent-generated docs) and [vercel/eve](https://github.com/vercel/eve) (3.3k, Vercel's agent-building framework) — join the watchlist.
- **June 24 – July 2 2026 — top of the table freezes** — No breakout this window: [mattpocock/skills](https://github.com/mattpocock/skills) held the #1 gain spot for a second straight window (+9.3k, past 153k), with [Superpowers](superpowers.md) and [Hermes Agent](hermes-agent.md) steady at #2/#3. Within the skills wave (still 5/10), [anthropics/skills](https://github.com/anthropics/skills) climbed to #4 while [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) cooled to #6; [TradingAgents](https://github.com/TauricResearch/TradingAgents) re-entered higher at #7. New-inclusion scan found no new in-scope surface; the freshest candidates — [tigicion/dao-code](https://github.com/tigicion/dao-code) (1.2k, a DeepSeek-V4 terminal coding CLI) and [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) (2.2k, Claude Design as an Agent Skill) — join the watchlist.
- **June 17–24 2026 — Skills Wave lead rotates, MiMoCode cools** — [mattpocock/skills](https://github.com/mattpocock/skills) posted the window's biggest gain (+11.1k, past 144k) to retake the #1 gain spot, while last week's breakout [MiMoCode](mimocode.md) added only ~1.0k (9.6k → 10.6k) and dropped off the gain top 10. [Codex CLI](codex.md) re-entered the table at #9 and [Hermes Agent](hermes-agent.md) broke 200k. New-inclusion scan found no new in-scope surface; the biggest fresh repos ([op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) 4.0k, [ruvnet/agent-harness-generator](https://github.com/ruvnet/agent-harness-generator) 0.3k) stay on the watchlist.
- **Late May 2026 — rebrand** — The agent profiled here as DeepSeek-TUI renamed to [CodeWhale](codewhale.md) (`Hmbown/CodeWhale`, now 36.6k) and broadened from DeepSeek-only to **DeepSeek + MiMo**. Old `DeepSeek-TUI` links redirect; this directory now uses the new name.
- **Late May 2026 — code-context breakout** — [codegraph](codegraph.md) more than doubled in one window (16.4k → 37.5k), the clearest sign yet that "agent context infrastructure" is its own demand center. New harness-framework newcomer [jcode](https://github.com/1jehuang/jcode) (1jehuang, Rust, 6.8k) joins the watchlist alongside [SWE-agent](swe-agent.md) / [mini-swe-agent](mini-swe-agent.md) and [OpenHarness](openharness.md).
- **May 2026 (cooling)** — The `.claude/skills` wave continues but narrowed from six of the top ten to four ([mattpocock/skills](https://github.com/mattpocock/skills), [Superpowers](superpowers.md), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills), [anthropics/skills](https://github.com/anthropics/skills)) as code-context and harness infrastructure absorbed more of the trending oxygen. Anthropic's own [skills](https://github.com/anthropics/skills) repo remains the canonical anchor.
- **April 8 2026** — Earendil (Armin Ronacher's company) acquired the [Pi](pi.md) project from Mario Zechner; the repo moved from `badlogic/pi-mono` to `earendil-works/pi`, and Earendil also began building Lefos, a cloud agent platform on top of it.
- **April 16 2026** — OpenAI shipped "Codex for (almost) everything," adding Background Computer Use, parallel multi-agent execution, an in-app browser, and 90+ plugins on the [Codex](codex.md) product surface. Reported 3M weekly active developers, ~2x early-March 2026.
- **April 23 2026** — OpenAI released [GPT-5.5](gpt-5.5.md), the model layer powering Codex, ChatGPT, and every OpenAI-API-based agent.

## Current Coverage

| Project | Category | Open source | One-line fit | Status |
| --- | --- | --- | --- | --- |
| [Aider](aider.md) | execution | Yes | Terminal-first AI pair programming with a strong git loop | Verified |
| [Claude Code](claude-code.md) | execution | No | Local and IDE-first coding agent | Verified |
| [Claude Managed Agents](claude-managed-agents.md) | automation | No | Anthropic managed / cloud execution mapping | Mapping documented |
| [Codex](codex.md) | execution | No | Cloud software engineering agent inside ChatGPT | Verified against current product boundary |
| [oh-my-claudecode](oh-my-claudecode.md) | multi-agent | Yes | Workflow and orchestration layer for Claude Code | Verified with package naming note |
| [oh-my-codex](oh-my-codex.md) | multi-agent | Yes | Workflow and orchestration layer for Codex CLI | Verified |
| [Cursor](cursor.md) | platform | No | AI editor spanning local coding, integrations, and background agents | Verified |
| [GitHub Copilot](github-copilot.md) | platform | No | Multi-surface agent platform across VS Code and GitHub | Verified |
| [Cline](cline.md) | execution | Yes | Approval-first editor-native coding agent | Verified |
| [Windsurf](windsurf.md) | platform | No | AI-native IDE centered on Cascade | Verified |
| [OpenHands](openhands.md) | execution | Yes | Open-source software engineering agent | Verified |
| [Devin](devin.md) | execution | No | Managed end-to-end software engineering execution | Verified |
| [Jules](jules.md) | automation | No | Google managed cloud coding agent with GitHub and PR flow | Verified against current docs |
| [AI Edge Gallery](ai-edge-gallery.md) | platform | Yes | On-device local assistant sandbox with agent skills and mobile actions | Verified with scope caveat |
| [Goose](goose.md) | platform | Yes | Extensible local agent across desktop, CLI, and API | Verified |
| [Hermes Agent](hermes-agent.md) | multi-agent | Yes | Self-hosted environment with memory, skills, and subagents | Verified |
| [OpenClaw](openclaw.md) | platform | Yes | Local-first runtime across channels and devices | Verified |
| [LangChain](langchain.md) | platform | Yes | High-level framework for custom agents | Verified |
| [LangGraph](langgraph.md) | platform | Yes | Low-level framework for durable workflows | Verified |
| [Continue](continue.md) | platform | Yes | Open-source IDE extension with full model freedom | Verified |
| [Claude Fable 5](claude-fable-5.md) | model / agentic | No | Anthropic's Mythos-class frontier model — the capability ceiling above Opus for Claude-based agents | Verified against launch + redeployment announcements |
| [GPT-5.5](gpt-5.5.md) | model / agentic | No | Frontier agentic model powering Codex, ChatGPT, and API surfaces (succeeded by GPT-5.6, July 2026) | Verified against launch materials |
| [AutoGPT](autogpt.md) | autonomous | Yes | Visual agent-builder platform with workflows and marketplace | Verified |
| [CrewAI](crewai.md) | multi-agent | Yes | Role-based multi-agent orchestration framework | Verified |
| [LlamaIndex](llamaindex.md) | platform | Yes | Data-first RAG and agent framework | Verified |
| [n8n](n8n.md) | runtime / tools | Fair-code | Visual workflow automation with native AI agent nodes | Verified |
| [MemGPT](memgpt.md) | runtime / tools | Yes | Stateful agents with persistent memory (now Letta) | Verified |
| [Agent Zero](agent-zero.md) | autonomous | Yes | Self-building autonomous agent with dynamic tool creation | Verified |
| [BabyAGI](babyagi.md) | experimental | Yes | Pioneering autonomous agent experiment — educational | Verified |
| [Julep](julep.md) | workflow engine | Yes | Temporal-backed durable workflow engine for stateful agents | Verified |
| [Haystack](haystack.md) | platform | Yes | Production-oriented RAG and agent framework by deepset | Verified |
| [Semantic Kernel](semantic-kernel.md) | platform | Yes | Microsoft AI orchestration SDK for .NET, Python, Java | Verified |
| [DSPy](dspy.md) | platform | Yes | Programmatic prompt optimization framework | Verified |
| [Open Interpreter](open-interpreter.md) | runtime / tools | Yes | Natural language to local code execution | Verified |
| [LiteLLM](litellm.md) | infrastructure | Yes | Unified API gateway for 100+ LLM providers | Verified |
| [Pydantic AI](pydantic-ai.md) | platform | Yes | Type-safe Python agent framework with structured outputs | Verified |
| [Flowise](flowise.md) | runtime / tools | Yes | Visual drag-and-drop LLM app and agent builder | Verified |
| [Froge Code](froge-code.md) | automation | Yes | Currently mapped to Automagik Genie | Public naming is still evolving |
| [Mercury Agent](mercury-agent.md) | multi-channel runtime | Yes | Permission-hardened self-hosted agent for CLI and Telegram with token budgets | Verified against current repo |
| [Pi](pi.md) | execution / toolkit | Yes | Minimal terminal coding-agent harness with multi-provider LLM support | Verified after April 2026 acquisition by Earendil |
| [ml-intern](ml-intern.md) | autonomous (domain-specific) | Yes | Autonomous ML engineering agent built on the Hugging Face ecosystem | Verified |
| [GenericAgent](generic-agent.md) | autonomous (self-evolving) | Yes | Small-seed agent that grows a personal skill tree on every task | Verified after week-2 of watchlist tracking |
| [Superpowers](superpowers.md) | skills framework / methodology | Yes | Composable agentic skills framework with Claude Code, Codex, Cursor, Copilot, Gemini plugins | Verified at v5.1 (May 2026) |
| [CodeWhale](codewhale.md) | execution (DeepSeek + MiMo) | Yes | DeepSeek + MiMo terminal coding agent (formerly DeepSeek-TUI) | Verified during May 2026 surge |
| [Ruflo](ruflo.md) | multi-agent orchestration | Yes | Multi-machine federated Claude orchestration platform (formerly Claude Flow) | Verified after rebrand |
| [OpenHuman](openhuman.md) | self-hosted / local runtime | Yes | Open-source desktop life-integration agent with 118+ connectors, local Memory Tree, Ollama support | Verified after two-week trending run |
| [CodeGraph](codegraph.md) | runtime / agent context | Yes | Pre-indexed code knowledge graph + MCP server for Claude Code, Cursor, Codex CLI, opencode, Hermes Agent | Verified during May 2026 trending surge |
| [CLI-Anything](cli-anything.md) | runtime / agent-native bridge | Yes | Auto-generates Click-based CLIs for arbitrary software so agents can drive non-API apps | Verified at v1 (May 2026) with HKUDS ownership |
| [SWE-agent](swe-agent.md) | harness framework / research | Yes | Princeton + Stanford's original SWE-bench harness with single-YAML configuration | Verified against current upstream; team now emphasizes mini-swe-agent |
| [mini-swe-agent](mini-swe-agent.md) | harness framework / minimal | Yes | ~100-line Python successor to SWE-agent; SWE-bench Verified >74% | Verified against upstream README |
| [OpenHarness](openharness.md) | harness framework / production | Yes | HKUDS's 10-subsystem open harness with 43+ tools, anthropics/skills, MCP | Verified at v0.1.9 (May 2026) |
| [jcode](jcode.md) | harness framework / coding | Yes | Rust multi-session coding harness — fastest boot, provider-neutral OAuth, passive semantic memory | Verified July 2026 (10.6k, promoted from watchlist) |

## Writing Standard

See [evaluation framework](evaluation-framework.md).

## Naming Notes

If a project name or public boundary is ambiguous, this directory keeps the ambiguity visible instead of pretending verification is complete.