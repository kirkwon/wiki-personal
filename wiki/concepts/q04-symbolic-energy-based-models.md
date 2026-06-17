---
tags: [permanent-question, research, ml-alternatives]
created: 2026-05-25
question: "What non-transformer architectures show promise? Energy-based models, neural-symbolic, state space models (Mamba), differentiable logic, Hopfield networks — what's state of art and practical utility?"
type: permanent-question
description: "Q04: Symbolic AI and Energy-Based (Non-Transformer) Models"
reviewed: 2026-05-25
---

# Q04: Symbolic AI and Energy-Based (Non-Transformer) Models

## Question
*What non-transformer architectures show promise? Energy-based models, neural-symbolic, state space models (Mamba), differentiable logic, Hopfield networks — what's state of art and practical utility?*

## Current State of Knowledge

### State Space Models (Mamba / S4)
- **What they are**: Recurrent models that can be computed like convolutions, competitive with transformers on long sequences
- **Mamba** (2023): Selective state spaces, hardware-aware algorithm. Can process 1M token sequences.
- **vs Transformer**: More efficient on long sequences, linear complexity vs quadratic
- **Finance applicability**: Modeling very long dependencies in market data. SOTA for genomics, potentially useful for multi-year economic cycles.
- **Limitation**: Less mature than transformers. Not clearly better for standard financial prediction tasks with short histories.
- **Key paper**: Gu & Dao — "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (2023)

### Energy-Based Models (EBMs)
- **What they are**: Models that learn to assign low energy to correct samples, high energy to incorrect ones. The model defines a probability distribution via its energy function.
- **Examples**: Hopfield Networks, Boltzmann Machines, Contrastive Divergence
- **Recent advances**: 
  - Flow-based models (Nice, RealNVP, Glow) — tractable density estimation via invertible transforms
  - Score-based / diffusion models — denoising score matching
  - EBMs + neural networks: energy-based neural networks for structured prediction
- **Finance applicability**: Modeling probability distributions of returns for risk scenarios. Generating realistic synthetic data for backtesting.
- **Where they shine**: Modeling multimodal distributions (finance returns often have fat tails and multiple regimes)
- **Limitation**: Hard to train (contrastive divergence is tricky). Not clearly better than VAEs or GANs for generation.

### Neural-Symbolic Integration
- **What it is**: Combining symbolic reasoning (logic, rules, knowledge graphs) with neural networks (pattern recognition, gradients)
- **Why it matters**: Finance has strong prior knowledge (Black-Scholes, factor models). Symbolic integration lets you encode these as constraints.
- **Physics-Informed Neural Networks (PINNs)**: Encode physical/conservation laws as soft constraints. In finance: encode no-arbitrage conditions as constraints.
- **Differentiable Logic**: Neural networks that can learn logical operations, enabling symbolic reasoning within gradient-based learning.
- **Key paper**: Garcez et al. — "Neural-Symbolic Learning and Reasoning: A Survey"
- **Finance applicability**: Encoding no-arbitrage constraints in option pricing models. Knowledge graphs for market entities + NN for inference.

### Knowledge Graphs + Graph Neural Networks
- **What**: Explicit structured knowledge + graph neural networks for inference
- **Finance use**: Modeling company relationships, supply chains, market correlations as graphs
- **GNN for finance**: Predicting credit risk from company relationships. Detecting contagion pathways.
- **Practical**: Knowledge graphs are the most immediately deployable "symbolic" approach for finance.

### What NOT to Use (yet)
- Pure symbolic AI for prediction (too brittle, can't handle noise)
- Hopfield networks for anything beyond memory models (ancient, superceded)
- Most neurosymbolic approaches are research prototypes

### Hybrid That Could Work for Finance
1. **PINNs for derivatives pricing**: Encode Black-Scholes PDE as physics loss, train NN to solve it. More flexible than analytic solution.
2. **GNN + Market microstructure**: Model order book as graph, predict price impact.
3. **EBM for tail risk**: Learn the energy landscape of returns, identify when system is in a high-energy (risky) state.

## Key Papers
- Gu & Dao — "Mamba" (2023)
- LeCun — "A Tutorial on Energy-Based Models" (2019, comprehensive overview)
- Garcez et al. — "Neural-Symbolic Learning and Reasoning" (2019, survey)
- Raissi et al. — "Physics-Informed Neural Networks" (2019, PINNs)
- Hamilton et al. — "Embedding Entities and Relations for Learning" (2018, knowledge graph embeddings)



### Pearl's Causal Framework + Microsoft's DoWhy

**This is arguably the most important non-transformer development for finance AI.**

**Why**: Pearl's causal inference framework (structural causal models, do-calculus) provides a
formal language for reasoning about causality. This is categorically different from
correlation-based ML and is the primary gap in most financial AI systems.

**The core idea**:
- Build a causal graph (DAG) encoding your assumptions about what causes what
- Use do-calculus to determine if causal effects can be identified
- Estimate causal effects, then test robustness with refutation tests

**Microsoft DoWhy** (https://www.microsoft.com/en-us/research/project/dowhy/):
Implements Pearl's framework in Python. Four steps:
1. Model causal assumptions as a graph
2. Identify identifiable causal queries
3. Estimate using appropriate methods
4. Refute with sensitivity analysis and placebo tests

**Why it matters for non-transformer AI**:
- DoWhy doesn't require neural networks — it's about causal reasoning, not model architecture
- Can be combined with any underlying model (linear, tree-based, deep learning)
- Enables causal discovery from observational data (when experiments aren't possible)
- Critical for finance, where experiments are usually impossible

**Judea Pearl's lab** (bayes.cs.ucla.edu) — the theoretical foundation:
- "Causality: Models, Reasoning, and Inference" (Pearl, 2009) — the definitive text
- "Causal Inference in Statistics: A Primer" (Pearl, Glymour, Jewell, 2016) — starting point
- Do-calculus: the formal system for determining what can be inferred from causal assumptions
- Confounders: variables that cause both treatment and outcome; must be controlled for

**The connection to energy-based models**: EBMs can be seen as defining an energy landscape
where causal interventions shift the landscape. This is speculative but potentially interesting.

**Key papers**:
1. Pearl — "Causality: Models, Reasoning, and Inference" (2009)
2. Pearl, Glymour, Jewell — "Causal Inference in Statistics: A Primer" (2016)
3. Sharma et al. — "DoWhy: An End-to-End Library for Causal Inference" (arXiv:2011.04216)
4. Pearl — "The Book of Why" (2018, with Dana Mackenzie) — accessible version


## Emerging Methodology

The most immediately applicable non-transformer approaches for finance:

1. **GNNs for market networks** — low-hanging fruit, well-supported by libraries
2. **PINNs for pricing** — if you're doing derivatives work, this is interesting
3. **Diffusion models for scenario generation** — generating realistic market scenarios is practically valuable

The "energy-based" framing is mostly interesting as conceptual — diffusion models are the practical descendant.

## Connections
- [[q02]] — symbolic reasoning could enable better agent tool use
- [[q05]] — GNNs and PINNs are directly applicable to predictive finance

## Last Updated
_2026-05-25_ — Initial research position
