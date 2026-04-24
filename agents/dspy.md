# DSPy

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/dspy.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](dspy.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: DSPy replaces hand-crafted prompts with declarative Python modules that a compiler optimizes automatically — programming, not prompting, language models.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Stanford NLP / Omar Khattab |
| Route | Programmatic prompt optimization framework |
| Open source | Yes, MIT |
| Best for | Teams that want algorithmically optimized prompts instead of manually engineered ones |
| Main cost | Steep learning curve; debugging compiled prompts can be opaque |
| Official website | https://dspy.ai |
| GitHub repo | https://github.com/stanfordnlp/dspy |

## When To Pick It

- You want a compiler to find optimal few-shot examples and instructions automatically, instead of writing prompts by hand.
- You need composable LM pipelines — chain modules like ChainOfThought, ReAct, and ProgramOfThought like PyTorch layers.
- You care about evaluation-driven optimization with built-in assertions and metrics.
- You want to swap models without rewriting prompts — DSPy recompiles for the new model.

## When Not To Pick It

- You have a simple single-prompt task. DSPy is overkill.
- You need production deployment tooling — tracing, auth, rate-limiting. LangChain's ecosystem is more mature there.
- You want a visual builder or low-code experience.
- You need a finished agent product, not a research-grade optimization framework.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Prompt optimization | Very strong | Core design — compilers search for optimal prompts |
| Composable pipelines | Very strong | Declarative modules chained like PyTorch layers |
| Evaluation / metrics | Strong | Built-in assertions and metric-driven optimization |
| Model agnostic | Strong | OpenAI, Anthropic, Ollama, vLLM, etc. |
| Production tooling | Weak | Less mature than LangChain for deployment infra |
| Visual builder | None | Pure Python, code-first |

## Operating Cost

Complexity is High. DSPy is fundamentally different from prompt engineering — it requires understanding compilers, signatures, and optimization loops. The payoff is significant for teams running many LM calls at scale, where prompt optimization directly reduces cost and improves quality. But the learning curve is real.

## Bottom Line

DSPy is not a competitor to LangChain or LlamaIndex — it is complementary. It optimizes the prompts that other frameworks execute. Pick it when you want the machine to find better prompts than you can write by hand.
