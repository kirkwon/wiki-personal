---
date: 2026-06-21
type: concept
title: Web Extraction Provider Architecture
description: "Hermes Agent's pluggable web extraction system — any backend (Firecrawl, Crawl4AI, ScrapeGraphAI) behind a unified interface, with per-capability routing (search vs extract)."
created: 2026-06-21
updated: 2026-06-21
tags: [architecture, web, scraping, hermes, plugin-system]
sources: [agent-session, hermes-agent-docs]
summary: "Pluggable web extraction architecture in Hermes — backends swap via config, no code changes. Crawl4AI (fast/free) and ScrapeGraphAI (LLM-powered/free) now sit alongside Firecrawl."
tier: core
base_confidence: 0.85
lifecycle: draft
lifecycle_changed: "2026-06-21"
provenance:
  extracted: 0.7
  inferred: 0.3
  ambiguous: 0.0
relationships:
  - target: "[[entities/hermes-agent]]"
    type: uses
  - target: "[[entities/firecrawl]]"
    type: related_to
  - target: "[[entities/crawl4ai]]"
    type: related_to
  - target: "[[entities/scrapegraphai]]"
    type: related_to
---

# Web Extraction Provider Architecture

## Problem

Web content extraction (URL → markdown/structured data) is a foundational capability for any agent system — research, ingestion, monitoring, and automation all depend on it. But the tooling landscape is fragmented:

- **Cloud APIs** (Firecrawl, Tavily) — powerful but credit-limited and rate-capped
- **Local scrapers** (Crawl4AI, ScrapeGraphAI) — free but slower, no anti-bot layer
- **Search engines** (Brave, DuckDuckGo, Exa) — discovery, not extraction

Hardcoding any single backend creates lock-in: when Firecrawl credits run out, the agent goes blind.

## Architecture: Per-Capability Provider Split

Hermes solves this with a **plugin-based web provider system** that separates two capabilities:

```
web_search    → find URLs (query → results)
web_extract   → get content (URL → markdown/JSON)
```

Each capability can be routed to a different backend independently:

```yaml
web:
  backend: firecrawl          # default for both
  search_backend: ''          # override for search only
  extract_backend: crawl4ai   # override for extract only
```

### Provider Lifecycle

1. **Plugin discovery** — Hermes scans `plugins/web/<name>/` at startup
2. **Registration** — each plugin's `register(ctx)` calls `ctx.register_web_search_provider(ProviderClass())`
3. **Selection** — `web_tools.py` resolves which provider to use based on config + availability
4. **Dispatch** — `web_search_tool` / `web_extract_tool` call the selected provider's method

### Provider Interface

Every provider subclasses `WebSearchProvider` and implements:

| Method | Required? | Purpose |
|---|---|---|
| `is_available()` | ✅ | Can this backend run? (env vars, package importable) |
| `supports_search()` | ✅ | Does it do search? |
| `supports_extract()` | ✅ | Does it do extraction? |
| `search(query, limit)` | If `supports_search()` | Query → result list |
| `extract(urls, format)` | If `supports_extract()` | URL list → content list |
| `get_setup_schema()` | ✅ | UI metadata for setup wizard |

### Backend Resolution Priority

```
1. Explicit config override (search_backend / extract_backend)
2. Shared backend (web.backend)
3. Auto-detect: scan candidates in priority order, pick first available
```

## Backends Matrix (as of 2026-06-21)

| Backend | Search | Extract | Cost | Speed | Quality | Anti-bot |
|---|---|---|---|---|---|---|
| **Firecrawl** | ✅ | ✅ | Credits | Fast (~2-5s) | Good | ✅ (Fire-engine) |
| **Crawl4AI** | ❌ | ✅ | **Free** | Fast (~1-4s) | Good (heuristic) | ⚠️ (stealth mode) |
| **ScrapeGraphAI** | ❌ | ✅ | **Free** (Ollama) | Slow (~30-60s) | **Best** (LLM-filtered) | ⚠️ |
| **Tavily** | ✅ | ✅ | Credits | Fast | Good | ❌ |
| **Exa** | ✅ | ✅ | Credits | Fast | Good | ❌ |
| **DDGS** | ✅ | ❌ | Free | Fast | Basic | ❌ |
| **Brave Free** | ✅ | ❌ | Free | Fast | Basic | ❌ |
| **Parallel** | ✅ | ✅ | Credits | Fast | Good | ❌ |
| **XAI** | ✅ | ❌ | Free | Fast | Basic | ❌ |

## Key Insight: Extract-Only Backends

Crawl4AI and ScrapeGraphAI are **extract-only** — they can't search the web. This is why the per-capability split matters: `web_search` stays on Firecrawl/ddgs (which have search), while `web_extract` routes to Crawl4AI (which is free and local).

Before this architecture, extract-only tools couldn't be used without also providing search. The split unlocks an entire category of free local tools. ^[inferred]

## Implementation Pattern

Creating a new extract backend requires:

1. **3 plugin files**: `plugins/web/<name>/{__init__.py, plugin.yaml, provider.py}`
2. **6 edit points** in `web_tools.py`: backend name sets, availability checks, display
3. **Config switch**: `hermes config set web.extract_backend <name>`

Total effort: ~4-8 hours for a well-documented library like Crawl4AI.

## Related Pages

- [[entities/hermes-agent]] — the agent framework this powers
- [[entities/crawl4ai]] — fast local extraction backend
- [[entities/scrapegraphai]] — LLM-powered extraction backend
- [[entities/firecrawl]] — cloud extraction backend (credits)
- [[concepts/plugin-architecture]] — Hermes plugin system overview
