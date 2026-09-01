---
type: concept
title: Web Fallback
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - uncategorized
---

# web-fallback

>

## Usage

# Web Fallback Skill

This skill wraps Hermes' native `web_search` and `web_extract` tools with
fallbacks to:
- **Exa AI search** (via `mcporter`) for semantic, zero‑API‑key search
- **Jina Reader** (`https://r.jina.ai/URL`) for universal web‑page text extraction

It also keeps a simple in‑session counter of calls and fallbacks, useful for
monitoring quota usage during a session.

## Usage

The skill does not expose direct CLI commands; instead it provides two
Python callables that can be used from `execute_code` or delegated subagents:

- `web_fallback_search(query, limit=5)` → dict (same shape as `web_search` output)
- `web_fallback_extract(url)` → dict (same shape as `web_extract` output)

Both functions first try the native Hermes tool; on failure or empty result,
they automatically fall back to the respective backup.

## Implementation details

The skill stores counters in a module‑level dictionary:
```python
_calls = {
    'web_search': {'attempts': 0, 'success': 0, 'fallback': 0},
    'web_extract': {'attempts': 0, 'success': 0, 'fallback': 0}
}
```
These are reset when the Python interpreter is reloaded (i.e., per session).

## Example

```python
from hermes_tools import execute_code

code = '''
from web_fallback import web_fallback_search, web_fallback_extract

# Search
results = web_fallback_search("Hermes agent framework", limit=3)
print(f"Search results: {len(results.get('data',{}).get('web',[]))}")

# Extract
content = web_fallback_extract("https://hermes-agent.nousresearch.com/docs/")
print(f"Extracted length: {len(content.get('results',[{}])[0].get('content',''))}")
'''

res = execute_code(code=code)
print(res['output'])
```

## Notes

- The Exa fallback uses the free tier; be mindful of the ~$10/month credit
  (roughly 10 QPS sustained). For heavy usage consider adding your own
  rate‑limit or switching to a paid plan.
- The Jina Reader fallback is free and key‑less, but excessive calls from a
  single IP may be throttled; keep occasional fallback usage well below
  a few requests per second.
- This skill does **not** persist counters across Hermes sessions; if you
  need longer‑term tracking, wrap the calls in your own logging.

---
# Python implementation (web_fallback.py)

Place this file alongside SKILL.md in the skill directory.

```python
"""Web fallback utilities for Hermes Agent."""

from hermes_tools import web_search, web_extract, mcporter, json_parse

# Simple in‑session call counters
_calls = {
    'web_search': {'attempts': 0, 'success': 0, 'fallback': 0},
    'web_extract': {'attempts': 0, 'success': 0, 'fallback': 0}
}


def web_fallback_search(query: str, limit: int = 5) -> dict:
    """
    Search with fallback to Exa.
    Returns a dict matching the shape of `web_search` output.
    """
    _calls['web_search']['attempts'] += 1
    try:
        res = web_search(query, limit=limit)
        # Consider it a success if we got any results
        if res and res.get('data', {}).get('web'):
            _calls['web_searc

...(truncated)