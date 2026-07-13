# Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/README.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](README.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This is not a wall of names.

Think of it as a shortlist directory: understand the route first, then decide which profile is worth opening.

## Browse By Route

| Route | Representative projects | Best for |
| --- | --- | --- |
| Direct execution | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md), [CodeWhale](codewhale.md), [Devin](devin.md), [Jules](jules.md) | People who want to hand a coding task directly to an agent (compared in [terminal coding CLI agents](../comparisons/coding-cli-agents.md)) |
| Agent harness framework | [Pi](pi.md), [OpenHands](openhands.md), [SWE-agent](swe-agent.md), [mini-swe-agent](mini-swe-agent.md), [OpenHarness](openharness.md) | People who want to own the loop, tool surface, and permissions instead of inheriting a vendor product |
| Frontier agentic model | [GPT-5.5](gpt-5.5.md) | People choosing which model to wire into their agent system, or evaluating the capability ceiling of OpenAI surfaces |
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

> **Last updated:** 2026-07-14 · **Snapshot window:** 2026-07-08 → 2026-07-14 (gain since last update, ~6 days, approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When a profile exists in this directory, it is linked separately in the "Directory status" column.

| Rank | Project | Current stars | Snapshot gain | Directory status | Note |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 168.3k | +7,712 | Watchlist (Skills Wave) | Held the gain lead for a fourth straight window — curated `.claude/skills` directory cleared 168k |
| #2&nbsp;(↑) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 77.9k | +5,052 | Watchlist (Skills Wave) | Climbed one spot to #2 — Addy Osmani's curated agent-skills collection cleared 77k |
| #3&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 253.8k | +4,445 | [Profile](superpowers.md) | Slipped one spot but crossed 253k — the agentic skills framework keeps compounding |
| #4&nbsp;(=) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 214.2k | +2,915 | [Profile](hermes-agent.md) | Steady at #4 — the in-scope absolute leader cleared 214k |
| #5&nbsp;(↑) | [Pi](https://github.com/earendil-works/pi) | 70.5k | +1,907 | [Profile](pi.md) | Jumped two spots from #7 — the Earendil-owned harness cleared 70k |
| #6&nbsp;(↓) | [anthropics/skills](https://github.com/anthropics/skills) | 160.9k | +1,490 | Watchlist (Skills Wave canonical) | Slipped one spot — Anthropic's own reference `.claude/skills` repo, cleared 160k |
| #7&nbsp;(↑) | [Codex CLI](https://github.com/openai/codex) | 97.7k | +1,459 | [Profile](codex.md) | Climbed two spots from #9 — OpenAI's Codex CLI neared 98k |
| #8&nbsp;(↓) | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 59.7k | +1,147 | [Profile](codegraph.md) | Cooled two spots to #8 — pre-indexed code knowledge graph neared 60k |
| #9&nbsp;(↓) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 92.8k | +1,038 | Not included | Vertical finance-research multi-agent system slipped one spot past 92k — out of scope as a domain vertical |
| #10&nbsp;(=) | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 37.7k | +821 | Watchlist (Skills Wave) | Held #10 — academic research pipeline for Claude Code cleared 37k |

**Market events:**
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
| [GPT-5.5](gpt-5.5.md) | model / agentic | No | Frontier agentic model powering Codex, ChatGPT, and API surfaces | Verified against launch materials |
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

## Writing Standard

See [evaluation framework](evaluation-framework.md).

## Naming Notes

If a project name or public boundary is ambiguous, this directory keeps the ambiguity visible instead of pretending verification is complete.