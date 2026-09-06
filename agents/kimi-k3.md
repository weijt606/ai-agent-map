# Kimi K3

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/kimi-k3.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](kimi-k3.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Kimi K3 is the first open 3T-class model — 2.8T parameters, natively multimodal, 1M context — and on its own published comparison it trades blows with the closed frontier on agentic coding rather than trailing it.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Moonshot AI |
| Route | Open-weights agentic model |
| Weights | [`MoonshotAI/Kimi-K3`](https://github.com/MoonshotAI/Kimi-K3) · [Hugging Face](https://huggingface.co/moonshotai) |
| Licence | **Kimi K3 License** — a custom licence, not OSI-standard; read it before commercial deployment |
| Best for | Teams that want frontier-class agentic capability with weights they control |
| Main cost | 2.8T parameters is a serving problem before it is a licensing one |
| Context | 1,048,576 tokens; text and image |
| Tech blog | https://www.kimi.com/blog/kimi-k3 |

## Why This Entry Exists

This map's model layer covered two closed vendors and nothing else, which left a real question unanswered: **how much do you give up by running weights you host yourself?** For most of 2025 the honest answer was "a lot". K3 is the entry that makes the answer arguable.

It is also the model under [Kimi Work](kimi-work.md) and adjacent to [Kimi Code](kimi-code.md), so it closes a loop this map already had two thirds of.

## When To Pick It

- You want **open frontier weights**. Moonshot's framing is exactly that: the full weights released so frontier intelligence is available for research, deployment, and further work.
- Your agent runs **long sessions over large repositories**. The stated design point is sustaining long engineering sessions with minimal oversight, navigating massive repositories, and orchestrating terminal tools.
- You need **native vision in the loop**, not a bolted-on captioner: a MoonViT-V2 encoder (401M) is part of the model, and the vendor cites vision-in-the-loop game development and CAD.
- You need genuinely long context — 1M tokens native.
- You want efficiency at serving time: quantization-aware training ships MXFP4 weights with MXFP8 activations.

## When Not To Pick It

- **The licence is bespoke.** It is the "Kimi K3 License", not Apache-2.0 or MIT. If your requirement is a standard permissive licence, [DeepSeek V4](deepseek-v4.md) (MIT) and [GLM-5.3](glm-5.md) (Apache-2.0) are the entries to compare against.
- **You cannot serve it.** 2.8T total parameters with 16 of 896 experts active per token is a serious deployment; if the point of open weights was to run locally, look at [Qwen3-Coder-Next](qwen3-coder.md) instead.
- You want a hosted product with support — this is a weights release.
- You need a vendor-neutral benchmark story: the comparison below is Moonshot's own.

## Architecture

| Property | Value |
| --- | --- |
| Total parameters | 2.8T (first open 3T-class model, per Moonshot) |
| Experts | 896, with 16 selected per token plus 2 shared |
| Attention | Kimi Delta Attention (KDA) and Gated MLA, with Attention Residuals |
| Context length | 1,048,576 tokens |
| Vision encoder | MoonViT-V2, 401M parameters |
| Quantization | MXFP4 weights / MXFP8 activations, quantization-aware training |
| Modality | Text and image |

Moonshot attributes roughly a **2.5x improvement in scaling efficiency over Kimi K2** to the Stable LatentMoE framework behind that expert configuration.

## Published Comparison

These are **Moonshot's own numbers**, from the model's README, at max settings. This map reproduces them because a vendor comparing itself against named closed models on named benchmarks is a checkable claim — not because it is neutral.

| Benchmark | Kimi K3 | Claude Fable 5 | GPT-5.6 Sol | Claude Opus 4.8 | GLM-5.2 |
| --- | :-: | :-: | :-: | :-: | :-: |
| Terminal-Bench 2.1 | **88.3** | 88.0 | 88.8 | 84.6 | 82.7 |
| SWE-Marathon | **42.0** | 35.0 | 39.0 | 40.0 | 13.0 |
| ProgramBench | **77.8** | 76.8 | 77.6 | 71.9 | 63.7 |
| FrontierSWE | 81.2 | **86.6** | 71.3 | 66.7 | 67.3 |
| DeepSWE | 67.5 | 70.0 | **73.0** | 59.0 | 46.2 |
| GPQA Diamond | 93.5 | 92.6 | **94.1** | 91.0 | 91.2 |

The shape worth reading: on long-horizon agentic work (Terminal-Bench, SWE-Marathon, ProgramBench) K3 is at or ahead of the closed frontier, while on single-shot software-engineering benchmarks (DeepSWE, FrontierSWE) it sits behind Fable 5 or Sol. That is a more useful distinction than a single ranking, and it maps onto how you would actually deploy it.

## Relationship To Moonshot's Products

K3 is the model. [Kimi Code](kimi-code.md) is the terminal coding agent, [Kimi Work](kimi-work.md) the desktop knowledge-work agent. If you want Moonshot's loop, take the products; this profile is for the case where you are wiring a model into your own system — see the [harness route](../comparisons/agent-harness-frameworks.md) for what to wire it into.

## Bottom Line

K3 is the strongest argument yet that the open-weights tier is a real option at the top of the market rather than a budget fallback — with two caveats that matter more than the benchmark table: the licence is custom, and 2.8T parameters means the serving bill replaces the token bill. Compare against [DeepSeek V4](deepseek-v4.md) if licence purity matters and [GLM-5.3](glm-5.md) if coding is the whole job.
