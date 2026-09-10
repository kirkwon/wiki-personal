---
date: 2026-07-19
type: concept
title: Test Driven Development
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- testing
- tdd
- development
- quality
- red-green-refactor
- software-development
sources:
- hermes://skill/test-driven-development
description: 'TDD: enforce RED-GREEN-REFACTOR, tests before code.'
---

# Test Driven Development

> TDD: enforce RED-GREEN-REFACTOR, tests before code.

## Overview

- **Overview** — Write the test first. Watch it fail. Write minimal code to pass.
- **When to Use** — **Always:** - New features - Bug fixes - Refactoring - Behavior changes
- **The Iron Law** — Write code before the test? Delete it. Start over.

## Further detail

### Avoid Horizontal Slices

Do **not** write all tests first and then all implementation. That is horizontal slicing: RED becomes "write a pile of imagined tests" and GREEN becomes "make the pile pass." It produces brittle tests because the tests are designed before the implementation has taught you what behavior and interface actually matter.

### Why Order Matters

**"I'll write tests after to verify it works"**

### Common Rationalizations

| Excuse | Reality | |--------|---------| | "Too simple to test" | Simple code breaks. Test takes 30 seconds. | | "I'll test after" | Tests passing immediately prove nothing. | | "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" | | "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. | | "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. | | "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. | | "Need to explore first" | Fi

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/test-driven-development/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
