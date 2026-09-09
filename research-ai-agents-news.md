---
type: concept
title: Research Ai Agents News
created: 2026-09-08
updated: 2026-09-08
tags:
  - Skill
  - uncategorized
---

# research-ai-agents-news

Research AI agents news across HN, YouTube, Polymarket (+ Reddit/Twitter social layer).

## Usage

# Research AI Agents News Across Platforms

## When to Use
Use this skill when you need to gather recent news, developments, or market sentiments about AI agents from Hacker News, YouTube, Polymarket, Reddit, and Twitter/X within a configurable timeframe (default last 30 days).

## Description
Skill for researching recent AI agents news from multiple platforms. Uses HN Algolia API for posts with points/comments, YouTube search for recent videos with view counts, Polymarket for relevant markets with odds, and — when the social layer is requested — Reddit via OpenCLI and Twitter/X via twitter-cli.

## Trigger
User requests research on AI agents news, trends, or developments within a recent timeframe (e.g., last 30 days). Explicitly include the social layer (Reddit + Twitter) when the user asks about "discussions", "sentiment", "what people are saying", or similar.

## Search Strategy

Use Exa AI (agent-reach search backend) as the primary search tool. Exa is documented in
`~/.hermes/skills/agent-reach/references/search.md` and invoked via `mcporter`.

Fallback chain for each search step below:

1. **Exa** via `mcporter call 'exa.web_search_exa(query: "...", numResults: N)'` — high-quality AI search, strong on tech/English.
2. **Native web_search** tool — fallback if Exa fails or returns empty.
3. **Empty result** → note the gap, move on.

**Note on Jina Reader:** `~/.hermes/skills/agent-reach/references/web.md` documents `curl r.jina.ai/URL`
as a universal web reader. From this network (AS7018), anonymous Jina Reader requests return
`401 AuthenticationRequiredError` — Jina Reader is **not wireable** here without authentication.
Do not rely on it as a fallback. Defuddle (`https://defuddle.md/<url>`) handles static page→MD
conversion and is the preferred web-extraction path.

## Steps

### 1. Determine Timestamp for 30 Days Ago
- Use Python to compute Unix timestamp for 30 days ago:
  ```bash
  python -c "import time, datetime; print(int((datetime.datetime.now() - datetime.timedelta(days=30)).timestamp()))"
  ```

### 2. Query Hacker News via Algolia API
- Call HN Algolia search endpoint with query `AI agents news`, hitsPerPage=10, and numeric filter for created_at_i greater than the timestamp.
  ```bash
  curl -s "https://hn.algolia.com/api/v1/search?query=AI+agents+news&hitsPerPage=10&numericFilters=created_at_i>TIMESTAMP"
  ```
- Extract from JSON: title, points, num_comments, url, story_id, created_at.

### 3. Search YouTube for Recent Videos

- Use web search with query: `site:youtube.com "AI agents" after:YYYY-MM-DD` (where YYYY-MM-DD is 30 days ago).

**Exa-first routing (agent-reach search backend):**

1. **Primary:** `mcporter call 'exa.web_search_exa(query: "site:youtube.com \"AI agents\" after:YYYY-MM-DD", numResults: 10)'`
2. **Fallback:** native `web_search` tool with same query.
3. **Empty** → note gap, skip Videos section.

For each result URL, navigate via browser_navigate, then browser_snapshot (full=true) to extract view count.
In t

...(truncated)