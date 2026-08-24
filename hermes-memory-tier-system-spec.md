---
title: "Hermes Memory Tier System — Specification v1.0"
date: 2026-06-27
status: draft-spec
type: architecture-spec
tags: [memory-architecture, agent-design, hermes, implementation-spec]
related: "[[agent-layered-architecture-spec]]"
created: 2026-06-28
updated: 2026-06-28
---

# Hermes Memory Tier System — Specification v1.0

## 1. Purpose

Formalize a 4-tier memory hierarchy for Hermes that maximizes context efficiency while preventing tier-boundary decay. This is an operating system for agent memory — not theory, but rules, budgets, and automation that govern what lives where, when facts move, and how conflicts resolve.

## 2. Tier Definitions (Formalized for Hermes)

| Tier | Name | Hermes Implementation | Budget | Load Strategy |
|------|------|-----------------------|--------|---------------|
| **T1** | HOT | System prompt injection (`SOUL.md` + `memory` tool entries) | Dynamic (see §5) | Always loaded, every turn |
| **T2** | WARM | `MEMORY.md` + `USER.md` (curated via `memory` tool) | Dynamic (see §5) | Loaded on session start |
| **T3** | COOL | Skills (`~/.hermes/skills/`) | Unlimited (on-demand) | Loaded via `skill_view()` when triggered |
| **T4** | COLD | GBrain knowledge graph + `memory/YYYY-MM-DD.md` archives | Unlimited (search-only) | Searched via `gbrain think` / `session_search` |

### Content Rules Per Tier

**T1 (HOT) — "Who am I and what am I doing right now"**
- Identity (name, role, operating principles)
- Active anchors (current project IDs, immediate task context)
- Hard constraint: ≤ N chars, must be relevant to THIS session

**T2 (WARM) — "What do I know that's still active"**
- Active project summaries (max 1 line each)
- Key user preferences and corrections
- Stable environment facts (tool URLs, API quirks, conventions)
- Recent decisions still in effect

**T3 (COOL) — "How do I do X"**
- Procedural workflows (skills)
- Tool-specific commands and pitfalls
- Domain methodologies (financial analysis, debugging, etc.)

**T4 (COLD) — "What happened and what's the deep knowledge"**
- Historical session transcripts
- Completed project decisions
- Domain deep knowledge (research, wiki content)
- Raw daily logs

## 3. Promotion Rules (Event-Driven)

Facts flow **upward** (COLD→COOL→WARM→HOT) when they demonstrate repeated relevance.

### Promotion Triggers

| Signal | Action | Mechanism |
|--------|--------|-----------|
| Fact referenced/needed **3+ times** across different sessions | Promote one tier | Observation counter in tracker file |
| User explicitly says "remember this" | Promote immediately to WARM | Manual override |
| Fact needed within first 5 turns of 2 consecutive sessions | Promote to HOT (if ≤100 chars) | Session-start log analysis |
| Procedural pattern repeated across 3+ sessions | Promote to COOL as skill | Skill creation via `skill_manage` |

### Implementation: Observation Tracker

```json
// ~/.hermes/memory/tier-tracker.json
{
  "observations": {
    "fact_fingerprint_hash": {
      "count": 3,
      "first_seen": "2026-06-20",
      "last_seen": "2026-06-27",
      "current_tier": "warm",
      "content_preview": "Firecrawl credits exhausted..."
    }
  }
}
```

- **Fingerprint:** First 200 chars normalized (lowercase, whitespace-collapsed) → SHA256[:16]
- **Update:** On every session, if I look something up that wasn't already in my active tiers, log it as an observation
- **Promotion check:** When `count ≥ 3` and `current_tier != hot`, trigger promotion

## 4. Demotion Rules (Cron-Driven)

Facts flow **downward** (HOT→WARM→COOL→COLD) when they go stale.

### Weekly Demotion Cron (Sundays 09:00)

| Rule | Condition | Action |
|------|-----------|--------|
| **Stale project** | Project not referenced in 14 days | Demote from WARM → COLD (move to GBrain, remove from MEMORY.md) |
| **Completed project** | User confirms "done" or status file says complete | Demote from WARM → COLD immediately |
| **Stale skill** | Skill not invoked in 30 days | Mark `status: dormant` (keep in COOL but don't suggest) |
| **Saturated HOT** | HOT budget > 90% full | Force-evict lowest-importance entry to WARM |

### Demotion Script Logic

```
1. Read MEMORY.md entries
2. For each entry:
   a. Extract entity references (project names, tool names)
   b. Check session_search for mentions in last 14 days
   c. Check gbrain for existing COLD entry
   d. If no mentions AND no gbrain entry → promote to gbrain, then remove from MEMORY.md
   e. If no mentions BUT gbrain entry exists → just remove from MEMORY.md
3. Report what was demoted (structured report-back)
```

## 5. Dynamic Memory Budgets

### Formula

```
T1_HOT_BUDGET  = min(max_context_tokens * 0.008, 1200)    # ~800-1200 chars
T2_WARM_BUDGET = min(max_context_tokens * 0.025, 4000)     # ~2000-4000 chars
USER_BUDGET    = min(max_context_tokens * 0.015, 2000)     # ~1200-2000 chars
```

### Current Values (GLM-5, 128K context)

| Budget | Old (Fixed) | New (Dynamic) | Config Key |
|--------|-------------|---------------|------------|
| WARM (memory) | 2,200 chars | **3,500 chars** | `memory.memory_char_limit` |
| User profile | 1,375 chars | **2,000 chars** | `memory.user_char_limit` |
| HOT | ~500 chars | **800 chars** | (injection budget) |

### Rationale

GLM-5 has 128K token context. 3,500 chars of WARM memory ≈ 875 tokens, which is 0.68% of context — negligible impact on instruction following, meaningful gain in active context density.

## 6. Conflict Resolution

When tiers disagree, **tier precedence** determines truth:

### Precedence Rules

| Conflict Type | Winner | Rationale |
|---------------|--------|-----------|
| **Factual claim** (e.g., "X was cancelled") | **COLD (GBrain)** wins | Curated, timestamped, validated |
| **Operational state** (e.g., "working on X now") | **HOT/WARM** wins | Reflects current reality |
| **User preference** (e.g., "prefers terse responses") | **WARM (USER.md)** wins | Most recent explicit statement |
| **Procedural method** (e.g., "how to deploy") | **COOL (Skill)** wins | Skills are maintained, memory can drift |
| **Timestamp tie** | **Newest wins** | Default fallback |

### Resolution Protocol

1. Detect conflict (contradictory info between tiers on same topic)
2. Apply precedence rule from table above
3. **Log the conflict** to `~/.hermes/memory/conflict-log.jsonl`
4. **Update the losing tier** to match the winner (correct the drift)
5. If unresolvable, flag to user for clarification

## 7. Eviction Policy

When a tier exceeds its budget, importance-scored eviction applies.

### Importance Score

```
importance = (recency_score * 0.40) + (frequency_score * 0.30) + (relevance_score * 0.30)
```

Where:
- **recency_score:** `1.0` if referenced today → `0.0` if >30 days
- **frequency_score:** `min(reference_count / 10, 1.0)`
- **relevance_score:** `1.0` if active project → `0.5` if general knowledge → `0.0` if archived

### Eviction Actions

1. Sort entries by importance score (ascending)
2. Evict lowest-scored entries to next-lower tier
3. Log evictions to tracker
4. Never evict: identity entries, active project anchors, user-stated "always remember" facts

## 8. Write Strategy (Tiered by Severity)

| Severity | Examples | Strategy | Implementation |
|----------|----------|----------|----------------|
| **Critical** | API key change, broken tool, user correction | **Write-through** (immediate) | `memory()` call in same turn |
| **High** | New project started, environment change | **Write-through** (session start) | `memory()` call within first 3 turns |
| **Routine** | Session observations, task outcomes | **Write-back** (session end) | Daily log + heartbeat curation |
| **Archive** | Completed work, historical | **Batch** (weekly) | Demotion cron → GBrain |

## 9. Implementation Plan (Phased)

### Phase A: Configuration (Immediate)
- [ ] Increase memory budgets in config.yaml
- [ ] Create tracker infrastructure files
- [ ] Document conflict-log format

### Phase B: Automation (Days 1-3)
- [ ] Build weekly demotion cron script
- [ ] Build promotion tracker (observation counter)
- [ ] Wire demotion cron to Hermes scheduler
- [ ] Test demotion with dummy stale entries

### Phase C: Integration (Days 4-7)
- [ ] Add promotion logic to session-start routine
- [ ] Build conflict detection into memory writes
- [ ] Add importance scoring to eviction
- [ ] End-to-end test: stale entry → demotion → GBrain → verify

### Phase D: Monitoring (Ongoing)
- [ ] Weekly health report (tier sizes, promotion/demotion counts)
- [ ] Budget utilization tracking
- [ ] Conflict resolution audit

## 10. Metrics & Verification

| Metric | Target | Measurement |
|--------|--------|-------------|
| WARM budget utilization | 60-85% | `len(MEMORY.md)` / `memory_char_limit` |
| Stale entry rate | <10% of WARM entries | Weekly demotion scan |
| Promotion accuracy | >90% promoted facts still relevant | 30-day lookback |
| Conflict resolution latency | <1 session | Conflict log review |
| Crashed-session recovery | No HOT/WARM loss | Write-through on critical facts |

## 11. Open Questions

1. Should promotion counters decay over time? (e.g., count halves every 30 days)
2. Should GBrain demotion be automatic or require user confirmation?
3. How to handle multi-profile memory (work vs personal) — separate tier systems or shared COLD?
4. Should skills auto-promote from session patterns, or always require explicit creation?

## References
- Original Layer 6 spec: [[agent-layered-architecture-spec]]
- Hermes memory tool: `memory` (add/replace/remove/operations)
- Hermes skill system: `skill_manage` / `skill_view`
- GBrain: `gbrain think` / `gbrain put` / `gbrain link`
