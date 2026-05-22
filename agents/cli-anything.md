# CLI-Anything

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/cli-anything.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](cli-anything.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CLI-Anything is an HKUDS-built framework that auto-generates Click-based command-line interfaces for arbitrary software — its premise is "tomorrow's users will be agents," so it rewrites human-designed apps into agent-native CLIs.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | HKUDS (Hong Kong University Data Science group) |
| Route | Runtime and tools — agent-native software bridge |
| Open source | Yes (Apache-2.0) |
| Best for | Teams who need agents to control software without exposed APIs — creative tools, office suites, scientific apps |
| Main cost | Generated CLIs need ongoing maintenance as upstream apps evolve; the pipeline is novel and still maturing |
| GitHub repo | https://github.com/HKUDS/CLI-Anything |

## When To Pick It

- You need an agent to drive software like Blender, GIMP, LibreOffice, QGIS, FreeCAD, ComfyUI, or Calibre, and you don't want to script GUI automation.
- You prefer structured CLI control (JSON output, `--help` introspection, REPL mode) over brittle screen-scraping.
- You are willing to run a 7-phase pipeline (analyze → design → implement → test → document → publish) over a target application.
- You want each generated CLI to ship as a real PyPI package with SKILL.md documentation an agent can read.

## When Not To Pick It

- The software you want agents to drive already has a solid API or CLI — use that directly.
- The value is in visual interaction, not state changes (real-time games, video editing, animation timelines).
- You want a polished, production-hardened product. CLI-Anything is academic-group infrastructure with strong test coverage (2,330+ tests across 18+ apps) but is still maturing.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| CLI auto-generation | Very strong | 7-phase pipeline, Click-based outputs with REPL and JSON output modes |
| Coverage breadth | Strong | 18+ professional applications already generated |
| Agent surface | Strong | `--help` introspection, `--json` output, structured errors, SKILL.md docs |
| Maintenance over time | Open question | Generated CLIs need re-validation as upstream apps evolve |
| Productionization | Medium | Apache-2.0 with HKUDS academic ownership rather than a vendor |

## Operating Cost

Complexity is Medium to High. You run the pipeline once per target application, but each generated CLI is its own artifact you maintain forward. The trade is well-suited to "I need agents to drive this complex desktop application reliably" and over-engineered for "I need to call this REST API."

## Bottom Line

CLI-Anything inverts the usual framing — instead of teaching agents to click on GUIs, it rewrites software so agents never need to click. The 18+ generated CLIs (creative, office, scientific, AI/ML tools) make this more than a thought experiment, and the Click + REPL + JSON output combination is a clean agent surface. The right test is whether the pipeline produces a maintainable CLI for one of your own target applications — if so, the trade against GUI automation tilts strongly toward CLI-Anything.
