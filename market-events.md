# Market Events

[English](market-events.md) | [中文](zh/market-events.md)

Structural events that reshaped agent selection — model releases, product mergers, and waves — newest first. The weekly play-by-play lives in the "Market events" timeline in [agents/README.md](agents/README.md); this page keeps the durable records.

## August 21 2026 — OpenAI Cuts Sol By More Than 20%, And Price Moves The Board

OpenAI **lowered GPT-5.6 Sol from $5 / $30 to $4 / $20 per million input / output tokens on August 21 2026**, a cut of 20% on input and **33% on output**. It is billed as promotional and runs for three months — through at least November 21 2026 — and it applies to the pay-as-you-go API, **Codex credits**, and eligible ChatGPT Work plans, not just raw API calls. It is the second reduction in the GPT-5.6 family in under a month. The same day, OpenAI reported **20M active Codex users**.

**Impact on selection:** this is the first window in which the heat board's top mover is explained by a price change rather than a launch. [Codex CLI](agents/codex.md) went from #9 to #2 on a **4.5× jump in weekly star rate** — the largest re-acceleration this map has recorded — with no comparable product event inside the window; its releases over the period were ordinary increments (Bedrock Runtime support, async hooks with MCP tools, session forking and restore, TUI conversation export). Two things follow for selection. First, the output-side cut is the larger one, which matters disproportionately for agent workloads: an agent loop spends its tokens on generated diffs, tool calls, and reasoning, not on prompt text, so a 33% output cut is a bigger real discount than the headline "20%+" suggests. Second, and less comfortably, **the promotional framing is load-bearing**. A three-month rate is not a budget baseline; anything sized against $4 / $20 needs a November review, and a per-tier cost model — see [cost & benchmarks](comparisons/cost-and-benchmarks.md) — is now a live operational document rather than a reference table. The broader pattern the map has been tracking holds: vendors are competing on **access and price**, not on the loop.

Sources: [OpenAI cuts GPT-5.6 Sol prices](https://enterprisedna.co/resources/news/openai-gpt-56-sol-price-cut-20-percent-frontier-model-august-2026/), [GPT-5.6](https://openai.com/index/gpt-5-6/), [GPT-5.6 pricing after the cuts](https://cellcog.ai/blog/gpt-5-6-pricing/), [openai/codex releases](https://github.com/openai/codex/releases).

## August 5–10 2026 — Meta Closes The Vendor-CLI Field; Claude Code Goes Self-Hosted

Three things landed in one week, and together they move the vendor layer rather than the open-source one.

**Meta shipped [Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) (beta) on August 5**, a terminal coding agent powered by a new coding-focused model, **Muse Spark 1.2**. It installs with one command, coordinates multiple persistent subagents per task, and — the genuinely distinctive part — appends every model call, tool run, approval, and edit to a local event log, making the runtime **replay-exact and restart-safe** for long jobs. Default skills are `/plan` (task → approval-gated plan), `/grill` (stress-test that plan), and `/goal`. Muse Spark 1.2 is available through Muse Code, the Meta Model API, and OpenRouter.

**Anthropic put [self-hosted environments for Claude Code](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute) into public beta on August 6** — sessions run on the customer's own infrastructure, inside their network and next to internal services, instead of Anthropic-hosted compute. Team and Enterprise only, off by default, unavailable to organizations on ZDR.

**OpenAI released [GPT-5.6-Cyber](https://developers.openai.com/api/docs/models/gpt-5.6-cyber) on August 10**, a security-specialized model built on GPT-5.6 Sol and gated behind approval in the Daybreak program.

**Impact on selection:** this map wrote in July that "every major model vendor now ships a first-party coding CLI" and listed the field as Anthropic, OpenAI, Moonshot, Xiaomi, and xAI. Meta was the conspicuous absence, and now is not — but note *how* it arrived. Muse Code is a beta distributed through the Meta Model API with **no public repository**, so unlike Grok Build it does not even reach the source-available end of the governance split; it is not tracked on this map's boards for that reason. The vendor field closing shut in under a month, mostly with agents you cannot read, is the actual story. Meanwhile the Claude Code and GPT-5.6-Cyber releases point the same direction from a different angle: the differentiator vendors are now competing on is **deployment and access control** — whose infrastructure the loop runs on, and who is allowed to run it — not the loop. Muse Code's replay-exact event log is the one genuine capability idea in the batch, and it is the same durability problem the [observability layer](comparisons/observability-and-evals.md) attacks from outside. Pricing and index figures for Muse Spark 1.2 are not yet recorded here, so it does not appear in [cost & benchmarks](comparisons/cost-and-benchmarks.md).

Sources: [Introducing Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2), [developer.meta.com/ai/models/muse-spark](https://developer.meta.com/ai/models/muse-spark/), [Self-hosted environments for Claude Code](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute), [Claude Code self-hosted docs](https://code.claude.com/docs/en/self-hosted-environments), [GPT-5.6-Cyber](https://developers.openai.com/api/docs/models/gpt-5.6-cyber).

## July–August 2026 — The Meta-Harness Appears

Two projects landed the same idea from opposite ends within weeks of each other. **[QM](agents/qm.md)** (`yc-software/qm`, MIT) — Y Combinator's *multiplayer* agent for Slack and the web — reached **~11.4k stars and 1.3k forks in its first seven days**, and **[Omnigent](agents/omnigent.md)** (`omnigent-ai/omnigent`, Apache-2.0) passed 8k. Neither ships an agent loop. Both are layers that run *other* harnesses — Pi, OpenCode, Codex, Claude Code, Cursor, Hermes — behind one interface, and add what a bare loop leaves out: identity, approval policy, spend caps, sandboxing, scheduling, and session continuity.

**Impact on selection:** for two years the harness question was "which one do I fork." These projects assume the answer is "several, and that is fine" — which is a bet that the loop itself is commoditizing and the durable value sits in the governance layer above it. If that bet is right, "which harness" becomes a reversible decision and the important choice moves up a level. Note the two split cleanly on unit of account: QM's is an **organization** (a scope per person and per room, one admin-set security posture, self-hosted in your own cloud), Omnigent's is a **developer** (one session following you across terminal, browser, phone, and desktop, across nine cloud sandbox providers). Also note the maturity: QM is days old and Omnigent is self-declared alpha, so this is a shape worth tracking, not yet a layer worth depending on. QM carries the same governance caveat the map flagged for Grok Build in a different form — the license is MIT, but contributions are accepted as *written proposals*, not code. Details: [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [agent harness frameworks](comparisons/agent-harness-frameworks.md).

Sources: [yc-software/qm](https://github.com/yc-software/qm), [qm.ycombinator.com](https://qm.ycombinator.com), [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent), [omnigent.ai](https://omnigent.ai).

## July 14 2026 — xAI Ships Grok Build, And Open Source Splits In Two

SpaceXAI (xAI) released **[Grok Build](agents/grok-build.md)** (`grok`), a Rust terminal coding agent in the Claude Code mold — full-screen TUI, headless mode for CI, and an Agent Client Protocol server so editors can drive it, plus MCP servers, skills, plugins, hooks, and sandboxing. It reached **23.2k stars and 4.4k forks within 15 days**, the fastest debut this map has recorded. Every major model vendor now ships a first-party coding CLI.

**Impact on selection:** the vendor-CLI field is now essentially complete (Anthropic, OpenAI, Moonshot, Xiaomi, xAI), so "which coding CLI" is increasingly downstream of "which model do you pay for." The more durable lesson is a governance split the map now has to make explicit: Grok Build is **Apache-2.0 but closed to contributions** — a periodic export from a private monorepo, with in-tree ports of `openai/codex` and `sst/opencode` tool code. Source-available and community-built have visibly diverged, and the LICENSE file no longer tells you which one you are getting. Details: [Grok Build](agents/grok-build.md), [terminal coding CLI comparison](comparisons/coding-cli-agents.md).

Sources: [xai-org/grok-build](https://github.com/xai-org/grok-build), [x.ai/cli](https://x.ai/cli), [docs.x.ai/build/overview](https://docs.x.ai/build/overview).

## July 9 2026 — Codex Merges Into ChatGPT; GPT-5.6 Ships

OpenAI merged the standalone Codex app into the ChatGPT desktop app (macOS/Windows): Codex is now a dedicated coding entry next to Chat and the new agentic **ChatGPT Work** mode, available on every plan including Free. The same day, **GPT-5.6** replaced GPT-5.5 across ChatGPT, Codex, and the API in three tiers — Sol ($5/$30 per M tokens), Terra ($2.5/$15), Luna ($1/$6) — plus an Ultra multi-agent setting. Codex reports 5M+ weekly users, over 1M of them working outside software development.

**Impact on selection:** the "which coding agent" question on the OpenAI side collapsed into "how do you use ChatGPT" — the product boundary moved, not just the capability. GPT-5.6 Sol leads the Artificial Analysis Coding Agent Index (80, vs Fable 5 77.2, GPT-5.5 76.4, Opus 4.8 72.5) at GPT-5.5's old price, making GPT-5.5 a legacy choice. Details: [Codex](agents/codex.md), [GPT-5.5](agents/gpt-5.5.md).

Sources: [OpenAI Codex changelog](https://learn.chatgpt.com/docs/changelog), [GPT-5.6 announcement](https://openai.com/index/gpt-5-6/), [Axios](https://www.axios.com/2026/07/09/ai-openai-gpt-release).

## June 17 2026 — Vercel Ships eve, And The Build-Your-Own Route Grows A Delivery Surface

Vercel released **[eve](agents/eve.md)** (`vercel/eve`, Apache-2.0) at Vercel Ship in London, as part of a set of products it groups under **Agent Stack**. The framing is "Next.js for agents": an agent is a *directory of files* — `instructions.md`, `tools/`, `skills/`, `subagents/`, `channels/`, `schedules/`, `connections/` — and the framework owns durable execution (checkpointed sessions on the open-source Workflow SDK that survive crashes *and* redeploys), a per-agent sandbox, `needsApproval` gates that pause a run indefinitely without consuming compute, subagents with isolated context windows, `defineEval` test suites, and channel adapters for Slack, Discord, Teams, GitHub, Linear, Telegram, Twilio, and HTTP. It reached **4.8k stars** in its first ten weeks. **This map missed it at the time and is recording it now as a backfill**, alongside the profile.

**Impact on selection:** eve changes the shape of the build-your-own route rather than just lengthening it. Every other framework on that route ([LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md)) scores **—** on delivery surfaces in the [capability matrix](capabilities/matrix.md), because they are libraries and where the agent *shows up* is your problem. eve is the first entry there with channels, scheduling, and approvals as framework primitives — which makes it the closest thing on the build side to what the [meta-harnesses](agents/qm.md) do on the operate side. The cost is on the last column: it is the only framework on that route whose documented production path runs through one vendor's platform (`vercel deploy`, sandboxes and model access via AI Gateway), with self-hosting undocumented. Apache-2.0 makes the code portable; it does not make the deployment portable. That is a clean, explicit trade — batteries in exchange for a platform — and it is the whole decision.

Sources: [Introducing eve](https://vercel.com/blog/introducing-eve), [vercel/eve](https://github.com/vercel/eve), [eve.dev](https://eve.dev/), [Vercel debuts eve](https://www.theregister.com/devops/2026/06/19/vercel-debuts-eve-open-source-agent-framework-tries-to-fix-shadow-ai-with-passport/5258726).

## June 9 2026 — Claude 5 Family: Fable 5 And The Mythos Tier

Anthropic released **Claude Fable 5** and **Claude Mythos 5** — the same underlying model, with Fable 5 generally available (with added safety measures) and Mythos 5 restricted to approved organizations. Mythos is a new tier above Opus. Fable 5 became the default Claude Code model for Pro/Max, was pulled worldwide June 12 under short-lived US export controls, returned July 1 behind stricter safety classifiers (blocked requests fall back to Opus 4.8), and moved to metered usage credits on July 7. Two weeks earlier (May 28), **Opus 4.8** had already fixed Opus 4.7's tool-calling issues and shipped Dynamic workflows.

**Impact on selection:** the Anthropic model layer became a two-tier budget decision — Fable 5 credits for the hardest work, Opus 4.8 as the dependable default. Details: [Claude Fable 5](agents/claude-fable-5.md), [Claude Code](agents/claude-code.md).

Sources: [Anthropic announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5), [Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5), [Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8).

## May 2026 (ongoing) — The `.claude/skills` Wave

The wave that broke into GitHub trending in mid-May keeps compounding: curated skill collections and skills frameworks have held roughly half of the weekly heat top 10 ever since. Star counts as of 2026-08-12:

| Repo | Stars | Shape |
| --- | --- | --- |
| [Superpowers](agents/superpowers.md) | 270.9k | Complete skills framework + methodology, plugging into Claude Code, Codex, Cursor, Copilot, and more |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 214.3k | Matt Pocock's curated personal `.claude/skills` directory |
| [anthropics/skills](https://github.com/anthropics/skills) | 168.4k | Anthropic's canonical Agent Skills reference — the upstream source of the pattern |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 86.4k | Addy Osmani's production-grade engineering skill set for coding agents |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 42.1k | Curated academic research pipeline for Claude Code |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 33.3k | Ready-to-use skills for research, science, engineering, analysis, finance, writing |

Through August the wave stopped growing in *breadth* and started rotating in place: it has held exactly four of the weekly top ten for two windows running while the membership churns, and the movement is increasingly concentrated in the two largest curated directories. In the 2026-08-05 → 08-12 window `mattpocock/skills` and `addyosmani/agent-skills` took the top two gain seats outright for the first time, the latter on a 4.9× jump (+945 → +4,664) after a window off the table entirely.

**Impact on selection:** the `.claude/skills` pattern crossed from curiosity into shared infrastructure — engineers publish skill libraries the way they used to publish dotfiles, and for many tasks the skill layer matters as much as the underlying agent. The concentration is worth watching, though: a wave whose gain increasingly accrues to two personal directories is a wave with key-person risk, not a broadening ecosystem. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks curated collections as watchlist entries (content assets, not agent surfaces); the wave has its own boards in [rankings/skill-verticals.md](rankings/skill-verticals.md).

## April 2026 — GPT-5.5 And "Codex For (Almost) Everything"

Two OpenAI releases a week apart set up the spring landscape. **April 16**: the largest Codex product update before the ChatGPT merge — background Computer Use across any macOS app, parallel multi-agent execution on one machine, an in-app browser with proactive suggestions, 90+ plugins, and 3M weekly developers (2x early March). **April 23**: **GPT-5.5** shipped as OpenAI's frontier agentic model — 82.7% on Terminal-Bench 2.0 (highest at launch), a 1M-token context window, at 2x GPT-5.4's price.

**Impact on selection:** together they raised the ceiling for every OpenAI-based surface and made the model layer part of agent selection. Both have since been superseded (see the July 9 entry) but remain the reference point for how fast the 2026 race moved. Details: [GPT-5.5](agents/gpt-5.5.md), [Codex](agents/codex.md).

## January 2026 — ClickHouse Acquires Langfuse

ClickHouse acquired **[Langfuse](agents/langfuse.md)**, the most-starred open-source LLM/agent observability platform (32.0k stars as of 2026-07-29). Langfuse offers tracing, evaluation, prompt management, and datasets under an open-core model — MIT core, with governance features under a separate Enterprise license — and remains free to self-host without limits.

**Impact on selection:** agent observability is being absorbed into general data infrastructure rather than remaining a standalone category, which matters if you are betting on a vendor staying independent. It also sharpens a distinction this map now documents explicitly: in this layer "open source" spans four different things — permissive (Opik, Traceloop, Helicone under Apache-2.0), open core (Langfuse), source-available but not OSI-approved (Arize Phoenix under Elastic 2.0), and fully closed (LangSmith, Braintrust). Langfuse states it remains 100% open source with an unchanged roadmap; that is a vendor commitment, not a verifiable guarantee. Details: [Langfuse](agents/langfuse.md), [observability & evaluation](comparisons/observability-and-evals.md).

Sources: [Joining ClickHouse](https://langfuse.com/blog/joining-clickhouse), [ClickHouse announcement](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), [langfuse/langfuse](https://github.com/langfuse/langfuse).
