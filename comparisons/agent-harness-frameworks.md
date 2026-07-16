# Agent Harness Frameworks

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/agent-harness-frameworks.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](agent-harness-frameworks.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

A "harness" is the minimal scaffolding around an LLM that turns it into an agent — the loop, the tool surface, the permission model, the skills hook. These are projects you can fork, audit, and own end-to-end, rather than vendor products you adopt as-is.

Current star totals for all five live in the [rankings boards](../rankings/README.md); this page compares shape, not size.

## At A Glance

| Project | License | Sweet spot | Footprint |
| --- | --- | --- | --- |
| [Pi](../agents/pi.md) | MIT (TS) | Terminal-first coding harness with broad LLM provider coverage | Small core + opt-in skills/extensions |
| [OpenHands](../agents/openhands.md) | Open source | Full open-source SWE agent (CLI + GUI + cloud option) | Heaviest — closer to a product |
| [SWE-agent](../agents/swe-agent.md) | MIT (Py) | Research reference behind SWE-bench, single-YAML config | Medium; upstream moving focus to mini-swe-agent |
| [mini-swe-agent](../agents/mini-swe-agent.md) | MIT (Py) | ~100-line successor; SWE-bench Verified >74% | Tiny — readable in one sitting |
| [OpenHarness](../agents/openharness.md) | MIT (Py) | 10-subsystem open harness with anthropics/skills + MCP + 43 tools | Medium; production-shaped, sibling to [CLI-Anything](../agents/cli-anything.md) |

## How To Choose

- Pick by footprint, not by stars. The right harness is the one whose surface area you are willing to maintain.
- If you want the smallest credible base to fork: [mini-swe-agent](../agents/mini-swe-agent.md).
- If you want a production-shaped open runtime to self-host: [OpenHarness](../agents/openharness.md).
- If you want to publish SWE-bench numbers: [SWE-agent](../agents/swe-agent.md) is the canonical reference; mini-swe-agent is the working successor.
- If you want a terminal-first day-to-day coding harness: [Pi](../agents/pi.md).
- If you want a more complete SWE agent product that is still open source: [OpenHands](../agents/openhands.md).
