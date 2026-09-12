---
tags: [permanent-question, research, ai-agents]
created: 2026-05-25
question: "What are the frontier approaches for agents to improve their own scaffolding, tool use, and learning harness? Metalearning, self-critique, recursive improvement — what's working?"
date: 2026-05-25
type: note
description: "Q02: Agent Self-Improvement Models"
reviewed: 2026-05-25
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
- Practical: Systematic prompt versioning + A/B testing + extracting lessons = "self-improvement"

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
- [[q03]] — self-improvement is limited by learning speed
- [[q06]] — more specific version: recursive improvement in agent harnesses

## Last Updated
_2026-05-25_ — Initial research position
