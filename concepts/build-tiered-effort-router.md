---
date: 2026-07-19
type: concept
title: Build Tiered Effort Router
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Effort-Routing
- Thompson-Sampling
- Bandit
- TDD
- Router
- software-development
sources:
- hermes://skill/build-tiered-effort-router
description: 'Build a two-tier effort router: rule-based + learned bandit.'
---

# Build Tiered Effort Router

> Build a two-tier effort router: rule-based + learned bandit.

## Overview

- **When to Use** — - "Build a task-difficulty / effort classifier for LLM calls" - "Route reasoning_effort (low/medium/high/max) based on task type" - "I want a learned router with a rule-based cold-start fallback" - "Add a bandit/Thompson-sampling layer to my classification system" - "A/B test rule-based vs learned routing"
- **Prerequisites** — - Python 3.8+ with `scikit-learn`, `numpy`, `pytest` — invoke through the `terminal` tool: `pip install scikit-learn numpy pytest` - **Interpreter consistency**: verify `which python3` matches the pytest shebang (`head -1 $(which pytest)`). If they differ, the test suite passes but CLI scripts fail with `ModuleNotFoundError`. Fix: use the same interpreter for both, or alias. - Target system must accept a `reasoning_effort` parameter (Z.AI/glm-5 supports `low`/`high`/`max`)
- **How to Run** — Build is TDD-first: tests → implementation → fix failures → green. Tier 1 first, Tier 3 second. Use `write_file` for new scripts, `patch` for fixes, `terminal` to run `pytest`.

## Further detail

### Architecture

**Key design properties:** - **Cold start never breaks** — `LearnedRouter.classify()` returns Tier 1 result when untrained - **JSONL is the contract** — Tier 1 logs → `retrain.py` → Tier 3 model. Outcome tracker feeds the bandit online. - **Cost-aware** — bandit prefers cheaper arms at similar success probability (`score = beta_sample / cost`) - **Non-stationary** — `decay_all()` shrinks Beta params toward prior, handling task-drift over time

### Test Thresholds Reference

| Test | Wrong assert | Right assert | Why | |------|-------------|-------------|-----| | Converges to best arm | `all(s == 'high')` | `count('high') >= 18/20` | Uniform prior blips | | Cost-aware prefers cheaper | `count('low') > 0.7` | `count('low') > 0.7` ✓ | This one is stable | | Pipeline email high-effort | `high_pct > 0.5` | `high_pct >= 0.4` | Cost-aware tradeoff | | TF-IDF clustering | `labels[0]==labels[1]` | `len(set(labels)) >= 2` | Small-corpus incoherence |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/build-tiered-effort-router/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
