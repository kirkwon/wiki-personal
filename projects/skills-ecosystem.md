title: Skills Ecosystem (Book Dashboard + Hermes Library + Auto-Generation)
status: active
priority: P1
created: 2026-06-28T00:00:00.000Z
updated: 2026-06-28T00:00:00.000Z
---

# Skills Ecosystem

## Summary
Three interconnected skill systems: (1) **Book Skills Dashboard** — interactive HTML visualization of 303 skills/concepts from 33 books with D3.js network graphs, (2) **Hermes Skills Library** — 320 installed Hermes agent skills across 20+ categories, (3) **Skill Auto-Generation** — research into mining SKILL.md files from interaction trajectories.

## Progress

### Book Skills Dashboard
- [x] Original dashboard built — 303 skills, 152 tags, 13 overlaps, 243 multi-tag skills
- [x] D3.js network visualization (force-directed graph, top 30 tags)
- [x] Tabbed interface: All Skills, All Tags, Overlaps, Multi-Tag, Network View
- [x] `book-skills-dashboard` Hermes skill v1.2.0 (4 data pipelines)
- [x] Wiki ontology pipeline (newest) — live CLI from 4,690-page vault
- [x] Spec document at `~/clawd/skills-dashboard-spec.md`
- [x] Multiple HTML versions in wiki backups (v5.0, v6.0)
- [ ] Live dashboard needs regeneration from current wiki state
- [ ] Dashboard not linked from project dashboard

### Hermes Skills Library
- [x] 320 skills installed across `~/.hermes/skills/`
- [x] 20+ categories: finance, devops, creative, mlops, research, etc.
- [x] `hermes skills` CLI available (basic listing)
- [x] 45 skills with Google Workspace integration
- [x] 7 skills with NotebookLM bridges
- [ ] No interactive dashboard for Hermes skill library
- [ ] No health/coverage analysis (orphaned, duplicate, stale skills)

### Skill Auto-Generation Research
- [x] Paper captured: "Automating SKILL.md Generation via Trajectory Mining" (NeurIPS 2026)
- [x] GBrain connections made (8 links to SDAR, BINEVAL, Self-Harness)
- [x] `skill-from-masters` skill built (practice-first research layer)
- [x] `skill-creator` skill available
- [ ] No automated skill auditing (mine 320 skills for gaps/dupes)

## Next Steps
1. Regenerate book skills dashboard from live wiki ontology
2. Build Hermes skills inventory dashboard (categories, counts, health metrics)
3. Run skill gap detection (find repeated patterns with no corresponding skill)

## Key Files
- `~/clawd/skills-dashboard-spec.md` — full spec (352 lines)
- `~/.hermes/skills/productivity/book-skills-dashboard/SKILL.md` — dashboard skill v1.2.0
- `~/Downloads/10-projects/10-active-projects/wiki-tools/` — live wiki CLI pipeline
- `~/.zeroclaw/workspace/skills_visualization.html` — original working dashboard (6,497 lines)
- `~/wiki-personal/_raw/automating-skill-md-generation-cua.md` — paper capture
- `~/.hermes/skills/research/skill-from-masters/` — practice-first skill creation

## Automation / Cron
- None currently — dashboard generation is manual

## Blockers
- Live wiki pipeline (`wiki_api.py` + `cli.py`) needs verification — may need wiki vault sync
