---
type: concept
title: Gbrain Health
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Gbrain Health

> Check orphans, broken links, and run GBrain doctor.

## Overview

- **When to Use** — - **Weekly health checks**: Sundays 10:00 AM (cron-scheduled) - **After major content additions**: Validate vault integrity - **When GBrain feels slow**: Diagnose orphan/broken link bloat
- **Sampling for Speed** — Large vaults (thousands of files) would timeout if scanned fully. The script uses sampling:
- **Thresholds** — **Critical issues** (exit 1): - Broken links: >10 in sampled files

## Further detail

### Pitfalls (learned 2026-08-16, expanded 2026-08-30)

- **Vault root**: `BRAIN_DIR` must be `~/brain` (the live `wiki` source). `~/gbrain` is the gbrain *source repo* — scanning it reports repo docs, not vault state. Confirm with `gbrain sources list`. - **False-green health scripts**: A script can report "✅ Healthy" while measuring the wrong surface — e.g. git status of `~/gbrain` (source repo) instead of `gbrain doctor --fast --json` against `~/brain` (vault). Spot-check by running the script AND the real tool side by side. See `references/false-green-health-checks.md`. - **Subshell counters**: never increment a counter inside `cmd | while read

### Related Files

- `~/.hermes/scripts/gbrain-enhanced-health-check.sh` - Main health script - `~/.hermes/scripts/gbrain-weekly-health-wrapper.sh` - Legacy wrapper (calls standard check + dashboard gen) - `~/.hermes/scripts/generate-gbrain-dashboard.py` - Dashboard generator - `references/false-green-health-checks.md` — when a health script reports "✅" but measures the wrong surface (e.g. git status of source repo instead of `gbrain doctor` against the vault)

### Standard Health Check vs Enhanced

- **Standard** (`gbrain doctor --fast`): Quick health snapshot - **Enhanced**: Adds duplicate/orphan/broken-link/tag checks - **Run sequence**: Standard first (fast), then enhanced if standard passes

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/gbrain-health/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[gbrain-health-dashboard]]

[[gbrain-timeline-enrichment]]
