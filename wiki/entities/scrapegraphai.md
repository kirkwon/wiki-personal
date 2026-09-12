---
date: 2026-06-21
type: media
title: ScrapeGraphAI
description: "LLM-powered web extraction tool (23k GitHub stars). Uses SmartScraperGraph with Ollama (free, local) to produce clean, focused content from URLs. Slower but higher quality than heuristic extraction."
created: 2026-06-21
updated: 2026-06-21
tags: [tool, web, scraping, llm, open-source, local, free]
sources: [agent-session, scrapegraphai-docs]
summary: "LLM-powered extraction via Ollama gemma4 — strips noise, produces focused content. Available as Hermes extract backend for quality-sensitive research."
tier: supporting
base_confidence: 0.85
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
  - target: "[[entities/crawl4ai]]"
    type: related_to
---

# ScrapeGraphAI

**ScrapeGraphAI** (v2.1.3, 23k GitHub stars) is a Python library that uses LLM-powered graph-based scraping. Unlike heuristic extractors, it sends page content through an LLM to produce clean, focused output.

## Why It Matters

While [[entities/crawl4ai|Crawl4AI]] extracts everything and lets the consumer filter, ScrapeGraphAI's LLM pre-filters — stripping ads, navigation, boilerplate, and irrelevant content before returning the result. This produces dramatically cleaner output for research workflows where signal-to-noise ratio matters.

## Capabilities

| Capability | Support |
|---|---|
| URL → Focused Text | ✅ (LLM-filtered — best quality) |
| URL → Structured JSON | ✅ (NL prompt → schema) |
| Batch extraction | ✅ (sequential, each URL = LLM call) |
| JS rendering | ✅ (Playwright via undetected-playwright) |
| Web search | ❌ |
| Site crawling | ✅ (SmartCrawler graph) |

## LLM Configuration

ScrapeGraphAI auto-selects its LLM:

| Priority | Source | Model | Cost |
|---|---|---|---|
| 1 | `SCRAPEGRAPH_MODEL` env var | User-specified | Varies |
| 2 | `OPENAI_API_KEY` present | `openai/gpt-4o-mini` | Tokens |
| 3 | **Default** | `ollama/gemma4` | **Free** |

## Performance Characteristics

| Metric | Value |
|---|---|
| Ollama gemma4 | ~30-60s per URL (9.6GB model, local inference) |
| OpenAI gpt-4o-mini | ~5-10s per URL (API call) |
| Output quality | **Best** — LLM strips everything non-essential |
| Output length | Shorter than Crawl4AI (focused vs. complete) |

## Integration in Hermes

Installed 2026-06-21 as an extract-only backend:

- **Plugin path**: `plugins/web/scrapegraphai/`
- **Config**: `web.extract_backend: scrapegraphai` (switch when quality matters)
- **Skill**: `devops/scrapegraphai-extract`

Uses `asyncio.to_thread()` to run the synchronous `SmartScraperGraph.run()` without blocking the event loop. A 120-second timeout accommodates slow LLM inference.

## When to Use

- **Research workflows** — quality > speed, you want the signal not the noise
- **Structured extraction** — NL prompt → JSON schema (e.g., "extract all product prices")
- **Wiki ingestion** — cleaner source content for knowledge distillation

## When NOT to Use

- **Speed-sensitive** — 30-60s per URL vs Crawl4AI's 1-4s
- **Bulk scraping** — each URL burns an LLM call (free with Ollama, but slow)
- **Full-page capture** — LLM may omit content you consider relevant

## Comparison: Same URL, Different Approach

| Backend | example.com Result |
|---|---|
| [[entities/crawl4ai]] | Full page: title, body text, all elements (~17K chars on HN) |
| ScrapeGraphAI | Focused text only: "Example Domain. This domain is for use in documentation..." (~117 chars) |

## Related Pages

- [[concepts/web-extraction-provider-architecture]] — how this fits in the provider system
- [[entities/crawl4ai]] — faster heuristic alternative (default extract backend)
- [[entities/firecrawl]] — cloud backend with both search and extract
