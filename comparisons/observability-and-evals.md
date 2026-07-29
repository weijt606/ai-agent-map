# Agent Observability & Evaluation

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/observability-and-evals.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](observability-and-evals.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

Every other page on this map answers "which agent should do the work." This one answers the question that arrives immediately after you ship: **how do you know it worked?**

Once an agent runs unattended, the failure mode stops being a crash and becomes a *silent quality drift* — the loop still completes, the output is just worse, more expensive, or subtly wrong. Logs do not catch that. This layer exists to catch it.

## What These Tools Do — And Do Not Do

**They watch agents. They do not run them.** Every project on this page sits outside your execution path: your app emits traces, the platform stores, visualizes, and scores them. None of them replace [LangGraph](../agents/langgraph.md), [CrewAI](../agents/crewai.md), or a coding CLI — they instrument whatever you already chose.

The shared feature set has converged on four things:

| Capability | What it answers |
| --- | --- |
| **Tracing** | What did the agent actually do — every step, tool call, token, and millisecond |
| **Evaluation** | Was it any good — LLM-as-a-judge, code assertions, human review |
| **Prompt management** | Which prompt version produced this, and can I roll it back |
| **Datasets & experiments** | Does the change I am about to ship beat what is live |

Most teams need tracing on day one, evaluation by the time they have real users, and the rest only if prompt iteration becomes a team sport.

## The Field

Star counts and licenses checked **2026-07-29** against each project's own repository.

| Project | Open source? | License | Stars | Self-host | Shape |
| --- | --- | --- | --: | --- | --- |
| **[Langfuse](../agents/langfuse.md)** | Open core | MIT + EE | 32.0k | Free, unlimited | The OSS default — tracing + evals + prompt management in one self-hostable platform |
| **Comet Opik** | Yes | Apache-2.0 | 20.9k | Yes | The closest fully-permissive rival; strong eval focus, backed by Comet |
| **Arize Phoenix** | **No — source-available** | **Elastic 2.0** | 10.8k | Yes | Strong tracing and drift analysis, but the license is not OSI-approved |
| **Traceloop / OpenLLMetry** | Yes | Apache-2.0 | 7.3k | Yes | OpenTelemetry-native instrumentation layer; thinner UI, cleanest standards story |
| **Helicone** | Yes | Apache-2.0 | 6.0k | Yes | Proxy-first — easiest drop-in, since it can sit in front of the API call |
| **W&B Weave** | SDK only | Apache-2.0 | 1.1k | No (SaaS backend) | Natural pick if your ML org already lives in Weights & Biases |
| **LangSmith** | **No — closed** | SDK is MIT | — | Enterprise only | LangChain's first-party platform; deepest LangChain/LangGraph integration |
| **Braintrust** | **No — closed** | SDKs open | — | Enterprise only | Eval-first workflow, popular with teams treating prompts as CI artifacts |

> **"Open source" means four different things in this table** — and this is the distinction most comparisons blur. Apache-2.0 (Opik, Traceloop, Helicone) is genuinely permissive. **Open core** (Langfuse) means the core is MIT but governance features — RBAC, audit logs, SCIM, SSO, retention, masking — are commercially licensed. **Source-available** (Phoenix, under Elastic 2.0) lets you read and modify but restricts offering it as a service, and is *not* OSI-approved open source. **Closed** (LangSmith, Braintrust) publishes only client SDKs. Check the LICENSE file, not the marketing page.

## How To Choose

1. **Start from your framework, but do not stop there.** If you are all-in on LangChain/[LangGraph](../agents/langgraph.md), LangSmith is the path of least resistance — you are trading openness for integration depth. Everyone else should start at [Langfuse](../agents/langfuse.md), which integrates across [LlamaIndex](../agents/llamaindex.md), [CrewAI](../agents/crewai.md), OpenAI Agents SDK, Claude Agent SDK, and even coding agents like [Claude Code](../agents/claude-code.md), [Codex](../agents/codex.md), [Goose](../agents/goose.md), and [Pi](../agents/pi.md).
2. **Decide whether self-hosting is a requirement or a preference.** If prompts or traces carry regulated data, this collapses the field fast: Langfuse, Opik, Traceloop, and Helicone can run entirely on your infrastructure; LangSmith and Braintrust cannot, and Weave's backend is SaaS.
3. **Match the entry cost to your stack's maturity.** Helicone's proxy model is the fastest possible start (point your base URL at it). OTel-native instrumentation (Traceloop, and Langfuse's OTel path) costs more up front and avoids lock-in, because the traces are standard.
4. **Only pay for evaluation when you have something to evaluate against.** Datasets and LLM-as-a-judge are worth real money once you have production traffic to sample and regressions to catch — not before. Tracing first.
5. **Read the governance tier before you commit.** For most of these, the features that make a security review pass — SSO, RBAC, audit logs, data masking — are the paid ones. That is a licensing question, not a technical one, and it decides more migrations than feature lists do.

## Three Things Not To Mix Up

- **Observability is not evaluation.** Tracing tells you what happened; evaluation tells you whether it was good. Most tools here ship both, which makes it easy to buy one and never configure the other — and tracing alone will not catch quality drift.
- **A proxy is not an SDK is not OpenTelemetry.** Helicone's proxy sees traffic through the API boundary; an SDK sees your application's internal structure; OTel sees whatever you instrument, portably. They produce different traces at different granularity, and the choice is hard to reverse later.
- **Agent-facing is not agent.** Several of these expose MCP servers so *your* agent can query observability data — [Langfuse](../agents/langfuse.md) does, and it also ships an Agent Skill. That makes them agent-*accessible*, not agents. The one real agent loop in this field, Langfuse Assistant, operates the observability tool itself and is Cloud-only, beta, and approval-gated.

## Market Note

**ClickHouse acquired Langfuse in January 2026** — the largest consolidation this layer has seen, and a signal that agent observability is being absorbed into general data infrastructure rather than remaining a standalone category. Langfuse's stated commitment is that it remains fully open source with an unchanged roadmap; treat that as a vendor promise, not a verified guarantee. Details in [market events](../market-events.md).

For what these tools instrument, see [build-your-own frameworks](mainstream-agent-landscape.md) and the [capability matrix](../capabilities/matrix.md). For the profiled OSS reference, see [Langfuse](../agents/langfuse.md).
