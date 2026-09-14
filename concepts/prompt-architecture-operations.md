---
type: concept
title: Prompt Architecture Operations
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Prompt Architecture Operations
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- prompt-engineering
- agent-design
- system-prompt
- architecture
- guardrails
- routing
- control-surface
- cross-domain
- software-development
sources:
- hermes://skill/prompt-architecture-operations
description: Operational conditions and patterns for constructing long-running agent
  system prompts. Derived from structural teardown of Claude Fable's 1,597-line prompt
  + transcendental analysis. Use when building or auditing agent/skill system prompts,
  routing logic, guardrails, or tool contracts.
---

# Prompt Architecture Operations

> Operational conditions and patterns for constructing long-running agent system prompts. Derived from structural teardown of Claude Fable's 1,597-line prompt + transcendental analysis. Use when building or auditing agent/skill system prompts, routing logic, guardrails, or tool contracts.

## Overview

- **When to Use** — Trigger this skill when: - Building or revising a system prompt, SOUL.md, or multi-surface agent contract - Designing tool contracts, routing logic, or output-modality rules for an agent - Auditing an existing prompt for structural weaknesses - Building skills with guardrails, thresholds, or verification hooks - Designing any control surface that governs a long-running agent (>5 turns)
- **Part I: The Six Conditions (Transcendental Substrate Facts)** — Each condition is an **a priori property of autoregressive generation** that makes a corresponding pattern necessary. The pattern is irrational *unless* the condition holds. Understanding the condition tells you when to apply the pattern and when to skip it.
- **Part II: The Ten Patterns (Operational Construction Guide)** — Each pattern: **what it is → which condition forces it → how to implement → worked example (or conjecture where none exists).**

## Further detail

### Part III: The Meta-Lesson

**Design the prompt as a map of the model's known deficits, not as a description of desired behavior.**

### Part IV: Conjectures (Patterns Without Worked Examples)

These are hypothesized corrections for gaps the Fable teardown reveals but does not demonstrate. Each is marked as conjecture and includes an implementation direction.

### Part V: Implementation Checklist

When building or auditing an agent's system prompt, run through this checklist:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/prompt-architecture-operations/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
