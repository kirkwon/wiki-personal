---
type: concept
title: Knowledge Master
created: 2026-07-15
updated: 2026-07-15
tags: [domain-master, knowledge-management, gbrain, architecture]
---

# Knowledge Master

## Summary

Knowledge Master is a **domain-specialized cognitive layer** within the Hermes agent architecture responsible for governing the complete knowledge lifecycle: ingestion, synthesis, validation, and retirement.

## Purpose

Knowledge Master operates as a semi-autonomous subsystem that:
- Oversees gbrain indexing and quality assurance
- Manages wiki/gbrain synchronization
- Enforces knowledge freshness policies
- Coordinates cross-domain knowledge synthesis

## Responsibilities

| Responsibility | Mechanism | Integration Point |
|:--------------|:----------|:----------------|
| Ingestion Oversight | Repo ingestion, web scraping pipelines | → Exploration |
| Synthesis Coordination | GBrain dream cycle, concept formation | → Interpretation |
| Quality Control | Orphan detection, connectivity scoring | → Learning |
| Freshness Management | Source currency tracking | → Awareness |

## Knowledge Lifecycle

```
INGESTION → PROCESSING → STORAGE → RETRIEVAL → SYNTHESIS → VALIDATION → RETIREMENT
    ↑                                                                    ↓
    └────────────────────── KNOWLEDGE MASTER LOOP ─────────────────────────┘
```

### Ingestion Sub-Loop
- Sources identified via Exploration stage
- Raw content captured (web, repos, PDFs)
- Initial quality filtering applied

### Processing Sub-Loop
- Entity extraction from raw content
- Concept clustering and disambiguation
- Link resolution and connectivity optimization

### Storage & Retrieval
- GBraiin semantic indexing with text-embedding-3-large
- Tiered storage (HOT/WARM/COOL/COLD memory)
- Query routing based on relevance and freshness

### Validation Sub-Loop
- Orphan page detection
- Broken link identification
- Knowledge graph health scoring
- Source credibility weighting

## Health Signals

| Metric | Description | Threshold |
|:-------|:------------|:----------|
| brain_size | Total indexed pages | > 20,000 ideal |
| orphan_ratio | Undiscovered pages % | < 10% target |
| connectivity_score | Link density quality | > 90% target |
| source_freshness | Days since last ingest | < 30 days |
| concept_coverage | Domains represented | Track by category |

## Integration with Memory Tiering

Knowledge Master actively manages the 4-tier memory system:

| Tier | Size | Content | Knowledge Master Role |
|:-----|:-----|:--------|:--------------------|
| HOT | ~500 chars | Session context | Real-time triage |
| WARM | ~2,000 chars | MEMORY.md | Immediate history |
| COOL | Unlimited | Skills | On-demand activation |
| COLD | ~20,000 pages | GBraiin/wiki | Deep retrieval |

### Self-Evolving Memory Harness

Builds on the concept from the FinAcumen paper (arXiv:2606.17642) and Self-Harness paradigm:

- **Usage Analytics**: Track what's accessed frequently vs. never
- **Adaptive Boundaries**: Adjust tier sizes based on working set patterns
- **Value Scoring**: Content read but never leads to success → demote
- **RL Policy**: Tier transitions learned from task success signals

## Related Pages

- [[hermes-agent-stack]] — Core architecture context
- [[documentation-master]] — Documentation layer
- [[decision-master]] — Decision layer
- [[productivity-master]] — Workflow layer
- [[gbrain]] — Knowledge base system
- [[memory-tiering]] — 4-tier memory architecture
- [[self-harness-paradigm]] — Three-stage improvement loop
- [[knowledge-metabolism]] — Knowledge health checks