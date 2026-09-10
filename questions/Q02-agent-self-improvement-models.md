---
tags: [permanent-question, research]
created: 2026-05-25
question: "What are the frontier approaches for agents to improve their own scaffolding, tool use, and learning harness? Metalearning, self-critique, recursive improvement — what's working?"
date: 2026-05-25
type: permanent-question
reviewed: 2026-09-02
confidence: 0.95
evidence_count: 370
last_evidence_date: 2026-09-09
---


# Q02: Agent Self-Improvement Models

## Question
*What are the frontier approaches for agents to improve their own scaffolding, tool use, and learning harness? Metalearning, self-critique, recursive improvement — what's working?*

## Current State of Knowledge

### Core Idea: The Agent Improvement Stack
Agents can potentially improve at multiple levels:
1. **Prompt level** — Learn better instructions for themselves
2. **Tool level** — Synthesize new tools or compose existing ones better
3. **Memory level** — Build better knowledge structures from experience
4. **Reasoning level** — Improve how they think (Chain-of-Thought variants)
5. **Meta-level** — Improve their own improvement process itself

### What's Working

**Self-critique / Self-Reflection**
- Reflexion (Shinn et al.) — agent critiques own execution trace, stores lessons in semantic memory
- ReAct + self-reflection loops — model generates reasoning, evaluates it, revises
- Constitutional AI — model critiques itself against principles, self-aligns
- Evidence: self-critique improves performance on reasoning tasks by 15-30%

**Tool Use + Composition**
- Toolformer (Schick et al.) — LLM learns to invoke external tools
- HuggingGPT, ChatGPT plugins — LLM orchestrates multiple tools
- AutoGPT-style recursive task decomposition — agent breaks down goals, executes, revises
- Key insight: **tools extend cognition, not just capability.** A good tool-use framework is a cognitive scaffold.

**Memory-Augmented Agents**
- Memory is the key differentiator between stateless and stateful agents
- Types: episodic (past experiences), semantic (facts), procedural (how to do things)
- RAG (Retrieval-Augmented Generation) — most deployed approach
- Vector stores vs symbolic memory — hybrid is better
- HippoRAG (OIDC) —Episodic knowledge graph memory for agents

**Metalearning (Learning to Learn)**
- MAML (Model-Agnostic Metalearning) — find initialization that adapts fast to new tasks
- Problem: MAML is compute-heavy; not clearly applied to LLM-style agents yet
- What's closer: in-context metalearning — learning from few examples in context
- LLM compilers (Codex) show implicit metalearning via pre-training

**Recursive Self-Improvement**
- Most speculative. Current systems can improve at margins but not core architecture.
- Debate: Letta's "Compounding" agent — agent improves its own prompts over time
- Evidence: Human feedback (RLHF) is currently the best self-improvement mechanism for LLMs
|- Practical: Systematic prompt versioning + A/B testing + extracting lessons = "self-improvement"

**Self-Harness Paradigm**
|- The agent's own execution harness is the primary surface for self-improvement — not the LLM weights
|- Hermes Agent pioneered this: skill system allows agent to write, patch, and version its own abilities
|- Loops through: task -> tool-use -> reflection -> skill-patch -> retry — fully automated
|- Paradigm shift: instead of improving the model, improve the *agent runtime and tool ecosystem*
|- Key: the harness is legible (code), editable (patch tool), and testable (immediate execution feedback)

**Methodology-Loop**
|- Structured meta-cognitive workflow: plan -> execute -> reflect -> synthesize -> refine -> re-execute
|- Distinct from simple ReAct in that it *explicitly externalizes the improvement process* into files/memories
|- The loop is itself a methodology that gets iteratively improved (meta-methodology)
|- Codified in Hermes as the `methodology` skill — a repeatable template for any task class

**Critic Separation**
|- One critique pattern: the *executor* generates output, then a separate *critic* prompt evaluates it
|- Critic separation prevents the agent from rubber-stamping its own work (confirmation bias)
|- Best practice: different temperature, different model, or even different persona for critic vs actor
|- In Hermes: achieved via `temperature_review` or calling review in a separate agent turn with explicit criteria
|- Evidence from LLM-as-judge literature: separation improves evaluation accuracy by 20-40%

**Skill Auto-Patch**
|- When an agent's skill produces suboptimal results, the agent can auto-patch it mid-execution
|- Hermes `patch` tool enables this directly — agent reads its own skill files, identifies issues, patches
|- Triggers: reflection reveals a pattern of failure (e.g., "I always forget to sort before dedup")
|- Guardrails: patch is tested via re-execution; if the fix fails, rollback is automatically considered
|- This is the most concrete form of recursion we have: agent modifies its own ability to modify itself

**/goal Primitive**
|- A top-level goal primitive that the agent can reset, refactor, or decompose at any time
|- Provides a single point-of-truth for what the agent is currently trying to accomplish
|- Enables: goal-checking (am I still on track?), goal-refinement (this goal was too vague), goal-decomposition (break big goal into sub-goals)
|- In Hermes: the system prompt includes `current_goal` tracking; agent can rewrite its own goal mid-session
|- Critical for agents doing long-running autonomous work — prevents drift

**Memory Tiering**
- Not all memory is equally important. Agents benefit from explicit memory tiers:
  1. **Ephemeral** (current conversation context) — fast, small, volatile
  2. **Working** (session-level reflections, in-progress results) — lasts a session
  3. **Semantic** (facts, patterns, lessons across sessions) — persistent, retrievable
  4. **Procedural** (skills, methodologies, templates) — executable knowledge, versioned
  5. **Episodic** (full run traces with metadata) — auditable, replayable
- Tiering allows an agent to decide *what to remember* and *how fast to retrieve*, rather than drowning in uniform storage
- Hermes implements this via: `memories/` (episodic + procedural), skill files (procedural), and system prompt (working/ephemeral)

**The CL4R1T4S Dataset — 66 Leaked System Prompts as Self-Improvement Evidence**

The [[wiki/sources/cl4r1t4s-leaked-system-prompts|CL4R1T4S]] repository (maintained by Pliny/elder-plinius) contains 66 leaked system prompts from 26 major AI providers (Anthropic, OpenAI, xAI, Google, Devin, Cursor, Windsurf, Replit, etc.). This dataset reveals how the industry actually solves agent self-improvement in production:

| Pattern | Prevalence | Relevance to Q02 |
|---------|-----------|-----------------|
| Search-before-answer mandate | ~100% of 2026 prompts | Training-data insufficiency is universal — every provider independently concluded that static knowledge must be augmented by dynamic retrieval |
| Dynamic tool discovery | Sophisticated systems (Anthropic Fable 5/Opus 4.7, Hermes) | **The key architectural convergence.** Instead of static tool lists, tools are loaded on-demand via `tool_search` — identical to Hermes skill-loading ([[prompt-architecture-operations]]). The prompt lists visible tools as \"partial by design.\" |
| Skills pre-read mandate | Anthropic Fable 5 | \"Reading the relevant SKILL.md is a **required first step** before writing any code\" — independently converged with Hermes's mandatory skill-loading pattern in SOUL.md |
| Modular prompt sectioning | Anthropic (tag-based namespacing) | Enables A/B testing of prompt components — each section independently versioned. This is **prompt-level self-improvement infrastructure**: the prompt itself supports iterative improvement of its own components |
| Apology avoidance | 13 prompts (spreading) | Convergent UX research finding — excessive apology erodes trust. Minor but shows how shared behavioral patterns emerge across providers |

**Three key insights for agent self-improvement:**

1. **The prompt has become the product specification.** Claude Fable 5's 17.5K-word prompt is not just behavioral instructions — it's a 1,597-line document covering tool schemas (15+ JSON-schema), file system architecture, MCP connectors, API permissions, copyright enforcement, and safety protocols. The system prompt absorbs what would traditionally be product documentation, API specs, and integration guides. This confirms the Q02 thesis that **prompt-level** self-improvement is the most immediately impactful level — because the prompt *is* the product interface.

2. **Dynamic tool discovery is the dominant 2026 pattern.** Both Anthropic (Fable 5/Opus 4.7) and Hermes independently arrived at the same architecture: deferred capability loading. The prompt searches for tools the way it searches for information. This validates the design decisions in [[prompt-architecture-operations]] and confirms that **static tool lists don't scale** — any agent with a growing tool surface needs a capability resolution layer.

3. **Skills-environments are the convergence point.** The independent emergence of mandatory SKILL.md pre-read in both Anthropic Fable 5 and Hermes Agent is the strongest evidence yet that **externalized, environment-specific skill encoding** (rather than in-weight knowledge) is the right architecture for agent self-improvement. Both systems treat skill files as constraint documents encoding knowledge that isn't and shouldn't be in training data.

See: [[wiki/synthesis/system-prompt-arms-race]], [[concepts/system-prompt-architecture-patterns]], [[concepts/anthropic-system-prompt-evolution]], [[references/claude-fable-5-system-prompt]].

**Code World Models (CWM) for Toolchain Synthesis**

The [[concepts/code-world-models|Code World Model]] pattern (Lehrach et al., 2025, Google DeepMind) reframes LLMs from *direct actors* to *compilers* — translating natural language specifications into executable code, then handing off to classical solvers. This is directly relevant to Q02's "Tool level" of self-improvement:

- **Tool synthesis**: Instead of the LLM *using* a fixed toolset, it *generates* new tools (CWM functions) on-demand for each novel problem domain
- **Division of labor**: LLM handles semantic translation (natural language → code); classical solver (MCTS, constraints) handles multi-step reasoning
- **Verifiability**: CWM outputs are executable — correctness is decidable, not probabilistic

Applied to agent self-improvement: an agent that encounters a novel task class could CWM-compile the task rules into executable code, then iterate on the code rather than iterating on in-context prompting. This shifts self-improvement from "better prompting" to "better tool generation" — a higher-leverage level of the improvement stack.

See: [[papers/code-world-models-general-game-playing]], [[concepts/llm-as-compiler]], [[concepts/verifiable-planning]].

### What Doesn't Work (Yet)
- Fully autonomous code improvement (AI reviewing+modifying its own code) — too many failure modes
- Multi-agent competition causing rapid capability gain without careful design
- Agents reliably improving their own reasoning without external validation

## Key Papers
- Shinn et al. — "Reflexion: Language Agents with Verbal Reinforcement Learning"
- Schick et al. — "Toolformer: Language Models Can Teach Themselves to Use Tools"
- Yao et al. — "ReAct: Synergizing Reasoning and Acting in Language Models"
- Bai et al. — "Constitutional AI: Harmlessness from AI Feedback"
- Anand et al. — "Unleashing the Power of Agents with a Unified Memory System"
- Zhang et al. — "Self-Harness: Harnesses That Improve Themselves" (2026, arXiv:2606.09498) — Formalizes the Weakness Mining → Harness Proposal → Proposal Validation loop for model-specific harness self-improvement. The canonical paper for the Self-Harness paradigm discussed above.
- Lou et al. — "AutoHarness: Improving LLM Agents by Synthesizing a Code Harness" (2026, arXiv:2603.03329) — Automatic synthesis of code harnesses constraining agent actions to valid operations. Direct academic reference for agent harness automation.
- Pan et al. — "Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference" (2026, arXiv:2606.05922) — Improving agent harnesses without ground-truth validation using retrospective self-preference. Relevant to self-improvement in settings without explicit evaluators.

## Emerging Methodology

The most practical self-improvement loop for a personal agent:
1. **Task execution** — agent does something
2. **Reflection** — what went wrong? Log it.
3. **Memory update** — add to relevant skill/memory structure
4. **Prompt refinement** — update system prompt based on lessons
5. **Verification** — next run should improve

This is like a personal learning journal, but automated.

**For quantitative research agents specifically:**
- The agent should track which models/features worked on which market regimes
- Store failures explicitly (what went wrong, why, what to change next time)
- Build a "what we've tried" knowledge base

## Connections
- [[Q03]] — self-improvement is limited by learning speed
- [[Q06]] — more specific version: recursive improvement in agent harnesses
- [[loop-engineering]]
- [[memory-tiering]]
- [[methodology-loop]]
- [[wiki/synthesis/system-prompt-arms-race]] — CL4R1T4S dataset synthesis: 66 prompts reveal convergent evolution on dynamic tool discovery and skills pre-read
- [[concepts/system-prompt-architecture-patterns]] — Cross-cutting patterns from 66 leaked prompts
- [[concepts/anthropic-system-prompt-evolution]] — Anthropic's 3.5 → Fable 5 evolution as a case study in prompt-level self-improvement
- [[concepts/code-world-models]] — CWM pattern for toolchain synthesis by agent systems
- [[concepts/llm-as-compiler]] — LLM as translator → executable artifact → classical solver
- [[concepts/verifiable-planning]] — Why executability beats probability for agent decisions

## Last Updated
_2026-06-24_ — Added: CL4R1T4S dataset (66 leaked prompts, system prompt arms race, dynamic tool discovery convergence, skills pre-read mandate). Added CWM/LLM-as-compiler pattern for toolchain synthesis. Updated Connections with new references.
_2026-06-17_ — Added new papers (Self-Harness, AutoHarness, Evolving Agents in the Dark) to Key Papers section
_2026-06-13_ — Added June 2026 findings: causal AI pipeline deepening, Self-Harness applied, dashboard fixes, Headroom compression, /last30days skill, loop engineering

## Evidence Log

<!-- Weekly scan appends dated evidence blocks below this line.
     Format: ### YYYY-MM-DD: <topic>
             - Finding
             - Source: [[wikilink]] or URL
             - Confidence: High/Medium/Low
-->

### 2026-06-12: Self-Harness paradigm — harness is the improvement surface
- Hermes skill system lets agents write, patch, and version their own procedures. The execution harness (not LLM weights) is the primary surface for self-improvement.
- Source: [[self-harness]]
- Confidence: High

### 2026-06-17: Key papers: Self-Harness, AutoHarness, Evolving Agents in the Dark
- Three 2026 papers formalize harness self-improvement: Self-Harness (Weakness Mine → Harness Proposal → Validation), AutoHarness (code harness synthesis), Evolving Agents (self-preference optimization without ground truth).
- Source: arXiv:2606.09498, arXiv:2603.03329, arXiv:2606.05922
- Confidence: High

### 2026-06-24: CL4R1T4S — convergent architecture across 26 AI providers

### 2026-07-30: GPT-Red: Automated Red Teaming via Self-Play at Scale

### 2026-07-01: TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

### 2026-07-01: Hierarchical Experimentalist Agents

### 2025-07-01: SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via

### 2026-07-15: Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Vis

### 2025-09-03: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

### 2026-07-16: KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Ev

### 2025-09-08: Bootstrapping Task Spaces for Self-Improvement

### 2026-07-16: Self-Improvements in Modern Agentic Systems: A Survey

### 2026-07-20: SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcem

### 2025-09-29: WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level

### 2026-07-24: AREX: Towards a Recursively Self-Improving Agent for Deep Research

### 2025-10-01: Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified

### 2026-07-24: NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

### 2026-07-27: Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Lea

### 2025-10-08: Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and

### 2025-10-08: Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for

### 2025-10-14: Self-Improving LLM Agents at Test-Time

### 2025-10-29: SPICE: Self-Play In Corpus Environments Improves Reasoning

### 2025-11-07: Scaling Agent Learning via Experience Synthesis

### 2025-11-13: WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

### 2025-12-05: SIMA 2: A Generalist Embodied Agent for Virtual Worlds

### 2025-12-24: Reinforcement Learning for Self-Improving Agent with Skill Library

### 2026-01-08: MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecula

### 2026-01-23: From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantific

### 2026-01-27: Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability

### 2026-02-04: FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via Development-Oriente

### 2026-02-04: Scaling Small Agents Through Strategy Auctions

### 2026-02-09: Self-Improving World Modelling with Latent Actions

### 2026-02-12: Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters

### 2026-02-13: The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving

### 2026-03-03: Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data

### 2026-03-11: SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive

### 2026-04-14: TRACE: Capability-Targeted Agentic Training

### 2026-05-01: Synthetic Computers at Scale for Long-Horizon Productivity Simulation

### 2026-05-06: ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

### 2026-05-12: G-Zero: Self-Play for Open-Ended Generation from Zero Data

### 2026-05-18: Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design

### 2026-05-26: ECHO: Terminal Agents Learn World Models for Free

### 2026-05-28: OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

### 2026-06-03: Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories

### 2026-06-03: Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment 

### 2026-06-03: The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Develop

### 2026-06-08: CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

### 2026-06-15: From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomo

### 2026-06-15: StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning

### 2026-06-19: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

### 2026-07-01: TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

### 2026-07-01: Hierarchical Experimentalist Agents

### 2026-07-15: Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Vis

### 2026-07-16: KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Ev

### 2026-07-16: Self-Improvements in Modern Agentic Systems: A Survey

### 2026-07-24: AREX: Towards a Recursively Self-Improving Agent for Deep Research

### 2026-08-03: Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a Longitudina

### 2026-08-03: SAF-OPD: Stable Advantage Fusion for On-Policy Distillation

### 2026-08-03: RL^2-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for V

### 2026-08-03: Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocat

### 2026-08-03: In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous Driving

### 2026-08-03: One Future, Every Robot: Label-Efficient Collective-State Prediction with Decent

### 2026-08-03: SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark fo

### 2026-08-03: Enhancing Rubric-based RL via Self-Distillation

### 2026-08-03: Evaluation-Verification Reward for Consistent Multi-Reference Image Editing

### 2026-08-03: Meshy T2: Fast Native Mesh Generation with Flow Matching

### 2026-08-03: N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Token

### 2026-08-03: From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open

### 2026-08-03: β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation

### 2026-08-03: AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emot

### 2026-08-03: Multi-Head Attention Residuals

### 2026-08-03: LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structure

### 2026-08-03: Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Founda

### 2026-08-04: SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space

### 2026-08-04: Seeing or Knowing? Visual Context Sensitivity in Multimodal Large Language Model

### 2026-08-04: ICDAR 2026 Competition on Information Extraction from Atomic Layer Deposition/Et

### 2026-08-04: RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender System

### 2026-08-04: DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimo

### 2026-08-04: DAPD: Dual-Anchored Policy Distillation

### 2026-08-04: LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks

### 2026-08-04: LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation

### 2026-08-04: Progressive Agent Skill Generation via Reinforcement Learning

### 2026-08-04: WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reacti

### 2026-08-04: SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zer

### 2026-08-04: WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

### 2026-08-04: StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph

### 2026-08-04: Roomer: Reflective Object-Grounded Model Editing and Repair for 3D Indoor Layout

### 2026-08-04: Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous 

### 2026-08-04: VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Poli

### 2026-08-04: Weak-to-Strong On-Policy Distillation

### 2026-08-04: Constitutional Midtraining: Content Presence Drives Alignment Gains
- HF trending paper (arxiv: 2607.26654). Keywords: alignment. Status: pending-review.
- Source: [[papers/2607.26654]] | https://huggingface.co/papers/2607.26654
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26246). Keywords: distillation. Status: pending-review.
- Source: [[papers/2607.26246]] | https://huggingface.co/papers/2607.26246
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28590). Keywords: ppo, distillation. Status: pending-review.
- Source: [[papers/2607.28590]] | https://huggingface.co/papers/2607.28590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01755). Keywords: rlvr. Status: pending-review.
- Source: [[papers/2608.01755]] | https://huggingface.co/papers/2608.01755
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01973). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.01973]] | https://huggingface.co/papers/2608.01973
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01954). Keywords: preference learning. Status: pending-review.
- Source: [[papers/2608.01954]] | https://huggingface.co/papers/2608.01954
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29613). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2607.29613]] | https://huggingface.co/papers/2607.29613
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02023). Keywords: grpo, ppo, curriculum learning. Status: pending-review.
- Source: [[papers/2608.02023]] | https://huggingface.co/papers/2608.02023
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02603). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.02603]] | https://huggingface.co/papers/2608.02603
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01678). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.01678]] | https://huggingface.co/papers/2608.01678
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00079). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.00079]] | https://huggingface.co/papers/2608.00079
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01964). Keywords: agent loop, ppo. Status: pending-review.
- Source: [[papers/2608.01964]] | https://huggingface.co/papers/2608.01964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01735). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.01735]] | https://huggingface.co/papers/2608.01735
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01827). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.01827]] | https://huggingface.co/papers/2608.01827
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29241). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2607.29241]] | https://huggingface.co/papers/2607.29241
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26848). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.26848]] | https://huggingface.co/papers/2607.26848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26326). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.26326]] | https://huggingface.co/papers/2607.26326
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01397). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.01397]] | https://huggingface.co/papers/2608.01397
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28227). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.28227]] | https://huggingface.co/papers/2607.28227
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28374). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.28374]] | https://huggingface.co/papers/2607.28374
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27230). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.27230]] | https://huggingface.co/papers/2607.27230
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25289). Keywords: distillation. Status: pending-review.
- Source: [[papers/2607.25289]] | https://huggingface.co/papers/2607.25289
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28582). Keywords: reinforcement learning, policy optimization, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2607.28582]] | https://huggingface.co/papers/2607.28582
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23802). Keywords: self-improvement, self-play, reinforcement learning, reward model. Status: pending-review.
- Source: [[papers/2607.23802]] | https://huggingface.co/papers/2607.23802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23782). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2607.23782]] | https://huggingface.co/papers/2607.23782
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28675). Keywords: ppo. Status: pending-review.
- Source: [[papers/26
### 2026-08-05: Autonomous email triage with Bayesian sender trust, SPF/DKIM/DMARC authentication gate, and centralized safety reference for fraud, theft, and identity leakage.
- Source: [[email-safety-system.md]]
- Confidence: Medium

### 2026-08-05: Centralized blog draft pipeline: 2 active drafts, 12 verified candidates across 3 tiers, organized into thematic series.
- Source: [[blog-content-pipeline.md]]
- Confidence: Medium

### 2026-08-05: Self-maintaining personal knowledge graph: ~19,800 pages, 8 ingestion pipelines, cron-driven sync across GBrain + NotebookLM + Obsidian wiki.
- Source: [[gbrain-knowledge-ecosystem.md]]
- Confidence: Medium

### 2026-08-05: 13 MCP servers configured across Hermes, providing tools for search, code, finance, data, and automation. n8n deployed as visual automation layer. Docker infrastructure running.
- Source: [[mcp-infrastructure.md]]
- Confidence: High

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

### 2026-08-05: Applied causal inference (Pearl/DoWhy/EconML) for risk management and portfolio construction, building toward an autonomous causal hedge signal generator.
- Source: [[causal-ai-hedge-agent.md]]
- Confidence: Medium

### 2026-08-05: Live portfolio dashboard (port 5001) with allocation, concentration, tax-loss harvesting, and performance views.
- Source: [[portfolio-dashboard.md]]
- Confidence: Medium

### 2026-08-05: > **Skill stub** — auto-generated by knowledge-maintenance on 2026-08-02.
- Source: [[cross-linker.md]]
- Confidence: Medium

### 2026-08-05: Autonomous email triage with Bayesian sender trust, SPF/DKIM/DMARC authentication gate, and centralized safety reference for fraud, theft, and identit...
- Source: [[email-safety-system.md]]
- Confidence: Medium

### 2026-08-05: Self-maintaining personal knowledge graph: ~19,800 pages, 8 ingestion pipelines, cron-driven sync across GBrain + NotebookLM + Obsidian wiki.
- Source: [[gbrain-knowledge-ecosystem.md]]
- Confidence: Medium

### 2026-08-05: > **Skill stub** — auto-generated by knowledge-maintenance on 2026-08-02.
- Source: [[dify-ollama-embedding-setup.md]]
- Confidence: Medium

### 2026-08-05: > **Skill stub** — auto-generated by knowledge-maintenance on 2026-08-02.
- Source: [[gbrain-dual-layer-acl.md]]
- Confidence: Medium

### 2026-08-05: > **Skill stub** — auto-generated by knowledge-maintenance on 2026-08-02.
- Source: [[agent-subsystem-build.md]]
- Confidence: Medium

### 2026-08-05: Applied BINEVAL (binary question decomposition) methodology to 6 evaluation/critique skills. Created shared reference file. Each skill now decomposes ...
- Source: [[bineval-skill-patches.md]]
- Confidence: Medium

### 2026-08-05: 4-tier memory hierarchy for Hermes agent: HOT (session state), WARM (MEMORY.md), COOL (session search), COLD (GBrain/wikis). Implements importance-sco...

### 2026-08-05: RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic KV Cac

### 2026-08-05: MiniWorld: Democratizing the Training of Video World Models from Scratch

### 2026-08-05: ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

### 2026-08-05: When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, a

### 2026-08-05: Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

### 2026-08-05: PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Person

### 2026-08-05: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Lear

### 2026-08-05: CAPEval: A Decoupled Caption Evaluation across Understanding and Generation

### 2026-08-05: TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

### 2026-08-05: JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusi

### 2026-08-05: Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D Generation, Un

### 2026-08-05: SkillJack: Persistent Skill Backdoors in Self-Evolving Agents

### 2026-08-05: UniWorld-Design: From Pixel Generation to Layer-Native Design

### 2026-08-05: GROVE: Growing and Reasoning over Temporally Stratified Memory from Streaming Vi

### 2026-08-05: Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via Repre

### 2026-08-05: InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthe

### 2026-08-05: AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?

### 2026-08-05: MemSFT: Mitigating Alignment Tax with an External Parametric Memory

### 2026-08-05: Wnuan: Staged Post-Training for Question Answering over Proprietary Enterprise K

### 2026-08-06: DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial P

### 2026-08-06: Self-Evolving Coding Agents

### 2026-08-06: ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assi

### 2026-08-06: AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities

### 2026-08-06: Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data

### 2026-08-06: K-EXAONE 2.0 Technical Report

### 2026-08-06: Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from A

### 2026-08-06: BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Langua

### 2026-08-06: WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World 

### 2026-08-06: When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation

### 2026-08-06: The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monit

### 2026-08-06: Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horiz

### 2026-08-06: SKILL-KD: Contrastive Skill Distillation for LLM Agents

### 2026-08-06: ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation

### 2026-08-06: Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Ear

### 2026-08-06: Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Sele

### 2026-08-06: HelloWorld: Enabling Socially Interactive Characters in Video World Models

### 2026-08-06: OPD-V: Visual On-Policy Self-Distillation with Modality Balance

### 2026-08-06: Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking

### 2026-08-06: When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K C

### 2026-08-07: DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous 

### 2026-08-07: Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulu

### 2026-08-07: From Economic Agents to Agentic Economies: A Systems Blueprint for Economic Worl

### 2026-08-07: ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Con

### 2026-08-07: OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Re

### 2026-08-07: EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinf

### 2026-08-07: SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding

### 2026-08-07: CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

### 2026-08-07: AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

### 2026-08-07: On-Policy Delta Distillation for Multilingual Math Reasoning

### 2026-08-07: Recursive Synthesis for Long-Horizon Terminal Tasks

### 2026-08-07: Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised Wor

### 2026-08-08: GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splat

### 2026-08-10: Relevant but Incomplete: Referential Dangling as a Paradigm-Level Failure Mode i

### 2026-08-10: Adversarial Attacks for Good: A Survey of Proactive Protection across the Visual

### 2026-08-10: FATE: Frame-Level Audio-Visual Temporal Embedding

### 2026-08-10: Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chun

### 2026-08-10: OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understandi

### 2026-08-10: Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence

### 2026-08-10: Beyond Simply Environment Scaling: Designing Effective Environment Distributions

### 2026-08-10: SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task L

### 2026-08-10: Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning

### 2026-08-10: YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family

### 2026-08-10: When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Sel

### 2026-08-10: SimWAM: A Simple World Action Model for End-to-End Autonomous Driving

### 2026-08-10: The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, an

### 2026-08-11: The Loss Does Not See the Basis, but Adam Does

### 2026-08-11: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaborat

### 2026-08-11: Vision-Language Grounding as Bidirectional Concept Correspondence

### 2026-08-11: What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conve

### 2026-08-11: Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher

### 2026-08-11: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

### 2026-08-11: Factorized Hypothesis Search for Evidence-to-Taxonomy Retrieval

### 2026-08-12: Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness

### 2026-08-12: UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models

### 2026-08-12: AdvFD: Boosting Visual Generation via Adversarial Fr'echet Distance Loss

### 2026-08-12: Reference-Free Post-Training of Open Large Language Models for Multilingual Mach

### 2026-08-12: ComBodied Agents: a New Paradigm of Human-Centric Agentic AI

### 2026-08-12: iFAN: Inference-Aware Learning for Plain Mask Transformers

### 2026-08-12: SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discover

### 2026-08-12: SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Pe

### 2026-08-12: Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evo

### 2026-08-12: The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents

### 2026-08-12: On-Policy Self-Distillation without Any Supervision

### 2026-08-12: Business Arena: Benchmarking LLM Agents in a Realistic Marketplace

### 2026-08-12: MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation

### 2026-08-12: Omega-S: A Functional Resilience Index for LLM Fine-Tuning

### 2026-08-12: The Loss Does Not See the Basis, but Adam Does

### 2026-08-12: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaborat

### 2026-08-12: Vision-Language Grounding as Bidirectional Concept Correspondence

### 2026-08-12: What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conve

### 2026-08-12: Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher

### 2026-08-12: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

### 2026-08-12: Factorized Hypothesis Search for Evidence-to-Taxonomy Retrieval

### 2026-08-13: Parameter Exploration for RLVR via Variational Learning

### 2026-08-13: Ready Cohorts: Bounding GPU Opportunity and Avoiding Host Round Trips in LLM-Age

### 2026-08-13: Self-Evolving Embodied Agents via Skill-Harness Evolution

### 2026-08-13: AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

### 2026-08-13: From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-

### 2026-08-13: StateFlow: Building, Evolving, and Accessing 3D World States for Previsualizatio

### 2026-08-13: Agent Safety Should Be a Runtime Contract

### 2026-08-13: ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignme

### 2026-08-14: Context-Matched Distillation: Teacher Causality for Autoregressive Video Distill

### 2026-08-14: Mitigating Gender Bias in English to Romanian Machine Translation

### 2026-08-14: Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing

### 2026-08-14: PixSDS: Why Latent SDS Makes Noisy Pixels

### 2026-08-14: Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and 

### 2026-08-14: Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

### 2026-08-14: SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in 

### 2026-08-14: UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

### 2026-08-14: LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time

### 2026-08-14: DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

### 2026-08-14: Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intellige

### 2026-08-14: DarwinX: Evolving Agent Harnesses Through Natural Selection

### 2026-08-14: Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attent

### 2026-08-14: AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

### 2026-08-14: LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-

### 2026-08-14: Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

### 2026-08-14: How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in 

### 2026-08-14: Intern-S2-Preview: Scientific Agentic Foundation Model

### 2026-08-14: ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Fr

### 2026-08-17: Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models

### 2026-08-17: Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi

### 2026-08-17: A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientif

### 2026-08-17: UNMASK: Discovering and Causally Verifying Spurious Shortcuts in Text Classifier

### 2026-08-17: SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Rea

### 2026-08-17: UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Mu

### 2026-08-17: PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment

### 2026-08-17: Multimodal Model Diffing for Feature Discovery and Control

### 2026-08-17: CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Im

### 2026-08-17: Verifier-Induced Support Reshaping in On-Policy Optimization

### 2026-08-18: Valid Per-Field Selective Risk Control for Document Extraction: Three Failure Mo

### 2026-08-18: Plausible but Not Valid: A Psychometric Audit of LLMs as Synthetic Survey Respon

### 2026-08-18: GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective 

### 2026-08-18: WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Ri

### 2026-08-18: Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting f

### 2026-08-18: Drive, Pack, Fly: The Travelling Thief Problem with Drone

### 2026-08-18: UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrati

### 2026-08-18: Is this Citation on Point?
- HF trending paper (arxiv: 2608.12571). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.12571]] | https://huggingface.co/papers/2608.12571
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15930). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.15930]] | https://huggingface.co/papers/2608.15930
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16435). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.16435]] | https://huggingface.co/papers/2608.16435
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16072). Keywords: reinforcement learning, dpo, policy optimization. Status: pending-review.
- Source: [[papers/2608.16072]] | https://huggingface.co/papers/2608.16072
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15659). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.15659]] | https://huggingface.co/papers/2608.15659
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16328). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.16328]] | https://huggingface.co/papers/2608.16328
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14606). Keywords: bootstrap. Status: pending-review.
- Source: [[papers/2608.14606]] | https://huggingface.co/papers/2608.14606
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14639). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.14639]] | https://huggingface.co/papers/2608.14639
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00220). Keywords: reinforcement learning, dpo, ppo, policy optimization. Status: pending-review.
- Source: [[papers/2608.00220]] | https://huggingface.co/papers/2608.00220
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14546). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.14546]] | https://huggingface.co/papers/2608.14546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09928). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.09928]] | https://huggingface.co/papers/2608.09928
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14284). Keywords: reward model, ppo. Status: pending-review.
- Source: [[papers/2608.14284]] | https://huggingface.co/papers/2608.14284
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10835). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.10835]] | https://huggingface.co/papers/2608.10835
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14277). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.14277]] | https://huggingface.co/papers/2608.14277
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09209). Keywords: reward model. Status: pending-review.
- Source: [[papers/2608.09209]] | https://huggingface.co/papers/2608.09209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14075). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.14075]] | https://huggingface.co/papers/2608.14075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03744). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.03744]] | https://huggingface.co/papers/2608.03744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13760). Keywords: self-correction, alignment. Status: pending-review.
- Source: [[papers/2608.13760]] | https://huggingface.co/papers/2608.13760
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11045). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.11045]] | https://huggingface.co/papers/2608.11045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13505). Keywords: reinforcement learning, ppo, distillation. Status: pending-review.
- Source: [[papers/2608.13505]] | https://huggingface.co/papers/2608.13505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08975). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.08975]] | https://huggingface.co/papers/2608.08975
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13546). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.13546]] | https://huggingface.co/papers/2608.13546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12990). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.12990]] | https://huggingface.co/papers/2608.12990
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13560). Keywords: self-improvement, recursive self. Status: pending-review.
- Source: [[papers/2608.13560]] | https://huggingface.co/papers/2608.13560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12149). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.12149]] | https://huggingface.co/papers/2608.12149
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07545). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2608.07545]] | https://huggingface.co/papers/2608.07545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12743). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.12743]] | https://huggingface.co/papers/2608.12743
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13489). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.13489]] | https://huggingface.co/papers/2608.13489
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11745). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.11745]] | https://huggingface.co/papers/2608.11745
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11752). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.11752]] | https://huggingface.co/papers/2608.11752
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10538). Keywords: reinforcement learning, ppo. Status: pending-review.
- Source: [[papers/2608.10538]] | https://huggingface.co/papers/2608.10538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29211). Keywords: reinforcement learning, hindsight. Status: pending-review.
- Source: [[papers/2607.29211]] | https://huggingface.co/papers/2607.29211
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13430). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.13430]] | https://huggingface.co/papers/2608.13430
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12997). Keywords: ppo, distillation. Status: pending-review.
- Source: [[papers/2608.12997]] | https://huggingface.co/papers/2608.12997
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11660). Keywords: distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.11660]] | https://huggingface.co/papers/2608.11660
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08606). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.08606]] | https://huggingface.co/papers/2608.08606
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13391). Keywords: alignment, distillation. Status: pending-review.
- Source: [[papers/2608.13391]] | https://huggingface.co/papers/2608.13391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11878). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.11878]] | https://huggingface.co/papers/2608.11878
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11274). Keywords: constitutional ai, rlhf, dpo. Status: pending-review.
- Source: [[papers/2608.11274]] | https://huggingface.co/papers/2608.11274
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12314). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.12314]] | https://huggingface.co/papers/2608.12314
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11562). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.11562]] | https://huggingface.co/papers/2608.11562
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12307). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.12307]] | https://huggingface.co/papers/2608.12307
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11350). Keywords: reinforcement learning, self-evolving. Status: pending-review.
- Source: [[papers/2608.11350]] | https://huggingface.co/papers/2608.11350
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12123). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.12123]] | https://huggingface.co/papers/2608.12123
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09805). Keywords: reinforcement learning, grpo, policy optimization, rlvr. Status: pending-review.
- Source: [[papers/2608.09805]] | https://huggingface.co/papers/2608.09805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06614). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.06614]] | https://huggingface.co/papers/2608.06614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09853). Keywords: reward model. Status: pending-review.
- Source: [[papers/2608.09853]] | https://huggingface.co/papers/2608.09853
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07169). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.07169]] | https://huggingface.co/papers/2608.07169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07565). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.07565]] | https://huggingface.co/papers/2608.07565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07886). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.07886]] | https://huggingface.co/papers/2608.07886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03499). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.03499]] | https://huggingface.co/papers/2608.03499
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03887). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.03887]] | https://huggingface.co/papers/2608.03887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07463). Keywords: alignment, distillation. Status: pending-review.
- Source: [[papers/2608.07463]] | https://huggingface.co/papers/2608.07463
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08621). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.08621]] | https://huggingface.co/papers/2608.08621
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06296). Keywords: grpo, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.06296]] | https://huggingface.co/papers/2608.06296
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06065). Keywords: grpo, hindsight, distillation. Status: pending-review.
- Source: [[papers/2608.06065]] | https://huggingface.co/papers/2608.06065
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07645). Keywords: recursive self. Status: pending-review.
- Source: [[papers/2608.07645]] | https://huggingface.co/papers/2608.07645
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10692). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.10692]] | https://huggingface.co/papers/2608.10692
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11079). Keywords: self-evolving, ppo. Status: pending-review.
- Source: [[papers/2608.11079]] | https://huggingface.co/papers/2608.11079
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03216). Keywords: distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.03216]] | https://huggingface.co/papers/2608.03216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10915). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.10915]] | https://huggingface.co/papers/2608.10915
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10812). Keywords: reinforcement learning, grpo, policy optimization, distillation. Status: pending-review.
- Source: [[papers/2608.10812]] | https://huggingface.co/papers/2608.10812
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11205). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.11205]] | https://huggingface.co/papers/2608.11205
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08627). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.08627]] | https://huggingface.co/papers/2608.08627
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09900). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.09900]] | https://huggingface.co/papers/2608.09900
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06614). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.06614]] | https://huggingface.co/papers/2608.06614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09853). Keywords: reward model. Status: pending-review.
- Source: [[papers/2608.09853]] | https://huggingface.co/papers/2608.09853
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07169). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.07169]] | https://huggingface.co/papers/2608.07169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07565). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.07565]] | https://huggingface.co/papers/2608.07565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07886). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.07886]] | https://huggingface.co/papers/2608.07886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03499). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.03499]] | https://huggingface.co/papers/2608.03499
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06714). Keywords: agent loop. Status: pending-review.
- Source: [[papers/2608.06714]] | https://huggingface.co/papers/2608.06714
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07468). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.07468]] | https://huggingface.co/papers/2608.07468
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05219). Keywords: ppo, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.05219]] | https://huggingface.co/papers/2608.05219
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07051). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.07051]] | https://huggingface.co/papers/2608.07051
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02831). Keywords: reinforcement learning, self-evolving, verifiable reward. Status: pending-review.
- Source: [[papers/2608.02831]] | https://huggingface.co/papers/2608.02831
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03573). Keywords: reinforcement learning, policy optimization. Status: pending-review.
- Source: [[papers/2608.03573]] | https://huggingface.co/papers/2608.03573
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03571). Keywords: curriculum learning. Status: pending-review.
- Source: [[papers/2608.03571]] | https://huggingface.co/papers/2608.03571
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06756). Keywords: reinforcement learning, verifiable reward, distillation. Status: pending-review.
- Source: [[papers/2608.06756]] | https://huggingface.co/papers/2608.06756
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06013). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.06013]] | https://huggingface.co/papers/2608.06013
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03796). Keywords: ppo, distillation. Status: pending-review.
- Source: [[papers/2608.03796]] | https://huggingface.co/papers/2608.03796
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01310). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.01310]] | https://huggingface.co/papers/2608.01310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04314). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.04314]] | https://huggingface.co/papers/2608.04314
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04569). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.04569]] | https://huggingface.co/papers/2608.04569
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01492). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.01492]] | https://huggingface.co/papers/2608.01492
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04378). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.04378]] | https://huggingface.co/papers/2608.04378
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05466). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.05466]] | https://huggingface.co/papers/2608.05466
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05802). Keywords: reinforcement learning, distillation. Status: pending-review.
- Source: [[papers/2608.05802]] | https://huggingface.co/papers/2608.05802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05987). Keywords: reinforcement learning, recursive self, grpo, policy optimization. Status: pending-review.
- Source: [[papers/2608.05987]] | https://huggingface.co/papers/2608.05987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06352). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.06352]] | https://huggingface.co/papers/2608.06352
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05137). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.05137]] | https://huggingface.co/papers/2608.05137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06197). Keywords: reinforcement learning, ppo. Status: pending-review.
- Source: [[papers/2608.06197]] | https://huggingface.co/papers/2608.06197
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28609). Keywords: reinforcement learning, reward model, alignment. Status: pending-review.
- Source: [[papers/2607.28609]] | https://huggingface.co/papers/2607.28609
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04956). Keywords: ppo, distillation. Status: pending-review.
- Source: [[papers/2608.04956]] | https://huggingface.co/papers/2608.04956
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06020). Keywords: self-evolving, alignment, ppo. Status: pending-review.
- Source: [[papers/2608.06020]] | https://huggingface.co/papers/2608.06020
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01481). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.01481]] | https://huggingface.co/papers/2608.01481
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03451). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.03451]] | https://huggingface.co/papers/2608.03451
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03506). Keywords: reward model. Status: pending-review.
- Source: [[papers/2608.03506]] | https://huggingface.co/papers/2608.03506
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.00482). Keywords: self-correction, grpo. Status: pending-review.
- Source: [[papers/2607.00482]] | https://huggingface.co/papers/2607.00482
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05131). Keywords: distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.05131]] | https://huggingface.co/papers/2608.05131
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05070). Keywords: ppo, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.05070]] | https://huggingface.co/papers/2608.05070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04349). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.04349]] | https://huggingface.co/papers/2608.04349
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05000). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.05000]] | https://huggingface.co/papers/2608.05000
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04436). Keywords: reinforcement learning, grpo. Status: pending-review.
- Source: [[papers/2608.04436]] | https://huggingface.co/papers/2608.04436
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28048). Keywords: distillation. Status: pending-review.
- Source: [[papers/2607.28048]] | https://huggingface.co/papers/2607.28048
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05139). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.05139]] | https://huggingface.co/papers/2608.05139
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04570). Keywords: ppo, bootstrap. Status: pending-review.
- Source: [[papers/2608.04570]] | https://huggingface.co/papers/2608.04570
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03632). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.03632]] | https://huggingface.co/papers/2608.03632
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04964). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.04964]] | https://huggingface.co/papers/2608.04964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05042). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.05042]] | https://huggingface.co/papers/2608.05042
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00782). Keywords: reinforcement learning, grpo, policy optimization, verifiable reward. Status: pending-review.
- Source: [[papers/2608.00782]] | https://huggingface.co/papers/2608.00782
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04505). Keywords: dpo, ppo. Status: pending-review.
- Source: [[papers/2608.04505]] | https://huggingface.co/papers/2608.04505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02580). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.02580]] | https://huggingface.co/papers/2608.02580
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.24821). Keywords: alignment. Status: pending-review.
- Source: [[papers/2607.24821]] | https://huggingface.co/papers/2607.24821
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05102). Keywords: reinforcement learning, grpo. Status: pending-review.
- Source: [[papers/2608.05102]] | https://huggingface.co/papers/2608.05102
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03392). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2608.03392]] | https://huggingface.co/papers/2608.03392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03207). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.03207]] | https://huggingface.co/papers/2608.03207
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01862). Keywords: reinforcement learning, bootstrap. Status: pending-review.
- Source: [[papers/2608.01862]] | https://huggingface.co/papers/2608.01862
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25614). Keywords: alignment. Status: pending-review.
- Source: [[papers/2607.25614]] | https://huggingface.co/papers/2607.25614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00155). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2608.00155]] | https://huggingface.co/papers/2608.00155
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02437). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.02437]] | https://huggingface.co/papers/2608.02437
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03316). Keywords: ppo, distillation. Status: pending-review.
- Source: [[papers/2608.03316]] | https://huggingface.co/papers/2608.03316
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02392). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.02392]] | https://huggingface.co/papers/2608.02392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03971). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.03971]] | https://huggingface.co/papers/2608.03971
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03509). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2608.03509]] | https://huggingface.co/papers/2608.03509
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02711). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.02711]] | https://huggingface.co/papers/2608.02711
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03974). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.03974]] | https://huggingface.co/papers/2608.03974
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04007). Keywords: reinforcement learning, hindsight, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.04007]] | https://huggingface.co/papers/2608.04007
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02589). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.02589]] | https://huggingface.co/papers/2608.02589
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01837). Keywords: reinforcement learning, grpo, ppo, distillation. Status: pending-review.
- Source: [[papers/2608.01837]] | https://huggingface.co/papers/2608.01837
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04003). Keywords: self-improvement, agent loop, recursive self, ppo. Status: pending-review.
- Source: [[papers/2608.04003]] | https://huggingface.co/papers/2608.04003
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03979). Keywords: grpo, policy optimization. Status: pending-review.
- Source: [[papers/2608.03979]] | https://huggingface.co/papers/2608.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03700). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.03700]] | https://huggingface.co/papers/2608.03700
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03874). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.03874]] | https://huggingface.co/papers/2608.03874
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01127). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.01127]] | https://huggingface.co/papers/2608.01127
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01247). Keywords: distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.01247]] | https://huggingface.co/papers/2608.01247
- Confidence: Low (auto-matched, not yet reviewed)
- Source: [[memory-tier-system.md]]
- Confidence: Medium
07.28675]] | https://huggingface.co/papers/2607.28675
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29025). Keywords: reinforcement learning, reward model. Status: pending-review.
- Source: [[papers/2607.29025]] | https://huggingface.co/papers/2607.29025
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.18082). Keywords: policy optimization, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2607.18082]] | https://huggingface.co/papers/2607.18082
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28996). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.28996]] | https://huggingface.co/papers/2607.28996
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28443). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.28443]] | https://huggingface.co/papers/2607.28443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.15820). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.15820]] | https://huggingface.co/papers/2607.15820
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27888). Keywords: reinforcement learning, grpo, ppo, verifiable reward. Status: pending-review.
- Source: [[papers/2607.27888]] | https://huggingface.co/papers/2607.27888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26991). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2607.26991]] | https://huggingface.co/papers/2607.26991
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29209). Keywords: reinforcement learning, grpo, verifiable reward, rlvr. Status: pending-review.
- Source: [[papers/2607.29209]] | https://huggingface.co/papers/2607.29209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27851). Keywords: ppo. Status: pending-review.
- Source: [[papers/2607.27851]] | https://huggingface.co/papers/2607.27851
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21461). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.21461]] | https://huggingface.co/papers/2607.21461
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.13104). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.13104]] | https://huggingface.co/papers/2607.13104
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12625). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.12625]] | https://huggingface.co/papers/2607.12625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05382). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.05382]] | https://huggingface.co/papers/2607.05382
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.29315). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.29315]] | https://huggingface.co/papers/2606.29315
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.32017). Keywords: reinforcement learning agent. Status: pending-review.
- Source: [[papers/2606.32017]] | https://huggingface.co/papers/2606.32017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.19980). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.19980]] | https://huggingface.co/papers/2606.19980
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.18401). Keywords: reinforcement learning agent. Status: pending-review.
- Source: [[papers/2604.18401]] | https://huggingface.co/papers/2604.18401
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.14502). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.14502]] | https://huggingface.co/papers/2606.14502
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28742). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.28742]] | https://huggingface.co/papers/2605.28742
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.04455). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.04455]] | https://huggingface.co/papers/2606.04455
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.01770). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.01770]] | https://huggingface.co/papers/2606.01770
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03979). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.03979]] | https://huggingface.co/papers/2606.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28805). Keywords: self-correction. Status: pending-review.
- Source: [[papers/2605.28805]] | https://huggingface.co/papers/2605.28805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.24517). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.24517]] | https://huggingface.co/papers/2605.24517
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.15871). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.15871]] | https://huggingface.co/papers/2605.15871
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.09959). Keywords: self-improvement, self-play. Status: pending-review.
- Source: [[papers/2605.09959]] | https://huggingface.co/papers/2605.09959
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.03042). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.03042]] | https://huggingface.co/papers/2605.03042
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.28181). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2604.28181]] | https://huggingface.co/papers/2604.28181
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.05336). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2604.05336]] | https://huggingface.co/papers/2604.05336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.06333). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2603.06333]] | https://huggingface.co/papers/2603.06333
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.21320). Keywords: self-play. Status: pending-review.
- Source: [[papers/2602.21320]] | https://huggingface.co/papers/2602.21320
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.09877). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2602.09877]] | https://huggingface.co/papers/2602.09877
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.10604). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2602.10604]] | https://huggingface.co/papers/2602.10604
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06130). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2602.06130]] | https://huggingface.co/papers/2602.06130
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.02751). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2602.02751]] | https://huggingface.co/papers/2602.02751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.03798). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2602.03798]] | https://huggingface.co/papers/2602.03798
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.18778). Keywords: self-improvement, self-play. Status: pending-review.
- Source: [[papers/2601.18778]] | https://huggingface.co/papers/2601.18778
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.15690). Keywords: self-improvement, self-correction. Status: pending-review.
- Source: [[papers/2601.15690]] | https://huggingface.co/papers/2601.15690
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.02075). Keywords: self-correction. Status: pending-review.
- Source: [[papers/2601.02075]] | https://huggingface.co/papers/2601.02075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.17102). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2512.17102]] | https://huggingface.co/papers/2512.17102
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.04797). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2512.04797]] | https://huggingface.co/papers/2512.04797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.09515). Keywords: self-correction. Status: pending-review.
- Source: [[papers/2511.09515]] | https://huggingface.co/papers/2511.09515
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.03773). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2511.03773]] | https://huggingface.co/papers/2511.03773
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.24684). Keywords: self-improvement, self-play. Status: pending-review.
- Source: [[papers/2510.24684]] | https://huggingface.co/papers/2510.24684
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.07841). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2510.07841]] | https://huggingface.co/papers/2510.07841
- Confidence: Low (auto-matched, not yet reviewed)
  Academic P
- HF trending paper (arxiv: 2510.05571). Keywords: self-improvement, self-correction. Status: pending-review.
- Source: [[papers/2510.05571]] | https://huggingface.co/papers/2510.05571
- Confidence: Low (auto-matched, not yet reviewed)
  Synthesi
- HF trending paper (arxiv: 2509.24107). Keywords: self-play. Status: pending-review.
- Source: [[papers/2509.24107]] | https://huggingface.co/papers/2509.24107
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21653). Keywords: reinforcement learning agent. Status: pending-review.
- Source: [[papers/2607.21653]] | https://huggingface.co/papers/2607.21653
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.20709). Keywords: agent loop. Status: pending-review.
- Source: [[papers/2607.20709]] | https://huggingface.co/papers/2607.20709
- Confidence: Low (auto-matched, not yet reviewed)
  Self-Play
- HF trending paper (arxiv: 2509.25541). Keywords: self-improvement, self-play. Status: pending-review.
- Source: [[papers/2509.25541]] | https://huggingface.co/papers/2509.25541
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21461). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.21461]] | https://huggingface.co/papers/2607.21461
- Confidence: Low (auto-matched, not yet reviewed)
  Feedba
- HF trending paper (arxiv: 2509.22644). Keywords: reinforcement learning agent. Status: pending-review.
- Source: [[papers/2509.22644]] | https://huggingface.co/papers/2509.22644
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.10966). Keywords: self-correction. Status: pending-review.
- Source: [[papers/2607.10966]] | https://huggingface.co/papers/2607.10966
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.13104). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.13104]] | https://huggingface.co/papers/2607.13104
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.04575). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2509.04575]] | https://huggingface.co/papers/2509.04575
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12625). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.12625]] | https://huggingface.co/papers/2607.12625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.02547). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2509.02547]] | https://huggingface.co/papers/2509.02547
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05382). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.05382]] | https://huggingface.co/papers/2607.05382
- Confidence: Low (auto-matched, not yet reviewed)
  Multi-Agent Mul
- HF trending paper (arxiv: 2506.24119). Keywords: self-play. Status: pending-review.
- Source: [[papers/2506.24119]] | https://huggingface.co/papers/2506.24119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.29315). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2606.29315]] | https://huggingface.co/papers/2606.29315
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.32017). Keywords: reinforcement learning agent. Status: pending-review.
- Source: [[papers/2606.32017]] | https://huggingface.co/papers/2606.32017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26115). Keywords: self-improvement, self-play. Status: pending-review.
- Source: [[papers/2607.26115]] | https://huggingface.co/papers/2607.26115
- Confidence: Low (auto-matched, not yet reviewed)
- 66 leaked system prompts show convergent evolution: dynamic tool discovery (Anthropic + Hermes independently), mandatory skills pre-read, prompt as product spec. Validates skill-based self-improvement as industry-standard pattern.
- Source: [[wiki/sources/cl4r1t4s-leaked-system-prompts]]
- Confidence: High

### 2026-08-19: Scaffold compression via causal masking — E2-Explainer (arXiv:2608.12921)

### 2026-08-19: V-RAE: Rethinking Video Latent Spaces for Generation

### 2026-08-19: Demystifying Agent Skills: Why They Work-Until They Don't

### 2026-08-19: Cross-Model Memory Transfer via Target-Side Reader Adaptation

### 2026-08-19: CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Gu

### 2026-08-19: MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Ve

### 2026-08-19: Agent Lightning v1.0: Towards Harnessed Agentic RL

### 2026-08-19: FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution

### 2026-08-19: Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation

### 2026-08-19: Energy-Guided Flow Matching

### 2026-08-19: Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Ind

### 2026-08-19: From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

### 2026-08-19: Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements

### 2026-08-20: SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents

### 2026-08-20: The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning

### 2026-08-20: Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

### 2026-08-20: Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical In

### 2026-08-20: Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditi

### 2026-08-20: FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents

### 2026-08-20: SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution

### 2026-08-20: LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents

### 2026-08-21: Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Har

### 2026-08-21: CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical 

### 2026-08-21: Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accura

### 2026-08-21: FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving

### 2026-08-21: SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback

### 2026-08-21: Repo0: Design-Driven Zero-to-All Code Generation

### 2026-08-21: Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowled

### 2026-08-21: ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World

### 2026-08-21: FACET: Preserving Source Intent and Executable State in Terminal Task Synthesis

### 2026-08-21: EXIMO: VLM Guided Exploration of VLA Policies

### 2026-08-21: PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-C

### 2026-08-21: VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio 

### 2026-08-21: LLMs Get Smarter from Targeted Synthetic Multilingual Data

### 2026-08-22: FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executab

### 2026-08-22: The Embedder's Dilemma: LLMs Are Better, but at What Cost?

### 2026-08-24: Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but No R

### 2026-08-24: Hydra-0: Action Flow for Generalist World Modeling and Control

### 2026-08-24: FlavourBench: Ranking Frontier Language Models with Executable Culinary Ground T

### 2026-08-24: Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference

### 2026-08-24: Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Dist

### 2026-08-24: AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Sce

### 2026-08-24: Hadith computational science in the age of large language models: a critical nar

### 2026-08-24: Towards Faithful Simulation of Human Shopping Behavior

### 2026-08-24: Graph Engineering in the Era of LLM Agents: From Individual Intelligence to Syst

### 2026-08-24: CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Align

### 2026-08-24: Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Think

### 2026-08-25: Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit 

### 2026-08-25: EXPL-FR: Explaining Face Recognition Models via Vision-Language Alignment

### 2026-08-25: Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning 

### 2026-08-25: Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM P

### 2026-08-25: EchoWM: Open and Enterable Omnimodal World Models

### 2026-08-25: One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents i

### 2026-08-25: MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks

### 2026-08-25: ReWorld: An Interactive World Model with Long-Horizon Memory

### 2026-08-25: Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress

### 2026-08-25: TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration

### 2026-08-25: Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Chu

### 2026-08-25: RISE: Adaptive Imagination for World Action Models

### 2026-08-25: TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming
- HF trending paper (arxiv: 2608.20958). Keywords: alignment, grpo, ppo. Status: pending-review.
- Source: [[papers/2608.20958]] | https://huggingface.co/papers/2608.20958
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20430). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.20430]] | https://huggingface.co/papers/2608.20430
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22856). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.22856]] | https://huggingface.co/papers/2608.22856
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17336). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.17336]] | https://huggingface.co/papers/2608.17336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19408). Keywords: policy optimization, distillation. Status: pending-review.
- Source: [[papers/2608.19408]] | https://huggingface.co/papers/2608.19408
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23565). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.23565]] | https://huggingface.co/papers/2608.23565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23035). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.23035]] | https://huggingface.co/papers/2608.23035
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19741). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.19741]] | https://huggingface.co/papers/2608.19741
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23189). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.23189]] | https://huggingface.co/papers/2608.23189
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23311). Keywords: grpo, ppo, policy optimization. Status: pending-review.
- Source: [[papers/2608.23311]] | https://huggingface.co/papers/2608.23311
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22817). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.22817]] | https://huggingface.co/papers/2608.22817
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21486). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.21486]] | https://huggingface.co/papers/2608.21486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20953). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.20953]] | https://huggingface.co/papers/2608.20953
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12781). Keywords: reinforcement learning, reward model, alignment. Status: pending-review.
- Source: [[papers/2608.12781]] | https://huggingface.co/papers/2608.12781
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21278). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.21278]] | https://huggingface.co/papers/2608.21278
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21156). Keywords: self-improvement, ppo. Status: pending-review.
- Source: [[papers/2608.21156]] | https://huggingface.co/papers/2608.21156
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20707). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.20707]] | https://huggingface.co/papers/2608.20707
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20364). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.20364]] | https://huggingface.co/papers/2608.20364
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20634). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.20634]] | https://huggingface.co/papers/2608.20634
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16647). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.16647]] | https://huggingface.co/papers/2608.16647
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20210). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.20210]] | https://huggingface.co/papers/2608.20210
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20574). Keywords: dpo, bootstrap. Status: pending-review.
- Source: [[papers/2608.20574]] | https://huggingface.co/papers/2608.20574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18077). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.18077]] | https://huggingface.co/papers/2608.18077
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20438). Keywords: ppo, bootstrap. Status: pending-review.
- Source: [[papers/2608.20438]] | https://huggingface.co/papers/2608.20438
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12875). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.12875]] | https://huggingface.co/papers/2608.12875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21596). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2607.21596]] | https://huggingface.co/papers/2607.21596
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15964). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.15964]] | https://huggingface.co/papers/2608.15964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18607). Keywords: reinforcement learning, reward model. Status: pending-review.
- Source: [[papers/2608.18607]] | https://huggingface.co/papers/2608.18607
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19861). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.19861]] | https://huggingface.co/papers/2608.19861
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19891). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.19891]] | https://huggingface.co/papers/2608.19891
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18580). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.18580]] | https://huggingface.co/papers/2608.18580
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14022). Keywords: ppo, distillation. Status: pending-review.
- Source: [[papers/2608.14022]] | https://huggingface.co/papers/2608.14022
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20281). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.20281]] | https://huggingface.co/papers/2608.20281
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19854). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.19854]] | https://huggingface.co/papers/2608.19854
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13120). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.13120]] | https://huggingface.co/papers/2608.13120
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19758). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.19758]] | https://huggingface.co/papers/2608.19758
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17744). Keywords: reinforcement learning, verifiable reward. Status: pending-review.
- Source: [[papers/2608.17744]] | https://huggingface.co/papers/2608.17744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19776). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.19776]] | https://huggingface.co/papers/2608.19776
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08466). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2608.08466]] | https://huggingface.co/papers/2608.08466
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17393). Keywords: reinforcement learning, alignment. Status: pending-review.
- Source: [[papers/2608.17393]] | https://huggingface.co/papers/2608.17393
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18933). Keywords: self-evolving, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.18933]] | https://huggingface.co/papers/2608.18933
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18423). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.18423]] | https://huggingface.co/papers/2608.18423
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18746). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.18746]] | https://huggingface.co/papers/2608.18746
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16590). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2608.16590]] | https://huggingface.co/papers/2608.16590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17253). Keywords: reinforcement learning, verifiable reward. Status: pending-review.
- Source: [[papers/2608.17253]] | https://huggingface.co/papers/2608.17253
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14229). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.14229]] | https://huggingface.co/papers/2608.14229
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18852). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.18852]] | https://huggingface.co/papers/2608.18852
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17310). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.17310]] | https://huggingface.co/papers/2608.17310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16002). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.16002]] | https://huggingface.co/papers/2608.16002
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16393). Keywords: agent loop. Status: pending-review.
- Source: [[papers/2608.16393]] | https://huggingface.co/papers/2608.16393
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05811). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.05811]] | https://huggingface.co/papers/2608.05811
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17512). Keywords: alignment, grpo, policy optimization. Status: pending-review.
- Source: [[papers/2608.17512]] | https://huggingface.co/papers/2608.17512
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16157). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.16157]] | https://huggingface.co/papers/2608.16157
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17528). Keywords: dpo, ppo. Status: pending-review.
- Source: [[papers/2608.17528]] | https://huggingface.co/papers/2608.17528
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14221). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.14221]] | https://huggingface.co/papers/2608.14221
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17566). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.17566]] | https://huggingface.co/papers/2608.17566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17050). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.17050]] | https://huggingface.co/papers/2608.17050
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14036). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2608.14036]] | https://huggingface.co/papers/2608.14036
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13556). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.13556]] | https://huggingface.co/papers/2608.13556
- Confidence: Low (auto-matched, not yet reviewed)
- Granger-style edge masking identifies minimal communication subgraphs that preserve task outcome; pruning them cuts communication cost at competitive performance — scaffold optimization by intervention rather than observation, with an amortized explainer distilled for cheap post-hoc topology selection.
- Source: [[papers/e2-explainer-mas-topologies]]
- Confidence: High

### 2026-08-24: One Recipe, Many Harnesses — self-evolution recipe held fixed across 8 languages x 3 models

### 2026-08-26: GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with 

### 2026-08-26: DREAM Technical Report

### 2026-08-26: Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video

### 2026-08-26: WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report

### 2026-08-26: Length-Adaptive Decoding for Masked Diffusion Machine Translation

### 2026-08-26: Best Practice Critic Optimization

### 2026-08-26: On-policy Distillation with Verifiable Reward

### 2026-08-26: Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses

### 2026-08-26: Meta^n: Recursive Self-Improvement through Emergent Depth

### 2026-08-26: ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Froz

### 2026-08-27: Skill Issue: Are Skills Language-Invariant in LLMs?

### 2026-08-27: Prefix Sliding for efficient test-time scaling

### 2026-08-27: LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech De

### 2026-08-27: RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieva

### 2026-08-27: Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategie

### 2026-08-27: Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worl

### 2026-08-27: FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling

### 2026-08-27: Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation

### 2026-08-27: WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploratio

### 2026-08-27: MA-VLA: Multi-Arm Vision-Language-Action Model for Collaboration and Composition

### 2026-08-27: StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Mode

### 2026-08-27: Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy

### 2026-08-27: V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning

### 2026-08-27: Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agen

### 2026-08-27: Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans

### 2026-08-27: Agent-G^2: Gaussian Guidance for Agentic Reinforcement Learning

### 2026-08-27: Code World Model: Coding Agent as World Brain

### 2026-08-27: VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning

### 2026-08-28: EditaLive! Unified Character Video Editing for Live Streaming

### 2026-08-28: Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling Worl

### 2026-08-28: GameWAM: A World Action Model for Video Games

### 2026-08-28: TTPO: Test-Time Policy Optimization

### 2026-08-28: Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reaso

### 2026-08-28: Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Techn

### 2026-08-28: PAWBench: How Far Are We from Probabilistically Aligned World Modeling?

### 2026-08-28: UrbanGround: From Local Perception to Spatial Agency in a Real-Scale City

### 2026-08-28: Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher

### 2026-08-28: Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage

### 2026-08-28: What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents

### 2026-08-28: GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Gro

### 2026-08-30: Luce: Relightable Gaussians for 3D Asset Generation

### 2026-08-31: Language Chain in Alignment: Cross-lingual Ranking Preference Optimization

### 2026-08-31: Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities

### 2026-08-31: DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation of Mu

### 2026-08-31: LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in V

### 2026-08-31: J-Zero: Unified Challenger--Solver--Judge Co-Evolution from Zero Data

### 2026-08-31: StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-U

### 2026-09-01: DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution

### 2026-09-01: SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Mo

### 2026-09-01: LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigatio

### 2026-09-01: WebWorld: The Browser as a World Model for Self-Improving Web Code

### 2026-09-01: Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation

### 2026-09-01: Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied

### 2026-09-01: SHAPE of Chain-of-Thought in Math Reasoning

### 2026-09-01: Dynamic Important Example Mining for Reinforcement Finetuning

### 2026-09-01: CogEvol: Towards Efficient and Reliable Learning Environment Generation

### 2026-09-01: Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superinte

### 2026-09-01: PaperGym: Rubric-Centered Evolution for Research-Plan Generation

### 2026-09-02: From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers

### 2026-09-02: Recursive Criticality of AI Self-Improvement

### 2026-09-02: Safin-1: Safety from Within through Memory-Native State Evolution

### 2026-09-02: H3-World: Turning Language Understanding into World Control

### 2026-09-02: StudentSim: Training LLM-based Student Simulators

### 2026-09-02: Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models:

### 2026-09-02: ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Trans

### 2026-09-02: InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Rei

### 2026-09-02: The Mechanics of Democratic Dominance: A System Dynamics Paradigm for Dynamic Co

### 2026-09-03: Wasserstein-Barycentric Interaction Fields for Spatial Factor Models: Evidence f

### 2026-09-03: NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Eff

### 2026-09-03: Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Qu

### 2026-09-03: A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss

### 2026-09-03: Aspire: Can Models Self-Evolve from Vague Goals?

### 2026-09-03: S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?

### 2026-09-03: Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills

### 2026-09-03: EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction

### 2026-09-03: Post-Training Language Models for Gold-Medal Performance in Coding Competitions

### 2026-09-03: PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specificat

### 2026-09-03: ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrie

### 2026-09-03: MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information

### 2026-09-03: SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

### 2026-09-03: Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Tok

### 2026-09-03: Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall

### 2026-09-03: AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agent

### 2026-09-04: DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agen

### 2026-09-04: QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentati

### 2026-09-04: Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Pos

### 2026-09-04: Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States

### 2026-09-04: The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Vide

### 2026-09-04: FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow

### 2026-09-04: WorldReward: Reward Modeling for Camera-Conditioned World Models

### 2026-09-04: Rethinking On-Policy Distillation of Large Language Models II: One Training Exam

### 2026-09-04: Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Hal

### 2026-09-04: An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender Sys

### 2026-09-04: Small Language Models as Judges for Rubric-Based Reinforcement Learning

### 2026-09-05: A Common Measure of Communication for Speech Brain-Computer Interfaces

### 2026-09-05: VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement

### 2026-09-05: Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space

### 2026-09-07: Dr. Claw: An AI Scientist Workspace for Vibe Research

### 2026-09-07: UniMate: One Unified Model to Animate Diverse Skeletons

### 2026-09-07: One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Edit

### 2026-09-07: Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reason

### 2026-09-07: Training-Free Speech-Centric Omni Understanding with Frozen VLMs

### 2026-09-07: The Attention Triangle in Audio-Video Models

### 2026-09-07: Enoki: Efficient Multi-Level Hallucination Detection

### 2026-09-07: Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive O

### 2026-09-07: Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue

### 2026-09-07: When Models Edit Too Much: On the Fidelity of Minimal Code Edits

### 2026-09-07: RISE: Recursive Improvement via Self-Extrapolating Policy Distillation

### 2026-09-07: Group Adaptive Clipping Policy Optimization

### 2026-09-08: Safety for Whom? Boundary-Aware Self-Distillation for Controlled LLM Safety Refu

### 2026-09-08: One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation

### 2026-09-08: EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying V

### 2026-09-08: FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experie

### 2026-09-08: Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillatio

### 2026-09-08: Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning
- HF trending paper (arxiv: 2609.03729). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2609.03729]] | https://huggingface.co/papers/2609.03729
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02998). Keywords: grpo, distillation. Status: pending-review.
- Source: [[papers/2609.02998]] | https://huggingface.co/papers/2609.02998
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03241). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2609.03241]] | https://huggingface.co/papers/2609.03241
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01281). Keywords: agent loop, ppo. Status: pending-review.
- Source: [[papers/2609.01281]] | https://huggingface.co/papers/2609.01281
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25936). Keywords: reinforcement learning, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.25936]] | https://huggingface.co/papers/2608.25936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04482). Keywords: alignment, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2609.04482]] | https://huggingface.co/papers/2609.04482
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00444). Keywords: reinforcement learning, grpo, ppo, policy optimization. Status: pending-review.
- Source: [[papers/2609.00444]] | https://huggingface.co/papers/2609.00444
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05295). Keywords: rlvr, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2609.05295]] | https://huggingface.co/papers/2609.05295
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04061). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2609.04061]] | https://huggingface.co/papers/2609.04061
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04250). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.04250]] | https://huggingface.co/papers/2609.04250
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05258). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.05258]] | https://huggingface.co/papers/2609.05258
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00581). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2609.00581]] | https://huggingface.co/papers/2609.00581
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03586). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2609.03586]] | https://huggingface.co/papers/2609.03586
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04242). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.04242]] | https://huggingface.co/papers/2609.04242
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04753). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.04753]] | https://huggingface.co/papers/2609.04753
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04190). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.04190]] | https://huggingface.co/papers/2609.04190
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05415). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.05415]] | https://huggingface.co/papers/2609.05415
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00365). Keywords: skill library. Status: pending-review.
- Source: [[papers/2609.00365]] | https://huggingface.co/papers/2609.00365
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29188). Keywords: reinforcement learning, dpo, grpo, ppo. Status: pending-review.
- Source: [[papers/2608.29188]] | https://huggingface.co/papers/2608.29188
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03153). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.03153]] | https://huggingface.co/papers/2609.03153
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02887). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.02887]] | https://huggingface.co/papers/2609.02887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30005). Keywords: reinforcement learning, reward model, grpo. Status: pending-review.
- Source: [[papers/2608.30005]] | https://huggingface.co/papers/2608.30005
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2504.15476). Keywords: bootstrap. Status: pending-review.
- Source: [[papers/2504.15476]] | https://huggingface.co/papers/2504.15476
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04098). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.04098]] | https://huggingface.co/papers/2609.04098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04172). Keywords: alignment, distillation. Status: pending-review.
- Source: [[papers/2609.04172]] | https://huggingface.co/papers/2609.04172
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03952). Keywords: reward model. Status: pending-review.
- Source: [[papers/2609.03952]] | https://huggingface.co/papers/2609.03952
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03563). Keywords: alignment, distillation. Status: pending-review.
- Source: [[papers/2609.03563]] | https://huggingface.co/papers/2609.03563
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02367). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.02367]] | https://huggingface.co/papers/2609.02367
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04196). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.04196]] | https://huggingface.co/papers/2609.04196
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26730). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.26730]] | https://huggingface.co/papers/2608.26730
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29253). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.29253]] | https://huggingface.co/papers/2608.29253
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04094). Keywords: reinforcement learning, grpo, verifiable reward. Status: pending-review.
- Source: [[papers/2609.04094]] | https://huggingface.co/papers/2609.04094
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26623). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.26623]] | https://huggingface.co/papers/2608.26623
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01532). Keywords: distillation. Status: pending-review.
- Source: [[papers/2609.01532]] | https://huggingface.co/papers/2609.01532
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29846). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.29846]] | https://huggingface.co/papers/2608.29846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02886). Keywords: distillation. Status: pending-review.
- Source: [[papers/2609.02886]] | https://huggingface.co/papers/2609.02886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30949). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.30949]] | https://huggingface.co/papers/2608.30949
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01865). Keywords: bootstrap. Status: pending-review.
- Source: [[papers/2609.01865]] | https://huggingface.co/papers/2609.01865
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02272). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.02272]] | https://huggingface.co/papers/2609.02272
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02849). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2609.02849]] | https://huggingface.co/papers/2609.02849
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02783). Keywords: distillation. Status: pending-review.
- Source: [[papers/2609.02783]] | https://huggingface.co/papers/2609.02783
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02749). Keywords: skill library, distillation. Status: pending-review.
- Source: [[papers/2609.02749]] | https://huggingface.co/papers/2609.02749
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31100). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2608.31100]] | https://huggingface.co/papers/2608.31100
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31111). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.31111]] | https://huggingface.co/papers/2608.31111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00591). Keywords: grpo. Status: pending-review.
- Source: [[papers/2609.00591]] | https://huggingface.co/papers/2609.00591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21450). Keywords: alignment, distillation. Status: pending-review.
- Source: [[papers/2608.21450]] | https://huggingface.co/papers/2608.21450
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01657). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.01657]] | https://huggingface.co/papers/2609.01657
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29669). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.29669]] | https://huggingface.co/papers/2608.29669
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27509). Keywords: dpo. Status: pending-review.
- Source: [[papers/2608.27509]] | https://huggingface.co/papers/2608.27509
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28612). Keywords: reinforcement learning, alignment. Status: pending-review.
- Source: [[papers/2608.28612]] | https://huggingface.co/papers/2608.28612
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00968). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.00968]] | https://huggingface.co/papers/2609.00968
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01607). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.01607]] | https://huggingface.co/papers/2609.01607
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01591). Keywords: reinforcement learning, reward model. Status: pending-review.
- Source: [[papers/2609.01591]] | https://huggingface.co/papers/2609.01591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01560). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.01560]] | https://huggingface.co/papers/2609.01560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00092). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2609.00092]] | https://huggingface.co/papers/2609.00092
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00137). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2609.00137]] | https://huggingface.co/papers/2609.00137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01572). Keywords: grpo. Status: pending-review.
- Source: [[papers/2609.01572]] | https://huggingface.co/papers/2609.01572
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31119). Keywords: reinforcement learning, grpo. Status: pending-review.
- Source: [[papers/2608.31119]] | https://huggingface.co/papers/2608.31119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31075). Keywords: reinforcement learning, verifiable reward, rlvr. Status: pending-review.
- Source: [[papers/2608.31075]] | https://huggingface.co/papers/2608.31075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30968). Keywords: grpo. Status: pending-review.
- Source: [[papers/2608.30968]] | https://huggingface.co/papers/2608.30968
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29252). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.29252]] | https://huggingface.co/papers/2608.29252
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28600). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.28600]] | https://huggingface.co/papers/2608.28600
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30428). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.30428]] | https://huggingface.co/papers/2608.30428
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24293). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.24293]] | https://huggingface.co/papers/2608.24293
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30530). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2608.30530]] | https://huggingface.co/papers/2608.30530
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30935). Keywords: reinforcement learning, ppo. Status: pending-review.
- Source: [[papers/2608.30935]] | https://huggingface.co/papers/2608.30935
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29098). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.29098]] | https://huggingface.co/papers/2608.29098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31106). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.31106]] | https://huggingface.co/papers/2608.31106
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24777). Keywords: grpo. Status: pending-review.
- Source: [[papers/2608.24777]] | https://huggingface.co/papers/2608.24777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26582). Keywords: self-improvement, self-evolving, ppo. Status: pending-review.
- Source: [[papers/2608.26582]] | https://huggingface.co/papers/2608.26582
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28460). Keywords: self-correction. Status: pending-review.
- Source: [[papers/2608.28460]] | https://huggingface.co/papers/2608.28460
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18524). Keywords: ppo, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.18524]] | https://huggingface.co/papers/2608.18524
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28122). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.28122]] | https://huggingface.co/papers/2608.28122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23149). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.23149]] | https://huggingface.co/papers/2608.23149
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23943). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.23943]] | https://huggingface.co/papers/2608.23943
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21832). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.21832]] | https://huggingface.co/papers/2608.21832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27260). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.27260]] | https://huggingface.co/papers/2608.27260
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27351). Keywords: grpo, policy optimization. Status: pending-review.
- Source: [[papers/2608.27351]] | https://huggingface.co/papers/2608.27351
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26872). Keywords: alignment, distillation. Status: pending-review.
- Source: [[papers/2608.26872]] | https://huggingface.co/papers/2608.26872
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27456). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.27456]] | https://huggingface.co/papers/2608.27456
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27345). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.27345]] | https://huggingface.co/papers/2608.27345
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15763). Keywords: reinforcement learning, distillation. Status: pending-review.
- Source: [[papers/2608.15763]] | https://huggingface.co/papers/2608.15763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26993). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.26993]] | https://huggingface.co/papers/2608.26993
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27448). Keywords: reinforcement learning, policy optimization, distillation, self-distillation. Status: pending-review.
- Source: [[papers/2608.27448]] | https://huggingface.co/papers/2608.27448
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26200). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.26200]] | https://huggingface.co/papers/2608.26200
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25518). Keywords: reinforcement learning, ppo. Status: pending-review.
- Source: [[papers/2608.25518]] | https://huggingface.co/papers/2608.25518
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27123). Keywords: distillation. Status: pending-review.
- Source: [[papers/2608.27123]] | https://huggingface.co/papers/2608.27123
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26105). Keywords: reinforcement learning, alignment, verifiable reward. Status: pending-review.
- Source: [[papers/2608.26105]] | https://huggingface.co/papers/2608.26105
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25927). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.25927]] | https://huggingface.co/papers/2608.25927
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23318). Keywords: reinforcement learning, policy optimization. Status: pending-review.
- Source: [[papers/2608.23318]] | https://huggingface.co/papers/2608.23318
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24909). Keywords: self-evolving, ppo. Status: pending-review.
- Source: [[papers/2608.24909]] | https://huggingface.co/papers/2608.24909
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24099). Keywords: reinforcement learning, grpo. Status: pending-review.
- Source: [[papers/2608.24099]] | https://huggingface.co/papers/2608.24099
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25580). Keywords: reinforcement learning, grpo, ppo. Status: pending-review.
- Source: [[papers/2608.25580]] | https://huggingface.co/papers/2608.25580
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19098). Keywords: reinforcement learning, distillation. Status: pending-review.
- Source: [[papers/2608.19098]] | https://huggingface.co/papers/2608.19098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26067). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.26067]] | https://huggingface.co/papers/2608.26067
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25864). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.25864]] | https://huggingface.co/papers/2608.25864
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24479). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.24479]] | https://huggingface.co/papers/2608.24479
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24138). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2608.24138]] | https://huggingface.co/papers/2608.24138
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21839). Keywords: reward model, alignment. Status: pending-review.
- Source: [[papers/2608.21839]] | https://huggingface.co/papers/2608.21839
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23383). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.23383]] | https://huggingface.co/papers/2608.23383
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23256). Keywords: rlvr. Status: pending-review.
- Source: [[papers/2608.23256]] | https://huggingface.co/papers/2608.23256
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25625). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.25625]] | https://huggingface.co/papers/2608.25625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25204). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.25204]] | https://huggingface.co/papers/2608.25204
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26070). Keywords: reinforcement learning. Status: pending-review.
- Source: [[papers/2608.26070]] | https://huggingface.co/papers/2608.26070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25832). Keywords: self-play, ppo. Status: pending-review.
- Source: [[papers/2608.25832]] | https://huggingface.co/papers/2608.25832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22510). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.22510]] | https://huggingface.co/papers/2608.22510
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24735). Keywords: self-improvement, recursive self. Status: pending-review.
- Source: [[papers/2608.24735]] | https://huggingface.co/papers/2608.24735
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24876). Keywords: self-improvement, recursive self. Status: pending-review.
- Source: [[papers/2608.24876]] | https://huggingface.co/papers/2608.24876
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24696). Keywords: reinforcement learning, grpo, verifiable reward, rlvr. Status: pending-review.
- Source: [[papers/2608.24696]] | https://huggingface.co/papers/2608.24696
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23566). Keywords: reinforcement learning, grpo, ppo. Status: pending-review.
- Source: [[papers/2608.23566]] | https://huggingface.co/papers/2608.23566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22274). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.22274]] | https://huggingface.co/papers/2608.22274
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24053). Keywords: alignment, ppo. Status: pending-review.
- Source: [[papers/2608.24053]] | https://huggingface.co/papers/2608.24053
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20492). Keywords: reinforcement learning, grpo. Status: pending-review.
- Source: [[papers/2608.20492]] | https://huggingface.co/papers/2608.20492
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09408). Keywords: ppo. Status: pending-review.
- Source: [[papers/2608.09408]] | https://huggingface.co/papers/2608.09408
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15875). Keywords: alignment. Status: pending-review.
- Source: [[papers/2608.15875]] | https://huggingface.co/papers/2608.15875
- Confidence: Low (auto-matched, not yet reviewed)
- Evolved harnesses converge on the same abstract playbook (60-80% concept overlap) with disjoint ecosystem plumbing; gains are defect-compensation, not new capability — near-zero where defect mass ~ 0 (Python cells, GPT-5-mini); one universal distilled harness recovers only 48-68% of native gains
- Source: [[concepts/one-recipe-many-harnesses-self-evolution]]
- Confidence: High

### 2026-09-09: S3Gym: self-improvement is neither automatic nor uniform
- Benchmark decomposing experience-driven learning into Self-Testing/Self-Judging/Self-Improvement; summary memory beats raw history only when experience compresses into reusable rules, parameter training shows unstable gains + severe negative transfer
- Source: [[2608.31100]]
- Confidence: High

### 2026-09-09: BCIT: conditional experience transfer in autonomous post-training
- Past update evidence must be re-authorized before reuse after the parent model changes — binding effects to source context + vetoing hard conflicts beats context-free reuse on a 4B model across finance reasoning/SQL/function-calling
- Source: [[2608.26730]]
- Confidence: High

### 2026-09-09: Bilevel coordinated reflection + verifier-gated memory ascent (SRMA)
- Proves no transcript-only gate can uniformly improve memory (information-theoretic impossibility); only environment-grounded evaluation gates help — accept memory writes when grounded eval risk strictly decreases (72.2% vs 70.8% on SWE-bench)
- Source: [[2609.02750]]
- Confidence: High

### 2026-09-09: AgentJudgeBench: structural ceiling on LLM judges for agentic tool-calling

### 2026-09-09: EVOHARNESSBENCH: Can Your Agents Keep Pace with an Evolving Harness?

### 2026-09-09: RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives

### 2026-09-09: Learning 3D Editing without Paired Supervision via Generative Prior Distillation

### 2026-09-09: Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Serie

### 2026-09-09: Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-

### 2026-09-09: Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswe

### 2026-09-09: AuK Technical Report: An Open-Source Foundational Model for Speech Generation an

### 2026-09-09: Omni Interaction Agent Technical Report

### 2026-09-09: Procedural Graphs: Self-Evolving Execution Structures for LLM Agents

### 2026-09-09: Steering Geometry: Validating Human Value Geometry in LLM Steering Space

### 2026-09-09: Miles v0.1: Production-Level Post-Training

### 2026-09-09: Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents i

### 2026-09-09: Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context R

### 2026-09-09: Agentic Visual Generation: From Generative Models to Agentic Control

### 2026-09-09: NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Ro

### 2026-09-09: MOLE: Detecting Insider Threats in AI Agents

### 2026-09-09: DriveZero: End-to-End Driving Beyond Human Demonstrations
- HF trending paper (arxiv: 2609.06055). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.06055]] | https://huggingface.co/papers/2609.06055
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06966). Keywords: alignment. Status: pending-review.
- Source: [[papers/2609.06966]] | https://huggingface.co/papers/2609.06966
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08183). Keywords: self-improvement, recursive self, distillation. Status: pending-review.
- Source: [[papers/2609.08183]] | https://huggingface.co/papers/2609.08183
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06758). Keywords: reinforcement learning, reward model, ppo. Status: pending-review.
- Source: [[papers/2609.06758]] | https://huggingface.co/papers/2609.06758
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07108). Keywords: reinforcement learning, ppo. Status: pending-review.
- Source: [[papers/2609.07108]] | https://huggingface.co/papers/2609.07108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08404). Keywords: reinforcement learning, self-evolving, grpo, bootstrap. Status: pending-review.
- Source: [[papers/2609.08404]] | https://huggingface.co/papers/2609.08404
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08368). Keywords: alignment, ppo, distillation. Status: pending-review.
- Source: [[papers/2609.08368]] | https://huggingface.co/papers/2609.08368
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06289). Keywords: alignment, rlhf, dpo, ppo. Status: pending-review.
- Source: [[papers/2609.06289]] | https://huggingface.co/papers/2609.06289
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.09153). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2609.09153]] | https://huggingface.co/papers/2609.09153
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08977). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.08977]] | https://huggingface.co/papers/2609.08977
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08936). Keywords: reinforcement learning, ppo. Status: pending-review.
- Source: [[papers/2609.08936]] | https://huggingface.co/papers/2609.08936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29109). Keywords: alignment, dpo. Status: pending-review.
- Source: [[papers/2608.29109]] | https://huggingface.co/papers/2608.29109
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07470). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.07470]] | https://huggingface.co/papers/2609.07470
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06008). Keywords: bootstrap. Status: pending-review.
- Source: [[papers/2609.06008]] | https://huggingface.co/papers/2609.06008
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04942). Keywords: distillation. Status: pending-review.
- Source: [[papers/2609.04942]] | https://huggingface.co/papers/2609.04942
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05738). Keywords: ppo. Status: pending-review.
- Source: [[papers/2609.05738]] | https://huggingface.co/papers/2609.05738
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04280). Keywords: self-evolving. Status: pending-review.
- Source: [[papers/2609.04280]] | https://huggingface.co/papers/2609.04280
- Confidence: Low (auto-matched, not yet reviewed)
- On hard queries without ground truth all six judges (20B→frontier) converge to 77–82% alignment regardless of scale; ground-truth exposure can HURT (over-anchoring); rubrics +6.5pp, CoT negligible — bounds what self-critique alone can achieve
- Source: [[2608.26623]]
- Confidence: High
