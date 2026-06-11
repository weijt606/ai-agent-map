# CoStrict

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/costrict.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](costrict.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CoStrict is an enterprise-first coding agent built on the Cline / Roo Code lineage, but rebuilt around two things those tools leave to you — a standardized "strict" generation workflow (requirements → architecture → task plan → tests) and repository-wide AI code review — with private, physically-isolated deployment as a first-class option.

> **Lineage and vendor:** CoStrict (`zgsm-ai/costrict`, formerly the "诸葛神码 / Shenma" project, maintained by the zgsm-sangfor team) is a downstream of the Cline / Roo Code / kilo-code family. It keeps the editor-agent shape and adds an enterprise control layer on top.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | zgsm-ai (CoStrict / Sangfor) |
| Route | Review-first automation — enterprise, private-deployment |
| Open source | Yes (Apache-2.0) |
| Implementation | TypeScript |
| Surfaces | VS Code, JetBrains, CLI, Cloud (experimental) |
| Models | Built-in free models + Anthropic, OpenAI, OpenAI-compatible, and local models |
| Best for | Organizations that need standardized, reviewable AI coding with on-prem / isolated deployment |
| Main cost | The enterprise framing (strict workflow, review gates) is overhead for solo / fast iteration |
| GitHub repo | https://github.com/zgsm-ai/costrict |

## When To Pick It

- You are in an enterprise that needs **private deployment** — physical isolation and end-to-end encryption — rather than sending code to a hosted vendor.
- You want code generation to follow a **standardized pipeline** (requirements analysis, architecture design, task planning, test generation) instead of free-form prompting, so output is auditable and consistent across a team.
- You want **repository-wide AI code review** (RAG indexing + multi-model verification) wired into the same tool that writes the code, inside VS Code or JetBrains.

## When Not To Pick It

- You are a solo developer or want the fastest possible loop — the strict workflow and review gates are overhead a terminal CLI like [Aider](aider.md) or [Claude Code](claude-code.md) avoids.
- You want a terminal-native single-process agent — CoStrict is primarily an IDE extension; for the CLI field see the [terminal coding CLI comparison](../comparisons/coding-cli-agents.md).
- You already standardized on [Cline](cline.md) and do not need the enterprise control layer — the base lineage may be enough.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Strict / standardized generation | Very strong | The headline differentiator — req → architecture → tasks → tests |
| Repository-wide code review | Strong | RAG-indexed, multi-model verification, Git/SCM integrated |
| Private / isolated deployment | Strong | Physical isolation + E2E encryption; the enterprise selling point |
| Editor coverage | Strong | VS Code + JetBrains, plus a CLI and experimental cloud |
| Multi-provider support | Strong | Anthropic, OpenAI, OpenAI-compatible, and local models |
| Solo / fast-iteration fit | Weaker | The control layer is overhead outside a team setting |

## Operating Cost

Complexity is Medium. As an IDE extension it installs easily, but the value proposition — strict workflow, review gates, private deployment — is aimed at teams with process and infrastructure to match. A self-hosted, isolated deployment is real operational work; that is the point for the enterprises it targets, and the wrong trade for an individual.

## Bottom Line

CoStrict is the "enterprise control layer" entry in this map's coding-agent set: a Cline-lineage IDE agent that trades free-form speed for standardized, reviewable, privately-deployable AI development. If your blocker is governance — auditable generation, in-loop code review, on-prem isolation — it is a strong open-source option. If you want a fast personal loop, a terminal CLI ([Aider](aider.md), [Claude Code](claude-code.md), or the vendor CLIs compared [here](../comparisons/coding-cli-agents.md)) fits better; if you want the base editor-agent without the enterprise scaffolding, [Cline](cline.md) is the upstream.
