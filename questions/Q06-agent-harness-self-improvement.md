---

tags: [permanent-question, research]
created: 2026-05-25
question: "Beyond generic metalearning — what specific architectural and algorithmic ideas let agents build better toolchains, improve their own prompting, and recursively self-optimize? How does this apply to quantitative research workflows?"
type: permanent-question
reviewed: 2026-05-25
confidence: 0.85
evidence_count: 16
last_evidence_date: "2026-08-19" 

---


# Q06: Agent Recursive Self-Improvement

## Question
*Beyond generic metalearning — what specific architectural and algorithmic ideas let agents build better toolchains, improve their own prompting, and recursively self-optimize? How does this apply to quantitative research workflows?*

## Current State of Knowledge

Note: Q02 covers the general agent self-improvement landscape. This question focuses specifically on recursive, quantitative-research-oriented self-improvement.

### What Recursive Self-Improvement Means in Practice

The idea: an agent that can improve its own:
- Tool selection and composition
- System prompts and instructions
- Memory organization and retrieval
- Workflow design

...without human intervention on each improvement cycle.

### Specific Mechanisms

**1. Prompt Evolution via Feedback**
- Keep a log of task outcomes (success/failure + reasoning)
- After N tasks, extract: what prompts led to good outcomes? What failed?
- Update system prompt with learned patterns
- Tool: can be as simple as "extract principles from failed tasks, append to system prompt"
- Hermes has skill management for this — could automate

**2. Toolchain Synthesis**
- Given a goal, the agent synthesizes a new tool from existing primitives
- Example: "I need to compute 30-day rolling Sharpe ratio" → agent generates a Python function that gets added to its tool library
- This is programming by description — LLMs can do this
- Relevant: Toolformer (Schick et al.) — LLM learns to call APIs; beyond this, LLM writes new APIs

**3. Memory Consolidation**
- After working sessions, extract key lessons → write to persistent memory
- Organize memory hierarchically (skills, facts, procedures)
- Periodically review memory for consistency and outdated info
- Relevant: This is exactly what Hermes MEMORY.md is for

**4. Workflow Refinement**
- Track what sequences of tools lead to good research outcomes
- Build reusable "research pipelines" from successful traces
- Example: "When researching a factor, always: find academic source → check practitioner implementation → backtest → document failure modes"

**5. Self-Backtesting**
- The agent generates hypotheses about market behavior
- Runs backtests
- Updates beliefs based on results
- This is what quantitative researchers do — an agent can do it iteratively

### For Quantitative Research Specifically

A research agent could:
1. **Maintain a strategy database** — what factors, what regimes, what worked
2. **Propose new hypotheses** — based on reading new papers or observing patterns
3. **Run systematic experiments** — sweep parameter spaces, test in different regimes
4. **Report failures clearly** — what went wrong, why (market changed? overfitting? wrong assumption?)
5. **Accumulate institutional knowledge** — not just "this worked" but "why it worked and when it won't"

The key challenge: **a quantitative research agent needs to be right, not just articulate**. Bad alpha is worse than no alpha.

### The Risk: Self-Improvement Without Reality Check

Agents can improve their confidence without improving their accuracy ("hallucinating improvement").
Solution: Always ground improvement in measurable outcomes (backtest results, prediction accuracy).

### What's Actually Deployed

Most deployed "self-improvement" is:
- Prompt versioning + A/B testing (simple, effective)
- Logging failure cases and updating system prompt (Hermes does this manually)
- Retrieval-augmented memory (adding relevant context at inference time)
- Not fully autonomous recursive improvement

## Key Papers
- Zhang et al. — "Self-Harness: Harnesses That Improve Themselves" (2026, arXiv:2606.09498) — Formalizes Weakness Mining → Harness Proposal → Proposal Validation with regression testing. The canonical paper for the self-improving harness paradigm deployed in Hermes.
- Lou et al. — "AutoHarness: Improving LLM Agents by Synthesizing a Code Harness" (2026, arXiv:2603.03329) — Automatic code harness synthesis constraining agent actions to valid operations.
- Pan et al. — "Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference" (2026, arXiv:2606.05922) — Harness improvement without ground-truth validation sets, using self-preference optimization.
- Reflection agents (see Q02) — most practical self-improvement mechanism currently
- Toolformer for tool synthesis
- Self-verification mechanisms (detect own errors before outputting)

## Emerging Methodology

The practical loop for a quantitative research agent:

```
1. Research task (e.g., "does earnings sentiment predict 30-day returns?")
2. Agent executes: literature → data → hypothesis → backtest → analysis
3. Store results in structured memory (strategy database)
4. If failure → log what went wrong, update beliefs
5. Next task → retrieval of relevant prior results + lessons
6. Periodic review: extract cross-strategy patterns → methodology notes
```

This doesn't require cutting-edge AI. It requires **disciplined logging and retrieval**.

## June 2026 Findings

### 1. Loop Engineering — Direct Application

Practical mechanisms deployed in the agent harness for immediate self-improvement:

- **Critic Separation** (`critic.sh`): A dedicated verifier harness decoupled from the actor. The critic validates every output before it's committed — acting as a real-time quality gate. This prevents hallucinated improvements from entering the system.
- **Triage Inbox**: All failure feedback is routed into a structured inbox that feeds back into the harness. Failures aren't just logged — they actively reshape future behavior by updating prompts, constraints, and verification criteria.
- **Skill Auto-Patch**: The harness learns from its own output. When a skill produces suboptimal results, the harness generates a patch, tests it in isolation, and deploys it if verification passes. This is the lowest-risk closed loop: the agent improves its own toolchain from its own mistakes.

### 2. Self-Harness Karpathy Enhancement

Inspired by Karpathy's framing of "self-improving infrastructure" — the harness itself becomes the object of improvement. Rather than the agent improving its outputs within a fixed harness, the harness architecture (prompts, tool schemas, verification logic, loop structure) is versioned, tested, and evolved over time. The harness introspects its own performance: which loop patterns produced correct results fastest? Which guards caught errors early? The answers rewrite the harness definition. This is **meta-self-improvement** — improving the mechanism that does the improving.

### 3. `methodology-loop.md` — Three-Layered Meta-System

A formalized three-layer architecture for recursive improvement:

| Layer | Role | Mechanism |
|-------|------|-----------|
| **L1 — Execution Loop** | Agent performs tasks using tools and skills | Standard agent harness loop (act → observe → act) |
| **L2 — Improvement Loop** | Agent reflects on L1 outcomes and updates its own prompts, skills, memory | Critic feedback, triage processing, skill auto-patch |
| **L3 — Meta-Loop** | Agent improves the improvement process itself | Rewrites methodology-loop.md, adjusts improvement strategies, experiments with new loop architectures |

The meta-loop (L3) is the key innovation: the agent doesn't just get better at its tasks — it gets better at getting better. It maintains a methodology document that it treats as executable infrastructure.

### 4. Headroom MCP Integration

The agent can call `headroom_compress` via MCP to optimize its own context window in real time. Instead of relying on static context management, the agent actively decides:
- What to compress (which conversation turns, tool outputs, memory blobs)
- When to compress (context approaching threshold)
- What granularity (summarization vs. structural compression vs. drop)

This gives the agent **autonomous context budget management** — a prerequisite for sustained recursive improvement without manual context purging.

### 5. Memory Tiering

The agent manages its own memory hierarchy across four tiers with explicit promote/demote/archive operations:

| Tier | Scope | Latency | Example |
|------|-------|---------|---------|
| **T1 — Working** | Current session context | Instant | Active conversation, recent tool outputs |
| **T2 — Episodic** | Recent sessions (days) | Fast retrieval | Yesterday's research session summary |
| **T3 — Semantic** | Reusable knowledge (weeks/months) | Slower retrieval | Skill definitions, methodology notes |
| **T4 — Archival** | Historical record (indefinite) | Explicit recall | Past project artifacts, deprecated strategies |

Promote: frequently accessed T4 content moves to T3. Demote: stale T2 content moves to T4. Archive: T4 items are compressed and indexed, not deleted. The agent orchestrates this lifecycle autonomously, ensuring the most relevant knowledge is always in the fastest tier.

### 6. `/goal` Primitive

The `/goal` primitive changes the loop termination condition from "all tools called" to "condition satisfied." The harness runs until:
- The specified condition is met (e.g., backtest passes threshold, hypothesis is confirmed/refuted)
- Resources are exhausted (time, token budget, API calls)
- The agent explicitly declares the goal unachievable

This transforms the harness from a linear execution pipeline into a **goal-directed search process**. The agent is free to iterate, backtrack, and try alternative approaches without needing a human to re-prompt.

### 7. CL4R1T4S Dataset — Industry Evidence for Recursive Self-Improvement

The [[wiki/sources/cl4r1t4s-leaked-system-prompts|CL4R1T4S]] repository (66 leaked system prompts from 26 providers) provides real-world evidence of how frontier AI systems solve the same recursive improvement problems Q06 addresses:

**Convergent Architecture: Dynamic Tool Discovery**
Both Anthropic Fable 5/Opus 4.7 (via `tool_search`) and Hermes (via `tool_search` / skill-loading) independently converged on the same architecture: tools loaded on-demand rather than listed statically. The prompt describes visible tools as "partial by design." This validates the design decisions documented in [[prompt-architecture-operations]] and confirms that **static capability declaration doesn't scale** for self-improving agents.

**Convergent Pattern: Mandatory Skills Pre-Read**
Anthropic Fable 5 mandates: "Reading the relevant SKILL.md is a **required first step** before writing any code, creating any file, or running any other computer tool." This is structurally identical to Hermes's SOUL.md mandate: "scan the skills below. If a skill matches... you MUST load it." Both systems independently arrived at the same solution: externalized, environment-specific skill encoding as the mechanism for agent self-improvement ([[wiki/synthesis/system-prompt-arms-race]]).

**The Prompt as Product Specification (Meta-Loop Validation)**
Claude Fable 5's 17.5K-word prompt ([[references/claude-fable-5-system-prompt]]) covers not just behavior but tool schemas (15+ JSON-schema), MCP connectors, API permissions, file system architecture, and safety protocols. The prompt has evolved from "how to behave" to "how the product works" — absorbing what would traditionally be product documentation. This validates the Q06 thesis that **prompt-level self-improvement infrastructure is the product**: the system prompt is where the agent's capabilities are defined, and improving the prompt IS improving the agent.

**Modular Prompt Architecture Enables A/B Testing**
Anthropic's tag-based sectioning (`{claude_behavior}`, `{memory_system}`, `{computer_use}`, etc.) enables independent versioning and A/B testing of prompt components. This is **meta-level infrastructure for prompt self-improvement** — the same L3 meta-loop concept from the methodology-loop system, but at the prompt architectural level. See [[concepts/anthropic-system-prompt-evolution]].

Key cross-cutting patterns (see [[concepts/system-prompt-architecture-patterns]]):
- Search-before-answer: Universal by 2026 — every provider concluded training data is never sufficient
- Refusal architecture maturity: Three generations from moralizing to meta-safe (don't reveal detection mechanics)
- Apology avoidance: 13 prompts explicitly prohibit "I'm sorry" — convergent UX research finding

### 8. Code World Models for Agent Toolchain Synthesis

The [[concepts/code-world-models|Code World Model]] pattern (Lehrach et al., 2025) reframes LLMs from direct actors to compilers: translate natural language rules into executable code, then hand off to classical solvers. For recursive self-improvement, this is directly applicable to Q06's "Toolchain Synthesis" mechanism:

| Self-Improvement Level | CWM Application |
|------------------------|-----------------|
| Tool generation | Agent encounters novel domain → CWM-compile domain rules → new tool/capability emerges |
| Verifiability | CWM outputs are executable — correctness is decidable, not probabilistic ([[concepts/verifiable-planning]]) |
| Division of labor | LLM handles translation (language→code); classical solver handles search (MCTS, constraints) |
| Generalization | LLM doesn't need to have seen the domain — it needs to understand the rules and express them as code |

The [[wiki/synthesis/cwm-game-theory-application|CWM Game Theory Application]] synthesis shows how this pattern maps to existing agent skills:
- **Autoresearch**: Experiment as game against nature → encode success criteria as executable evaluation scripts
- **Meta-critic**: Strategy selection as multi-armed bandit → prioritizes executable critique dimensions (linters, tests) over NL dimensions
- **Structured execution**: Adversarial critic as 2-player zero-sum game → formalizes acceptance criteria as executable assertions

This creates a **reliability hierarchy** for agent self-improvement:
```
Most reliable: Executable CWM + classical solver (deterministic)
              ↓
             Executable assertions + LLM critique (verifiable)
              ↓
             LLM critique with guardrails (probabilistic)
              ↓
Least reliable: Raw LLM judgment (unverifiable)
```

See: [[papers/code-world-models-general-game-playing]], [[concepts/llm-as-compiler]], [[concepts/verifiable-planning]].

### 9. Game Theory Gaps for Agent Orchestration

The [[wiki/gaps/game-theory-gaps|Game Theory Gaps]] audit identified two gaps directly relevant to agent recursive self-improvement:

**GAP-2: Mechanism Design for Multi-Agent Orchestration [HIGH LEVERAGE]**
Symphony (6 agents, 15 assignees) is a principal-agent game. Workers can "phone it in" (observed in STORM runs). Current mitigation is monitoring (review/unblock), which is reactive. Missing capabilities:
- Scoring rules that incentivize honest difficulty estimates
- Self-selection mechanisms (revealed preference for task assignment)
- Verification games (how much checking is game-theoretically optimal?)
- Moral hazard modeling (worker effort as hidden action)

**GAP-5: Adversarial Review Depth Not Formalized [MEDIUM LEVERAGE]**
Critical review and meta-critic use adversarial review but don't formalize the minimax depth or game type. Missing formalization:
- Minimax depth specification for multi-round critique
- Game type classification (zero-sum vs cooperative improvement)
- Optimal mixed strategy for critic (randomize critique dimensions to avoid gaming)

## Connections
- [[Q02]] — general agent self-improvement
- [[Q05]] — applying these ideas to finance specifically
- [[Q01]] — the underlying skills the agent needs
- [[loop-engineering]] — critic separation, triage inbox, skill auto-patch
- [[methodology-loop]] — three-layer meta-system with meta-loop
- [[headroom-integration]] — agent-controlled context compression
- [[memory-tiering]] — 4-tier memory hierarchy with promote/demote/archive
- [[wiki/sources/cl4r1t4s-leaked-system-prompts]] — 66 leaked prompts as industry evidence for recursive self-improvement
- [[wiki/synthesis/system-prompt-arms-race]] — Convergent evolution on dynamic tool discovery and skills pre-read
- [[concepts/system-prompt-architecture-patterns]] — Cross-cutting patterns from 66 prompts
- [[concepts/anthropic-system-prompt-evolution]] — Case study: prompt-level self-improvement across 5 versions
- [[references/claude-fable-5-system-prompt]] — Deep dive into most sophisticated system prompt
- [[concepts/code-world-models]] — CWM pattern for toolchain synthesis
- [[concepts/llm-as-compiler]] — LLM as translator → executable artifact → classical solver
- [[concepts/verifiable-planning]] — Reliability hierarchy for agent decisions
- [[wiki/synthesis/cwm-game-theory-application]] — CWM mapped to agent skills (autoresearch, meta-critic, structured execution)
- [[wiki/gaps/game-theory-gaps]] — GAP-2 (mechanism design) and GAP-5 (adversarial review depth)

## Last Updated
_2026-06-24_ — Added: CL4R1T4S dataset evidence (dynamic tool discovery convergence, mandatory skills pre-read, prompt as product spec, modular prompt A/B testing). Added CWM pattern for toolchain synthesis. Added game theory gaps (GAP-2 mechanism design, GAP-5 adversarial review depth). Updated Connections with 10 new references.
_2026-06-17_ — Added key papers (Self-Harness, AutoHarness, Evolving Agents in the Dark) to Key Papers section
_2026-06-12_ — Added June 2026 findings: loop engineering, Self-Harness Karpathy, methodology-loop, Headroom MCP, memory tiering, /goal primitive

## Evidence Log

<!-- Weekly scan appends dated evidence blocks below this line.
     Format: ### YYYY-MM-DD: <topic>
             - Finding
             - Source: [[wikilink]] or URL
             - Confidence: High/Medium/Low
-->

### 2026-06-12: Three-layer methodology loop — L1 execute, L2 improve, L3 meta-improve
- Formalized architecture: L1 (task execution), L2 (reflect + update prompts/skills/memory), L3 (improve the improvement process itself). Meta-loop rewrites methodology-loop.md as executable infrastructure. Agent gets better at getting better.
- Source: [[methodology-loop]]
- Confidence: High

### 2026-06-12: Memory tiering — 4-tier autonomous hierarchy (T1-T4)
- Working → Episodic → Semantic → Archival with promote/demote/archive ops. Agent orchestrates lifecycle autonomously: frequently accessed T4 → T3, stale T2 → T4. Ensures most relevant knowledge is always in fastest tier.
- Source: [[memory-tiering]]
- Confidence: High

### 2026-06-24: GAP-2: Mechanism design for multi-agent orchestration
- Symphony (6 agents, 15 assignees) is a principal-agent game. Workers can 'phone it in.' Missing: scoring rules for honest estimates, self-selection mechanisms, verification games, moral hazard modeling. Reactive monitoring is insufficient.
- Source: [[wiki/gaps/game-theory-gaps]]
- Confidence: Medium

### 2026-06-24: CL4R1T4S validates prompt-level self-improvement as the product

### 2026-07-30: SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

### 2026-07-30: SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution

### 2026-07-30: GPT-Red: Automated Red Teaming via Self-Play at Scale

### 2026-07-30: OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal Biomedi

### 2026-07-30: ReDesign: Recovering Editable Design Structures from Images via Agentic Decompos

### 2026-07-01: TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

### 2026-07-01: Hierarchical Experimentalist Agents

### 2026-07-02: Personalization as Inverse Planning: Learning Latent Design Intents for Agentic 

### 2025-07-01: SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via

### 2026-07-06: Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care

### 2025-07-02: Thinking Beyond Tokens: From Brain-Inspired Intelligence to Cognitive

### 2026-07-07: LLM-as-a-Verifier: A General-Purpose Verification Framework

### 2026-07-07: GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automat

### 2026-07-08: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Paramete

### 2025-08-07: SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from

### 2026-07-09: Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

### 2026-07-10: CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

### 2026-07-15: Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Vis

### 2026-07-15: Towards Autonomous and Auditable Medical Imaging Model Development

### 2025-09-03: The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

### 2025-09-03: VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use

### 2026-07-16: KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Ev

### 2025-09-08: Bootstrapping Task Spaces for Self-Improvement

### 2025-09-09: Reinforcement Learning Foundations for Deep Research Systems: A Survey

### 2026-07-16: Self-Improvements in Modern Agentic Systems: A Survey

### 2026-07-17: SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

### 2025-09-15: QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading

### 2025-09-18: Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation

### 2026-07-20: When Does Muon Help Agentic Reinforcement Learning?

### 2025-09-26: UserRL: Training Interactive User-Centric Agent via Reinforcement

### 2025-09-29: Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive

### 2026-07-21: Masked Diffusion Language Models are Strong and Steerable Text-Based World Model

### 2026-07-24: AREX: Towards a Recursively Self-Improving Agent for Deep Research

### 2025-10-01: Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified

### 2026-07-24: NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

### 2026-07-27: Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Lea

### 2026-07-28: From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent P

### 2025-10-03: StockBench: Can LLM Agents Trade Stocks Profitably In Real-world

### 2026-07-28: The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-train

### 2025-10-03: TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis

### 2025-10-07: AdvEvo-MARL: Shaping Internalized Safety through Adversarial

### 2025-10-08: Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and

### 2025-10-08: Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for

### 2025-10-14: Self-Improving LLM Agents at Test-Time

### 2025-10-16: Stronger Together: On-Policy Reinforcement Learning for Collaborative

### 2025-10-21: Enterprise Deep Research: Steerable Multi-Agent Deep Research for

### 2025-10-21: Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native

### 2025-10-22: AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement

### 2025-10-28: Code Aesthetics with Agentic Reward Feedback

### 2025-10-29: SPICE: Self-Play In Corpus Environments Improves Reasoning

### 2025-10-29: FunReason-MT Technical Report: Overcoming the Complexity Barrier in

### 2025-11-07: Scaling Agent Learning via Experience Synthesis

### 2025-12-05: SIMA 2: A Generalist Embodied Agent for Virtual Worlds

### 2025-12-11: Towards a Science of Scaling Agent Systems

### 2025-12-19: Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment with Na

### 2025-12-24: Reinforcement Learning for Self-Improving Agent with Skill Library

### 2026-01-08: MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecula

### 2026-01-15: The AI Hippocampus: How Far are We From Human Memory?

### 2026-01-22: Agentic Reasoning for Large Language Models

### 2026-01-23: From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantific

### 2026-01-27: Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability

### 2026-01-29: Reinforcement Learning via Self-Distillation

### 2026-02-04: FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via Development-Oriente

### 2026-02-04: Scaling Small Agents Through Strategy Auctions

### 2026-02-06: PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling

### 2026-02-09: Self-Improving World Modelling with Latent Actions

### 2026-02-10: QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining

### 2026-02-10: AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

### 2026-02-11: P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics Olympiads

### 2026-02-11: Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems

### 2026-02-12: Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters

### 2026-02-13: The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving

### 2026-02-13: Budget-Constrained Agentic Large Language Models: Intention-Based Planning for C

### 2026-02-20: Discovering Multiagent Learning Algorithms with Large Language Models

### 2026-03-03: Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data

### 2026-03-11: SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive

### 2026-03-12: Meissa: Multi-modal Medical Agentic Intelligence

### 2026-03-18: FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use

### 2026-03-24: Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large 

### 2026-04-06: GrandCode: Achieving Grandmaster Level in Competitive Programming via Agentic Re

### 2026-04-09: SEVerA: Verified Synthesis of Self-Evolving Agents

### 2026-04-09: Qualixar OS: A Universal Operating System for AI Agent Orchestration

### 2026-04-09: AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement Learning

### 2026-04-10: Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

### 2026-04-14: TRACE: Capability-Targeted Agentic Training

### 2026-04-14: Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and

### 2026-05-01: Synthetic Computers at Scale for Long-Horizon Productivity Simulation

### 2026-05-06: ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration

### 2026-05-06: Healthcare AI GYM for Medical Agents

### 2026-05-07: OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

### 2026-05-11: InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search

### 2026-05-12: G-Zero: Self-Play for Open-Ended Generation from Zero Data

### 2026-05-12: AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Syst

### 2026-05-15: Orchard: An Open-Source Agentic Modeling Framework

### 2026-05-15: Nexus : An Agentic Framework for Time Series Forecasting

### 2026-05-18: Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design

### 2026-05-19: Code as Agent Harness

### 2026-05-19: Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces

### 2026-05-26: Foundation Protocol: A Coordination Layer for Agentic Society

### 2026-05-26: ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Rei

### 2026-05-26: ECHO: Terminal Agents Learn World Models for Free

### 2026-05-28: OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

### 2026-05-29: Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Ge

### 2026-05-29: Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleav

### 2026-06-03: Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories

### 2026-06-03: Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment 

### 2026-06-03: The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Develop

### 2026-06-05: EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Conte

### 2026-06-08: CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

### 2026-06-09: DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and R

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

### 2026-07-10: CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

### 2026-07-15: Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Vis

### 2026-07-16: KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Ev

### 2026-07-16: Self-Improvements in Modern Agentic Systems: A Survey

### 2026-07-17: SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

### 2026-07-24: AREX: Towards a Recursively Self-Improving Agent for Deep Research

### 2026-07-31: Beacon: Knowing When and How to Perform Agentic Visual Reasoning

### 2026-08-03: Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a Longitudina

### 2026-08-03: SAF-OPD: Stable Advantage Fusion for On-Policy Distillation

### 2026-08-03: SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle Autonom

### 2026-08-03: In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous Driving

### 2026-08-03: Mental World Modeling

### 2026-08-03: One Future, Every Robot: Label-Efficient Collective-State Prediction with Decent

### 2026-08-03: ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

### 2026-08-03: N_0-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulatio

### 2026-08-03: Enhancing Rubric-based RL via Self-Distillation

### 2026-08-03: ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

### 2026-08-03: Meshy T2: Fast Native Mesh Generation with Flow Matching

### 2026-08-03: From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open

### 2026-08-03: β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation

### 2026-08-03: Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts 

### 2026-08-03: Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainabil

### 2026-08-03: Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions

### 2026-08-03: ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamic

### 2026-08-03: LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structure

### 2026-08-03: Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generati

### 2026-08-03: AI Tour Meeting: Group Travel Planning by LLM Agents

### 2026-08-03: Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Founda

### 2026-08-03: BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms

### 2026-08-04: SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space

### 2026-08-04: Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis in Multim

### 2026-08-04: A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples

### 2026-08-04: Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

### 2026-08-04: RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender System

### 2026-08-04: Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language

### 2026-08-04: DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon Multimo

### 2026-08-04: 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question 

### 2026-08-04: DAPD: Dual-Anchored Policy Distillation

### 2026-08-04: LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks

### 2026-08-04: LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation

### 2026-08-04: Progressive Agent Skill Generation via Reinforcement Learning

### 2026-08-04: SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation

### 2026-08-04: UEmbed: Unified Sparse and Dense Multimodal Embeddings

### 2026-08-04: SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zer

### 2026-08-04: ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map Points to 

### 2026-08-04: Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous 

### 2026-08-04: VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Poli
- HF trending paper (arxiv: 2607.28590). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.28590]] | https://huggingface.co/papers/2607.28590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01755). Keywords: planning. Status: pending-review.
- Source: [[papers/2608.01755]] | https://huggingface.co/papers/2608.01755
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02358). Keywords: autonomous agent, environment, execution. Status: pending-review.
- Source: [[papers/2608.02358]] | https://huggingface.co/papers/2608.02358
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02023). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.02023]] | https://huggingface.co/papers/2608.02023
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02583). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.02583]] | https://huggingface.co/papers/2608.02583
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02287). Keywords: agent harness, gui, harness. Status: pending-review.
- Source: [[papers/2608.02287]] | 
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

### 2026-08-05: ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Lev

### 2026-08-05: MiniWorld: Democratizing the Training of Video World Models from Scratch

### 2026-08-05: ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

### 2026-08-05: PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diver

### 2026-08-05: LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

### 2026-08-05: Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

### 2026-08-05: Quo Vadis, World Modeling?

### 2026-08-05: PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Person

### 2026-08-05: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Lear

### 2026-08-05: CAPEval: A Decoupled Caption Evaluation across Understanding and Generation

### 2026-08-05: TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

### 2026-08-05: Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D Generation, Un

### 2026-08-05: UniWorld-Design: From Pixel Generation to Layer-Native Design

### 2026-08-05: MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Ope

### 2026-08-05: InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthe

### 2026-08-05: AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?

### 2026-08-06: Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Inte

### 2026-08-06: Self-Evolving Coding Agents

### 2026-08-06: ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assi

### 2026-08-06: GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks

### 2026-08-06: AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities

### 2026-08-06: K-EXAONE 2.0 Technical Report

### 2026-08-06: Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from A

### 2026-08-06: BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Langua

### 2026-08-06: WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World 

### 2026-08-06: OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents

### 2026-08-06: NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the English-Korea

### 2026-08-06: SKILL-KD: Contrastive Skill Distillation for LLM Agents

### 2026-08-06: UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models

### 2026-08-06: ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation

### 2026-08-06: OPD-V: Visual On-Policy Self-Distillation with Modality Balance

### 2026-08-06: ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct R

### 2026-08-07: DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous 

### 2026-08-07: MameLoshnLM: Yiddish Language Model and Evaluation Benchmark

### 2026-08-07: Continual Learning in Transition

### 2026-08-07: Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptati

### 2026-08-07: From Economic Agents to Agentic Economies: A Systems Blueprint for Economic Worl

### 2026-08-07: MASS: Multiplayer World Models with Authoritative Shared State

### 2026-08-07: ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Con

### 2026-08-07: EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object R

### 2026-08-07: EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinf

### 2026-08-07: SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding

### 2026-08-07: CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks

### 2026-08-07: AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning

### 2026-08-07: WorldClaw: Agentic 3D Open-World Generation at Scale

### 2026-08-07: HarnessOpt-Bench: Evaluating LLMs at Harness Optimization

### 2026-08-07: Recursive Synthesis for Long-Horizon Terminal Tasks

### 2026-08-07: Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised Wor

### 2026-08-08: GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splat

### 2026-08-08: FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channel

### 2026-08-08: Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and 

### 2026-08-10: Adversarial Attacks for Good: A Survey of Proactive Protection across the Visual

### 2026-08-10: OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understandi

### 2026-08-10: Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence

### 2026-08-10: Beyond Simply Environment Scaling: Designing Effective Environment Distributions

### 2026-08-10: YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family

### 2026-08-10: When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Sel

### 2026-08-10: Uncertainty-Aware World Model for Aerial Image-Goal Navigation

### 2026-08-10: StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming 

### 2026-08-10: The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, an

### 2026-08-10: Characterizing the Quality Profile of AI-Generated C++ in Production

### 2026-08-10: Modular TTT: Rethinking Test-Time Training as Composable Modules

### 2026-08-11: Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under 

### 2026-08-11: A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven Op

### 2026-08-11: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaborat

### 2026-08-11: Vision-Language Grounding as Bidirectional Concept Correspondence

### 2026-08-11: CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems

### 2026-08-11: A^2E : An End-to-End Agent Auditing Engine

### 2026-08-11: What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conve

### 2026-08-11: Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher

### 2026-08-11: Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution

### 2026-08-12: InSight-doc: Agentic Visual Perception for Long-Document Understanding

### 2026-08-12: 360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents

### 2026-08-12: UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models

### 2026-08-12: Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research A

### 2026-08-12: ComBodied Agents: a New Paradigm of Human-Centric Agentic AI

### 2026-08-12: SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discover

### 2026-08-12: Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Des

### 2026-08-12: DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Comp

### 2026-08-12: SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Pe

### 2026-08-12: VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World

### 2026-08-12: Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evo

### 2026-08-12: VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model w

### 2026-08-12: The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents

### 2026-08-12: Beyond Starry Night: Shortcut-Aware Control-State Planning for Artist-Grounded T

### 2026-08-12: On-Policy Self-Distillation without Any Supervision

### 2026-08-12: Business Arena: Benchmarking LLM Agents in a Realistic Marketplace

### 2026-08-12: MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation

### 2026-08-12: Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under 

### 2026-08-12: A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven Op

### 2026-08-12: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaborat

### 2026-08-12: Vision-Language Grounding as Bidirectional Concept Correspondence

### 2026-08-12: CEAA: A Cognitive Embodied Agents Architecture for Interactive Computing Systems

### 2026-08-12: A^2E : An End-to-End Agent Auditing Engine

### 2026-08-12: What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conve

### 2026-08-12: Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher

### 2026-08-13: SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Librari

### 2026-08-13: Parameter Exploration for RLVR via Variational Learning

### 2026-08-13: Ready Cohorts: Bounding GPU Opportunity and Avoiding Host Round Trips in LLM-Age

### 2026-08-13: Self-Evolving Embodied Agents via Skill-Harness Evolution

### 2026-08-13: Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop

### 2026-08-13: Persistent Recursive Worlds Enable Autonomous Software Evolution

### 2026-08-13: OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution

### 2026-08-13: AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models

### 2026-08-13: Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in 

### 2026-08-13: AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

### 2026-08-13: AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Resear

### 2026-08-13: StateFlow: Building, Evolving, and Accessing 3D World States for Previsualizatio

### 2026-08-13: Agent Safety Should Be a Runtime Contract

### 2026-08-13: Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill

### 2026-08-13: ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignme

### 2026-08-14: AVA-Encoder: Towards Agent-Native Video Representation Learning

### 2026-08-14: SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in 

### 2026-08-14: UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

### 2026-08-14: H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Mo

### 2026-08-14: Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intellige

### 2026-08-14: DarwinX: Evolving Agent Harnesses Through Natural Selection

### 2026-08-14: AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

### 2026-08-14: Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

### 2026-08-14: How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in 

### 2026-08-14: Intern-S2-Preview: Scientific Agentic Foundation Model

### 2026-08-14: ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Fr

### 2026-08-17: Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi

### 2026-08-17: A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientif

### 2026-08-17: UNMASK: Discovering and Causally Verifying Spurious Shortcuts in Text Classifier

### 2026-08-17: LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure

### 2026-08-17: Second Thought: Reasoning in Parallel as LLM Agents Act and Observe

### 2026-08-17: PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment

### 2026-08-17: CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Im

### 2026-08-17: Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Infe

### 2026-08-17: SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Gen

### 2026-08-17: Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Resea

### 2026-08-18: GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective 

### 2026-08-18: Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search

### 2026-08-18: TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation

### 2026-08-18: WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Ri

### 2026-08-18: DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs

### 2026-08-18: HiFi-BRep: High-Fidelity Latent Representation for Robust B-Rep Generation

### 2026-08-18: HarnessEval-W: Agentifying the Evaluation of Visual Worlds

### 2026-08-18: An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models

### 2026-08-18: UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrati

### 2026-08-18: Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs

### 2026-08-18: Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped Tr
- HF trending paper (arxiv: 2608.13987). Keywords: mcp, agentic, harness. Status: pending-review.
- Source: [[papers/2608.13987]] | https://huggingface.co/papers/2608.13987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16391). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.16391]] | https://huggingface.co/papers/2608.16391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15930). Keywords: gui, workflow, environment, execution. Status: pending-review.
- Source: [[papers/2608.15930]] | https://huggingface.co/papers/2608.15930
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16887). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.16887]] | https://huggingface.co/papers/2608.16887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16859). Keywords: workflow, harness. Status: pending-review.
- Source: [[papers/2608.16859]] | https://huggingface.co/papers/2608.16859
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16485). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.16485]] | https://huggingface.co/papers/2608.16485
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14614). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.14614]] | https://huggingface.co/papers/2608.14614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15659). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.15659]] | https://huggingface.co/papers/2608.15659
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16765). Keywords: recursive. Status: pending-review.
- Source: [[papers/2608.16765]] | https://huggingface.co/papers/2608.16765
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15669). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.15669]] | https://huggingface.co/papers/2608.15669
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16328). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.16328]] | https://huggingface.co/papers/2608.16328
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13417). Keywords: autonomous agent, harness, execution. Status: pending-review.
- Source: [[papers/2608.13417]] | https://huggingface.co/papers/2608.13417
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14138). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.14138]] | https://huggingface.co/papers/2608.14138
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12209). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.12209]] | https://huggingface.co/papers/2608.12209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14546). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.14546]] | https://huggingface.co/papers/2608.14546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14284). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.14284]] | https://huggingface.co/papers/2608.14284
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13667). Keywords: agentic, environment. Status: pending-review.
- Source: [[papers/2608.13667]] | https://huggingface.co/papers/2608.13667
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13545). Keywords: gui, environment, sandbox. Status: pending-review.
- Source: [[papers/2608.13545]] | https://huggingface.co/papers/2608.13545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09209). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.09209]] | https://huggingface.co/papers/2608.09209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14075). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.14075]] | https://huggingface.co/papers/2608.14075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03744). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2608.03744]] | https://huggingface.co/papers/2608.03744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11045). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.11045]] | https://huggingface.co/papers/2608.11045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13505). Keywords: agentic, environment. Status: pending-review.
- Source: [[papers/2608.13505]] | https://huggingface.co/papers/2608.13505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08975). Keywords: recursive, gui, workflow. Status: pending-review.
- Source: [[papers/2608.08975]] | https://huggingface.co/papers/2608.08975
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13546). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.13546]] | https://huggingface.co/papers/2608.13546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13560). Keywords: recursive, self-improvement, agentic, code agent. Status: pending-review.
- Source: [[papers/2608.13560]] | https://huggingface.co/papers/2608.13560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07545). Keywords: self-improvement, agent harness, harness. Status: pending-review.
- Source: [[papers/2608.07545]] | https://huggingface.co/papers/2608.07545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12743). Keywords: agentic, gui, planning, environment. Status: pending-review.
- Source: [[papers/2608.12743]] | https://huggingface.co/papers/2608.12743
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13049). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.13049]] | https://huggingface.co/papers/2608.13049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11752). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.11752]] | https://huggingface.co/papers/2608.11752
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10538). Keywords: agent harness, harness, environment, execution. Status: pending-review.
- Source: [[papers/2608.10538]] | https://huggingface.co/papers/2608.10538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12313). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.12313]] | https://huggingface.co/papers/2608.12313
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11878). Keywords: workflow, environment. Status: pending-review.
- Source: [[papers/2608.11878]] | https://huggingface.co/papers/2608.11878
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11924). Keywords: planning, orchestration, workflow. Status: pending-review.
- Source: [[papers/2608.11924]] | https://huggingface.co/papers/2608.11924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11274). Keywords: agentic, autonomous agent, harness, sandbox. Status: pending-review.
- Source: [[papers/2608.11274]] | https://huggingface.co/papers/2608.11274
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12314). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.12314]] | https://huggingface.co/papers/2608.12314
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11216). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.11216]] | https://huggingface.co/papers/2608.11216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12307). Keywords: harness, scaffold. Status: pending-review.
- Source: [[papers/2608.12307]] | https://huggingface.co/papers/2608.12307
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08160). Keywords: gui, environment. Status: pending-review.
- Source: [[papers/2608.08160]] | https://huggingface.co/papers/2608.08160
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06729). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.06729]] | https://huggingface.co/papers/2608.06729
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00677). Keywords: workflow, environment. Status: pending-review.
- Source: [[papers/2608.00677]] | https://huggingface.co/papers/2608.00677
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10450). Keywords: recursive, agentic. Status: pending-review.
- Source: [[papers/2608.10450]] | https://huggingface.co/papers/2608.10450
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11215). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.11215]] | https://huggingface.co/papers/2608.11215
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11350). Keywords: harness, environment, execution. Status: pending-review.
- Source: [[papers/2608.11350]] | https://huggingface.co/papers/2608.11350
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12123). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.12123]] | https://huggingface.co/papers/2608.12123
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09805). Keywords: code generation. Status: pending-review.
- Source: [[papers/2608.09805]] | https://huggingface.co/papers/2608.09805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05604). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.05604]] | https://huggingface.co/papers/2608.05604
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07169). Keywords: function calling, workflow, sandbox. Status: pending-review.
- Source: [[papers/2608.07169]] | https://huggingface.co/papers/2608.07169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07565). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.07565]] | https://huggingface.co/papers/2608.07565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07346). Keywords: agent harness, tool use, gui, planning. Status: pending-review.
- Source: [[papers/2608.07346]] | https://huggingface.co/papers/2608.07346
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09848). Keywords: environment, execution. Status: pending-review.
- Source: [[papers/2608.09848]] | https://huggingface.co/papers/2608.09848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07886). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.07886]] | https://huggingface.co/papers/2608.07886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03499). Keywords: tool use, sandbox. Status: pending-review.
- Source: [[papers/2608.03499]] | https://huggingface.co/papers/2608.03499
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08156). Keywords: harness. Status: pending-review.
- Source: [[papers/2608.08156]] | https://huggingface.co/papers/2608.08156
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08722). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.08722]] | https://huggingface.co/papers/2608.08722
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07463). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.07463]] | https://huggingface.co/papers/2608.07463
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08621). Keywords: workflow, environment. Status: pending-review.
- Source: [[papers/2608.08621]] | https://huggingface.co/papers/2608.08621
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06296). Keywords: gui, environment. Status: pending-review.
- Source: [[papers/2608.06296]] | https://huggingface.co/papers/2608.06296
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06751). Keywords: planning. Status: pending-review.
- Source: [[papers/2608.06751]] | https://huggingface.co/papers/2608.06751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06065). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.06065]] | https://huggingface.co/papers/2608.06065
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08477). Keywords: tool use. Status: pending-review.
- Source: [[papers/2608.08477]] | https://huggingface.co/papers/2608.08477
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07645). Keywords: recursive. Status: pending-review.
- Source: [[papers/2608.07645]] | https://huggingface.co/papers/2608.07645
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10875). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.10875]] | https://huggingface.co/papers/2608.10875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10692). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.10692]] | https://huggingface.co/papers/2608.10692
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10366). Keywords: tool use, agentic, browser, orchestration. Status: pending-review.
- Source: [[papers/2608.10366]] | https://huggingface.co/papers/2608.10366
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10299). Keywords: agentic, environment. Status: pending-review.
- Source: [[papers/2608.10299]] | https://huggingface.co/papers/2608.10299
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11079). Keywords: gui, workflow, execution. Status: pending-review.
- Source: [[papers/2608.11079]] | https://huggingface.co/papers/2608.11079
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10915). Keywords: agentic, environment. Status: pending-review.
- Source: [[papers/2608.10915]] | https://huggingface.co/papers/2608.10915
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08389). Keywords: agentic, gui. Status: pending-review.
- Source: [[papers/2608.08389]] | https://huggingface.co/papers/2608.08389
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08627). Keywords: workflow. Status: pending-review.
- Source: [[papers/2608.08627]] | https://huggingface.co/papers/2608.08627
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08814). Keywords: planning, environment. Status: pending-review.
- Source: [[papers/2608.08814]] | https://huggingface.co/papers/2608.08814
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10628). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.10628]] | https://huggingface.co/papers/2608.10628
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08311). Keywords: recursive, agent harness, harness. Status: pending-review.
- Source: [[papers/2608.08311]] | https://huggingface.co/papers/2608.08311
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07169). Keywords: function calling, workflow, sandbox. Status: pending-review.
- Source: [[papers/2608.07169]] | https://huggingface.co/papers/2608.07169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07565). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.07565]] | https://huggingface.co/papers/2608.07565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07346). Keywords: agent harness, tool use, gui, planning. Status: pending-review.
- Source: [[papers/2608.07346]] | https://huggingface.co/papers/2608.07346
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09848). Keywords: environment, execution. Status: pending-review.
- Source: [[papers/2608.09848]] | https://huggingface.co/papers/2608.09848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07886). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.07886]] | https://huggingface.co/papers/2608.07886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03499). Keywords: tool use, sandbox. Status: pending-review.
- Source: [[papers/2608.03499]] | https://huggingface.co/papers/2608.03499
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08156). Keywords: harness. Status: pending-review.
- Source: [[papers/2608.08156]] | https://huggingface.co/papers/2608.08156
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08722). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.08722]] | https://huggingface.co/papers/2608.08722
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07110). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.07110]] | https://huggingface.co/papers/2608.07110
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06640). Keywords: workflow, environment. Status: pending-review.
- Source: [[papers/2608.06640]] | https://huggingface.co/papers/2608.06640
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06714). Keywords: gui, workflow, scaffold. Status: pending-review.
- Source: [[papers/2608.06714]] | https://huggingface.co/papers/2608.06714
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05703). Keywords: agentic, environment. Status: pending-review.
- Source: [[papers/2608.05703]] | https://huggingface.co/papers/2608.05703
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05597). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.05597]] | https://huggingface.co/papers/2608.05597
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05219). Keywords: gui, environment, execution. Status: pending-review.
- Source: [[papers/2608.05219]] | https://huggingface.co/papers/2608.05219
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07051). Keywords: planning. Status: pending-review.
- Source: [[papers/2608.07051]] | https://huggingface.co/papers/2608.07051
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03571). Keywords: harness, environment. Status: pending-review.
- Source: [[papers/2608.03571]] | https://huggingface.co/papers/2608.03571
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06756). Keywords: gui, environment, execution. Status: pending-review.
- Source: [[papers/2608.06756]] | https://huggingface.co/papers/2608.06756
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06013). Keywords: workflow. Status: pending-review.
- Source: [[papers/2608.06013]] | https://huggingface.co/papers/2608.06013
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04314). Keywords: autonomous agent. Status: pending-review.
- Source: [[papers/2608.04314]] | https://huggingface.co/papers/2608.04314
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05784). Keywords: harness. Status: pending-review.
- Source: [[papers/2608.05784]] | https://huggingface.co/papers/2608.05784
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01049). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.01049]] | https://huggingface.co/papers/2608.01049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01492). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.01492]] | https://huggingface.co/papers/2608.01492
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04378). Keywords: workflow. Status: pending-review.
- Source: [[papers/2608.04378]] | https://huggingface.co/papers/2608.04378
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05466). Keywords: recursive, agentic, terminal agent, workflow. Status: pending-review.
- Source: [[papers/2608.05466]] | https://huggingface.co/papers/2608.05466
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06301). Keywords: agentic, gui, orchestration, harness. Status: pending-review.
- Source: [[papers/2608.06301]] | https://huggingface.co/papers/2608.06301
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05248). Keywords: agentic, planning. Status: pending-review.
- Source: [[papers/2608.05248]] | https://huggingface.co/papers/2608.05248
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05987). Keywords: recursive, agentic. Status: pending-review.
- Source: [[papers/2608.05987]] | https://huggingface.co/papers/2608.05987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06352). Keywords: terminal agent. Status: pending-review.
- Source: [[papers/2608.06352]] | https://huggingface.co/papers/2608.06352
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05137). Keywords: gui, orchestration. Status: pending-review.
- Source: [[papers/2608.05137]] | https://huggingface.co/papers/2608.05137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06197). Keywords: tool use, mcp, agentic, environment. Status: pending-review.
- Source: [[papers/2608.06197]] | https://huggingface.co/papers/2608.06197
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05565). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.05565]] | https://huggingface.co/papers/2608.05565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04956). Keywords: workflow. Status: pending-review.
- Source: [[papers/2608.04956]] | https://huggingface.co/papers/2608.04956
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06257). Keywords: multi-agent, environment. Status: pending-review.
- Source: [[papers/2608.06257]] | https://huggingface.co/papers/2608.06257
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06020). Keywords: agentic, planning, environment, sandbox. Status: pending-review.
- Source: [[papers/2608.06020]] | https://huggingface.co/papers/2608.06020
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05785). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.05785]] | https://huggingface.co/papers/2608.05785
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06216). Keywords: harness. Status: pending-review.
- Source: [[papers/2608.06216]] | https://huggingface.co/papers/2608.06216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05850). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.05850]] | https://huggingface.co/papers/2608.05850
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03451). Keywords: agent harness, harness, execution. Status: pending-review.
- Source: [[papers/2608.03451]] | https://huggingface.co/papers/2608.03451
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03972). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.03972]] | https://huggingface.co/papers/2608.03972
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05131). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.05131]] | https://huggingface.co/papers/2608.05131
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04436). Keywords: tool use, agentic, workflow. Status: pending-review.
- Source: [[papers/2608.04436]] | https://huggingface.co/papers/2608.04436
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04701). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.04701]] | https://huggingface.co/papers/2608.04701
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28048). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.28048]] | https://huggingface.co/papers/2607.28048
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04397). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.04397]] | https://huggingface.co/papers/2608.04397
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05013). Keywords: autonomous agent, workflow, harness, environment. Status: pending-review.
- Source: [[papers/2608.05013]] | https://huggingface.co/papers/2608.05013
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04964). Keywords: planning, execution. Status: pending-review.
- Source: [[papers/2608.04964]] | https://huggingface.co/papers/2608.04964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05042). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.05042]] | https://huggingface.co/papers/2608.05042
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00782). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.00782]] | https://huggingface.co/papers/2608.00782
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04505). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.04505]] | https://huggingface.co/papers/2608.04505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.24821). Keywords: execution. Status: pending-review.
- Source: [[papers/2607.24821]] | https://huggingface.co/papers/2607.24821
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03764). Keywords: workflow, harness. Status: pending-review.
- Source: [[papers/2608.03764]] | https://huggingface.co/papers/2608.03764
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05102). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.05102]] | https://huggingface.co/papers/2608.05102
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03392). Keywords: agentic, gui, workflow. Status: pending-review.
- Source: [[papers/2608.03392]] | https://huggingface.co/papers/2608.03392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03836). Keywords: workflow, harness, execution. Status: pending-review.
- Source: [[papers/2608.03836]] | https://huggingface.co/papers/2608.03836
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00155). Keywords: agentic, gui. Status: pending-review.
- Source: [[papers/2608.00155]] | https://huggingface.co/papers/2608.00155
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02437). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.02437]] | https://huggingface.co/papers/2608.02437
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28956). Keywords: tool use, environment. Status: pending-review.
- Source: [[papers/2607.28956]] | https://huggingface.co/papers/2607.28956
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03971). Keywords: recursive, agentic. Status: pending-review.
- Source: [[papers/2608.03971]] | https://huggingface.co/papers/2608.03971
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02711). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.02711]] | https://huggingface.co/papers/2608.02711
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04007). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.04007]] | https://huggingface.co/papers/2608.04007
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02589). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.02589]] | https://huggingface.co/papers/2608.02589
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01837). Keywords: agentic, gui, environment. Status: pending-review.
- Source: [[papers/2608.01837]] | https://huggingface.co/papers/2608.01837
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04003). Keywords: recursive, self-improvement, gui. Status: pending-review.
- Source: [[papers/2608.04003]] | https://huggingface.co/papers/2608.04003
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02713). Keywords: gui, environment, execution. Status: pending-review.
- Source: [[papers/2608.02713]] | https://huggingface.co/papers/2608.02713
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03979). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.03979]] | https://huggingface.co/papers/2608.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03457). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.03457]] | https://huggingface.co/papers/2608.03457
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02218). Keywords: multi-agent, gui, workflow. Status: pending-review.
- Source: [[papers/2608.02218]] | https://huggingface.co/papers/2608.02218
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03874). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.03874]] | https://huggingface.co/papers/2608.03874
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01127). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.01127]] | https://huggingface.co/papers/2608.01127
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03507). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.03507]] | https://huggingface.co/papers/2608.03507
- Confidence: Low (auto-matched, not yet reviewed)
- Source: [[portfolio-dashboard.md]]
- Confidence: Medium
https://huggingface.co/papers/2608.02287
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01678). Keywords: execution. Status: pending-review.
- Source: [[papers/2608.01678]] | https://huggingface.co/papers/2608.01678
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00079). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.00079]] | https://huggingface.co/papers/2608.00079
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01964). Keywords: agent harness, tool use, harness, environment. Status: pending-review.
- Source: [[papers/2608.01964]] | https://huggingface.co/papers/2608.01964
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01735). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.01735]] | https://huggingface.co/papers/2608.01735
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01185). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.01185]] | https://huggingface.co/papers/2608.01185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01827). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.01827]] | https://huggingface.co/papers/2608.01827
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00574). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.00574]] | https://huggingface.co/papers/2608.00574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29241). Keywords: agentic, harness. Status: pending-review.
- Source: [[papers/2607.29241]] | https://huggingface.co/papers/2607.29241
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28802). Keywords: multi-agent, harness, scaffold, environment. Status: pending-review.
- Source: [[papers/2607.28802]] | https://huggingface.co/papers/2607.28802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29122). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.29122]] | https://huggingface.co/papers/2607.29122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01462). Keywords: harness. Status: pending-review.
- Source: [[papers/2608.01462]] | https://huggingface.co/papers/2608.01462
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01397). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.01397]] | https://huggingface.co/papers/2608.01397
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26497). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.26497]] | https://huggingface.co/papers/2607.26497
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28227). Keywords: browser, computer use, gui, workflow. Status: pending-review.
- Source: [[papers/2607.28227]] | https://huggingface.co/papers/2607.28227
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.18806). Keywords: planning, orchestration, workflow. Status: pending-review.
- Source: [[papers/2607.18806]] | https://huggingface.co/papers/2607.18806
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27372). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.27372]] | https://huggingface.co/papers/2607.27372
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28374). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.28374]] | https://huggingface.co/papers/2607.28374
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28362). Keywords: environment. Status: pending-review.
- Source: [[papers/2607.28362]] | https://huggingface.co/papers/2607.28362
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.20891). Keywords: planning, workflow, environment. Status: pending-review.
- Source: [[papers/2607.20891]] | https://huggingface.co/papers/2607.20891
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26637). Keywords: harness, sandbox, execution. Status: pending-review.
- Source: [[papers/2607.26637]] | https://huggingface.co/papers/2607.26637
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28308). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.28308]] | https://huggingface.co/papers/2607.28308
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28582). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.28582]] | https://huggingface.co/papers/2607.28582
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23802). Keywords: self-improvement, multi-agent, environment. Status: pending-review.
- Source: [[papers/2607.23802]] | https://huggingface.co/papers/2607.23802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28675). Keywords: scaffold. Status: pending-review.
- Source: [[papers/2607.28675]] | https://huggingface.co/papers/2607.28675
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29677). Keywords: agentic, gui, workflow. Status: pending-review.
- Source: [[papers/2607.29677]] | https://huggingface.co/papers/2607.29677
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.18082). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.18082]] | https://huggingface.co/papers/2607.18082
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23783). Keywords: execution. Status: pending-review.
- Source: [[papers/2607.23783]] | https://huggingface.co/papers/2607.23783
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27924). Keywords: planning. Status: pending-review.
- Source: [[papers/2607.27924]] | https://huggingface.co/papers/2607.27924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28443). Keywords: planning. Status: pending-review.
- Source: [[papers/2607.28443]] | https://huggingface.co/papers/2607.28443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27201). Keywords: planning. Status: pending-review.
- Source: [[papers/2607.27201]] | https://huggingface.co/papers/2607.27201
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.15820). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.15820]] | https://huggingface.co/papers/2607.15820
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25388). Keywords: multi-agent, planning. Status: pending-review.
- Source: [[papers/2607.25388]] | https://huggingface.co/papers/2607.25388
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29209). Keywords: code generation. Status: pending-review.
- Source: [[papers/2607.29209]] | https://huggingface.co/papers/2607.29209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27851). Keywords: gui. Status: pending-review.
- Source: [[papers/2607.27851]] | https://huggingface.co/papers/2607.27851
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28595). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.28595]] | https://huggingface.co/papers/2607.28595
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21461). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2607.21461]] | https://huggingface.co/papers/2607.21461
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.14777). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.14777]] | https://huggingface.co/papers/2607.14777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.13104). Keywords: self-improvement, agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2607.13104]] | https://huggingface.co/papers/2607.13104
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12625). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2607.12625]] | https://huggingface.co/papers/2607.12625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05382). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2607.05382]] | https://huggingface.co/papers/2607.05382
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.08093). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.08093]] | https://huggingface.co/papers/2607.08093
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.01232). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.01232]] | https://huggingface.co/papers/2607.01232
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05369). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2607.05369]] | https://huggingface.co/papers/2607.05369
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05391). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.05391]] | https://huggingface.co/papers/2607.05391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.29315). Keywords: self-improvement, agentic. Status: pending-review.
- Source: [[papers/2606.29315]] | https://huggingface.co/papers/2606.29315
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.32017). Keywords: agentic. Status: pending-review.
- Source: [[papers/2606.32017]] | https://huggingface.co/papers/2606.32017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.26080). Keywords: agentic. Status: pending-review.
- Source: [[papers/2606.26080]] | https://huggingface.co/papers/2606.26080
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.18831). Keywords: agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2606.18831]] | https://huggingface.co/papers/2606.18831
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.19980). Keywords: self-improvement, tool use, agentic. Status: pending-review.
- Source: [[papers/2606.19980]] | https://huggingface.co/papers/2606.19980
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.19236). Keywords: tool use. Status: pending-review.
- Source: [[papers/2606.19236]] | https://huggingface.co/papers/2606.19236
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.15007). Keywords: agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2606.15007]] | https://huggingface.co/papers/2606.15007
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.18401). Keywords: agentic. Status: pending-review.
- Source: [[papers/2604.18401]] | https://huggingface.co/papers/2604.18401
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.13707). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2606.13707]] | https://huggingface.co/papers/2606.13707
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.14249). Keywords: agent harness, multi-agent. Status: pending-review.
- Source: [[papers/2606.14249]] | https://huggingface.co/papers/2606.14249
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.14502). Keywords: self-improvement, tool use. Status: pending-review.
- Source: [[papers/2606.14502]] | https://huggingface.co/papers/2606.14502
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03108). Keywords: agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2606.03108]] | https://huggingface.co/papers/2606.03108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.07299). Keywords: recursive, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2606.07299]] | https://huggingface.co/papers/2606.07299
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28742). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.28742]] | https://huggingface.co/papers/2605.28742
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03841). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2606.03841]] | https://huggingface.co/papers/2606.03841
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.04455). Keywords: recursive, self-improvement, autonomous agent. Status: pending-review.
- Source: [[papers/2606.04455]] | https://huggingface.co/papers/2606.04455
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.01770). Keywords: self-improvement, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2606.01770]] | https://huggingface.co/papers/2606.01770
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03979). Keywords: recursive, self-improvement. Status: pending-review.
- Source: [[papers/2606.03979]] | https://huggingface.co/papers/2606.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.29861). Keywords: agent harness, tool use, autonomous agent, multi-agent. Status: pending-review.
- Source: [[papers/2605.29861]] | https://huggingface.co/papers/2605.29861
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28424). Keywords: agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2605.28424]] | https://huggingface.co/papers/2605.28424
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28805). Keywords: agentic. Status: pending-review.
- Source: [[papers/2605.28805]] | https://huggingface.co/papers/2605.28805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.24517). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.24517]] | https://huggingface.co/papers/2605.24517
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.20342). Keywords: tool use, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2605.20342]] | https://huggingface.co/papers/2605.20342
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.23218). Keywords: agentic, autonomous agent, multi-agent. Status: pending-review.
- Source: [[papers/2605.23218]] | https://huggingface.co/papers/2605.23218
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.17698). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2605.17698]] | https://huggingface.co/papers/2605.17698
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.18747). Keywords: agent harness, tool use, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2605.18747]] | https://huggingface.co/papers/2605.18747
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.15871). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2605.15871]] | https://huggingface.co/papers/2605.15871
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.14389). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2605.14389]] | https://huggingface.co/papers/2605.14389
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.15040). Keywords: agent harness, tool use, agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2605.15040]] | https://huggingface.co/papers/2605.15040
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.08715). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2605.08715]] | https://huggingface.co/papers/2605.08715
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.09959). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2605.09959]] | https://huggingface.co/papers/2605.09959
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.07510). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2605.07510]] | https://huggingface.co/papers/2605.07510
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.05185). Keywords: agentic. Status: pending-review.
- Source: [[papers/2605.05185]] | https://huggingface.co/papers/2605.05185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.02943). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2605.02943]] | https://huggingface.co/papers/2605.02943
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.03042). Keywords: self-improvement, mcp, multi-agent. Status: pending-review.
- Source: [[papers/2605.03042]] | https://huggingface.co/papers/2605.03042
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.28181). Keywords: self-improvement, agentic. Status: pending-review.
- Source: [[papers/2604.28181]] | https://huggingface.co/papers/2604.28181
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.11544). Keywords: agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2604.11544]] | https://huggingface.co/papers/2604.11544
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.05336). Keywords: self-improvement, tool use, agentic. Status: pending-review.
- Source: [[papers/2604.05336]] | https://huggingface.co/papers/2604.05336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.08545). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2604.08545]] | https://huggingface.co/papers/2604.08545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.05846). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2604.05846]] | https://huggingface.co/papers/2604.05846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.06392). Keywords: mcp, multi-agent. Status: pending-review.
- Source: [[papers/2604.06392]] | https://huggingface.co/papers/2604.06392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.25111). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2603.25111]] | https://huggingface.co/papers/2603.25111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.02721). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2604.02721]] | https://huggingface.co/papers/2604.02721
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.18118). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2603.18118]] | https://huggingface.co/papers/2603.18118
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.08262). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2603.08262]] | https://huggingface.co/papers/2603.08262
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.09018). Keywords: tool use, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2603.09018]] | https://huggingface.co/papers/2603.09018
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.06333). Keywords: recursive, self-improvement. Status: pending-review.
- Source: [[papers/2603.06333]] | https://huggingface.co/papers/2603.06333
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.21320). Keywords: agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2602.21320]] | https://huggingface.co/papers/2602.21320
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.16928). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2602.16928]] | https://huggingface.co/papers/2602.16928
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.11541). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2602.11541]] | https://huggingface.co/papers/2602.11541
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.09877). Keywords: self-improvement, multi-agent. Status: pending-review.
- Source: [[papers/2602.09877]] | https://huggingface.co/papers/2602.09877
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.10604). Keywords: self-improvement, tool use, agentic. Status: pending-review.
- Source: [[papers/2602.10604]] | https://huggingface.co/papers/2602.10604
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.08847). Keywords: tool use, multi-agent. Status: pending-review.
- Source: [[papers/2602.08847]] | https://huggingface.co/papers/2602.08847
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.09443). Keywords: agentic. Status: pending-review.
- Source: [[papers/2602.09443]] | https://huggingface.co/papers/2602.09443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06855). Keywords: agentic. Status: pending-review.
- Source: [[papers/2602.06855]] | https://huggingface.co/papers/2602.06855
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.07085). Keywords: agentic. Status: pending-review.
- Source: [[papers/2602.07085]] | https://huggingface.co/papers/2602.07085
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06130). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2602.06130]] | https://huggingface.co/papers/2602.06130
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06030). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2602.06030]] | https://huggingface.co/papers/2602.06030
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.02751). Keywords: self-improvement, agentic. Status: pending-review.
- Source: [[papers/2602.02751]] | https://huggingface.co/papers/2602.02751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.03798). Keywords: self-improvement, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2602.03798]] | https://huggingface.co/papers/2602.03798
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.20802). Keywords: tool use. Status: pending-review.
- Source: [[papers/2601.20802]] | https://huggingface.co/papers/2601.20802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.18778). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2601.18778]] | https://huggingface.co/papers/2601.18778
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.15690). Keywords: self-improvement, tool use, autonomous agent. Status: pending-review.
- Source: [[papers/2601.15690]] | https://huggingface.co/papers/2601.15690
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.12538). Keywords: tool use, agentic, autonomous agent, multi-agent. Status: pending-review.
- Source: [[papers/2601.12538]] | https://huggingface.co/papers/2601.12538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.09113). Keywords: agentic, autonomous agent, multi-agent. Status: pending-review.
- Source: [[papers/2601.09113]] | https://huggingface.co/papers/2601.09113
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.02075). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2601.02075]] | https://huggingface.co/papers/2601.02075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.17102). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2512.17102]] | https://huggingface.co/papers/2512.17102
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.11251). Keywords: agentic. Status: pending-review.
- Source: [[papers/2512.11251]] | https://huggingface.co/papers/2512.11251
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.08296). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2512.08296]] | https://huggingface.co/papers/2512.08296
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.04797). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2512.04797]] | https://huggingface.co/papers/2512.04797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.03773). Keywords: self-improvement, autonomous agent. Status: pending-review.
- Source: [[papers/2511.03773]] | https://huggingface.co/papers/2511.03773
- Confidence: Low (auto-matched, not yet reviewed)
  Multi-Turn
- HF trending paper (arxiv: 2510.24645). Keywords: tool use, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2510.24645]] | https://huggingface.co/papers/2510.24645
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.24684). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2510.24684]] | https://huggingface.co/papers/2510.24684
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.23272). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2510.23272]] | https://huggingface.co/papers/2510.23272
- Confidence: Low (auto-matched, not yet reviewed)
  Learning F
- HF trending paper (arxiv: 2510.14264). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2510.14264]] | https://huggingface.co/papers/2510.14264
- Confidence: Low (auto-matched, not yet reviewed)
  Agentic A
- HF trending paper (arxiv: 2510.16720). Keywords: tool use, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2510.16720]] | https://huggingface.co/papers/2510.16720
- Confidence: Low (auto-matched, not yet reviewed)
  Enterprise A
- HF trending paper (arxiv: 2510.17797). Keywords: mcp, agentic, autonomous agent, multi-agent. Status: pending-review.
- Source: [[papers/2510.17797]] | https://huggingface.co/papers/2510.17797
- Confidence: Low (auto-matched, not yet reviewed)
  LLMs
- HF trending paper (arxiv: 2510.11062). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2510.11062]] | https://huggingface.co/papers/2510.11062
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.07841). Keywords: self-improvement, agentic. Status: pending-review.
- Source: [[papers/2510.07841]] | https://huggingface.co/papers/2510.07841
- Confidence: Low (auto-matched, not yet reviewed)
  Academic P
- HF trending paper (arxiv: 2510.05571). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2510.05571]] | https://huggingface.co/papers/2510.05571
- Confidence: Low (auto-matched, not yet reviewed)
  Synthesi
- HF trending paper (arxiv: 2509.24107). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2509.24107]] | https://huggingface.co/papers/2509.24107
- Confidence: Low (auto-matched, not yet reviewed)
  Co-Evolution in M
- HF trending paper (arxiv: 2510.01586). Keywords: tool use, multi-agent. Status: pending-review.
- Source: [[papers/2510.01586]] | https://huggingface.co/papers/2510.01586
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.01538). Keywords: agentic. Status: pending-review.
- Source: [[papers/2510.01538]] | https://huggingface.co/papers/2510.01538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.24720). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.24720]] | https://huggingface.co/papers/2607.24720
- Confidence: Low (auto-matched, not yet reviewed)
  Markets?
- HF trending paper (arxiv: 2510.02209). Keywords: tool use, autonomous agent. Status: pending-review.
- Source: [[papers/2510.02209]] | https://huggingface.co/papers/2510.02209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.24280). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2607.24280]] | https://huggingface.co/papers/2607.24280
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21653). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.21653]] | https://huggingface.co/papers/2607.21653
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.20709). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.20709]] | https://huggingface.co/papers/2607.20709
- Confidence: Low (auto-matched, not yet reviewed)
  Self-Play
- HF trending paper (arxiv: 2509.25541). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2509.25541]] | https://huggingface.co/papers/2509.25541
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.21461). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2607.21461]] | https://huggingface.co/papers/2607.21461
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16204). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.16204]] | https://huggingface.co/papers/2607.16204
- Confidence: Low (auto-matched, not yet reviewed)
  Explorat
- HF trending paper (arxiv: 2509.22601). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2509.22601]] | https://huggingface.co/papers/2509.22601
- Confidence: Low (auto-matched, not yet reviewed)
  Learning
- HF trending paper (arxiv: 2509.19736). Keywords: agentic. Status: pending-review.
- Source: [[papers/2509.19736]] | https://huggingface.co/papers/2509.19736
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16169). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.16169]] | https://huggingface.co/papers/2607.16169
- Confidence: Low (auto-matched, not yet reviewed)
  Framewo
- HF trending paper (arxiv: 2509.14180). Keywords: agentic. Status: pending-review.
- Source: [[papers/2509.14180]] | https://huggingface.co/papers/2509.14180
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.09995). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2509.09995]] | https://huggingface.co/papers/2509.09995
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.14777). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.14777]] | https://huggingface.co/papers/2607.14777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.13104). Keywords: self-improvement, agentic, autonomous agent. Status: pending-review.
- Source: [[papers/2607.13104]] | https://huggingface.co/papers/2607.13104
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.06733). Keywords: agentic. Status: pending-review.
- Source: [[papers/2509.06733]] | https://huggingface.co/papers/2509.06733
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.04575). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2509.04575]] | https://huggingface.co/papers/2509.04575
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12625). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2607.12625]] | https://huggingface.co/papers/2607.12625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.01055). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2509.01055]] | https://huggingface.co/papers/2509.01055
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.02547). Keywords: self-improvement, tool use, agentic. Status: pending-review.
- Source: [[papers/2509.02547]] | https://huggingface.co/papers/2509.02547
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.10522). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2607.10522]] | https://huggingface.co/papers/2607.10522
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05382). Keywords: recursive, self-improvement, agentic. Status: pending-review.
- Source: [[papers/2607.05382]] | https://huggingface.co/papers/2607.05382
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.08093). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.08093]] | https://huggingface.co/papers/2607.08093
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.07508). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.07508]] | https://huggingface.co/papers/2607.07508
- Confidence: Low (auto-matched, not yet reviewed)
  Experi
- HF trending paper (arxiv: 2508.04700). Keywords: agentic. Status: pending-review.
- Source: [[papers/2508.04700]] | https://huggingface.co/papers/2508.04700
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.01232). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.01232]] | https://huggingface.co/papers/2607.01232
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05369). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2607.05369]] | https://huggingface.co/papers/2607.05369
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.05391). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.05391]] | https://huggingface.co/papers/2607.05391
- Confidence: Low (auto-matched, not yet reviewed)
  Foundati
- HF trending paper (arxiv: 2507.00951). Keywords: tool use, agentic, multi-agent. Status: pending-review.
- Source: [[papers/2507.00951]] | https://huggingface.co/papers/2507.00951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.31036). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2606.31036]] | https://huggingface.co/papers/2606.31036
- Confidence: Low (auto-matched, not yet reviewed)
  Multi-Agent Mul
- HF trending paper (arxiv: 2506.24119). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2506.24119]] | https://huggingface.co/papers/2506.24119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.00407). Keywords: agentic, multi-agent. Status: pending-review.
- Source: [[papers/2607.00407]] | https://huggingface.co/papers/2607.00407
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.29315). Keywords: self-improvement, agentic. Status: pending-review.
- Source: [[papers/2606.29315]] | https://huggingface.co/papers/2606.29315
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.32017). Keywords: agentic. Status: pending-review.
- Source: [[papers/2606.32017]] | https://huggingface.co/papers/2606.32017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25565). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.25565]] | https://huggingface.co/papers/2607.25565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25108). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2607.25108]] | https://huggingface.co/papers/2607.25108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26115). Keywords: self-improvement. Status: pending-review.
- Source: [[papers/2607.26115]] | https://huggingface.co/papers/2607.26115
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26784). Keywords: agentic. Status: pending-review.
- Source: [[papers/2607.26784]] | https://huggingface.co/papers/2607.26784
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27703). Keywords: tool use, agentic. Status: pending-review.
- Source: [[papers/2607.27703]] | https://huggingface.co/papers/2607.27703
- Confidence: Low (auto-matched, not yet reviewed)
- Claude Fable 5's 17.5K-word prompt covers behavior + tool schemas + MCP + file architecture + safety. Prompt evolved from 'how to behave' to 'how the product works.' Modular tag-based sectioning enables A/B testing of prompt components — meta-level prompt self-improvement infrastructure.
- Source: [[references/claude-fable-5-system-prompt]]
- Confidence: High

### 2026-08-19: Skill saliency by intervention — amortized explainer as routing signal (arXiv:2608.12921)
- E2-Explainer's masking objective is a do-operator: ablate each channel, measure outcome delta; distilling expensive ablations into a cheap predictor of load-bearing components is structurally identical to skill routing in a large stack — and pruning causally-redundant edges lost no task performance.
- Source: [[papers/e2-explainer-mas-topologies]]
- Confidence: High

### 2026-08-19: β (co-failure ceiling) upgrade path — from statistics to causal estimation

### 2026-08-19: DiSCO: Defending text-to-image generation through distribution-guided contrastiv

### 2026-08-19: Demystifying Agent Skills: Why They Work-Until They Don't

### 2026-08-19: EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing

### 2026-08-19: CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Gu

### 2026-08-19: MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Ve

### 2026-08-19: Agent Lightning v1.0: Towards Harnessed Agentic RL

### 2026-08-19: HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

### 2026-08-19: FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution

### 2026-08-19: Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation

### 2026-08-19: Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents

### 2026-08-19: Energy-Guided Flow Matching

### 2026-08-19: Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Ind

### 2026-08-19: ASI-Bench: At the Dawn of Artificial Superintelligence

### 2026-08-19: StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End

### 2026-08-19: aDSL: Agentic 3D Creation via Joint Agent-Program Design

### 2026-08-19: From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

### 2026-08-19: Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements

### 2026-08-19: Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning

### 2026-08-20: SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents

### 2026-08-20: Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

### 2026-08-20: Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre E

### 2026-08-20: Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical In

### 2026-08-20: Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditi

### 2026-08-20: Training Leaves Traces: Centered Residual Signatures for Language Model Lineage 

### 2026-08-20: Training Chemical Plausibility-Aware Large Language Models for Single-Step Retro

### 2026-08-20: SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Gener

### 2026-08-20: Looped Language Models Improve Compositional Tool Calling

### 2026-08-20: FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents

### 2026-08-20: The Problem Is the Problem: Towards Scalable Mathematical Discovery

### 2026-08-20: LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents
- HF trending paper (arxiv: 2608.17393). Keywords: agent harness, orchestration, harness, environment. Status: pending-review.
- Source: [[papers/2608.17393]] | https://huggingface.co/papers/2608.17393
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16977). Keywords: workflow. Status: pending-review.
- Source: [[papers/2608.16977]] | https://huggingface.co/papers/2608.16977
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18423). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.18423]] | https://huggingface.co/papers/2608.18423
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18171). Keywords: tool use, agentic, planning, tool calling. Status: pending-review.
- Source: [[papers/2608.18171]] | https://huggingface.co/papers/2608.18171
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18565). Keywords: agent harness, code generation, harness, execution. Status: pending-review.
- Source: [[papers/2608.18565]] | https://huggingface.co/papers/2608.18565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18940). Keywords: planning. Status: pending-review.
- Source: [[papers/2608.18940]] | https://huggingface.co/papers/2608.18940
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14929). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.14929]] | https://huggingface.co/papers/2608.14929
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18746). Keywords: gui, planning. Status: pending-review.
- Source: [[papers/2608.18746]] | https://huggingface.co/papers/2608.18746
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16590). Keywords: agentic, harness, environment, execution. Status: pending-review.
- Source: [[papers/2608.16590]] | https://huggingface.co/papers/2608.16590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13947). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.13947]] | https://huggingface.co/papers/2608.13947
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17253). Keywords: multi-agent. Status: pending-review.
- Source: [[papers/2608.17253]] | https://huggingface.co/papers/2608.17253
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18852). Keywords: agentic, execution. Status: pending-review.
- Source: [[papers/2608.18852]] | https://huggingface.co/papers/2608.18852
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15869). Keywords: environment. Status: pending-review.
- Source: [[papers/2608.15869]] | https://huggingface.co/papers/2608.15869
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17310). Keywords: agentic. Status: pending-review.
- Source: [[papers/2608.17310]] | https://huggingface.co/papers/2608.17310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16002). Keywords: gui, environment, execution. Status: pending-review.
- Source: [[papers/2608.16002]] | https://huggingface.co/papers/2608.16002
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17975). Keywords: agentic, multi-agent, workflow, execution. Status: pending-review.
- Source: [[papers/2608.17975]] | https://huggingface.co/papers/2608.17975
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17800). Keywords: agent harness, workflow, harness. Status: pending-review.
- Source: [[papers/2608.17800]] | https://huggingface.co/papers/2608.17800
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17271). Keywords: gui, sandbox, execution. Status: pending-review.
- Source: [[papers/2608.17271]] | https://huggingface.co/papers/2608.17271
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16393). Keywords: harness, execution. Status: pending-review.
- Source: [[papers/2608.16393]] | https://huggingface.co/papers/2608.16393
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05811). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.05811]] | https://huggingface.co/papers/2608.05811
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15008). Keywords: gui, harness. Status: pending-review.
- Source: [[papers/2608.15008]] | https://huggingface.co/papers/2608.15008
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17512). Keywords: planning, environment, execution. Status: pending-review.
- Source: [[papers/2608.17512]] | https://huggingface.co/papers/2608.17512
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16157). Keywords: agentic, execution. Status: pending-review.
- Source: [[papers/2608.16157]] | https://huggingface.co/papers/2608.16157
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17597). Keywords: agent harness, workflow, harness, sandbox. Status: pending-review.
- Source: [[papers/2608.17597]] | https://huggingface.co/papers/2608.17597
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17528). Keywords: agent harness, agentic, workflow, harness. Status: pending-review.
- Source: [[papers/2608.17528]] | https://huggingface.co/papers/2608.17528
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14221). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.14221]] | https://huggingface.co/papers/2608.14221
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17566). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.17566]] | https://huggingface.co/papers/2608.17566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18063). Keywords: gui, workflow. Status: pending-review.
- Source: [[papers/2608.18063]] | https://huggingface.co/papers/2608.18063
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14036). Keywords: agent harness, gui, workflow, harness. Status: pending-review.
- Source: [[papers/2608.14036]] | https://huggingface.co/papers/2608.14036
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17067). Keywords: gui. Status: pending-review.
- Source: [[papers/2608.17067]] | https://huggingface.co/papers/2608.17067
- Confidence: Low (auto-matched, not yet reviewed)
- Conditional causal discovery (arXiv:2608.12640) can re-express β as a posterior over causal structure given the co-failure event, separating shared-cause co-failure (fixable by decoupling components) from coincidental co-occurrence — a distinction frequency-counted β cannot make; co-failures are tail events, the rare-posterior-mass regime this method was built for.
- Source: [[concepts/co-failure-ceiling]]
- Confidence: Medium
