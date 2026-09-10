---
date: 2026-07-13
type: concept
title: Hermes Web Search Backend Diagnostic
created: 2026-07-13
updated: '2026-09-09'
tags:
- skill
- Skill
sources:
- hermes://skill/hermes-web-search-backend-diagnostic
description: Diagnose and fix web_search backend mis-resolution in Hermes.
---

# Hermes Web Search Backend Diagnostic

> Diagnose and fix web_search backend mis-resolution in Hermes.

## Overview

- **When to Use** — - `web_search` returns "Firecrawl search failed: Payment Required" but config says `search_backend: ddgs` - `web_search` errors mention a backend the user never configured - Suspecting web_search is ignoring `web.search_backend` / `web.extract_backend` config - After a profile or model switch, web_search behavior changed unexpectedly
- **Prerequisites** — - Hermes installed at `~/.hermes/hermes-agent/` with the **runtime** venv at `~/.hermes/hermes-agent/venv/` (Python 3.11). There is also a `.venv/` (Python 3.12) used for dev/build only — do NOT install into it. - `terminal` toolset enabled - Read access to `tools/web_tools.py` via `search_files` / `read_file`
- **How to Run** — 1. Invoke `web_search` with a simple query and capture the exact error text. 2. Read the configured `web.search_backend` from the active profile config. 3. Run the diagnostic snippet against the **runtime** venv Python. 4. Install the `ddgs` package into the runtime venv if the check returns `False`. 5. Verify against the same runtime venv — never assume.

## Further detail

### Quick Reference

- Backend resolution chain: `_get_search_backend()` → `_get_capability_backend("search")` → `_is_backend_available(configured)` → fallback `_get_backend()` - Fallback priority in `_get_backend()`: tavily → exa → parallel → firecrawl → searxng → brave-free → ddgs - ddgs availability: `_ddgs_package_importable()` → `import ddgs` - **PyPI package: `ddgs`** (v9.x, module `ddgs`). NOT `duckduckgo-search` (v8.x, module `duckduckgo_search`) — different package, does NOT provide `ddgs` import. - **Runtime venv Python: `~/.hermes/hermes-agent/venv/bin/python3`** (NOT `.venv/`)

### Procedure

1. **Capture the symptom.** Invoke `web_search` with `query="test"`. Note the backend named in the error.

### Pitfalls

- **Two venvs — only `venv/` is the runtime:** `~/.hermes/hermes-agent/` contains both `venv/` (Python 3.11, the runtime the gateway and sessions use) and `.venv/` (Python 3.12, dev/build). Installing into `.venv/` produces a fix that passes local verification but has zero effect on the running session. Always confirm with `head -1 $(which hermes)`. - **`ddgs` ≠ `duckduckgo-search`:** Two separate PyPI packages. `duckduckgo-search` (v8.x) provides module `duckduckgo_search` and does NOT provide `import ddgs`. The Hermes ddgs plugin does `from ddgs import DDGS` — only the `ddgs` package (v9.x)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/hermes-web-search-backend-diagnostic/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
