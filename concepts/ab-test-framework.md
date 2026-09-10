---
date: 2026-07-19
type: concept
title: Ab Test Framework
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- a-b-testing
- experimentation
- statistics
- web-development
- dashboard
- software-development
sources:
- hermes://skill/ab-test-framework
description: 'Generate complete A/B testing infrastructure: variant setup, tracking
  code, statistical analysis, and a reporting dashboard with framework-aware project
  detection.'
---

# Ab Test Framework

> Generate complete A/B testing infrastructure: variant setup, tracking code, statistical analysis, and a reporting dashboard with framework-aware project detection.

## Overview

- **Parameters** — | Parameter | Required | Default | Description | |-----------|----------|---------|-------------| | `project_path` | ✅ | — | Path to the project | | `test_name` | ✅ | — | Name of the experiment (e.g., "signup-button-color") | | `variants` | ✅ | — | Comma-separated variant names (e.g., "control,variant-a,variant-b") | | `metrics` | ✅ | — | Comma-separated metric names (e.g., "click_rate,conversion,revenue") | | `framework` | ❌ | `auto` | Web framework (auto/react/vue/angular/vanilla) | | `sample_size` | ❌ | `1000` | Minimum sample size per variant | | `confidence_level` | ❌ | `95` | Statistical
- **Pitfalls** — - **User bucketing must be deterministic** — use consistent hashing on user ID, not random assignment per page load - **Multiple experiments on the same page** — ensure experiment gates don't conflict; each experiment should use a unique namespace - **Sequential testing** — standard fixed-horizon analysis inflates false positives if checked continuously; implement the confidence interval approach or use the sequential testing module - **Novelty effects** — results in the first few days may not be stable; the dashboard should show confidence over time, not just current p-value - **Dashboard is

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/ab-test-framework/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
