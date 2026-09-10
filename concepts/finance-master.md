---
date: 2026-07-19
type: concept
title: Finance Master
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/finance-master
description: Meta-skill for financial analysis, portfolio management, options, and
  market modeling — pick the right analytical tool for any financial question.
---

# Finance Master

> Meta-skill for financial analysis, portfolio management, options, and market modeling — pick the right analytical tool for any financial question.

## Overview

- **Delegation Contract — Phase Discipline** — Finance-master is a **toolkit** (not a pipeline), so the phase mapping is per-skill, not per-workflow-stage:
- **A/B Testing Overlapping Skills** — Don't consolidate by intuition — A/B test overlapping skills on the same input.
- **Notes** — - Finance skills depend on data sources (OpenBB MCP, yfinance, Alpha Vantage). Verify `hermes status` shows active data pipeline before running. - **Pre-flight checklist** before any analysis: 1. Run `hermes status` — check OpenBB, yfinance, Alpha Vantage availability 2. Quick price check: `curl -sL "https://query2.finance.yahoo.com/v8/finance/chart/SYMBOL?interval=1d&range=5d" -H "User-Agent: Mozilla/5.0"` 3. If OpenBB available: `obb.equity.price.quote('SYMBOL')` for options (use `.results` to access data, not `.head()`) 4. If yfinance missing: install with `uv pip install yfinance` or use O

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance-master/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
