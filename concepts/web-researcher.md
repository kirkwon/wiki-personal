---
date: 2026-07-19
type: concept
title: Web Researcher
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- research
- web-search
- synthesis
- citation
- deep-dive
sources:
- hermes://skill/web-researcher
description: Structured deep-dive web research with query analysis, multi-source search,
  content extraction, quote-backed findings, and gap identification. Designed for
  investigating unfamiliar topics with provenance.
---

# Web Researcher

> Structured deep-dive web research with query analysis, multi-source search, content extraction, quote-backed findings, and gap identification. Designed for investigating unfamiliar topics with provenance.

## Overview

- **Parameters** — | Parameter | Required | Default | Description | |-----------|----------|---------|-------------| | `topic` | ✅ | — | The research topic or question | | `source_type` | ❌ | `documentation` | Type of sources: `documentation`, `tutorials`, `solutions`, `comparisons`, `news`, `papers` |
- **Summary** — {2–3 paragraph answer to the main question}
- **Sources Used** — | Source | URL | Relevance | Date | |--------|-----|-----------|------|

## Further detail

### Gaps & Limitations

- {What the research couldn't determine} - {Conflicting information} - {Areas needing further investigation}

### Prompt Architecture Notes

- **C4 Absent self-model (routing):** Search depth is underdetermined by the query. Don't "decide" how many sources to pull — match a number. 1 fact → 2-3 sources; medium comparison → 5-8; deep investigation → 10-15. When unsure, search more — the model cannot reliably self-assess "is this enough." - **C1 Confabulation equilibrium:** NEVER fabricate URLs, attributions, or quote text. If a source can't be verified, omit it. "Phantom citations" — URLs that look real but don't resolve — are the highest-cost failure in research. Every quote must trace to a fetched page, not a plausible reconstruct

### Pitfalls

- **Source recency matters** — for fast-moving tech (AI/ML, frontend frameworks), prefer sources <6 months old. Flag older sources explicitly. - **LLM overview pages** — many top search results are AI-generated overviews with no original content. Prefer primary sources: official docs, GitHub repos, author blogs, peer-reviewed papers. - **Surface-level coverage** — if your search only returns introductory articles, note this and try more specific queries with technical jargon. - **No single source is authoritative** — cross-reference claims between at least 2 independent sources before reportin

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/web-researcher/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
