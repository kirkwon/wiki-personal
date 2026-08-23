---
date: 2026-07-02
type: concept
title: Retirement Calculator (skill candidate)
description: "Executable skill for retirement planning — savings targets, RMD projections, Roth conversion optimization, and withdrawal sequencing."
created: 2026-07-02
updated: 2026-07-02
tags:
- skill-candidate
- finance
- retirement
- tax
phase: P3
io_contract:
  input: "{age, current_savings, annual_income, annual_expenses, savings_rate, current_allocation, tax_bracket, retirement_age}"
  output: "{portfolio_target, monthly_savings_needed, rmd_amount_at_73, roth_conversion_savings, withdrawal_sequence, success_probability}"
depends_on:
- retirement-planning (wiki)
- retirement-account-types (wiki)
- required-minimum-distributions-rmds (wiki)
- mean-variance-analyzer (skill)
priority: high
rationale: "14KB of retirement content in wiki (4% rule, RMD calc, account types). Used by update-financial-strategy-notebook cron weekly. Should be executable."
---
# Retirement Calculator

**Phase:** P3 (Execute)
**Master:** finance-master
**Priority:** High

## Input Schema
```json
{
  "age": 35,
  "current_savings": 250000,
  "annual_income": 150000,
  "annual_expenses": 80000,
  "savings_rate": 0.15,
  "current_allocation": {"stocks": 0.8, "bonds": 0.15, "cash": 0.05},
  "tax_bracket": 0.24,
  "retirement_age": 62,
  "social_security_estimate": 25000
}
```

## Output Schema
```json
{
  "portfolio_target": 1500000,
  "monthly_savings_needed": 1875,
  "rmd_at_73": 28840,
  "roth_conversion_savings": 45000,
  "withdrawal_sequence": ["taxable", "traditional_ira", "roth_ira"],
  "success_probability": 0.88,
  "allocation_glide_path": {"at_62": "60/30/10", "at_72": "40/40/20"}
}
```

## Sources
- [[retirement-planning]] — Full framework (14KB)
- [[retirement-account-types]] — Account decision tree
- [[required-minimum-distributions-rmds]] — RMD formula
- [[low-cost-index-funds]] — Fund recommendations
- [[mean-variance-analyzer]] — Allocation optimization

## DAG Position
`inputs → RetirementCalculator → portfolio-dashboard (age-based allocation) → gbrain-content-ops (store)`
