---
date: 2026-07-19
type: concept
title: Verification Before Completion
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- verification
- completion
- testing
- honesty
- guardrails
- evidence
- software-development
sources:
- hermes://skill/verification-before-completion
description: 'Iron law: no completion claims without fresh verification evidence.
  Use when about to claim work is complete, fixed, or passing — before committing,
  creating PRs, or telling the user something is done. Evidence before assertions,
  always.'
---

# Verification Before Completion

> Iron law: no completion claims without fresh verification evidence. Use when about to claim work is complete, fixed, or passing — before committing, creating PRs, or telling the user something is done. Evidence before assertions, always.

## Overview

- **Core Principle** — **Claiming work is complete without verification is dishonesty, not efficiency.**
- **The Iron Law** — If you haven't run the verification command in this message, you cannot claim it passes.
- **Claim → Evidence Matrix** — | Claim | Required Evidence | NOT Sufficient | |---|---|---| | Tests pass | `terminal(test command)` → 0 failures | Previous run, "should pass" | | Linter clean | `terminal(lint command)` → 0 errors | Partial check, extrapolation | | Build succeeds | `terminal(build command)` → exit 0 | Linter passing, logs look good | | Bug fixed | Test original symptom: passes | Code changed, assumed fixed | | Regression test works | Red-green cycle verified | Test passes once | | Agent completed task | `terminal(git diff)` shows changes | Agent reports "success" | | File written correctly | `read_file(path)

## Further detail

### Red Flags — STOP

- Using "should", "probably", "seems to" - Expressing satisfaction before verification ("Great!", "Perfect!", "Done!") - About to commit/push/PR without verification - Trusting agent success reports (subagent self-reports are NOT verified facts) - Relying on partial verification - Thinking "just this once" - Tired and wanting work over - **ANY wording implying success without having run verification**

### Rationalization Prevention

| Excuse | Reality | |---|---| | "Should work now" | RUN the verification | | "I'm confident" | Confidence ≠ evidence | | "Just this once" | No exceptions | | "Linter passed" | Linter ≠ compiler ≠ tests | | "Agent said success" | Verify independently (git diff, file check) | | "I'm tired" | Exhaustion ≠ excuse | | "Partial check is enough" | Partial proves nothing | | "Different words so rule doesn't apply" | Spirit over letter |

### Hermes-Specific Verification Patterns

| Task Type | Verification Method | |---|---| | Python script | `terminal("python script.py")` — check exit code + output | | Config change | `read_file(path)` + try loading with yaml.safe_load | | File write | `read_file(path)` to confirm content landed | | Git operations | `terminal("git log --oneline -3")` or `git diff` | | Skill creation | `skill_view(name)` to confirm it loads | | Subagent task | Check actual artifacts (files, commits, URLs) — not just the summary | | Web scraping | Verify the extracted data matches expectations | | Package install | `terminal("which binary")` or `binary

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/verification-before-completion/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
