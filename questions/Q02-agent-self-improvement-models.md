---
tags: [permanent-question, research, ai-agents]
created: 2026-05-25
question: "What are the frontier approaches for agents to improve their own scaffolding, tool use, and learning harness? Metalearning, self-critique, recursive improvement — what's working?"
type: permanent-question
reviewed: 2026-06-17
status: Active - accumulating
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
|- Not all memory is equally important. Agents benefit from explicit memory tiers:
|  1. **Ephemeral** (current conversation context) — fast, small, volatile
|  2. **Working** (session-level reflections, in-progress results) — lasts a session
|  3. **Semantic** (facts, patterns, lessons across sessions) — persistent, retrievable
|  4. **Procedural** (skills, methodologies, templates) — executable knowledge, versioned
|  5. **Episodic** (full run traces with metadata) — auditable, replayable
|- Tiering allows an agent to decide *what to remember* and *how fast to retrieve*, rather than drowning in uniform storage
|- Hermes implements this via: `memories/` (episodic + procedural), skill files (procedural), and system prompt (working/ephemeral)

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

## Last Updated
_2026-06-17_ — Added new papers (Self-Harness, AutoHarness, Evolving Agents in the Dark) to Key Papers section
_2026-06-13_ — Added June 2026 findings: causal AI pipeline deepening, Self-Harness applied, dashboard fixes, Headroom compression, /last30days skill, loop engineering
