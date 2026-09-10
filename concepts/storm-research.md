---
date: 2026-07-19
type: concept
title: Storm Research
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- research
sources:
- hermes://skill/storm-research
description: Stanford STORM multi-perspective research via delegate_task subagents.
  Anti-hallucination contracts, pre-flight tool checks, citation-enforced output,
  cross-validation, and verification layer. Use for deep-dive research requiring multiple
  expert angles.
---

# Storm Research

> Stanford STORM multi-perspective research via delegate_task subagents. Anti-hallucination contracts, pre-flight tool checks, citation-enforced output, cross-validation, and verification layer. Use for deep-dive research requiring multiple expert angles.

## Overview

- **When to Use** — - Deep-dive research needing 3+ distinct expert angles - Topics where a single-prompt pass would miss entire categories of inquiry - Investment research, competitive analysis, technology assessment - Any research where structural blind spots are costly
- **When NOT to Use** — - Simple factual lookup → use web_search directly - Research with <3 angles → just do it inline - Time-critical (<10 min) → STORM adds ~15-20 min overhead for quality gates
- **Phase 0: Pre-Flight Checklist** — **Run BEFORE dispatching any subagents.** This catches the #1 failure mode (broken tools).

## Further detail

### ANTI-HALLUCINATION CONTRACT (binding)

- Every factual claim MUST reference a tool call output from THIS session. - "I couldn't verify this" is acceptable. Fabrication is not. - Do NOT use pre-training knowledge as a primary source. - If web tools are unavailable, say so explicitly and stop. - Any number without a source = automatic failure. - If you find a figure in a workspace file, cite the file path.

### RESEARCH QUESTIONS

[3-4 narrow questions with explicit search strategy for each]

### OUTPUT FORMAT (mandatory — do not deviate)

Return a JSON array of findings:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/storm-research/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
