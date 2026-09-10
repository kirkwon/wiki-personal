---
date: 2026-08-02
type: concept
title: Crawl4Ai
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- research
sources:
- hermes://skill/crawl4ai
description: Local web crawler for extracting clean markdown from any URL. Full local,
  zero API costs, no credits needed. Default replacement for Firecrawl.
---

# Crawl4Ai

> Local web crawler for extracting clean markdown from any URL. Full local, zero API costs, no credits needed. Default replacement for Firecrawl.

## Overview

- **Installation** — Already installed at `/Users/kirkwon/.hermes/hermes-agent/.venv/lib/python3.12/site-packages/crawl4ai`. Version 0.9.0.
- **Performance** — | Site | Time | Output | |---|---|---| | Blog post (addyosmani.com) | 1.27s | 17,520 chars clean markdown | | Article (langchain.com) | ~1-2s | Full article | | News (theregister.co.uk) | ~2s | Article body |
- **When to Use** — **Use crawl4ai for:** - All web article/blog extraction (default) - Multi-URL batch scraping - Deep-dive research (quality extraction) - Any skill that previously called `web_extract` or Firecrawl

## Further detail

### Integration with Hermes Skills

Replace all `web_extract` calls with crawl4ai where possible. The pattern:

### Notes

- crawl4ai handles most sites including JS-rendered content (via Playwright under the hood) - Word count threshold of 50 filters out navigation/menu noise - Returns clean markdown — no HTML parsing needed - No rate limits — fully local - If a site blocks crawlers, fall back to browser tools or curl + regex

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/crawl4ai/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
