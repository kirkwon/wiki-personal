---
date: 2026-07-19
type: concept
title: Critical Review
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- review
- critique
- methodology
- design-review
- feedback
- quality
- software-development
sources:
- hermes://skill/critical-review
description: 'Structured critical feedback on plans, frameworks, designs, and methodologies.
  Assesses for: too simple, too complex, gaps, redundancies, ordering issues, assumptions,
  blind spots. Outputs actionable revision suggestions.'
---

# Critical Review

> Structured critical feedback on plans, frameworks, designs, and methodologies. Assesses for: too simple, too complex, gaps, redundancies, ordering issues, assumptions, blind spots. Outputs actionable revision suggestions.

## Overview

- **When to Use** — Trigger this skill when: - A plan, framework, or methodology has been drafted and needs review before use - Someone asks "What do you think of this approach?" - You're about to invest significant resources in an idea and want to stress-test it first - You want to identify blind spots, missing pieces, or unnecessary complexity - A design decision needs adversarial review
- **The Seven Review Dimensions** — ---
- **Phase 0: Policy Selection (Pre-review)** — *This phase is optional when running standalone. The meta-critic (Level 1) handles this automatically.*

## Further detail

### Phase 1: Understand the Artifact

Before critiquing, restate what you're reviewing in your own words. This ensures you understand it AND surfaces any initial confusion:

### Phase 3: Frame & Improve

After identifying issues, apply the **reframing pattern** (from Fabric's `create_better_frame`) to each critical flaw:

### BINEVAL Integration: Binary Question Templates (Optional Precision Mode)

For low-variance, high-debuggability reviews, decompose each dimension into **atomic binary questions** (BINEVAL method — [Cho et al. 2026](https://arxiv.org/abs/2606.27226)). Instead of a subjective 0-10 score per dimension, each dimension becomes 3-5 yes/no checks that aggregate into a calibrated pass-rate.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/critical-review/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
