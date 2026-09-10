---
date: 2026-08-02
type: concept
title: Entity Normalization Pipeline
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- data-engineering
- normalization
- entity-resolution
- etl
- software-development
sources:
- hermes://skill/entity-normalization-pipeline
description: Normalize extracted data into canonical entities.
---

# Entity Normalization Pipeline

> Normalize extracted data into canonical entities.

## Overview

- **When to Use** — - You have extracted raw signals from multiple sources needing consolidation - Need to merge duplicate records representing the same real-world entity - Building a knowledge base, CRM, or entity graph from disparate data sources - Preparing cleaned, structured data for analysis, machine learning, or downstream applications - Dealing with data that has inconsistent naming, formatting, or representation across sources
- **Core Principles** — - **Entity Identity First**: Focus on determining when two records represent the same entity before merging - **Evidence Preservation**: Never lose provenance; maintain detailed source tracking for all merged data - **Temporal Awareness**: Handle time-varying attributes correctly (e.g., first_seen/last_seen, not averages) - **Merge Rule Transparency**: Explicitly define and document how different field types are combined - **Incremental Processing Design**: Build for resumability and scalability from the start
- **Output Structure** — Normalized entities follow your defined schema (e.g., JSON Schema) with: - Canonical IDs (source-independent, stable identifiers) - Consolidated attributes per entity (earliest first_seen, latest last_seen, etc.) - Preserved evidence trails showing provenance for every data point - Properly typed and validated fields per schema requirements

## Further detail

### Pitfalls to Avoid

- ❌ **Losing Evidence During Merge**: Always preserve source traces; this is non-negotiable for auditability and confidence scoring - ❌ **Over-Aggressive Deduplication**: Merging distinct entities (e.g., two different "John Smith" at different addresses) creates false positives - ❌ **Ignoring Temporal Dimensions**: Treating time-variant attributes like address or phone number as static creates inaccuracies - ❌ **Hard-Coded Merge Rules**: Make rules configurable per entity type and use case; what works for vendors may not work for locations - ❌ **No Validation Feedback**: Always report what was

### Verification Checklist

Before declaring normalization complete: - [ ] Spot-check 5-10 merged entities against source records - [ ] Verify ID uniqueness across all entity outputs - [ ] Confirm evidence traces correctly to source documents - [ ] Validate temporal fields (first_seen ≤ last_seen, reasonable ranges) - [ ] Run JSON Schema validation on all output files - [ ] Test downstream consumers can successfully ingest the output - [ ] Review metrics: merge rate, yield, evidence retention within expected bounds - [ ] Ensure no PII or sensitive data leaked inappropriately per security policy

### Related Skills

- `/data-ingestion-normalization` - For deduplication and normalization during data ingestion - `/batch-entity-web-scraper` - For extracting structured entities from web sources - `/grammar-induction-corpora` - For linguistic normalization patterns in text data - `/research-pipeline-builder` - For end-to-end research data processing workflows - `/feature-store-patterns` - For serving normalized entities to ML models

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/data-engineering/entity-normalization-pipeline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
