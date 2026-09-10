---
date: 2026-07-19
type: concept
title: Task Difficulty Guideline
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- decision
sources:
- hermes://skill/task-difficulty-guideline
description: Handle simple tasks autonomously; ask for input on complex or uncertain
  tasks.
---

# Task Difficulty Guideline

> Handle simple tasks autonomously; ask for input on complex or uncertain tasks.

## Overview

- **When to Use** — - You receive a request that could range from a quick fact lookup to a multi‑step project. - You want to avoid over‑asking on trivial items while ensuring you do not proceed blindly on unclear or high‑effort work. - The user has expressed a preference for minimal interruptions on routine work.
- **Prerequisites** — - None. This is a behavioral guideline; no external tools or credentials are required.
- **How to Run** — Apply the guideline internally before committing to any course of action. No explicit invocation is needed; it shapes your decision‑making process.

## Further detail

### Quick Reference

- **Simple task**: clear goal, known procedure, low risk, can be completed with existing tools and knowledge. - **Complex/task**: vague goal, missing information, requires novel synthesis, involves external side‑effects, or the user has previously indicated uncertainty.

### Procedure

1. **Assess Task Complexity** - If the request includes a clear, actionable goal (e.g., “fetch the price of AAPL”, “summarize this file”, “run this script”) and you have the necessary tools and context → treat as **simple**. - If the request is open‑ended, asks for opinions, requires creative synthesis, or you lack key data (e.g., “What should I do about X?”, “How can I improve Y?”) → treat as **complex**.

### Pitfalls

- **Over‑automation**: Do not treat a task as simple merely because it sounds short; verify that you have all required inputs and understand the expected output. - **Under‑asking**: Avoid proceeding on assumptions when the user’s intent could vary (e.g., “fix the cron job” could mean diagnose, patch, or replace). Ask for the desired outcome. - **Annoyance from over‑clarifying**: For truly trivial tasks (e.g., “what is 2+2?”), a clarification request would be unnecessary and irritating. Use your judgment: if the answer is immediately obvious from your knowledge and requires no tool use, answer

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/decision/task-difficulty-guideline/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
