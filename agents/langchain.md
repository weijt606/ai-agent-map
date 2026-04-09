# LangChain

[![中文](https://img.shields.io/badge/中文-查看中文版-9ca3af?style=flat-square)](../zh/agents/langchain.md)
[![English](https://img.shields.io/badge/English-Current%20Page-1f6feb?style=flat-square)](langchain.md)

One-line take: LangChain is not a ready-made agent. It is a higher-level assembly layer for building custom agents quickly.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | LangChain |
| Route | High-level agent framework |
| Open source | Yes |
| Best for | Fast prototyping of custom agents |
| Main cost | Complex workflows often still push downward into lower-level orchestration |
| Official entry | https://docs.langchain.com/oss/python/langchain/overview |

## When To Pick It

- You want to build a custom agent or autonomous app quickly.
- You want high-level abstractions rather than starting with state-machine design.
- You want to validate a direction before committing to heavier platform work.

## When Not To Pick It

- You actually want a ready-to-run coding agent.
- You need fine-grained control over checkpoints, recovery, and durable state.
- You only need a small script and not an agent framework.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agent abstraction | Strong | Fast to get moving |
| Tool use | Strong | Good tool integration story |
| Model integrations | Strong | Convenient across providers |
| Speed to prototype | Strong | One of the most practical reasons to use it |
| Durable orchestration | Medium | Lower-level control lives more naturally in LangGraph |

## Operating Cost

Complexity is Medium. It is lighter than LangGraph, but it is still a framework, which means you still own prompts, tools, evals, and deployment boundaries.

## Bottom Line

If your goal is “get a custom agent standing up quickly,” LangChain is usually the cleaner first step.