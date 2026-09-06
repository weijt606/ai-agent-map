# GLM-5.3

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/glm-5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](glm-5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: GLM-5.3 is the strongest open-weights coding model on Zhipu's own numbers, under Apache-2.0 — and it is also the first model on this map to ship state-of-the-art vulnerability-discovery capability with downloadable weights and no gate in front of it.

> This profile covers the GLM-5 series (5, 5.1, 5.2, 5.3, and 5.3-Flash), which ship from one repository.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Zhipu / Z.ai |
| Route | Open-weights agentic model |
| Weights | [`zai-org/GLM-5`](https://github.com/zai-org/GLM-5) — **Apache-2.0** |
| Best for | Long-horizon coding agents on weights you control, under a standard permissive licence |
| Main cost | Vendor-run benchmarks are the primary evidence; and see the cyber note below |
| Context | Solid 1M tokens (from 5.2) |
| Blog | https://z.ai/blog/glm-5.3 |

## Why This Entry Exists

Two reasons, and the second one is why this profile is longer than a spec sheet.

First, GLM is the model under [ZCode](zcode.md), and this map profiles the product without previously profiling what makes it work. Second, GLM-5.3 is the clearest instance so far of a pattern this map has been tracking from the closed side: **capability that vendors gate, arriving ungated**.

## When To Pick It

- You want **Apache-2.0**. Among the open frontier models here, this is the cleanest licence — [Kimi K3](kimi-k3.md) ships a bespoke licence and [DeepSeek V4](deepseek-v4.md) is MIT.
- **Coding is the whole job.** Zhipu positions 5.3 as the most capable open-weights model for coding, claiming a 50% improvement over 5.2 on their in-house Z.ai Code Bench and open-source state of the art on Terminal Bench 3.0 and Agents' Last Exam.
- You need long context that holds up: 5.2 introduced what Zhipu calls a *solid* 1M-token context, with IndexShare reusing one indexer across every four sparse attention layers to cut per-token FLOPs 2.9x at 1M.
- You want to tune spend per task — 5.2 added multiple thinking-effort levels.
- You want the efficient variant: **GLM-5.3-Flash** is a separately trained base model with a hybrid sparse-plus-linear attention architecture and Manifold-Constrained Hyper-Connections, aimed at cutting long-context serving cost.

## When Not To Pick It

- You need vendor-neutral evidence. The headline gains are measured on an in-house benchmark, and this map records that as a vendor claim.
- You need native multimodality in the same model — [Kimi K3](kimi-k3.md) ships a vision encoder in-model.
- You want a hosted product rather than weights — that is [ZCode](zcode.md) and the Z.ai API platform.
- **You have a policy position on dual-use capability.** See below; for some organizations this is a reason not to deploy it, and for others it is the reason to.

## Published Numbers (vendor-reported)

| Benchmark | GLM-5.2 | GLM-5.1 | Note |
| --- | :-: | :-: | --- |
| Terminal-Bench 2.1 | **81.0** | 62.0 | Zhipu puts this within a few points of Claude Opus 4.8 (85.0) |
| SWE-bench Pro | **62.1** | 58.4 | Strongest open-source result at the time of the 5.2 release |

For 5.3, Zhipu reports the gains as a 50% improvement over 5.2 on its in-house code benchmark plus open-source SOTA on Terminal Bench 3.0 and Agents' Last Exam, rather than as a public head-to-head table. [Kimi K3's own comparison](kimi-k3.md) puts GLM-5.2 at 82.7 on Terminal-Bench 2.1 — close to Zhipu's 81.0, which is a useful cross-check between two vendors who both had reason to measure it.

## The Cyber Capability Note

Zhipu states plainly that as post-training scaled, **cyber capability developed faster than expected**: GLM-5.3 is state of the art on CyberGym for vulnerability discovery, and its largest gains are further up the exploitation chain, where it **more than doubles GLM-5.2 on exploitation benchmarks**.

Set that beside what this map recorded in the same window on the closed side. [GPT-6 Astra](gpt-6-astra.md)'s generally available version **refuses part of its own cybersecurity capability**, with more behind Daybreak Blue approval. Anthropic's Mythos tier — the same underlying model as [Fable 5.1](claude-fable-5.md) with lighter safeguards — is restricted to vetted organizations through Project Glasswing. GLM-5.3 has the capability, an Apache-2.0 licence, and a download link.

This map does not editorialize about whether that is good. It records the selection consequence, which is concrete: **on the open tier, the gate is your policy, not the vendor's.** If you deploy here, the approval design in your harness is doing work that a closed vendor would otherwise be doing for you — see [observability and evals](../comparisons/observability-and-evals.md) and the approval columns in the [capability matrix](../capabilities/matrix.md). It also means a defender evaluating this model has the same access an attacker does, which is the argument the open-weights side makes for itself.

## Bottom Line

For a coding agent on self-hosted weights under a standard licence, GLM-5.3 is the strongest case on this map. Treat the in-house benchmark claims as claims, and treat the cyber capability as a live governance decision rather than a footnote — it is the first time this map has had to write that sentence about an openly downloadable model.
