# T3 Code

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/t3-code.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](t3-code.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: T3 Code is an open-source control plane for the coding agents you already have installed. A server on your machine drives Claude Code, Codex and eight other named agents (plus any ACP agent), and desktop, web and phone clients all show the same threads. It does not ship an agent of its own; its FAQ says plainly that T3 Code is not a harness.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | T3 Tools, Inc. (GitHub org `pingdotgg`; site [t3.codes](https://t3.codes)). The LICENSE names "T3 Tools Inc." as copyright holder |
| Route | Workflow / orchestration layer, across many coding agents rather than on top of one |
| Repository | [`pingdotgg/t3code`](https://github.com/pingdotgg/t3code): MIT, TypeScript, 81,794 stars as of 2026-11-27 (repo created 2026-02-08) |
| Open source | Yes (MIT), but the README says the license "applies **only to the source code**"; forks must use their own branding. Contributions: "Small, focused fixes are the most likely to be merged. Features need an approved discussion first." |
| Form factor | Desktop app for macOS, Windows and Linux; a `t3` CLI that starts the server and opens a web app; the hosted web client at `app.t3.codes`; iOS and Android apps |
| Agents | Claude Code, Codex, Cursor, OpenCode, Grok Build, Antigravity, Kiro, Pi, Muse Code, fx, "and any [ACP](https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-acp.md) agent" (GitHub Copilot is added through the ACP Registry) |
| Models and billing | Your own subscriptions or keys: "T3 Code does not resell tokens." The FAQ answers "How much does T3 Code cost?" with "Nothing. You pay your own model/agent providers." Extra provider instances can use an API key or OpenRouter |
| Default model | T3 Code picks none of its own; it uses whatever the provider CLI is signed in to. In the source, Codex and Claude are the provider instances enabled by default and the other eight drivers start disabled; new threads then reuse "your last provider, model, and options". Background text tasks (titles, commits, PR text) default to the Codex instance with `gpt-6-luna` at low reasoning effort |
| Default safety posture | New threads default to **Full access** ("Runs commands and edits without approval prompts"; `DEFAULT_RUNTIME_MODE = "full-access"` in source). SECURITY.md: an environment "is not a sandbox", and a full-scope session "equals a shell as the server's OS user" and "is the default grant". New background services "bind to localhost only" |
| Best for | A developer who runs Claude Code, Codex or both and wants parallel worktree threads, cross-agent delegation and phone approvals from one interface, on machines they own |
| Main cost | The out-of-the-box mode is no-prompt, so approvals are something you turn on; the host must stay awake; releases are pre-1.0 and frequent, and several features (workflows, linked environments, guest links) sit under Labs |
| Docs | [User guide](https://github.com/pingdotgg/t3code/blob/main/docs/user/README.md) · [all docs](https://github.com/pingdotgg/t3code/blob/main/docs/README.md) (in the repo) |

## What It Is

The README opens with: *"The open-source control plane for coding agents."* and *"T3 Code runs the coding agents on your machine and gives them one fast interface. Start a thread at your desk, then approve the next step from your phone."* The user guide splits it into a host and clients: "A T3 Code **server** runs on the machine that holds your code and provider CLIs (your laptop, desktop, workstation, or VPS). Your desktop app, browser, and phone are **clients** connected to one or more environments."

The FAQ draws the line against harnesses: "A harness turns an LLM into an agent (tools, execution loop, and results)—like Claude Code's Agent SDK or Codex App Server. T3 Code drives those harnesses through one fast interface; it does not work without at least one installed agent."

Around that it puts:

- **Threads and worktrees**: each task is a thread; **New worktree** gives it "an isolated Git branch and working directory so multiple agents can work in parallel". `Shift`-clicking several models in a new thread "starts a separate thread and worktree for each model."
- **Cross-agent work**: "Change models in the middle of a thread. Let Claude hand a task to Codex." An agent can call `delegate_task` to start a subagent on another provider or model, in an isolated worktree, or on a linked machine.
- **Review and source control**: turn, uncommitted, branch and commit diffs; inline review comments that are sent to the agent in one message; one-button commit, push and pull request. The source-control guide lists GitHub, GitLab, Forgejo/Gitea, Bitbucket, Azure DevOps, GitCafe, Cursor Origin, and Linear and Jira issues.
- **Workspace tools**: integrated terminals, a built-in browser with an element picker, iOS Simulators and Android Emulators in a Devices panel, and voice input.
- **Automation**: scheduled tasks and webhook-triggered tasks, plus **Workflows** (Labs), described as "durable TypeScript scripts that chain agents, code steps, schedules, webhooks, issue/PR triggers, and human approvals into multi-stage runs that survive server restarts."
- **An MCP endpoint for outside agents**: Claude Code, Codex, ChatGPT or "any OAuth-capable MCP client" can read projects and threads, and with a Supervised-or-higher grant launch, message and stop threads.

## When To Pick It

- You already use Claude Code or Codex (or both) on a subscription and want them in one place. The README: "It drives the agents you are already signed in to."
- You want to steer agents from your phone. The FAQ lists "Approve steps, review PRs, and steer threads from iOS and Android", and remote access works over T3 Connect, LAN, Tailscale or desktop-managed SSH.
- You want one agent to hand work to another. `delegate_task` can pick another provider or model, and "A delegated subagent can never exceed its parent thread's permission mode."
- You run agents on a home server or VPS. `t3 service install` runs it as a background user service on Linux, macOS or Windows, and load balancing can spread new threads across connected machines.
- You need an admin to set limits. A managed policy can "set defaults, lock settings, and restrict capabilities (such as maximum permission mode, allowed providers, or remote access)" for every user on a machine.

## When Not To Pick It

- **You expect it to ask before acting by default.** The default for new threads is **Full access**. You can switch to **Supervised**, **Auto-accept edits** or **Auto**, but how each mode is enforced depends on the provider: "Providers enforce permissions differently, and some read-only actions proceed even in **Supervised**". Muse Code and Kiro offer only Supervised and Full access.
- You want an isolation boundary. SECURITY.md says an environment "is not a sandbox: it intentionally runs agents and terminals with that user's privileges."
- You want local models. The FAQ: "Does T3 Code support local models? No. T3 Code focuses on frontier coding agents." Local OpenAI-compatible endpoints are only for lightweight text generation such as thread titles.
- Your host sleeps. "If the host machine sleeps or shuts down, agents pause until it wakes", and workflow runs "only advance while the server that started them is online."
- You need a memory layer. T3 Code keeps threads, imports recent Claude Code, Codex and Pi conversations, and carries context across provider switches, but memory stays with each agent; rewind "cannot undo external actions or separate provider memory."
- You need stable interfaces. Six stable releases shipped between v0.1.8 (2026-11-09) and v0.1.13 (2026-11-26), with nightlies in between; v0.1.13 alone lists "401 changes from 52 contributors".
- You want one agent in one terminal. Run [Claude Code](claude-code.md), [Codex](codex.md) or [OpenCode](opencode.md) directly.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Parallel execution | Very strong | A thread per task, optional worktree per thread, one-prompt-many-models runs, local, SSH or linked hosts |
| Agent breadth | Strong | Ten named providers plus the ACP Registry; each needs its own install and sign-in on the host |
| Delivery surfaces | Very strong | Desktop on three OSes, `t3` CLI with a web app, `app.t3.codes`, iOS and Android, and an MCP endpoint |
| Coordinated multi-agent | Strong | `delegate_task` across providers, worktrees and linked machines; durable multi-stage workflows are Labs |
| Review | Strong | Turn and branch diffs, inline review comments sent to the agent, one-button PRs, many source-control hosts |
| Scheduling | Strong | Scheduled and webhook tasks in Settings; workflow schedules and issue/PR triggers (Labs); host must stay online |
| Human approval | Medium | Four permission modes, approvals from the phone, push-hook prompts below Full access, workflow `ask`; but Full access is the default and enforcement varies by provider |
| Memory | Weak | Threads, session import and context handoff; no memory layer of its own |
| Governance | Medium | MIT, managed policy, scoped tokens and device approval; trademark limits on forks and a narrow contribution policy |

## Operating Cost

Low to start: download the desktop app, `brew install --cask t3-code`, or `curl -fsSL https://t3.codes/install.sh | sh` and run `t3`. The other requirement is one agent "installed and signed in" on the same machine, for example `claude auth login` or `codex login`. The cost grows with remote use. New background services listen on localhost; `t3 up --lan` opens LAN and Tailscale addresses, where "Anyone on that network can reach the port (gated by pairing)". With T3 Connect, "By default, any device signed into your T3 Connect account can connect" until you turn on **Require approval for new devices**, and the docs say to "Treat pairing URLs and codes as passwords". A free T3 Connect account links up to 3 host machines, and a paid T3 Chat account raises that limit. Code and prompts "go directly from your machine to your chosen provider"; T3 Connect traffic runs over a Cloudflare tunnel, and T3's relay "coordinates the link without proxying your HTTP/WebSocket sessions". Product usage events (provider, model, token totals, no prompts or file contents) are on until you set `T3CODE_TELEMETRY_ENABLED=false` or `DO_NOT_TRACK=1`.

## Relationship To The Rest Of This Map

T3 Code sits in the same lane as [Orca](orca.md): an MIT desktop app plus phone companion that runs the CLI agents you already pay for in parallel worktrees, and ships no agent of its own. Orca's profile describes it as an editor-shaped workbench whose coordinator/worker orchestration is experimental and off by default; T3 Code is a client/server control plane where agent-to-agent delegation is documented as a normal feature and the durable workflow engine is the Labs piece. On approvals the two differ in kind: Orca leaves permissions to each agent's own settings, while T3 Code sets a permission mode per thread and maps it onto each provider, with Full access as the default. For managing agents as an organization with goals, budgets and an audit log, see [Paperclip](paperclip.md); for approval and spend policies in front of every harness, see [Omnigent](omnigent.md).

## Bottom Line

T3 Code is a good fit if you already run Claude Code or Codex and want one fast interface for parallel threads, cross-agent hand-offs, review, and approvals from your phone, on hardware you own. It is not an agent, not a sandbox, and not a memory layer. The defaults favour speed: new threads run in Full access and a full-scope client equals a shell on the host. Set the default permission mode, turn on new-device approval, and consider a managed policy before you point it at anything important.

## Sources

- [pingdotgg/t3code README](https://github.com/pingdotgg/t3code) · [LICENSE](https://github.com/pingdotgg/t3code/blob/main/LICENSE) · [SECURITY.md](https://github.com/pingdotgg/t3code/blob/main/SECURITY.md) · [Releases (v0.1.13, 2026-11-26)](https://github.com/pingdotgg/t3code/releases) · [t3.codes](https://t3.codes)
- Source defaults: [`providerPolicy.ts`](https://github.com/pingdotgg/t3code/blob/main/packages/contracts/src/providerPolicy.ts) · [`settings.ts`](https://github.com/pingdotgg/t3code/blob/main/packages/contracts/src/settings.ts) · [`model.ts`](https://github.com/pingdotgg/t3code/blob/main/packages/contracts/src/model.ts)
- Docs: [User guide](https://github.com/pingdotgg/t3code/blob/main/docs/user/README.md) · [FAQ](https://github.com/pingdotgg/t3code/blob/main/docs/user/faq.md) · [Install](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md) · [Permission modes](https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md) · [Remote access](https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md) · [Subagents](https://github.com/pingdotgg/t3code/blob/main/docs/user/subagents.md) · [Workflows](https://github.com/pingdotgg/t3code/blob/main/docs/user/workflows.md) · [Project settings](https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md) · [Outside agents](https://github.com/pingdotgg/t3code/blob/main/docs/user/outside-agents.md) · [Managed policy](https://github.com/pingdotgg/t3code/blob/main/docs/user/managed-policy.md) · [Background service](https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md) · [Composer](https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md) · [Diffs](https://github.com/pingdotgg/t3code/blob/main/docs/user/diffs.md) · [Telemetry](https://github.com/pingdotgg/t3code/blob/main/docs/user/telemetry.md)
