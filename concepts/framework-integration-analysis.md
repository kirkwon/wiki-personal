---
date: 2026-07-19
type: concept
title: Framework Integration Analysis
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Frameworks
- Integration
- Orthogonal-Axis
- Knowledge-Synthesis
- Decision-Routing
- knowledge-management
sources:
- hermes://skill/framework-integration-analysis
description: Map frameworks onto systems via orthogonal axis analysis.
---

# Framework Integration Analysis

> Map frameworks onto systems via orthogonal axis analysis.

## Overview

- **When to Use** — - User proposes a new framework/lens and says it "might fit into" or "could help" an existing system - You have a working system with 2+ routing/decision axes and want to know if a framework adds a new dimension - User mentions two frameworks and you need to determine if they compete or complement - After building a system, a user suggests additional "lenses" to consider - You need to synthesize multiple decision/analysis frameworks into one coherent routing layer
- **Prerequisites** — - `gbrain` CLI installed and working (`gbrain query` / `gbrain capture --file`) - `nlm` CLI if syncing to NotebookLM notebooks - Target system must have an existing skill or doc you can `skill_view` (you need to know the current axes before you can find a new orthogonal one)
- **How to Run** — Frame the work through Hermes tools: `web_extract` for authoritative framework sources, `skill_view` to load the target system, `write_file` to draft the integration doc, `terminal` for gbrain/nlm ingestion. No scripts needed — this is an analytical workflow, not a pipeline.

## Further detail

### Pitfalls

- **Treating frameworks as competing:** The most common error. Cynefin vs Bayesian funnel is a false dichotomy — they answer different questions. Always test for orthogonality before deciding to integrate or reject. - **Adding an axis that overlaps:** If the framework's question substantially overlaps an existing axis, merge findings into that axis instead of creating routing ambiguity. - **Skipping the gap-finding step:** Without identifying what the framework reveals as missing, the integration is just documentation, not an upgrade. The gap is the leverage point. - **Vague cross-links:** gbr

### Verification

The integration page should appear at >0.9 relevance with the target system's pages in the top results. If the new page doesn't connect to the target, the cross-links in frontmatter are wrong — fix the `links:` list and re-capture.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/framework-integration-analysis/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
