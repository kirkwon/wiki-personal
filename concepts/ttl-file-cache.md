---
date: 2026-07-19
type: concept
title: Ttl File Cache
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- caching
- performance
- file-system
- python
- pattern
- software-development
sources:
- hermes://skill/ttl-file-cache
description: Use when implementing persistent, TTL-based file caching for a CLI tool.
  Provides MD5 key generation, TTL expiry checks, and read/write operations. Works
  with any JSON-serializable data.
---

# Ttl File Cache

> Use when implementing persistent, TTL-based file caching for a CLI tool. Provides MD5 key generation, TTL expiry checks, and read/write operations. Works with any JSON-serializable data.

## Overview

- **When to Use** — - Speeding up repeated CLI operations (search, query, fetch) - Avoiding redundant API calls or file scans - Implementing cache-aside pattern with configurable TTL - Storing JSON-serializable results across invocations
- **Testing** — Expected output:
- **Pitfalls** — 1. **MD5 collision** — astronomically unlikely for cache keys; not a practical concern 2. **Cache file permissions** — JSON cache is world-readable by default; don't store secrets 3. **TTL=0 means always expired** — useful for testing, not for production 4. **File mtime precision** — some filesystems have 1-2 second resolution; TTL < 5s is unreliable 5. **No cache size limit** — implement LRU eviction if disk space is a concern

## Further detail

### Success Metrics

| Metric | Target | |--------|--------| | Cache read (hit) | <10ms | | Cache write | <50ms | | TTL expiry accuracy | ±1s |

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/ttl-file-cache/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
