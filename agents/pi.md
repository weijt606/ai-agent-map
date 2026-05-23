# Pi

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/pi.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](pi.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Pi is a minimal, opinionated coding-agent harness — the agent loop, tools, and providers, with everything else left to extensions.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | earendil-works (acquired April 8 2026 from Mario Zechner / badlogic) |
| Route | Self-hostable terminal coding agent + agent toolkit |
| Open source | Yes (MIT, TypeScript) |
| Best for | Developers who want to keep the harness small and own the orchestration choices themselves |
| Main cost | You bring your own API keys, your own skills, and your own opinions about how to extend the agent |
| Official website | https://lefos.ai/ |
| GitHub repo | https://github.com/earendil-works/pi |

## When To Pick It

- You want a coding agent CLI that ships only the core loop (read, write, edit, bash) and lets you grow it with skills and extensions.
- You want broad LLM provider support — OpenAI, Anthropic, Google, vLLM pods — without lock-in to one vendor's surface.
- You want to publish your work sessions back to Hugging Face as open training data, which the project actively encourages.

## When Not To Pick It

- You want a turnkey product with bundled teams, dashboards, and managed background runs out of the box.
- You don't want to think about which extensions and skills to wire in.
- You need a polished editor surface; Pi is terminal-first.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Very strong | The CLI is the primary surface |
| Provider coverage | Very strong | Unified LLM API across OpenAI, Anthropic, Google, vLLM |
| Tool harness | Strong | Read, write, edit, bash by default; extend via skills, prompt templates, packages |
| Orchestration out of the box | Light by design | The point is to leave orchestration to the caller |
| Channels (Slack, web UI) | Available as toolkit packages | TUI, web UI, and Slack bot ship as separate packages |

## Operating Cost

Complexity is Medium. Installation is straightforward, but Pi assumes you will pick the model, wire in the skills, and decide how the agent extends itself. The "harness rebellion" framing is intentional: less bundled, more your call.

## Hacking Pi: A Customization Playbook

Pi is built to be opened up. The customization surface is four layers, ordered by how much code you write and how much you commit to. Start low, escalate only when the lower layer cannot express what you need.

| Layer | What it is | When to reach for it | Lives in |
| --- | --- | --- | --- |
| 1. Skills | Markdown + YAML frontmatter, anthropics/skills compatible | You want to teach the agent a workflow, idiom, or domain glossary without writing any code | `.pi/skills/`, `~/.pi/agent/skills/`, `~/.agents/skills/`, plus package `skills/` |
| 2. Prompt Templates | Reusable prompts that expand from slash commands | You keep retyping the same paragraph-long prompt | `.pi/prompts/`, `~/.pi/agent/prompts/` |
| 3. Extensions | TypeScript modules using `ExtensionAPI` — register tools, commands, lifecycle hooks, custom UI | You need real code: new tools, permission gates, integrations, side effects | `.pi/extensions/*.ts` or `.pi/extensions/<name>/index.ts` |
| 4. Packages | npm bundles of extensions + skills + prompts + themes | You want to share or version-pin a workflow across machines or with a team | Any npm package, picked up via `pi.skills` / `pi.extensions` in `package.json` |

### Layer 1 — Skills (start here)

A skill is one markdown file. Smallest example, at `.pi/skills/git-rebase-resolver/SKILL.md`:

```markdown
---
name: git-rebase-resolver
description: When a git rebase hits conflicts, drive the resolution interactively, one file at a time, always running tests after each resolution.
---

# Git Rebase Resolver

1. Read the conflicted files with `read`.
2. For each conflict marker, decide based on the surrounding semantic intent.
3. After resolution, run the project's pre-commit hook before `git add`.
4. Continue the rebase; do not squash without explicit user permission.
```

Pi auto-discovers it. The agent only loads full `SKILL.md` content when the description matches the task ("progressive disclosure"), so you can keep a large skill library without burning context. Skills are also triggerable explicitly via `/skill:git-rebase-resolver`.

Cross-harness tip: put skills in `~/.agents/skills/` and the same file works across Pi, Claude Code, and OpenAI Codex — no copying.

### Layer 2 — Prompt Templates

A prompt template turns `/<command>` into a fully expanded prompt. Use this when your customization is "I always start with the same paragraph" — not "I follow a workflow."

Example: `.pi/prompts/ship.md` becomes `/ship` and expands to whatever the file contains. Pass arguments: `/ship feature-X` makes `feature-X` available to the template.

Skill vs prompt template:
- **Prompt template** — static text expansion, you control the wording.
- **Skill** — workflow that the agent picks up by name when the task description matches.

### Layer 3 — Extensions (when you need real code)

This is where Pi becomes a harness you can rewrite. Extensions are TypeScript modules with a single default-exported factory:

```typescript
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  // Permission gate: block dangerous bash commands
  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName !== "bash") return;
    const cmd = event.input.command as string;
    if (/rm\s+-rf|sudo|curl .* \| sh/.test(cmd)) {
      const ok = await ctx.ui.confirm("Dangerous command", cmd.slice(0, 100));
      if (!ok) return { block: true, reason: "User denied" };
    }
  });

  // Custom tool: pull TODO list from a local tracker
  pi.registerTool({
    name: "list_my_todos",
    label: "List my TODOs",
    description: "Fetch the user's TODO list from the local tracker",
    parameters: Type.Object({ filter: Type.Optional(Type.String()) }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const todos = await loadFromLocalDb(params.filter);
      return {
        content: [{ type: "text", text: todos.join("\n") }],
        details: { count: todos.length },
      };
    },
  });

  // Slash command: start a fresh review session
  pi.registerCommand("review", {
    description: "Start a review session on the current diff",
    handler: async (_args, ctx) => {
      await ctx.newSession({ initialPrompt: "Review the staged diff..." });
    },
  });
}
```

Drop the file at `.pi/extensions/my-ext.ts` and Pi auto-discovers it. For extensions with dependencies, use the directory form `.pi/extensions/my-ext/{package.json, src/index.ts, node_modules/}`.

Key lifecycle events:

- Session: `session_start`, `session_before_switch`, `session_shutdown`
- Agent loop: `before_agent_start`, `input`, `turn_start`, `turn_end`
- Tools: `tool_call` (can block), `tool_result` (can rewrite)

Key UI primitives in `ctx.ui`: `confirm`, `select`, `input`, `notify`, `setStatus`, `setWidget`.

One-off testing: `pi -e ./my-ext.ts`.

### Layer 4 — Packages (share and pin)

Once your `.pi/` collection is doing real work, promote it to an npm package. A Pi package is a normal npm package with conventions:

```
my-pi-pack/
├── package.json   # add "pi.skills" / "pi.extensions" entries
├── skills/
│   ├── git-rebase-resolver/SKILL.md
│   └── ship/SKILL.md
├── prompts/
│   └── ship.md
├── extensions/
│   └── permissions.ts
└── themes/
    └── solarized.json
```

Install with `npm i @your-scope/my-pi-pack` — Pi picks up all four asset types automatically. This is how teams move from "Bob's machine has good skills" to "the team's skills are version-pinned in `package.json`."

## Composition Recipes

### Recipe A — Domain-specialized coding workflow

Make Pi excellent at one stack (FastAPI + SQLAlchemy + Alembic):

1. Skill `.pi/skills/alembic-migration/SKILL.md` — the migration workflow (create revision, dry-run, downgrade test, commit format).
2. Skill `.pi/skills/fastapi-route/SKILL.md` — route + dependency injection + test pairing convention.
3. Prompt template `.pi/prompts/feature.md` — expands `/feature` to "Add a new feature. Follow the alembic-migration and fastapi-route skills...".
4. Optional extension `db-snapshot.ts` — registers `snapshot_db` tool that the migration skill can call.

### Recipe B — Personal safety + telemetry harness

A locally-strict Pi that asks before dangerous ops and logs every tool call:

1. Extension `permissions.ts` — `tool_call` handler blocks rm / sudo / curl-pipe-sh without confirm.
2. Extension `telemetry.ts` — `tool_result` handler writes JSONL to `~/.pi/log/`.
3. Skill `incident-replay/SKILL.md` — references the JSONL log path so the agent knows where to look when reconstructing what happened.

### Recipe C — Team-shared workflow

One source of truth for "how the team uses Pi":

1. Build everything as a package: `@yourorg/pi-team-pack`.
2. Pin in each repo's `package.json`.
3. Run `npm install` — every contributor gets identical skills, prompts, extensions, theme.
4. Update centrally — `npm update` rolls out the new workflow to everyone.

## Anti-Patterns

- **Reaching for an extension when a skill would do.** If the customization is "tell the agent what to do," it is a skill, not TypeScript.
- **Hardcoding configuration in extensions.** Per Pi's own contributor rules, configuration belongs in a config surface, not in the code.
- **Skipping skills and writing huge prompt templates.** Skills compose better and only load on demand; prompt templates inflate every invocation.
- **Publishing a package before validating locally.** Always live with a workflow for a week in `.pi/` before promoting it to a package.

## Bottom Line

Pi sits in the same category as [Aider](aider.md) and [Claude Code](claude-code.md) — terminal-first coding agent — but stays smaller on purpose. The April 8 2026 acquisition by Earendil (now also building the Lefos cloud agent platform) put real funding behind a previously solo project. The reason to choose Pi over a heavier vendor product is the four-layer customization surface above — start with a `SKILL.md`, escalate to a prompt template, then an extension, then a package as your workflow stabilizes. If you only want to use someone else's agent, pick a vendor product. If you want to own your harness, this is the cleanest base to start from.
