---
date: 2026-05-14
type: note
title: Skills Dashboard - Summary
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
-

# Skills Dashboard - Summary

## Overview
Fixed and updated the skills dashboard with normalized data from 98 books.

## What Was Fixed

### Original Issues
1. **"All Skills" tab only showed 5 skills** - The embedded `all_skills` array was incomplete
2. **Missing tags** - Many tags referenced in `multi_tag_skills` weren't in `skills_by_tag`
3. **Data inconsistency** - HTML had partial/corrupted embedded data

### Solution
Created `normalize_skills_data.py` to:
1. **Parse new JSON format** from `/Users/kirkwon/Downloads/book_summaries/unified_books_improved/`
2. **Normalize tags** - Consolidated 100+ variations into 10 main categories
3. **Filter generic terms** - Removed non-descriptive words like "planning", "improvement", "technique"
4. **Generate complete dataset** - 367 unique skills (up from 5!)

## Final Statistics

| Metric | Count |
|--------|-------|
| **Total Skills** | 367 |
| **Total Tags** | 10 |
| **Books Processed** | 98 |
| **Overlapping Skills** | 69 |
| **Multi-Tag Skills** | 105 |

### Top Tags by Skill Count
1. **self-improvement**: 354 skills
2. **finance**: 162 skills
3. **strategy**: 114 skills
4. **productivity**: 96 skills
5. **thinking**: 62 skills
6. **systems**: 48 skills
7. **psychology**: 48 skills
8. **innovation**: 30 skills
9. **habits**: 30 skills
10. **focus**: 24 skills

## Tag Normalization

The script consolidates similar tags:
- `habit-formation`, `habit` → `habits`
- `time-management`, `prioritization`, `execution` → `productivity`
- `mental-models`, `first-principles`, `systems-thinking` → `thinking`
- `behavioral-economics`, `mindset`, `self-awareness` → `psychology`
- `decision-making`, `probabilistic-thinking` → `strategy`
- And 90+ more mappings...

## Files Created

1. **`skills_data_updated.json`** - Complete normalized dataset
2. **`skills-dashboard-updated.html`** - Fixed dashboard with full data
3. **`normalize_skills_data.py`** - Script to regenerate from source

## Usage

### View Dashboard
```bash
open /Users/kirkwon/wiki-personal/skills-dashboard-updated.html
```

### Regenerate Data
```bash
python3 /Users/kirkwon/wiki-personal/normalize_skills_data.py
```

### Access Data
```python
import json
with open('skills_data_updated.json', 'r') as f:
    data = json.load(f)

# Access all skills
all_skills = data['all_skills']  # 367 skills

# Get skills by tag
productivity_skills = data['skills_by_tag']['productivity']

# Find overlapping skills
overlaps = data['overlaps']  # Skills in multiple books
```

## Sample Skills

### High-Quality Examples
- **Meaning finding framework** (Man's Search for Meaning)
- **Logotherapy techniques for existential analysis** (Man's Search for Meaning)
- **Swarm intelligence algorithms** (Out of Control)
- **Evolutionary computation and genetic algorithms** (Out of Control)
- **Network science and graph theory** (Out of Control)

### Multi-Tag Skills
Skills appearing in multiple categories:
- Mathematical models (finance, strategy, thinking)
- Game theory models (finance, strategy)
- Network analysis models (finance, thinking)
- Systems dynamics models (finance, thinking)

## Next Steps

1. **Improve extraction** - The current parsing extracts from `agent_structure.core_skills`
   - Could also parse `summary` sections for more skills
   - Extract from chapter summaries

2. **Better descriptions** - Currently uses generic "To apply X effectively" format
   - Could extract from `quick_reference.why_it_matters`
   - Use summary text for richer descriptions

3. **Manual review** - Some generic terms still slip through
   - Add to `generic_terms` set as needed
   - Consider a blacklist approach for author names

4. **Add more books** - Script can process any JSON in the source directory
   - Drop new `*_improved.json` files in the directory
   - Re-run normalization script

## Technical Details

### Data Format
```json
{
  "skills_by_tag": {
    "tag": [["skill_name", "book_title"], ...]
  },
  "all_skills": ["skill_name", ...],
  "all_tags": ["tag", ...],
  "overlaps": {
    "skill_name": ["book1", "book2", ...]
  },
  "multi_tag_skills": {
    "skill_name": ["tag1", "tag2", ...]
  },
  "descriptions": {
    "skill_name": "description text"
  }
}
```

### Tag Normalization Rules
1. Convert to lowercase
2. Remove special characters
3. Apply normalization mapping
4. Skip empty results

### Skill Filtering
1. Skip if in `generic_terms` set
2. Skip if < 3 characters
3. Skip if just a verb without object
4. Skip if in `generic_concepts` set

---

**Generated**: 2025-05-05
**Source**: 108 JSON files from `unified_books_improved/`
**Output**: `/Users/kirkwon/wiki-personal/`
