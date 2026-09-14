---
type: concept
title: Graph Of Thoughts
ingested_via: put_page
ingested_at: '2026-06-24T00:58:58.957Z'
source_kind: put_page
created: 2026-06-24
---
# Graph of Thoughts (GoT)

## Overview

**Graph of Thoughts (GoT)** is a framework that models LLM reasoning as a directed graph where vertices are "thoughts" (information units) and edges represent dependencies. It extends Chain-of-Thought (CoT) and Tree-of-Thoughts (ToT) by enabling arbitrary graph transformations including aggregation, refinement, and generation.

## Core Concept

- **Vertices**: LLM "thoughts" (units of information)
- **Edges**: Dependencies between thoughts
- **Transformations**: Operations on thoughts (generate, score, aggregate, refine)

## Key Transformations

### 1. Aggregation
Combine arbitrary thoughts into new ones to reinforce advantages and eliminate weaknesses.

**Use case**: Merging sorted subarrays or combining article summaries.

### 2. Refinement
Enhance a current thought by modifying its content through feedback loops.

**Use case**: Improving a code snippet or correcting a sorted list.

### 3. Generation
Generate new thoughts based on existing single thought (similar to ToT branching).

**Use case**: Exploring different reasoning paths or sorting sub-lists.

## Comparison to Existing Methods

| Scheme | Chain | Multiple Chains | Tree | Arbitrary Graph |
|--------|-------|-----------------|------|-----------------|
| CoT | ✅ | ❌ | ❌ | ❌ |
| CoT-SC | ❌ | ✅ | ❌ | ❌ |
| ToT | ❌ | ❌ | ✅ | ❌ |
| **GoT** | ❌ | ❌ | ❌ | ✅ **UNIQUE** |

## Performance

- **Quality**: +62% improvement over ToT
- **Cost**: -31% reduction compared to naive ensemble
- **Reasoning**: Depth + breadth through feedback loops and branching
- **Robustness**: Higher through multiple perspective merging

## System Architecture

The modular architecture consists of:

1. **Controller**: Coordinates the process
   - Graph of Operations (GoO): Static structure specifying graph decomposition
   - Graph Reasoning State (GRS): Dynamic state (thoughts, scores, history)

2. **Prompter**: Prepares prompts sent to LLM, encoding graph structure

3. **Parser**: Extracts information from LLM replies to update GRS

4. **Scoring & Validation**: Verifies correctness and assigns scores (LLM, human, or local functions)

## Formal Definition

GoT is modeled as a tuple: $(G, \mathcal{T}, \mathcal{E}, \mathcal{R})$

- $G$: LLM reasoning process (graph of thoughts and relationships)
- $\mathcal{T}$: Potential thought transformations
- $\mathcal{E}$: Evaluator function to obtain scores
- $\mathcal{R}$: Ranking function to select relevant thoughts

## Installation

```bash
pip install graph_of_thoughts
```

**Config file (`config.json`):**
```json
{
  "openai_key": "sk-...",
  "model": "gpt-4"
}
```

## Quick Example

```python
from graph_of_thoughts import operations, controller, language_models

# Create graph: Generate → Score → Aggregate → Refine
gop = operations.GraphOfOperations()
gop.append_operation(operations.Generate(k=5))
gop.append_operation(operations.Score(scoring_function=sharpe_ratio))
gop.append_operation(operations.Aggregate(top_k=2))
gop.append_operation(operations.Refine())

lm = language_models.ChatGPT("config.json")
ctrl = controller.Controller(lm, gop, Prompter(), Parser())
ctrl.run()
```

## Related Concepts

- [[Chain of Thought (CoT)]]
- [[Tree of Thoughts (ToT)]]
- [[Self-Consistency]]
- [[Prompt Engineering]]

## Applications

### Portfolio Analysis
- Explore multiple rebalancing strategies in parallel
- Score each by Sharpe ratio, drawdown, risk-adjusted returns
- Aggregate top strategies into hybrid approach

### Causal Discovery
- Generate multiple candidate causal graphs
- Score each by stability, predictive power, domain knowledge
- Merge or select most robust graph

### Risk Attribution
- Run VaR/CVaR with different methods (historical, parametric, Monte Carlo)
- Analyze factor exposure with different factor models
- Stress test with different scenarios
- Synthesize comprehensive risk report

### Macro Brief Generation
- Generate bull/bear/base case scenarios
- Score by data support
- Merge into balanced brief
- Refine into executive summary

## Resources

- **Paper**: [Graph of Thoughts: Solving Elaborate Problems with LLMs (arXiv)](https://arxiv.org/pdf/2308.09687.pdf)
- **GitHub**: [spcl/graph-of-thoughts](https://github.com/spcl/graph-of-thoughts)
- **Maintainer**: Scalable Parallel Computing Laboratory (spcl)

## Citations

If you use GoT, cite:
```bibtex
@article{besta2024got,
  title = {{Graph of Thoughts: Solving Elaborate Problems with Large Language Models}},
  author = {Besta, Maciej and Blach, Nils and Kubicek, Ales and Gerstenberger, Robert and Gianinazzi, Lukas and Gajda, Joanna and Lehmann, Tomasz and Podstawski, Micha{\l} and Niewiadomski, Hubert and Nyczyk, Piotr and others},
  journal = {arXiv preprint arXiv:2308.09687},
  year = {2024}
}
```

## Tags

#ai #llm #reasoning #graph #framework #prompting #causal #quantitative
