---
date: 2026-06-21
type: gap-analysis
title: "Game Theory Gaps in Methodology & Skills"
created: 2026-06-21
status: active
tags: [gap-analysis, game-theory, methodology, skills, finance, agents]
---

# Game Theory Gaps in Methodology & Skills

## Context

Audited 2026-06-21. Wiki has 167 game theory mentions across ~95 files (rich knowledge layer). Skills have 55 mentions across ~38 files, but most are decorative ("strategic positioning") not operational. The CWM paper ingest (Lehrach et al., 2025) surfaced the pattern: **formalize the game rules as executable code, then use classical solvers.** The gaps below are where game theory should be operationalized but isn't.

## Gap Inventory

### GAP-1: No Game-Theoretic Finance Analysis [HIGH LEVERAGE]

**Problem:** Markets are multi-player games. Current finance skills (options-market-analysis, competitive-analysis, thesis-tracker) treat them as optimization or description problems. No skill models: Who are the players? What are their payoffs? What's the equilibrium? What move exploits mispricing?

**Missing capabilities:**
- Player belief modeling (what does the other side believe?)
- Payoff matrix construction for market scenarios
- Nash equilibrium computation for competitive dynamics
- Signaling game analysis (what do options flows signal about informed traders?)
- Mechanism design for trade execution (optimal order splitting as a game against predatory strategies)
- **Simulation** — agent-based market simulation to test strategies against adaptive opponents

**Affected skills:** options-market-analysis, competitive-analysis, thesis-tracker, buyer-list, dcf-model, comps-analysis

**Status:** → STARTING (2026-06-21). See `game-theoretic-finance-analysis` skill.

---

### GAP-2: No Mechanism Design for Multi-Agent Orchestration [HIGH LEVERAGE]

**Problem:** Symphony (6 agents, 15 assignees) is a principal-agent game. Workers can "phone it in" (observed in STORM runs). Current mitigation is monitoring (review/unblock), which is reactive. No skill applies mechanism design — structuring incentives so quality is the dominant strategy.

**Missing capabilities:**
- Scoring rules that incentivize honest difficulty estimates
- Self-selection mechanisms (revealed preference for task assignment)
- Verification games (how much checking is game-theoretically optimal?)
- Moral hazard modeling (worker effort as hidden action)

**Affected skills:** kanban-orchestrator, kanban-worker, delegate-task-protocol, storm-research

---

### GAP-3: STORM Overlap Not Optimized [MEDIUM LEVERAGE]

**Problem:** STORM persona overlap (30%) is a heuristic. The optimal overlap is a coverage problem: minimize total search cost while guaranteeing all questions are answered with cross-validation.

**Missing capabilities:**
- Formal coverage optimization (set cover problem)
- Shapley value computation for persona contribution
- Free-ride detection (persona relying on others' searches)
- Correlation-aware redundancy (overlapping personas should cover different sources, not same)

**Affected skills:** storm-research

---

### GAP-4: Kanban Task Assignment = Manual, Not Game-Theoretic [MEDIUM LEVERAGE]

**Problem:** Task assignment is an assignment game (Shapley-Shubik). Current skill uses manual/orchestrator assignment. No market mechanism.

**Missing capabilities:**
- Self-selection / auction mechanism for task assignment
- Scoring rules for honest capability signaling
- Claim race modeling (is first-come-first-served optimal?)

**Affected skills:** kanban-orchestrator

---

### GAP-5: Adversarial Review Depth Not Formalized [MEDIUM LEVERAGE]

**Problem:** Critical review and meta-critic use adversarial review but don't formalize the minimax depth or game type (zero-sum vs cooperative).

**Missing capabilities:**
- Minimax depth specification (how many counter-moves deep?)
- Game type classification (zero-sum critique vs cooperative improvement)
- Optimal mixed strategy for critic (randomize critique dimensions to avoid gaming)

**Affected skills:** critical-review, meta-critic, self-harness

---

### GAP-6: Monitoring Frequency Not Optimized [LOW LEVERAGE]

**Problem:** Cron monitoring (SPCX, email, heartbeat) plays a repeated game against the environment. Frequency is heuristic, not optimized.

**Missing capabilities:**
- Optimal stopping theory for monitoring frequency
- Signal value of silence (absence of news = news)
- Cost-of-information vs cost-of-ignorance tradeoff

**Affected skills:** hermes-cron-management, inbox-triage, SPCX monitor

---

### GAP-7: Wiki Consensus = Coordination Game [LOW LEVERAGE]

**Problem:** Cross-linker, dedup, and canonical-page selection are coordination games on a graph. No skill formalizes consensus.

**Missing capabilities:**
- Consensus protocol for canonical page selection
- Schelling point identification (which page is the natural focal point?)
- Network effects in cross-linking (more links = more canonical?)

**Affected skills:** cross-linker, wiki-dedup, wiki-lint

---

## Priority Order

1. **GAP-1** (finance game theory) — Highest leverage. Markets are literally games. Starting now.
2. **GAP-2** (mechanism design for agents) — High leverage. We've already observed the failure mode (STORM phoned-in personas).
3. **GAP-5** (adversarial review depth) — Medium leverage, directly improves quality of all review skills.
4. **GAP-3** (STORM overlap optimization) — Medium, narrolder scope.
5. **GAP-4** (kanban assignment) — Medium, would benefit from GAP-2 first.
6. **GAP-6** (monitoring frequency) — Low, optimization not game theory per se.
7. **GAP-7** (wiki consensus) — Low, interesting but not urgent.

## Reference

- CWM paper: Lehrach et al. (2025), [arXiv:2510.04542](https://doi.org/10.48550/arxiv.2510.04542)
- Wiki synthesis: [[wiki/synthesis/cwm-game-theory-application]]
- Audit performed: 2026-06-21
