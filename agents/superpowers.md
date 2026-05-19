# Superpowers

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/superpowers.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](superpowers.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Superpowers is a composable agentic skills framework plus a development methodology — it sits on top of existing coding agents and turns ad-hoc prompting into structured workflows.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Jesse Vincent and the Prime Radiant team |
| Route | Agentic skills framework / methodology layer |
| Open source | Yes (MIT, Shell + plugin packs) |
| Best for | Engineers who want a consistent skills layer across Claude Code, Codex, Cursor, Copilot, Gemini, and similar |
| Main cost | You inherit a methodology — the framework has opinions about brainstorm → design → plan → implement → review → complete |
| GitHub repo | https://github.com/obra/superpowers |

## When To Pick It

- You already use Claude Code, Codex, Cursor, GitHub Copilot, Gemini, OpenCode, or Factory Droid and want a shared skills layer across them.
- You want a methodology that enforces TDD, evidence-based verification, and complexity reduction — not just isolated skill files.
- You want to lean on a plugin marketplace integration rather than maintain your own `.claude/skills` directory by hand.

## When Not To Pick It

- You want a single end-to-end agent product; Superpowers does not run the agent itself, it only shapes how skills compose on top of one.
- You disagree with the imposed development cycle (brainstorm → design → plan → implement → review → complete) and prefer your own.
- You want a lightweight, minimal skill set — Superpowers is comprehensive on purpose, not minimal.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Skill composition | Very strong | Composable skills activate based on development stage |
| Cross-agent coverage | Very strong | Plugins for Claude Code, Codex, Cursor, GitHub Copilot, Gemini, OpenCode, Factory Droid |
| Methodology enforcement | Strong | Test-driven development and evidence-based verification are first-class concerns |
| Standalone runtime | Not the goal | Superpowers does not run agents — it shapes how an existing agent works |
| Plugin marketplace integration | Strong | Official plugin in Anthropic's marketplace |

## Operating Cost

Complexity is Medium. Installation is straightforward but you are adopting a methodology, not just a tool — the value depends on whether your team is willing to follow the stage-based workflow it enforces.

## Bottom Line

Superpowers is the most-starred project in the `.claude/skills` wave that hit GitHub trending in May 2026. Unlike a curated skills folder, it is a methodology with framework support and plugin integration into nearly every major coding agent. If you are choosing between bare Claude Code and Claude Code + Superpowers, the question is whether you want to inherit Jesse Vincent's opinions about TDD and verification, or grow your own. Both are valid; this profile exists because the opinionated framework end of the skills wave is now mature enough to compare against.
