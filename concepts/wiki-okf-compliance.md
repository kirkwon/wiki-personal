---
type: concept
title: Wiki Okf Compliance
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Wiki Okf Compliance
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- okf
- wiki
- frontmatter
- descriptions
- index-manifest
- gbrain
- knowledge-management
sources:
- hermes://skill/wiki-okf-compliance
description: Make a markdown wiki compatible with Google's Open Knowledge Format (OKF)
  — normalize type taxonomy, backfill descriptions, generate bundle manifests, and
  validate against the spec.
---

# Wiki Okf Compliance

> Make a markdown wiki compatible with Google's Open Knowledge Format (OKF) — normalize type taxonomy, backfill descriptions, generate bundle manifests, and validate against the spec.

## Overview

- **Overview** — Google's **Open Knowledge Format (OKF)** is a vendor-neutral spec for storing organizational knowledge as a directory of markdown files with YAML frontmatter. It's designed to be consumed by AI agents directly — no API, no SDK, no database required.
- **Key OKF Concepts** — | Concept | OKF Spec | Your Wiki | |---------|----------|-----------| | **Bundle** | Directory tree of `.md` files | `~/wiki-personal/wiki/` | | **Concept** | One `.md` file = one unit of knowledge | `concepts/`, `entities/`, etc. | | **Type** | Only required frontmatter field | `type: concept`, `type: entity`, etc. | | **Title** | Strongly recommended | `title:` in most files | | **Description** | Strongly recommended | ~89% backfilled from body text | | **Manifest** | `index.md` per directory | Generated — one per top-level dir | | **Cross-links** | Bundle-relative paths (`/tables/users.md`)
- **OKF Compliance for Scaffolded Projects (GraphWork)** — OKF compliance isn't only for the main wiki vault — scaffolded GraphWork projects (`~/clawd/NN.ProjectName/`) should also be OKF-compliant. These projects feed into gbrain and the knowledge graph, so missing frontmatter creates the same gaps.

## Further detail

### Remaining Gaps

| Gap | Status | Impact | |-----|--------|--------| | `log.md` | Not created | Low — changelogs are rare in practice | | Cross-link format | Wikilinks vs bundle-relative paths | Medium — OKF expects `/foo/bar.md` not `[[bar]]` | | Type registry enforcement | No validation in write pipeline | Low — manual review sufficient for now | | Stray `---` in body (vault ingestion artifact) | ~30-50 files | Low — cosmetic, YAML parses despite stray doc separator | | Descriptions for stubs with no body text | ~376 files | Low — will fill when stubs get content |

### Scripts

- `scripts/okf-project-audit.py` — OKF compliance audit for scaffolded GraphWork projects. Scans all .md files, reports missing type/title/description, and can auto-fix with `--fix` flag using predictable type mapping for scaffolded files. - `scripts/okf-audit.py` — Audit script: reports type taxonomy, missing fields, directory coverage - `scripts/okf-implement.py` — Combined implementation: type normalization + description backfill + index.md generation - `scripts/fix-import-artifacts.py` — Fix import artifact titles: Greek finance terms → English, Polish/Spanish auto-translates, `{{title}}`

### References

- `references/okf-implementation-session-2026-06-16.md` — Full session log: research, multi-phase fix, and implementation details - `references/okf-spec-notes.md` — Condensed notes from OKF v0.1 SPEC.md: bundle structure, frontmatter requirements, cross-linking semantics, design principles (vendor-neutral, producer/consumer independence, format-not-platform) - `references/okf-community-reception-2026-06-16.md` — last30days research results: Reddit threads, HN discussion (76 pts), 32 GitHub repos (3K stars top), 14 editorial articles, YouTube content, community sentiment analysis

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/wiki-okf-compliance/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
