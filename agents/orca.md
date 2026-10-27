# Orca

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/orca.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](orca.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Orca is an open-source desktop app for running several coding agents at once. You bring the CLI agents and subscriptions you already pay for (Claude Code, Codex, OpenCode, Pi, and any other CLI agent), and Orca gives each one its own git worktree, terminal and browser, then tracks them in one window and on a phone companion app. It does not ship an agent of its own. It is the workbench the agents run in.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Stably AI (`stablyai/orca`, onorca.dev; "Backed by Y Combinator"). The LICENSE file names Lovecast Inc. as copyright holder |
| Route | Workflow / orchestration layer, across many CLI agents rather than on top of one |
| Repository | [`stablyai/orca`](https://github.com/stablyai/orca): MIT, TypeScript, 107.8k stars as of 2026-10-28 |
| Open source | Yes (MIT). The desktop app, the mobile app, and the relay that pairs them are all in the repo |
| Form factor | Desktop app for macOS, Windows and Linux; iOS and Android companion app (beta); a headless `orca serve` runtime; an `orca` CLI |
| Agents | "Works with any CLI agent": the README lists over thirty, including Claude Code, Codex, Grok, Cursor, GitHub Copilot, Antigravity, OpenCode, Pi, Hermes Agent, Goose, Kimi, Qwen Code and DeepSeek Harness |
| Models and billing | Your own agent subscriptions or keys: "Plug in the subscriptions you already have and run them side by side." Account switching and Claude/Codex usage tracking are built in |
| Price | The site says "Free and open source". An Enterprise page offers rollout support with "contact us" pricing; no hosted plan is described, and the docs say Orca "does **not** sell managed VPS hosting" |
| Best for | A developer who already runs two or more coding agents and wants them in parallel worktrees, with review, a browser and phone alerts in one place |
| Main cost | One more app between you and your agents, shipping a release almost every day; orchestration, Cloud VM and remote servers are labelled experimental or beta |

## What It Is

Orca's README calls it "The AI Orchestrator for 100x builders" and the site calls it "The agent development environment". In practice it is an editor-shaped desktop app whose basic unit is the git worktree. You "fan one prompt across five agents, each in its own isolated git worktree", compare the results and merge the winner. Around that it puts the pieces you would otherwise keep in other windows:

- **Terminals** with WebGL rendering, splits, and scrollback that survives restarts.
- **Review**: a diff viewer where you can "drop comments on any diff line and ship them back to the agent", plus in-app GitHub PRs and issues and Linear and Jira items.
- **A per-worktree Chromium browser** with Design Mode, which sends a clicked element's HTML, CSS and a cropped screenshot into the agent's prompt.
- **A Monaco editor** with autosave, and drag-and-drop of files and images into prompts.
- **Notifications** that know when an agent has finished or is waiting on you.

## How It Runs Agents

Every worktree runs somewhere, and the [Ways to run Orca](https://www.onorca.dev/docs/ways-to-run) page lists four places:

| Mode | Where agents run |
| --- | --- |
| Local | Your desktop |
| SSH target | A host you reach over SSH; the editor and UI stay on your laptop |
| Remote Orca Server (beta) | A machine you control running Orca desktop or `orca serve`; laptop, web and phone clients pair to it, and agents keep running after your laptop sleeps |
| Cloud VM (experimental) | A disposable sandbox, VM or Docker container per worktree, booted from an `orca.yaml` recipe on your own provider account (the docs name Vercel Sandbox, Fly, Modal, SSH hosts and local Docker) |

Two features turn this from a window manager into an orchestration layer:

- **Orchestration** (experimental, off by default under Settings → Experimental): a coordinator agent opens a durable "Run", defines tasks with dependencies, dispatches them to worker agents in their own worktrees, and receives `worker_done`, heartbeat and question messages through an inbox. "Decision gates" hold a task until someone resolves it.
- **Scheduled automations**: the `orca` CLI creates automations with presets (`hourly`, `daily`, `weekdays`, `weekly`), cron expressions or RRULE strings, run in a chosen repo or worktree on this computer or a connected Orca host.

The **mobile companion** is a remote control, not an editor: it shows every worktree and agent status across connected hosts, lets you reply to an agent that is waiting, attach files, commit from source control, switch agent accounts, and get a push notification when an agent finishes. Phones reach the desktop through a relay; its source is in the repo's `cloud/` directory, while its deployment "is owned by the private `stablyai/orca-cloud` repository".

## When To Pick It

- You already use more than one CLI agent, or several sessions of one, and you are juggling terminals and branches by hand. Parallel worktrees and a single status view are the core of the product.
- You want to race agents against each other on the same task and keep the best result. The docs ship this as a recipe ("Race three agents on the same task").
- You want to leave agents running on a home server or VPS and check on them from your phone. The Remote Orca Server plus mobile companion covers this without building it yourself, on hardware you own.
- You pay for Claude or Codex subscriptions rather than API keys and want to use them as they are. Orca launches the vendors' own CLIs and tracks their usage and rate-limit resets.

## When Not To Pick It

- You use one agent in one terminal and are happy. Run [Claude Code](claude-code.md), [Codex](codex.md) or [OpenCode](opencode.md) directly.
- You want a policy layer that enforces approvals and spend limits across agents. Orca leaves permissions to each agent's own settings; [Omnigent](omnigent.md) puts approval and spend policies in front of every harness.
- You want to manage agents as a team with goals, budgets and an org chart rather than as worktrees. That is [Paperclip](paperclip.md).
- You need stable interfaces. Releases land most days (`v1.4.239` to `v1.4.242` shipped Oct 24 to Oct 27, 2026), and the multi-agent orchestration, Cloud VM and Remote Orca Server features carry experimental or beta labels.
- You want to stay inside your existing editor. Orca is a separate desktop app; for an agent inside the editor you already use, see [Cursor](cursor.md) or [Cline](cline.md).

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Parallel execution | Very strong | One worktree, terminal and browser per agent; local, SSH, remote server or per-worktree Cloud VM |
| Agent breadth | Very strong | Any CLI agent; over thirty named in the README |
| Delivery surfaces | Very strong | Desktop on three OSes, iOS/Android companion, web client to a remote server, and a CLI |
| Review | Strong | Diff annotations sent back to the agent, GitHub/Linear/Jira inside the app |
| Coordinated multi-agent | Medium | A coordinator/worker protocol exists but is experimental and off by default |
| Scheduling | Medium | Cron/RRULE automations from the CLI |
| Memory | Weak | Leaves `CLAUDE.md` and `AGENTS.md` to the agents; adds session restore and history, not memory |
| Governance | Weak | No cross-agent approval or budget policy; each agent keeps its own permission mode |

## Operating Cost

Low to start: download a desktop build or `brew install --cask stablyai/orca/orca` (the README warns that bare `orca` is an unrelated cask), then point it at agents you already have installed. The cost grows with the remote modes. A Remote Orca Server needs every agent CLI installed and signed in on the server, the docs recommend Tailscale between machines, and the pairing link "grants access to this Orca runtime" and should be treated "like a password". Orca collects anonymous usage telemetry, with an opt-out documented on its [privacy & telemetry page](https://www.onorca.dev/docs/telemetry).

## Bottom Line

Orca is a cockpit for agents you already have, not another agent. It covers the work that piles up once you run several agents at once: isolated worktrees, a status board, review, a browser, and a phone that tells you when something finished. All of it is MIT, and every remote mode runs on machines you own. Its multi-agent coordination is newer and still marked experimental, so pick Orca for running agents side by side today, not for a supervised agent team. For the same "many harnesses, one layer" idea with a policy engine, see [Omnigent](omnigent.md); for managing agents as an organization with goals and budgets, see [Paperclip](paperclip.md).

## Sources

- [stablyai/orca README](https://github.com/stablyai/orca) · [LICENSE](https://github.com/stablyai/orca/blob/main/LICENSE) · [Releases (v1.4.242, Oct 27 2026)](https://github.com/stablyai/orca/releases) · [Relay README (`cloud/`)](https://github.com/stablyai/orca/blob/main/cloud/README.md)
- [onorca.dev](https://www.onorca.dev) · [Enterprise](https://www.onorca.dev/enterprise) · Docs: [Ways to run Orca](https://www.onorca.dev/docs/ways-to-run) · [Remote Orca Servers](https://www.onorca.dev/docs/remote-servers) · [Orchestration](https://www.onorca.dev/docs/cli/orchestration) · [Scheduled automations](https://www.onorca.dev/docs/cli/automations) · [Mobile companion](https://www.onorca.dev/docs/mobile) · [Agent hooks & memory](https://www.onorca.dev/docs/agents/hooks-memory)
