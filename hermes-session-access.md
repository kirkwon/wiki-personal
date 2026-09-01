---
type: concept
title: Hermes Session Access
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - uncategorized
---

# hermes-session-access

Pattern for accessing Hermes session data (e.g., user messages) from Python scripts when the hermes_tools module does not expose the expected functions.

## Usage

# Hermes Session Access

## Trigger
When you need to access session data (e.g., user messages) from within a Python script running in the Hermes agent environment, and the standard import from `hermes_tools` does not provide the expected function (e.g., `session_search`).

## Solution

### The Correct Import Path (verified 2026-07-24)

`hermes_tools` is **NOT** an importable package. The `session_search` function lives in the Hermes agent's `tools/` directory as `session_search_tool.py`.

```python
import sys, json

# Add BOTH the hermes-agent root and the tools/ subdirectory
sys.path.insert(0, '/Users/kirkwon/.hermes/hermes-agent')
sys.path.insert(0, '/Users/kirkwon/.hermes/hermes-agent/tools')

from session_search_tool import session_search

# session_search returns a JSON STRING, not a dict — must parse
raw = session_search(query='your query', limit=5)
result = json.loads(raw) if isinstance(raw, str) else raw

# Result structure: {success, mode, query, results, count, sessions_searched}
# Each result has: session_id, title, snippet, when, source, model, matched_role, match_message_id
```

**Critical details:**
- Must run with the Hermes venv Python: `~/.hermes/hermes-agent/venv/bin/python3`
- Returns a **JSON string**, not a dict — always `json.loads()` the result
- Results are under `result["results"]`, NOT `result["data"]["sessions"]`

### Fallback: Direct SQLite Access

If you only need session metadata (not FTS5 search), query `state.db` directly:

```python
import sqlite3
from pathlib import Path

conn = sqlite3.connect(str(Path.home() / '.hermes' / 'state.db'))
conn.row_factory = sqlite3.Row
rows = conn.execute(
    'SELECT id, title, message_count FROM sessions WHERE message_count >= 10 ORDER BY started_at DESC LIMIT 5'
).fetchall()
sessions = [dict(r) for r in rows]
```

## Notes
- The `hermes_tools` module **does not exist** as an importable package despite the `execute_code` environment providing a `hermes_tools` namespace for tool calls. Scripts running standalone via `python3` or `subprocess` must import from `session_search_tool` directly.
- `session_search` returns a JSON string, not a dict.
- Always handle the case where the import fails and provide a fallback mechanism.
- For a detailed explanation of this pattern, see `references/hermes-session-access-pattern.md`.

## Example
See the `lightweight_intent_tracker.py` script in the UserIntentBaseline project for an implementation of this pattern.