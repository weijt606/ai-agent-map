# Agent Skills

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/agent-skills.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](agent-skills.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

A skill is a folder of instructions, and sometimes scripts, that an agent loads when a task calls for it. Since the [`.claude/skills` wave](../market-events.md#may-2026-ongoing--the-claudeskills-wave) began in May, skill collections have been among the most-starred repositories this map tracks. This map does not profile curated collections, because they are content assets, not agent surfaces. This page is where they are compared. It covers what a skill is, which agents load one, the five largest collections and frameworks, and what to check before you install someone else's.

> **Last reviewed:** 2026-11-01 · Every fact below comes from the vendor's own docs, the repository's own README and files, or the maintainer's own site. Star counts are this map's 2026-10-28 snapshot. Numbers a vendor reports about itself are labelled as such.

## What A Skill Is

The open specification at [agentskills.io](https://agentskills.io) defines a skill as "a folder containing a `SKILL.md` file". That file holds metadata (`name` and `description`, at minimum) and instructions. A skill can also bundle `scripts/`, `references/`, `assets/` and other files.

```
my-skill/
├── SKILL.md      # required: name + description, then instructions
├── scripts/      # optional: code the agent can run
├── references/   # optional: docs it reads when needed
└── assets/       # optional: templates, resources
```

Skills load in stages, which the spec and Anthropic's docs both call **progressive disclosure**. Anthropic's docs give the cost of each stage:

| Stage | When it loads | Context cost (Anthropic's docs) |
| --- | --- | --- |
| Metadata (`name`, `description`) | Always, at startup | ~100 tokens per skill |
| `SKILL.md` body | When a request matches the description | Under 5k tokens |
| Bundled files and scripts | Only when the instructions reference them | None until read; a script's code never enters context, only its output |

So the `description` decides when a skill fires. Anthropic's docs say it "must say both what the Skill does and when to use it."

**How a skill differs from the things it is confused with**, each in its owner's words:

- **A prompt** is "conversation-level instructions for one-off tasks"; skills "load on demand, so you don't have to repeat the same guidance across conversations" (Anthropic docs). Custom instructions "apply broadly to all your conversations"; skills are "task-specific and only load when relevant" (Claude Help Center).
- **MCP** "is an open-source standard for connecting AI applications to external systems" (modelcontextprotocol.io). The Claude Help Center separates the two: MCP connects Claude to services and data, and a skill holds the procedure. The two can be combined, so that Claude knows how to use the tools MCP provides.
- **A plugin** is, in Claude Code, "a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit". A skill is one thing a plugin can carry. Most of the collections below ship as plugins.
- **A Claude Project** gives "static background knowledge that's always loaded"; skills "activate dynamically when needed" (Claude Help Center).

## Where Skills Run

Only agents whose own docs document Agent Skills support are listed. The pre-built document skills (Word, Excel, PowerPoint, PDF) are an Anthropic product feature, not part of the standard. Anthropic's docs list them for claude.ai and the Claude API, and say they are not available in Claude Code.

| Agent | Where you put a skill | How it is used | Notes from its docs |
| --- | --- | --- | --- |
| **Claude apps** (claude.ai) | Customize → Skills → "+" → Upload a skill (a ZIP of the folder) | Claude picks it when relevant; toggle each skill on or off | Needs code execution turned on. Custom skills are per user, not org-wide |
| **[Claude Code](../agents/claude-code.md)** | `~/.claude/skills/<name>/SKILL.md` (personal), `.claude/skills/<name>/SKILL.md` (project), or inside a plugin | Automatic, or type `/skill-name` | Custom commands "have been merged into skills" |
| **Claude Agent SDK** | `.claude/skills/` and `~/.claude/skills/`, loaded via `settingSources` | Model-invoked, or send `/<name>`; scope with the `skills` option | No programmatic registration; skills are files on disk |
| **Claude API / Managed Agents** | Upload via `/v1/skills`, or use the pre-built `pptx` / `xlsx` / `docx` / `pdf` | List `skill_ids` in the `container` parameter with the code execution tool | Runs in a sandbox with no network access |
| **[Codex](../agents/codex.md) and ChatGPT** | `.agents/skills/` (repo), `~/.agents/skills/` (user); `$skill-installer` adds curated ones | Automatic, or `$` / `/skills` in Codex, `@` in ChatGPT | Standalone skills are in the ChatGPT desktop app, Codex CLI and IDE extension; plugin-bundled skills also on web and mobile |
| **[Cursor](../agents/cursor.md)** | `.agents/skills/`, `.cursor/skills/` (and `~/` equivalents); also reads `.claude/skills/` | Automatic, or `/` in Agent chat | Skills from a GitHub repo come in as a plugin |
| **[GitHub Copilot](../agents/github-copilot.md) in VS Code** | `.github/skills/`, `~/.copilot/skills/`; also lists `.claude/skills/` and `.agents/skills/` | Loaded when a skill applies; `/skills` in chat | Docs say to reuse only trusted skills |
| **[Gemini CLI](../agents/gemini-cli.md)** | `.gemini/skills/` or `.agents/skills/` (and `~/` equivalents); `gemini skills install <git url>` | Gemini calls `activate_skill`; you approve a consent prompt | Unpaid and Google One users were moved to Antigravity CLI on 2026-06-18 |
| **[OpenCode](../agents/opencode.md)** | `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` (and global equivalents) | Loaded on demand by the built-in `skill` tool | Each skill can be set to allow, deny or ask in `opencode.json` |

Two things follow from the table. First, `.agents/skills/` is the folder most of these agents share: Codex, Cursor, Copilot in VS Code, Gemini CLI and OpenCode all read it, Claude Code's docs do not list it, and Claude Code, the Agent SDK, Cursor, Copilot in VS Code and OpenCode read `.claude/skills/`. Second, custom skills do not sync across Claude's own surfaces. A skill uploaded to claude.ai must be uploaded again to the API, and Claude Code keeps its own copy on disk.

One inconsistency in Anthropic's own pages: the Help Center lists skills on Free, Pro, Max, Ultra, Team and Enterprise plans, while the platform docs list custom-skill upload on Pro and above. Check your plan's settings page.

## The Standard Now Belongs To A Foundation

On **2026-10-22** Anthropic [donated Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) (AAIF). AAIF is a Linux Foundation project that Anthropic co-founded with Block and OpenAI, and the donation includes the agentskills.io domain. Anthropic says "more than 70 agent platforms, including ChatGPT, Cursor, GitHub Copilot, and VS Code," have integrated the standard, and that "1 million skills have been published and nearly 280 million installed." Those are Anthropic's own figures; this map has no independent count, and the announcement names only those four platforms. In practice nothing changes for a skill author today: the format is the same, and only its home has moved. The event is recorded in [market events](../market-events.md).

## The Collections Compared

Ordered by stars as of 2026-10-28. "Skills" counts the `SKILL.md` files in each repository on 2026-11-01, except for ECC, whose own folder tree holds translated copies, so its README figure is used.

| Project | Kind | What it changes for you | Skills | Agents its README covers | Footprint | Maintainer | License | Stars (2026-10-28) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Superpowers](../agents/superpowers.md) | Framework + methodology | A mandatory workflow that triggers on its own: brainstorming → git worktree → plan → subagent or inline execution → TDD → code review → finish the branch | 15 | 16 install targets, incl. Claude Code, Codex app and CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenCode, Antigravity, Kimi Code, Qwen Code, Pi, Hermes Agent | One plugin per harness; a session-start bootstrap | Jesse Vincent and Prime Radiant | MIT | 306.1k |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Personal collection | Small skills you call or the agent picks: `/grill-me`, `/tdd`, `/to-spec`, `/diagnosing-bugs` and so on, split into user-invoked and model-invoked | 39 (27 in the documented engineering and productivity sets) | Claude Code, Codex, GitHub Copilot (CLI and VS Code), Gemini CLI; others via `npx skills` | Plugin (self-updating) or editable copies, not both | Matt Pocock | MIT | 304.7k |
| [ECC](../agents/ecc.md) | Framework + runtime layer | A whole engineering system: subagents, hooks that gate commands, a local memory vault, the AgentShield config scanner | 314 skills, 71 agents (README) | Claude Code stable; Codex and Qoder native; Cursor, OpenCode, Copilot CLI beta; others experimental | Large; README recommends `--profile minimal` when context matters | Affaan Mustafa ("a single maintainer", per its README) | MIT (hosted Pro tier is paid) | 290.6k¹ |
| [anthropics/skills](https://github.com/anthropics/skills) | Official reference examples | Shows the pattern: creative and design, development, enterprise communication, and the document skills behind Claude's file creation | 20 (incl. a template) | Claude Code (plugin marketplace), claude.ai, Claude API | Pick individual plugins (`document-skills`, `example-skills`) | Anthropic | Many Apache-2.0; `docx` / `pdf` / `pptx` / `xlsx` are source-available, not open source | 184.2k |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Collection organised as a lifecycle | Nine commands from `/spec` to `/ship` (define → plan → build → verify → review → ship), with skills that activate on their own | 25 | Claude Code (recommended), Codex, Cursor, Antigravity CLI, Gemini CLI, OpenCode, GitHub Copilot, Windsurf, Kiro, Command Code | Whole pack or one skill at a time via `npx skills` | Addy Osmani | MIT | 111.0k |

¹ ECC is not in this map's star snapshot. Its figure is the one recorded in [its profile](../agents/ecc.md) for 2026-10-28.

Who the maintainers are, as each describes himself: **Matt Pocock** is "an educator, content creator and engineer" who teaches AI engineering full-time and runs Total TypeScript. **Addy Osmani**'s site says he is "a Member of Technical Staff at Anthropic" who works on Claude Code, after 14+ years at Google, most recently as a Director at Google Cloud AI. **Jesse Vincent** builds Superpowers with Prime Radiant, which offers commercial support. **Affaan Mustafa** is ECC's single maintainer, per its README.

On reading the table: Superpowers and ECC change *how your agent works*, and you adopt their process. mattpocock/skills and addyosmani/agent-skills are libraries you can take one skill at a time. anthropics/skills says of itself that its skills are "for demonstration and educational purposes only". Read it to learn the format, not as a product.

For domain collections (research, finance, methodology) see the [skill verticals](../rankings/skill-verticals.md) boards.

## Before You Install Someone Else's Skill

1. **A skill can run code.** Anthropic's docs: "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic," and if you must use one from an unknown source, "thoroughly audit it before use", meaning `SKILL.md`, scripts, images and other bundled files, looking for unexpected network calls or file access. They also say "treat like installing software." Claude Code adds two specifics. A project skill's `allowed-tools` applies even in a folder you have never trusted, so review skills checked into a repository. And `` !`command` `` lines run shell commands before Claude sees the skill; `"disableSkillShellExecution": true` turns that off. VS Code's docs give the same advice to reuse only trusted skills. Gemini CLI asks for consent before it activates a skill, and OpenCode can set a skill to "ask".
2. **Skills cost context even when idle.** Each installed skill's description sits in context on every turn: about 100 tokens per skill per Anthropic's docs, with Claude Code truncating each listing at 1,536 characters. A plugin's skills and agents add theirs "even in sessions where nothing from the plugin runs". Claude Code's official marketplace shows a context-cost estimate before you install. Installing the same pack two ways doubles it; mattpocock/skills warns that a plugin plus copied files "gives you every skill twice".
3. **Check who keeps it working.** In the August 5–12 window, the two largest gains in the wave went to two personal directories, and [market events](../market-events.md#may-2026-ongoing--the-claudeskills-wave) flagged key-person risk. ECC's README says it has a single maintainer. A skill tuned to one agent's behaviour can break when that agent changes, and anthropics/skills tells you to "always test skills thoroughly in your own environment."
4. **Read the fine print on data.** Superpowers' optional visual companion loads a logo from Prime Radiant's site that reports the Superpowers version. Its README says it carries no project details, and the `SUPERPOWERS_DISABLE_TELEMETRY` variable turns it off.

## Where To Start

1. **You only want Claude to make documents.** You already have the pre-built Word, Excel, PowerPoint and PDF skills on claude.ai with nothing to install.
2. **You want to understand the format.** Read one skill in [anthropics/skills](https://github.com/anthropics/skills) and the spec at agentskills.io, then write one `SKILL.md` of your own in `~/.claude/skills/` or `.agents/skills/`. A ten-line skill you wrote teaches more than a 300-skill install.
3. **You use a coding agent and want a whole method.** [Superpowers](../agents/superpowers.md) if you want the process without extra runtime; [ECC](../agents/ecc.md) if you live in Claude Code and want hooks, memory and a config scanner as well. Install one, not both: each imposes its own cycle.
4. **You want to borrow a few good habits.** Take single skills from [mattpocock/skills](https://github.com/mattpocock/skills) (alignment and TDD) or [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (a define-to-ship lifecycle). Install at project scope first and remove what does not fire.

Whatever you pick, the host agent still sets the ceiling. A skill tells a capable agent what to do; it does not make a weaker one capable. See the [terminal coding CLI comparison](coding-cli-agents.md) for the agents themselves.

## Recent Changes

- **2026-11-01** — Page created, after Anthropic's Oct 22 donation of the standard. Recorded on the way: ECC's README now gives 314 skills and 98 commands (its profile, from Oct 28, says 311 and 97). Superpowers' README now lists 16 install targets, more than its profile names.

## Sources

- Standard: [agentskills.io overview](https://agentskills.io) · [Specification](https://agentskills.io/specification) · [Donating Agent Skills to the Agentic AI Foundation](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation) (Anthropic, Oct 22 2026)
- Anthropic: [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Skills in Claude Code](https://code.claude.com/docs/en/skills) · [Plugins overview](https://code.claude.com/docs/en/plugins) · [Skills in the Agent SDK](https://code.claude.com/docs/en/agent-sdk/skills) · [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) · [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- Other agents: [Codex / ChatGPT skills](https://learn.chatgpt.com/docs/build-skills) · [Cursor skills](https://cursor.com/docs/context/skills) · [VS Code agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) · [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) · [OpenCode skills](https://opencode.ai/docs/skills/) · [What is MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- Collections: [Superpowers README](https://github.com/obra/superpowers#readme) · [mattpocock/skills README](https://github.com/mattpocock/skills#readme) · [ECC README](https://github.com/affaan-m/ECC#readme) · [anthropics/skills README](https://github.com/anthropics/skills#readme) · [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills#readme)
- Maintainers: [mattpocock.com](https://www.mattpocock.com/) · [totaltypescript.com](https://www.totaltypescript.com/) · [addyosmani.com](https://addyosmani.com/)
