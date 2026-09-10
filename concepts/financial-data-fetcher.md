---
date: 2026-08-02
type: concept
title: Financial Data Fetcher
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/financial-data-fetcher
description: Financial data fetcher with caching.
---

# Financial Data Fetcher

> Financial data fetcher with caching.

## Overview

- **Trigger Conditions** — Use when you need to fetch financial market data (prices, economic indicators, index data) from multiple sources with caching to reduce API load and ensure consistency across scripts.
- **Steps** — 1. Set up the module in `~/.hermes/scripts/finance/data_fetcher.py` 2. Import functions in your Python script 3. Fetch data using standardized interfaces 4. Handle missing dependencies gracefully 5. Optionally manage the cache
- **Functions** — - get_price_data: OHLCV data via yfinance - get_close_data: Adjusted close prices - get_fred_data: FRED economic indicators - get_openbb_index_data: OpenBB index/fundamental data - get_cache_info: Cache statistics - clear_cache: Clear cached files

## Further detail

### Pitfalls

- Import path issues (missing sys.path addition) - Missing API keys (FRED_API_KEY not set) - Missing dependencies (assuming OpenBB is installed) - Data availability (handling empty results) - Cache mutation (always work on copies) - Cache expiration (default 1 hour) - Invalid yfinance parameters - Single vs multiple ticker return formats

### Verification

1. Import test: Verify module imports correctly 2. Basic fetch test: Get data for known tickers 3. Cache test: Verify caching behavior 4. Error handling test: Test with invalid inputs/missing deps 5. Integration test: Confirm updated scripts work

### Maintenance

- Adjust CACHE_EXPIRY_HOURS as needed - Add new data sources following existing patterns - Monitor cache directory size - Keep dependencies updated

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/financial-data-fetcher/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
