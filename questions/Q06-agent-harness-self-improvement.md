---
tags: [permanent-question, research, ai-agents]
created: 2026-05-25
question: "Beyond generic metalearning — what specific architectural and algorithmic ideas let agents build better toolchains, improve their own prompting, and recursively self-optimize? How does this apply to quantitative research workflows?"
type: permanent-question
reviewed: 2026-06-17
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
