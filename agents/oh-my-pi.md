# oh-my-pi

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/oh-my-pi.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](oh-my-pi.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: oh-my-pi (`omp`) is a terminal coding agent from Stencil Labs, forked from [Pi](pi.md) and filled in with the parts Pi leaves to extensions: LSP and debugger tools, subagents, an optional reviewer model, live session sharing and opt-in memory. It runs with no approval prompts by default (`yolo`), so set the approval mode before you point it at anything you care about.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Stencil Labs. The README says "Built by Stencil Labs"; the LICENSE lists Mario Zechner (2025), Can Bölük (2025-2026) and Stencil Labs, Inc. (2026) |
| Route | Direct execution (terminal coding agent) |
| Repository | [`can1357/oh-my-pi`](https://github.com/can1357/oh-my-pi): MIT, TypeScript with a Rust native core, 40,027 stars as of 2026-11-27 (repo created 2025-12-31) |
| Relation to Pi | A fork. The README says "Fork of Pi by @mariozechner" and links `badlogic/pi-mono`, which now redirects to `earendil-works/pi`, the repository behind this map's [Pi](pi.md) profile. GitHub does not mark the repo as a fork; it is a separate repository |
| Open source | Yes (MIT). Pull requests are "temporarily open to everyone" as a trial, and the README warns that "the vouch system may return" |
| Form factor | A CLI and TUI (`omp`), a one-shot mode (`omp -p`), a Node SDK, an RPC mode over stdio and an ACP server for editors; npm package `@oh-my-pi/pi-coding-agent` |
| Models and billing | Bring your own provider. The README lists API-key providers, `oauth` ("signs in with your provider account"), `plan` ("routes through a coding-plan subscription") and `local` servers with the key optional |
| Default model | No fixed default. At startup it takes `--model`, then a saved default, then "known provider defaults" among providers you have credentials for. The catalog at commit `e95d0dd` sets `claude-opus-5-5` for `anthropic`, `gpt-5.5` for `openai` and `openai-codex`, and `gemini-3.1-pro-preview` for `google`. `omp setup` has a default-model step |
| Best for | Developers who want a Pi-based terminal agent that already includes language servers, debuggers, subagents and a large provider list |
| Main cost | The default approval mode is `yolo`, which the settings table describes as "auto-approve all tiers", and there is no OS sandbox. Opening a repository also loads its extensions, hooks and MCP config "by design" |
| Docs | [omp.sh/docs](https://omp.sh/docs) · [repo docs](https://github.com/can1357/oh-my-pi/tree/main/docs) |

## What It Is

The README calls it "A coding agent with the IDE wired in." It also describes the project as "a fork of Pi by Mario Zechner, rewritten as a coding-first surface", and as "extended with a batteries-included coding workflow." The README counts "60+" providers and "31" built-in tools. Its own wording for the entry points is "Same engine, four wrappers": the TUI, `omp -p`, the Node SDK, and `omp --mode rpc` / `omp acp`.

Around the agent loop it puts:

- **Code intelligence**: an `lsp` tool for diagnostics, navigation, renames and code actions, and a `debug` tool that drives a DAP session (breakpoints, stepping, threads, variables).
- **Execution**: a `bash` tool backed by its own bash 5.3 engine with in-process coreutils, and an `eval` tool with "persistent Python and JavaScript cells" that can call back into the agent's tools.
- **Subagents**: the `task` tool fans work out to subagents. `task.maxConcurrency` "defaults to `32`". Isolated workspaces exist but `task.isolation.enabled` defaults to `false`, and tasks without `isolated: true` "share the parent checkout". **Agent Hub** (`Alt+A`) shows each subagent's activity and lets you steer or kill one.
- **Advisor**: a second model in the `advisor` role "reads every turn the main agent takes" and injects notes. `advisor.enabled` defaults to `false`, and the docs say an advisor "does not approve actions".
- **Collab**: `/collab` shares a live session through a relay. "Guests can prompt and interrupt the agent; the host machine runs the agent and all tools." The default relay is `wss://my.omp.sh`, and the docs say the production relay "is not currently distributed for self-hosting".
- **Memory**: five modes (`off`, `local`, `hindsight`, `mnemopi`, `sharpshooter`). "Memory is disabled by default."
- **Desktop and web**: a `browser` tool, a disabled-by-default `computer` API for the host desktop, and `web_search` across 25 listed backends.

## When To Pick It

- You want the agent to use language servers and real debuggers. `lsp` and `debug` are built in, not extensions.
- You want subagents in the box, with a hub to watch and steer them, and optional isolated workspaces per task.
- You want to switch providers freely. The README lists frontier APIs, coding-plan subscriptions and local servers (Ollama, LM Studio, llama.cpp, vLLM), plus custom OpenAI-compatible providers in `~/.omp/agent/models.yml`, per-role models and fallback chains.
- You want one agent for your terminal and your editor. `omp acp` speaks the Agent Client Protocol, and the README names Zed.
- Your repo already has `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.codex/` or `opencode.json`. The README says omp reads those project files, but "never reads another tool's `~/` config".
- You started on [Pi](pi.md) and want its base with these parts already added.

## When Not To Pick It

- **You expect a prompt before risky actions by default.** `tools.approvalMode` defaults to `yolo`. You can switch to `always-ask`, `always-ask-cached` or `write`, and `tools.restrictedFolders` forces a prompt "whatever the approval mode (`yolo` and `--auto-approve` included)". In `yolo`, a bare critical-command override in `bash` "is ignored".
- **You need isolation.** The docs say bash pattern rules are "not process or filesystem containment", that "Extensions are not sandboxed", and that `computer.run`'s read-only flag "is not a sandbox". Subagents share the parent checkout unless you enable isolation.
- **You open repositories you do not trust.** "Opening a repository loads its project inputs by design: settings, extensions, hooks, tools, commands, skills, rules, and project MCP configuration." Flags such as `--no-extensions` narrow this, but the README says they do so "without changing the repository-trust model."
- You want scheduled or background runs. The docs describe no cron or scheduler, and SDK, RPC and print sessions start no idle work unless the owner opts in.
- You want memory on from the first session. You have to pick a backend first.
- You want a small harness to read end to end. That is [Pi](pi.md)'s pitch; omp adds a Rust core the README sizes at "~80k" lines.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Very strong | LSP, DAP debugger, AST edit and search, browser, web search across 25 backends, MCP, extensions, skills |
| Code execution | Very strong | Built-in bash engine with in-process utilities, persistent Python and JavaScript `eval` cells that call back into tools |
| Multi-agent | Strong | `task` fan-out (32 concurrent by default), Agent Hub, `orchestrate` and `workflowz` keywords; isolation is opt-in |
| Delivery surfaces | Strong | TUI, one-shot, Node SDK, RPC, ACP for editors, browser guests through `/collab` |
| Human approval | Medium | Four approval modes, per-tool policies and restricted folders, but the default is `yolo` |
| Memory | Medium | Four backends (plus `off`) with retain, recall and learn tools, all off by default |
| Scheduling | Weak | No scheduler described in the docs |
| Governance | Medium | MIT, PRs open to everyone as a trial that may be withdrawn |

## Operating Cost

Low to start: `curl -fsSL https://omp.sh/install | sh`, `brew install can1357/tap/omp`, `bun install -g @oh-my-pi/pi-coding-agent`, Nix, PowerShell or mise. The README lists "macOS · Linux · Windows · bun ≥ 1.4.4". Then add a provider key or sign in with `/login`. State lives in `~/.omp`. The cost is in configuration. To get prompts you change the approval mode, to get separate checkouts per subagent you enable isolation, and to get memory you choose a backend. Releases are frequent: `v19.2.0` and `v19.2.1` both shipped on 2026-11-25. Collab sessions go through the hosted relay at `my.omp.sh`, which you cannot self-host today; the README says "Frames are sealed client-side; the relay never sees your keys."

## Relationship To The Rest Of This Map

omp sits on the direct-execution route with [Claude Code](claude-code.md) and [OpenCode](opencode.md): a terminal coding agent you run on your own machine. Its base is [Pi](pi.md), which this map files as an own-the-loop harness. The split follows each README. Pi's profile describes a core of read, write, edit and bash and says "The point is to leave orchestration to the caller", while omp says it adds "everything you're missing" and ships subagents, LSP, a debugger and memory as built-ins. omp also still exposes Pi-style building blocks (SDK, RPC, extensions), so if you want to own the loop, start from Pi; if you want those parts already wired in, start here. It also reads OpenCode's `opencode.json` and Claude Code's `.claude/` project files, which lowers the cost of trying it in an existing repo.

## Bottom Line

oh-my-pi fits developers who want a Pi-based coding agent with the IDE parts already inside: language servers, debuggers, subagents, a reviewer model and many providers. The defaults trust you and the repo: no approval prompts, no OS sandbox, subagents in the same checkout and project extensions loaded on open. Set `tools.approvalMode` and `tools.restrictedFolders` before you use it on code that matters.

## Sources

- [can1357/oh-my-pi README](https://github.com/can1357/oh-my-pi) · [LICENSE](https://github.com/can1357/oh-my-pi/blob/main/LICENSE) · [Releases (v19.2.1, Nov 25 2026)](https://github.com/can1357/oh-my-pi/releases) · [CHANGELOG](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/CHANGELOG.md) · [provider catalog defaults](https://github.com/can1357/oh-my-pi/tree/main/packages/catalog/src/compat/rules/providers) · [task settings](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/src/task/settings.ts)
- Docs: [Approval mode](https://github.com/can1357/oh-my-pi/blob/main/docs/approval-mode.md) · [Settings](https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md) · [Models](https://github.com/can1357/oh-my-pi/blob/main/docs/models.md) · [Memory](https://github.com/can1357/oh-my-pi/blob/main/docs/memory.md) · [Task tool](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md) · [Advisor](https://github.com/can1357/oh-my-pi/blob/main/docs/advisor-watchdog.md) · [Collab](https://github.com/can1357/oh-my-pi/blob/main/docs/collab.md) · [Extension loading](https://github.com/can1357/oh-my-pi/blob/main/docs/extension-loading.md) · [Computer use](https://github.com/can1357/oh-my-pi/blob/main/docs/computer-use.md) · [SDK](https://github.com/can1357/oh-my-pi/blob/main/docs/sdk.md) · [omp.sh](https://omp.sh)
