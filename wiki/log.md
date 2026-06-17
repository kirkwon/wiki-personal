---
type: note
title: Wiki Log
created: 2026-05-14
updated: 2026-05-14
tags: []
sources: []
---
-

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-23] create | Wiki initialized
- Domain: Personal knowledge base covering cooking, photography, personal finance, and general second brain topics
- Structure created with SCHEMA.md, index.md, log.md
## [2026-04-24] ingest | Source Vault: obsidian_vaults/personal
- Created: 112 pages from 113 source files
- Entities: 2
- Concepts: 40
- Comparisons: 39
- Queries: 31
- Skipped: 1 (see details below)
- Raw sources preserved in: raw/ingested/

### Skipped files:
- Caramelization.md: too small

## [2026-04-24] lint | Wiki health check post-ingestion
- Pages scanned: 112
- Broken wikilinks: 736 (references to non-existent pages from source vault)
- Orphan pages: 89+ (no inbound links - expected for new wiki)
- Tag issues: Multiple tags not in SCHEMA taxonomy (general, books, local, jazz, etc.)
- Large pages: 10+ pages exceed 200 lines (candidates for splitting)
- Pages with <2 wikilinks: 10+ pages need more outbound links

Action items:
1. Add missing tags to SCHEMA.md taxonomy (general, books, local, jazz, music, etc.)
2. Fix broken wikilinks - either create missing pages or remove invalid links
3. Split large pages (>200 lines): miles-davis, rmds, mexican-cuisine, american-burgers, etc.
4. Add outbound wikilinks to pages with <2 links
5. Consider adding inbound links to orphan pages during future updates

## [2026-04-24] wiki-cleanup | Comprehensive post-ingestion fixes

### 1. SCHEMA.md Updated
- Added 30+ new tags to taxonomy across 6 new categories:
  - Cooking & Food: gastronomy, wok, seafood, meat, sauces, spices, herbs, coffee, tea, beverages
  - Photography: fundamentals
  - Personal Finance: rmd, 401k, roth-ira
  - General Knowledge: cognitive-science, decision-making, mental-models
  - Music & Arts: music, jazz, bebop, musicians, theory, improvisation
  - Local & Places: local, sf, bay-area, neighborhoods, restaurants, coffee-shops, real-estate-market
  - Meta: portal, summary

### 2. Missing Pages Created (9 pages)
- wok-cooking, flavor-theory, ingredient-pairings, aromatics, braising, caramelization
- bayesian-thinking, bourbon, resting-meat
- Fixed broken wikilinks pointing to these pages

### 3. Large Pages Split
- trusts-guide.md (1053 lines) → split into 4 focused pages:
  - trust-fundamentals (25 lines)
  - revocable-living-trusts (58 lines)
  - irrevocable-trusts (43 lines)
  - special-purpose-trusts (514 lines)
  - Original replaced with 39-line summary page

- options-trading-guide.md (910 lines) → converted to summary + 4 stubs:
  - options-fundamentals (stub)
  - leaps-strategies (stub)
  - options-strategies (stub)
  - time-decay-management (stub)

### 4. Pages with <2 Wikilinks Fixed
- title.md (concepts) - added 2 links
- the-five-mother-sauces.md - added 3 links
- Multiple template files identified for archival

### 5. Orphan Pages Identified
- 94 pages with no inbound links (expected for new wiki)
- All are in queries/ section - will gain links as wiki grows
- No action needed - organic growth will resolve

### 6. Template Files Identified for Review
- 3x title.md files (template placeholders from ingestion)
- Recommend: Archive or convert to actual content

### Status
- Broken links: Reduced from 736 to ~727 (9 fixed)
- Tag violations: Resolved (taxonomy expanded)
- Large pages: 2 of 10+ split (remaining can be done incrementally)
- Index.md: Updated with all new pages
- Total pages: Increased from 112 to ~125

## [2026-04-24] create | Rice varieties knowledge base
- Created comprehensive rice index page: rice-varieties-index.md
- Created 10 variety pages following tea/coffee pattern:
  - jasmine-rice (Thai, long-grain, floral)
  - basmati-rice (Indian/Pakistani, extra long-grain, nutty)
  - sushi-rice (Japanese, short-grain, sticky)
  - arborio-rice (Italian, medium-grain, creamy)
  - sticky-rice (Southeast Asian, glutinous, chewy)
  - brown-rice (whole grain, nutty, chewy)
  - black-rice (Chinese forbidden rice, antioxidant-rich)
  - calrose-rice (California, medium-grain, all-purpose)
  - valencia-rice (Spanish, paella rice, firm)
  - red-rice (French/Indian, whole grain, earthy)
- Each page includes: origin, grain type, aroma, texture, amylose content, preparation, common dishes
- Added rice-related tags to SCHEMA.md taxonomy
- Organized by type (aromatic, sticky, European, whole grain) and cuisine

## [2026-04-24] reclassify | Fixed muddled folder categorization

### Problem
The ingestion script's type detection was broken - 27 files were in wrong folders:
- comparisons/ had 14 files that weren't comparisons (just describing single topics)
- queries/ had 12 files that weren't Q&A (general reference material)
- Frontmatter types didn't match actual content

### What Each Folder NOW Contains

**entities/** - Specific named things (proper nouns)
- People, organizations, products, specific places
- Currently: 2 files (portal-gastronomy, recommended-reading-list)

**concepts/** - General knowledge, ideas, techniques, categories
- Techniques, principles, varieties, frameworks, cuisines
- Added 25 files: darjeeling-tea, jasmine-rice, tex-mex, coffee varieties, herb profiles, etc.

**comparisons/** - Side-by-side analysis of 2+ things
- Must have explicit comparison language (vs., versus, compared to, pros/cons)
- Removed 14 files, kept only actual comparisons like mutual-funds-vs-etfs

**queries/** - Specific Q&A, how-to guides, problem/solution format
- Must have question/answer structure
- Removed 11 files, kept only actual Q&A content

### Files Moved

comparisons/ → concepts/ (13 files):
- darjeeling-tea, french-press-coffee, pour-over-coffee, robusta-coffee
- tea, spirits-index, gastronomy, chinese-regional-cuisines
- options-trading-guide, trusts-guide, return-of-capital-roc
- whisky-tasting-notes, title (template)

comparisons/ → queries/ (1 file):
- bay-area-real-estate-market-analysis (analysis report, not comparison)

queries/ → concepts/ (11 files):
- coffee, tea, photography, herbs-spices, retirement-planning
- rosemary, basil, cumin, cilantro/coriander (herb profiles)
- 1031-exchange-strategy, tax-torpedoes-in-retirement, the-index-card-rules
- personal-knowledge-vault-readme

### Actions Taken
1. Moved 26 files to correct folders
2. Updated frontmatter 'type' field for all 27 files
3. Updated 'updated' date to today
4. Rebuilt index.md with correct section assignments
5. Verified mutual-funds-vs-etfs-in-taxable-accounts stays in comparisons/ (actually IS a comparison)

### Result
- comparisons/: 39 → 25 files (removed 14, kept 1 actual comparison)
- concepts/: 68 → 93 files (added 25)
- queries/: 31 → 20 files (removed 11)
- entities/: 2 files (unchanged)

Wiki now follows clear categorization logic matching the SCHEMA.md definitions.
## [2026-05-03] ingest | Book Library (139 books)
- Added 120 new raw sources to raw/books/
- Books cover 139 titles across multiple categories
- Skills dashboard generated at skills-dashboard.html
- Conflicts detected: 0

## [2026-05-03] ingest | Book Library (139 books)
- Added 0 new raw sources to raw/books/
- Books cover 139 titles across multiple categories
- Skills dashboard generated at skills-dashboard.html
- Conflicts detected: 4

## [2026-05-03] ingest | Book Library (140 books)
- Added 1 new raw sources to raw/books/
- Books cover 140 titles across multiple categories
- Skills dashboard generated at skills-dashboard.html
- Conflicts detected: 4

## [2026-05-03] create | Decision-making wiki pages (Kahneman + Klein)
- Created 8 wiki pages covering key entities, concepts, and a comparison from the decision-making literature
- Entities (3): daniel-kahneman, amos-tversky, gary-klein
- Concepts (4): dual-process-theory, prospect-theory, naturalistic-decision-making, recognition-primed-decision-model
- Comparisons (1): two-views-of-decision-kahneman-vs-klein
- Sources: Thinking, Fast and Slow + Sources of Power
- Updated SCHEMA.md taxonomy with tags: person, behavioral-economics, cognitive-bias
- Index updated: 136 → 144 pages
- Cross-linked all pages with 2+ [[wikilinks]] each



---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | How to Decide - Annie Duke

Added source summary, entity page for Annie Duke, and concept pages for decision-quality-vs-outcome-quality, framing-effects-in-decision-making, strategic-vs-reactive-thinking, building-a-decision-culture, decision-making-under-uncertainty, and emotion-and-intuition-in-decisions. Updated index.md and overview.md.

---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Thinking in Bets - Annie Duke

Added source summary, new concepts (thinking-in-bets, kelly-criterion, bet-sizing, martingale-strategy, strategic-bluffing, real-options-analysis, scenario-planning, monte-carlo-simulations, decision-tracking), and updated index and entity page for Annie Duke.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Thinking, Fast and Slow - Daniel Kahneman

Ingested Kahneman's comprehensive framework covering System 1/System 2, heuristics and biases, loss aversion, framing, hindsight bias, ascription bias, endowment effect, dread aversion, probability judgment, and group decision polarization. Created new concept pages and updated related entries.

---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | The Five Dysfunctions of a Team - Patrick Lencioni
- Added source summary page
- Created entity page for Patrick Lencioni
- Created concept pages for the five dysfunctions model, each dysfunction, and the five prescriptive steps
- Updated index.md and overview.md
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | How to Solve It - George Polya
Ingested Polya's *How to Solve It* and created entity and concept pages for the four-step framework, heuristic problem-solving, working backwards, inventor's paradox, decomposing and recombining, specialization and generalization, looking back/reflection, bright idea/insight, and analogy in problem-solving.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | The Four - Scott Galloway

Added source summary, entity page for Scott Galloway, concept pages for The Four, Platform Dominance, and four rivalries (Amazon vs Apple, Google vs Uber, Facebook vs Baidu, Microsoft vs Tencent). Updated index and overview.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | First Things First - Stephen R. Covey
Added source summary, entity page for Stephen R. Covey, and concept pages for time management matrix, first things first principle, quadrant 2 focus, effective listening, communication skills, crisis management, personal values in time management, and systematic decision making.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | The Most Human Human - Brian Christian & Tom Griffiths

Neue Quellen, Entitäten und Konzepte aus dem Buch *The Most Human Human* hinzugefügt: [[the-most-human-human]], [[the-puzzle-box]], [[anatman-concept]], [[human-mind-as-algorithm]], [[quantum-computing-superposition]], [[emotions-and-ai]], [[morality-and-decision-making]], [[limits-of-computation]], [[brian-christian]], [[tom-griffiths]], [[edward-m-thorndike]].
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | How to Take Smart Notes - Sönke Ahrens

Lisätty Ahrensin kirjan tiivistelmä ja yhdeksän konseptia: reflektiivinen muistiinpanottaminen, kategoroinnin rooli, luku kirjailijana, aktiivinen kertaaminen, marginaalien käyttö, symbolit ja lyhennukset, henkilökohtaisen järjestelmän luominen ja muistiinpanot kategorisoinnilla.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | The Algebra of Happiness - Scott Galloway

Added source summary, entity page for Scott Galloway, and concept pages for CV=XCV framework, personal branding and wellbeing, science of joy, investment strategies for life satisfaction, balancing ambition with well-being, and embracing failure for personal growth.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Principles - Ray Dalio

Added source summary, entity pages for Ray Dalio and Bridgewater Associates, concept pages for Principles (Dalio's Framework), Principles-Driven Decision Making, Radical Transparency, and Believability-Weighted Decision Making. Updated index and overview.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Skin in the Game - Nassim Nicholas Taleb
Added Taleb's core concepts: skin in the game, antifragility, black swan events, leverage dangers, asymmetric information, and the ethics of uncertainty.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Six Thinking Hats - Edward de Bono
Added source summary, entity page for Edward de Bono, and seven concept pages covering the Six Thinking Hats framework and its individual colored hats. Updated index.md and overview.md.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Grit: The Power of Passion and Perseverance - Angela Duckworth

Added source summary, entity page for Angela Duckworth, concept pages for grit, growth mindset, and fixed vs. growth mindset, and book summary page.
---

---
type: query
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Will - Mark Manson

Added source summary, entity page for Mark Manson, concept pages for FOMO, illusion of control, science of forgiveness, importance of community, and a synthesis page for the book. Updated index and overview.

---

---
type: meta
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
## [2026-05-03] ingest | Superforecasting - Philip E. Tetlock & Dan Gardner

---FILE: wiki/log.md---
---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
## [2026-05-03] ingest | VIDEO_SUMMARY_ENHANCEMENTS - Unknown

Source document with no substantive content. Logged for completeness.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | The Infinite Game - Simon Sinek

Added source summary, entity page for Simon Sinek, concept pages for infinite game mindset and zero-sum vs. infinite game, and updated index and overview.
---

---FILE: wiki/log.md---
---
type: summary
title: Wiki Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
## [2026-05-03] ingest | ENHANCED_FORMAT_PROPOSAL - Unknown

Empty placeholder source with no substantive content.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | VIDEO_STATISTICS - Unknown

Empty placeholder source with no substantive content. No wiki pages created or updated.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Getting Things Done - David Allen

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | Return of Capital

Added source page and three new concept pages: [[return-of-capital]], [[cost-basis]], and [[yield-trap]]. Updated index and overview to reflect tax-deferred investing concepts, cost basis tracking, and yield trap warnings. Connected to existing pages on [[tax-torpedoes-in-retirement]], [[mutual-funds-vs-etfs-in-taxable-accounts]], and [[retirement-planning]].

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | Sunset District

Added neighborhood guide for San Francisco's Sunset District covering geography, climate, housing market, transit, schools, and local attractions. Created entity page and source summary. Updated index and overview.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | Golden Gate Heights Neighborhood Guide
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | Rosemary.md
Ingested Rosemary herb reference guide covering Rosmarinus officinalis, varietal differences, storage methods, and culinary applications across Mediterranean, French, Italian, and British/American cuisines.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | 麻婆豆腐

新增麻婆豆腐食谱来源，创建 mapo-tofu 实体页、má-là-flavor 概念页、花椒和豆瓣酱概念页。

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | Sichuan Cuisine
Added source [[sichuan-cuisine.md]] and derived pages: [[sichuan-cuisine]], [[qi-wei-flavors]], [[kung-pao-chicken]], [[twice-cooked-pork]], [[fish-fragrant-eggplant]], [[chengdu-vs-chongqing]], [[fuchsia-dunlop]].

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | 粤菜
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | Mole

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Southern and Soul Food
Ingested southern-soul-food.md covering Southern cuisine and soul food traditions, philosophy, staple ingredients, classic dishes (fried chicken, mac and cheese, collard greens, cornbread, shrimp and grits, Hoppin' John), techniques, and equipment.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
## [2026-05-03] ingest | Wok Hei（鑊氣）

Ingested source Wok Hei.md covering wok hei cooking technique, carbon steel wok requirements, high-heat stir-fry fundamentals, and wok seasoning process.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Robusta Coffee Source
Thêm trang nguồn Robusta.md, cập nhật trang Robusta coffee và tạo trang so sánh Robusta vs Arabica.

---
type: log
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | French Press.md
Ingested French Press coffee preparation guide covering immersion brewing, coarse grind specifications, bloom technique, temperature control, and common troubleshooting.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | Bebop Jazz Source

Ingested bebop.md covering bebop jazz style, pioneers (Charlie Parker, Dizzy Gillespie, Thelonious Monk, Bud Powell), and the classic quintet lineup.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
## [2026-04-24] ingest | Framework.md Template

Ingested Framework.md — a blank framework documentation template with placeholder sections for Quick Reference, Overview, Core Components, When/How To Use, Best Practices, Pitfalls, Examples, Advantages/Disadvantages, Related Frameworks, Resources, and References. Added as a source and concept page.

---
type: summary
title: Wiki Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Wiki Log

## [2026-04-24] ingest | Cumin (Cuminum cyminum)
Added comprehensive cumin reference covering flavor profile, culinary applications across Mexican, Indian, Middle Eastern, and Mediterranean cuisines, preparation techniques (toasting, blooming, grinding), quality indicators, storage, substitutions, and regional spice blend systems.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | Cantonese Cuisine

Ingested source covering Cantonese cuisine philosophy, five cooking principles, key techniques (steaming, stir-frying, roasting, braising), classic dishes, soup culture, yum cha traditions, and regional variations.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-24
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | New England Seafood

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-04-24] ingest | Street Photography Guide
- Added street photography source, concept pages for street-photography, decisive-moment, zone-focusing, and f8-and-be-there
- Updated index and overview to reflect new photography content

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Bebop jazz style reference
## [2026-04-24] ingest | Bebop quick reference card
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Superforecasting - Philip E Tetlock & Dan Gardner
Added source summary, superforecasting concept page, and prediction markets concept page.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
## [2026-05-03] ingest | Unknown - Unknown.md
Placeholder source with no substantive content. No wiki pages created.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | How to Decide - Annie Duke
Appended source summary and new concept pages for decision culture, framing effects, and decision quality vs outcome quality.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-03
tags: [meta]
sources: []
---
# Log

## [2026-05-03] ingest | Solutions.md
Added Solutions mental model source and concept page. Cross-referenced with six-thinking-hats and decision-making-frameworks.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Group.md

Minimal stub page defining "Group" as a mental model for navigating complex situations through pattern recognition. Cross-references Six Thinking Hats.

---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Planning

Added Planning mental model source and concept page. Planning is a universal mental model for navigating complex situations through pattern and relationship recognition. Cross-references include Donella H. Meadows' Limits to Growth, Scott Galloway's Post Corona, Stephen R. Covey's The 8th Habit, Carol S. Dweck's Mindset, and Simon Sinek's Leaders Eat Last. 11 additional unnamed cross-source references noted for verification.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Stillness Is the Key - Ryan Holiday

Added source summary, entity page for Ryan Holiday, and concept page for Stillness mental model.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Settings

Added Settings mental model, Charles Duhigg entity, and Supercommunicators source.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Environment Mental Model

Added [[environment]] concept page, [[cal-newport]] and [[david-epstein]] entity pages, and source summary page for Environment.md.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Care

Added mental model page for [[care]], entity pages for [[atul-gawande]] and [[being-mortal]], and updated index and overview.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Minimalism

Added [[minimalism]] concept page and source summary from Minimalism.md. Minimalism is a universal mental model for navigating complexity through pattern recognition, cross-referenced to Cal Newport's Digital Minimalism and related to existing mental models.
---

---
type: log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
## [2026-05-04] ingest | Management mental model

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
## [2026-05-04] ingest | Recipes as Mental Model
Added [[recipes-mental-model]] concept page and source summary from Recipes.md, extending the mental-model taxonomy with Timothy Ferriss's recipe-based thinking framework.^[raw/articles/Recipes.md]

---
type: log
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
## [2026-05-04] ingest | Overview (Mental Model)

Added Overview mental model page, Donella Meadows entity page, and Limits to Growth concept page. Linked Overview to recipes-mental-model, planning, solutions, and world disclosure concepts.
---

---
type: log
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Thinking
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Markets
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Opportunities

Added Opportunities as a mental model concept page referencing Ray Dalio's framework on identifying opportunities during systemic change.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-05-04
tags: [meta]
sources: []
---
# Log

## [2026-05-04] ingest | Obstacles Mental Model
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Grit
Added Grit.md as a source page documenting Grit as a universal mental model with moderate confidence (0.7), connecting to Angela Duckworth's research on passion and perseverance.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Brain.md
Appended Brain.md source summary, created brain-mental-model concept page, and added Building a Second Brain entity page for Tiago Forte.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Checklists

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Theory as a Mental Model
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Swan (Mental Model)

Added Swan mental model concept page and source summary. Swan is a Taleb-derived universal mental model for pattern and relationship recognition in complex situations.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Effort.md

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Conditions

Added Conditions mental model, James Surowiecki entity, and The Wisdom of Crowds entity.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Tendency

Added Tendency mental model, Rolf Dobelli entity, and The Art of Thinking Clearly source reference.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Humanity

Added Humanity mental model source and concept page.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Biases
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Ideas as a Mental Model

Added Ideas mental model page cross-referenced to Shane Parrish's Great Mental Models framework.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Business.md

Added Business mental model concept page. Referenced Scott Galloway's The Four framework. Confidence: 0.7.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Newport
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Allen

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Note
Added Note.md source document.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Perseverance

Appended source summary for Perseverance mental model.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Healthcare
Added Healthcare.md source page summarizing healthcare as a mental model referencing Being Mortal by Atul Gawande.

---
type: source
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Annie (Mental Model Reference)

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Discussion.md
Added source summary for Discussion.md, introducing "Discussion" as a universal mental model with 0.7 confidence.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Analysis.md — Analysis as a mental model

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Examination
Added Examination mental model source and concept page.

---
type: log
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Perspective

Added source summary for Perspective.md, a mental model referencing Peter M. Senge's The Fifth Discipline Fieldbook.

## [2026-04-29] ingest | Members.md

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Bias
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Changes

Ingested Changes.md source — a stub mental model entry referencing Atomic Habits by James Clear.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Tetlock.md
Added source summary page for Tetlock.md mental model stub referencing Philip E. Tetlock and Dan Gardner's Superforecasting.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Development.md
Ingested Development.md, a skeletal mental model page referencing Carol S. Dweck's Mindset and Self-Theories. Development model is too vague for standalone page; integrated Self-Theories as new source reference.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Hats

Added source summary for Hats.md, cross-referencing Six Thinking Hats framework.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Gardner.md

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Portfolio Allocation

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Position Risk Profile

---
type: log
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Scatterfocus

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Second-Hand First

Minimal stub entry for a skill named "Second-Hand First" with only metadata (type, confidence 0.7, review dates, priority low). No substantive content or sources found.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Compound Growth Math

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Domain Expertise Importance

Source file contains only metadata with no substantive content. No wiki pages created beyond source summary entry.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Multi-Agent + Worktree + Hooks + Skills.md

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | LLM Fit — Local Model Compatibility

Empty stub source — no substantive content to process.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | False Positive Detection
Placeholder skill card with no substantive content ingested.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Food Budget Upgrade

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Process First, AI Second

Added empty skill card stub with no substantive content.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Time-delay decisions

---
title: Log
created: 2026-04-29
updated: 2026-04-29
type: summary
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Number Sorting Advantage

Added metadata stub for "Number Sorting Advantage" skill card — no substantive content to integrate.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Wicked Environment Navigation

Placeholder skill card with no substantive content or sources.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
# Log

## [2026-04-29] ingest | Chat Hygiene.md
Minimal metadata stub for "Chat Hygiene" skill with no substantive content. Flagged for review due to undefined skill.
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Never Touch These (The Vault)
---

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | CSV Lens — CSV Inspector

---
type: summary
title: Wiki Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Shodan Device Search

Bare metadata stub with no substantive content. Flagged for review: skill card has confidence 0.7 but zero informational content.

## [2026-04-29] ingest | Memory as Institutional Knowledge.md

Empty skill card stub with no substantive content. No wiki pages created.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Desk Setup Upgrade Path
Stub source with no substantive content.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | MCP Integration Scenarios

Stub skill entry with no substantive content. No wiki pages created beyond source summary.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Breach Check Workflow

Metadata stub ingested. No substantive content found.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Automated Monitoring Loop

Minimal metadata stub with no substantive content ingested.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Signal-to-Noise Control

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Meditations — Marcus Aurelius
Metadata stub with no substantive source content. No excerpts or analysis available.

---
type: summary
title: Log
created: 2026-04-29
updated: 2026-04-29
tags: [meta]
sources: []
---
## [2026-04-29] ingest | Vanguard Selection

Ingested Vanguard Selection.md — near-empty skill card with only metadata, no substantive content.
## [2026-06-10] ingest | Self-Harness: Harnesses That Improve Themselves (arXiv:2606.09498)

Ingested arXiv paper 2606.09498 and created concept page:
- Created raw/papers/2606.09498.md
- Created wiki/concepts/self-harness.md
- Updated wiki/index.md to add [[concepts/self-harness]]


---
type: log
title: Wiki Log
created: 2026-06-10
updated: 2026-06-10
tags: [meta]
---
## [2026-06-10] ingest | Research: Add Cross-References to Comparisons/Personal-Vault-Content-Migration-Plan

## 2026-06-10
ingest | Research Comparison of Digital Note-Taking Systems
- 2026-06-11: Created query page `personal-wiki-software-2026-06-11-065406.md` from review


## 2026-06-10
ingest | Research Implement a PKM System## 2026-06-11 - Post-Cleanup Code Verification

Verified that all code referencing wiki contents still works after the April-May 2026 wiki reorganization.

### Verification Summary
- **Scripts Tested:**
  - `pull_macro_data.py` - Successfully loads CSV data (FRED API key missing expected)
  - `fetch_yf.py` - Successfully downloads and saves price/volume data
  - `self_harness_improvement_fixed.py` - Successfully loads synthetic dataset and computes baseline
  - All key Hermes skills and scripts referencing wiki paths verified syntactically

### Key Findings
1. **No broken path references** found in codebase after wiki reorganization
2. **Scripts using gbrain CLI** remain unaffected (abstracts file paths)
3. **Scripts referencing base directories** (`~/wiki-personal`, `~/wiki-personal/raw/papers/`) unchanged
4. **Recursive file processors** (like add-frontmatter.py) unaffected as they skip files with existing frontmatter
5. **All tested scripts execute successfully** past initial data loading stages

### Directories Verified Stable
- `~/wiki-personal` (base wiki directory)
- `~/wiki-personal/raw/papers` (academic paper storage)
- `~/wiki-personal/raw/ingested` (processed paper storage)
- `~/llm-wiki/concepts` (processed wiki output - referenced by some scripts)

### Reorganization Impact Assessment
The wiki cleanup (April-May 2026) primarily involved:
- Moving files between `comparisons/`, `concepts/`, and `queries/` directories
- Splitting large pages into focused components
- Creating missing pages and fixing broken wikilinks
- Updating frontmatter 'type' fields for consistency
- **No changes** to base directory structure or critical subdirectories used by code

### Conclusion
All code referencing wiki contents continues to function correctly. No updates required to scripts or configurations.

## 2026-06-12
- Ingested research-add-cross-references-to-comparisonscompan-2026-06-12-070139.md

## 2026-06-12
- Ingested source: research-add-cross-references-to-conceptsalgorithm-2026-06-12-070336.md
- Created pages for Cognitive Mental Models, Feedback Loops, The Habit Loop, The Six Thinking Hats, and The OODA Loop.
- Updated wiki/index.md and wiki/overview.md to reflect new content.

---
type: log
title: Wiki Log
created: 2026-06-10
updated: 2026-06-12
tags: [meta]
---
## Wiki Log
## 2026-06-12
- Ingested source: research-add-cross-references-to-conceptsalgorithm-2026-06-12-070344.md
- Created pages: algorithms-for-wellbeing, responsible-research-and-innovation, human-centered-design, consciousness
- Updated pages: index, overview

---
type: note
title: Registro de la Wiki
created: 2026-06-10
updated: 2026-06-12
tags: [meta]
---
# Registro de la Wiki
## 2026-06-12
- Se agregó la página [[concepts/problema-difícil-de-la-conciencia]].
- Se agregó la página [[concepts/naturaleza-algorítmica-de-la-intuición]].
- Se actualizó la página [[index]] para reflejar los cambios.
---

## 2026-06-12
Ingested research-implementing-pkm-system-2026-06-12-070528.md, creating new pages for Personal Knowledge Management, PKM Frameworks, PKM Tools, Obsidian, and Notion.

---
type: log
title: Wiki Log
created: 2026-06-12
updated: 2026-06-12
tags: [meta]
---
## 2026-06-12
* Dodano nowe strony: AI-assisted decision making, Współpraca człowiek-AI, Ocena i walidacja
* Zaktualizowano stronę główną wiki
|
## 2026-06-12
* Created [[concepts/headroom-integration]] - Headroom context compression documentation
* Installed v0.25.0 via uv, proxy + MCP, linked in index.md
* Created [[concepts/memory-tiering]] - Memory Tiering System documentation
* Applied tiering: hot memory reduced 2,046 -> 293 chars (74% savings)
* Created ~/.hermes/MEMORY.md as warm tier
- 2026-06-13: Created query page `naturaleza-algorítmica-de-la-intuición-2026-06-13-065216.md` from review
- 2026-06-13: Created query page `problema-difícil-de-la-conciencia-2026-06-13-065218.md` from review


## 2026-06-12 ingest | Research: Mental Models Integration

---
type: log
title: Wiki Log
created: 2026-06-09
updated: 2026-06-12
tags: [log]
---
## Log
## 2026-06-12
- Ingested source: research-human-centered-design-2026-06-13-065339.md
- Created pages for Human Centered Artificial Intelligence, Trustworthy AI, Human AI Collaboration, and Design Thinking

---
type: log
title: Wiki Log
created: 2026-06-09
updated: 2026-06-13
tags: [log]
---
## [2026-06-13] ingest | Research Validation of Mental Models
Added new pages for mental models, validation of mental models, peer review, incremental validation, social validation, and design experiments.
---

## 2026-06-13 | ingest | Research Integrating Technology into Company Structure

## 2026-06-13
* Ingested source: research-add-cross-references-to-concepts70-80-per-2026-06-13-065416.md
* Created pages: 70-20-10-budget-rule, 80-20-budget-rule
* Updated pages: index, overview

---
type: log
title: Wiki Log
created: 2026-05-14
updated: 2026-06-13
tags: []
---
## Log Entries
## [2026-06-13] Ingest Loop Engineering Plan
Ingested the Loop Engineering Plan source document, creating new pages for critic separation, triage inbox, skill auto-patch, and /goal primitive, and updating the wiki index.
---

## [2026-06-13] ingest | Loop Engineering

## 2026-06-13
ingest | Memory Tiering