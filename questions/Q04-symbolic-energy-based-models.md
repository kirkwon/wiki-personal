---
tags: [permanent-question, research]
created: 2026-05-25
question: "What non-transformer architectures show promise? Energy-based models, neural-symbolic, state space models (Mamba), differentiable logic, Hopfield networks — what's state of art and practical utility?"
date: 2026-05-25
type: permanent-question
reviewed: 2026-09-02
confidence: 0.95
evidence_count: 192
last_evidence_date: 2026-09-01
---


# Q04: Symbolic AI and Energy-Based (Non-Transformer) Models

## Question
*What non-transformer architectures show promise? Energy-based models, neural-symbolic, state space models (Mamba), differentiable logic, Hopfield networks — what's state of art and practical utility?*

## Current State of Knowledge

**June 2026: CWM/LLM-as-Compiler emerged as the most practical neural-symbolic integration pattern — added below.**

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

### LLM-as-Compiler + Code World Models — Neural-Symbolic in Practice

The [[concepts/llm-as-compiler|LLM-as-Compiler]] pattern (Lehrach et al., 2025, DeepMind) is the most practically deployed neural-symbolic approach to date. The [[concepts/code-world-models|Code World Model]] pattern reframes the LLM from *direct actor* to *translator* — converting natural language specifications into executable code, then handing off to classical solvers ([[concepts/monte-carlo-tree-search|MCTS]], constraint solvers).

**Why this is neural-symbolic integration:**

| Element | Neural Component | Symbolic Component |
|---------|-----------------|-------------------|
| Role | LLM translates rules | Executable code encodes formal constraints |
| Reasoning | Semantic understanding (fuzzy, flexible) | Search/planning (deterministic, verifiable) |
| Correctness | Probabilistic (may hallucinate) | Decidable (code runs or doesn't) |
| Output | Heuristic evaluation function | MCTS search tree, game plan |

**The key insight:** The LLM provides the *semantic bridge* (natural language → formal code), while the symbolic side handles *formal reasoning* (search, constraints, optimization). This division of labor exploits each component's strength — exactly what neural-symbolic integration aims to do ([[concepts/verifiable-planning]]).

**For finance specifically:** Financial rules (Black-Scholes, factor model constraints, no-arbitrage conditions) can be encoded as CWM programs, then solved by classical optimizers rather than relying on LLM prediction. This directly addresses Q04's "Hybrid That Could Work" list — the CWM pattern provides an architecture for implementing PINN-like constraints without needing to train neural networks.

See [[papers/code-world-models-general-game-playing]], [[wiki/synthesis/cwm-game-theory-application]].

## Key Papers
- Gu & Dao — "Mamba" (2023)
- LeCun — "A Tutorial on Energy-Based Models" (2019, comprehensive overview)
- Garcez et al. — "Neural-Symbolic Learning and Reasoning" (2019, survey)
- Raissi et al. — "Physics-Informed Neural Networks" (2019, PINNs)
- Hamilton et al. — "Embedding Entities and Relations for Learning" (2018, knowledge graph embeddings)
- Lehrach et al. — "Code World Models for General Game Playing" (2025, arxiv:2510.04542, Google DeepMind)



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
- [[Q02]] — symbolic reasoning could enable better agent tool use
- [[Q05]] — GNNs and PINNs are directly applicable to predictive finance
- [[concepts/llm-as-compiler]] — LLM-as-Compiler as neural-symbolic integration (CWM pattern)
- [[concepts/code-world-models]] — CWM: LLM generates executable symbolic code for classical solvers
- [[concepts/verifiable-planning]] — Executability as the bridge between neural and symbolic
- [[papers/code-world-models-general-game-playing]] — Source paper: Lehrach et al. 2025

## Last Updated
_2026-06-24_ — Added LLM-as-Compiler / Code World Models section as the most practical neural-symbolic integration pattern (DeepMind CWM 2025). Updated status from Stable to Active.
_2026-06-12_ — Status set to stable; no recent progress
_2026-05-25_ — Initial research position

## Evidence Log

<!-- Weekly scan appends dated evidence blocks below this line.
     Format: ### YYYY-MM-DD: <topic>
             - Finding
             - Source: [[wikilink]] or URL
             - Confidence: High/Medium/Low
-->

### 2026-06-12: Code World Models — LLM as compiler, not direct actor
- CWM pattern (Lehrach et al. 2025): LLM translates natural language rules → executable code → classical solver (MCTS, constraints). Outputs are verifiable, not probabilistic. Creates reliability hierarchy for agent decisions.
- Source: [[concepts/code-world-models]] [[papers/code-world-models-general-game-playing]]
- Confidence: High

### 2026-06-24: CWM applied to game-theoretic finance

### 2026-07-30: OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedi

### 2026-07-30: Parallel Decoding Distillation for Fast Image and Video Generation

### 2026-07-02: Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Gene

### 2026-07-06: Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care

### 2025-07-02: Thinking Beyond Tokens: From Brain-Inspired Intelligence to Cognitive

### 2026-07-07: LLM-as-a-Verifier: A General-Purpose Verification Framework

### 2026-07-07: GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automat

### 2026-07-10: CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

### 2025-08-27: Forecasting Probability Distributions of Financial Returns with Deep

### 2025-10-02: CurES: From Gradient Analysis to Efficient Curriculum Learning for

### 2025-10-15: Tensor Logic: The Language of AI

### 2025-10-29: Latent Chain-of-Thought for Visual Reasoning

### 2025-11-18: Genomic Next-Token Predictors are In-Context Learners

### 2025-12-05: QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory

### 2026-01-23: From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantific

### 2026-02-06: PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling

### 2026-02-09: Self-Improving World Modelling with Latent Actions

### 2026-02-11: P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads

### 2026-03-03: Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-tra

### 2026-03-18: I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Prob

### 2026-04-09: SEVerA: Verified Synthesis of Self-Evolving Agents

### 2026-04-09: Qualixar OS: A Universal Operating System for AI Agent Orchestration

### 2026-05-28: OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

### 2026-06-15: HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

### 2026-07-07: LLM-as-a-Verifier: A General-Purpose Verification Framework

### 2026-07-07: GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automat

### 2026-07-10: CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

### 2026-08-03: In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous Driving

### 2026-08-03: Mental World Modeling

### 2026-08-03: One Future, Every Robot: Label-Efficient Collective-State Prediction with Decent

### 2026-08-03: ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

### 2026-08-03: Meshy T2: Fast Native Mesh Generation with Flow Matching

### 2026-08-03: Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential A

### 2026-08-03: ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamic

### 2026-08-03: Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generati

### 2026-08-04: SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space

### 2026-08-04: Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multim

### 2026-08-04: A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples

### 2026-08-04: DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered Video Diff

### 2026-08-04: Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language

### 2026-08-04: 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question 

### 2026-08-04: LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation

### 2026-08-04: WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reacti

### 2026-08-04: UEmbed: Unified Sparse and Dense Multimodal Embeddings

### 2026-08-04: SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zer

### 2026-08-04: WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

### 2026-08-04: Roomer: Reflective Object-Grounded Model Editing and Repair for 3D Indoor Layout
- HF trending paper (arxiv: 2608.01973). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.01973]] | https://huggingface.co/papers/2608.01973
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29613). Keywords: world model. Status: pending-review.
- Source: [[papers/2607.29613]] | https://huggingface.co/papers/2607.29613
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02023). Keywords: vae. Status: pending-review.
- Source: [[papers/2608.02023]] | https://huggingface.co/papers/2608.02023
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02583). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.02583]] | https://huggingface.co/papers/2608.02583
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02603). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.02603]] | https://huggingface.co/papers/2608.02603
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00079). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.00079]] | https://huggingface.co/papers/2608.00079
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01185). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.01185]] | https://huggingface.co/papers/2608.01185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00574). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.00574]] | https://huggingface.co/papers/2608.00574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00486). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.00486]] | https://huggingface.co/papers/2608.00486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29122). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2607.29122]] | https://huggingface.co/papers/2607.29122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01462). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.01462]] | https://huggingface.co/papers/2608.01462
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01397). Keywords: world model, geometry. Status: pending-review.
- Source: [[papers/2608.01397]] | https://huggingface.co/papers/2608.01397
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27372). Keywords: generative model, diffusion. Status: pending-review.
- Source: [[papers/2607.27372]] | https://huggingface.co/papers/2607.27372
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28362). Keywords: world model. Status: pending-review.
- Source: [[papers/2607.28362]] | https://huggingface.co/papers/2607.28362
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28319). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2607.28319]] | https://huggingface.co/papers/2607.28319
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28675). Keywords: vae, geometry, topology. Status: pending-review.
- Source: [[papers/2607.28675]] | https://huggingface.co/papers/2607.28675
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27924). Keywords: world model. Status: pending-review.
- Source: [[papers/2607.27924]] | https://huggingface.co/papers/2607.27924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28443). Keywords: embedding, topology. Status: pending-review.
- Source: [[papers/2607.28443]] | https://huggingface.co/papers/2607.28443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27201). Keywords: world model. Status: pending-review.
- Source: [[papers/2607.27201]] | https://huggingface.co/papers/2607.27201
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.15820). Keywords: world model. Status: pending-review.
- Source: [[papers/2607.15820]] | https://huggingface.co/papers/2607.15820
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.08093). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2607.08093]] | https://huggingface.co/papers/2607.08093
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05369). Keywords: variational. Status: pending-review.
- Source: [[papers/2607.05369]] | https://huggingface.co/papers/2607.05369
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05391). Keywords: probabilistic. Status: pending-review.
- Source: [[papers/2607.05391]] | https://huggingface.co/papers/2607.05391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.14249). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2606.14249]] | https://huggingface.co/papers/26
### 2026-08-05: Loop engineering is the practice of structuring agent improvement as a closed-loop system with a **critic/doer separation** — one component acts, another validates. This separation enables the agent t...

### 2026-08-05: ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Lev

### 2026-08-05: Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-B

### 2026-08-05: MiniWorld: Democratizing the Training of Video World Models from Scratch

### 2026-08-05: LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

### 2026-08-05: Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains and Sur

### 2026-08-05: ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visua

### 2026-08-05: Quo Vadis, World Modeling?

### 2026-08-05: Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for Streaming Rec

### 2026-08-05: JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusi

### 2026-08-05: Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D Generation, Un

### 2026-08-05: UniWorld-Design: From Pixel Generation to Layer-Native Design

### 2026-08-05: Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via Repre

### 2026-08-05: InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthe

### 2026-08-06: DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial P

### 2026-08-06: Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation Learnin

### 2026-08-06: WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World 

### 2026-08-06: SKILL-KD: Contrastive Skill Distillation for LLM Agents

### 2026-08-06: UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models

### 2026-08-06: HelloWorld: Enabling Socially Interactive Characters in Video World Models

### 2026-08-06: TriGlue: a Biology-Inspired Generative Model for Generating Molecular Glue-Induc

### 2026-08-06: When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K C

### 2026-08-07: Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulu

### 2026-08-07: Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptati

### 2026-08-07: From Economic Agents to Agentic Economies: A Systems Blueprint for Economic Worl

### 2026-08-07: MASS: Multiplayer World Models with Authoritative Shared State

### 2026-08-07: EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinf

### 2026-08-07: CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

### 2026-08-07: AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

### 2026-08-07: Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised Wor

### 2026-08-08: FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channel

### 2026-08-08: KVAE: Family of Tokenizers for Multimodal Generative Models

### 2026-08-10: Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure Mode i

### 2026-08-10: FATE: Frame-Level Audio-Visual Temporal Embedding

### 2026-08-10: Round-Trip Consistency: Bidirectional Diffusion Models Can Predict Their Own Rol

### 2026-08-10: Uncertainty-Aware World Model for Aerial Image-Goal Navigation

### 2026-08-10: Addressable Memory for Video World Models

### 2026-08-11: A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven Op

### 2026-08-11: SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification

### 2026-08-12: AdvFD: Boosting Visual Generation via Adversarial Fr'echet Distance Loss

### 2026-08-12: ComBodied Agents: a New Paradigm of Human-Centric Agentic AI

### 2026-08-12: Beyond Pixels: From Video Priors to 4D Worlds

### 2026-08-12: Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers

### 2026-08-12: MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation

### 2026-08-12: A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven Op

### 2026-08-12: SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification

### 2026-08-13: Parameter Exploration for RLVR via Variational Learning

### 2026-08-13: Simplex Relaxation for Discrete Diffusion

### 2026-08-13: OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution

### 2026-08-13: AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models

### 2026-08-13: Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically 

### 2026-08-13: From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-

### 2026-08-13: AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Resear

### 2026-08-13: StateFlow: Building, Evolving, and Accessing 3D World States for Previsualizatio

### 2026-08-14: AVA-Encoder: Towards Agent-Native Video Representation Learning

### 2026-08-14: PixSDS: Why Latent SDS Makes Noisy Pixels

### 2026-08-14: TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation wi

### 2026-08-14: UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

### 2026-08-14: LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time

### 2026-08-14: H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Mo

### 2026-08-14: DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

### 2026-08-14: Full-bandwidth transformer

### 2026-08-14: Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

### 2026-08-14: From Atomic Evidence to Logical Composition: Structured Compositional Reasoning 

### 2026-08-14: ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Fr

### 2026-08-14: Learning How the World Evolves: Extrapolative Video World Models via Latent Dyna

### 2026-08-17: UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Mu

### 2026-08-17: Multimodal Model Diffing for Feature Discovery and Control

### 2026-08-17: Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Infe

### 2026-08-17: SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Gen

### 2026-08-17: Marionette: Predicting World States, Rendering Geometry, Painting Appearance

### 2026-08-18: Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search

### 2026-08-18: WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Ri

### 2026-08-18: Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe Ac

### 2026-08-18: HiFi-BRep: High-Fidelity Latent Representation for Robust B-Rep Generation

### 2026-08-18: AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation

### 2026-08-18: Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable

### 2026-08-18: HarnessEval-W: Agentifying the Evaluation of Visual Worlds

### 2026-08-18: An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models

### 2026-08-18: NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Docum

### 2026-08-19: CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Represent

### 2026-08-19: V-RAE: Rethinking Video Latent Spaces for Generation

### 2026-08-19: DiSCO: Defending text-to-image generation through distribution-guided contrastiv

### 2026-08-19: PixRestore: Unified Image Restoration via Pixel Diffusion Transformer

### 2026-08-19: Demystifying Agent Skills: Why They Work-Until They Don't

### 2026-08-19: EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing

### 2026-08-19: Energy-Guided Flow Matching

### 2026-08-19: From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Gen

### 2026-08-19: GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation

### 2026-08-19: aDSL: Agentic 3D Creation via Joint Agent-Program Design

### 2026-08-19: Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning

### 2026-08-20: Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditi

### 2026-08-20: SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deforma

### 2026-08-21: GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipul

### 2026-08-21: CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical 

### 2026-08-21: Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learne

### 2026-08-21: 4DAnyone: Create Anyone in 4D from a Casual Monocular Video

### 2026-08-21: ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World

### 2026-08-21: WithEveryone: Unified Planning and Identity Grounding for Group Image Generation

### 2026-08-21: Towards Real-Time and Adaptable LiDAR Scene Completion

### 2026-08-22: TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity

### 2026-08-22: The Embedder's Dilemma: LLMs Are Better, but at What Cost?

### 2026-08-24: Hydra-0: Action Flow for Generalist World Modeling and Control

### 2026-08-24: Human-Centric Intelligence in the Era of Foundation Models: A Survey

### 2026-08-24: UniSpace: Unified Visual Representation and Scalable Multimodal Modeling

### 2026-08-24: EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking

### 2026-08-25: The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration

### 2026-08-25: EXPL-FR: Explaining Face Recognition Models via Vision-Language Alignment

### 2026-08-25: WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning

### 2026-08-25: Towards a Densing Law for User Representation Learning at Billion-Scale Capacity

### 2026-08-25: RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling

### 2026-08-25: EchoWM: Open and Enterable Omnimodal World Models

### 2026-08-25: Block3D: Efficient Text-to-3D Generation via Block-Wise Diffusion

### 2026-08-25: Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervisi

### 2026-08-25: ReWorld: An Interactive World Model with Long-Horizon Memory

### 2026-08-25: WorldMind: Decoupled Game World Model for State-Aware NPC Behavior

### 2026-08-26: Automata from Agent Traces: Failure and Next-Step Prediction

### 2026-08-26: MoTE: Mixture of Task Experts for Multi-Task Video Understanding

### 2026-08-26: Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Trainin

### 2026-08-26: WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report

### 2026-08-26: Length-Adaptive Decoding for Masked Diffusion Machine Translation

### 2026-08-27: Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worl

### 2026-08-27: Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models

### 2026-08-27: Code World Model: Coding Agent as World Brain

### 2026-08-27: MARS: Multi-Specialist LLM Relay System for Competitive Programming

### 2026-08-28: Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling Worl

### 2026-08-28: GameWAM: A World Action Model for Video Games

### 2026-08-28: CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval

### 2026-08-28: PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

### 2026-08-28: Magpie: Real-Time World Renderer for Interactive Games

### 2026-08-28: GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Gro

### 2026-08-30: Luce: Relightable Gaussians for 3D Asset Generation

### 2026-08-31: GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generati

### 2026-08-31: Language Chain in Alignment: Cross-lingual Ranking Preference Optimization

### 2026-08-31: Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities

### 2026-08-31: DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Mu

### 2026-08-31: Ring Forcing: Towards Precise Long-Term Memory for Autoregressive Video Diffusio

### 2026-08-31: LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in V

### 2026-09-01: SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language Models

### 2026-09-01: Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation a

### 2026-09-01: DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution

### 2026-09-01: WebWorld: The Browser as a World Model for Self-Improving Web Code

### 2026-09-01: Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation

### 2026-09-02: ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-

### 2026-09-02: H3-World: Turning Language Understanding into World Control

### 2026-09-02: ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Trans

### 2026-09-03: Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fie

### 2026-09-03: Wasserstein-Barycentric Interaction Fields for Spatial Factor Models: Evidence f

### 2026-09-03: NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Eff

### 2026-09-03: Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Qu

### 2026-09-03: Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Model

### 2026-09-03: ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes

### 2026-09-03: A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss

### 2026-09-03: ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrie

### 2026-09-03: MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information

### 2026-09-03: SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

### 2026-09-04: QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentati

### 2026-09-04: Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reco

### 2026-09-04: Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States

### 2026-09-04: FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow

### 2026-09-04: WorldReward: Reward Modeling for Camera-Conditioned World Models

### 2026-09-04: Editable Visual Design

### 2026-09-04: LatentPress: Context Compression Beyond Text and Vision

### 2026-09-04: Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens

### 2026-09-05: VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement

### 2026-09-07: UniMate: One Unified Model to Animate Diverse Skeletons

### 2026-09-07: The Attention Triangle in Audio-Video Models

### 2026-09-07: To See a World in a Living Context: Unified Indoor-Outdoor Urban World Generatio
- HF trending paper (arxiv: 2608.05879). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.05879]] | https://huggingface.co/papers/2608.05879
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03586). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2609.03586]] | https://huggingface.co/papers/2609.03586
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05415). Keywords: diffusion, embedding, topology. Status: pending-review.
- Source: [[papers/2609.05415]] | https://huggingface.co/papers/2609.05415
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03153). Keywords: world model. Status: pending-review.
- Source: [[papers/2609.03153]] | https://huggingface.co/papers/2609.03153
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01936). Keywords: embedding. Status: pending-review.
- Source: [[papers/2609.01936]] | https://huggingface.co/papers/2609.01936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01507). Keywords: embedding. Status: pending-review.
- Source: [[papers/2609.01507]] | https://huggingface.co/papers/2609.01507
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04034). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2609.04034]] | https://huggingface.co/papers/2609.04034
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03952). Keywords: world model, geometry. Status: pending-review.
- Source: [[papers/2609.03952]] | https://huggingface.co/papers/2609.03952
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03563). Keywords: geometry. Status: pending-review.
- Source: [[papers/2609.03563]] | https://huggingface.co/papers/2609.03563
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04196). Keywords: geometry. Status: pending-review.
- Source: [[papers/2609.04196]] | https://huggingface.co/papers/2609.04196
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04201). Keywords: geometry. Status: pending-review.
- Source: [[papers/2609.04201]] | https://huggingface.co/papers/2609.04201
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29253). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.29253]] | https://huggingface.co/papers/2608.29253
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02886). Keywords: world model, geometry. Status: pending-review.
- Source: [[papers/2609.02886]] | https://huggingface.co/papers/2609.02886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30949). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.30949]] | https://huggingface.co/papers/2608.30949
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01865). Keywords: embedding. Status: pending-review.
- Source: [[papers/2609.01865]] | https://huggingface.co/papers/2609.01865
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00591). Keywords: contrastive, embedding. Status: pending-review.
- Source: [[papers/2609.00591]] | https://huggingface.co/papers/2609.00591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01740). Keywords: vae, geometry. Status: pending-review.
- Source: [[papers/2609.01740]] | https://huggingface.co/papers/2609.01740
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30751). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.30751]] | https://huggingface.co/papers/2608.30751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21450). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.21450]] | https://huggingface.co/papers/2608.21450
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01657). Keywords: diffusion, embedding. Status: pending-review.
- Source: [[papers/2609.01657]] | https://huggingface.co/papers/2609.01657
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29669). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.29669]] | https://huggingface.co/papers/2608.29669
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29692). Keywords: embedding, geometry. Status: pending-review.
- Source: [[papers/2608.29692]] | https://huggingface.co/papers/2608.29692
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00968). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2609.00968]] | https://huggingface.co/papers/2609.00968
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01560). Keywords: world model. Status: pending-review.
- Source: [[papers/2609.01560]] | https://huggingface.co/papers/2609.01560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00188). Keywords: world model. Status: pending-review.
- Source: [[papers/2609.00188]] | https://huggingface.co/papers/2609.00188
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24293). Keywords: variational, diffusion, vae. Status: pending-review.
- Source: [[papers/2608.24293]] | https://huggingface.co/papers/2608.24293
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30530). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.30530]] | https://huggingface.co/papers/2608.30530
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31106). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.31106]] | https://huggingface.co/papers/2608.31106
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30795). Keywords: probabilistic. Status: pending-review.
- Source: [[papers/2608.30795]] | https://huggingface.co/papers/2608.30795
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29974). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.29974]] | https://huggingface.co/papers/2608.29974
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28460). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.28460]] | https://huggingface.co/papers/2608.28460
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26794). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.26794]] | https://huggingface.co/papers/2608.26794
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18524). Keywords: topology. Status: pending-review.
- Source: [[papers/2608.18524]] | https://huggingface.co/papers/2608.18524
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28122). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.28122]] | https://huggingface.co/papers/2608.28122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23149). Keywords: manifold. Status: pending-review.
- Source: [[papers/2608.23149]] | https://huggingface.co/papers/2608.23149
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25375). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.25375]] | https://huggingface.co/papers/2608.25375
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23943). Keywords: variational, geometry. Status: pending-review.
- Source: [[papers/2608.23943]] | https://huggingface.co/papers/2608.23943
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21832). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.21832]] | https://huggingface.co/papers/2608.21832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27168). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.27168]] | https://huggingface.co/papers/2608.27168
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27345). Keywords: probabilistic, world model. Status: pending-review.
- Source: [[papers/2608.27345]] | https://huggingface.co/papers/2608.27345
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25500). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2608.25500]] | https://huggingface.co/papers/2608.25500
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26200). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.26200]] | https://huggingface.co/papers/2608.26200
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25518). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.25518]] | https://huggingface.co/papers/2608.25518
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23918). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.23918]] | https://huggingface.co/papers/2608.23918
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25927). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.25927]] | https://huggingface.co/papers/2608.25927
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19556). Keywords: diffusion, geometry. Status: pending-review.
- Source: [[papers/2608.19556]] | https://huggingface.co/papers/2608.19556
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23383). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.23383]] | https://huggingface.co/papers/2608.23383
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22274). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.22274]] | https://huggingface.co/papers/2608.22274
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24053). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.24053]] | https://huggingface.co/papers/2608.24053
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24680). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.24680]] | https://huggingface.co/papers/2608.24680
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24763). Keywords: topology. Status: pending-review.
- Source: [[papers/2608.24763]] | https://huggingface.co/papers/2608.24763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23670). Keywords: topology. Status: pending-review.
- Source: [[papers/2608.23670]] | https://huggingface.co/papers/2608.23670
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21439). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.21439]] | https://huggingface.co/papers/2608.21439
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23565). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.23565]] | https://huggingface.co/papers/2608.23565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16812). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.16812]] | https://huggingface.co/papers/2608.16812
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19567). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.19567]] | https://huggingface.co/papers/2608.19567
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23189). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.23189]] | https://huggingface.co/papers/2608.23189
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22849). Keywords: diffusion, representation learning. Status: pending-review.
- Source: [[papers/2608.22849]] | https://huggingface.co/papers/2608.22849
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23392). Keywords: representation learning. Status: pending-review.
- Source: [[papers/2608.23392]] | https://huggingface.co/papers/2608.23392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22591). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.22591]] | https://huggingface.co/papers/2608.22591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21486). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.21486]] | https://huggingface.co/papers/2608.21486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23252). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.23252]] | https://huggingface.co/papers/2608.23252
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20886). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.20886]] | https://huggingface.co/papers/2608.20886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08676). Keywords: vae, embedding. Status: pending-review.
- Source: [[papers/2608.08676]] | https://huggingface.co/papers/2608.08676
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18184). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.18184]] | https://huggingface.co/papers/2608.18184
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18077). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.18077]] | https://huggingface.co/papers/2608.18077
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12875). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.12875]] | https://huggingface.co/papers/2608.12875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15767). Keywords: probabilistic. Status: pending-review.
- Source: [[papers/2608.15767]] | https://huggingface.co/papers/2608.15767
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16490). Keywords: generative model, geometry. Status: pending-review.
- Source: [[papers/2608.16490]] | https://huggingface.co/papers/2608.16490
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20336). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.20336]] | https://huggingface.co/papers/2608.20336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14022). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.14022]] | https://huggingface.co/papers/2608.14022
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20335). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.20335]] | https://huggingface.co/papers/2608.20335
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19863). Keywords: representation learning, embedding. Status: pending-review.
- Source: [[papers/2608.19863]] | https://huggingface.co/papers/2608.19863
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19776). Keywords: manifold, geometry, topology. Status: pending-review.
- Source: [[papers/2608.19776]] | https://huggingface.co/papers/2608.19776
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19759). Keywords: generative model, geometry. Status: pending-review.
- Source: [[papers/2608.19759]] | https://huggingface.co/papers/2608.19759
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18701). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.18701]] | https://huggingface.co/papers/2608.18701
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18746). Keywords: world model, geometry. Status: pending-review.
- Source: [[papers/2608.18746]] | https://huggingface.co/papers/2608.18746
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15869). Keywords: world model, embedding. Status: pending-review.
- Source: [[papers/2608.15869]] | https://huggingface.co/papers/2608.15869
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17975). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.17975]] | https://huggingface.co/papers/2608.17975
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17988). Keywords: vae, geometry. Status: pending-review.
- Source: [[papers/2608.17988]] | https://huggingface.co/papers/2608.17988
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18076). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.18076]] | https://huggingface.co/papers/2608.18076
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05811). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.05811]] | https://huggingface.co/papers/2608.05811
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18063). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.18063]] | https://huggingface.co/papers/2608.18063
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14036). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.14036]] | https://huggingface.co/papers/2608.14036
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16793). Keywords: variational, diffusion, vae. Status: pending-review.
- Source: [[papers/2608.16793]] | https://huggingface.co/papers/2608.16793
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17067). Keywords: generative model, contrastive. Status: pending-review.
- Source: [[papers/2608.17067]] | https://huggingface.co/papers/2608.17067
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13556). Keywords: generative model, vae. Status: pending-review.
- Source: [[papers/2608.13556]] | https://huggingface.co/papers/2608.13556
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12944). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.12944]] | https://huggingface.co/papers/2608.12944
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12898). Keywords: representation learning. Status: pending-review.
- Source: [[papers/2608.12898]] | https://huggingface.co/papers/2608.12898
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16887). Keywords: generative model, diffusion. Status: pending-review.
- Source: [[papers/2608.16887]] | https://huggingface.co/papers/2608.16887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16859). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.16859]] | https://huggingface.co/papers/2608.16859
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15022). Keywords: latent variable. Status: pending-review.
- Source: [[papers/2608.15022]] | https://huggingface.co/papers/2608.15022
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16143). Keywords: diffusion, embedding. Status: pending-review.
- Source: [[papers/2608.16143]] | https://huggingface.co/papers/2608.16143
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16485). Keywords: embedding, manifold, geometry, topology. Status: pending-review.
- Source: [[papers/2608.16485]] | https://huggingface.co/papers/2608.16485
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15037). Keywords: manifold. Status: pending-review.
- Source: [[papers/2608.15037]] | https://huggingface.co/papers/2608.15037
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15659). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.15659]] | https://huggingface.co/papers/2608.15659
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15669). Keywords: bayesian, generative model. Status: pending-review.
- Source: [[papers/2608.15669]] | https://huggingface.co/papers/2608.15669
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14530). Keywords: diffusion, world model, geometry. Status: pending-review.
- Source: [[papers/2608.14530]] | https://huggingface.co/papers/2608.14530
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14138). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.14138]] | https://huggingface.co/papers/2608.14138
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12209). Keywords: diffusion, representation learning, embedding. Status: pending-review.
- Source: [[papers/2608.12209]] | https://huggingface.co/papers/2608.12209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09928). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.09928]] | https://huggingface.co/papers/2608.09928
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10835). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.10835]] | https://huggingface.co/papers/2608.10835
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09926). Keywords: diffusion, world model. Status: pending-review.
- Source: [[papers/2608.09926]] | https://huggingface.co/papers/2608.09926
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11045). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.11045]] | https://huggingface.co/papers/2608.11045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12836). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.12836]] | https://huggingface.co/papers/2608.12836
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13546). Keywords: world model, geometry. Status: pending-review.
- Source: [[papers/2608.13546]] | https://huggingface.co/papers/2608.13546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08888). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.08888]] | https://huggingface.co/papers/2608.08888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13489). Keywords: world model, geometry. Status: pending-review.
- Source: [[papers/2608.13489]] | https://huggingface.co/papers/2608.13489
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13049). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.13049]] | https://huggingface.co/papers/2608.13049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11745). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.11745]] | https://huggingface.co/papers/2608.11745
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11752). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.11752]] | https://huggingface.co/papers/2608.11752
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11951). Keywords: variational, generative model. Status: pending-review.
- Source: [[papers/2608.11951]] | https://huggingface.co/papers/2608.11951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12997). Keywords: diffusion, vae. Status: pending-review.
- Source: [[papers/2608.12997]] | https://huggingface.co/papers/2608.12997
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12313). Keywords: representation learning. Status: pending-review.
- Source: [[papers/2608.12313]] | https://huggingface.co/papers/2608.12313
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12314). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.12314]] | https://huggingface.co/papers/2608.12314
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11216). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.11216]] | https://huggingface.co/papers/2608.11216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11562). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.11562]] | https://huggingface.co/papers/2608.11562
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10708). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.10708]] | https://huggingface.co/papers/2608.10708
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06729). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.06729]] | https://huggingface.co/papers/2608.06729
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00677). Keywords: markov. Status: pending-review.
- Source: [[papers/2608.00677]] | https://huggingface.co/papers/2608.00677
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10615). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.10615]] | https://huggingface.co/papers/2608.10615
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09805). Keywords: variational. Status: pending-review.
- Source: [[papers/2608.09805]] | https://huggingface.co/papers/2608.09805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08786). Keywords: symbolic, neuro-symbolic. Status: pending-review.
- Source: [[papers/2608.08786]] | https://huggingface.co/papers/2608.08786
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08156). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2608.08156]] | https://huggingface.co/papers/2608.08156
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07463). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.07463]] | https://huggingface.co/papers/2608.07463
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06111). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.06111]] | https://huggingface.co/papers/2608.06111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10744). Keywords: variational, diffusion, vae, geometry. Status: pending-review.
- Source: [[papers/2608.10744]] | https://huggingface.co/papers/2608.10744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10915). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.10915]] | https://huggingface.co/papers/2608.10915
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11205). Keywords: diffusion, geometry. Status: pending-review.
- Source: [[papers/2608.11205]] | https://huggingface.co/papers/2608.11205
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08786). Keywords: symbolic, neuro-symbolic. Status: pending-review.
- Source: [[papers/2608.08786]] | https://huggingface.co/papers/2608.08786
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08156). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2608.08156]] | https://huggingface.co/papers/2608.08156
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07408). Keywords: world model, embedding. Status: pending-review.
- Source: [[papers/2608.07408]] | https://huggingface.co/papers/2608.07408
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05597). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.05597]] | https://huggingface.co/papers/2608.05597
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00675). Keywords: generative model, diffusion. Status: pending-review.
- Source: [[papers/2608.00675]] | https://huggingface.co/papers/2608.00675
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01310). Keywords: contrastive, embedding. Status: pending-review.
- Source: [[papers/2608.01310]] | https://huggingface.co/papers/2608.01310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04569). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.04569]] | https://huggingface.co/papers/2608.04569
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05798). Keywords: generative model, diffusion, vae. Status: pending-review.
- Source: [[papers/2608.05798]] | https://huggingface.co/papers/2608.05798
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01049). Keywords: world model, embedding. Status: pending-review.
- Source: [[papers/2608.01049]] | https://huggingface.co/papers/2608.01049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04378). Keywords: symbolic, world model, embedding. Status: pending-review.
- Source: [[papers/2608.04378]] | https://huggingface.co/papers/2608.04378
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05987). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2608.05987]] | https://huggingface.co/papers/2608.05987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06352). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2608.06352]] | https://huggingface.co/papers/2608.06352
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06197). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.06197]] | https://huggingface.co/papers/2608.06197
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06257). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.06257]] | https://huggingface.co/papers/2608.06257
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06020). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.06020]] | https://huggingface.co/papers/2608.06020
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05785). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.05785]] | https://huggingface.co/papers/2608.05785
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01481). Keywords: embedding, geometry. Status: pending-review.
- Source: [[papers/2608.01481]] | https://huggingface.co/papers/2608.01481
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03506). Keywords: symbolic, bayesian. Status: pending-review.
- Source: [[papers/2608.03506]] | https://huggingface.co/papers/2608.03506
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.22143). Keywords: generative model. Status: pending-review.
- Source: [[papers/2607.22143]] | https://huggingface.co/papers/2607.22143
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05070). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.05070]] | https://huggingface.co/papers/2608.05070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04701). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.04701]] | https://huggingface.co/papers/2608.04701
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28048). Keywords: contrastive. Status: pending-review.
- Source: [[papers/2607.28048]] | https://huggingface.co/papers/2607.28048
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04964). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.04964]] | https://huggingface.co/papers/2608.04964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04926). Keywords: representation learning. Status: pending-review.
- Source: [[papers/2608.04926]] | https://huggingface.co/papers/2608.04926
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03207). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.03207]] | https://huggingface.co/papers/2608.03207
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02437). Keywords: geometry. Status: pending-review.
- Source: [[papers/2608.02437]] | https://huggingface.co/papers/2608.02437
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03316). Keywords: vae. Status: pending-review.
- Source: [[papers/2608.03316]] | https://huggingface.co/papers/2608.03316
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03971). Keywords: generative model. Status: pending-review.
- Source: [[papers/2608.03971]] | https://huggingface.co/papers/2608.03971
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02711). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.02711]] | https://huggingface.co/papers/2608.02711
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03974). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.03974]] | https://huggingface.co/papers/2608.03974
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02738). Keywords: embedding, geometry. Status: pending-review.
- Source: [[papers/2608.02738]] | https://huggingface.co/papers/2608.02738
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02713). Keywords: world model. Status: pending-review.
- Source: [[papers/2608.02713]] | https://huggingface.co/papers/2608.02713
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28993). Keywords: vae. Status: pending-review.
- Source: [[papers/2607.28993]] | https://huggingface.co/papers/2607.28993
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00730). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.00730]] | https://huggingface.co/papers/2608.00730
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03457). Keywords: diffusion. Status: pending-review.
- Source: [[papers/2608.03457]] | https://huggingface.co/papers/2608.03457
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01127). Keywords: diffusion, vae, world model. Status: pending-review.
- Source: [[papers/2608.01127]] | https://huggingface.co/papers/2608.01127
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02791). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.02791]] | https://huggingface.co/papers/2608.02791
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03507). Keywords: embedding. Status: pending-review.
- Source: [[papers/2608.03507]] | https://huggingface.co/papers/2608.03507
- Confidence: Low (auto-matched, not yet reviewed)
- Source: [[loop-engineering.md]]
- Confidence: Low
06.14249
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28805). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2605.28805]] | https://huggingface.co/papers/2605.28805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.06392). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2604.06392]] | https://huggingface.co/papers/2604.06392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.25111). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2603.25111]] | https://huggingface.co/papers/2603.25111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.15670). Keywords: probabilistic, variational. Status: pending-review.
- Source: [[papers/2603.15670]] | https://huggingface.co/papers/2603.15670
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.02208). Keywords: symbolic, bayesian. Status: pending-review.
- Source: [[papers/2603.02208]] | https://huggingface.co/papers/2603.02208
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.09443). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2602.09443]] | https://huggingface.co/papers/2602.09443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06130). Keywords: variational. Status: pending-review.
- Source: [[papers/2602.06130]] | https://huggingface.co/papers/2602.06130
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06030). Keywords: symbolic, neuro-symbolic. Status: pending-review.
- Source: [[papers/2602.06030]] | https://huggingface.co/papers/2602.06030
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.15690). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2601.15690]] | https://huggingface.co/papers/2601.15690
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05049). Keywords: variational. Status: pending-review.
- Source: [[papers/2512.05049]] | https://huggingface.co/papers/2512.05049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.12797). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2511.12797]] | https://huggingface.co/papers/2511.12797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.23925). Keywords: bayesian, variational. Status: pending-review.
- Source: [[papers/2510.23925]] | https://huggingface.co/papers/2510.23925
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.12269). Keywords: symbolic, graphical model. Status: pending-review.
- Source: [[papers/2510.12269]] | https://huggingface.co/papers/2510.12269
- Confidence: Low (auto-matched, not yet reviewed)
  Reasoning L
- HF trending paper (arxiv: 2510.01037). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2510.01037]] | https://huggingface.co/papers/2510.01037
- Confidence: Low (auto-matched, not yet reviewed)
  Neural Ne
- HF trending paper (arxiv: 2508.18921). Keywords: probabilistic. Status: pending-review.
- Source: [[papers/2508.18921]] | https://huggingface.co/papers/2508.18921
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.08093). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2607.08093]] | https://huggingface.co/papers/2607.08093
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05369). Keywords: variational. Status: pending-review.
- Source: [[papers/2607.05369]] | https://huggingface.co/papers/2607.05369
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05391). Keywords: probabilistic. Status: pending-review.
- Source: [[papers/2607.05391]] | https://huggingface.co/papers/2607.05391
- Confidence: Low (auto-matched, not yet reviewed)
  Foundati
- HF trending paper (arxiv: 2507.00951). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2507.00951]] | https://huggingface.co/papers/2507.00951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.31036). Keywords: bayesian. Status: pending-review.
- Source: [[papers/2606.31036]] | https://huggingface.co/papers/2606.31036
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.00924). Keywords: symbolic. Status: pending-review.
- Source: [[papers/2607.00924]] | https://huggingface.co/papers/2607.00924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26004). Keywords: variational. Status: pending-review.
- Source: [[papers/2607.26004]] | https://huggingface.co/papers/2607.26004
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25108). Keywords: probabilistic. Status: pending-review.
- Source: [[papers/2607.25108]] | https://huggingface.co/papers/2607.25108
- Confidence: Low (auto-matched, not yet reviewed)
- CWM maps to finance: encode market rules as executable code, use classical solvers for equilibrium computation. Synthesis shows application to autoresearch (experiment as game), meta-critic (strategy as multi-armed bandit), structured execution (adversarial critic as zero-sum game).
- Source: [[wiki/synthesis/cwm-game-theory-application]]
- Confidence: Medium
