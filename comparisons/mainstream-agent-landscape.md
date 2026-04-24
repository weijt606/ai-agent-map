# Mainstream Agent Selection Matrix

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/mainstream-agent-landscape.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](mainstream-agent-landscape.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This is not a leaderboard. It is a first-pass matrix for shrinking the shortlist.

Each row answers one question: what kind of problem is this project best suited to solve?

## One-Page Comparison View

| Project | Route | Where it runs | Operating rhythm | Best for | Main cost |
| --- | --- | --- | --- | --- | --- |
| [Aider](../agents/aider.md) | Terminal-first pair-programming agent | Local terminal and repo | High interaction, git-centered | Repo-local coding with explicit diffs and model choice | API and model setup are part of the workflow |
| [Claude Code](../agents/claude-code.md) | Local collaboration coding agent | Terminal, IDE, desktop, web | High interaction | Teams who want to code with an agent in-flow | Less ideal for fully detached background execution |
| [Claude Managed Agents](../agents/claude-managed-agents.md) | Managed automation path | Anthropic managed / cloud execution | Scheduled, detached, programmatic | Background Claude workflows | Public boundary is spread across multiple concepts |
| [Codex](../agents/codex.md) | Cloud delegation coding agent | Isolated cloud execution plus CLI / IDE | Async delegation | Reviewable task execution with logs and tests | Less immediate than editor-native agents |
| [GPT-5.5](../agents/gpt-5.5.md) | Frontier agentic model | ChatGPT, Codex, API, GitHub Copilot | Model upgrade across surfaces | Agent builders choosing the strongest OpenAI model, or teams evaluating the new capability ceiling | 2x API price vs GPT-5.4 and fully proprietary |
| [oh-my-claudecode](../agents/oh-my-claudecode.md) | Workflow / orchestration layer | Claude Code plugin, terminal, tmux | In-session plus orchestrated side flows | Claude Code users who want reusable skills, teams, and richer runtime control | Best value depends on already using Claude Code |
| [oh-my-codex](../agents/oh-my-codex.md) | Workflow / orchestration layer | Codex CLI, local terminal, tmux | Local workflow standardization | Codex users who want teams, hooks, and durable session state | Adds ceremony and works best on macOS or Linux with tmux |
| [Cursor](../agents/cursor.md) | AI editor / agent platform | Editor, CLI, cloud, web, mobile | Editor-led with optional background delegation | Teams that want one polished AI surface for coding and handoff | Broad product surface can be more than some teams want |
| [GitHub Copilot](../agents/github-copilot.md) | Agent platform | VS Code, local CLI, cloud, GitHub | Local-to-cloud handoff | Teams centered on VS Code and GitHub | Best value depends on ecosystem alignment |
| [Cline](../agents/cline.md) | Approval-first coding agent | Editor and local terminal | High approval, high control | Powerful editor-native automation with human control | Approval overhead is part of the model |
| [Windsurf](../agents/windsurf.md) | AI-native IDE | Dedicated editor and local environment | Editor-first, in-flow | Users who want Cascade-centered AI editing inside a dedicated IDE | Narrower extension story than VS Code |
| [OpenHands](../agents/openhands.md) | Open-source SWE agent | Self-hosted, cloud, enterprise | Flexible | Teams evaluating serious open-source execution | Heavier setup and runtime requirements |
| [Devin](../agents/devin.md) | Managed executor | Managed cloud product | Delegate then review | Clear issue-to-PR style execution | Less room for self-hosting and deep customization |
| [Jules](../agents/jules.md) | Managed cloud coding agent | Google-managed cloud VM, web, CLI, API | Async delegation | GitHub-connected coding tasks with PR-oriented handoff | Cloud-first and some surfaces are still alpha |
| [AI Edge Gallery](../agents/ai-edge-gallery.md) | On-device assistant sandbox | Mobile devices | Local experimentation | Private local models, mobile actions, and edge-agent skills | Not a coding-first agent or orchestration platform |
| [Goose](../agents/goose.md) | Extensible local agent | Desktop, CLI, API, local machine | Local and extensible | Open-source local agent with extensions, MCP, and shared config | Product boundary is broader than coding alone |
| [Hermes Agent](../agents/hermes-agent.md) | Self-hosted multi-agent environment | CLI plus gateway | Long-lived | Memory, skills, delegation, channels | Needs ongoing operational curation |
| [OpenClaw](../agents/openclaw.md) | Runtime / gateway | Local-first self-hosted runtime | Always-on runtime style | Multi-channel, device-aware, tool-rich assistants | Too heavy for pure coding-only work |
| [LangChain](../agents/langchain.md) | High-level framework | Open-source library | Fast assembly | Building custom agents quickly | Less precise than lower-level orchestration |
| [LangGraph](../agents/langgraph.md) | Low-level orchestration framework | Open-source library | Platform building | Durable stateful agent workflows | Highest design and ops burden |
| [Continue](../agents/continue.md) | Open-source editor AI extension | VS Code, JetBrains | Editor-centric, BYO model | Teams wanting model freedom and open-source IDE assistant | You own model setup and configuration |
| [AutoGPT](../agents/autogpt.md) | Autonomous agent platform | Cloud platform or self-hosted Docker | Autonomous loop execution | Visual agent building with marketplace and multi-model support | Reliability still catching up; token spend adds up fast on autonomous loops |
| [CrewAI](../agents/crewai.md) | Multi-agent orchestration framework | Local or CrewAI Cloud | Role-based crew collaboration | Fast multi-agent prototyping with role-based agent teams | Complex conditional logic pushes you toward LangGraph |
| [LlamaIndex](../agents/llamaindex.md) | Data-first RAG and agent framework | Local or LlamaCloud | Data ingestion and retrieval-first | Applications that need agents to reason over documents, databases, and APIs | Not a general-purpose agent orchestrator |
| [n8n](../agents/n8n.md) | Visual workflow automation | Self-hosted or n8n Cloud | Event-driven workflow | AI agent workflows with 400+ real integrations and visual builder | Fair-code license, not pure OSI open-source |
| [MemGPT](../agents/memgpt.md) | Stateful agent platform | Self-hosted Docker or Letta Cloud | Long-running stateful | Agents that need to remember across sessions and learn over time | Extra LLM calls for memory management; replaces your agent stack |
| [Froge Code](../agents/froge-code.md) | Review-first automation platform | Self-hosted platform | Multiple attempts plus human choice | Task-board-centric coding automation | Name still needs confirmation |

## How To Read This Table

1. Start with the route and eliminate the models that do not match your workflow.
2. Check where the system runs and remove anything that violates your deployment boundary.
3. Read the “main cost” column carefully. It is usually more important than the feature list.

## Three Things Not To Mix Up

- A framework is not the same thing as a finished agent.
- Feature support is not the same thing as primary strength.
- Operating cost is part of the product.