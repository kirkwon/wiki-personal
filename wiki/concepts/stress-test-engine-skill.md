---
type: concept
title: Stress Test Engine (skill candidate)
description: "Executable skill for running scenario analysis on real estate and portfolio cash flows — rent decline, vacancy spikes, rate hikes, and expense increases."
created: 2026-07-02
updated: 2026-07-02
tags:
- skill-candidate
- finance
- risk-management
- real-estate
phase: P3
io_contract:
  input: "{asset_type, baseline_cashflows, scenarios: [{name, rent_change_pct, expense_change_pct, vacancy_rate, rate_change_bps}]}"
  output: "{stress_metrics: [{scenario, noi, dscr, ltv, cash_flow, status}], worst_case, probability_weighted_expected}"
depends_on:
- cash-flow-stress-testing (wiki)
- leverage-risk-analysis (wiki)
- risk-assessment-framework (wiki)
- value-at-risk-var (wiki)
priority: medium
rationale: "Cash flow stress testing has explicit thresholds (vacancy >10% = high risk, expenses >50% = medium). Makes these executable as a scenario engine rather than just reference text."
---
# Stress Test Engine

**Phase:** P3 (Execute)
**Master:** finance-master
**Priority:** Medium

## Input Schema
```json
{
  "asset_type": "rental_property",
  "baseline_cashflows": {
    "monthly_gross_rent": 6500,
    "monthly_expenses": 2275,
    "loan_payment": 4100,
    "vacancy_rate": 0.05
  },
  "scenarios": [
    {"name": "mild_recession", "rent_change_pct": -0.1, "expense_change_pct": 0.05, "vacancy_rate": 0.08, "rate_change_bps": 0},
    {"name": "deep_recession", "rent_change_pct": -0.2, "expense_change_pct": 0.10, "vacancy_rate": 0.15, "rate_change_bps": 100},
    {"name": "rate_shock", "rent_change_pct": 0, "expense_change_pct": 0.03, "vacancy_rate": 0.05, "rate_change_bps": 200}
  ]
}
```

## Output Schema
```json
{
  "stress_metrics": [
    {"scenario": "mild_recession", "noi": 45630, "dscr": 1.27, "ltv": 0.68, "cash_flow": 820, "status": "CAUTION"},
    {"scenario": "deep_recession", "noi": 32500, "dscr": 0.93, "ltv": 0.75, "cash_flow": -1250, "status": "BREACH"},
    {"scenario": "rate_shock", "noi": 50700, "dscr": 1.12, "ltv": 0.72, "cash_flow": -340, "status": "WARNING"}
  ],
  "worst_case": "deep_recession",
  "probability_weighted_expected_noi": 43100
}
```

## Sources
- [[cash-flow-stress-testing]] — Thresholds and scenarios
- [[leverage-risk-analysis]] — LTV/DSCR risk levels
- [[risk-assessment-framework]] — Risk matrix methodology
- [[value-at-risk-var]] — VaR integration
- [[portfolio-dashboard]] — Existing risk tab

## DAG Position
`inputs → StressTestEngine → portfolio-dashboard (risk tab) → knowledge-ecosystem-ops (log scenario results)`
