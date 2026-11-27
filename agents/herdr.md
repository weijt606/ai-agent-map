# herdr

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/herdr.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](herdr.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: herdr is a terminal workspace manager for coding agents, a single Rust binary that works like tmux but knows which pane holds an agent and whether that agent is working, blocked or idle. You run Claude Code, Codex, OpenCode, Pi and the rest inside it; herdr keeps their terminals alive in a background server, across SSH machines, and gives scripts and other agents a CLI and socket API to start, prompt and wait on them. It ships no agent and no model of its own.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | The `herdrdev` GitHub organization (herdr.dev). The LICENSE is the standard Apache 2.0 text and names no copyright holder; the top committer is `ogulcancelik` |
| Route | Workflow / orchestration layer, at the terminal level, across many CLI agents |
| Repository | [`herdrdev/herdr`](https://github.com/herdrdev/herdr): Apache-2.0, Rust, 53,195 stars as of 2026-11-27 (repo created 2026-03-27) |
| Open source | Yes (Apache-2.0). The README lists an enterprise / partnership contact; no hosted service is described |
| Form factor | "one rust binary, no electron": a background server plus terminal clients for Linux, macOS and Windows, a `herdr` CLI, a local socket API, plugins and an agent skill file |
| Agents | The [Agents](https://herdr.dev/docs/agents/) page lists 23 agents herdr supports (Claude Code, Codex, GitHub Copilot CLI, Cursor Agent CLI, OpenCode, Pi, Hermes Agent, Grok CLI, Gemini CLI, Cline and others) and five that report their state to herdr themselves. "Other agents still run normally in Herdr panes. They just show up as plain terminals." |
| Models and billing | None of its own. Each agent keeps its own model, sign-in and billing; herdr "doesn't wrap or replace them; it owns their terminals." |
| Default safety posture | No sandbox and no approval layer of its own: each agent keeps its own permission mode. herdr marks a pane `blocked` when it sees an approval or question UI, and `agent prompt` refuses to type into a blocked agent. Background version and detection-manifest checks to herdr.dev are on by default |
| Best for | A developer who already runs several terminal agents, often over SSH, and wants them in persistent panes with a status sidebar and a scriptable control surface |
| Main cost | A new multiplexer to learn and live in; the original processes do not survive a server or machine restart; latest stable release is v0.9.5 (Oct 14 2026) |

## What It Is

The README's tagline is "the runtime your coding agents live on." The docs are more literal: "Herdr is a terminal workspace manager. It keeps real terminal processes running and adds structure around them." Its building blocks are workspaces (one per repo or task), tabs, and panes, where "A pane is a real terminal." The server owns the panes; clients attach and detach, and `ctrl+b q` detaches without stopping anything.

On top of the multiplexer it adds the pieces that matter for agents:

- **Agent state.** herdr recognizes the agent in each pane and classifies it as `blocked`, `working`, `done`, `idle` or `unknown`, by reading the live bottom of the screen against detection manifests or by taking reports from an integration. State rolls up to tabs and workspaces in the sidebar, and notifications can fire when an agent finishes or needs input (popups are `off` by default).
- **Automation.** "agents drive herdr through the cli and socket api: they can spawn panes, prompt each other, and wait until another agent is genuinely blocked." `herdr agent start reviewer --kind codex`, `agent prompt … --wait` and `agent wait --until blocked` are the core verbs; `pane run` and `pane wait-output` cover ordinary processes such as tests and servers.
- **An agent skill.** `skills/herdr/SKILL.md` teaches a coding agent to use the herdr CLI from inside a pane, and tells it to stop if `HERDR_ENV=1` is not set.
- **Session restore.** After a server restart herdr restores the saved layout, and with an integration installed it relaunches supported agents into their own conversations (for example `claude --resume <id>`, `codex resume <id>`). Native agent session restore is on by default.
- **Several machines.** Saved SSH machines appear in one window "with a combined agent list and independent reconnects"; each keeps its own herdr server.
- **Git worktrees and plugins.** Workspace rows can create, open and remove Git worktree checkouts; plugins add actions, event hooks and panes from a manifest.

## When To Pick It

- You run several terminal agents at once and keep losing track of which one is waiting on you. The status sidebar and blocked detection are the main workflow: "start several agents, let them work in parallel, and use the sidebar to see which project needs a decision".
- You work on remote boxes over SSH and want agents to keep running when your connection drops. herdr "keeps terminals running in a background server when you close the client or lose your SSH connection."
- You want to check on agents from a phone without installing an app. "Herdr works on your phone without a mobile app or web dashboard": SSH in and run `herdr`, and the TUI adapts to narrow screens.
- You want one agent to hand work to another, or a script to drive agents, without adopting a framework. The CLI wrappers return JSON and `agent prompt --wait` blocks until the target settles.
- You already know tmux or zellij. The docs say "The prefix is `ctrl+b`, panes persist, detach and reattach work the way you expect", and mouse support is on by default.

## When Not To Pick It

- **You need herdr to enforce approvals or isolation.** herdr adds no sandbox and leaves permissions to each agent. Its own docs warn that unusual prompts "may initially show as `idle` instead of `blocked`", that automation trusting that state "can type into an approval dialog", and that "idle status is not authorization to approve an action." For a policy layer in front of agents, see [Omnigent](omnigent.md).
- You want a desktop app with diff review and a built-in browser. herdr runs in "whatever terminal you already use"; [Orca](orca.md) is the desktop workbench in this lane.
- You want a task graph, goals or budgets. herdr has panes, agents and waits, not tickets or a coordinator protocol; [Paperclip](paperclip.md) organizes agents as a company with tickets, budgets and approvals.
- You need running processes to survive a reboot. A server restart brings back the layout and, where supported, the agent conversation, but "Snapshot restore does not preserve running shells, servers, tests, or arbitrary processes." Live handoff on update is "experimental and opt-in".
- You do not want background calls home. `update.version_check` and `update.manifest_check` both default to `true`, and herdr "applies valid per-agent rule updates automatically"; set them to `false` if that matters.
- You only use one agent in one terminal. Run [Claude Code](claude-code.md), [Codex](codex.md) or [OpenCode](opencode.md) directly.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agent state awareness | Very strong | Per-pane `blocked` / `working` / `done` / `idle` / `unknown`, rolled up to tabs and workspaces; integrations can report state directly |
| Agent breadth | Very strong | 23 supported agents plus five that support herdr themselves; any other agent runs as a plain terminal |
| Scriptable control | Very strong | CLI with JSON output, socket API with a published schema and event subscriptions, an agent skill file |
| Persistence | Strong | Processes survive detach and lost SSH; after a restart the layout returns and supported agents resume their conversations, but processes do not |
| Multi-machine | Strong | Saved SSH machines in one window with independent reconnects; `--machine` routes CLI commands to a remote server |
| Delivery surfaces | Medium | TUI in your own terminal (including a phone SSH client), CLI and socket; no GUI, web or mobile app |
| Human approval | Weak | Detects and notifies on blocked agents; the approval itself stays in each agent's own UI |
| Memory | Weak | None of its own; session resume relies on each agent's native sessions |
| Scheduling | Weak | No scheduler; waits and plugins react to events |

## Operating Cost

Low to start: `curl -fsSL https://herdr.dev/install.sh | sh`, `brew install herdr`, `mise use -g herdr`, or a PowerShell installer on Windows, then run `herdr` where the work lives. Agents you already have installed are detected as they start. The cost is in what you install around it. Session resume needs an integration per agent (`herdr integration install claude` and so on), which writes hooks or extensions into that agent's own config. Plugins "run as your user, inherit your environment, and can call the full Herdr CLI", and herdr "does not review or sandbox plugin code". Pane screen history is off by default "because pane output can include secrets, tokens, prompts, and command output"; if you enable it, treat the session directory like terminal history. Remote setup uses your normal OpenSSH authentication and asks before installing herdr on a remote host or stopping a running server there; for stopping a server, the default answer is No.

## Relationship To The Rest Of This Map

herdr sits in the same lane as [Orca](orca.md): neither ships an agent, both run the CLI agents you already have side by side and track which one needs you. Orca does it as a desktop app built around git worktrees, with diff review, a browser and a phone companion; herdr does it as a terminal multiplexer, with persistent panes, SSH machines and a CLI/socket API that agents can drive. [Paperclip](paperclip.md) works a layer higher, giving agents roles, tickets, budgets, routines and approvals. [Ruflo](ruflo.md) builds swarms and memory on top of Claude Code; herdr adds neither memory nor a swarm model and stays agent-agnostic.

## Bottom Line

herdr is a good fit if your agents already live in terminals and the problem is keeping them alive, finding the one that is stuck, and letting scripts or other agents hand them work. It is open source, runs entirely on machines you control, and leaves models, billing and permissions to each agent. That last point cuts both ways: herdr tells you an agent is blocked, but it does not decide or enforce anything, so keep each agent's own approval settings where you want them.

## Sources

- [herdrdev/herdr README](https://github.com/herdrdev/herdr) · [LICENSE](https://github.com/herdrdev/herdr/blob/master/LICENSE) · [Releases (v0.9.5, Oct 14 2026)](https://github.com/herdrdev/herdr/releases) · [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) · [v0.9.5 docs source](https://github.com/herdrdev/herdr/tree/master/docs/versions/0.9.5/website/src/content/docs)
- Docs: [Concepts](https://herdr.dev/docs/concepts/) · [Agents](https://herdr.dev/docs/agents/) · [Agent automation](https://herdr.dev/docs/agent-automation/) · [Agent skill](https://herdr.dev/docs/agent-skill/) · [Session state](https://herdr.dev/docs/session-state/) · [Connecting machines](https://herdr.dev/docs/connecting-machines/) · [How to work](https://herdr.dev/docs/how-to-work/) · [Integrations](https://herdr.dev/docs/integrations/) · [Plugins](https://herdr.dev/docs/plugins/) · [Configuration](https://herdr.dev/docs/configuration/) · [Config reference](https://herdr.dev/docs/config-reference/) · [Socket API](https://herdr.dev/docs/socket-api/) · [Install](https://herdr.dev/docs/install/)
