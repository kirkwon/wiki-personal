---
date: 2026-07-19
type: concept
title: Meta Critic
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- meta
- critique
- rl
- policy
- learning
- calibration
- review
- feedback
- software-development
sources:
- hermes://skill/meta-critic
description: 'RL-inspired meta-layer for critique: observes artifact type, selects
  optimal critique dimensions/patterns via learned policy, executes critique, measures
  reward, and updates the policy through calibration. Sits above critical-review and
  Fabric patterns as the policy layer.'
---

# Meta Critic

> RL-inspired meta-layer for critique: observes artifact type, selects optimal critique dimensions/patterns via learned policy, executes critique, measures reward, and updates the policy through calibration. Sits above critical-review and Fabric patterns as the policy layer.

## Overview

- **What This Is** — The meta-critic is a **reinforcement learning-inspired layer** that sits above individual critique tools and patterns. It doesn't critique artifacts directly — it decides *how* to critique them, then learns from the outcomes to make better selections next time.
- **When to Use** — - **Before** running a critique, to decide which dimensions matter most - When you want to **learn** which critique approach works best over time - When the artifact type is **ambiguous** and needs classification first - When you want an **exploration/exploitation balance** (try new critique patterns vs use proven ones) - When you're reviewing a **portfolio of decisions** and want systematic improvement
- **Mode 3: 37% Quick Model (Optimal Stopping for Complex Decisions)** — For one-shot complex artifacts where the RL loop has no history, the meta-critic can use **optimal stopping** — the 37% rule from the secretary problem — to decide when to stop analyzing and start acting.

## Further detail

### Running the Abductive Reasoner (Concrete Procedure)

This is the executable implementation of the abductive logic. Run this after the induced model is built (from 37% or full critique).

### Exploration vs Exploitation (Gittins Index)

The meta-critic's exploration policy uses a **Gittins Index** formulation:

### Example Session

**User:** "Review this plan to build a causal hedge agent"

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/meta-critic/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
