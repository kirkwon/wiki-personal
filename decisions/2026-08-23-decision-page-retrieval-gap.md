---
date: '2026-08-23'
type: note
status: committed
tags:
  - gbrain
  - decision
  - retrieval
  - gbrain-decide
supersedes: none
---

# Decision: Fix decision-page retrieval gap in gbrain (one-shot, cheap)

## Decision Frame
gbrain's DB reports 4 pages typed `type: decision`, but `gbrain list --type decision` returns nothing. At least one decision page is retrievable via semantic query (`gbrain query`), so the pages exist — they're just not listable by type. Fix the type-based retrieval path in one shot rather than leaving the gap open. The `gbrain-decide` skill's Phase 1.3 rule #1 ("decision pages outrank topical stubs") depends on this working.

## Options Considered
- **A) Do nothing** — `gbrain query` can still find decision pages semantically; the gap only affects type-based filtering. Cost: every `gbrain-decide` invocation that wants to boost decision-type pages can't, and the skill's primary ranking rule stays toothless.
- **B) One-shot fix** — investigate root cause (type-filter bug, soft-deleted pages, frontmatter parsing edge case) and patch or work around it. If a workaround path exists (e.g., `gbrain search "type: decision"` or `gbrain list --tag decision`), use that in the skill. Cost: one afternoon. Risk: if no fix works, status quo unchanged.
- **C) Full retrieval overhaul** — rejected. The 20-question eval showed retrieval works fine for decision queries otherwise; this is a narrow type-filter gap, not a retrieval problem.

## Chosen: B
One-shot investigation + fix or workaround. Targeted, bounded, reversible.

## Reasoning
Kirk's pattern from the cron-process-fidelity decision (2026-09-05): when a silent-process-failure mode is identified (green jobs that do no work, or decision pages that exist but can't be surfaced), prefer a targeted low-cost fix over a full rewrite, and document the pre-mortem. This gap is the same shape — a process failure (decision pages present but not listable by type), not an outcome failure (the pages are in the DB).

The GBrain Knowledge Ecosystem project page lists GAPs 1, 4, 7 as open but does NOT list this gap — meaning it wasn't on the radar. That's a blind-spot signal, not a "doesn't matter" signal.

## Next Steps
1. Run `gbrain list --include-deleted --type decision` to test if the 4 pages are soft-deleted.
2. Run `gbrain search "type: decision"` to test if keyword search surfaces them.
3. Run `gbrain list --tag decision` to test if tag-based filtering works.
4. If one of the above works, wire it into `gbrain-decide` as the retrieval path.
5. If none work, re-ingest or re-type the 4 decision pages so they're listable.
6. Update `gbrain-decide` SKILL.md if the retrieval path changes.
7. Add this gap to the GBrain Knowledge Ecosystem GAP list if still open after investigation.

## Pre-mortem (assume this failed in 3 months — why?)
1. **The gap is actually a non-issue** — `gbrain query` finds decision pages well enough and the type filter is a convenience that doesn't matter in practice. If true, document that and move on.
2. **The fix reveals a deeper problem** — e.g., multiple custom types have broken filters, not just `decision`. If so, scope the fix to decision type only; don't boil the ocean.
3. **The 4 decision pages are unrecoverable** — deleted, corrupted, or otherwise inaccessible. If so, the corpus has a decision-page hole; create new ones from this decision.

## Review Trigger
Next gbrain-decide invocation that wants to rank decision pages — if the retrieval path works, this decision is done. If not, revisit.

**Process check:** Decision based on measured eval results (20-question retrieval eval passed) + a concrete observed failure (`list --type decision` returns nothing). Not an outcome bias. Written before any fix attempt.
