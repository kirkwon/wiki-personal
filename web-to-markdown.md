---
type: concept
title: Web To Markdown
created: 2026-09-03
updated: 2026-09-03
tags:
  - Skill
  - productivity
---

# web-to-markdown

>

## Usage

# web-to-markdown — Universal Web → Markdown Pipeline

Two-stage pipeline: **agent-browser** extracts rendered HTML (handling JS, auth, lazy-load), **markitdown** normalizes to clean markdown. Handles pages that `web_extract` and `crawl4ai` can't reach.

## When to Use This vs Alternatives

| Tool | Best For | Handles JS | Handles Auth | Output |
|------|----------|-----------|-------------|--------|
| `web_extract` | Static pages, articles, APIs | No | No | Markdown |
| `crawl4ai` | Static-to-medium JS pages | Partial | No | Markdown |
| **web-to-markdown** | SPAs, dashboards, authenticated, lazy-load | **Yes** | **Yes** | Clean markdown |
| `agent-browser read` | Quick one-shot reads | Yes | With flags | Rough markdown |

Use this when `web_extract` returns empty/garbage, the page requires login, or content loads via JS after scroll.

## Prerequisites

```bash
# agent-browser (already installed at /opt/homebrew/bin/agent-browser)
agent-browser --version  # verify

# markitdown (installed via uv)
markitdown --help  # verify

# Both must be on PATH
```

## Quick Start

```bash
# Basic: extract any page to markdown (Defuddle default)
~/.hermes/scripts/web-to-markdown.sh "https://example.com/page" output.md

# Defuddle sha
# Non-Defuddle: authenticated, JS-heavy, or defuddle.md itself
# --auth: use Chrome Default profile (authenticated session) — skips Defuddle
# --full: scroll-triggered lazy content — skips Defuddle
# --skip-defuddle: force agent-browser path even for plain pages (debugging)
~/.hermes/scripts/web-to-markdown.sh "https://example.com/page" output.md --auth
~/.hermes/scripts/web-to-markdown.sh "https://example.com/feed" feed.md --full
~/.hermes/scripts/web-to-markdown.sh "https://example.com/page" page.md --skip-defuddle
```

## The Pipeline (How It Works)

```mermaid
    URL
     │
     ▼
┌──────────────────────────────┐
│  Defuddle (default)          │
│  • Static HTML → clean MD    │
│  • YAML frontmatter          │
│  • Zero browser overhead     │
│  • Fails → agent-browser     │
└──────────────────────────────┘
     │
     ▼ (auth / JS / --full / --skip-defuddle)
┌──────────────────────────────────┐
│  agent-browser (Chrome via CDP)  │
│  • Renders JS, SPAs              │
│  • Handles auth (--profile)      │
│  • Scrolls for lazy content      │
│  • Extracts rendered HTML        │
└──────────────────────────────────┘
 │
 ▼  Raw HTML (500KB-1MB)
┌──────────────────────────────────┐
│  markitdown (Microsoft)          │
│  • Strips nav/scripts/styles     │
│  • Converts tables, lists        │
│  • Normalizes headings/links     │
│  • 30-50x size reduction         │
└──────────────────────────────────┘
 │
 ▼  Clean Markdown (10-25KB)
┌──────────────────────────────────┐
│  gbrain add / wiki-ingest / NLM  │
│  (downstream knowledge pipeline) │
└──────────────────────────────────┘
```

## Manual Usage (More Control)

When the script doesn't give you enough control, run the stages manually:

```bash
# 1. Open page
agent-browser open "h

...(truncated)