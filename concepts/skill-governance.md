---
date: 2026-07-19
type: concept
title: Skill Governance
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/skill-governance
description: Govern the skill library with meta-masters, scoring, A/B testing, and
  archive workflows. Never delete — consolidate with evidence.
---

# Skill Governance

> Govern the skill library with meta-masters, scoring, A/B testing, and archive workflows. Never delete — consolidate with evidence.

## Overview

- **Core Principles** — 1. **Never delete. Archive.** `mv` to `.archive/`, never `rm -rf`. Deletion loses knowledge; archive preserves it with an `archived_at` timestamp.
- **The Meta-Master Pattern** — Every meta-master follows this structure:
- **Scoring System** — | Axis | Weight | 10 | 0 | |---|---|---|---| | Recency | 40% | Used this week | Not used in 12+ months | | Frequency | 35% | 20+ uses in 3 months | 0 uses | | Quality | 25% | Always delivers, reliable | Broken, unreliable, never used |

## Further detail

### A/B Test Protocol

When two skills overlap:

### Active Meta-Masters

| Meta-Master | Phase | Created | Sub-Skills | |---|---|---|---| | `software-development-master` | implement + ship | 2026-07-03 | 38 | | `knowledge-master` | discover + assimilate | 2026-07-01 | 38 | | `finance-master` | analyze + model | 2026-07-01 | 10 | | `productivity-master` | operate | 2026-07-01 | 24 | | `creativity-master` | generate | 2026-07-01 | 15 | | `learning-master` | retain | 2026-07-01 | 14 |

### Phase Alignment — Skill Classification for Delegation

Every sub-skill in a meta-master should be classified by **phase** to determine delegation discipline. This is a governance concern — it prevents over-constraining exploration or under-specifying execution.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/skill-governance/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
