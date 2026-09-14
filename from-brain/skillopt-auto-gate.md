---
type: note
title: SkillOpt Auto-Gate
created: '2026-07-21T00:00:00.000Z'
updated: '2026-07-21T00:00:00.000Z'
ingested_via: put_page
ingested_at: '2026-07-22T00:25:09.929Z'
source_kind: put_page
tags:
  - auto-gate
  - llm-judge
  - loop-engineering
  - skill-optimization
---

# SkillOpt Auto-Gate

An automated acceptance gate for skill instruction optimization. Closes the loop on [[loop-engineering]]'s skill auto-patch phase — instead of proposing changes for human review, the gate auto-applies optimized instructions that beat benchmark scores and auto-rejects those that don't.

Inspired by Microsoft's SkillOpt (open-sourced Jul 2026), which optimizes agent skills the same way you train an AI model: a base model runs the task, an optimizer evaluates the output and rewrites the instructions itself.

## Pipeline

```
1. Read SKILL.md (baseline)
2. Run against benchmark test prompts → score with LLM judge (0-10 rubric)
3. Generate optimized instructions (LLM rewrites based on weak areas)
4. Run optimized version → score
5. Gate: if delta ≥ threshold → auto-apply (with backup); else reject
6. Log to ~/loop-state/skillopt/ for monitoring
```

## Components

### skill-optimizer.py (Gate Engine)
- **Baseline scoring**: Runs skill instructions as system prompt against test prompts, LLM judge scores each response on configurable rubric (accuracy, completeness, clarity)
- **Optimization loop**: LLM generates improved instructions targeting weak areas identified by the judge. Iterates up to N times, keeping the best.
- **Acceptance gate**: Auto-applies if `delta ≥ threshold` (default 0.5/10). Creates .bak backup before writing.
- **Scoring**: Per-prompt weighted average normalized to 0-10 scale

Usage:
```bash
python3 skill-optimizer.py --skill ~/.hermes/skills/foo/SKILL.md \
  --benchmarks benchmarks.json \
  --threshold 0.5 --max-iterations 3
```

### skill-optimizer-monitor.py (Effectiveness Monitor)
Reads all run logs and computes:
- Accept/reject rates over time
- Average score deltas (is the optimizer actually improving skills?)
- Per-skill history
- Weekly trends
- Health assessment (accept_rate >90% = too loose, <10% = too conservative)

Usage:
```bash
python3 skill-optimizer-monitor.py          # Human report
python3 skill-optimizer-monitor.py --json   # For scripting
python3 skill-optimizer-monitor.py --list-runs  # Per-run detail
```

## Benchmark Format

```json
{
  "test_prompts": ["prompt 1", "prompt 2", ...],
  "rubric": {
    "criteria": [
      {"name": "accuracy", "weight": 3.0, "description": "..."},
      {"name": "completeness", "weight": 2.0, "description": "..."}
    ]
  }
}
```

## Key Design Decisions

1. **LLM-as-judge** (not deterministic tests) — skills produce natural language; rubric scoring handles this. Judge model is separate from optimizer (critic separation).
2. **Per-prompt weighted average** normalized to 0-10 — comparable across skills with different rubrics.
3. **Default threshold 0.5** — filters LLM judge variance (~0.2-0.3 noise floor) while accepting real improvements.
4. **Backup before apply** — every auto-applied change creates a .bak file.
5. **All runs logged** — monitor reads JSON logs for effectiveness tracking.

## Relationship to Existing Systems

- **Extends [[loop-engineering]]**: Phase 3 (skill auto-patch detection) was "propose only, never auto-apply." This gate closes that loop.
- **Complements [[self-harness]]**: Self-harness is the inner loop (weakness mine → propose → validate). SkillOpt is the acceptance gate that decides whether proposals get applied.
- **Within [[graph-engineering]] framework**: The optimization-cycle loop node embeds in the project DAG. The outer double-loop reviews effectiveness.

## Verified Results (2026-07-21)

- **REJECT case**: Bad skill scored 8.61/10 baseline → optimized to 9.06 (+0.45) — correctly rejected (+0.45 < 0.5 threshold)
- **ACCEPT case**: Same skill re-run, optimized to 9.72 (+0.61) — correctly accepted, file applied (9 lines → 123 lines), backup created
- **Monitor**: 2 runs tracked, 50% accept rate, +0.53 avg delta, health "moderate"

## Implementation

- **Project**: `~/clawd/100.SkilloptAuto-gate/`
- **Gate engine**: `03.Scripts/skill-optimizer.py`
- **Monitor**: `03.Scripts/skill-optimizer-monitor.py`
- **State dir**: `~/loop-state/skillopt/`
- **Default model**: deepseek-v4-flash via OpenRouter (~$0.001/run)

## Related

- [[loop-engineering]] — Predecessor (critic/doer, triage, skill auto-patch)
- [[self-harness]] — Inner improvement loop
- [[graph-engineering]] — Framework context
- [[graphwork]] — Project scaffold system used
