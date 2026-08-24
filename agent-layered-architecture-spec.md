---
title: "Agent Layered Architecture Spec"
date: 2026-06-27
source: research-citation
tags: [agent-architecture, memory-hierarchy, structured-execution, knowledge-management]
status: ingested
created: 2026-06-27
updated: 2026-06-27
---

# Agent Layered Architecture Spec

## Layer 6: Knowledge Integration (Memory Management)

The final layer dictates how the agent organizes learned information across a **4-Tier Memory Hierarchy** to maximize context efficiency [18, 19]:

- **Tier 1 (HOT):** Crucial, active context (~500 chars) always loaded in memory — identity, active anchors, current state [18].
- **Tier 2 (WARM):** Session-specific context (~2,000 chars) loaded on start — active projects, key decisions [18].
- **Tier 3 (COOL):** Procedural knowledge and tool patterns, loaded on demand [18].
- **Tier 4 (COLD):** Historical decisions and deep domain knowledge stored in the "GBrain" knowledge graph, searched only as needed [18].

### Operational Rules
- **Promotion:** Facts are promoted to higher tiers when repeated across sessions.
- **Demotion:** Facts are demoted/archived when projects conclude or grow stale [20].
- **Strict structured report-backs** after any execution: goals, duration, status, and verification results [18].

## References
- [18] — Source citation for structured execution reporting and memory hierarchy tiers.
- [19] — Source citation for context efficiency rationale.
- [20] — Source citation for promotion/demotion rules.

## Notes
- Fragment ingested from a larger 6-layer architecture document. Only Layer 6 was captured.
- Aligns with existing Hermes memory model (MEMORY.md = HOT/WARM, skills = COOL, GBrain = COLD).
