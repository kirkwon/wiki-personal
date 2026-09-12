---
date: 2026-06-28
type: media
title: OSWorld 2.0 — Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks
created: 2026-06-28
updated: 2026-06-28
tags: [model, comparison, methodology]
sources: [papers/osworld-v2-xlang-ai]
---

# OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks

**Source:** [osworld-v2.xlang.ai](https://osworld-v2.xlang.ai/)
**Author group:** XLANG Lab (HKU), UCSD, Columbia, UC Santa Barbara, Mila, Uniphore, Snorkel AI, UW-Madison, Alibaba Qwen, Ohio State, Simular, NeoCognition
**Code:** [github.com/xlang-ai/OSWorld-V2](https://github.com/xlang-ai/OSWorld-V2)
**Data:** [huggingface.co/datasets/xlangai/osworld_v2_tasks](https://huggingface.co/datasets/xlangai/osworld_v2_tasks)

## The Benchmark

**108 long-horizon computer-use workflows** spanning everyday and professional tasks across **31 self-hosted websites**:

| Metric | Value |
|--------|-------|
| Median human time | ~1.6 hours |
| Tasks >1 hour | 69.6% |
| Avg agent steps | >250 |
| Avg scoring checkpoints | 27.25 |
| Economic value covered | **$1.64T GDP proxy** |

## Leaderboard (108 tasks, 500-step budget)

| Rank | Model | Binary | Partial |
|:----:|-------|:-----:|:-------:|
| 1 | **Claude Opus 4.8** (Anthropic) | **20.6%** | **54.8%** |
| 2 | Claude Opus 4.7 (Anthropic) | 18.2% | 48.9% |
| 3 | **GPT-5.5** (OpenAI) | 13.0% | 49.5% |
| 4 | Claude Sonnet 4.6 | 9.3% | 33.9% |
| 5 | MiniMax M3 | 4.6% | 22.3% |
| 6 | Kimi 2.6 | 4.6% | 22.1% |
| 7 | Qwen 3.7-Plus | 2.8% | 21.5% |

## Key Findings

1. **Higher scores require disproportionately more tokens** — GPT-5.5 plateaus at ~14%, Claude scales to 20% but at 225K tokens
2. **Task horizon is a hard limit** — above 137 min no model exceeds 10%; above 163 min **all models score 0%**
3. **Agents are weak at recovering hidden state** — implicit-state inference, multi-item tracking, conflict disambiguation, dynamic environments are the hardest failure modes

## Relevance to Our Stack

- Directly applicable to our **computer-use** toolchain (CUA driver, Camofox, agent-browser)
- OSWorld 2.0 is the benchmark our computer-use agents should be evaluated against
- The "task horizon as hard limit" finding supports investing in **state management** over raw capability scaling
- Failure modes (implicit-state inference, multi-item tracking) are areas where [[concepts/scaffold-optimization]] could help — better prompts for tracking hidden state

## Connections

- [[concepts/scaffold-optimization]] — better scaffolds could address the hidden-state failure modes
- [[papers/tmax-terminal-agents]] — terminal agents (Tmax) vs computer-use agents (OSWorld 2.0): complementary domains
- P3-T7 (Evaluation) — OSWorld 2.0 should be one of the evaluation benchmarks for agentic coding tasks
