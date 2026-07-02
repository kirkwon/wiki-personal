---
type: concept
title: Real Estate Analyzer (skill candidate)
description: "Executable skill for single-property and portfolio-level real estate investment analysis. Calculates NOI, cap rate, cash-on-cash, LTV, DSCR, 1031 exchange tax savings, and portfolio concentration risk."
created: 2026-07-02
updated: 2026-07-02
tags:
- skill-candidate
- finance
- real-estate
- risk-management
phase: P3
io_contract:
  input: "{property_address, purchase_price, down_payment_pct, loan_rate, loan_term, monthly_rent, operating_expenses, vacancy_rate, tax_bracket, sale_price_projection}"
  output: "{noi, cap_rate, cash_on_cash, ltv, dscr, var_95, 1031_tax_savings, concentration_hhi}"
depends_on:
- leverage-risk-analysis (wiki)
- single-property-analysis (wiki)
- 1031-exchange-strategy (wiki)
- net-operating-income (wiki)
- portfolio-dashboard (skill)
priority: high
rationale: "18KB of real estate finance content across 4 wiki concepts with no executable skill. Cron already ingests 3 of these concepts. Building a calculator skill closes the gap."
---
# Real Estate Analyzer

**Phase:** P3 (Execute)
**Master:** finance-master
**Priority:** High

## Input Schema
```json
{
  "property_address": "123 Main St",
  "purchase_price": 1000000,
  "down_payment_pct": 0.2,
  "loan_rate": 0.0675,
  "loan_term_years": 30,
  "monthly_gross_rent": 6500,
  "operating_expenses_pct": 0.35,
  "vacancy_rate": 0.05,
  "tax_bracket": 0.35,
  "sale_price_projection": 1200000,
  "holding_years": 5
}
```

## Output Schema
```json
{
  "noi": 50700,
  "cap_rate": 0.0507,
  "cash_on_cash": 0.087,
  "ltv": 0.625,
  "dscr": 1.41,
  "var_95": -38000,
  "1031_tax_savings": 236000,
  "concentration_hhi": 0.18,
  "recommendation": "HOLD — cash flow positive, LTV within limits"
}
```

## Sources
- [[leverage-risk-analysis]] — LTV/DSCR thresholds
- [[single-property-analysis]] — Cash flow breakdown
- [[1031-exchange-strategy]] — Tax deferral calc
- [[net-operating-income]] — NOI formula
- [[portfolio-dashboard]] — VaR/CVaR integration
- [[cash-flow-stress-testing]] — Scenario engine

## DAG Position
`inputs → RealEstateAnalyzer → portfolio-dashboard (VaR) → gbrain-content-ops (store)`
