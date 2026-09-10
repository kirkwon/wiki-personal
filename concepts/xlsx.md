---
date: 2026-07-19
type: concept
title: Xlsx
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- productivity
- xlsx
- excel
- spreadsheets
- finance
- data
- openpyxl
sources:
- hermes://skill/xlsx
description: 'Create, read, edit, and analyze Excel spreadsheets (.xlsx, .xlsm, .csv,
  .tsv). Use for financial models, data analysis, reports, charts, and any tabular
  data work. Emphasizes Excel formulas over hardcoded values for dynamic spreadsheets.
  Triggers on: ''.xlsx'', ''spreadsheet'', ''Excel'', ''financial model'', ''data
  analysis'', ''sheet''.'
---

# Xlsx

> Create, read, edit, and analyze Excel spreadsheets (.xlsx, .xlsm, .csv, .tsv). Use for financial models, data analysis, reports, charts, and any tabular data work. Emphasizes Excel formulas over hardcoded values for dynamic spreadsheets. Triggers on: '.xlsx', 'spreadsheet', 'Excel', 'financial model', 'data analysis', 'sheet'.

## Overview

- **Overview** — Two tools for different jobs: - **pandas**: Data analysis, bulk operations, simple data export - **openpyxl**: Complex formatting, formulas, charts, Excel-specific features
- **Quick Reference** — | Task | Tool | Command | |------|------|---------| | Read/analyze data | pandas | `pd.read_excel('file.xlsx')` | | Create with formulas | openpyxl | `Workbook()` then `sheet['A1'] = '=SUM(B:B)'` | | Format/style | openpyxl | `Font()`, `PatternFill()`, `Alignment()` | | Charts | openpyxl | `BarChart()`, `LineChart()`, `Reference()` | | Large files | pandas | `pd.read_excel('file.xlsx', usecols=['A','B'])` |
- **Formula Verification** — After creating/modifying, verify:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/xlsx/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
