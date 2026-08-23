---
date: 2026-06-21
title: Hot Cache
updated: 2026-06-21
---

## Recent Activity
- **2026-06-21**: Documented Web Extraction Provider Architecture — Crawl4AI + ScrapeGraphAI added as free local extract backends for Hermes. Eliminates Firecrawl credit dependency for `web_extract`.

## Active Threads
- Web extraction architecture: per-capability provider split (search vs extract) enables free local backends
- Portfolio dashboard upgrade: Phase 1 (Rebalance/Catalyst/Tax) + Phase 2 (Risk Attribution) complete
- Firecrawl alternatives evaluation: 2 adapters built (Crawl4AI fast, ScrapeGraphAI quality)

## Key Takeaways
- Hermes web extraction is now free and unlimited — `web.extract_backend: crawl4ai` routes all extract calls locally
- ScrapeGraphAI available for quality-sensitive research (LLM-filtered output via Ollama gemma4)
- Provider pattern: extract-only backends work because search and extract are split at the config level

## Flagged Contradictions
- None
