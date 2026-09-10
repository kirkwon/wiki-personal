---
date: 2026-07-19
type: concept
title: Grill Me
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- socratic
- planning
- stress-test
- design-review
- decision-making
- software-development
sources:
- hermes://skill/grill-me
description: Relentless Socratic interview to stress-test a plan, design, or decision
  before committing to implementation. Use when the user says 'grill me', wants to
  pressure-test a plan, or before any high-stakes build. Merges mattpocock/grill-me
  + grilling for Hermes.
---

# Grill Me

> Relentless Socratic interview to stress-test a plan, design, or decision before committing to implementation. Use when the user says 'grill me', wants to pressure-test a plan, or before any high-stakes build. Merges mattpocock/grill-me + grilling for Hermes.

## Overview

- **When to Use** — - User says "grill me", "stress-test this", "poke holes in this" - Before building anything non-trivial (features, architecture decisions, refactors) - User presents a plan/design and wants to validate it - Before committing to a direction when multiple options exist - Part of the **Sieve phase** in Explore→Sieve→Exploit
- **Core Protocol** — Interview the user relentlessly about every aspect of the plan until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
- **Rules of Engagement** — 1. **One question at a time.** Asking multiple questions simultaneously is bewildering. Wait for feedback on each before continuing.

## Further detail

### Integration with Hermes Workflow

1. **Explore → Grill → Exploit**: Use grilling as the gate between exploration and execution 2. **Post-grill output**: Summarize into a `plan` skill output or `writing-plans` SKILL.md 3. **Kanban tasks**: Each resolved decision becomes a trackable task 4. **For delegated work**: Pass the validated decisions to subagents as explicit constraints

### BINEVAL Binary Grilling Mode (Optional Precision Mode)

For high-stakes go/no-go decisions, complement the open-ended Socratic interview with **binary grilling** — atomic yes/no questions that produce a defensible, traceable verdict (BINEVAL method — [Cho et al. 2026](https://arxiv.org/abs/2606.27226)).

### Pitfalls

- **Don't grill trivia.** Skip questions with obvious answers or that don't affect the design. - **Don't grill forever.** 5-15 questions is typical. If you're past 20, the plan needs decomposition, not more questions. - **Don't forget the recommendation.** Pure interrogation without recommendations is annoying, not helpful. - **Don't skip the codebase.** If you can read the answer from a file, do it — don't waste the user's time.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/grill-me/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
