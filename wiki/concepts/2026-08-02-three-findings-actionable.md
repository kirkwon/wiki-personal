---
type: analysis
title: Three NLM-Synthesized Findings — Aug 2026 Actionability Assessment
date: '2026-08-02T00:00:00.000Z'
source: 'NotebookLM aiml-analysis export (67K chars, 187 sources)'
status: active
ingested_via: put_page
ingested_at: '2026-08-02T21:29:26.006Z'
source_kind: put_page
tags:
  - actionable
  - dojo
  - nlm-synthesis
  - p5
  - retrieval
created: 2026-08-02
source: brain/ (retired 2026-09-13)
---
# Three Findings From Today's NLM Export — Are They Actionable?

## Finding 1: Single-Layer RL Suffices

**Claim:** Training just one middle transformer layer can recover most gains of full-parameter RL post-training, sometimes surpassing it.

**Relevant to:** P5 (Reasoning Models & Skill→LoRA Pipeline)

**Already in brain:** `papers/2607.01232` ("Is One Layer Enough?"), `papers/2604.05336` (TRACE — trains LoRA per capability)

**Actionable? YES — but changes the P5 thesis.**

Current P5 assumption: skills → LoRA adapters, one per skill domain.
New implication: instead of full fine-tuning or even broad LoRA, target a **single middle layer** per skill. This is dramatically cheaper (1/32 the parameters for a 32-layer model) and may be more effective.

**Concrete action:**
- P5 experiment design should include a "single-layer LoRA" arm vs full LoRA
- If confirmed, this collapses the compute budget by ~30x — could run on consumer hardware
- Connects to Brainstacks paper (frozen MoE-LoRA stacks) — middle-layer targeting may be why frozen stacks work

---

## Finding 2: Intrinsic Self-Correction Without External Grounding Does Not Work

**Claim:** Self-critique loops without an oracle or verifiable reward consume tokens without improving accuracy. Sometimes degrades below first-pass.

**Relevant to:** Dojo-eval, information-effectiveness-evaluator, dual-model-critique

**Already in brain:** `2026-07-22-can-llms-correct-themselves` (Tie et al 2025, already ingested with full analysis)

**Actionable? YES — and we're partially violating it.**

The dojo-eval system uses self-critique loops in several places:
1. Knowledge-maintenance skill reviews its own work
2. The cron failure watchdog checks its own output
3. Symptom→fix matching uses the same model to both diagnose and verify

**Concrete action:**
- Audit dojo-eval for self-critique loops lacking external grounding
- Where verification exists (exit codes, file existence, gbrain doctor), ensure the verifier is a **different code path** than the executor
- The `verification-before-completion` skill already encodes this ("independent verification from a separate code path") — enforce it harder
- Dual-model-critique skill already exists but isn't used in cron pipelines — wire it in for high-stakes verification

---

## Finding 3: Knowledge Boundary Training — Agents Must Learn When NOT to Search

**Claim:** Blindly searching for external information injects noise and corrupts accurate internal knowledge. Agents must learn their own "knowledge boundary" — searching only for what they can't internalize.

**Relevant to:** Retrieval-reflex (gbrain), agent-reach, HF papers pipeline scoring

**Already in brain:** `concepts/hermes-agent-stack` documents the retrieval-reflex (zero-LLM entity resolution). But this finding says the reflex itself can be harmful.

**Actionable? PARTIALLY — the reflex is too aggressive right now.**

Current behavior: every named entity triggers a gbrain retrieval. This is good for grounding but bad when the agent already knows the answer — retrieval adds context noise.

**Concrete action:**
- Add a confidence gate before retrieval: if the entity appears in MEMORY.md or recent session context, skip retrieval
- The HF papers pipeline scoring (Q01-Q07) is a form of knowledge boundary — papers are only fetched if they score ≥3. But 0/50 processed for 3 days suggests the gate is too tight, not too loose. Calibrate.
- Longer-term: track retrieval hit rate. If gbrain retrieval consistently returns the same page, cache it in session memory instead of re-fetching.

---

## Priority Ranking

| Finding | Impact | Effort | Priority |
|---------|--------|--------|----------|
| #1 Single-layer RL | High (changes P5 thesis) | Medium (experiment design) | **P1** — next P5 session |
| #2 Self-correction grounding | Medium (audit + wire existing skills) | Low (audit existing loops) | **P2** — next dojo cycle |
| #3 Knowledge boundary gate | Medium (reduce context noise) | Medium (confidence gating logic) | **P3** — backlog |

---

*Synthesized from NotebookLM aiml-analysis export, 2026-08-02. 187 sources, 67K chars.*
