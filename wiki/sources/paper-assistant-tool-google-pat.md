---
date: 2026-06-30

type: source
tags: [paper, peer-review, ai-review, scientific-review, inference-scaling]
related: [autoresearch-pattern, evaluation-patterns, scientific-research]
---

# Towards Automating Scientific Review with Google's Paper Assistant Tool

**Authors:** Rajesh Jayaram, Drew Tyler, David Woodruff, Corinna Cortes, Yossi Matias, Vahab Mirrokni, Vincent Cohen-Addad (Google Research & Carnegie Mellon University)

**arXiv:** 2606.28277, June 26, 2026
**URL:** https://arxiv.org/abs/2606.28277
**Pages:** 10
**License:** © 2026 Google LLC. All rights reserved.

## Abstract

Introduces the Paper Assistant Tool (PAT), an agentic AI framework for deep scientific review and verification. PAT ingests full manuscripts and produces comprehensive evaluation: checking theoretical results, validating experiments, suggesting improvements, identifying flaws. Uses inference scaling techniques to achieve 34% improvement over zero-shot recall on mathematical errors in the SPOT benchmark. Pilot deployments at STOC and ICML demonstrate ability to identify critical errors.

## Architecture

```
Input Manuscript
    │
    ▼
Stage 1: Document Segmentation
    │  (segmenter agent → logical segments)
    ▼
Stage 2: Adaptive Budgeting
    │  (dynamically allocates Light/Medium/High thinking)
    ▼
Stage 3: Deep Review
    │  (specialized Deep Review agents per segment,
    │   powered by Gemini Deep Think inference-scaling)
    ▼
Stage 4: Global Synthesis
    │  (deduplication, severity checking, Google Search grounding)
    ▼
PAT Review
```

### Design vs Alternatives
| Approach | Limitation |
|----------|-----------|
| Single inference call | Limited by context window for deep analysis of full paper |
| Pass@k (independent calls) | Precision degradation (hallucinations multiply), no coordination between calls |
| **PAT (orchestrated)** | Segmented focus, coordinated deep review, synthesis with grounding |

## Key Results

### SPOT Benchmark (Math/CS Equation and Proof Errors)

| Method | Detection Accuracy |
|--------|-------------------|
| Original SPOT SOTA | 21.1% |
| Gemini 3.1 Pro (Zero-Shot) | 55.2% |
| **PAT (Gemini 3.1 Pro)** | **89.7%** |

*Note: 26 papers, 29 errors. Uses specialized LLM grader (not exact keyword match). Human-audited by authors.*

### Pilot Programs
- **STOC 2025** — Freely provided to authors pre-submission
- **ICML 2026** — Experimental program for all authors
- **Testimonials:** Vijay Vazirani, Hung Le, Jason Li reported catching critical errors

### Known Limitations (from pilots)
1. Date hallucinations / outdated knowledge cutoffs
2. PDF parsing issues
3. False claims of proof errors (model misunderstandings)

## Four-Level Taxonomy of AI Roles in Peer Review

| Role | Description | AI Does | Human Does |
|------|-------------|---------|------------|
| **Role 1:** Tool for Authors | Pre-submission quality check | Find errors, suggest improvements | Full responsibility for paper |
| **Role 2:** Tool for Reviewers | AI assists reviewer | Point out flaws, draft reviews | Full responsibility for review |
| **Role 3:** Supporting Reviewer | AI generates full review | Objective assessment (proofs, experiments) | AC makes acceptance decisions |
| **Role 3.5:** Supporting Reviewer with Ratings | AI + subjective assessment | Also provides ratings/recommendations | Human AC judges |
| **Role 4:** Total AI Automation | Fully automated review | All review stages | Human editors safeguard integrity |

## Related Concepts
- [[autoresearch-pattern]] — PAT is a directed, structured version of autoreview
- [[evaluation-patterns]] — Maps to the "Attack→Fix→Verify" and "Benchmark evaluation" patterns
- [[awesome-autoresearch]] — Scientific research is one of the main categories
