------

# Gbrain To Notebooklm

> Selective migration from GBrain to NotebookLM for research synthesis. Cleans GBrain pages (remove YAML frontmatter, convert wikilinks) and adds them to NotebookLM for deep research. Integrates with query-escalation-pipeline.

## Overview

- **When This Skill Activates** — Use this skill when the user: - Wants to research a topic using NotebookLM with GBrain sources - Says "add GBrain pages to NotebookLM" or "migrate to NLM" - Is escalating from Tier 1 (GBrain) to Tier 2 (NotebookLM) in the query pipeline - Wants to prepare GBrain content for NotebookLM synthesis - Mentions cleaning GBrain pages for NotebookLM - Wants to research a **cross-cutting topic** that spans skills + GBrain + files (multi-source survey) - Mentions cleaning GBrain pages for NotebookLM - Wants to research a **cross-cutting topic** that spans skills + GBrain + files (multi-source survey) -
- **Multi-Source Survey Pattern (2026-06-18)** — For cross-cutting topics that span multiple source types (skills, GBrain, files, queue entries), use the **multi-source survey** pattern instead of single-page migration. See `references/multi-source-survey-pattern.md` for the full workflow, including the `clean_and_add()` and `add_gbrain_source()` shell functions.
- **Cleaning Script** — Save this as `scripts/clean_for_notebooklm.py` in the skill directory:

## Further detail

### Integration with Query Escalation Pipeline

This skill is the **bridge** between Tier 1 (GBrain) and Tier 2 (NotebookLM) in `query-escalation-pipeline`.

### Batch Migration Command

For convenience, here's a one-shot command:

### Pitfalls

- **NotebookLM quota limits** — Designed for ~40-80 sources per deep research. Don't migrate 2,000+ pages. - **YAML frontmatter blocks rendering** — Sources appear blank if YAML isn't removed. Always clean before adding. - **Wikilinks don't work** — `[[link]]` format is not recognized. Convert to plain text or `[text](url)`. - **Session expires ~20min** — If `nlm` commands fail with auth errors, run `nlm login`. - **Empty research results** — If `nlm research start` returns `no_research`, check that sources are actually readable in NotebookLM web interface. - **Don't bulk import** — This skill

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/gbrain-to-notebooklm/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[notebooklm-research-pipeline]]
