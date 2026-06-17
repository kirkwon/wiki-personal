---
type: concept
title: Memory Tiering System
description: "Memory Tiering System
What: A 4-tier memory hierarchy that keeps the agent's hot context under ~500 chars by promoting/demoting facts across memory tiers based on recency and relevance."
created: 2026-06-12
updated: 2026-06-13
tags: [concept, memory, tiering, context, gbrain, optimization, knowledge management]
related: ["information-architecture", "knowledge-management", "hybrid-memory-systems", "headroom-integration", "methodology-loop"]
sources: [memory-tiering.md]
---

# Memory Tiering System
**What:** A 4-tier memory hierarchy that keeps the agent's hot context under ~500 chars by promoting/demoting facts across memory tiers based on recency and relevance.
**Why:** Before tiering, hot memory was 2,046 chars (88% of limit) with 8 entries — most of which weren't needed every turn. After tiering: 293 chars (13%) with 2 entries. The agent has room to think instead of reading memory.
**How:** The `memory-tiering` Hermes skill defines the rules. A background file (`MEMORY.md`) acts as the warm tier between hot memory and GBrain.

## The Four Tiers
``` 
T1: HOT memory() tool ~500 chars ALWAYS loaded, every turn
T2: WARM MEMORY.md ~2,000 chars Loaded on session start
T3: COOL Hermes skills unlimited Loaded on demand by task match
T4: COLD GBrain / wiki ~19K pages Searched when needed
```
Every turn, the system prompt includes T1 + T2. T3 loads when a skill matches the task. T4 is searched only when the agent needs deep context.

## What Goes Where
### Tier 1: HOT — memory() tool
**Capacity:** ~500 chars target, 2,200 hard max
**Persistence:** Across all sessions, automatically injected
| Priority | Content | Example |
|---|---|---|
| 1 | Identity | Bayesian Rogue, Kirk Won |
| 2 | Preferences | concrete plans, SHA256 verify, Telegram docs, no hand-holding |
| 3 | Active anchors | port :8787, loop-engine scripts, current project context |
**Remove from hot when:** project finishes, preference stabilizes into USER.md, fact not referenced for 2+ sessions.

### Tier 2: WARM — MEMORY.md (file on disk)
**Capacity:** ~2,000 chars
**Persistence:** Git-tracked, loaded on session start via AGENTS.md
| Section | Content |
|---|---|
| Recent Work | Last 1-2 sessions distilled to 3-4 lines each |
| Cross-Session Facts | Portfolio dashboard, GBrain status, stable decisions |
**Archive to GBrain when:** session summary >2 weeks old, project complete + 2 weeks idle.

### Tier 3: COOL — Hermes Skills
**Capacity:** Unlimited (loaded on demand)
**Management:** Created via `skill_manage`, patched when workflows change, deleted when stale.

### Tier 4: COLD — GBrain + Wiki
**Capacity:** ~19K+ pages
**Access:** Searched on demand via `gbrain query` / `gbrain think`

## Memory Lifecycle
### Promote (move up a tier)
| Trigger | Action |
|---|---|
| User says "remember this" | Promote straight to hot |
| User repeats a fact twice | Promote from warm to hot |
| Skill invoked 3+ times in one session | Keep in warm for rest of session |
| Decision affects current work | Pull from GBrain to warm |
| Fact referenced across sessions | Promote to warm |

### Demote (move down a tier)
| Trigger | Action |
|---|---|
| Project finishes | Hot → warm, then GBrain after 2 weeks |
| Fact not referenced for 2 sessions | Hot → warm |
| Session summary >2 weeks old | Warm → GBrain |
| Skill not used in 30 days | Consider deleting |

### Archive (warm → cold)
Done by the agent when MEMORY.md exceeds ~2,200 chars or during weekly heartbeat:
1. Move stale session summaries to GBrain
2. Merge overlapping entries
3. Remove task-completion details (in daily logs)
4. If still over limit, move least-important entries to GBrain

## Before/After: Real Application
### Before (June 12, 2026 — 8 entries, 2,046 chars, 88% full)
``` 
Portfolio CLI: portfolio. Dash :5001, launchd auto.
Causal AI (2026-06-03): risk/portfolio focus...
User: concrete plans, SHA256 verify...
Memory: references/memory-architecture.md...
Memory consolidated to 27%.
A/B test protocol...
Created /last30days Hermes skill...
Loop engineering 2026-06-12: 4-phase implementation...
Headroom integration 2026-06-12: installed v0.25.0...
```
### After (June 12, 2026 — 2 entries, 293 chars, 13% full)
``` 
User: Kirk Won. Bayesian Rogue.
Work: Explore→Sieve→Exploit...
Active: Headroom proxy :8787, loop-engine scripts, memory-tiering...
```
**Difference:** 1,753 chars freed (74% reduction). The removed entries now live in MEMORY.md (warm tier) or GBrain (cold tier) — not lost, just tiered appropriately.

## Files
| File | Tier | Purpose |
|---|---|---|
| `memory()` tool entries | T1: Hot | Always-injected identity + anchors |
| `~/.hermes/MEMORY.md` | T2: Warm | Session summaries + stable facts |
| `~/.hermes/skills/research/memory-tiering/SKILL.md` | T3: Cool | Tiering rules (this skill) |
| `~/.hermes/skills/research/hybrid-memory-systems/SKILL.md` | T3: Cool | 4-layer architecture |
| `~/wiki-personal/wiki/concepts/` | T4: Cold | Full knowledge base |
| `~/.gbrain/` | T4: Cold | Vector searchable graph |

## Related Concepts
- [[hybrid-memory-systems]] — Architecture of the 4-layer system (related skill)
- [[headroom-integration]] — Context compression (complementary: Headroom compresses tool output, tiering compresses memory)
- [[methodology-loop]] — Meta-loop for improving processes (tiering is a process improvement)
- [[information-architecture]] — Organizing information for efficient access
- [[knowledge-management]] — Strategies for managing knowledge in a system

## References
- `memory-tiering` Hermes skill — operational rules for promote/demote/archive
- `hybrid-memory-systems` Hermes skill — architecture of the 4-layer system
- `~/.hermes/MEMORY.md` — warm tier file (created 2026-06-12)