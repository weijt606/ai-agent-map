# AutoGPT

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/autogpt.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](autogpt.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: AutoGPT evolved from the viral autonomous GPT-4 experiment into a visual agent-building platform with workflows, a marketplace, and multi-model support.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Significant Gravitas Ltd. |
| Route | Autonomous agent platform with visual workflow builder |
| Open source | Yes, custom license (source-available) |
| Best for | Building and sharing autonomous agents through a visual interface with multi-model support |
| Main cost | Token spend accumulates fast on autonomous loops; self-hosting requires Docker and infra management |
| Official website | https://agpt.co |
| GitHub repo | https://github.com/Significant-Gravitas/AutoGPT |

## When To Pick It

- You want a visual drag-and-drop workflow builder to design autonomous agents.
- You need multi-model support — OpenAI, Anthropic, Google, Meta, Mistral, and more.
- You want to browse and use pre-built agent templates from the marketplace.
- You want to import workflows from n8n, Make, or Zapier.
- You want both a cloud platform and a self-hosted option.

## When Not To Pick It

- You need deterministic, auditable execution for high-stakes or compliance workflows.
- You want a polished turnkey product. AutoGPT is still beta-grade in many areas.
- Autonomous agents running unsupervised make you uncomfortable — long-running loops can burn tokens and produce unreliable results.
- You need a coding-first agent. Look at Claude Code, Codex, or Devin instead.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Visual workflow builder | Strong | Drag-and-drop blocks for actions, logic, integrations |
| Autonomous execution | Strong | Multi-step autonomous task execution with retry |
| Multi-model support | Very strong | Supports most major LLM providers |
| Marketplace | Medium | Agent and workflow templates available |
| Workflow import | Medium | Can import from n8n / Make / Zapier |
| Determinism / reliability | Weak | Prone to looping and hallucination on ambiguous tasks |
| Coding-specific | Weak | General-purpose, not coding-first |

## Operating Cost

Complexity is High. Self-hosting requires Docker, database setup, and ongoing maintenance. The platform is free to use, but LLM API token costs accumulate quickly — autonomous agents that loop and retry can burn through budgets. The project has pivoted multiple times since 2023, so the API surface and architecture are still stabilizing.

## Bottom Line

AutoGPT is the most well-known autonomous agent project (182k stars) and has evolved significantly from a CLI experiment to a visual platform. The trade-off: high ambition, broad feature set, but reliability and polish are still catching up.
