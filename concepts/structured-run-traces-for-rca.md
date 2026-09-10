---
date: 2026-09-09
type: concept
title: Structured Run Traces for RCA
created: 2026-09-09
updated: 2026-09-09
tags:
  - rca
  - agents
  - observability
sources:
  - hermes://session/2026-09-09
---

# Structured Run Traces for RCA

For long-running agent/tool runs, failure diagnosis is far more accurate when the run is
represented as a **structured trace** (phases + statuses + failure signature) than as a raw
log dump. An LLM reading the full raw history may blame a late symptom for an early mistake.

## Evidence

Reported from a Microsoft + Tsinghua study (via @rohanpaul_ai, 2026-09-09): giving the judge a
structured run view raised exact fault localization from **3.63% to 31.35%** (GPT-5.1).
Representation — not just judge-model strength — drives localization quality.

Related work already in this brain:

- [[2505.00212]] — automated failure attribution in LLM multi-agent systems
- [[2608.22510]] — procedural trace compliance

## Application

- Capture per-phase status (ok / failed / skipped) plus a short detail, not just the tail of stdout.
- Emit a failure **signature** so classification does not require re-reading the log.
- Store the trace on the backlog item so the resolver starts at the right step.

Implemented in the inbox-outbox backlog schema (`signature`, `classification`, `trace[]`).

## Related

- [[cron-failure-signatures]]
- [[silent-cron-failures]]
