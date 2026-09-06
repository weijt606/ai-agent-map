# Microsoft Agent Framework

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/microsoft-agent-framework.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](microsoft-agent-framework.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Microsoft Agent Framework is the successor to AutoGen and the reason this map does not profile AutoGen — Microsoft put AutoGen into **maintenance mode** and points new users here.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Microsoft |
| Route | Build-your-own system |
| Repository | [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) — MIT, Python and .NET (Go SDK in [`agent-framework-go`](https://github.com/microsoft/agent-framework-go)) |
| Open source | Yes (MIT) |
| Best for | Teams taking multi-agent systems from prototype into production, especially on .NET |
| Main cost | Enterprise-shaped framework; heavier than a loop you can read in one sitting |
| Predecessor | **AutoGen** — 60.8k stars, now maintenance mode, community managed |
| Blog | https://devblogs.microsoft.com/agent-framework/ |

## Why This Entry Exists

Two reasons.

First, the map's [build-your-own route](../comparisons/agent-harness-frameworks.md) covered LangChain, LangGraph, CrewAI, Semantic Kernel, DSPy, Pydantic AI, and eve — and had nothing from the vendor whose previous framework (AutoGen) was one of the most cited in the category.

Second, and more useful: **AutoGen is the entry a reader would go looking for, and recommending it today would be wrong.** Its README carries a maintenance-mode notice — no new features or enhancements, community managed going forward — and directs new users here, with a published migration guide. This map's contribution rules require separating a current product from a superseded one rather than collapsing them, so the profile goes to the successor and records the lineage.

## When To Pick It

- You are **taking agents to production**, not prototyping: the project's own framing is durability, restartability, observability, governance, and human-in-the-loop control.
- You need **orchestration beyond a chat loop** — graph-based patterns for sequential, concurrent, handoff, and group-collaboration workflows.
- You are a **.NET shop**. This is the strongest first-class .NET option in this map's build-your-own route; Python and Go are supported alongside it.
- You want provider flexibility so the architecture survives a model change — Microsoft Foundry, Azure OpenAI, OpenAI, and the GitHub Copilot SDK are supported paths.
- You are migrating off AutoGen and want a supported destination with stable APIs and a long-term support commitment.

## When Not To Pick It

- You want something small. This is an enterprise-grade framework; if you want a loop you can read end to end, look at [mini-swe-agent](mini-swe-agent.md) or [Pi](pi.md).
- You want a finished agent product rather than a framework — see the direct-execution route.
- Your stack is Python-only and already committed to LangGraph or CrewAI; the migration cost is real and MAF's differentiator (multi-language, .NET-first-class) may not apply to you.
- You want vendor neutrality in the ecosystem: MIT and multi-provider, but the surrounding platform story is Microsoft's.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Multi-language reach | **Very strong** | Python, .NET, and Go — unmatched in this route |
| Orchestration patterns | Very strong | Sequential, concurrent, handoff, group collaboration as graph patterns |
| Production concerns | Very strong | Durability, restartability, observability, governance, human-in-the-loop |
| Provider flexibility | Strong | Microsoft Foundry, Azure OpenAI, OpenAI, GitHub Copilot SDK |
| Interoperability | Strong | A2A and MCP for cross-runtime work |
| Weight | Medium | Enterprise-shaped; not a small dependency |

## Note On AutoGen

AutoGen (`microsoft/autogen`, 60.8k stars, CC-BY-4.0) remains a widely cited multi-agent framework and a large body of existing code. Its current status, in its own words, is maintenance mode: no new features, community managed, with new users directed to this framework and existing users pointed at a migration guide. This map records it here rather than as its own entry, because a profile implies a current recommendation and this one would not be true. If you are evaluating agent frameworks and AutoGen came up in your research, that research is out of date — start here instead.

## Bottom Line

The reason to read this page is often the AutoGen note above it. As a framework, MAF is the production-and-.NET answer in the build-your-own route; as a map entry, it is a correction to a recommendation the ecosystem is still making by inertia.
