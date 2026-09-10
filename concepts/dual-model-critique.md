---
date: 2026-08-02
type: concept
title: Dual Model Critique
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/dual-model-critique
description: Route verification to a different model than the executor.
---

# Dual Model Critique

> Route verification to a different model than the executor.

## Overview

- **When to Use** — - Code review where the executor's model might miss class-specific bugs - Plan/task validation before committing resources - Writing voice checks (does this match an established style guide?) - Security audits (does this output leak data?) - Any RDEIUR-style cycle where the "Invalidate" step needs genuine independence
- **When NOT to Use** — - Simple tasks where a single pass suffices (costs latency for no gain) - Tasks where the executor model is already the strongest available - Interactive/real-time work where the 5-30s critic latency is unacceptable
- **The Core Insight** — **Role separation without model separation is theater.** If glm-5 grades glm-5's work, the "critic" shares the same training distribution, the same failure modes, and the same blind spots. The separation is nominal, not functional. This was confirmed by premortem analysis (Project 108, failure mode F1) and by benchmark:

## Further detail

### Model Selection for the Critic Role

The critic MUST be a different model family than the executor. Diversity of training distribution is the whole point.

### OmniRoute API Quirks

OmniRoute wraps multiple free providers and exposes an OpenAI-compatible API. Key quirks documented in `references/omniroute-api-reference.md`:

### Token Economics

The critic step costs ~15% of a full RDEIUR cycle's tokens. At OmniRoute's $0 cost, the critic adds zero financial overhead. At OpenRouter pricing, a typical critique (4K input + 1K output on DeepSeek V4 Flash) costs $0.00055 — less than a cent.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/dual-model-critique/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
