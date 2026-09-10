---
date: 2026-08-02
type: concept
title: Dojo State File Maintenance
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/dojo-state-file-maintenance
description: 'Maintain the three Dojo JSON state files: deduplicate the fix queue,
  reclassify stale learned patterns, and reset circuit breakers. Complements dojo-circuit-breaker-triage
  (which covers circuit-breakers.json only).'
---

# Dojo State File Maintenance

> Maintain the three Dojo JSON state files: deduplicate the fix queue, reclassify stale learned patterns, and reset circuit breakers. Complements dojo-circuit-breaker-triage (which covers circuit-breakers.json only).

## Overview

- **When to Use** — - Dojo report shows the same recommendations as yesterday (queue not draining) - Fix queue has >15 entries (usually means duplicates across runs) - Learned patterns show high counts for items you've already resolved - Circuit breakers are stuck open/half-open after a fix was applied - You're doing a periodic Dojo cleanup (weekly or after a dojo-eval run)
- **The Three State Files** — | File | Purpose | Problem | Maintenance Action | |------|---------|---------|-------------------| | `~/.hermes/dojo-eval/circuit-breakers.json` | Tool failure tracking | Stale open/half-open circuits after fix | Reset to closed, add notes | | `~/.hermes/dojo-eval/fix-queue.json` | Fix recommendation queue | Duplicates accumulate every run without draining | Deduplicate by (tool, action), resolve/reclassify | | `~/.hermes/dojo-eval/learned_patterns.json` | Error pattern history | Resolved patterns keep high counts, triggering false recommendations | Zero counts, add reclassification metadata |
- **Model-Level Retry Loops vs Skill Bugs** — This is the most common misclassification. The Dojo detects "retry loops" (same tool called multiple times in a session) and recommends patching skills. **Most retry loops are model-level behavior:**

## Further detail

### Common False Positives (2026-07-22 Session)

| Tool | "Failure" | Actual Cause | Correct Classification | |------|-----------|-------------|----------------------| | `browser_vision` | 400 error (code 1210), 28 consecutive fails | Vision API rejecting low-quality/too-small images | Image quality, not tool bug | | `vision_analyze` | 400 error, same root cause | Same as browser_vision | Image quality | | `tool_describe` | "not a deferrable tool" × 15 | Model calling tool_describe on directly-available tools | Usage error | | `memory` | "content is required for 'replace' action" | Model omitting required parameter | Usage error | | `skill_m

### Pitfalls

- **Don't reset a circuit breaker before verifying the tool works.** Always call the tool directly first. If it fails, fix the root cause. - **The fix queue is append-only by design.** The Dojo never removes entries — it only adds. Without periodic deduplication, it grows unboundedly. - **Learned pattern counts are cumulative.** They never decrease on their own. A pattern seen 115 times will keep generating recommendations even after the root cause is fixed, unless you zero the count. - **Plan files accumulate too.** Each fix-router run writes 8-10 `.md` files. After a week, that's 50-70 files

### Automation

A one-shot triage script is available at `scripts/triage_dojo.py`. Run it for the full cleanup (dedup + reclassify + reset) in one pass:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/dojo-state-file-maintenance/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
