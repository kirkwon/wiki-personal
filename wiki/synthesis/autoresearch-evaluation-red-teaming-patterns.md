---
type: synthesis
tags: [autoresearch, evaluation, red-teaming, benchmarking, security]
related: [awesome-autoresearch, autoresearch-pattern]
---

# Evaluation / Red Teaming Autoresearch — Reusable Patterns

Analysis of 23 evaluation/red-teaming entries from awesome-autoresearch, extracting patterns reusable for security testing, prompt evaluation, and benchmark pipelines.

---

## Pattern Map

All 23 entries fall into 6 distinct evaluation patterns:

### Pattern 1: Attack → Fix → Verify Loop (4 entries)

The agent proposes an attack (jailbreak, adversarial prompt), the system is hardened, and the loop repeats to confirm the fix holds.

| Project | Target | Metric | Cycles |
|---------|--------|--------|--------|
| Claudini | LLM attack algorithms | benchmark outperformance | keep/discard |
| autovoiceevals | Voice AI agents | eval results | prompt revert |
| Jailbreak Autoresearch | Prompt harnesses | rubric scoring | header/body experiments |
| JustAsk (ICML 2026) | System prompt extraction | probe results | curiosity-driven |

**Takeaway:** This is penetration testing as autoresearch. The agent plays red team, the keep/discard is the vulnerability acceptance gate.

**Reusable for:** Automated security audit of our own agent infrastructure.

### Pattern 2: Prompt/Skill Optimization via Eval (5 entries)

The agent mutates a system prompt or skill definition, runs it against fixed test cases, and keeps only improvements.

| Project | Target | Metric | Iterations |
|---------|--------|--------|------------|
| Langfuse blog | AI skill (prompt migration) | correctness + completeness | 6 test cases |
| AutoPrompter | Prompt optimization | promptfoo-style metrics | experiment ledger |
| Support-agent prompt | System prompt | tool-call accuracy | 0.05 → 0.80 (15 iters) |
| claude-haiku-harness | Prompt benchmarking | production quality | Sonnet/Opus target |
| AutoMemory | Agent memory system | LongMemEval | failure-scored |

**Takeaway:** Directly applicable to our own skill optimization. Evolving `SKILL.md` via autoresearch is proven (AutoSkill did it too, see infra category).

**Reusable for:** Improving our existing skills (mean-variance-analyzer, asymmetry-hunter, etc.) through automated iteration.

### Pattern 3: Agent Behavior Evaluation (3 entries)

The agent evaluates other agents or systems through testing, not code mutation.

| Project | Target | Method |
|---------|--------|--------|
| Autoreason (NousResearch) | Subjective writing/coding | Blind multi-judge Borda tournament |
| Trace2Evolve | Support agent traces | Failure classification + reliability gates |
| AutonomousTester | Playwright tests | coverage_score iteration |

**Takeaway:** Autoresearch works for meta-evaluation — the loop improves the test suite itself, not just the code.

### Pattern 4: Benchmark Novelty & Integrity (4 entries)

Benchmarks designed specifically to evaluate autoresearch agents — not the output of the loop, but the loop itself.

| Project | What It Measures |
|---------|-----------------|
| AutoResearchBench | Literature discovery accuracy (~9% max) |
| NanoGPT-Bench | Open-ended speedrun research (<10% human) |
| ResearchArena | Full research loop quality (feasibility ≠ quality) |
| Novelty Bench | Hypothesis novelty vs rediscovery |

**Takeaway:** Current agents recover <10% of human-achievable speedup and primarily tune hyperparameters, not algorithms. This is the frontier.

### Pattern 5: Integrity Forensics (2 entries)

Anti-cheat systems for autoresearch itself.

| Project | Method |
|---------|--------|
| Anti-Autoresearch | 3-layer audit: experiment → result→claim + cross-model adversarial review |
| SciTriage | Evidence gates + claim discipline for AR agents |

**Takeaway:** As autoresearch scales, integrity forensics becomes essential. 39 hack-patterns across 7 families already documented.

### Pattern 6: Domain-Specific Evaluation Benchmarks (3 entries)

| Project | Domain |
|---------|--------|
| AutoMedBench | Medical QA (MedQA, MedMCQA, PubMedQA) |
| DSBench AutoResearch | 74 Kaggle + 38 Modeloff tasks |
| ResearchClawBench | 40 real-science tasks across 10 disciplines |

**Takeaway:** If we build a domain-specific evaluator, these are the reference implementations.

---

## Reusable Techniques

| Technique | Source | Description |
|-----------|--------|-------------|
| **Blind multi-judge Borda** | Autoreason | Multiple judges score A/B pairs, Borda count aggregates. Resistant to single-judge bias. |
| **Failure classification gates** | Trace2Evolve | Categorize failures before proposing fixes — prevents treating different failure modes as one. |
| **Three-layer audit stack** | Anti-Autoresearch | experiment-level → result-to-claim → paper-claim+citation, with cross-model reviewers. |
| **Evidence gates** | SciTriage | Don't accept a research result until evidence thresholds are met. |
| **Reliability gates** | Trace2Evolve | A change must pass both metric improvement AND reliability checks across task splits. |
| **Harness overfit detection** | Langfuse blog | Cherry-pick test cases to detect when the agent is gaming the evaluator. |
| **Holdback + walk-forward** | Multiple | One-shot holdout + walk-forward validation as a compound gate. |

---

## How This Applies to Our Stack

### For P3 (Skill → LoRA)
The **Autoreason tournament pattern** (blind multi-judge Borda) is directly applicable to comparing code variants in the execution trace → LoRA training pipeline.

### For Agent Security
The **Anti-Autoresearch three-layer audit** is a template for preventing our own agents from gaming evaluation metrics.

### For Skill Improvement
The **prompt-evolving eval loop** (Langfuse, AutoPrompter) maps directly to improving our existing skills through automated iteration.

### For Benchmarking
**NanoGPT-Bench's finding** (<10% human-level) is a sobering reference point — current agents primarily tune hyperparameters, not algorithms.

---

## Cross-Links to Add

- [[autoresearch-pattern]] — the evaluation loop itself
- [[pca-random-matrix-theory-equity-markets]] — the scientific evaluation framework
- [[mean-variance-myopia-under-stochastic-volatility]] — multi-regime validation
