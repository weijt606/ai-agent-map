# n8n

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/n8n.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](n8n.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: n8n is a workflow automation platform with native AI agent capabilities — 400+ integrations, visual builder, and self-hostable.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | n8n GmbH |
| Route | Visual workflow automation with AI agent nodes |
| Open source | Fair-code (Sustainable Use License, source-available, not OSI) |
| Best for | Teams that want to build AI agent workflows visually with real integrations, triggers, and custom code |
| Main cost | Self-hosting requires DevOps; cloud plans have execution limits; fair-code license is not MIT/Apache |
| Official website | https://n8n.io |
| GitHub repo | https://github.com/n8n-io/n8n |

## When To Pick It

- You want to build AI agent workflows with a visual drag-and-drop builder.
- You need 400+ integrations — Slack, Gmail, Notion, databases, webhooks, APIs.
- You want to self-host the entire platform for data control.
- You need AI agents with memory, tools, multi-agent orchestration, and LLM evaluation — all configured visually.
- You already use workflow automation and want to add AI agent capabilities on top.

## When Not To Pick It

- You need a pure OSI open-source license. n8n's fair-code license restricts commercial redistribution.
- You need real-time, sub-second latency pipelines. n8n is event-driven, not stream processing.
- You want a coding-first agent. n8n is a workflow platform, not a coding assistant.
- You are a non-technical team wanting pure no-code. n8n leans toward developers.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Visual workflow builder | Very strong | Drag-and-drop with 400+ integrations |
| AI agent nodes | Strong | Agent node with memory, tools, multi-agent orchestration |
| Self-hosting | Strong | Docker, Kubernetes, or bare metal |
| Integrations | Very strong | 400+ pre-built connectors |
| Custom code | Strong | JavaScript and Python nodes inside visual flows |
| LLM support | Strong | OpenAI, Anthropic, Google, Ollama |
| Coding-specific | None | Not a coding agent |

## Operating Cost

Complexity is Medium. Self-hosting is free with unlimited executions, but requires Docker/Kubernetes knowledge for setup and maintenance. Cloud plans range from $20 to $800/month with execution-based limits. The real value proposition is combining AI agent capabilities with the massive integration ecosystem — something pure agent frameworks do not offer.

## Bottom Line

n8n is the right choice when you need AI agents that connect to real systems — send emails, update databases, trigger webhooks, call APIs — all through a visual builder. It is not a coding agent; it is the workflow layer that makes agents operational.
