# LlamaIndex

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/llamaindex.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](llamaindex.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: LlamaIndex is the data framework for building RAG and agentic applications — strongest when your agents need to reason over your own documents and data.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | LlamaIndex, Inc. |
| Route | Data-first agent and RAG framework |
| Open source | Yes, MIT |
| Best for | Applications that need to ingest, index, and reason over documents, databases, and APIs |
| Main cost | Tuning chunking, indexing, and retrieval quality for production takes effort |
| Official website | https://www.llamaindex.ai |
| GitHub repo | https://github.com/run-llama/llama_index |

## When To Pick It

- Your agents need to reason over your own data — documents, PDFs, SQL, APIs.
- You want production-grade RAG with advanced indexing, chunking, and re-ranking.
- You need 300+ data connectors out of the box.
- You want agent capabilities (ReAct agents, tool calling) built on top of strong retrieval.
- You want event-driven Workflows for multi-step agent orchestration with branching and parallel execution.

## When Not To Pick It

- You need complex stateful multi-agent orchestration with conditional logic and human-in-the-loop. LangGraph is stronger there.
- You have no retrieval needs and just want a simple prompt chain.
- You want a visual no-code agent builder. Look at n8n or AutoGPT instead.
- You want a finished coding agent, not a framework. Look at Claude Code or Cursor instead.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| RAG / retrieval | Very strong | Core strength — advanced indexing, chunking, re-ranking |
| Data connectors | Very strong | 300+ integrations for documents, databases, APIs |
| Agent framework | Strong | ReAct agents, tool calling, Agent Workflows |
| Workflow orchestration | Medium | Event-driven Workflows engine, but less control than LangGraph |
| MCP support | Medium | MCP server support added in 2026 |
| Multi-agent orchestration | Weak | Not the primary design focus |
| Visual builder | None | Code-first framework |

## Operating Cost

Complexity is Medium. The framework itself is free (MIT). Costs come from LLM API calls for both embedding and inference. The real effort is tuning retrieval quality — choosing the right chunking strategy, index type, and re-ranker for your data. Many production systems pair LlamaIndex for retrieval with LangGraph for orchestration.

## Bottom Line

If your agent needs to know your data, LlamaIndex is the strongest retrieval foundation to build on. It is not a general-purpose agent orchestrator — it is the retrieval layer that makes other agents smarter.
