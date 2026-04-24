# Open Interpreter

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/open-interpreter.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](open-interpreter.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Open Interpreter lets LLMs execute code directly on your machine through natural language — an open-source, local alternative to ChatGPT's Code Interpreter with no sandbox restrictions.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Killian Lucas / Open Interpreter org |
| Route | Local code execution via natural language |
| Open source | Yes, MIT |
| Best for | Developers who want LLMs to run Python, JS, and Shell directly on their machine with no file-size or time restrictions |
| Main cost | Code runs unsandboxed on your real machine — every command is a real operation |
| Official website | https://www.openinterpreter.com |
| GitHub repo | https://github.com/openinterpreter/open-interpreter |

## When To Pick It

- You want to tell an LLM what to do and have it execute code directly on your computer.
- You need file manipulation — create/edit photos, videos, PDFs, spreadsheets.
- You want browser and computer control (OS mode with Anthropic computer-use support).
- You want full internet access and no file-size or time restrictions.
- You want to use cloud models (GPT-4, Claude) or local models (Llama, etc.).

## When Not To Pick It

- You are uncomfortable with unsandboxed code execution on your machine. Every command runs for real.
- You need enterprise SLA or support.
- You want a coding-focused agent with git integration, PR workflows, and project context. Look at Claude Code or Aider.
- You need multi-agent orchestration or team workflows.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Code execution | Very strong | Python, JS, Shell — directly on your machine |
| File manipulation | Strong | Create and edit files, images, videos, PDFs |
| Computer control | Medium | OS mode with Anthropic computer-use |
| Model flexibility | Strong | Cloud and local models supported |
| Safety / sandboxing | Weak | No built-in sandbox — runs on your real machine |
| Git / project context | Weak | Not designed for repo-aware coding workflows |

## Operating Cost

Complexity is Low to Medium. Install with pip, point at a model, and start talking. The LLM API cost is the primary expense. The real cost is risk management — you are giving an LLM the ability to execute arbitrary code on your machine without sandboxing.

## Bottom Line

Open Interpreter is the most direct path from natural language to code execution on your own machine. The power is real; the risk is also real. Treat it as a sharp tool, not a safe one.
