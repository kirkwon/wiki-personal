---
type: concept
title: Dojo Baseline Tracker
created: 2026-09-02
updated: 2026-09-02
tags:
  - Skill
  - uncategorized
---

# dojo-baseline-tracker

Track Dojo trends and detect model_degradation spikes.

## Usage

# Dojo Baseline Tracker

Track category distribution over time in Dojo eval reports to detect model_degradation spikes against a 7-day rolling baseline.

## When to Use

Run daily after Dojo eval to build baseline history. Use `--report` flag for weekly comparison.

## Core Workflow

### Daily Update

```bash
uv run python ~/.hermes/scripts/dojo-baseline-tracker.py --update
```

Reads `~/.hermes/dojo-eval/latest_analysis.json` and appends category counts to `baseline_history.json`.

### Baseline Report

```bash
uv run python ~/.hermes/scripts/dojo-baseline-tracker.py --report
```

Shows 7-day averages, today's deviation, and model_degradation alerts (2x/1.5x/OK thresholds).

## Integration

Update daily Dojo eval cron to wrapper:
```bash
0 7 * * * ~/.hermes/scripts/dojo-eval-with-baseline.sh
```

Wrapper runs Dojo eval then records baseline.

## Model Degradation

Category patterns: `No code provided`, `empty.*tool.*call`, `invalid.*tool.*call.*format`. These are provider/model issues, not tool bugs. Fix: switch model, not patch skill.

**Alert thresholds**:
- 2.0x above baseline: ⚠️ ALERT
- 1.5x above baseline: ⚠️ WARNING
- Within range: ✅ OK

## Files

- `~/.hermes/scripts/dojo-baseline-tracker.py` - Main script
- `~/.hermes/scripts/dojo-eval-with-baseline.sh` - Wrapper
- `~/.hermes/dojo-eval/baseline_history.json` - Baseline data

## Related Skills

- `dojo-eval-tuning` - Cut false positives in analyzer
- `dojo-circuit-breaker-triage` - Reset stale breakers
- `dojo-to-production-pipeline` - End-to-end workflow