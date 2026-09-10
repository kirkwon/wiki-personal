---
date: 2026-07-19
type: concept
title: Feeds
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/feeds
description: Monitor and process information feeds — RSS, Twitter/X, newsletters,
  blogwatcher, and other content streams. Extract items, categorize, surface interesting
  signals, and queue for wiki/GBrain ingestion. Trigger on phrases like "check feeds",
  "new content", "blog watcher", "RSS", "newsletter", "what's new", "catch up".
---

# Feeds

> Monitor and process information feeds — RSS, Twitter/X, newsletters, blogwatcher, and other content streams. Extract items, categorize, surface interesting signals, and queue for wiki/GBrain ingestion. Trigger on phrases like "check feeds", "new content", "blog watcher", "RSS", "newsletter", "what's new", "catch up".

## Overview

- **Feed Sources** — - Blogwatcher tracked blogs and substacks - X/Twitter accounts via xitter - Arxiv paper feeds - Newsletters via email
- **Processing Pipeline** — 1. **Collect** — Fetch new items from each source 2. **Filter** — Skip items below relevance threshold 3. **Extract** — Pull key content, links, and metadata 4. **Categorize** — Tag by domain (AI/ML, Finance, etc.) 5. **Queue** — Add high-value items to paper/research queue 6. **Store** — Ingest to GBrain if worth keeping

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/feeds/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
