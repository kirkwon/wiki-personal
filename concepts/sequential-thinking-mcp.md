---
date: 2026-07-19
type: concept
title: Sequential Thinking Mcp
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- MCP
- reasoning
- problem-solving
- mcp
sources:
- hermes://skill/sequential-thinking-mcp
description: MCP server for structured step-by-step problem solving via sequential
  thinking. Enables multi-step reasoning with branching, revision, and hypothesis
  verification.
---

# Sequential Thinking Mcp

> MCP server for structured step-by-step problem solving via sequential thinking. Enables multi-step reasoning with branching, revision, and hypothesis verification.

## Overview

- **Tool: `sequential_thinking`** — | Parameter | Type | Description | |-----------|------|-------------| | `thought` | string | The current reasoning step | | `nextThoughtNeeded` | boolean | Whether to continue thinking after this | | `thoughtNumber` | integer | Which step this is | | `totalThoughts` | integer | Estimated total steps needed | | `isRevision` | boolean | Whether this revises a prior step | | `revisesThought` | integer | Which step is being revised | | `branchFromThought` | integer | Branching point for alternative paths | | `branchId` | string | Unique branch identifier | | `needsMoreThoughts` | boolean | Signals
- **When to Use It** — Best for: - Database migrations, deployment planning, architecture decisions - Debugging production-only failures (multi-step root cause analysis) - Comparing N architectural options with branching when assumptions change - Problems where the model should "think out loud" rather than one-shot answer - Tasks where a pivot midway through is likely
- **Hermes Integration** — When connected via mcporter, Hermes will use the `sequential_thinking` tool automatically when you ask complex, multi-step reasoning problems.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mcp/sequential-thinking-mcp/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
