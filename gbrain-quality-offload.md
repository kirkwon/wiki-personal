---
type: concept
title: Gbrain Quality Offload
created: 2026-09-05
updated: 2026-09-05
tags:
  - Skill
  - uncategorized
---

# gbrain-quality-offload

"Use when gbrain has garbage or stale pages. Offload to OKF archive."

## Usage

# GBrain Quality Offload

## When to Use
- gbrain search results are noisy with garbage/low-value pages
- Periodic cleanup (monthly or quarterly)
- After bulk ingestion that imported low-quality content

## The Pipeline

### Step 1: Export gbrain
```bash
gbrain export --dir /tmp/gbrain-export-full/
```

### Step 2: Classify pages
```bash
python3 /tmp/classify_gbrain.py
```
Classifies into: youtube_hash, clickbait, old_projects, archives, tiny_stubs, inbox, keep.

### Step 3: Archive to OKF vault
```bash
python3 ~/.hermes/scripts/gbrain_offload.py --dry-run  # preview
python3 ~/.hermes/scripts/gbrain_offload.py            # execute
```

### Step 4: Soft-delete from gbrain
```bash
python3 ~/.hermes/scripts/gbrain_batch_delete.py       # ~1hr for 5000 pages
```

### Step 5: Verify
```bash
gbrain stats    # should show reduced page count
gbrain search "test query"  # should show cleaner results
```

## Archive Location
- Vault: `~/gbrain-archive/`
- INDEX: `~/gbrain-archive/INDEX.md` (Obsidian MOC with category links)
- Each page has OKF v0.2 frontmatter with trust signals

## OKF Trust Signals on Archive Pages
```yaml
type: archive-page
verified_by: null        # unverified
confidence: low          # low | medium | high
staleness: archived      # fresh | aging | stale | archived
auto_generated: true     # pipeline-produced
```

## Garbage Categories (2026-08-03 audit)
- `_real` suffix: YouTube video IDs with garbled titles (340)
- `_improved` suffix: Auto-scraped clickbait articles (658)
- `10-projects/` paths: Pre-reorg project paths (68)
- `40-archives/`: Pre-existing archive content (1,727)
- <500 bytes: Tiny stub/placeholder pages (2,039)
- `inbox/`: Unprocessed research findings (94)