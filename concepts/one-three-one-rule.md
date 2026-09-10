---
date: 2026-07-19
type: concept
title: One Three One Rule
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- communication
- decision-making
- proposals
- trade-offs
sources:
- hermes://skill/one-three-one-rule
description: '1-3-1 decision briefs: problem, three options, one pick.'
---

# One Three One Rule

> 1-3-1 decision briefs: problem, three options, one pick.

## Overview

- **When to Use** — - The user explicitly asks for a "1-3-1" response. - The user says "give me options" or "what are my choices" for a technical decision. - A task has multiple viable approaches with meaningful trade-offs (architecture, tooling, migration strategy). - The user needs a proposal they can forward to a team or stakeholder.
- **Procedure** — 1. **Problem** (one sentence) - State the core decision or desired outcome in a single concise sentence. - Focus on the *what*, not the *how* — no implementation details, tool names, or specific technologies. - Keep it tight. If you need "and", you're describing two problems.
- **Verification** — - Response has exactly one Problem sentence. - Response has exactly three Options (A, B, C) with pros and cons for each. - Response has a single Recommendation that picks one option with reasoning. - Definition of Done and Implementation Plan align with the recommended option. - If the user selects a different option, Recommendation, DoD, and Implementation Plan update accordingly.

## Further detail

### Example

User: "Give me a 1-3-1 for adding retry logic to our API client."

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/communication/one-three-one-rule/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
