---
type: concept
title: Search Recipes
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - recipes
---

# search-recipes

>-

## Usage

# Allrecipes Recipe Search

## Purpose

Search Allrecipes for recipes matching a query (keyword, ingredient list, category browse, or direct recipe URL) and return structured JSON — per-recipe identifier, title, author + profile URL, hero image + gallery images, star rating + count, prep/cook/total time (ISO 8601 + minutes), servings, calories, full ingredient list, step-by-step instructions, full nutrition facts, category/cuisine/dietary tags, "Made it" count, and the canonical recipe URL. Read-only — never clicks Save, Add to Meal Plan, Print, Rate, Comment, or Sign In.

## When to Use

- "Find me chocolate-chip cookie recipes ranked best-first."
- "Give me five 30-minute vegan dinners using soy sauce."
- "Extract the recipe at allrecipes.com/recipe/10813/... into structured form."
- "Bulk-collect Italian dinner recipes from `/recipes/86/world-cuisine/european/italian/`."
- Building meal planners, ingredient-aware search, recipe databases, or dietary-filter UIs on top of Allrecipes' content.

## Workflow

The optimal path is **HTTP-only via `browse cloud fetch` (the Browserbase Fetch API)**. Allrecipes is lightly walled — every probe in this skill's development (8 search-page fetches and 6 recipe-detail fetches across 3 query shapes) returned 200 with full SSR HTML. No proxies, no `--verified` Verified, no session, no auth, no cookies are required. Recipe detail pages ship one **schema.org `application/ld+json` Recipe block** containing every field you need; search results pages are server-rendered HTML cards (no `__NEXT_DATA__`, no XHR).

### 1. Branch on the input shape

| Input | Action |
|---|---|
| Direct recipe URL (`/recipe/<id>/<slug>/`) | Skip to step 4 (single-recipe extraction). |
| Full Allrecipes search URL (`/search?q=…`) | Use as-is in step 2. |
| Free-form query / ingredient list (`"chicken rice soy sauce"`) | Build `https://www.allrecipes.com/search?q=<URL-encoded query>`. |
| Category-browse intent (e.g. "Desserts", "Italian", "Healthy") | Resolve to a **taxonomy hub URL** `/recipes/<id>/<slug>/` — see the "Honest filter mapping" gotcha below. There is **no `?category=` query param** on `/search`. |

### 2. Fetch the search results page

```bash
browse cloud fetch "https://www.allrecipes.com/search?q=chocolate+chip+cookies" \
  --output /tmp/page-0.html
# For pages 2, 3, …: append &offset=24, &offset=48, &offset=72, …
```

**No flags required** for the first attempt (no `--proxies`, no `--allow-redirects`). Add `--allow-redirects` only when fetching old `/recipe/<id>/<old-slug>/` URLs that have been renamed (see gotchas).

### 3. Parse search-result cards from SSR HTML

Each card is one `<a>` anchor with class `mntl-card-list-card`. Iterate them with:

```regex
<a[^>]*mntl-card-list-card[^>]*href="(https://www\.allrecipes\.com/recipe/(\d+)/[^"]+)"(.*?)</a>
```

Per-card fields (all stable across queries; verified on `chocolate chip cookies` and `vegan lasagna`):

| Field | Source | Notes |
|---|---|---|
| `recipe_id` | URL slu

...(truncated)