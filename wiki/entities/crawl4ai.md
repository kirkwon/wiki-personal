---
date: 2026-06-21
type: media
title: Crawl4AI
description: "Open-source web content extraction tool (62k GitHub stars). Uses Playwright + heuristic content extraction to return clean markdown from any URL. Free, local, no API key."
created: 2026-06-21
updated: 2026-06-21
tags: [tool, web, scraping, open-source, local, free]
sources: [agent-session, crawl4ai-docs]
summary: "Free local web extraction — Playwright + heuristic markdown output. Installed as Hermes extract backend replacing Firecrawl credit dependency."
tier: core
base_confidence: 0.90
lifecycle: draft
lifecycle_changed: "2026-06-21"
provenance:
  extracted: 0.8
  inferred: 0.2
  ambiguous: 0.0
relationships:
  - target: "[[concepts/web-extraction-provider-architecture]]"
    type: implements
  - target: "[[entities/hermes-agent]]"
    type: uses
  - target: "[[entities/firecrawl]]"
    type: replaces
  - target: "[[entities/scrapegraphai]]"
    type: related_to
---

# Crawl4AI

**Crawl4AI** is an open-source Python library (v0.9.0, 62k GitHub stars) for web content extraction. It uses Playwright for JavaScript rendering and heuristic content extraction to produce clean markdown from any URL.

## Why It Matters

Crawl4AI eliminates the Firecrawl credit dependency for `web_extract` operations. Every page scrape that previously consumed Firecrawl credits now runs locally — free, unlimited, no rate limits.

## Capabilities

| Capability | Support |
|---|---|
| URL → Markdown | ✅ Native (primary use case) |
| URL → HTML | ✅ |
| Batch extraction | ✅ (sequential through shared crawler) |
| JS rendering | ✅ (Playwright) |
| Structured extraction | ⚠️ (CSS/XPath/semantic strategies, not LLM) |
| Web search | ❌ |
| Anti-bot | ⚠️ (stealth mode, no proxy rotation) |
| Caching | ✅ (built-in) |

## Performance Characteristics

| Metric | Value |
|---|---|
| Cold start | ~3-4s (Playwright browser launch) |
| Warm extract | ~1s per URL |
| Output quality | Good — captures full page content in markdown |
| Memory | Moderate (Chromium instance) |

## Integration in Hermes

Installed 2026-06-21 as an extract-only backend in Hermes's [[concepts/web-extraction-provider-architecture|provider system]]:

- **Plugin path**: `plugins/web/crawl4ai/`
- **Config**: `web.extract_backend: crawl4ai` (active default)
- **Skill**: `devops/crawl4ai-extract`

The provider uses a singleton `AsyncWebCrawler` instance — the browser pool starts once and stays warm for subsequent extractions. A 60-second timeout prevents hangs on unresponsive pages.

## Limitations

- **No search** — extract-only, can't discover URLs
- **No anti-bot layer** — Cloudflare-protected sites will block it ^[inferred]
- **Pre-1.0 dependency** — v0.9.x API may change between releases
- **Sequential** — URLs processed one at a time through the shared crawler

## When to Use

- **Default extraction** — speed matters, page is standard HTML
- **Credit conservation** — avoids burning Firecrawl credits
- **Offline/batch** — large scraping jobs where cloud costs would be prohibitive

## Related Pages

- [[concepts/web-extraction-provider-architecture]] — how this fits in the provider system
- [[entities/scrapegraphai]] — slower but higher-quality alternative (LLM-powered)
- [[entities/firecrawl]] — the cloud backend this replaces for extraction
