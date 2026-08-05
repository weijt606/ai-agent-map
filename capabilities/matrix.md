# Capability Matrix

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/capabilities/matrix.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](matrix.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

The heat ranking answers "what is popular." This page answers the harder question the map exists for: **for a given capability, who actually treats it as a core strength.**

Every column is one of the [priority dimensions](README.md). Every cell is scored on whether that capability is a *headline strength*, present but secondary, or simply not the point — because "both support it" hides most of the real difference.

## How To Read A Cell

| Mark | Meaning |
| --- | --- |
| ● | **Core strength** — a headline reason to pick it |
| ◐ | **Solid support** — real, but not the main event |
| ○ | **Limited / incidental** — possible, but you feel the seams |
| — | **Not a goal** — out of scope for this tool |

Columns, abbreviated from the [dimension vocabulary](README.md): **Tool** = tool use · **Exec** = code execution · **Mem** = memory · **Orch** = orchestration · **Multi** = multi-agent · **Appr** = human approval · **Sched** = scheduling · **Surf** = delivery surfaces · **Deploy** = deployment control.

> Scores are coarse by design — a selection aid, not a benchmark. They reflect each project's *stated* center of gravity as captured in its profile, not a lab measurement. For hard numbers on cost and coding capability, see [cost & benchmarks](../comparisons/cost-and-benchmarks.md).

## Evidence Behind A Cell

A bare mark can't be verified or disputed — six months on, nobody remembers which edition it applied to, where it was checked, or when. So a cell can carry an **[evidence record](evidence-records.md)**: the mark stays, but it travels with `scope`, `source`, `version`, `review_date`, and — the field that settles disagreements — `evidence_type` (`documentation` = advertised vs `source`/`demo`/`benchmark` = observed). Memory cells decompose further into a lifecycle sub-schema, because two ● memory cells can behave nothing alike.

This is rolling out in phases; [jcode](../agents/jcode.md)'s memory cell is worked end-to-end as the template — its `Mem` mark below links to its record. See **[evidence records](evidence-records.md)** for the schema, the memory sub-schema, and the phase plan. Schema credit: [u/teugent](https://www.reddit.com/r/AI_Agents/comments/1v56023/).

## Terminal Coding CLIs

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Claude Code](../agents/claude-code.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ● | ◐ |
| [Codex](../agents/codex.md) | ● | ● | ○ | ◐ | ● | ◐ | ◐ | ● | ○ |
| [Aider](../agents/aider.md) | ◐ | ● | ○ | ○ | — | ● | — | ○ | ◐ |
| [Kimi Code](../agents/kimi-code.md) | ● | ● | ○ | ○ | — | ◐ | — | ◐ | ◐ |
| [MiMoCode](../agents/mimocode.md) | ● | ● | ● | ○ | — | ◐ | — | ○ | ◐ |
| [CodeWhale](../agents/codewhale.md) | ● | ● | ○ | ○ | — | ◐ | — | ○ | ◐ |
| [Grok Build](../agents/grok-build.md) | ● | ● | ○ | ◐ | — | ◐ | ○ | ◐ | ◐ |

Standouts: Claude Code and Codex are the broadest **delivery surfaces**; Codex is alone here on **multi-agent** (parallel cloud agents); MiMoCode is the only CLI treating **memory** as a headline feature; Aider leads on explicit-diff **human approval**. Grok Build is the newest entry and the strongest **tool use** + **code execution** pairing among the vendor CLIs (MCP, skills, plugins, hooks, sandboxing, workspace checkpoints), but note its **deployment control** score reflects a source-available tree that does not accept contributions.

## Own-The-Loop Harness Frameworks

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Pi](../agents/pi.md) | ● | ● | ◐ | ◐ | ○ | ◐ | ○ | ○ | ● |
| [jcode](../agents/jcode.md) | ● | ● | [●](evidence-records.md#worked-example-jcode-memory-cell) | ◐ | ◐ | ◐ | ○ | ○ | ● |
| [OpenHands](../agents/openhands.md) | ● | ● | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ● |
| [SWE-agent](../agents/swe-agent.md) | ● | ● | ○ | ○ | — | ○ | — | ○ | ● |
| [mini-swe-agent](../agents/mini-swe-agent.md) | ◐ | ● | — | ○ | — | ○ | — | ○ | ● |
| [OpenHarness](../agents/openharness.md) | ● | ● | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ● |
| [QM](../agents/qm.md) | ◐ | ● | ● | ● | ◐ | ● | ● | ● | ● |
| [Omnigent](../agents/omnigent.md) | ● | ● | ○ | ● | ● | ● | ○ | ● | ● |

Standouts: the whole route is defined by **deployment control** (you own the loop). jcode is the only harness with **memory** as a headline (passive semantic graph — see [memory approaches](../comparisons/memory-approaches.md)); OpenHands and OpenHarness carry the most **orchestration**.

The two meta-harnesses score wide because they add the layer the single-loop harnesses deliberately leave out — and they split cleanly. [QM](../agents/qm.md) is the only entry on this route with **memory**, **scheduling**, and **delivery surfaces** all as core, because each scope owns its own memory, crons, and Slack/web presence; its **tool use** is deliberately ◐ (a small fixed tool surface, extended through skills rather than breadth). [Omnigent](../agents/omnigent.md) instead leads on **multi-agent** — mixing several harnesses in one session, including having one review another — and both make **human approval** core through policy engines rather than per-edit prompts. Read both marks with their maturity in mind: QM is days old and Omnigent is self-declared alpha, so these reflect stated design centers, not field-proven behavior.

## Editor-Centric & Review-First

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Cursor](../agents/cursor.md) | ● | ◐ | ○ | ◐ | ◐ | ◐ | ◐ | ● | ○ |
| [Windsurf](../agents/windsurf.md) | ● | ◐ | ○ | ◐ | ○ | ◐ | ○ | ◐ | ○ |
| [Continue](../agents/continue.md) | ◐ | ○ | ○ | ○ | — | ◐ | — | ◐ | ◐ |
| [Cline](../agents/cline.md) | ● | ● | ○ | ○ | — | ● | — | ◐ | ◐ |
| [GitHub Copilot](../agents/github-copilot.md) | ● | ◐ | ○ | ◐ | ◐ | ◐ | ◐ | ● | ○ |
| [CoStrict](../agents/costrict.md) | ● | ● | ○ | ● | ◐ | ● | ○ | ◐ | ● |
| [Open Code Review](../agents/open-code-review.md) | ● | — | — | ● | ◐ | ◐ | ○ | ● | ● |

Standouts: Cline and CoStrict make **human approval** the whole point; CoStrict is the only one here strong on **deployment control** (private, on-prem) and **orchestration** (a standardized requirement→review workflow).

[Open Code Review](../agents/open-code-review.md) is the odd shape in this group and worth reading carefully: it scores **—** on code execution and memory because it never runs your code and keeps no state beyond a resumable session, and only **◐** on human approval — not because humans are sidelined, but because it has no approval gate to offer: it comments and stops. Its **orchestration** ● is unusual for a review tool and is the actual product — deterministic file selection, bundling into concurrent sub-agents, and rule matching wrapped around the model. Its **delivery surfaces** ● covers a CLI, four CI systems, and plugins for Claude Code, Codex, Cursor, and OpenCode.

## Managed & Cloud Delegation

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Devin](../agents/devin.md) | ● | ● | ◐ | ● | ◐ | ◐ | ● | ◐ | — |
| [Jules](../agents/jules.md) | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | — |
| [Claude Managed Agents](../agents/claude-managed-agents.md) | ● | ● | ◐ | ● | ◐ | ◐ | ● | ◐ | — |

Standouts: the trade of this route is on the last column — you give up **deployment control** in exchange for **scheduling** and background execution that the foreground CLIs do not offer.

## Orchestration Layers On Top

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [oh-my-claudecode](../agents/oh-my-claudecode.md) | ◐ | ◐ | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ◐ |
| [oh-my-codex](../agents/oh-my-codex.md) | ◐ | ◐ | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ◐ |
| [Ruflo](../agents/ruflo.md) | ◐ | ◐ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ |

Standouts: **orchestration** is the reason these exist — they add teams, skills, and durable workflow to a base agent. Ruflo pushes furthest on **multi-agent** (multi-machine federation, 100+ specialized agents).

## Build-Your-Own Frameworks

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [LangChain](../agents/langchain.md) | ● | ◐ | ◐ | ● | ◐ | ○ | ○ | — | ● |
| [LangGraph](../agents/langgraph.md) | ● | ◐ | ● | ● | ● | ◐ | ◐ | — | ● |
| [CrewAI](../agents/crewai.md) | ● | ◐ | ◐ | ● | ● | ○ | ○ | — | ● |
| [LlamaIndex](../agents/llamaindex.md) | ◐ | ○ | ◐ | ◐ | ◐ | ○ | ○ | — | ● |

Standouts: no **delivery surface** — they are libraries you build on. LangGraph is the strongest on durable **memory** and **multi-agent** state; LlamaIndex's memory is data/retrieval, not conversation.

## Runtime, Gateways & Context Infrastructure

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [n8n](../agents/n8n.md) | ● | ◐ | ○ | ● | ◐ | ◐ | ● | ◐ | ● |
| [Letta (MemGPT)](../agents/memgpt.md) | ◐ | ○ | ● | ◐ | ◐ | ○ | ○ | — | ● |
| [Open Interpreter](../agents/open-interpreter.md) | ● | ● | ○ | ○ | — | ◐ | ○ | ◐ | ● |
| [Flowise](../agents/flowise.md) | ● | ◐ | ◐ | ● | ◐ | ○ | ◐ | ◐ | ● |
| [LiteLLM](../agents/litellm.md) | — | — | — | ○ | — | — | — | — | ● |
| [Langfuse](../agents/langfuse.md) | — | ○ | ○ | — | — | ◐ | ○ | ◐ | ● |
| [CodeGraph](../agents/codegraph.md) | ◐ | — | ● | — | — | — | — | ◐ | ● |
| [CLI-Anything](../agents/cli-anything.md) | ● | ◐ | — | — | — | — | — | ◐ | ● |

Standouts: this group is glue, so the shape is lopsided. n8n leads on **scheduling** (event/cron triggers); Letta is the reference for self-editing **memory**; CodeGraph's "memory" is a code knowledge graph (context, not conversation); LiteLLM is a pure gateway — its only real column is **deployment control**. [Langfuse](../agents/langfuse.md) scores almost nothing here by design: it *watches* agents rather than acting, so its real columns are **deployment control** (free unlimited self-host) and **human approval** (annotation queues, LLM-as-a-judge review) — see [observability & evals](../comparisons/observability-and-evals.md).

## Self-Hosted, Multi-Channel & Autonomous

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Hermes Agent](../agents/hermes-agent.md) | ● | ● | ● | ● | ● | ◐ | ◐ | ● | ● |
| [OpenClaw](../agents/openclaw.md) | ● | ● | ◐ | ● | ● | ◐ | ◐ | ● | ● |
| [Mercury Agent](../agents/mercury-agent.md) | ● | ◐ | ● | ◐ | ◐ | ● | ● | ◐ | ● |
| [Goose](../agents/goose.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ◐ | ● |
| [OpenHuman](../agents/openhuman.md) | ● | ○ | ● | ◐ | — | ◐ | ● | ◐ | ● |
| [AutoGPT](../agents/autogpt.md) | ● | ◐ | ◐ | ● | ◐ | ○ | ◐ | ◐ | ● |
| [AI Edge Gallery](../agents/ai-edge-gallery.md) | ◐ | ○ | ○ | — | — | ◐ | — | ◐ | ● |

Standouts: Hermes is the broadest single profile on this map — strong on nearly every dimension. Mercury pairs headline **human approval** with **scheduling** (permission-hardened, always-on); OpenHuman turns **memory** + **scheduling** into a life-integration loop.

## Using This For Selection

1. **Circle the columns that are mandatory** for your workflow — not the ones that sound nice.
2. Keep only the rows that score **●** on those columns. A ◐ or ○ where you need a ● is where projects quietly fail you later.
3. For the survivors, flip to the cost side of the ledger: [cost & benchmarks](../comparisons/cost-and-benchmarks.md) for price and coding capability, and the profile's own "Operating Cost" section for the operational burden each strength carries.

For the full route view see [agents/](../agents/README.md); for popularity over time see [rankings/](../rankings/README.md).
