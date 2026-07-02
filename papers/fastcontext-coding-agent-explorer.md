---
type: entity
title: FastContext — Training Efficient Repository Explorer for Coding Agents
created: 2026-06-28
updated: 2026-06-28
tags: [model, agent-systems, methodology]
sources: [papers/2606.14066]
---

# FastContext: Training Efficient Repository Explorer for Coding Agents

**arXiv:** [2606.14066](https://arxiv.org/abs/2606.14066) (cs.SE)
**Author group:** Microsoft Research + collaborators
**Submitted:** 12 Jun 2026 (v1), updated v3 18 Jun 2026
**Code:** [github.com/microsoft/fastcontext](https://github.com/microsoft/fastcontext)
**License:** CC BY-NC-ND 4.0

## Key Problem

Repository exploration is a bottleneck for coding agents: locating relevant code consumes substantial token budget and pollutes context with irrelevant snippets. Most agents use the same model to explore AND solve — conflating two different skills.

## Solution: Dedicated Subagent Architecture

FastContext is a **dedicated exploration subagent** separated from the solver:

| Component | Role | Size |
|-----------|------|:----:|
| FastContext (explorer) | Parallel tool calls, returns file paths + line ranges | 4B–30B |
| Main coding agent | Solves the task using focused context from FastContext | Any |

## Training Pipeline

1. **Bootstrapped** from strong reference-model trajectories
2. **Refined** with task-grounded rewards for:
   - Broad first-turn search
   - Multi-turn evidence gathering
   - Precise citation generation

## Results (integrated into Mini-SWE-Agent)

| Benchmark | Resolution Improvement | Token Reduction |
|-----------|:---------------------:|:--------------:|
| SWE-bench Multilingual | Up to **5.5%** | Up to **60%** |
| SWE-bench Pro | Included | Included |
| SWE-QA | Included | Included |

## Relevance to Our Stack

- **Subagent architecture pattern** directly applicable to P3's agent loop design
- Separating exploration from solving is a form of **architectural scaffold optimization** — optimizing the structure of tool use, not just the solving
- The 60% token reduction is significant for local-model deployment (our Gemma4-agent-12b has limited context)

## Connections

- [[concepts/scaffold-optimization]] — FastContext's subagent separation IS architectural scaffold optimization
- [[papers/ornith-1-self-improving-coding|Ornith-1.0]] — different approach to agent improvement (architecture vs. RL weights)
- P3: directly applicable — FastContext pattern could be trained as a skill-specific subagent
