# Haystack

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/haystack.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](haystack.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Haystack is deepset's production-oriented Python framework for RAG pipelines, AI agents, and semantic search — more opinionated than LangChain, lower overhead.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | deepset |
| Route | Production-grade RAG and agent framework |
| Open source | Yes, Apache 2.0 |
| Best for | Teams building production RAG pipelines, search, and agents who want explicit pipeline control with lower overhead |
| Main cost | Smaller ecosystem than LangChain; code-first, no visual builder |
| Official website | https://haystack.deepset.ai |
| GitHub repo | https://github.com/deepset-ai/haystack |

## When To Pick It

- You want modular, production-oriented pipelines with branching, loops, and conditional routing.
- You need RAG with pluggable retrievers, document stores, and evaluation built in.
- You care about lower framework overhead (~5.9ms vs LangChain's ~10ms in benchmarks).
- You want agent workflows with tool calling and memory in a well-structured pipeline.
- You need to expose pipelines as HTTP or MCP endpoints via Hayhooks.

## When Not To Pick It

- You need the largest third-party ecosystem — LangChain has more community integrations.
- You want a visual no-code builder.
- You have a simple project where Haystack's pipeline abstraction is overkill.
- You need a managed-only solution with zero self-hosting.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| RAG pipelines | Very strong | Core strength with pluggable retrievers and stores |
| Pipeline architecture | Very strong | Modular with branching, loops, conditional routing |
| Agent workflows | Strong | Tool calling and memory |
| Evaluation | Strong | Built-in observability and evaluation |
| Model agnostic | Very strong | OpenAI, Anthropic, Mistral, Cohere, HuggingFace, Azure, Bedrock, local |
| MCP / API exposure | Medium | Hayhooks for HTTP and MCP endpoints |
| Ecosystem size | Medium | Smaller than LangChain |

## Operating Cost

Complexity is Medium. Well-documented, production-oriented, and opinionated — which can be a feature. The framework is free (Apache 2.0). deepset also offers Enterprise Starter and Enterprise Platform for managed/governed deployments.

## Bottom Line

Haystack is the choice when you want LangChain-class capabilities with more production discipline and lower overhead. The trade-off is a smaller ecosystem and community.
