# ml-intern

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/ml-intern.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](ml-intern.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: ml-intern is an autonomous "ML engineer" agent — give it a task, it researches papers, writes code, and ships ML work using the Hugging Face ecosystem.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Hugging Face |
| Route | Domain-specific autonomous agent (ML engineering) |
| Open source | Yes (Apache-2.0, Python) |
| Best for | Letting an agent take an ML problem from "I read this paper" to "model card on the Hub" with deep HF tooling |
| Main cost | LLM API spend over long iterative loops, plus the discipline to review what the agent ships |
| Official website | https://smolagents-ml-intern.hf.space (web frontend) |
| GitHub repo | https://github.com/huggingface/ml-intern |

## When To Pick It

- You want an autonomous agent specialized for ML research and engineering, not a generic coding agent.
- You already work in the Hugging Face ecosystem and want native access to repos, datasets, models, and papers.
- You can stomach a long agentic loop (up to ~300 iterations) and have budget for it.

## When Not To Pick It

- You want a general-purpose autonomous agent — ml-intern is opinionated toward ML workflows.
- You need tight per-step approval; ml-intern is built for hands-off iteration with optional approval on sensitive ops.
- You don't use the Hugging Face Hub; the value is largely tied to that ecosystem.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Autonomous loop | Strong | Up to 300 iterations of plan → tool → result → refine |
| HF Hub integration | Very strong | Native access to repos, datasets, models, papers |
| Code execution | Strong | Sandbox execution for code testing |
| Provider coverage | Strong | Anthropic, OpenAI, local endpoints, MCP servers |
| General-purpose use | Limited | The whole framing is ML engineering |

## Operating Cost

Complexity is Medium-High. Installation is straightforward (`uv sync`), but operating cost compounds: long agentic loops consume tokens fast, sessions auto-upload to your private HF dataset (which is a feature, but a cost), and meaningful work needs review. Budget API spend accordingly.

## Bottom Line

ml-intern fills a gap in the autonomous agent landscape: most autonomous agents (AutoGPT, Agent Zero) are general-purpose; ml-intern is opinionated toward ML engineering and goes deep on the Hugging Face stack. If your problem fits the shape — a self-contained ML task with paper-to-shipping reach — it's the strongest current candidate. If it doesn't, a general autonomous agent or a coding agent is the better fit.
