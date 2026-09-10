---
date: 2026-07-19
type: concept
title: Improve Writing
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- creative
sources:
- hermes://skill/improve-writing
description: Enhance writing clarity, flow, and voice — fix grammar, adjust tone,
  strengthen arguments, and remove AI-isms (complements `humanizer` skill).
---

# Improve Writing

> Enhance writing clarity, flow, and voice — fix grammar, adjust tone, strengthen arguments, and remove AI-isms (complements `humanizer` skill).

## Overview

- **Steps** — 1. Analyze original text for grammar, flow, tone, and clarity issues 2. Preserve the author's original voice and intent 3. Check sentence length variance (calculate via script). Variance below 30 indicates overly uniform rhythm -- vary sentence length deliberately 4. Identify formulaic patterns: "The X lesson:", "The practical implication:", "The X question:" -- replace with direct statements 5. Apply targeted edits: fix grammar, restructure sentences, strengthen arguments 6. Remove AI-isms (see `humanizer` skill for detailed patterns) 7. Provide before/after comparison for major changes 8. Ve
- **Targeted Patching vs Full Rewrite** — For texts that are mostly clean (good arguments, natural voice, minor AI patterns), prefer targeted `patch` operations over full rewrites. Full rewrites risk losing the author's voice and introducing new problems. Only do a full rewrite when the structural problems are pervasive.
- **Pitfalls** — - Over-editing to the point of losing original voice - Introducing new factual errors during rewriting - Ignoring user-specified tone/style constraints

## Further detail

### Verification

- Read edited text aloud for flow - Confirm no new information was added unintentionally

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/creative/improve-writing/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
