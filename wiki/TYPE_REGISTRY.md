---
type: registry
title: OKF Type Registry — wiki-personal
created: 2026-06-16
updated: 2026-06-16
description: "Controlled vocabulary for the type: field across all wiki-personal concepts, entities, sources, and queries."
tags: [okf, taxonomy, schema, knowledge-management]
---

# OKF Type Registry

This registry defines the controlled vocabulary for the `type:` field in every concept document. Following OKF v0.1, `type` is the only required frontmatter field — but its values here are curated, not arbitrary.

## Taxonomy

### Content Types

| Type | Count | Description | Valid In |
|------|-------|-------------|----------|
| `concept` | 1,617 | A mental model, principle, idea, or framework. The atomic unit of knowledge. | concepts/ |
| `entity` | 1,424 | A person, place, thing, tool, or named reference. | entities/ |
| `source` | 391 | A book, article, paper, or other external reference. | sources/ |
| `comparison` | 10 | A structured comparison between two or more things. | comparisons/ |
| `synthesis` | 7 | A synthesized review across multiple time periods or topics. | synthesis/ |
| `query` | 20 | A saved research query or question with results. | queries/ |

### Meta Types

| Type | Count | Description | Valid In |
|------|-------|-------------|----------|
| `framework` | 14 | A structured method or system (subtype of concept/entity). | concepts/ or entities/ |
| `note` | 48 | A raw note, analysis, or working document. | concepts/ |
| `summary` | 17 | A condensed summary of a source or topic. | concepts/ or sources/ |
| `paper` | 1 | An academic paper reference. | concepts/ |
| `analysis` | 1 | A data analysis or pipeline result. | concepts/ |
| `problem` | 2 | A known problem or challenge in a domain. | concepts/ |
| `solution` | 1 | A known solution to a problem. | concepts/ |
| `overview` | 1 | A top-level overview of a domain. | root |
| `index` | 1 | A directory index page. | concepts/ |
| `permanent-question` | 6 | A permanent research question. | questions/ |

### Deprecated / Removed

| Old Type | Replaced By | Reason |
|----------|-------------|--------|
| `stub` | `concept` | Consolidation — stubs are concepts without body text |
| `concept-stub` | `concept` | Same as above |
| `question-index` | `index` | Standardized naming |

## Validation Rules

1. **Every page MUST have a `type:` field** — this is the OKF requirement
2. **Types MUST be one of the registered values above** — no ad-hoc types
3. **Type SHOULD match the directory** — e.g., files in `concepts/` should be `type: concept`
   - Exception: `entities/` may contain `framework`, `note`, `source`, `comparison`
   - Exception: `concepts/` may contain `note`, `summary`, `analysis`, `problem`, `solution`
4. **New types MUST be added to this registry** before first use
5. **Removed types MUST be documented here** with replacement

## OKF Frontmatter Fields

Per OKF v0.1 spec, the recommended frontmatter fields are:

| Field | Required | Description |
|-------|----------|-------------|
| `type` | **YES** | One of the registered types above |
| `title` | Recommended | Human-readable display name |
| `description` | Recommended | Single-sentence summary (max 200 chars) |
| `resource` | Optional | URI to the underlying asset |
| `tags` | Optional | List of cross-cutting category tags |
| `timestamp` | Optional | ISO 8601 last-modified datetime |
| `created` | Optional | ISO 8601 creation date |
| `updated` | Optional | ISO 8601 last-updated date |

### wiki-personal Extensions

These fields are wiki-personal additions beyond the OKF spec:

| Field | Used In | Purpose |
|-------|---------|---------|
| `sources` | concepts, entities | List of source references |
| `related` | concepts, entities | List of related concept links |
| `confidence` | concepts | Confidence level in the content |
| `status` | concepts | Filing status (e.g., `filed`) |
| `author` | sources | Source author |
| `year` | sources | Publication year |

## Type Distribution

```
concept           ████████████████████████████████ 1617
entity            ██████████████████████████████   1424
source            ████████                        391
note              █                                48
query                                               20
summary                                             17
framework                                           14
comparison                                          10
permanent-question                                   6
analysis                                             1
index                                                1
paper                                                1
problem                                              2
solution                                             1
synthesis                                            7
overview                                             1
```
