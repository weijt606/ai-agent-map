# CrewAI

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/crewai.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](crewai.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CrewAI is a Python framework for orchestrating role-based AI agents that collaborate on complex tasks as a crew.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | CrewAI Inc. |
| Route | Multi-agent orchestration framework |
| Open source | Yes, MIT |
| Best for | Teams that want role-based agent collaboration — researcher, writer, reviewer — with fast prototyping |
| Main cost | Token spend multiplies with agent count; complex conditional logic pushes you toward LangGraph |
| Official website | https://crewai.com |
| GitHub repo | https://github.com/crewAIInc/crewAI |

## When To Pick It

- You want to define agents by role, goal, and backstory, then have them collaborate in a crew.
- You need sequential, hierarchical, or parallel task pipelines with delegation between agents.
- You want fast multi-agent prototyping without a steep learning curve.
- You need MCP and A2A protocol support for interoperability.
- You are model-agnostic and want to wire in OpenAI, Anthropic, or local LLMs.

## When Not To Pick It

- You need complex branching, looping, and conditional state machines. LangGraph is stronger there.
- You need fine-grained control over execution graphs and human-in-the-loop approvals.
- You need production-grade observability out of the box without paying for the Enterprise tier.
- You want a finished agent product, not a framework to build your own.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Role-based agents | Very strong | Core design pattern — each agent has role, goal, backstory |
| Task pipelines | Strong | Sequential, hierarchical, and parallel |
| Agent delegation | Strong | Agents can delegate tasks to other agents |
| Memory | Medium | Built-in short and long-term memory |
| Tool use | Strong | Agents can use tools and call APIs |
| MCP / A2A | Medium | Supported as of 2026 |
| Visual builder | Medium | Available on paid Enterprise platform |
| State machine control | Weak | Not designed for graph-based conditional logic |

## Operating Cost

Complexity is Medium. The open-source core is free and quick to start with — define roles, wire up a crew, run it. The real cost is LLM API tokens: every agent call is a model call, and multi-agent crews multiply spend proportionally. Paid cloud plans range from $99/month to $120K/year for Enterprise.

## Bottom Line

CrewAI is the fastest path to multi-agent prototyping with role-based collaboration. The common pattern is: prototype in CrewAI, then migrate critical workflows to LangGraph if you need deeper state control.
