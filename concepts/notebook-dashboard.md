---
date: 2026-07-19
type: concept
title: Notebook Dashboard
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- productivity
sources:
- hermes://skill/notebook-dashboard
description: Creates an interactive HTML dashboard for browsing and filtering NotebookLM
  catalog data with sorting capabilities
---

# Notebook Dashboard

> Creates an interactive HTML dashboard for browsing and filtering NotebookLM catalog data with sorting capabilities

## Overview

- **When to Use** — - You have a NotebookLM catalog (like `clawd/27.NotebookLM-Catalog/catalog_data.json`) and want to visualize it - You need to filter notebooks by domain, source count, or other attributes - You want to sort the catalog by different columns (title, source count, etc.) - You want to see sample sources for each notebook - You want to generate a shareable HTML report
- **What It Creates** — The skill generates an HTML file (`notebook-dashboard.html`) that contains:
- **Customization** — The dashboard HTML and CSS live **inline** in the generator script at: `~/.hermes/skills/productivity/notebook-dashboard/bin/generate_dashboard.py` (the `HTML_TEMPLATE` constant).

## Further detail

### Integration Notes

- Works with any JSON array of notebook objects that have at least `title`, `source_count`, and `sample_sources` fields - Automatically infers domains from notebook titles using keyword matching - Preserves all original data in the detailed view - Responsive design works on mobile devices - Dark/light mode aware (follows system preferences)

### Example Usage

The dashboard will show all 46 notebooks from your catalog, allowing you to: - Sort by source count to see which notebooks have the most/least sources - Filter to see only Finance or AI/ML notebooks - Search for specific topics like "Bayesian" or "Transformer" - Click on any row to see the detailed sample sources for that notebook

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/notebook-dashboard/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
