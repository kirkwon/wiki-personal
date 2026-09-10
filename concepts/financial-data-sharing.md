---
date: 2026-08-02
type: concept
title: Financial Data Sharing
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/financial-data-sharing
description: Build reusable financial data utilities.
---

# Financial Data Sharing

> Build reusable financial data utilities.

## Overview

- **When to Use** — - Multiple scripts fetch similar financial data (price data, FRED indicators, etc.) - You notice repeated yfinance/FRED/OpenBB API calls across projects - Scripts are making redundant API calls that could be cached - You want to standardize data access patterns across financial tools - Building new financial analysis tools that will need market data
- **Why This Matters** — Financial analysis workflows often duplicate data fetching logic, leading to: - Unnecessary API load and rate limiting risks - Inconsistent error handling and data formats - Maintenance burden when fixing bugs or updating sources - Difficulty in sharing improvements across tools
- **Verification Steps** — After implementing and refactoring: - [ ] All updated scripts produce identical output to originals - [ ] Cache is functioning (second run faster, files in cache dir) - [ ] Error handling works (invalid tickers, missing API keys) - [ ] Scripts work when optional dependencies missing - [ ] No regression in performance or accuracy

## Further detail

### Reference Implementation

See `data_fetcher.py` in `~/.hermes/scripts/finance/` for a working example that: - Implements all the above patterns - Serves sector rotation, hedge signal, macro brief, and SPCX monitor - Includes comprehensive caching and error handling - Handles pandas MultiIndex correctly - Gracefully degrades when FRED/OpenBB unavailable

### Related Concepts

- **Data layer separation**: Keeps data fetching separate from business logic - **Caching strategies**: Reduces external API load and improves performance - **Interface standardization**: Makes tools more composable and maintainable - **Dependency isolation**: Makes scripts more resilient to environmental changes

### Maintenance Tips

- Update cache keys when function signatures change - Monitor cache directory size periodically - Consider adding cache pre-warming for predictable workloads - Update shared utility when new data sources are needed - Document any breaking changes for consumers of the utility

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/financial-data-sharing/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
