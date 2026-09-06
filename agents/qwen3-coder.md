# Qwen3-Coder

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/qwen3-coder.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](qwen3-coder.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Qwen3-Coder is the open-weights line you pick when the model has to fit on hardware you already have — Qwen3-Coder-Next activates about 3B parameters out of 80B per token and, on Alibaba's own framing, lands comparable to Claude Sonnet among open models on agentic coding.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Alibaba / Qwen |
| Route | Open-weights agentic model |
| Weights | [`QwenLM/Qwen3-Coder`](https://github.com/QwenLM/Qwen3-Coder) · [Hugging Face](https://huggingface.co/collections/Qwen/qwen3-coder-687fc861e53c939e52d52d10) |
| Sizes | Qwen3-Coder-480B-A35B-Instruct, 30B-A3B-Instruct, and **Qwen3-Coder-Next** (80B-A3B) |
| Best for | Local and cost-constrained agent deployments that still need real agentic coding |
| Main cost | Not the top of the open tier on raw capability — it trades ceiling for footprint |
| Context | 256K native, extendable to 1M with Yarn |
| Blog | https://qwenlm.github.io/blog/qwen3-coder-next/ |

## Why This Entry Exists

Every other model on this route answers "how close can open weights get to the frontier". Qwen3-Coder answers a different and, for many teams, more practical question: **what is the best agentic coding model that actually fits?**

[Kimi K3](kimi-k3.md) is 2.8T parameters and [DeepSeek V4](deepseek-v4.md) Pro is 1.6T. Those are clusters. Qwen3-Coder-Next is built on Qwen3-Next-80B-A3B-Base with a hybrid attention and MoE architecture that activates roughly 3B parameters per token — a different deployment class entirely, and the reason this entry earns a place next to models that beat it on benchmarks.

## When To Pick It

- **The model has to run where you are** — a workstation, a single node, an air-gapped environment, or a cost ceiling that a 1.6T model cannot meet.
- You want it wired into an existing loop: Qwen explicitly supports **Qwen Code, Cline, and Claude Code**, with a purpose-designed function-call format.
- You need **repository-scale context** without a frontier bill: 256K native, up to 1M with Yarn.
- Your codebase is unusual — the line advertises **358 coding languages**.
- You want size options rather than one deployment shape: 480B-A35B at the top, 30B-A3B for small deployments, Next as the efficiency pick.

## When Not To Pick It

- You want the open tier's capability ceiling — that is [Kimi K3](kimi-k3.md) or [GLM-5.3](glm-5.md) depending on the benchmark.
- You need native vision in-model.
- You need a licence guarantee from this page: the GitHub repository does not expose a standard licence field, so **verify the licence on the specific Hugging Face checkpoint you intend to use** — the Qwen line has historically shipped different terms for different sizes, and this map does not assert one.
- You want a finished agent — that is Qwen Code, a separate project this map does not yet profile.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Efficiency per unit capability | Very strong | ~3B activated of 80B on Next; the reason to choose this line |
| Agentic coding | Strong | Alibaba positions it as comparable to Claude Sonnet among open models on agentic coding and browser use |
| Long context | Strong | 256K native, 1M with Yarn, aimed at repository-scale understanding |
| Harness compatibility | Very strong | Qwen Code, Cline, Claude Code; dedicated tool parser in SGLang and vLLM |
| Language breadth | Very strong | 358 coding languages |
| Ceiling | Medium | Deliberately not competing for the top of the open tier |
| Licence clarity | **Check per checkpoint** | Not asserted here; confirm on the checkpoint you deploy |

## Deployment Note

Function calling depends on Qwen's tool parser in **SGLang** and **vLLM**, and the special tokens and token ids were updated for consistency with Qwen3 — so use the new tokenizer. That is the kind of detail that turns into a silent tool-calling failure inside an agent loop, which is why it is on this page rather than left to the model card.

## Bottom Line

Qwen3-Coder is the open tier's practical option: not the highest ceiling, but the one whose deployment story is a single machine rather than a cluster, with first-class support in harnesses this map already covers. If your constraint is hardware or cost rather than capability, start here and compare upward — and read the licence on the exact checkpoint before you ship.
