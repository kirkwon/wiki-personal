---
type: concept
title: Knowledge Maintenance Session Learnings
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - knowledge-management
---

# knowledge-maintenance-session-learnings

Hard-won operational details from running knowledge-maintenance at scale (268-skill gap closed 2026-07-19). Captures the CONTENT_DIRS constraint, cache-clearing requirement, batch-write pattern, and cross-ref --hermes limitation that the parent skill omits. Loaded when running knowledge-maintenance or debugging why newly-written wiki stubs don't appear in stats/cross-ref.

## Usage

# Knowledge Maintenance — Session Learnings

Operational details discovered while running the `knowledge-maintenance` skill at scale. The parent skill (`knowledge-maintenance`) is manually-authored and cannot be patched by the background curator, so this companion captures the gaps.

## When to load

- Running `knowledge-maintenance` cron job or manual invocation.
- Debugging: "I wrote wiki pages but `stats` / `cross-ref` / `search` can't see them."
- Reviewing why Action 1, 2, or 4 of the parent skill behaved unexpectedly.

## The CONTENT_DIRS Constraint (CRITICAL)

`wiki-tools` (`~/Downloads/10-projects/10-active-projects/wiki-tools/wiki_api.py`) only scans a FIXED list of directories, defined in `CONTENT_DIRS` at the top of the file. As of 2026-07-19:

```
wiki/concepts, wiki/entities, wiki/sources, wiki/comparisons,
wiki/synthesis, wiki/queries, wiki/gaps, wiki/assets,
concepts, entities, sources, comparisons, synthesis, gaps,
questions, references
```

**`wiki/skills/` is NOT in this list** — despite `wiki-agent`'s AGENTS.md implying it is a valid vault category. Pages written to `wiki/skills/` will exist on disk but be invisible to every CLI command (`stats`, `cross-ref`, `search`, `inventory`, `page`).

### Fix
Always write skill stubs to **`~/wiki-personal/concepts/`** (root), never `wiki/skills/`.

### Diagnostic
If a page exists on disk (`ls`) but `cross-ref` reports the skill as unmatched, check whether its directory is in `CONTENT_DIRS`:

```bash
grep -A20 '^CONTENT_DIRS' ~/Downloads/10-projects/10-active-projects/wiki-tools/wiki_api.py
```

## Frontmatter Cache Must Be Cleared After Bulk Writes

`wiki-tools` caches parsed frontmatter at `~/.cache/wiki-tools/frontmatter-cache.json`. After writing many pages:

```bash
rm -f ~/.cache/wiki-tools/frontmatter-cache.json
python3 cli.py stats
python3 cli.py cross-ref --wiki | tail -3
```

Without cache clearance, `stats` reports the OLD page count and `cross-ref` still shows the gap as unclosed — even though the files exist on disk.

### `--no-cache` flag is broken
`python3 cli.py --no-cache ...` throws `KeyError: '/Users/kirkwon/wiki-personal/AGENTS.md'` as of 2026-07-19. Prefer deleting the cache file over using `--no-cache` until that bug is fixed upstream.

## Batch Stub Creation Recipe (for 100+ skill gaps)

Per-skill `python3 cli.py write ...` calls are impractical at cron timescales when the gap is large. Use direct file writes instead. Full recipe with verification:

```python
import re
from pathlib import Path
from datetime import date

text = Path('/tmp/cross-ref-wiki.txt').read_text()
matches = re.findall(r'❌\s+(\S+)\s+\(no wiki match\)\s+\[([^\]]*)\]', text)

def to_title(slug):
    return ' '.join(w.capitalize() for w in slug.split('-'))

today = date.today().isoformat()
dst = Path.home() / 'wiki-personal' / 'concepts'
dst.mkdir(parents=True, exist_ok=True)

created, skipped = 0, 0
for slug, cat in matches:
    cat = cat or 'uncategorized'
    target = dst / f'{slug}.md'
    if 

...(truncated)