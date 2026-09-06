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

## Direct-Execution Agents (Terminal & Desktop)

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Claude Code](../agents/claude-code.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ● | ◐ |
| [Codex](../agents/codex.md) | ● | ● | ○ | ◐ | ● | ◐ | ◐ | ● | ○ |
| [Aider](../agents/aider.md) | ◐ | ● | ○ | ○ | — | ● | — | ○ | ◐ |
| [Kimi Code](../agents/kimi-code.md) | ● | ● | ○ | ○ | — | ◐ | — | ◐ | ◐ |
| [MiMoCode](../agents/mimocode.md) | ● | ● | ● | ○ | — | ◐ | — | ○ | ◐ |
| [CodeWhale](../agents/codewhale.md) | ● | ● | ○ | ○ | — | ◐ | — | ○ | ◐ |
| [Grok Build](../agents/grok-build.md) | ● | ● | ○ | ◐ | — | ◐ | ○ | ◐ | ◐ |
| [OpenCode](../agents/opencode.md) | ● | ● | ○ | ◐ | ○ | ◐ | — | ◐ | ● |
| [Gemini CLI](../agents/gemini-cli.md) | ● | ● | ○ | ○ | — | ◐ | — | ◐ | ◐ |
| [Qwen Code](../agents/qwen-code.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | — | ● | ● |
| [ZCode](../agents/zcode.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ● | ○ |

Standouts: Claude Code and Codex are the broadest **delivery surfaces**; MiMoCode and Qwen Code are the entries treating **memory** as a headline feature; Aider leads on explicit-diff **human approval**. Grok Build is the strongest **tool use** + **code execution** pairing among the vendor CLIs (MCP, skills, plugins, hooks, sandboxing, workspace checkpoints), but note its **deployment control** score reflects a source-available tree that does not accept contributions.

Four entries were added on 2026-09-06 and they split the route along **deployment control**, which is the column that actually separates them. [OpenCode](../agents/opencode.md) takes ● because it is MIT and belongs to no model vendor — the reason other harnesses build on it. [Qwen Code](../agents/qwen-code.md) also takes ●, and is the widest row here on **delivery surfaces** (terminal, IDE plugins, desktop, daemon mode, SDKs, and four IM platforms) because the client *and* the weights are open and it switches providers at runtime. [Gemini CLI](../agents/gemini-cli.md) is ◐: an Apache-2.0 client bound to one vendor's models, with a rate-limited free tier that is a genuine constraint on unattended runs. [ZCode](../agents/zcode.md) is ○ — a closed desktop client — and is the one entry in this group that is **not a terminal CLI**: its primary object is a long-running "Goal" you check on from WeChat, Feishu, or Telegram, which is why it scores ○ on **scheduling** where the terminal loops score — at all.

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
| [TrueForge](../agents/trueforge.md) | ● | ● | ○ | ● | ◐ | ● | — | ◐ | ● |
| [DeepSeek Harness](../agents/deepseek-harness.md) | ● | ● | ○ | ● | ◐ | ● | — | ● | ● |

Standouts: the whole route is defined by **deployment control** (you own the loop). jcode is the only harness with **memory** as a headline (passive semantic graph — see [memory approaches](../comparisons/memory-approaches.md)); OpenHands and OpenHarness carry the most **orchestration**.

The two meta-harnesses score wide because they add the layer the single-loop harnesses deliberately leave out — and they split cleanly. [QM](../agents/qm.md) is the only entry on this route with **memory**, **scheduling**, and **delivery surfaces** all as core, because each scope owns its own memory, crons, and Slack/web presence; its **tool use** is deliberately ◐ (a small fixed tool surface, extended through skills rather than breadth). [Omnigent](../agents/omnigent.md) instead leads on **multi-agent** — mixing several harnesses in one session, including having one review another — and both make **human approval** core through policy engines rather than per-edit prompts. Read both marks with their maturity in mind: QM is days old and Omnigent is self-declared alpha, so these reflect stated design centers, not field-proven behavior.

[TrueForge](../agents/trueforge.md) is a third shape: one loop, but run as a server behind an HTTP API. It scores like a single-loop harness on **tool use** and **code execution**, like a meta-harness on **orchestration** and **human approval** (both are product surfaces here, not debug prompts), and takes the route's usual ● on **deployment control** — it is MIT and self-hosted by design. The two blanks are the shape: **no scheduling primitive at all**, and **delivery surfaces** stop at a chat UI, an API, and an embeddable widget rather than channel adapters. Its **memory** ○ is deliberate: persisted sessions and compaction are durability and context engineering, not learning across sessions. Same maturity caveat — six weeks public, still on 0.x release candidates.

[DeepSeek Harness](../agents/deepseek-harness.md) is a fourth shape again, and its row reads oddly until you know why: it scores ● on **orchestration**, **human approval**, and **delivery surfaces** not because it ships more features than the loops above it, but because all three are *plugins in the base layer* rather than product decisions — the agent loop itself is replaceable from configuration, approval and sandbox policy live in the shared `dsh-base` bundle, and one codebase emits a web UI, a headless runner, a JSON-RPC SDK, and an ACP server. Its **memory** ○ is the same call made for TrueForge: an append-only session log is durability, not learning. **Scheduling** is blank because there is no scheduling primitive. Read every mark against the project's own label — developer preview, with compatibility-breaking changes promised.

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
| [Froge Code](../agents/froge-code.md) | ● | ● | ○ | ● | ◐ | ● | — | ○ | ◐ |

Standouts: Cline and CoStrict make **human approval** the whole point; CoStrict is the only one here strong on **deployment control** (private, on-prem) and **orchestration** (a standardized requirement→review workflow).

[Open Code Review](../agents/open-code-review.md) is the odd shape in this group and worth reading carefully: it scores **—** on code execution and memory because it never runs your code and keeps no state beyond a resumable session, and only **◐** on human approval — not because humans are sidelined, but because it has no approval gate to offer: it comments and stops. Its **orchestration** ● is unusual for a review tool and is the actual product — deterministic file selection, bundling into concurrent sub-agents, and rule matching wrapped around the model. Its **delivery surfaces** ● covers a CLI, four CI systems, and plugins for Claude Code, Codex, Cursor, and OpenCode.

[Froge Code](../agents/froge-code.md) fits this group on the strength of **human approval** — picking between parallel attempts is the product, not a safety wrapper — with worktree isolation behind its **code execution** ●. Read its row with the caveat its own profile carries: the page is written against an **Automagik Genie mapping** that this map has flagged as provisional, so these marks describe that mapping rather than a settled product boundary.

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
| [eve](../agents/eve.md) | ● | ● | ◐ | ● | ● | ● | ● | ● | ◐ |
| [Microsoft Agent Framework](../agents/microsoft-agent-framework.md) | ● | ◐ | ◐ | ● | ● | ◐ | ○ | — | ● |
| [Semantic Kernel](../agents/semantic-kernel.md) | ● | ◐ | ◐ | ● | ● | ○ | ○ | — | ● |
| [Haystack](../agents/haystack.md) | ● | ○ | ◐ | ● | ◐ | ○ | — | ◐ | ● |
| [Pydantic AI](../agents/pydantic-ai.md) | ● | ○ | ○ | ◐ | ○ | ○ | ○ | — | ● |
| [DSPy](../agents/dspy.md) | ◐ | ○ | ○ | ● | ○ | ○ | — | — | ● |

Standouts: LangGraph is the strongest of the libraries on durable **memory** and **multi-agent** state; LlamaIndex's memory is data/retrieval, not conversation.

[eve](../agents/eve.md) is the row that breaks this group's shape and is worth reading as a contrast. Everything above it scores **—** on delivery surfaces, because a library does not decide where the agent shows up; eve ships eight-plus channel adapters, so it is the only entry here with **delivery surfaces**, **scheduling**, and **human approval** all core (`needsApproval` pauses a run indefinitely without consuming compute). Its **code execution** ● is a per-agent sandbox rather than a helper tool, and its **memory** is deliberately ◐ — checkpointed durable sessions are state that survives a redeploy, not a memory system. The one column it gives up is the one every library above it owns: **deployment control** is ◐ because the documented production path is Vercel, Apache-2.0 license notwithstanding.

[Microsoft Agent Framework](../agents/microsoft-agent-framework.md) sits with the libraries rather than with eve: **delivery surfaces** is blank for the same reason LangChain's is — it hands you SDKs, not channels. What separates it inside the group is **orchestration** and **multi-agent** as named graph patterns (sequential, concurrent, handoff, group collaboration) across Python, .NET, and Go, plus **human approval** as a first-class production concern rather than an afterthought. Its **scheduling** ○ reflects durability and restartability, which is not the same as a scheduler. Note the succession: this row replaces the AutoGen row this matrix never had, because AutoGen is in maintenance mode.

The four libraries backfilled on 2026-09-06 sharpen what this group's blank **delivery surfaces** column actually means. [Semantic Kernel](../agents/semantic-kernel.md) scores like LangGraph on **orchestration** and **multi-agent** (planners plus a first-class agent framework) and is the one entry here whose spread across C#, Python, and Java is the reason to choose it. [Haystack](../agents/haystack.md) is the exception on **delivery surfaces** — Hayhooks exposes pipelines over HTTP and MCP, which none of the other libraries do — while its **code execution** stays ○ because it retrieves and routes rather than runs. [Pydantic AI](../agents/pydantic-ai.md) reads narrow on purpose: its differentiators (type safety, structured outputs, dependency injection) are not columns in this matrix, and its own profile calls multi-agent orchestration a non-goal. [DSPy](../agents/dspy.md) is the least agent-shaped row in the group — **orchestration** ● for composable modules, ◐ on **tool use**, and blanks below, because it is a prompt compiler you point at a pipeline, not a runtime.

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
| [WorkBuddy](../agents/workbuddy.md) | ● | ◐ | ○ | ● | ● | ○ | ● | ● | ○ |
| [Kimi Work](../agents/kimi-work.md) | ● | ◐ | ◐ | ● | ● | ○ | ● | ◐ | ○ |
| [Agent Zero](../agents/agent-zero.md) | ● | ● | ● | ◐ | ● | ○ | — | ○ | ● |
| [Julep](../agents/julep.md) | ● | ◐ | ● | ● | ◐ | ○ | ● | ○ | ● |
| [GenericAgent](../agents/generic-agent.md) | ● | ● | ● | ○ | — | ○ | — | ○ | ● |
| [ml-intern](../agents/ml-intern.md) | ● | ● | ○ | ◐ | — | ○ | — | ○ | ● |

Standouts: Hermes is the broadest single profile on this map — strong on nearly every dimension. Mercury pairs headline **human approval** with **scheduling** (permission-hardened, always-on); OpenHuman turns **memory** + **scheduling** into a life-integration loop.

[WorkBuddy](../agents/workbuddy.md) and [Kimi Work](../agents/kimi-work.md) are the first desktop knowledge-work agents in this matrix, and they score almost identically for a reason: they are the same loop pointed at documents instead of repositories. Both take ● on **orchestration**, **multi-agent**, and **scheduling** — parallel specialists on one goal, running on a cron or in the vendor's cloud around the clock — and both take ○ on **human approval** and **deployment control**, which is the honest cost. These are closed clients holding authorized access to your filesystem, and in Kimi Work's case a browser you are already logged into, with no documented per-action gate. Every other ● on those two rows should be read through that ○.

The four backfilled on 2026-09-06 split into two shapes. [Agent Zero](../agents/agent-zero.md) and [GenericAgent](../agents/generic-agent.md) both take ● on **memory** for the same unusual reason — they *learn*: Agent Zero remembers across sessions, and GenericAgent crystallizes each solved task into a reusable skill, which is closer to the spirit of that column than a session log is. [ml-intern](../agents/ml-intern.md) scores like a narrow autonomous coder (● on tool use and execution, — on multi-agent) and should be read with its own framing: the whole design is ML engineering, not general work. [Julep](../agents/julep.md) is the odd row and the most useful one — a Temporal-backed workflow engine, so **scheduling** and **memory** are core in a way no other entry in this group manages, at the cost of ○ on delivery surfaces and a **managed-hosting option that no longer exists**.

## Browser Agents

| Project | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Browser Use](../agents/browser-use.md) | ● | ○ | ○ | ○ | — | ○ | — | ◐ | ● |

Standouts: this row is deliberately narrow, because Browser Use is a **capability you give an agent**, not an agent that replaces one. **Tool use** is ● — driving a real browser is the entire product — and **deployment control** is ● (MIT, self-hostable, model-agnostic, with a hosted cloud as an option rather than a requirement). Everything else is thin on purpose: it does not orchestrate, schedule, or remember across runs; you bring the harness that does. The mark worth arguing about is **human approval** at ○. The library can be scoped, but the default posture is an autonomous loop acting inside your live sessions, and this map scores stated defaults rather than what a careful operator could configure. Compare Stagehand (MIT, TypeScript, SDK-shaped) and Skyvern (AGPL-3.0, workflow-shaped), both on the watchlist.

## What This Matrix Deliberately Does Not Score

Coverage here is a judgment, not an oversight, and the gaps are worth stating so nobody reads a missing row as a missing project.

- **Models** — [Fable 5.1](../agents/claude-fable-5.md), [Opus 5](../agents/claude-opus-5.md), [GPT-6 Astra](../agents/gpt-6-astra.md), [GPT-5.5](../agents/gpt-5.5.md), [Kimi K3](../agents/kimi-k3.md), [GLM-5.3](../agents/glm-5.md), [DeepSeek V4](../agents/deepseek-v4.md), [Qwen3-Coder](../agents/qwen3-coder.md). Every column here is a property of an agent *product* — approval gates, scheduling, delivery surfaces, deployment control. A model has none of them. Compare models in [cost & benchmarks](../comparisons/cost-and-benchmarks.md) instead.
- **[Superpowers](../agents/superpowers.md)** — a skills framework that runs *inside* other agents rather than having a loop of its own. Its capabilities are whichever agent you attach it to, so a row would measure the host, not the tool.
- **[BabyAGI](../agents/babyagi.md)** — kept in this map as a historical and educational entry; its own profile says it is not a production tool, and its capability table is scored on influence and educational value rather than on capability. A row in this matrix would imply it is a live candidate, which would be the wrong signal.

If a project is profiled and has none of the above reasons, a missing row is a backlog item rather than a decision.

## Using This For Selection

1. **Circle the columns that are mandatory** for your workflow — not the ones that sound nice.
2. Keep only the rows that score **●** on those columns. A ◐ or ○ where you need a ● is where projects quietly fail you later.
3. For the survivors, flip to the cost side of the ledger: [cost & benchmarks](../comparisons/cost-and-benchmarks.md) for price and coding capability, and the profile's own "Operating Cost" section for the operational burden each strength carries.

For the full route view see [agents/](../agents/README.md); for popularity over time see [rankings/](../rankings/README.md).
