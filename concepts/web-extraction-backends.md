---
date: 2026-07-19
type: concept
title: Web Extraction Backends
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- web
- scraping
- extract
- plugin-system
- hermes
- architecture
- devops
sources:
- hermes://skill/web-extraction-backends
description: Hermes web extraction provider system — pluggable backends for URL→content
  extraction. Covers backend comparison, switching, and the plugin creation pattern.
  Crawl4AI (fast/free), ScrapeGraphAI (LLM-powered/free), and Firecrawl (cloud/credits)
  supported.
---

# Web Extraction Backends

> Hermes web extraction provider system — pluggable backends for URL→content extraction. Covers backend comparison, switching, and the plugin creation pattern. Crawl4AI (fast/free), ScrapeGraphAI (LLM-powered/free), and Firecrawl (cloud/credits) supported.

## Overview

- **⚠️ Behavioral Rule (Read First)** — **NEVER report "web search unavailable" or answer from memory when `web_search` fails.** Always try free alternatives first. The user has explicitly flagged this as a recurring annoyance — a failed `web_search` is the *start* of a task, not the end of it.
- **Current Backends** — | Backend | Type | Search | Extract | Cost | Speed | Quality | Active | |---|---|---|---|---|---|---|---| | **Crawl4AI** | Local | ❌ | ✅ | **Free** | ~1-4s | Good (heuristic) | ✅ Default extract | | **ScrapeGraphAI** | Local | ❌ | ✅ | **Free** (Ollama) | ~30-60s | **Best** (LLM-filtered) | Available | | **Browser (agent-browser)** | Local (CDP) | ✅ | ❌ | **Free** | ~3-8s | Good (live render) | ✅ Default search | | **DDGS** | Local | ✅ | ❌ | Free | Fast | Basic | ✅ Default search | | Firecrawl | Cloud | ❌ | ✅ | Credits | ~2-5s | Good | Available (extract only) | | Tavily/Exa/Brave | Cloud | ✅ |
- **Switching Backends** — **Search vs Extract independence:** `web_search` and `web_extract` use completely independent backends. `web_search` uses DDGS or browser backends (never Firecrawl). `web_extract` may use crawl4ai, ScrapeGraphAI, or Firecrawl depending on config.

## Further detail

### When to Use Which

| Scenario | Backend | Why | |---|---|---| | Default scraping, bulk extraction | **Crawl4AI** | Speed + free + no LLM dependency | | Research, wiki ingest, quality-sensitive | **ScrapeGraphAI** | LLM strips noise, produces focused content | | Anti-bot needed (Cloudflare, etc.) | **Firecrawl** | Has Fire-engine proxy rotation | | Credits available, want cloud reliability | **Firecrawl** | No local resource usage |

### Architecture: Per-Capability Split

Resolution priority: 1. Per-capability override (`search_backend` / `extract_backend`) 2. Shared backend (`web.backend`) 3. Auto-detect (scan candidates, pick first available)

### Adding a New Backend

See **`references/web-backend-plugin-pattern.md`** for the complete 6-edit-point integration pattern. Every backend follows the same template:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/web-extraction-backends/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
