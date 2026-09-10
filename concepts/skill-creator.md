---
date: 2026-07-19
type: concept
title: Skill Creator
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- financial-analysis
sources:
- hermes://skill/skill-creator
description: Create new skills, modify and improve existing skills, and measure skill
  performance. Use when users want to create a skill from scratch, edit, or optimize
  an existing skill, run evals to test a skill, benchmark skill performance with variance
  analysis, or optimize a skill's description for better triggering accuracy.
---

# Skill Creator

> Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

## Overview

- **Communicating with the user** — The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. If you haven't heard (and how could you, it's only very recently that it started), there's a trend now where the power of Claude is inspiring plumbers to open up their terminals, parents and grandparents to google "how to install npm". On the other hand, the bulk of users are probably fairly computer-literate.
- **Report structure** — ALWAYS use this exact template:
- **Commit message format** — **Example 1:** Input: Added user authentication with JWT tokens Output: feat(auth): implement JWT-based authentication

## Further detail

### Running and evaluating test cases

This section is one continuous sequence — don't stop partway through. Do NOT use `/skill-test` or any other testing skill.

### Improving the skill

This is the heart of the loop. You've run the test cases, the user has reviewed the results, and now you need to make the skill better based on their feedback.

### Advanced: Blind comparison

For situations where you want a more rigorous comparison between two versions of a skill (e.g., the user asks "is the new version actually better?"), there's a blind comparison system. Read `agents/comparator.md` and `agents/analyzer.md` for the details. The basic idea is: give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/skill-creator/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
