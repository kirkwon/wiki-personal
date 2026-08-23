---
date: 2026-07-15
type: concept
title: Documentation Master
created: 2026-07-15
updated: 2026-07-15
tags: [domain-master, documentation, knowledge-management, architecture]
---

# Documentation Master

## Summary

Documentation Master is a **domain-specialized cognitive layer** within the Hermes agent architecture responsible for curating, organizing, and maintaining all technical and process documentation across the ecosystem.

## Purpose

Documentation Master operates as a semi-autonomous subsystem that:
- Tracks documentation freshness and identifies stale content
- Generates documentation from code comments and README files
- Detects broken links and missing documentation
- Maintains a living documentation corpus that feeds into the Awareness stage

## Responsibilities

| Responsibility | Mechanism | Integration Point |
|:--------------|:----------|:----------------|
| Documentation Audits | Git README ingestion, API doc scraping | → Awareness |
| Freshness Tracking | Last updated date monitoring | → Learning |
| Auto-Repair | Link rot detection + regeneration | → Interaction |
| Source Integration | Browser capture → structured markdown | → Exploration |

## Health Signals

- **coverage_score**: Percentage of systems with documentation
- **stale_threshold**: Days before content considered stale
- **link_health**: Percentage of working external links
- **doc_debt**: Undocumented systems requiring attention

## Implementation Status

**Status:** Proposed  
**Dependencies:** read-the-damn-docs skill, wiki-personal, gbrain  
**Next Steps:** 
- Create cron job for weekly doc audits
- Implement link checker script
- Build documentation quality scorer

## Related Pages

- [[hermes-agent-stack]] — Core architecture context
- [[knowledge-master]] — Sibling domain master for knowledge lifecycle
- [[decision-master]] — Decision governance layer
- [[productivity-master]] — Workflow optimization layer
- [[read-the-damn-docs]] — Documentation retrieval skill