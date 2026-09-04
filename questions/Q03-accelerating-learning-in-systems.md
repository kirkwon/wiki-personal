---
tags: [permanent-question, research]
created: 2026-05-25
question: "What approaches meaningfully accelerate learning — curriculum learning, active learning, knowledge distillation, continual learning, few-shot adaptation? What tradeoffs matter?"
date: 2026-05-25
type: permanent-question
reviewed: 2026-09-02
confidence: 0.95
evidence_count: 496
last_evidence_date: 2026-09-01
---


# Q03: Accelerating Learning in Systems

**Status:** Active - accumulating

## Question
*What approaches meaningfully accelerate learning — curriculum learning, active learning, knowledge distillation, continual learning, few-shot adaptation? What tradeoffs matter?*

## Current State of Knowledge

### 1. Active Learning (Learn What Matters)
- **Core idea**: Instead of training on random data, the model asks for labels on the most uncertain/important examples
- **Finance applicability**: Labeled financial data is expensive (requires expert annotation or real-world consequences). Active learning maximizes signal per label.
- **Use case**: If you have a small labeled dataset of insider trading signals, use active learning to pick the most informative cases first
- **Limitation**: Requires a model that can express uncertainty (Bayesian methods, ensembles)

### 2. Curriculum Learning (Start Simple, Grow Complex)
- **Core idea**: Train on easy examples first, then progressively harder ones
- **Evidence**: Works well in RL (starting with simple environments), less clear in supervised learning
- **In Finance**: Start with regime-predictable periods, then add edge cases. Or start with simple features, add complex ones.
- **Related**: Self-paced learning — model controls its own curriculum

### 3. Knowledge Distillation (Learn from a Bigger Model)
- **Core idea**: Train a small model to mimic a large model's soft predictions
- **In Finance**: Use a large model ( GPT-4 ) to generate synthetic labels or pseudo-labels for a smaller, faster model
- **Evidence**: Works. Distilled BERT models (DistilBERT) retain 97% performance with 60% less compute
- **Key tradeoff**: The small model is faster but less expressive. Useful for real-time inference.

### 4. Transfer Learning (Leverage Pretraining)
- **Core idea**: Pretrain on large related dataset, fine-tune on small target dataset
- **In Finance**: Pretrain on broad market data, fine-tune on specific asset class or strategy
- **Problem**: Markets are non-stationary. Pretrained patterns may not transfer across regimes.
- **Better approach**: Domain-adaptive pretraining (continue pretraining on in-domain corpus)

### 5. Few-Shot / Zero-Shot (Learn from Description)
- **Core idea**: Give model task description + few examples in context, no weight updates needed
- **In Finance**: Describe a new anomaly detection task in natural language, model applies it
- **Limitation**: Few-shot works for general reasoning, less reliable for precise numerical tasks
- **Use case**: Good for ideation, hypothesis generation, not for live trading signals

### 6. Continual Learning (Learn Without Forgetting)
- **Core idea**: System learns sequential tasks without catastrophic forgetting
- **In Finance**: Model needs to learn new regimes (2020 COVID, 2022 rates) without forgetting 2008
- **Methods**: 
  - Elastic Weight Consolidation (EWC) — protect important weights from previous tasks
  - Rehearsal — store exemplars of previous tasks
  - Progressive neural networks — add new columns for new tasks
- **Real problem**: In finance, old regimes matter. A model that forgets 2008 is dangerous.

### 7. Causal Inference Acceleration
- Using causal graphs to reduce the sample complexity of learning
- Instead of learning everything from data, encode causal structure and learn only the causal mechanisms
- Potentially huge efficiency gains if the causal structure is known

## Key Papers
- Settles — "Active Learning Literature Survey" (comprehensive review)
- Bengio et al. — "Curriculum Learning" (2009, original curriculum learning)
- Hinton et al. — "Distilling the Knowledge in a Neural Network" (2015, distillation)
- Kirkpatrick et al. — "Overcoming Catastrophic Forgetting in NNs" (EWC)

## Emerging Methodology

For a personal system learning about finance:
- **Active learning is underutilized**: Most quants label data randomly. Systematic active learning would dramatically improve signal.
- **Causal inference + ML** is the highest-leverage combination: Use domain knowledge to constrain what causal structures are possible, then ML learns the rest.
- **Distillation** is practical: Use a frontier model to generate insights, distill into faster local models.
- **Continual learning** matters: Build explicit regime memory so the system knows when conditions change.

### Loop Engineering & Agent Systems
- **`/goal` primitive (run-until-done)**: Long-running agent tasks that persist through interruptions, enabling autonomous research and iteration loops without manual restart.
- **Loop engineering automation**: Systematically building feedback loops (observe → decide → act → learn) into agent workflows so each cycle improves the next.
- **Triage inbox feedback loop**: A persistent inbox where raw inputs (ideas, errors, observations) are triaged, prioritized, and fed back into the learning system — closing the loop between discovery and action.
- **Skill auto-patch from learning**: When an agent learns something new, the skill file itself is patched to encode that knowledge permanently — the system improves its own capabilities over time.

### LLM-as-Compiler — Learning Acceleration via Externalization

The [[concepts/llm-as-compiler|LLM-as-Compiler]] pattern (Lehrach et al., 2025, DeepMind) reframes LLMs from direct actors to translators — converting natural language specifications into executable code, then handing off to classical solvers. This is a novel **learning acceleration technique**:

- **Learning via externalization**: Instead of the LLM *learning* to reason (probabilistic, slow, unverifiable), it *compiles* the reasoning task into executable code (deterministic, fast, verifiable)
- **Eliminates CoT's core weakness**: Chain-of-Thought is probabilistic and unverifiable — the LLM might make an arithmetic error on step 3. CWM's reasoning is deterministic and verifiable — the code either runs correctly or doesn't
- **Generalization without weight updates**: The LLM doesn't need to have seen the domain — it needs to understand the rules and express them as code. This is few-shot learning without the "learned from examples" step

See [[concepts/code-world-models]], [[concepts/verifiable-planning]], [[papers/code-world-models-general-game-playing]].

## Connections
- [[Q02]] — accelerated learning feeds self-improvement
- [[Q01]] — these techniques reduce the skills gap
- [[loop-engineering]] — core methodology for building learning loops into agent systems
- [[methodology-loop]] — meta-loop that governs how methodology evolves through usage
- [[concepts/llm-as-compiler]] — LLM-as-compiler as learning acceleration via externalization
- [[concepts/code-world-models]] — CWM pattern for learning transfer through code generation
- [[concepts/verifiable-planning]] — verifiability eliminates probabilistic learning errors

## Last Updated
_2026-06-24_ — Added LLM-as-Compiler / Code World Models section: learning acceleration via externalization. Updated Connections with new references.
_2026-05-25_ — Initial research position
_2026-06-13_ — Added loop engineering / agent systems methodology, updated status to Active - accumulating, added [[loop-engineering]] and [[methodology-loop]] connections

## Evidence Log

<!-- Weekly scan appends dated evidence blocks below this line.
     Format: ### YYYY-MM-DD: <topic>
             - Finding
             - Source: [[wikilink]] or URL
             - Confidence: High/Medium/Low
-->

### 2026-06-12: Loop engineering — observation → hypothesis → eval → reflect cycles
- Loop rate (iterations per day) is the key metric for learning velocity. Faster loops = faster discovery. Applied to strategy optimization, dashboard debugging, feature engineering.
- Source: [[loop-engineering]]
- Confidence: Medium

### 2026-06-13: Headroom compression enables larger context windows

### 2026-07-30: SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

### 2026-07-30: CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Ac

### 2026-07-30: CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization

### 2026-07-30: SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution

### 2026-07-30: GPT-Red: Automated Red Teaming via Self-Play at Scale

### 2026-07-30: OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedi

### 2026-07-01: TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

### 2026-07-01: Hierarchical Experimentalist Agents

### 2026-07-02: Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Gene

### 2026-07-02: Personalization as Inverse Planning: Learning Latent Design Intents for Agentic 

### 2026-07-03: Transferability for General Reasoning: An Automated Curriculum for Multi-Domain 

### 2026-07-03: Parameter-Efficient Quantum-Inspired Fast Weight Programmers for Traffic-Matrix 

### 2025-07-01: SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via

### 2026-07-06: Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care

### 2025-07-02: Thinking Beyond Tokens: From Brain-Inspired Intelligence to Cognitive

### 2026-07-07: LLM-as-a-Verifier: A General-Purpose Verification Framework

### 2025-07-11: Machine Bullshit: Characterizing the Emergent Disregard for Truth in

### 2026-07-07: GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automat

### 2026-07-08: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Paramete

### 2025-08-07: SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from

### 2026-07-09: Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

### 2025-08-14: Learning to Align, Aligning to Learn: A Unified Approach for

### 2025-08-19: Ovis2.5 Technical Report

### 2025-08-27: Forecasting Probability Distributions of Financial Returns with Deep

### 2026-07-15: Towards Autonomous and Auditable Medical Imaging Model Development

### 2025-09-03: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

### 2026-07-16: Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

### 2025-09-03: VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use

### 2026-07-16: KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Ev

### 2025-09-08: Bootstrapping Task Spaces for Self-Improvement

### 2025-09-09: Reinforcement Learning Foundations for Deep Research Systems: A Survey

### 2026-07-17: SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

### 2026-07-20: Understanding Reasoning from Pretraining to Post-Training

### 2026-07-20: When Does Muon Help Agentic Reinforcement Learning?

### 2025-09-26: UserRL: Training Interactive User-Centric Agent via Reinforcement

### 2026-07-20: SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcem

### 2025-09-29: Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive

### 2026-07-21: Masked Diffusion Language Models are Strong and Steerable Text-Based World Model

### 2025-09-29: WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level

### 2026-07-24: AREX: Towards a Recursively Self-Improving Agent for Deep Research

### 2025-10-01: Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified

### 2025-10-02: CurES: From Gradient Analysis to Efficient Curriculum Learning for

### 2026-07-27: Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Lea

### 2026-07-28: From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent P

### 2026-07-28: The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-train

### 2025-10-03: TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis

### 2026-07-28: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social

### 2025-10-06: Free Lunch Alignment of Text-to-Image Diffusion Models without

### 2025-10-07: AdvEvo-MARL: Shaping Internalized Safety through Adversarial

### 2025-10-08: Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and

### 2025-10-08: Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for

### 2025-10-08: A Contextual Quality Reward Model for Reliable and Efficient Best-of-N

### 2025-10-14: Self-Improving LLM Agents at Test-Time

### 2025-10-15: Tensor Logic: The Language of AI

### 2025-10-16: Stronger Together: On-Policy Reinforcement Learning for Collaborative

### 2025-10-21: Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native

### 2025-10-22: AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement

### 2025-10-28: Code Aesthetics with Agentic Reward Feedback

### 2025-10-29: SPICE: Self-Play In Corpus Environments Improves Reasoning

### 2025-10-29: FunReason-MT Technical Report: Overcoming the Complexity Barrier in

### 2025-10-29: Latent Chain-of-Thought for Visual Reasoning

### 2025-11-07: Scaling Agent Learning via Experience Synthesis

### 2025-11-13: WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

### 2025-11-18: Genomic Next-Token Predictors are In-Context Learners

### 2025-12-05: SIMA 2: A Generalist Embodied Agent for Virtual Worlds

### 2025-12-05: QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory

### 2025-12-10: TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion Models

### 2025-12-11: Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware ROI Pred

### 2025-12-24: Reinforcement Learning for Self-Improving Agent with Skill Library

### 2026-01-08: MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecula

### 2026-01-15: The AI Hippocampus: How Far are We From Human Memory?

### 2026-01-22: Agentic Reasoning for Large Language Models

### 2026-01-23: From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantific

### 2026-01-27: Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability

### 2026-01-29: Reinforcement Learning via Self-Distillation

### 2026-01-30: Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs v

### 2026-02-09: Self-Improving World Modelling with Latent Actions

### 2026-02-10: AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

### 2026-02-11: P1-VL: Bridging Visual Perception
### 2026-08-05: Autonomous email triage with Bayesian sender trust, SPF/DKIM/DMARC authentication gate, and centralized safety reference for fraud, theft, and identity leakage.
- Source: [[email-safety-system.md]]
- Confidence: Medium

### 2026-08-05: Centralized blog draft pipeline: 2 active drafts, 12 verified candidates across 3 tiers, organized into thematic series.
- Source: [[blog-content-pipeline.md]]
- Confidence: Medium

### 2026-08-05: Self-maintaining personal knowledge graph: ~19,800 pages, 8 ingestion pipelines, cron-driven sync across GBrain + NotebookLM + Obsidian wiki.
- Source: [[gbrain-knowledge-ecosystem.md]]
- Confidence: Medium

### 2026-08-05: > **Skill stub** — auto-generated by knowledge-maintenance on 2026-08-02.
- Source: [[agent-subsystem-build.md]]
- Confidence: Medium

### 2026-08-05: Loop engineering is the practice of structuring agent improvement as a closed-loop system with a **critic/doer separation** — one component acts, another validates. This separation enables the agent t...
- Source: [[loop-engineering.md]]
- Confidence: Low

### 2026-08-05: Three interconnected skill systems: (1) **Book Skills Dashboard** — interactive HTML visualization of 303 skills/concepts from 33 books with D3.js network graphs, (2) **Hermes Skills Library** — 320 i...
- Source: [[skills-ecosystem.md]]
- Confidence: Low

### 2026-08-05: Designing self-running agent loops: heartbeat, SKILL.md, state files, verifiers, worktrees, MCP — transitioning from prompting to engineering autonomous systems.
- Source: [[loop-engineering.md]]
- Confidence: High
 and Scientific Reasoning in Physics Olympiads

### 2026-02-11: Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems

### 2026-02-12: Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters

### 2026-02-20: Discovering Multiagent Learning Algorithms with Large Language Models

### 2026-03-03: Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data

### 2026-03-03: Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-tra

### 2026-03-12: Meissa: Multi-modal Medical Agentic Intelligence

### 2026-03-18: FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use

### 2026-03-18: I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Prob

### 2026-03-24: Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large 

### 2026-04-02: QuitoBench: A High-Quality Open Time Series Forecasting Benchmark

### 2026-04-03: Brainstacks: Cross-Domain Cognitive Capabilities via Frozen MoE-LoRA Stacks for 

### 2026-04-06: GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic Re

### 2026-04-07: Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning fro

### 2026-04-09: SEVerA: Verified Synthesis of Self-Evolving Agents

### 2026-04-09: Qualixar OS: A Universal Operating System for AI Agent Orchestration

### 2026-04-09: AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement Learning

### 2026-04-10: Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

### 2026-04-14: TRACE: Capability-Targeted Agentic Training

### 2026-04-14: Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and

### 2026-04-22: HP-Edit: A Human-Preference Post-Training Framework for Image Editing

### 2026-05-01: Synthetic Computers at Scale for Long-Horizon Productivity Simulation

### 2026-05-06: ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

### 2026-05-06: Healthcare AI GYM for Medical Agents

### 2026-05-07: OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

### 2026-05-11: InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search

### 2026-05-12: G-Zero: Self-Play for Open-Ended Generation from Zero Data

### 2026-05-12: AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Syst

### 2026-05-19: Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces

### 2026-05-20: CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization

### 2026-05-26: ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Rei

### 2026-05-26: ECHO: Terminal Agents Learn World Models for Free

### 2026-05-28: OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

### 2026-05-29: Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Ge

### 2026-06-03: Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories

### 2026-06-03: Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment 

### 2026-06-05: EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Conte

### 2026-06-08: CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

### 2026-06-11: EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agent

### 2026-06-15: From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomo

### 2026-06-15: HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

### 2026-06-15: Orchestra-o1: Omnimodal Agent Orchestration

### 2026-06-15: StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning

### 2026-06-16: Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Mo

### 2026-06-18: STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Sta

### 2026-06-19: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

### 2026-06-23: Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

### 2026-06-26: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents

### 2026-07-01: TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

### 2026-07-01: Hierarchical Experimentalist Agents

### 2026-07-07: LLM-as-a-Verifier: A General-Purpose Verification Framework

### 2026-07-07: GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automat

### 2026-07-08: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Paramete

### 2026-07-16: KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Ev

### 2026-07-17: SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

### 2026-07-24: AREX: Towards a Recursively Self-Improving Agent for Deep Research

### 2026-07-28: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social

### 2026-07-31: INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models

### 2026-07-31: Can Large Language Models Execute Parent Orders?

### 2026-07-31: Beacon: Knowing When and How to Perform Agentic Visual Reasoning

### 2026-08-03: SAF-OPD: Stable Advantage Fusion for On-Policy Distillation

### 2026-08-03: RL^2-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for V

### 2026-08-03: Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocat

### 2026-08-03: SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle Autonom

### 2026-08-03: ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

### 2026-08-03: Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Mo

### 2026-08-03: SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark fo

### 2026-08-03: Enhancing Rubric-based RL via Self-Distillation

### 2026-08-03: Evaluation-Verification Reward for Consistent Multi-Reference Image Editing

### 2026-08-03: Meshy T2: Fast Native Mesh Generation with Flow Matching

### 2026-08-03: N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Token

### 2026-08-03: From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open

### 2026-08-03: AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

### 2026-08-03: β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation

### 2026-08-03: Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts 

### 2026-08-03: Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential A

### 2026-08-03: Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainabil

### 2026-08-03: ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamic

### 2026-08-03: AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emot

### 2026-08-03: LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structure

### 2026-08-03: Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generati

### 2026-08-03: BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms

### 2026-08-04: Seeing or Knowing? Visual Context Sensitivity in Multimodal Large Language Model

### 2026-08-04: ICDAR 2026 Competition on Information Extraction from Atomic Layer Deposition/Et

### 2026-08-04: A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples

### 2026-08-04: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

### 2026-08-04: RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender System

### 2026-08-04: GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Ti

### 2026-08-04: Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language

### 2026-08-04: DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimo

### 2026-08-04: 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question 

### 2026-08-04: LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks

### 2026-08-04: Progressive Agent Skill Generation via Reinforcement Learning

### 2026-08-04: SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation

### 2026-08-04: UEmbed: Unified Sparse and Dense Multimodal Embeddings

### 2026-08-04: Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis

### 2026-08-04: SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zer

### 2026-08-04: WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

### 2026-08-04: StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph

### 2026-08-04: ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to 

### 2026-08-04: Roomer: Reflective Object-Grounded Model Editing and Repair for 3D Indoor Layout

### 2026-08-04: Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous 

### 2026-08-04: Weak-to-Strong On-Policy Distillation

### 2026-08-04: Constitutional Midtraining: Content Presence Drives Alignment Gains

### 2026-08-05: RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic KV Cac

### 2026-08-05: ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Lev

### 2026-08-05: Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-B

### 2026-08-05: ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

### 2026-08-05: LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

### 2026-08-05: Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

### 2026-08-05: Quo Vadis, World Modeling?

### 2026-08-05: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Lear

### 2026-08-05: TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

### 2026-08-05: SkillJack: Persistent Skill Backdoors in Self-Evolving Agents

### 2026-08-05: UniWorld-Design: From Pixel Generation to Layer-Native Design

### 2026-08-05: MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Ope

### 2026-08-05: GROVE: Growing and Reasoning over Temporally Stratified Memory from Streaming Vi

### 2026-08-05: MemSFT: Mitigating Alignment Tax with an External Parametric Memory

### 2026-08-05: Wnuan: Staged Post-Training for Question Answering over Proprietary Enterprise K

### 2026-08-06: ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assi

### 2026-08-06: Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation Learnin

### 2026-08-06: Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data

### 2026-08-06: K-EXAONE 2.0 Technical Report

### 2026-08-06: Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from A

### 2026-08-06: BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Langua

### 2026-08-06: WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World 

### 2026-08-06: When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation

### 2026-08-06: The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monit

### 2026-08-06: Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horiz

### 2026-08-06: SKILL-KD: Contrastive Skill Distillation for LLM Agents

### 2026-08-06: UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models

### 2026-08-06: ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation

### 2026-08-06: Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Ear

### 2026-08-06: Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Sele

### 2026-08-06: HelloWorld: Enabling Socially Interactive Characters in Video World Models

### 2026-08-06: OPD-V: Visual On-Policy Self-Distillation with Modality Balance

### 2026-08-06: Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking

### 2026-08-06: When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K C

### 2026-08-06: ARCHead: Activation-Metric Residual Correction for Large Language Model Output H

### 2026-08-06: ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct R

### 2026-08-07: Continual Learning in Transition

### 2026-08-07: Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptati

### 2026-08-07: ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Con

### 2026-08-07: EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object R

### 2026-08-07: OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Re

### 2026-08-07: EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinf

### 2026-08-07: SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding

### 2026-08-07: CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

### 2026-08-07: AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

### 2026-08-07: WorldClaw: Agentic 3D Open-World Generation at Scale

### 2026-08-07: On-Policy Delta Distillation for Multilingual Math Reasoning

### 2026-08-07: HarnessOpt-Bench: Evaluating LLMs at Harness Optimization

### 2026-08-07: DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for C

### 2026-08-07: Recursive Synthesis for Long-Horizon Terminal Tasks

### 2026-08-07: Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised Wor

### 2026-08-08: GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splat

### 2026-08-08: KVAE: Family of Tokenizers for Multimodal Generative Models

### 2026-08-08: Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and 

### 2026-08-10: Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure Mode i

### 2026-08-10: FATE: Frame-Level Audio-Visual Temporal Embedding

### 2026-08-10: Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chun

### 2026-08-10: OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understandi

### 2026-08-10: Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence

### 2026-08-10: Towards Interpretable Foundation Models for Retinal Fundus Images

### 2026-08-10: Beyond Simply Environment Scaling: Designing Effective Environment Distributions

### 2026-08-10: SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task L

### 2026-08-10: Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning

### 2026-08-10: YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family

### 2026-08-10: SimWAM: A Simple World Action Model for End-to-End Autonomous Driving

### 2026-08-10: The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, an

### 2026-08-10: Modular TTT: Rethinking Test-Time Training as Composable Modules

### 2026-08-10: Skaling: Chinchilla's Exponents Meet Kaplan's Coupling

### 2026-08-11: Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under 

### 2026-08-11: SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification

### 2026-08-11: The Loss Does Not See the Basis, but Adam Does

### 2026-08-11: BDH-CQ: In-Context Learning with Recurrent Latent Reasoning

### 2026-08-11: CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems

### 2026-08-11: What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conve

### 2026-08-11: OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching

### 2026-08-11: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

### 2026-08-11: Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution

### 2026-08-12: InSight-doc: Agentic Visual Perception for Long-Document Understanding

### 2026-08-12: 360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents

### 2026-08-12: Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness

### 2026-08-12: UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models

### 2026-08-12: Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research A

### 2026-08-12: Reference-Free Post-Training of Open Large Language Models for Multilingual Mach

### 2026-08-12: iFAN: Inference-Aware Learning for Plain Mask Transformers

### 2026-08-12: TSDS-Toolbox: A Toolbox for Measuring Time-Series Dataset Similarity

### 2026-08-12: JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles

### 2026-08-12: SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discover

### 2026-08-12: Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Des

### 2026-08-12: DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Comp

### 2026-08-12: SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Pe

### 2026-08-12: VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World

### 2026-08-12: VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model w

### 2026-08-12: The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents

### 2026-08-12: Beyond Starry Night: Shortcut-Aware Control-State Planning for Artist-Grounded T

### 2026-08-12: On-Policy Self-Distillation without Any Supervision

### 2026-08-12: Omega-S: A Functional Resilience Index for LLM Fine-Tuning

### 2026-08-12: Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under 

### 2026-08-12: SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification

### 2026-08-12: The Loss Does Not See the Basis, but Adam Does

### 2026-08-12: BDH-CQ: In-Context Learning with Recurrent Latent Reasoning

### 2026-08-12: CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems

### 2026-08-12: What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conve

### 2026-08-12: OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching

### 2026-08-12: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

### 2026-08-13: Parameter Exploration for RLVR via Variational Learning

### 2026-08-13: Self-Evolving Embodied Agents via Skill-Harness Evolution

### 2026-08-13: AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models

### 2026-08-13: Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically 

### 2026-08-13: NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving MLLMs

### 2026-08-13: AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

### 2026-08-13: StateFlow: Building, Evolving, and Accessing 3D World States for Previsualizatio

### 2026-08-13: Agent Safety Should Be a Runtime Contract

### 2026-08-13: ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignme

### 2026-08-14: Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing

### 2026-08-14: AVA-Encoder: Towards Agent-Native Video Representation Learning

### 2026-08-14: TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation wi

### 2026-08-14: Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and 

### 2026-08-14: Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

### 2026-08-14: An AI4AI Framework for Visual Token Pruning

### 2026-08-14: SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in 

### 2026-08-14: UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

### 2026-08-14: H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Mo

### 2026-08-14: Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intellige

### 2026-08-14: DarwinX: Evolving Agent Harnesses Through Natural Selection

### 2026-08-14: AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

### 2026-08-14: LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-

### 2026-08-14: Full-bandwidth transformer

### 2026-08-14: Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

### 2026-08-14: Intern-S2-Preview: Scientific Agentic Foundation Model

### 2026-08-14: From Atomic Evidence to Logical Composition: Structured Compositional Reasoning 

### 2026-08-14: ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Fr

### 2026-08-14: Gaze Target Estimation Anywhere with Concepts

### 2026-08-14: Learning How the World Evolves: Extrapolative Video World Models via Latent Dyna

### 2026-08-15: Thought-Level Beam Search for Reasoning

### 2026-08-17: Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models

### 2026-08-17: A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientif

### 2026-08-17: SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Rea

### 2026-08-17: LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure

### 2026-08-17: UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Mu

### 2026-08-17: Second Thought: Reasoning in Parallel as LLM Agents Act and Observe

### 2026-08-17: MobileMem: Learning from a Year of Mobile Experiences

### 2026-08-17: Multimodal Model Diffing for Feature Discovery and Control

### 2026-08-17: CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Im

### 2026-08-17: Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Infe

### 2026-08-17: Verifier-Induced Support Reshaping in On-Policy Optimization

### 2026-08-17: SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Gen

### 2026-08-17: Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning

### 2026-08-18: Plausible but Not Valid: A Psychometric Audit of LLMs as Synthetic Survey Respon

### 2026-08-18: GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective 

### 2026-08-18: MOSS-VL Technical Report

### 2026-08-18: TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation

### 2026-08-18: WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Ri

### 2026-08-18: Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe Ac

### 2026-08-18: Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting f

### 2026-08-18: HiFi-BRep: High-Fidelity Latent Representation for Robust B-Rep Generation

### 2026-08-18: Drive, Pack, Fly: The Travelling Thief Problem with Drone

### 2026-08-18: AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation

### 2026-08-18: HarnessEval-W: Agentifying the Evaluation of Visual Worlds

### 2026-08-18: Improving the matrix multiplication exponent with modern optimization and AlphaE

### 2026-08-18: UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrati

### 2026-08-18: NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Docum

### 2026-08-18: Is this Citation on Point?

### 2026-08-18: Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped Tr

### 2026-08-19: PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture

### 2026-08-19: CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Represent

### 2026-08-19: DiSCO: Defending text-to-image generation through distribution-guided contrastiv

### 2026-08-19: EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing

### 2026-08-19: MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Ve

### 2026-08-19: Agent Lightning v1.0: Towards Harnessed Agentic RL

### 2026-08-19: FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution

### 2026-08-19: Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation

### 2026-08-19: Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents

### 2026-08-19: Energy-Guided Flow Matching

### 2026-08-19: From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Gen

### 2026-08-19: GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation

### 2026-08-19: Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Ind

### 2026-08-19: ASI-Bench: At the Dawn of Artificial Superintelligence

### 2026-08-19: aDSL: Agentic 3D Creation via Joint Agent-Program Design

### 2026-08-19: From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

### 2026-08-19: Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements

### 2026-08-19: Accuracy and Order Sensitivity Diverge Under Label-Free Strategies

### 2026-08-19: Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning

### 2026-08-20: The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning

### 2026-08-20: Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

### 2026-08-20: Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre E

### 2026-08-20: Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical In

### 2026-08-20: Training Leaves Traces: Centered Residual Signatures for Language Model Lineage 

### 2026-08-20: Training Chemical Plausibility-Aware Large Language Models for Single-Step Retro

### 2026-08-20: Looped Language Models Improve Compositional Tool Calling

### 2026-08-20: SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution

### 2026-08-20: The Problem Is the Problem: Towards Scalable Mathematical Discovery

### 2026-08-20: LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents

### 2026-08-21: Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Har

### 2026-08-21: GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipul

### 2026-08-21: CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical 

### 2026-08-21: Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accura

### 2026-08-21: Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learne

### 2026-08-21: Towards Quantifying Benchmark Optimization in ASR Models

### 2026-08-21: FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving

### 2026-08-21: SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback

### 2026-08-21: Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowled

### 2026-08-21: FACET: Preserving Source Intent and Executable State in Terminal Task Synthesis

### 2026-08-21: EXIMO: VLM Guided Exploration of VLA Policies

### 2026-08-21: VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio 

### 2026-08-21: LLMs Get Smarter from Targeted Synthetic Multilingual Data

### 2026-08-21: Bounded Agents: Delegation Security for Multi-Agent AI Systems

### 2026-08-22: TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity

### 2026-08-22: The Embedder's Dilemma: LLMs Are Better, but at What Cost?

### 2026-08-24: Hydra-0: Action Flow for Generalist World Modeling and Control

### 2026-08-24: ParaTempo: Efficient Parallel Reasoning via Temporal Confidence

### 2026-08-24: FlavourBench: Ranking Frontier Language Models with Executable Culinary Ground T

### 2026-08-24: Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Dist

### 2026-08-24: Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Sc

### 2026-08-24: OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs

### 2026-08-24: AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Sce

### 2026-08-24: Hadith computational science in the age of large language models: a critical nar

### 2026-08-24: Towards Faithful Simulation of Human Shopping Behavior

### 2026-08-24: Graph Engineering in the Era of LLM Agents: From Individual Intelligence to Syst

### 2026-08-24: CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Align

### 2026-08-24: InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter

### 2026-08-24: Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Think

### 2026-08-25: AutoResearch: Insight In, Hallucination Out

### 2026-08-25: Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit 

### 2026-08-25: EXPL-FR: Explaining Face Recognition Models via Vision-Language Alignment

### 2026-08-25: WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning

### 2026-08-25: Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated B

### 2026-08-25: Towards a Densing Law for User Representation Learning at Billion-Scale Capacity

### 2026-08-25: Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning 

### 2026-08-25: RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling

### 2026-08-25: Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM P

### 2026-08-25: One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommender

### 2026-08-25: MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks

### 2026-08-25: Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervisi

### 2026-08-25: ReWorld: An Interactive World Model with Long-Horizon Memory

### 2026-08-25: Prime Agent: A Self-Improving RLM Harness

### 2026-08-25: Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress

### 2026-08-25: Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Chu

### 2026-08-25: TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming

### 2026-08-25: PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration

### 2026-08-26: AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace

### 2026-08-26: MoTE: Mixture of Task Experts for Multi-Task Video Understanding

### 2026-08-26: DREAM Technical Report

### 2026-08-26: Latent Action as Intention Enables Efficient Future Imagination for World Action

### 2026-08-26: Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video

### 2026-08-26: Length-Adaptive Decoding for Masked Diffusion Machine Translation

### 2026-08-26: Best Practice Critic Optimization

### 2026-08-26: On-policy Distillation with Verifiable Reward

### 2026-08-26: AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Exec

### 2026-08-26: Meta^n: Recursive Self-Improvement through Emergent Depth

### 2026-08-27: Skill Issue: Are Skills Language-Invariant in LLMs?

### 2026-08-27: Prefix Sliding for efficient test-time scaling

### 2026-08-27: Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling

### 2026-08-27: LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech De

### 2026-08-27: Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategie

### 2026-08-27: FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling

### 2026-08-27: WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploratio

### 2026-08-27: MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Composition

### 2026-08-27: StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Mode

### 2026-08-27: Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy

### 2026-08-27: V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning

### 2026-08-27: Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agen

### 2026-08-27: Agent-G^2: Gaussian Guidance for Agentic Reinforcement Learning

### 2026-08-27: Code World Model: Coding Agent as World Brain

### 2026-08-27: VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning

### 2026-08-27: MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-T

### 2026-08-27: MARS: Multi-Specialist LLM Relay System for Competitive Programming

### 2026-08-28: EditaLive! Unified Character Video Editing for Live Streaming

### 2026-08-28: Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling Worl

### 2026-08-28: Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning

### 2026-08-28: GameWAM: A World Action Model for Video Games

### 2026-08-28: TTPO: Test-Time Policy Optimization

### 2026-08-28: Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reaso

### 2026-08-28: CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval

### 2026-08-28: Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Techn

### 2026-08-28: CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehensi

### 2026-08-28: PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

### 2026-08-28: UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City

### 2026-08-28: Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task

### 2026-08-28: Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher

### 2026-08-28: Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage

### 2026-08-28: What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents

### 2026-08-28: GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Gro

### 2026-08-30: CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model 

### 2026-08-31: LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering

### 2026-08-31: GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generati

### 2026-08-31: Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities

### 2026-08-31: DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Mu

### 2026-08-31: Ring Forcing: Towards Precise Long-Term Memory for Autoregressive Video Diffusio

### 2026-08-31: LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in V

### 2026-08-31: Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090

### 2026-08-31: Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents

### 2026-08-31: StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environmen

### 2026-08-31: StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-U

### 2026-08-31: LMSM: LLM Security Framework Inspired by Linux Security Modules

### 2026-09-01: MMMMM: A Unified Taxonomy for Investigating the Mechanisms of Multilingual Multi

### 2026-09-01: Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Pref

### 2026-09-01: DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution

### 2026-09-01: Chat-Edit-3D++: Interactive 3D and 4D Scene Editing via Large Language Models

### 2026-09-01: LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigatio

### 2026-09-01: SHAPE of Chain-of-Thought in Math Reasoning

### 2026-09-01: Dynamic Important Example Mining for Reinforcement Finetuning

### 2026-09-01: CogEvol: Towards Efficient and Reliable Learning Environment Generation

### 2026-09-01: Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superinte

### 2026-09-01: PaperGym: Rubric-Centered Evolution for Research-Plan Generation

### 2026-09-01: Cross-lingual Functional Vectors for Emotion Detection in Large Language Models

### 2026-09-02: DramaChain Bench: An End-to-End Benchmark for Short-Drama Generation

### 2026-09-02: From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers

### 2026-09-02: Safin-1: Safety from Within through Memory-Native State Evolution

### 2026-09-02: UI-Venus-2 Technical Report

### 2026-09-02: ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-

### 2026-09-02: E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Oper

### 2026-09-02: H3-World: Turning Language Understanding into World Control

### 2026-09-02: StudentSim: Training LLM-based Student Simulators

### 2026-09-02: Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone

### 2026-09-02: Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs

### 2026-09-02: Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models:

### 2026-09-02: InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Rei

### 2026-09-02: The Mechanics of Democratic Dominance: A System Dynamics Paradigm for Dynamic Co

### 2026-09-03: Debias-SparseGPT: Bias-Aware Pruning for Large Language Models

### 2026-09-03: NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Eff

### 2026-09-03: Exploring Collaboration between a language and a non-language agent

### 2026-09-03: Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Model

### 2026-09-03: A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss

### 2026-09-03: CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivat

### 2026-09-03: HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

### 2026-09-03: Aspire: Can Models Self-Evolve from Vague Goals?

### 2026-09-03: S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?

### 2026-09-03: Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills

### 2026-09-03: Language Models Can Control Their Own Attention

### 2026-09-03: Post-Training Language Models for Gold-Medal Performance in Coding Competitions

### 2026-09-03: Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Tok

### 2026-09-03: RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Reques

### 2026-09-03: Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall

### 2026-09-03: AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agent

### 2026-09-03: Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured D
- HF trending paper (arxiv: 2608.31082). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.31082]] | https://huggingface.co/papers/2608.31082
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26623). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.26623]] | https://huggingface.co/papers/2608.26623
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01532). Keywords: learning, reasoning, knowledge distillation. Status: pending-review.
- Source: [[papers/2609.01532]] | https://huggingface.co/papers/2609.01532
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27831). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.27831]] | https://huggingface.co/papers/2608.27831
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29846). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.29846]] | https://huggingface.co/papers/2608.29846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02849). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2609.02849]] | https://huggingface.co/papers/2609.02849
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02737). Keywords: sparse. Status: pending-review.
- Source: [[papers/2609.02737]] | https://huggingface.co/papers/2609.02737
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02749). Keywords: learning. Status: pending-review.
- Source: [[papers/2609.02749]] | https://huggingface.co/papers/2609.02749
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31100). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.31100]] | https://huggingface.co/papers/2608.31100
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31111). Keywords: learning, sparse. Status: pending-review.
- Source: [[papers/2608.31111]] | https://huggingface.co/papers/2608.31111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01437). Keywords: learning. Status: pending-review.
- Source: [[papers/2609.01437]] | https://huggingface.co/papers/2609.01437
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01925). Keywords: sparse. Status: pending-review.
- Source: [[papers/2609.01925]] | https://huggingface.co/papers/2609.01925
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00591). Keywords: grpo, fine-tuning. Status: pending-review.
- Source: [[papers/2609.00591]] | https://huggingface.co/papers/2609.00591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30751). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.30751]] | https://huggingface.co/papers/2608.30751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00474). Keywords: sparse. Status: pending-review.
- Source: [[papers/2609.00474]] | https://huggingface.co/papers/2609.00474
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01657). Keywords: fine-tuning, quantization. Status: pending-review.
- Source: [[papers/2609.01657]] | https://huggingface.co/papers/2609.01657
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02496). Keywords: prompt, model compression, quantization, sparse. Status: pending-review.
- Source: [[papers/2609.02496]] | https://huggingface.co/papers/2609.02496
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27509). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.27509]] | https://huggingface.co/papers/2608.27509
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28612). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.28612]] | https://huggingface.co/papers/2608.28612
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01607). Keywords: learning. Status: pending-review.
- Source: [[papers/2609.01607]] | https://huggingface.co/papers/2609.01607
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00621). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2609.00621]] | https://huggingface.co/papers/2609.00621
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01404). Keywords: fine-tuning, prompt. Status: pending-review.
- Source: [[papers/2609.01404]] | https://huggingface.co/papers/2609.01404
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01591). Keywords: learning, sparse. Status: pending-review.
- Source: [[papers/2609.01591]] | https://huggingface.co/papers/2609.01591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01560). Keywords: lora. Status: pending-review.
- Source: [[papers/2609.01560]] | https://huggingface.co/papers/2609.01560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30730). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.30730]] | https://huggingface.co/papers/2608.30730
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00188). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2609.00188]] | https://huggingface.co/papers/2609.00188
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00028). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2609.00028]] | https://huggingface.co/papers/2609.00028
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00092). Keywords: fine-tuning, lora. Status: pending-review.
- Source: [[papers/2609.00092]] | https://huggingface.co/papers/2609.00092
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01572). Keywords: grpo, reasoning. Status: pending-review.
- Source: [[papers/2609.01572]] | https://huggingface.co/papers/2609.01572
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00646). Keywords: prompt. Status: pending-review.
- Source: [[papers/2609.00646]] | https://huggingface.co/papers/2609.00646
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29613). Keywords: learning, few-shot, in-context learning. Status: pending-review.
- Source: [[papers/2608.29613]] | https://huggingface.co/papers/2608.29613
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31119). Keywords: learning, grpo, fine-tuning. Status: pending-review.
- Source: [[papers/2608.31119]] | https://huggingface.co/papers/2608.31119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31075). Keywords: learning, curriculum, reasoning. Status: pending-review.
- Source: [[papers/2608.31075]] | https://huggingface.co/papers/2608.31075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30968). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2608.30968]] | https://huggingface.co/papers/2608.30968
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29252). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.29252]] | https://huggingface.co/papers/2608.29252
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28600). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.28600]] | https://huggingface.co/papers/2608.28600
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30935). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.30935]] | https://huggingface.co/papers/2608.30935
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29137). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.29137]] | https://huggingface.co/papers/2608.29137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31106). Keywords: learning, prompt. Status: pending-review.
- Source: [[papers/2608.31106]] | https://huggingface.co/papers/2608.31106
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29464). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.29464]] | https://huggingface.co/papers/2608.29464
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29681). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.29681]] | https://huggingface.co/papers/2608.29681
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25697). Keywords: prompt, sparse. Status: pending-review.
- Source: [[papers/2608.25697]] | https://huggingface.co/papers/2608.25697
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24777). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2608.24777]] | https://huggingface.co/papers/2608.24777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24804). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.24804]] | https://huggingface.co/papers/2608.24804
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25417). Keywords: curriculum. Status: pending-review.
- Source: [[papers/2608.25417]] | https://huggingface.co/papers/2608.25417
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27370). Keywords: curriculum, scaling law. Status: pending-review.
- Source: [[papers/2608.27370]] | https://huggingface.co/papers/2608.27370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28460). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.28460]] | https://huggingface.co/papers/2608.28460
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26794). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.26794]] | https://huggingface.co/papers/2608.26794
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18524). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2608.18524]] | https://huggingface.co/papers/2608.18524
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28122). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.28122]] | https://huggingface.co/papers/2608.28122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25375). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.25375]] | https://huggingface.co/papers/2608.25375
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28281). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.28281]] | https://huggingface.co/papers/2608.28281
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27455). Keywords: learning, in-context learning, reasoning. Status: pending-review.
- Source: [[papers/2608.27455]] | https://huggingface.co/papers/2608.27455
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21832). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2608.21832]] | https://huggingface.co/papers/2608.21832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27260). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.27260]] | https://huggingface.co/papers/2608.27260
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27351). Keywords: grpo, reasoning, catastrophic forgetting, sparse. Status: pending-review.
- Source: [[papers/2608.27351]] | https://huggingface.co/papers/2608.27351
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26872). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.26872]] | https://huggingface.co/papers/2608.26872
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26103). Keywords: learning, in-context learning, prompt. Status: pending-review.
- Source: [[papers/2608.26103]] | https://huggingface.co/papers/2608.26103
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27456). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2608.27456]] | https://huggingface.co/papers/2608.27456
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27345). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.27345]] | https://huggingface.co/papers/2608.27345
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23172). Keywords: learning, in-context learning, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.23172]] | https://huggingface.co/papers/2608.23172
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15763). Keywords: learning, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.15763]] | https://huggingface.co/papers/2608.15763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25500). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.25500]] | https://huggingface.co/papers/2608.25500
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26993). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.26993]] | https://huggingface.co/papers/2608.26993
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27448). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.27448]] | https://huggingface.co/papers/2608.27448
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26200). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.26200]] | https://huggingface.co/papers/2608.26200
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26809). Keywords: reasoning, sparse. Status: pending-review.
- Source: [[papers/2608.26809]] | https://huggingface.co/papers/2608.26809
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25518). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.25518]] | https://huggingface.co/papers/2608.25518
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27123). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.27123]] | https://huggingface.co/papers/2608.27123
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23918). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.23918]] | https://huggingface.co/papers/2608.23918
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24189). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.24189]] | https://huggingface.co/papers/2608.24189
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26105). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.26105]] | https://huggingface.co/papers/2608.26105
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25927). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.25927]] | https://huggingface.co/papers/2608.25927
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23318). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.23318]] | https://huggingface.co/papers/2608.23318
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24099). Keywords: learning, grpo, reasoning. Status: pending-review.
- Source: [[papers/2608.24099]] | https://huggingface.co/papers/2608.24099
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25580). Keywords: learning, grpo, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.25580]] | https://huggingface.co/papers/2608.25580
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19098). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.19098]] | https://huggingface.co/papers/2608.19098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26067). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.26067]] | https://huggingface.co/papers/2608.26067
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25864). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.25864]] | https://huggingface.co/papers/2608.25864
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24479). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.24479]] | https://huggingface.co/papers/2608.24479
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21839). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.21839]] | https://huggingface.co/papers/2608.21839
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23256). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.23256]] | https://huggingface.co/papers/2608.23256
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25204). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.25204]] | https://huggingface.co/papers/2608.25204
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14652). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.14652]] | https://huggingface.co/papers/2608.14652
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26070). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.26070]] | https://huggingface.co/papers/2608.26070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25832). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.25832]] | https://huggingface.co/papers/2608.25832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24735). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.24735]] | https://huggingface.co/papers/2608.24735
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23041). Keywords: learning, prompt. Status: pending-review.
- Source: [[papers/2608.23041]] | https://huggingface.co/papers/2608.23041
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24696). Keywords: learning, grpo, reasoning, sparse. Status: pending-review.
- Source: [[papers/2608.24696]] | https://huggingface.co/papers/2608.24696
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23566). Keywords: learning, grpo, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.23566]] | https://huggingface.co/papers/2608.23566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22274). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.22274]] | https://huggingface.co/papers/2608.22274
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20492). Keywords: learning, sample efficiency, grpo, prompt. Status: pending-review.
- Source: [[papers/2608.20492]] | https://huggingface.co/papers/2608.20492
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24882). Keywords: few-shot. Status: pending-review.
- Source: [[papers/2608.24882]] | https://huggingface.co/papers/2608.24882
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09408). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2608.09408]] | https://huggingface.co/papers/2608.09408
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24763). Keywords: learning, moe, sparse. Status: pending-review.
- Source: [[papers/2608.24763]] | https://huggingface.co/papers/2608.24763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23740). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.23740]] | https://huggingface.co/papers/2608.23740
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21031). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.21031]] | https://huggingface.co/papers/2608.21031
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20958). Keywords: grpo, fine-tuning, lora, reasoning. Status: pending-review.
- Source: [[papers/2608.20958]] | https://huggingface.co/papers/2608.20958
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22856). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.22856]] | https://huggingface.co/papers/2608.22856
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19408). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.19408]] | https://huggingface.co/papers/2608.19408
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23552). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.23552]] | https://huggingface.co/papers/2608.23552
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23565). Keywords: lora, adapter, sparse. Status: pending-review.
- Source: [[papers/2608.23565]] | https://huggingface.co/papers/2608.23565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16812). Keywords: learning, sparse. Status: pending-review.
- Source: [[papers/2608.16812]] | https://huggingface.co/papers/2608.16812
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23035). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.23035]] | https://huggingface.co/papers/2608.23035
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.13610). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2606.13610]] | https://huggingface.co/papers/2606.13610
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23311). Keywords: grpo, lora, reasoning. Status: pending-review.
- Source: [[papers/2608.23311]] | https://huggingface.co/papers/2608.23311
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22849). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.22849]] | https://huggingface.co/papers/2608.22849
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22817). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.22817]] | https://huggingface.co/papers/2608.22817
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23392). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.23392]] | https://huggingface.co/papers/2608.23392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13914). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.13914]] | https://huggingface.co/papers/2608.13914
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22591). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.22591]] | https://huggingface.co/papers/2608.22591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21486). Keywords: adapter, prompt. Status: pending-review.
- Source: [[papers/2608.21486]] | https://huggingface.co/papers/2608.21486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20953). Keywords: reasoning, quantization. Status: pending-review.
- Source: [[papers/2608.20953]] | https://huggingface.co/papers/2608.20953
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17906). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.17906]] | https://huggingface.co/papers/2608.17906
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12781). Keywords: learning, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.12781]] | https://huggingface.co/papers/2608.12781
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20910). Keywords: adapter. Status: pending-review.
- Source: [[papers/2608.20910]] | https://huggingface.co/papers/2608.20910
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21278). Keywords: lora, adapter, low-rank, prompt. Status: pending-review.
- Source: [[papers/2608.21278]] | https://huggingface.co/papers/2608.21278
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21156). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.21156]] | https://huggingface.co/papers/2608.21156
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20707). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.20707]] | https://huggingface.co/papers/2608.20707
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20364). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.20364]] | https://huggingface.co/papers/2608.20364
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20634). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.20634]] | https://huggingface.co/papers/2608.20634
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21360). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.21360]] | https://huggingface.co/papers/2608.21360
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20061). Keywords: learning, moe, scaling law. Status: pending-review.
- Source: [[papers/2608.20061]] | https://huggingface.co/papers/2608.20061
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16647). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.16647]] | https://huggingface.co/papers/2608.16647
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20574). Keywords: dpo, prompt. Status: pending-review.
- Source: [[papers/2608.20574]] | https://huggingface.co/papers/2608.20574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16425). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.16425]] | https://huggingface.co/papers/2608.16425
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18077). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.18077]] | https://huggingface.co/papers/2608.18077
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12875). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.12875]] | https://huggingface.co/papers/2608.12875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15767). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.15767]] | https://huggingface.co/papers/2608.15767
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15888). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.15888]] | https://huggingface.co/papers/2608.15888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15964). Keywords: fine-tuning, reasoning, prompt, catastrophic forgetting. Status: pending-review.
- Source: [[papers/2608.15964]] | https://huggingface.co/papers/2608.15964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18607). Keywords: learning, prompt. Status: pending-review.
- Source: [[papers/2608.18607]] | https://huggingface.co/papers/2608.18607
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19891). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.19891]] | https://huggingface.co/papers/2608.19891
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18580). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.18580]] | https://huggingface.co/papers/2608.18580
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20281). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.20281]] | https://huggingface.co/papers/2608.20281
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13120). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.13120]] | https://huggingface.co/papers/2608.13120
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19758). Keywords: quantization, sparse. Status: pending-review.
- Source: [[papers/2608.19758]] | https://huggingface.co/papers/2608.19758
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19936). Keywords: low-rank. Status: pending-review.
- Source: [[papers/2608.19936]] | https://huggingface.co/papers/2608.19936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19863). Keywords: learning, fine-tuning. Status: pending-review.
- Source: [[papers/2608.19863]] | https://huggingface.co/papers/2608.19863
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17744). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.17744]] | https://huggingface.co/papers/2608.17744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19776). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.19776]] | https://huggingface.co/papers/2608.19776
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19759). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.19759]] | https://huggingface.co/papers/2608.19759
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08466). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.08466]] | https://huggingface.co/papers/2608.08466
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17393). Keywords: learning, moe, sparse. Status: pending-review.
- Source: [[papers/2608.17393]] | https://huggingface.co/papers/2608.17393
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16977). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.16977]] | https://huggingface.co/papers/2608.16977
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18933). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.18933]] | https://huggingface.co/papers/2608.18933
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18171). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.18171]] | https://huggingface.co/papers/2608.18171
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18940). Keywords: fine-tuning, prompt. Status: pending-review.
- Source: [[papers/2608.18940]] | https://huggingface.co/papers/2608.18940
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14929). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.14929]] | https://huggingface.co/papers/2608.14929
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16590). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.16590]] | https://huggingface.co/papers/2608.16590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13947). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.13947]] | https://huggingface.co/papers/2608.13947
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17253). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.17253]] | https://huggingface.co/papers/2608.17253
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14229). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.14229]] | https://huggingface.co/papers/2608.14229
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15869). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.15869]] | https://huggingface.co/papers/2608.15869
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11947). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.11947]] | https://huggingface.co/papers/2608.11947
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17310). Keywords: learning, fine-tuning, lora, reasoning. Status: pending-review.
- Source: [[papers/2608.17310]] | https://huggingface.co/papers/2608.17310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16002). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.16002]] | https://huggingface.co/papers/2608.16002
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17975). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.17975]] | https://huggingface.co/papers/2608.17975
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17271). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.17271]] | https://huggingface.co/papers/2608.17271
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16393). Keywords: adapter, prompt. Status: pending-review.
- Source: [[papers/2608.16393]] | https://huggingface.co/papers/2608.16393
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17988). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.17988]] | https://huggingface.co/papers/2608.17988
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18076). Keywords: curriculum. Status: pending-review.
- Source: [[papers/2608.18076]] | https://huggingface.co/papers/2608.18076
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05811). Keywords: learning, dpo. Status: pending-review.
- Source: [[papers/2608.05811]] | https://huggingface.co/papers/2608.05811
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15008). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.15008]] | https://huggingface.co/papers/2608.15008
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17512). Keywords: sample efficiency, grpo, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.17512]] | https://huggingface.co/papers/2608.17512
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16157). Keywords: moe. Status: pending-review.
- Source: [[papers/2608.16157]] | https://huggingface.co/papers/2608.16157
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17528). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.17528]] | https://huggingface.co/papers/2608.17528
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14221). Keywords: learning, fine-tuning. Status: pending-review.
- Source: [[papers/2608.14221]] | https://huggingface.co/papers/2608.14221
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18063). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.18063]] | https://huggingface.co/papers/2608.18063
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17067). Keywords: fine-tuning, prompt. Status: pending-review.
- Source: [[papers/2608.17067]] | https://huggingface.co/papers/2608.17067
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12944). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.12944]] | https://huggingface.co/papers/2608.12944
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17379). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.17379]] | https://huggingface.co/papers/2608.17379
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13987). Keywords: lora, prompt. Status: pending-review.
- Source: [[papers/2608.13987]] | https://huggingface.co/papers/2608.13987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12571). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.12571]] | https://huggingface.co/papers/2608.12571
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12898). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.12898]] | https://huggingface.co/papers/2608.12898
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15930). Keywords: learning, prompt. Status: pending-review.
- Source: [[papers/2608.15930]] | https://huggingface.co/papers/2608.15930
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16884). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.16884]] | https://huggingface.co/papers/2608.16884
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16859). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.16859]] | https://huggingface.co/papers/2608.16859
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16143). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.16143]] | https://huggingface.co/papers/2608.16143
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16435). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.16435]] | https://huggingface.co/papers/2608.16435
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16485). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.16485]] | https://huggingface.co/papers/2608.16485
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16072). Keywords: learning, dpo, reasoning. Status: pending-review.
- Source: [[papers/2608.16072]] | https://huggingface.co/papers/2608.16072
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15037). Keywords: low-rank, prompt. Status: pending-review.
- Source: [[papers/2608.15037]] | https://huggingface.co/papers/2608.15037
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15659). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.15659]] | https://huggingface.co/papers/2608.15659
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16765). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.16765]] | https://huggingface.co/papers/2608.16765
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15045). Keywords: curriculum, reasoning. Status: pending-review.
- Source: [[papers/2608.15045]] | https://huggingface.co/papers/2608.15045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16328). Keywords: fine-tuning, prompt. Status: pending-review.
- Source: [[papers/2608.16328]] | https://huggingface.co/papers/2608.16328
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14606). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.14606]] | https://huggingface.co/papers/2608.14606
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14290). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.14290]] | https://huggingface.co/papers/2608.14290
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14138). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.14138]] | https://huggingface.co/papers/2608.14138
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00220). Keywords: learning, dpo, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.00220]] | https://huggingface.co/papers/2608.00220
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12209). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.12209]] | https://huggingface.co/papers/2608.12209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14546). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.14546]] | https://huggingface.co/papers/2608.14546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09928). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.09928]] | https://huggingface.co/papers/2608.09928
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13606). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.13606]] | https://huggingface.co/papers/2608.13606
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13667). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.13667]] | https://huggingface.co/papers/2608.13667
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10835). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.10835]] | https://huggingface.co/papers/2608.10835
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13545). Keywords: learning, skill acquisition, curriculum, in-context learning. Status: pending-review.
- Source: [[papers/2608.13545]] | https://huggingface.co/papers/2608.13545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14277). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.14277]] | https://huggingface.co/papers/2608.14277
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14075). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.14075]] | https://huggingface.co/papers/2608.14075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13760). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.13760]] | https://huggingface.co/papers/2608.13760
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08020). Keywords: reasoning, pruning. Status: pending-review.
- Source: [[papers/2608.08020]] | https://huggingface.co/papers/2608.08020
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09926). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.09926]] | https://huggingface.co/papers/2608.09926
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11367). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.11367]] | https://huggingface.co/papers/2608.11367
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11045). Keywords: dpo, quantization. Status: pending-review.
- Source: [[papers/2608.11045]] | https://huggingface.co/papers/2608.11045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12836). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.12836]] | https://huggingface.co/papers/2608.12836
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13505). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.13505]] | https://huggingface.co/papers/2608.13505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13546). Keywords: prompt, sparse. Status: pending-review.
- Source: [[papers/2608.13546]] | https://huggingface.co/papers/2608.13546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08888). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.08888]] | https://huggingface.co/papers/2608.08888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12990). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.12990]] | https://huggingface.co/papers/2608.12990
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13560). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.13560]] | https://huggingface.co/papers/2608.13560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07545). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.07545]] | https://huggingface.co/papers/2608.07545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12743). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.12743]] | https://huggingface.co/papers/2608.12743
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13049). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.13049]] | https://huggingface.co/papers/2608.13049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11752). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.11752]] | https://huggingface.co/papers/2608.11752
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10538). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.10538]] | https://huggingface.co/papers/2608.10538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07193). Keywords: reasoning, pruning. Status: pending-review.
- Source: [[papers/2608.07193]] | https://huggingface.co/papers/2608.07193
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29211). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2607.29211]] | https://huggingface.co/papers/2607.29211
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13430). Keywords: instruction tuning. Status: pending-review.
- Source: [[papers/2608.13430]] | https://huggingface.co/papers/2608.13430
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11951). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.11951]] | https://huggingface.co/papers/2608.11951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12313). Keywords: learning, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.12313]] | https://huggingface.co/papers/2608.12313
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11660). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.11660]] | https://huggingface.co/papers/2608.11660
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11878). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.11878]] | https://huggingface.co/papers/2608.11878
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11274). Keywords: rlhf, dpo. Status: pending-review.
- Source: [[papers/2608.11274]] | https://huggingface.co/papers/2608.11274
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12314). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.12314]] | https://huggingface.co/papers/2608.12314
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12307). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.12307]] | https://huggingface.co/papers/2608.12307
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08107). Keywords: learning, instruction tuning. Status: pending-review.
- Source: [[papers/2608.08107]] | https://huggingface.co/papers/2608.08107
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10708). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.10708]] | https://huggingface.co/papers/2608.10708
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06729). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.06729]] | https://huggingface.co/papers/2608.06729
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11350). Keywords: learning, fine-tuning. Status: pending-review.
- Source: [[papers/2608.11350]] | https://huggingface.co/papers/2608.11350
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09805). Keywords: learning, grpo, lora, reasoning. Status: pending-review.
- Source: [[papers/2608.09805]] | https://huggingface.co/papers/2608.09805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09853). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.09853]] | https://huggingface.co/papers/2608.09853
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08097). Keywords: reasoning, sparse. Status: pending-review.
- Source: [[papers/2608.08097]] | https://huggingface.co/papers/2608.08097
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07565). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.07565]] | https://huggingface.co/papers/2608.07565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09848). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.09848]] | https://huggingface.co/papers/2608.09848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09888). Keywords: learning, in-context learning, reasoning. Status: pending-review.
- Source: [[papers/2608.09888]] | https://huggingface.co/papers/2608.09888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: low-rank. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08786). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.08786]] | https://huggingface.co/papers/2608.08786
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08722). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.08722]] | https://huggingface.co/papers/2608.08722
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03887). Keywords: fine-tuning, lora, low-rank. Status: pending-review.
- Source: [[papers/2608.03887]] | https://huggingface.co/papers/2608.03887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06296). Keywords: grpo, reasoning. Status: pending-review.
- Source: [[papers/2608.06296]] | https://huggingface.co/papers/2608.06296
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06751). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.06751]] | https://huggingface.co/papers/2608.06751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06065). Keywords: learning, grpo, reasoning. Status: pending-review.
- Source: [[papers/2608.06065]] | https://huggingface.co/papers/2608.06065
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08477). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.08477]] | https://huggingface.co/papers/2608.08477
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10875). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.10875]] | https://huggingface.co/papers/2608.10875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10692). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.10692]] | https://huggingface.co/papers/2608.10692
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10366). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2608.10366]] | https://huggingface.co/papers/2608.10366
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10299). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.10299]] | https://huggingface.co/papers/2608.10299
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11079). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.11079]] | https://huggingface.co/papers/2608.11079
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27670). Keywords: fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2607.27670]] | https://huggingface.co/papers/2607.27670
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08119). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.08119]] | https://huggingface.co/papers/2608.08119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03216). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.03216]] | https://huggingface.co/papers/2608.03216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10812). Keywords: learning, grpo, fine-tuning. Status: pending-review.
- Source: [[papers/2608.10812]] | https://huggingface.co/papers/2608.10812
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08389). Keywords: pruning. Status: pending-review.
- Source: [[papers/2608.08389]] | https://huggingface.co/papers/2608.08389
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08627). Keywords: dpo, moe, sparse. Status: pending-review.
- Source: [[papers/2608.08627]] | https://huggingface.co/papers/2608.08627
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09900). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.09900]] | https://huggingface.co/papers/2608.09900
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08814). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2608.08814]] | https://huggingface.co/papers/2608.08814
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10628). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.10628]] | https://huggingface.co/papers/2608.10628
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08311). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.08311]] | https://huggingface.co/papers/2608.08311
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09853). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.09853]] | https://huggingface.co/papers/2608.09853
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08097). Keywords: reasoning, sparse. Status: pending-review.
- Source: [[papers/2608.08097]] | https://huggingface.co/papers/2608.08097
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07565). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.07565]] | https://huggingface.co/papers/2608.07565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09848). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.09848]] | https://huggingface.co/papers/2608.09848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09888). Keywords: learning, in-context learning, reasoning. Status: pending-review.
- Source: [[papers/2608.09888]] | https://huggingface.co/papers/2608.09888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: low-rank. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08786). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.08786]] | https://huggingface.co/papers/2608.08786
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08722). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.08722]] | https://huggingface.co/papers/2608.08722
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07222). Keywords: sparse, scaling law. Status: pending-review.
- Source: [[papers/2608.07222]] | https://huggingface.co/papers/2608.07222
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07110). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.07110]] | https://huggingface.co/papers/2608.07110
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06714). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.06714]] | https://huggingface.co/papers/2608.06714
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07468). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.07468]] | https://huggingface.co/papers/2608.07468
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07051). Keywords: fine-tuning, lora, adapter. Status: pending-review.
- Source: [[papers/2608.07051]] | https://huggingface.co/papers/2608.07051
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02831). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.02831]] | https://huggingface.co/papers/2608.02831
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03573). Keywords: learning, fine-tuning, reasoning, sparse. Status: pending-review.
- Source: [[papers/2608.03573]] | https://huggingface.co/papers/2608.03573
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03571). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2608.03571]] | https://huggingface.co/papers/2608.03571
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.18846). Keywords: learning. Status: pending-review.
- Source: [[papers/2603.18846]] | https://huggingface.co/papers/2603.18846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06756). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.06756]] | https://huggingface.co/papers/2608.06756
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06013). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.06013]] | https://huggingface.co/papers/2608.06013
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03796). Keywords: knowledge distillation. Status: pending-review.
- Source: [[papers/2608.03796]] | https://huggingface.co/papers/2608.03796
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01310). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.01310]] | https://huggingface.co/papers/2608.01310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04569). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.04569]] | https://huggingface.co/papers/2608.04569
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05784). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.05784]] | https://huggingface.co/papers/2608.05784
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05798). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.05798]] | https://huggingface.co/papers/2608.05798
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01492). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.01492]] | https://huggingface.co/papers/2608.01492
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04378). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.04378]] | https://huggingface.co/papers/2608.04378
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05466). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.05466]] | https://huggingface.co/papers/2608.05466
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06374). Keywords: learning, moe. Status: pending-review.
- Source: [[papers/2608.06374]] | https://huggingface.co/papers/2608.06374
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06301). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.06301]] | https://huggingface.co/papers/2608.06301
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05802). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.05802]] | https://huggingface.co/papers/2608.05802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05248). Keywords: lora, prompt. Status: pending-review.
- Source: [[papers/2608.05248]] | https://huggingface.co/papers/2608.05248
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05987). Keywords: learning, grpo, sparse. Status: pending-review.
- Source: [[papers/2608.05987]] | https://huggingface.co/papers/2608.05987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06352). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.06352]] | https://huggingface.co/papers/2608.06352
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05137). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.05137]] | https://huggingface.co/papers/2608.05137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06197). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.06197]] | https://huggingface.co/papers/2608.06197
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28609). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2607.28609]] | https://huggingface.co/papers/2607.28609
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05565). Keywords: curriculum, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.05565]] | https://huggingface.co/papers/2608.05565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04956). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.04956]] | https://huggingface.co/papers/2608.04956
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05785). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2608.05785]] | https://huggingface.co/papers/2608.05785
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06216). Keywords: learning, continual learning. Status: pending-review.
- Source: [[papers/2608.06216]] | https://huggingface.co/papers/2608.06216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03972). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.03972]] | https://huggingface.co/papers/2608.03972
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02703). Keywords: low-rank, quantization. Status: pending-review.
- Source: [[papers/2608.02703]] | https://huggingface.co/papers/2608.02703
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03506). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.03506]] | https://huggingface.co/papers/2608.03506
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.00482). Keywords: grpo, reasoning. Status: pending-review.
- Source: [[papers/2607.00482]] | https://huggingface.co/papers/2607.00482
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05131). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.05131]] | https://huggingface.co/papers/2608.05131
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05070). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.05070]] | https://huggingface.co/papers/2608.05070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04349). Keywords: curriculum, lora, adapter. Status: pending-review.
- Source: [[papers/2608.04349]] | https://huggingface.co/papers/2608.04349
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05000). Keywords: lora, moe. Status: pending-review.
- Source: [[papers/2608.05000]] | https://huggingface.co/papers/2608.05000
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04436). Keywords: learning, grpo, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2608.04436]] | https://huggingface.co/papers/2608.04436
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04701). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.04701]] | https://huggingface.co/papers/2608.04701
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28048). Keywords: skill acquisition, prompt. Status: pending-review.
- Source: [[papers/2607.28048]] | https://huggingface.co/papers/2607.28048
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05139). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.05139]] | https://huggingface.co/papers/2608.05139
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04570). Keywords: lora. Status: pending-review.
- Source: [[papers/2608.04570]] | https://huggingface.co/papers/2608.04570
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03632). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.03632]] | https://huggingface.co/papers/2608.03632
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04964). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2608.04964]] | https://huggingface.co/papers/2608.04964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05042). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.05042]] | https://huggingface.co/papers/2608.05042
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00782). Keywords: learning, grpo, lora, prompt. Status: pending-review.
- Source: [[papers/2608.00782]] | https://huggingface.co/papers/2608.00782
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04505). Keywords: dpo, reasoning, moe. Status: pending-review.
- Source: [[papers/2608.04505]] | https://huggingface.co/papers/2608.04505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02580). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.02580]] | https://huggingface.co/papers/2608.02580
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04926). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.04926]] | https://huggingface.co/papers/2608.04926
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05102). Keywords: learning, grpo, fine-tuning, sparse. Status: pending-review.
- Source: [[papers/2608.05102]] | https://huggingface.co/papers/2608.05102
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01862). Keywords: learning, fine-tuning. Status: pending-review.
- Source: [[papers/2608.01862]] | https://huggingface.co/papers/2608.01862
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25614). Keywords: fine-tuning, catastrophic forgetting. Status: pending-review.
- Source: [[papers/2607.25614]] | https://huggingface.co/papers/2607.25614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02392). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.02392]] | https://huggingface.co/papers/2608.02392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28956). Keywords: prompt. Status: pending-review.
- Source: [[papers/2607.28956]] | https://huggingface.co/papers/2607.28956
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03971). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.03971]] | https://huggingface.co/papers/2608.03971
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03509). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.03509]] | https://huggingface.co/papers/2608.03509
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04007). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.04007]] | https://huggingface.co/papers/2608.04007
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01837). Keywords: learning, grpo, sparse. Status: pending-review.
- Source: [[papers/2608.01837]] | https://huggingface.co/papers/2608.01837
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02713). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.02713]] | https://huggingface.co/papers/2608.02713
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03979). Keywords: learning, grpo, fine-tuning, lora. Status: pending-review.
- Source: [[papers/2608.03979]] | https://huggingface.co/papers/2608.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03457). Keywords: learning, fine-tuning, reasoning, moe. Status: pending-review.
- Source: [[papers/2608.03457]] | https://huggingface.co/papers/2608.03457
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03874). Keywords: learning, in-context learning. Status: pending-review.
- Source: [[papers/2608.03874]] | https://huggingface.co/papers/2608.03874
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02791). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.02791]] | https://huggingface.co/papers/2608.02791
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03507). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.03507]] | https://huggingface.co/papers/2608.03507
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01247). Keywords: lora, adapter. Status: pending-review.
- Source: [[papers/2608.01247]] | https://huggingface.co/papers/2608.01247
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26654). Keywords: curriculum, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2607.26654]] | https://huggingface.co/papers/2607.26654
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26246). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2607.26246]] | https://huggingface.co/papers/2607.26246
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01755). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.01755]] | https://huggingface.co/papers/2608.01755
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01973). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.01973]] | https://huggingface.co/papers/2608.01973
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02358). Keywords: curriculum, reasoning. Status: pending-review.
- Source: [[papers/2608.02358]] | https://huggingface.co/papers/2608.02358
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01954). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.01954]] | https://huggingface.co/papers/2608.01954
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29613). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.29613]] | https://huggingface.co/papers/2607.29613
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02023). Keywords: learning, curriculum, grpo, moe. Status: pending-review.
- Source: [[papers/2608.02023]] | https://huggingface.co/papers/2608.02023
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00440). Keywords: prompt. Status: pending-review.
- Source: [[papers/2608.00440]] | https://huggingface.co/papers/2608.00440
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02583). Keywords: sparse. Status: pending-review.
- Source: [[papers/2608.02583]] | https://huggingface.co/papers/2608.02583
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02287). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2608.02287]] | https://huggingface.co/papers/2608.02287
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01678). Keywords: learning. Status: pending-review.
- Source: [[papers/2608.01678]] | https://huggingface.co/papers/2608.01678
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01964). Keywords: adapter, reasoning. Status: pending-review.
- Source: [[papers/2608.01964]] | https://huggingface.co/papers/2608.01964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01185). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2608.01185]] | https://huggingface.co/papers/2608.01185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01827). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2608.01827]] | https://huggingface.co/papers/2608.01827
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00574). Keywords: prompt, moe. Status: pending-review.
- Source: [[papers/2608.00574]] | https://huggingface.co/papers/2608.00574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02585). Keywords: learning, reasoning, prompt. Status: pending-review.
- Source: [[papers/2608.02585]] | https://huggingface.co/papers/2608.02585
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29241). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2607.29241]] | https://huggingface.co/papers/2607.29241
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28802). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2607.28802]] | https://huggingface.co/papers/2607.28802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29122). Keywords: adapter. Status: pending-review.
- Source: [[papers/2607.29122]] | https://huggingface.co/papers/2607.29122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26848). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2607.26848]] | https://huggingface.co/papers/2607.26848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26326). Keywords: fine-tuning. Status: pending-review.
- Source: [[papers/2607.26326]] | https://huggingface.co/papers/2607.26326
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26497). Keywords: lora, reasoning. Status: pending-review.
- Source: [[papers/2607.26497]] | https://huggingface.co/papers/2607.26497
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27372). Keywords: learning, sample efficiency, lora. Status: pending-review.
- Source: [[papers/2607.27372]] | https://huggingface.co/papers/2607.27372
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28374). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2607.28374]] | https://huggingface.co/papers/2607.28374
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25289). Keywords: knowledge distillation. Status: pending-review.
- Source: [[papers/2607.25289]] | https://huggingface.co/papers/2607.25289
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28362). Keywords: learning, fine-tuning. Status: pending-review.
- Source: [[papers/2607.28362]] | https://huggingface.co/papers/2607.28362
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26637). Keywords: lora. Status: pending-review.
- Source: [[papers/2607.26637]] | https://huggingface.co/papers/2607.26637
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28319). Keywords: reasoning, prompt, pruning. Status: pending-review.
- Source: [[papers/2607.28319]] | https://huggingface.co/papers/2607.28319
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28308). Keywords: moe, sparse, pruning. Status: pending-review.
- Source: [[papers/2607.28308]] | https://huggingface.co/papers/2607.28308
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28582). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2607.28582]] | https://huggingface.co/papers/2607.28582
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28617). Keywords: prompt. Status: pending-review.
- Source: [[papers/2607.28617]] | https://huggingface.co/papers/2607.28617
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23802). Keywords: learning, reasoning. Status: pending-review.
- Source: [[papers/2607.23802]] | https://huggingface.co/papers/2607.23802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23782). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.23782]] | https://huggingface.co/papers/2607.23782
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28675). Keywords: quantization. Status: pending-review.
- Source: [[papers/2607.28675]] | https://huggingface.co/papers/2607.28675
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29025). Keywords: learning, fine-tuning, reasoning. Status: pending-review.
- Source: [[papers/2607.29025]] | https://huggingface.co/papers/2607.29025
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.18082). Keywords: learning, lora. Status: pending-review.
- Source: [[papers/2607.18082]] | https://huggingface.co/papers/2607.18082
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28996). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.28996]] | https://huggingface.co/papers/2607.28996
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28478). Keywords: reasoning, prompt. Status: pending-review.
- Source: [[papers/2607.28478]] | https://huggingface.co/papers/2607.28478
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27924). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.27924]] | https://huggingface.co/papers/2607.27924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25388). Keywords: reasoning. Status: pending-review.
- Source: [[papers/2607.25388]] | https://huggingface.co/papers/2607.25388
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27888). Keywords: learning, grpo, reasoning. Status: pending-review.
- Source: [[papers/2607.27888]] | https://huggingface.co/papers/2607.27888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26991). Keywords: learning, scaling law. Status: pending-review.
- Source: [[papers/2607.26991]] | https://huggingface.co/papers/2607.26991
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29209). Keywords: learning, grpo, lora, reasoning. Status: pending-review.
- Source: [[papers/2607.29209]] | https://huggingface.co/papers/2607.29209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28595). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.28595]] | https://huggingface.co/papers/2607.28595
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28410). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.28410]] | https://huggingface.co/papers/2607.28410
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26056). Keywords: learning, dpo. Status: pending-review.
- Source: [[papers/2607.26056]] | https://huggingface.co/papers/2607.26056
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23370). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.23370]] | https://huggingface.co/papers/2607.23370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21461). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.21461]] | https://huggingface.co/papers/2607.21461
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.14777). Keywords: learning, sample efficiency. Status: pending-review.
- Source: [[papers/2607.14777]] | https://huggingface.co/papers/2607.14777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12625). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.12625]] | https://huggingface.co/papers/2607.12625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.01232). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.01232]] | https://huggingface.co/papers/2607.01232
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05369). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.05369]] | https://huggingface.co/papers/2607.05369
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05391). Keywords: sample efficiency, grpo. Status: pending-review.
- Source: [[papers/2607.05391]] | https://huggingface.co/papers/2607.05391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.29315). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.29315]] | https://huggingface.co/papers/2606.29315
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.32017). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2606.32017]] | https://huggingface.co/papers/2606.32017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.26080). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.26080]] | https://huggingface.co/papers/2606.26080
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.18831). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2606.18831]] | https://huggingface.co/papers/2606.18831
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.19980). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.19980]] | https://huggingface.co/papers/2606.19980
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.19236). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2606.19236]] | https://huggingface.co/papers/2606.19236
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.15007). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.15007]] | https://huggingface.co/papers/2606.15007
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.18401). Keywords: learning, rlhf. Status: pending-review.
- Source: [[papers/2604.18401]] | https://huggingface.co/papers/2604.18401
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.13707). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2606.13707]] | https://huggingface.co/papers/2606.13707
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.14249). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.14249]] | https://huggingface.co/papers/2606.14249
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.14502). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.14502]] | https://huggingface.co/papers/2606.14502
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03108). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.03108]] | https://huggingface.co/papers/2606.03108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28742). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2605.28742]] | https://huggingface.co/papers/2605.28742
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03841). Keywords: learning, skill acquisition. Status: pending-review.
- Source: [[papers/2606.03841]] | https://huggingface.co/papers/2606.03841
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.01770). Keywords: dpo. Status: pending-review.
- Source: [[papers/2606.01770]] | https://huggingface.co/papers/2606.01770
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03979). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2606.03979]] | https://huggingface.co/papers/2606.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28424). Keywords: learning. Status: pending-review.
- Source: [[papers/2605.28424]] | https://huggingface.co/papers/2605.28424
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28805). Keywords: learning. Status: pending-review.
- Source: [[papers/2605.28805]] | https://huggingface.co/papers/2605.28805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.24517). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2605.24517]] | https://huggingface.co/papers/2605.24517
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.20342). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2605.20342]] | https://huggingface.co/papers/2605.20342
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.19436). Keywords: learning, dpo, grpo. Status: pending-review.
- Source: [[papers/2605.19436]] | https://huggingface.co/papers/2605.19436
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.17698). Keywords: curriculum. Status: pending-review.
- Source: [[papers/2605.17698]] | https://huggingface.co/papers/2605.17698
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.08715). Keywords: learning. Status: pending-review.
- Source: [[papers/2605.08715]] | https://huggingface.co/papers/2605.08715
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.09959). Keywords: dpo, grpo. Status: pending-review.
- Source: [[papers/2605.09959]] | https://huggingface.co/papers/2605.09959
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.07510). Keywords: dpo. Status: pending-review.
- Source: [[papers/2605.07510]] | https://huggingface.co/papers/2605.07510
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.05185). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2605.05185]] | https://huggingface.co/papers/2605.05185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.02943). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2605.02943]] | https://huggingface.co/papers/2605.02943
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.03042). Keywords: learning. Status: pending-review.
- Source: [[papers/2605.03042]] | https://huggingface.co/papers/2605.03042
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.28181). Keywords: learning. Status: pending-review.
- Source: [[papers/2604.28181]] | https://huggingface.co/papers/2604.28181
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.19406). Keywords: learning, rlhf, dpo, grpo. Status: pending-review.
- Source: [[papers/2604.19406]] | https://huggingface.co/papers/2604.19406
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.11544). Keywords: learning. Status: pending-review.
- Source: [[papers/2604.11544]] | https://huggingface.co/papers/2604.11544
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.05336). Keywords: grpo. Status: pending-review.
- Source: [[papers/2604.05336]] | https://huggingface.co/papers/2604.05336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.08545). Keywords: learning, curriculum, dpo. Status: pending-review.
- Source: [[papers/2604.08545]] | https://huggingface.co/papers/2604.08545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.05846). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2604.05846]] | https://huggingface.co/papers/2604.05846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.06392). Keywords: learning. Status: pending-review.
- Source: [[papers/2604.06392]] | https://huggingface.co/papers/2604.06392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.25111). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2603.25111]] | https://huggingface.co/papers/2603.25111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.04767). Keywords: learning, curriculum, sample efficiency, grpo. Status: pending-review.
- Source: [[papers/2604.04767]] | https://huggingface.co/papers/2604.04767
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.02721). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2604.02721]] | https://huggingface.co/papers/2604.02721
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.01152). Keywords: learning, curriculum, dpo, grpo. Status: pending-review.
- Source: [[papers/2604.01152]] | https://huggingface.co/papers/2604.01152
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.26017). Keywords: learning. Status: pending-review.
- Source: [[papers/2603.26017]] | https://huggingface.co/papers/2603.26017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.18118). Keywords: learning, dpo, grpo. Status: pending-review.
- Source: [[papers/2603.18118]] | https://huggingface.co/papers/2603.18118
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.15670). Keywords: learning. Status: pending-review.
- Source: [[papers/2603.15670]] | https://huggingface.co/papers/2603.15670
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.08262). Keywords: learning. Status: pending-review.
- Source: [[papers/2603.08262]] | https://huggingface.co/papers/2603.08262
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.09018). Keywords: learning. Status: pending-review.
- Source: [[papers/2603.09018]] | https://huggingface.co/papers/2603.09018
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.02208). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2603.02208]] | https://huggingface.co/papers/2603.02208
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.21320). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2602.21320]] | https://huggingface.co/papers/2602.21320
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.16928). Keywords: learning. Status: pending-review.
- Source: [[papers/2602.16928]] | https://huggingface.co/papers/2602.16928
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.10604). Keywords: learning. Status: pending-review.
- Source: [[papers/2602.10604]] | https://huggingface.co/papers/2602.10604
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.08847). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2602.08847]] | https://huggingface.co/papers/2602.08847
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.09443). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2602.09443]] | https://huggingface.co/papers/2602.09443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06855). Keywords: learning. Status: pending-review.
- Source: [[papers/2602.06855]] | https://huggingface.co/papers/2602.06855
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06130). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2602.06130]] | https://huggingface.co/papers/2602.06130
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.21590). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2601.21590]] | https://huggingface.co/papers/2601.21590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.20802). Keywords: learning, sample efficiency, dpo. Status: pending-review.
- Source: [[papers/2601.20802]] | https://huggingface.co/papers/2601.20802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.18778). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2601.18778]] | https://huggingface.co/papers/2601.18778
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.15690). Keywords: learning. Status: pending-review.
- Source: [[papers/2601.15690]] | https://huggingface.co/papers/2601.15690
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.12538). Keywords: learning. Status: pending-review.
- Source: [[papers/2601.12538]] | https://huggingface.co/papers/2601.12538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.09113). Keywords: learning. Status: pending-review.
- Source: [[papers/2601.09113]] | https://huggingface.co/papers/2601.09113
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.02075). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2601.02075]] | https://huggingface.co/papers/2601.02075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.17102). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2512.17102]] | https://huggingface.co/papers/2512.17102
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05402). Keywords: learning. Status: pending-review.
- Source: [[papers/2512.05402]] | https://huggingface.co/papers/2512.05402
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.08153). Keywords: learning, sample efficiency, grpo. Status: pending-review.
- Source: [[papers/2512.08153]] | https://huggingface.co/papers/2512.08153
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05049). Keywords: learning. Status: pending-review.
- Source: [[papers/2512.05049]] | https://huggingface.co/papers/2512.05049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.04797). Keywords: learning. Status: pending-review.
- Source: [[papers/2512.04797]] | https://huggingface.co/papers/2512.04797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.12797). Keywords: learning, meta-learning. Status: pending-review.
- Source: [[papers/2511.12797]] | https://huggingface.co/papers/2511.12797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.09515). Keywords: learning, sample efficiency, grpo. Status: pending-review.
- Source: [[papers/2511.09515]] | https://huggingface.co/papers/2511.09515
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.03773). Keywords: learning, curriculum, grpo. Status: pending-review.
- Source: [[papers/2511.03773]] | https://huggingface.co/papers/2511.03773
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.23925). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2510.23925]] | https://huggingface.co/papers/2510.23925
- Confidence: Low (auto-matched, not yet reviewed)
  Multi-Turn
- HF trending paper (arxiv: 2510.24645). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.24645]] | https://huggingface.co/papers/2510.24645
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.24684). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2510.24684]] | https://huggingface.co/papers/2510.24684
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.23272). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2510.23272]] | https://huggingface.co/papers/2510.23272
- Confidence: Low (auto-matched, not yet reviewed)
  Learning F
- HF trending paper (arxiv: 2510.14264). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.14264]] | https://huggingface.co/papers/2510.14264
- Confidence: Low (auto-matched, not yet reviewed)
  Agentic A
- HF trending paper (arxiv: 2510.16720). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.16720]] | https://huggingface.co/papers/2510.16720
- Confidence: Low (auto-matched, not yet reviewed)
  LLMs
- HF trending paper (arxiv: 2510.11062). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2510.11062]] | https://huggingface.co/papers/2510.11062
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.12269). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.12269]] | https://huggingface.co/papers/2510.12269
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.07841). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.07841]] | https://huggingface.co/papers/2510.07841
- Confidence: Low (auto-matched, not yet reviewed)
  Samplin
- HF trending paper (arxiv: 2510.04087). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.04087]] | https://huggingface.co/papers/2510.04087
- Confidence: Low (auto-matched, not yet reviewed)
  Academic P
- HF trending paper (arxiv: 2510.05571). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.05571]] | https://huggingface.co/papers/2510.05571
- Confidence: Low (auto-matched, not yet reviewed)
  Synthesi
- HF trending paper (arxiv: 2509.24107). Keywords: learning, curriculum, grpo. Status: pending-review.
- Source: [[papers/2509.24107]] | https://huggingface.co/papers/2509.24107
- Confidence: Low (auto-matched, not yet reviewed)
  Co-Evolution in M
- HF trending paper (arxiv: 2510.01586). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.01586]] | https://huggingface.co/papers/2510.01586
- Confidence: Low (auto-matched, not yet reviewed)
  Preference Imag
- HF trending paper (arxiv: 2509.25771). Keywords: learning, rlhf, dpo. Status: pending-review.
- Source: [[papers/2509.25771]] | https://huggingface.co/papers/2509.25771
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23370). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.23370]] | https://huggingface.co/papers/2607.23370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.01538). Keywords: learning. Status: pending-review.
- Source: [[papers/2510.01538]] | https://huggingface.co/papers/2510.01538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.24720). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.24720]] | https://huggingface.co/papers/2607.24720
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.24280). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.24280]] | https://huggingface.co/papers/2607.24280
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21653). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.21653]] | https://huggingface.co/papers/2607.21653
- Confidence: Low (auto-matched, not yet reviewed)
  Reasoning L
- HF trending paper (arxiv: 2510.01037). Keywords: learning, curriculum, grpo. Status: pending-review.
- Source: [[papers/2510.01037]] | https://huggingface.co/papers/2510.01037
- Confidence: Low (auto-matched, not yet reviewed)
  Self-Play
- HF trending paper (arxiv: 2509.25541). Keywords: learning. Status: pending-review.
- Source: [[papers/2509.25541]] | https://huggingface.co/papers/2509.25541
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21461). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.21461]] | https://huggingface.co/papers/2607.21461
- Confidence: Low (auto-matched, not yet reviewed)
  Feedba
- HF trending paper (arxiv: 2509.22644). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2509.22644]] | https://huggingface.co/papers/2509.22644
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16204). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.16204]] | https://huggingface.co/papers/2607.16204
- Confidence: Low (auto-matched, not yet reviewed)
  Explorat
- HF trending paper (arxiv: 2509.22601). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2509.22601]] | https://huggingface.co/papers/2509.22601
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.10966). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.10966]] | https://huggingface.co/papers/2607.10966
- Confidence: Low (auto-matched, not yet reviewed)
  Learning
- HF trending paper (arxiv: 2509.19736). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2509.19736]] | https://huggingface.co/papers/2509.19736
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16169). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.16169]] | https://huggingface.co/papers/2607.16169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16097). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.16097]] | https://huggingface.co/papers/2607.16097
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.14777). Keywords: learning, sample efficiency. Status: pending-review.
- Source: [[papers/2607.14777]] | https://huggingface.co/papers/2607.14777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.06733). Keywords: learning, sample efficiency, dpo. Status: pending-review.
- Source: [[papers/2509.06733]] | https://huggingface.co/papers/2509.06733
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.04575). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2509.04575]] | https://huggingface.co/papers/2509.04575
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12625). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.12625]] | https://huggingface.co/papers/2607.12625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.01055). Keywords: learning. Status: pending-review.
- Source: [[papers/2509.01055]] | https://huggingface.co/papers/2509.01055
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12395). Keywords: learning, sample efficiency. Status: pending-review.
- Source: [[papers/2607.12395]] | https://huggingface.co/papers/2607.12395
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.02547). Keywords: learning. Status: pending-review.
- Source: [[papers/2509.02547]] | https://huggingface.co/papers/2509.02547
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.10522). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.10522]] | https://huggingface.co/papers/2607.10522
- Confidence: Low (auto-matched, not yet reviewed)
  Neural Ne
- HF trending paper (arxiv: 2508.18921). Keywords: learning. Status: pending-review.
- Source: [[papers/2508.18921]] | https://huggingface.co/papers/2508.18921
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2508.11737). Keywords: curriculum, dpo, grpo. Status: pending-review.
- Source: [[papers/2508.11737]] | https://huggingface.co/papers/2508.11737
- Confidence: Low (auto-matched, not yet reviewed)
  Self-Optimized Al
- HF trending paper (arxiv: 2508.07750). Keywords: learning, sample efficiency, dpo, grpo. Status: pending-review.
- Source: [[papers/2508.07750]] | https://huggingface.co/papers/2508.07750
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.07508). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.07508]] | https://huggingface.co/papers/2607.07508
- Confidence: Low (auto-matched, not yet reviewed)
  Experi
- HF trending paper (arxiv: 2508.04700). Keywords: learning, curriculum, grpo. Status: pending-review.
- Source: [[papers/2508.04700]] | https://huggingface.co/papers/2508.04700
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.01232). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.01232]] | https://huggingface.co/papers/2607.01232
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05369). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.05369]] | https://huggingface.co/papers/2607.05369
- Confidence: Low (auto-matched, not yet reviewed)
  Large Lan
- HF trending paper (arxiv: 2507.07484). Keywords: learning, rlhf. Status: pending-review.
- Source: [[papers/2507.07484]] | https://huggingface.co/papers/2507.07484
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05391). Keywords: sample efficiency, grpo. Status: pending-review.
- Source: [[papers/2607.05391]] | https://huggingface.co/papers/2607.05391
- Confidence: Low (auto-matched, not yet reviewed)
  Foundati
- HF trending paper (arxiv: 2507.00951). Keywords: learning. Status: pending-review.
- Source: [[papers/2507.00951]] | https://huggingface.co/papers/2507.00951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.31036). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.31036]] | https://huggingface.co/papers/2606.31036
- Confidence: Low (auto-matched, not yet reviewed)
  Multi-Agent Mul
- HF trending paper (arxiv: 2506.24119). Keywords: learning, curriculum. Status: pending-review.
- Source: [[papers/2506.24119]] | https://huggingface.co/papers/2506.24119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.27821). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.27821]] | https://huggingface.co/papers/2606.27821
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.25178). Keywords: learning, curriculum, grpo. Status: pending-review.
- Source: [[papers/2606.25178]] | https://huggingface.co/papers/2606.25178
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.00407). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.00407]] | https://huggingface.co/papers/2607.00407
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.00924). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.00924]] | https://huggingface.co/papers/2607.00924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.29315). Keywords: learning. Status: pending-review.
- Source: [[papers/2606.29315]] | https://huggingface.co/papers/2606.29315
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.32017). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2606.32017]] | https://huggingface.co/papers/2606.32017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25108). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.25108]] | https://huggingface.co/papers/2607.25108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26115). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.26115]] | https://huggingface.co/papers/2607.26115
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26784). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.26784]] | https://huggingface.co/papers/2607.26784
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25659). Keywords: learning, grpo. Status: pending-review.
- Source: [[papers/2607.25659]] | https://huggingface.co/papers/2607.25659
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25294). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.25294]] | https://huggingface.co/papers/2607.25294
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27703). Keywords: learning. Status: pending-review.
- Source: [[papers/2607.27703]] | https://huggingface.co/papers/2607.27703
- Confidence: Low (auto-matched, not yet reviewed)
- Columnar compression on OHLCV data achieves 5-8x ratios (delta + zigzag + varint + FOR). 10yr 1-min OHLCV universe reduced from ~18GB to ~2.8GB. Enables in-memory backtests that previously required subsampling.
- Source: [[headroom-integration]]
- Confidence: High
