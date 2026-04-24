# Agent Zero

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/agent-zero.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](agent-zero.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Agent Zero is a general-purpose autonomous agent framework that dynamically creates its own tools, executes code, and learns organically — no predefined pipeline.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Jan Tomasek / agent0ai |
| Route | General-purpose autonomous agent framework |
| Open source | Yes |
| Best for | Developers who want a self-building, model-agnostic autonomous agent with dynamic tool creation |
| Main cost | Self-hosted only, no enterprise support, requires tuning for precise outputs |
| Official website | https://www.agent-zero.ai |
| GitHub repo | https://github.com/agent0ai/agent-zero |

## When To Pick It

- You want an agent that writes and executes its own tools at runtime instead of following a fixed pipeline.
- You need model flexibility — OpenAI, Anthropic, Groq, Ollama, and more via LiteLLM.
- You want multi-agent cooperation where the agent spawns sub-agents to divide tasks.
- You want persistent memory and self-correction across sessions.
- You are comfortable self-hosting and tuning.

## When Not To Pick It

- You need production-grade enterprise support and SLAs.
- You want a hosted SaaS with zero setup.
- You are on low-resource hardware — local models need 8GB+ RAM.
- You want polish and predictability over autonomy and flexibility.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Dynamic tool creation | Very strong | Core design — agent creates its own tools at runtime |
| Autonomous execution | Strong | Multi-step, self-correcting |
| Multi-agent | Strong | Spawns sub-agents for task division |
| Persistent memory | Strong | Remembers across sessions |
| Model agnostic | Very strong | Any provider via LiteLLM |
| Plugin ecosystem | Medium | Plugin Hub added in recent versions |
| Enterprise readiness | Weak | No commercial backing or SLA |

## Operating Cost

Complexity is Medium to High. Setup is ~10 minutes with Docker + Ollama, but ongoing tuning of model selection and prompts is your responsibility. Costs come from LLM API tokens or from running a VPS (~$24/month for a 4GB instance).

## Bottom Line

Agent Zero is for developers who want maximum autonomy in their agent — self-building tools, organic learning, no fixed pipeline. The trade-off is clear: no enterprise support, no hosted option, and you own the tuning.
