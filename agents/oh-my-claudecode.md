# oh-my-claudecode

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/oh-my-claudecode.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](oh-my-claudecode.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: oh-my-claudecode is best understood as a workflow and orchestration layer on top of Claude Code, not as a replacement for it.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Yeachan Heo and contributors |
| Route | Workflow / orchestration layer for Claude Code |
| Open source | Yes |
| Best for | Teams, reusable skills, persistent execution modes, and cross-provider advisory workflows inside Claude Code |
| Main cost | You still need Claude Code as the base surface, and the added workflow layer can be heavier than plain Claude Code |
| Official website | https://yeachan-heo.github.io/oh-my-claudecode-website |
| GitHub repo | https://github.com/Yeachan-Heo/oh-my-claudecode |

## When To Pick It

- You already like Claude Code and want stronger orchestration without switching to a different core agent.
- You want team workflows, reusable skills, persistent modes like Ralph or Autopilot, and optional provider cross-checks.
- You want notifications, observability, or OpenClaw-style gateway integration around Claude Code sessions.

## When Not To Pick It

- You do not use Claude Code and do not want to adopt it as your base surface.
- You want the lightest possible local coding loop with minimal extra ceremony.
- You want a fully managed cloud product rather than a local plugin and runtime layer.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Multi-agent orchestration | Very strong | Team mode is the center of the product story |
| Workflow reuse | Strong | Skills and guided execution modes are a major differentiator |
| Provider advisory | Strong | Codex and Gemini can be used as side advisors |
| Observability | Strong | HUD, logs, and callbacks make the runtime easier to inspect |
| Detached cloud execution | Medium | Better at orchestrating local and tmux-led flows than replacing managed cloud agents |

## Operating Cost

Complexity is Medium. Setup is fairly approachable, but the real cost is mental and operational: you are adding another layer of workflow, setup, and optional provider tooling on top of Claude Code. The public naming is also slightly messy because the repo and commands use oh-my-claudecode while the npm package is still published as `oh-my-claude-sisyphus`.

## Bottom Line

If Claude Code is already your base agent and you want more structure, delegation, and reusable operating patterns, oh-my-claudecode is one of the stronger workflow layers to evaluate.