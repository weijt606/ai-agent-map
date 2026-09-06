# DeepSeek V4

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/deepseek-v4.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](deepseek-v4.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: DeepSeek V4 is the MIT-licensed end of the open frontier — 1.6T parameters with 49B active, 1M context, 80.6 on SWE-bench Verified — and the licence is the point: its scores are reproducible by anyone with the GPUs.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | DeepSeek AI |
| Route | Open-weights agentic model |
| Weights | [`deepseek-ai/DeepSeek-V4-Pro`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) and [`DeepSeek-V4-Flash`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) — **MIT** |
| Best for | Teams that want a permissively licensed frontier model, self-hosted or through DeepSeek's API |
| Main cost | Pro is a 1.6T-parameter serving problem; Flash exists for that reason |
| Context | 1M tokens on both variants |
| Announcement | https://api-docs.deepseek.com/news/news260424/ |

## Why This Entry Exists

The open-weights tier is where several agents on this map actually run — [CodeWhale](codewhale.md) is built around DeepSeek and MiMo models, and [ZCode](zcode.md) can be pointed at DeepSeek's Anthropic-compatible endpoint. Profiling the products without the models left the map unable to answer the question underneath them.

DeepSeek is also the vendor behind [DeepSeek Harness](deepseek-harness.md), which means one company now sits on this map at both the model layer and the harness layer — with MIT on both.

## When To Pick It

- **MIT is a requirement.** This is the most permissive licence at this capability level; [Kimi K3](kimi-k3.md) ships a bespoke licence and [GLM-5.3](glm-5.md) is Apache-2.0.
- You want scores you can **reproduce rather than trust**. Open weights under MIT mean an independent lab with sufficient GPUs can re-run the evaluations — a materially different evidence position from a closed model's published table.
- You need **long context cheaply**: DeepSeek's stated design goal is world-leading long context at drastically reduced compute and memory cost, via token-wise compression and DeepSeek Sparse Attention.
- You want a smaller variant with the same lineage: **V4-Flash** is 284B total / 13B active, and DeepSeek reports its reasoning approaching Pro's when given a larger thinking budget.

## When Not To Pick It

- You need native multimodality in the model — [Kimi K3](kimi-k3.md) has the vision encoder.
- You need the strongest published coding numbers on the open tier — that argument belongs to [GLM-5.3](glm-5.md) and [Kimi K3](kimi-k3.md) depending on which benchmark you weight.
- You want to self-host Pro on modest hardware. 1.6T total parameters is a cluster, not a workstation; [Qwen3-Coder-Next](qwen3-coder.md) is the entry for that constraint.
- You want a vendor-managed agent product — DeepSeek ships the model and the harness separately, not a finished agent.

## Architecture And Numbers

| Property | V4-Pro | V4-Flash |
| --- | --- | --- |
| Total / activated parameters | 1.6T / 49B | 284B / 13B |
| Context | 1M tokens | 1M tokens |
| Licence | MIT | MIT |

| Benchmark | Score |
| --- | :-: |
| SWE-bench Verified | **80.6** |
| Terminal-Bench 2.0 (agentic) | 67.9 |
| LiveCodeBench (Pro-Max variant) | 93.5 |
| SimpleQA-Verified (Pro-Max variant) | 57.9 |

Architecture notes from the model card: a mixture-of-experts design with hybrid attention combining **Compressed Sparse Attention** and **Heavily Compressed Attention**, **Manifold-Constrained Hyper-Connections** for signal propagation, the **Muon** optimizer for training stability, and over **32T tokens** of pre-training. DeepSeek's own positioning has V4-Pro leading open models on reasoning, math, STEM, and coding, and trailing only Gemini-3.1-Pro on world knowledge.

## How To Read The SWE-bench Number

80.6 on SWE-bench Verified is the highest figure in this map's model layer — and it is not directly comparable to the numbers next to it. Anthropic publishes **SWE-bench Pro** (81.2 for [Fable 5.1](claude-fable-5.md)), a harder variant, and OpenAI quotes **DeepSWE** (74.1 for [GPT-6 Astra](gpt-6-astra.md)) rather than SWE-bench Verified at all. Three vendors, three benchmarks, no like-for-like row. This map records each vendor's own number and refuses to build the comparison table that would imply they are the same measurement — which is the honest state of the evidence in September 2026.

## Bottom Line

DeepSeek V4 is the licence answer on the open tier, and MIT at 1.6T parameters is a genuinely unusual thing to be able to write. Choose Pro if you have the cluster and want the ceiling, Flash if you want most of the reasoning at a fifth of the size — and hold the SWE-bench number as DeepSeek's own measurement on DeepSeek's chosen benchmark until someone independent re-runs it, which is at least something the licence permits.
