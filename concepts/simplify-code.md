---
date: 2026-07-19
type: concept
title: Simplify Code
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- code-review
- cleanup
- refactor
- delegation
- subagent
- parallel
- simplify
- software-development
sources:
- hermes://skill/simplify-code
description: Parallel 4-agent cleanup of recent code changes.
---

# Simplify Code

> Parallel 4-agent cleanup of recent code changes.

## Overview

- **When to Use** — Trigger this skill when the user says any of:
- **Pitfalls** — - **Don't fan out wider than 4.** More reviewers means more cost and more conflicting suggestions to reconcile, not better coverage. The four categories cover the space. - **Give the WHOLE diff to each reviewer.** Splitting the diff across reviewers defeats the design — cross-file duplication and N+1s only show up with the full picture. - **Reviewers search, they don't guess.** A reuse finding with no pointer to the existing utility ("there's probably a helper for this") is noise. Require `file:line` evidence; drop findings that lack it. - **Apply ≠ rewrite.** This is cleanup of the user's rec
- **Related** — If your install has the `subagent-driven-development` skill (optional), it covers the complementary case: parallel review *during* implementation, per task. This skill is the standalone *after-the-fact* cleanup pass. Use `requesting-code-review` for the pre-commit security/quality gate — that's the bug hunt; this is the cleanup.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/simplify-code/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
