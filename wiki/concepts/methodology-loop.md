---
type: concept
title: Methodology Loop (Inner, Validation, Meta)
created: 2026-06-11
updated: 2026-06-11
tags: [concept, methodology, self-harness, karpathy, validation, meta-loop]
sources: []
---

# Methodology Loop

A three‑layered improvement system that combines the Self‑Harness paradigm with Karpathy’s “build it yourself” principles and adds a meta‑loop to continuously refine the inner loop itself.

## 1. Inner Loop – Self‑Harness (Karpathy‑Enhanced)

The core improvement cycle operates on a specific *harness* (e.g., a data‑fetch script, an LLM‑agent configuration, or a knowledge‑base template). It consists of three stages:

1. **Weakness Mine** – Attempt to rebuild the harness from scratch (first‑principles, micro‑experiment). Immediately note what you cannot implement or where you get stuck → reveals gaps in understanding.
2. **Harness Propose** – Build a minimal, focused version that isolates the weak component (e.g., a standalone propensity‑score estimator). Keep it as simple as possible while preserving the problematic behavior.
3. **Proposal Validate** – Test the minimal version against known cases or synthetic data with ground‑truth outcomes. If it fails, return to step 1 with the new insight; if it passes, consider the harness improved.

**Validation Exit Criteria** – The inner loop stops when:
- The reconstructed harness produces output that matches a trusted reference (e.g., DoWhy’s PSM on a toy dataset) within a predefined tolerance.
- All unit‑level assertions pass (property‑based or example‑based tests).
- A SHA‑256 hash of the harness file is recorded and matches the expected hash after the change (ensuring no unintended drift).
- Optionally, a performance metric (e.g., error reduction %) exceeds a threshold (e.g., ≥70% improvement over baseline).

When any of these criteria are satisfied, the inner loop yields a *validated harness* that can be promoted to the next layer.

## 2. Validation Layer – Gatekeeping the Inner Loop

Before exiting the inner loop, run a verification suite:

- **Deterministic Tests**: Fixed seed, known‑input → known‑output checks.
- **Property‑Based Tests**: e.g., symmetry, idempotence, monotonicity where applicable.
- **Integration Smoke**: Run the harness in its real‑world context (e.g., `fetch_yf.py` with a short date range) and confirm it starts, logs correctly, and writes expected files.
- **Hash Verification**: Compute SHA‑256 of the harness file and compare to the recorded expected hash; update the hash only after successful validation.
- **Documentation Check**: Ensure the harness includes an up‑to‑date docstring and, if applicable, a wiki‑concept link.

If all checks pass, the inner loop is considered *complete* and the validated harness is ready for meta‑evaluation.

## 3. Meta‑Loop – Improving the Inner Loop Itself

After a batch of inner‑loop completions (or after a fixed time interval), step back and ask: *How can we make the inner loop more effective?* This is the meta‑loop.

### Meta‑Loop Steps

1. **Meta‑Weakness Mine** – Review the recent inner‑loop runs:
   - Where did the validation take the most attempts?
   - Which weakness‑mine steps revealed the same type of gap repeatedly?
   - Did any validation criteria prove too lax or too strict?
2. **Meta‑Harness Propose** – Propose a tweak to the inner‑loop process itself. Examples:
   - Add a new validation check (e.g., property‑based test for a missing invariant).
   - Change the micro‑experiment scope (e.g., limit the rebuild to a single function instead of the whole script).
   - Adjust the exit threshold (e.g., require 80% error reduction instead of 70%).
   - Automate a repetitive step (e.g., generate a test harness template).
3. **Meta‑Proposal Validate** – Test the proposed meta‑change on a *representative* inner‑loop task:
   - Run the inner loop with the meta‑change applied.
   - Measure the effect: fewer iterations to validation, higher success rate, or improved hash stability.
   - If the meta‑change worsens outcomes, discard or refine.

**Meta‑Validation Exit Criteria** – The meta‑loop stops when:
- The proposed change yields a statistically significant improvement across a small pilot set (e.g., median iterations ↓ 30%).
- The change does not introduce regressions in other inner‑loop tasks.
- The change is documented and added to the methodology wiki (closing the loop).

## 4. Putting It All Together – The Full Cycle

```
Meta‑Loop
↓
[Inner Loop]
↓
Weakness Mine → Harness Propose → Proposal Validate
↓
Validation Layer (tests, hashes, metrics)
↓
[Validated Harness]
↓
(Meta‑Loop evaluates the inner‑loop process)
```

Each time the inner loop produces a validated harness, feed that result into the meta‑loop’s evaluation. Over time, the inner loop becomes sharper, requiring fewer iterations and yielding more robust improvements.

## 5. Related Concepts

- [[self-harness]] – Base paradigm being enhanced.
- [[karpathy-self-harness-enhancement]] – Application of Karpathy’s methodology to data‑fetch scripts.
- [[validation-techniques]] – Property‑based testing, fuzzing, and deterministic checks.
- [[meta-learning]] – Learning how to learn; the meta‑loop is a concrete instance.
- [[knowledge-base-curation]] – How the loop applies to wiki‑personal updates (e.g., adding this concept).

## 6. Applications

This three‑layered loop can be used to improve:
- **LLM‑agent harnesses** (configuration, tool selection, prompting).
- **Data‑pipeline scripts** (fetch_yf.py, pull_macro_data.py).
- **Knowledge‑base entries** (ensuring each wiki page is clear, linked, and verified).
- **Personal workflows** (e.g., your permanent‑question investigation process).

By nesting validation and meta‑improvement, the system avoids local maxima and continually raises the bar for what counts as a “good enough” harness.

---
