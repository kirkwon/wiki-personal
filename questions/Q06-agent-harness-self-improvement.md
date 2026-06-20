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

## Connections
- [[Q02]] — general agent self-improvement
- [[Q05]] — applying these ideas to finance specifically
- [[Q01]] — the underlying skills the agent needs
- [[loop-engineering]] — critic separation, triage inbox, skill auto-patch
- [[methodology-loop]] — three-layer meta-system with meta-loop
- [[headroom-integration]] — agent-controlled context compression
- [[memory-tiering]] — 4-tier memory hierarchy with promote/demote/archive

## Last Updated
_2026-06-17_ — Added key papers (Self-Harness, AutoHarness, Evolving Agents in the Dark) to Key Papers section
_2026-06-12_ — Added June 2026 findings: loop engineering, Self-Harness Karpathy, methodology-loop, Headroom MCP, memory tiering, /goal primitive
