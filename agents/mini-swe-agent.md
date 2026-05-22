# mini-swe-agent

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/mini-swe-agent.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](mini-swe-agent.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: mini-swe-agent is a deliberately tiny — about 100 lines of Python — coding agent that nonetheless scores >74% on SWE-bench Verified; it is the upstream team's own successor to [SWE-agent](swe-agent.md).

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Princeton + Stanford NLP (same team as [SWE-agent](swe-agent.md)) |
| Route | Agent harness framework — minimal reference |
| Open source | Yes (MIT, Python) |
| Best for | Anyone who wants the smallest credible harness — readable in one sitting, hackable in an afternoon |
| Main cost | "No huge configs, no giant monorepo" is the design — if you need polish or breadth, this is not the right project |
| GitHub repo | https://github.com/SWE-agent/mini-swe-agent |

## When To Pick It

- You want to read and understand the entire agent loop in a single session — the whole thing is ~100 lines of Python.
- You want a credible SWE-bench baseline: >74% on SWE-bench Verified is competitive with significantly heavier systems.
- You want the upstream-recommended successor to SWE-agent — the SWE-agent README itself points here for "current development effort."
- You want to fork-and-modify rather than configure — the value is that you can rewrite the whole thing in an afternoon.

## When Not To Pick It

- You want a production-ready CLI with rich tools, plugins, and skills — [OpenHarness](openharness.md), [Pi](pi.md), or [OpenHands](openhands.md) are heavier but more complete.
- You need a YAML-driven research config surface — that is still [SWE-agent](swe-agent.md)'s strength.
- You want to compose with anthropics/skills or MCP out of the box — mini-swe-agent is intentionally minimal.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Readability | Very strong | The entire agent loop is one short file |
| SWE-bench Verified score | Strong | >74% reported, competitive with much heavier systems |
| Fork-ability | Very strong | "Radically simple" is the design philosophy |
| Tool / skill ecosystem | Light by design | This is the point — you bring the rest |
| Long-term operability | Open question | New project (June 2025); upstream maintenance is healthy but young |

## Operating Cost

Complexity is Low. The whole codebase is small enough to audit. The cost is what is *not* there — no managed config layer, no tool plugin ecosystem, no UI. If you want production extras, you will write them yourself or pick a different harness.

## Bottom Line

mini-swe-agent is what the SWE-bench authors actually use day-to-day now. Compared to [SWE-agent](swe-agent.md) it trades configurability for radical simplicity, and the >74% SWE-bench Verified score makes the trade legitimate. If you want a harness you can fully understand before adopting, this is the cleanest path. If you want it to ship as a real CLI with permissions, MCP, skills, and a tool ecosystem, look at [OpenHarness](openharness.md) or [Pi](pi.md) instead.
