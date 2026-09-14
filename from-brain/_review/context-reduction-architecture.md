---
type: note
title: 'Context Reduction Architecture: Three-File Pattern'
related:
  - concept/github-skill-discovery-loop
  - projects/loop-engineering
  - autoresearch-pattern
sources:
  - 'https://x.com/0xnoryxx/status/2082482833755402509'
  - 'https://x.com/rvaniaaaa/status/2082562583131726050'
ingested: '2026-07-29T00:00:00.000Z'
ingested_via: put_page
ingested_at: '2026-07-30T03:19:51.065Z'
source_kind: put_page
tags:
  - agent-architecture
  - context-engineering
  - hermes
  - skill-design
  - subagents
created: 2026-07-30
---
# Context Reduction Architecture: Three-File Pattern

## Core Principle

One large prompt consumes 100% of available context every turn. Splitting into three lazy-loaded files drops active context to ~20%, with the remaining 80% sitting on disk waiting to be needed. The same work gets done at 1/5th the token cost.

## The Three Layers

### Layer 1: The Law (Always Loaded, ~2K tokens)

| Concept | File | Purpose |
|---------|------|---------|
| Claude Code | CLAUDE.md | Conventions, commands, do-nots |
| Hermes | SOUL.md + AGENTS.md | Identity, workspace rules, run book |

**Rule:** A procedure in the law file is a procedure you pay for every turn. Keep it lean. Move anything that's job-specific to a skill.

**What belongs here:** Universal conventions (how to format responses, what requires permission, project structure map, safety rules).

**What does NOT belong here:** Step-by-step procedures for specific tasks (those are skills), role-specific instructions (those are subagents), or one-time context (that's memory).

### Layer 2: Skills (Lazy-Loaded, ~0 tokens until triggered)

| Concept | File | Purpose |
|---------|------|---------|
| Claude Code | skills/*.md | One SKILL.md per job |
| Hermes | ~/.hermes/skills/ | 200+ skills, on-demand loading |

**Rule:** A skill sits on disk costing zero context until the agent matches it to the current task. Only the matched skill loads; the other 199 cost nothing.

**Key distinction:** A prompt library has to be pasted manually. A skill library gets picked automatically by the agent via description/trigger matching.

**What belongs here:** Repeatable procedures with defined inputs and outputs (API calls, data processing, analysis workflows, tool usage patterns).

**Compounding effect:** Every new skill expands the agent's capability surface without growing its base context. The GitHub Skill Discovery Loop automates this — new skills are discovered and added continuously.

### Layer 3: Subagents (Isolated Context, ~0 tokens in parent)

| Concept | File | Purpose |
|---------|------|---------|
| Claude Code | subagents/*.md | Reviewer, tester, migrator roles |
| Hermes | delegate_task | Isolated sessions, summary-only return |

**Rule:** A role in the main prompt drags its entire context into every task. A subagent gets a clean window — its full transcript never enters the parent context. Only the final summary returns.

**What belongs here:** Heavy work that generates large intermediate output (code generation, multi-step research, file processing, parallel tasks).

**Context math:** 2 subagents building 2000 lines of code across 40 API calls each → parent context grows by ~2K tokens (summaries only), not ~80K tokens (full transcripts). This is the 80% reduction.

## Layer 4 (Hermes Extension): GraphWork Topology

Beyond the three-file pattern, Hermes adds a topology layer:

| Layer | File | Purpose |
|-------|------|---------|
| GraphWork | GRAPH.md | DAG topology tracking what's done without re-reading it |

**Why it matters:** Without GRAPH.md, future sessions must re-derive project state from chat history or file timestamps. GRAPH.md is a ~1K token summary of the entire project DAG — nodes, dependencies, exit criteria, status. One read replaces 20 file inspections.

## The Chain (How Layers Connect)

```
AGENTS.md (law)
  → names the skill to use
    → skill names the subagent role
      → subagent does the work, returns summary
        → summary updates GRAPH.md + memory
          → next session reads GRAPH.md, not chat history
```

This chain IS the graph. Three files, not three silos.

## Quantified Impact (Observed)

| Metric | Monolithic Prompt | Three-File Pattern |
|--------|------------------|-------------------|
| Active context per turn | 100% (50K+ tokens) | ~20% (10K tokens) |
| Skill library cost | N/A (all pasted) | 0 tokens (on disk) |
| Subagent work (7 scripts, 2000 LOC) | ~80K tokens in main | ~2K tokens (summary) |
| Cross-session continuity | Re-read entire chat | GRAPH.md + memory (~2K tokens) |

## Implementation Checklist

1. **Audit the law file:** Move anything job-specific to a skill. Keep only universal rules.
2. **Skill-ize repeatable work:** If you type the same procedure twice, it belongs in skills/.
3. **Subagent heavy work:** If a task generates >5K tokens of intermediate output, delegate it.
4. **Graph persistent projects:** For multi-session work, maintain GRAPH.md as state summary.
5. **Memory for facts, not procedures:** Procedures go in skills. Facts/preferences go in memory.
6. **Never paste a prompt library:** Convert it to skills with proper trigger descriptions.
