---
type: note
title: >-
  Metrics for Benchmarking Faster + Better Interactions with a Self‑Improving
  Claude
created: 2026-08-10
---
# Metrics for Benchmarking Faster + Better Interactions with a Self‑Improving Claude

*(Based on Anthropic’s June 2026 “Recursive Self‑Improvement” report and Hermes’ operational context.)*

## 1. Interaction‑time (speed) metrics
| Metric | What it captures | How to measure | Typical target / note |
|--------|------------------|----------------|----------------------|
| **Average Request‑to‑Response Latency** (ms) | End‑to‑end time from prompt → first token (or full response) | Timestamp at API call start vs. first token / final token | ↓ ≤ 200 ms for interactive chat; ≤ 2 s for code‑generation jobs |
| **95‑th‑percentile Latency** | Tail latency – worst‑case experience | Same as above, report p95 | ↓ ≤ 500 ms (chat) / ≤ 5 s (batch) |
| **Time‑to‑First‑Token (TTFT)** | Model startup / loading overhead | Measure from request receipt to first token emission | ↓ ≤ 50 ms (warm) |
| **Throughput (tokens / sec)** | Raw generation capacity | Count tokens generated ÷ wall‑clock time | ↑ ≥ 2 × baseline (early‑2025) |
| **Review Turn‑Around Time** | Human‑in‑the‑loop delay (code review, safety check) | Timestamp when code is submitted for review → when review is approved/rejected | ↓ target ≤ ½ of current (e.g., from 4 h → 2 h) |
| **Number of Review Cycles** | How many iterations before acceptance | Count of review submissions per PR / code chunk | ↓ aim ≤ 1.2 cycles (near‑autonomous) |
| **Pipeline Iteration Latency** (for self‑improvement loops) | Time for one generation → test → feedback → next generation | Log each stage in the automated self‑improvement pipeline | ↓ target ≤ 30 min per iteration (vs. hours today) |

## 2. Quality‑oriented metrics
| Metric | What it captures | How to measure | Typical target / note |
|--------|------------------|----------------|----------------------|
| **Pass@k (code generation)** | Probability that at least one of *k* sampled solutions passes unit tests | Generate *k* candidates, run test suite, compute fraction | ↑ Pass@1 ≥ 0.70, Pass@10 ≥ 0.90 (HumanEval‑style) |
| **CodeBLEU / BLEU‑4 / ROUGE‑L** | Lexical/syntactic similarity to reference implementation | Compare generated code to a golden reference (if available) | ↑ ≥ 0.45 CodeBLEU (state‑of‑the‑art) |
| **Execution Success Rate** | Fraction of generated snippets that run without error (ignoring test correctness) | Run each snippet in a sandbox, count non‑crashing runs | ↑ ≥ 0.95 |
| **Defect Density (bugs / KLOC)** | Post‑deployment defects discovered per thousand lines of code | Static analysis + dynamic testing + production incident count | ↓ ≤ 0.5 bugs/KLOC (industry‑best) |
| **Test‑Coverage Increase** | % of lines/exercised branches after AI‑generated code is added | Run coverage tool (e.g., coverage.py, JaCoCo) on the repo before/after | ↑ ≥ + 10 % coverage per sprint |
| **Alignment / Safety Score** | Degree to which output respects policy (no hallucinations, no harmful content) | Use a calibrated reward model or human‑rating rubric (0‑1) | ↑ ≥ 0.90 alignment |
| **Hallucination Rate** | % of factual statements that are unverifiable / false | Sample generated text, verify against knowledge base or expert review | ↓ ≤ 2 % |
| **Code Review Severity Distribution** | Shift from high‑severity to low‑severity issues in reviews | Tag review comments (critical, major, minor, info) and compute percentages | ↓ critical ≤ 5 % of comments |
| **Technical Debt Ratio** | (Debt‑remediation effort) / (total development effort) | Track time spent on refactoring vs. feature work | ↓ target ≤ 0.15 (15 %) |
| **User‑perceived Quality (Likert/NPS)** | Subjective satisfaction with speed & correctness | Short survey after each interaction (1‑5 or NPS) | ↑ ≥ 4.2/5 or NPS > 30 |

## 3. Composite / Efficiency metrics
| Metric | Formula | Why it matters |
|--------|---------|----------------|
| **Quality‑Per‑Second (QPS)** | `QualityScore ÷ AvgLatency` | Captures trade‑off: a model that is twice as fast but half as good scores the same; you want ↑ QPS. |
| **Efficiency Gain vs. Baseline** | `(QPS_new – QPS_baseline) / QPS_baseline` | Percentage improvement over the early‑2025 baseline. |
| **Cost‑Effectiveness** | `(QualityScore) ÷ (ComputeCost + HumanReviewCost)` | Helps decide when to invest in more compute vs. more human oversight. |
| **Risk‑Adjusted Velocity** | `Throughput × (1 – DefectDensity)` | Penalizes raw speed that produces many bugs. |

## 4. How to instrument & collect the data
| Layer | Tool / Approach | Example Implementation |
|-------|----------------|------------------------|
| **API‑level latency** | Middleware timestamps (e.g., Envoy, Istio, or custom Flask/Django middleware) | Log `request_start`, `first_token`, `request_end` → emit to Prometheus/OpenTelemetry. |
| **Token throughput** | Increment counter per generated token; expose as gauge. | `tokens_generated_total{model="claude-3"}` |
| **Review metrics** | Integrate with PR system (GitHub/GitLab) via webhook; record `review_opened_at`, `review_closed_at`, `review_state`. | Use GitHub Actions to push metrics to a Timeseries DB. |
| **Test execution** | CI pipelines (GitHub Actions, GitLab CI, Bazel) collect `pass/fail`, `duration`, `coverage`. | Upload results to Codecov / custom dashboard. |
| **Static analysis / security** | Run Bandit, SonarQube, Trivy, etc.; count findings by severity. | Export SARIF → aggregate. |
| **Human feedback** | Embed a lightweight rating widget in the chat UI (thumbs‑up/down, 1‑5 slider) + optional comment. | Store in event stream for aggregation. |
| **Self‑improvement loop** | Instrument each stage of the recursive pipeline (code gen → unit test → self‑critique → next gen). | Log stage timestamps and outcome flags; compute iteration latency. |
| **Alerting** | Set SLO‑based alerts (e.g., p95 latency > 500 ms → PagerDuty). | Helps catch regressions early. |

## 5. Suggested benchmarking protocol
1. **Baseline capture** – Run a representative workload (e.g., generate 1 000 typical code prompts from the internal issue backlog) on the *early‑2025* Claude snapshot. Record all metrics above.  
2. **Experimental run** – Repeat the same workload with the *June 2026* Claude (or the newer self‑improving variant).  
3. **Statistical comparison** – Use paired‑sample tests (Wilcoxon signed‑rank or t‑test) for latency; compute confidence intervals for Pass@k, defect density, etc.  
4. **A/B / Canary** – Deploy the new model to 5 % of traffic, compare real‑world latency & review‑cycle metrics against the control group.  
5. **Report** – Produce a one‑page “speed‑quality scorecard” showing:  
   * Δ latency (↓ %), Δ throughput (↑ %), Δ Pass@k (↑ pp), Δ defect density (↓ pp), Δ review turn‑around (↓ %), and the composite QPS gain.  

## 6. Adding this tracking & improvement to Hermes
1. **Instrument Hermes API calls** – Wrap the Hermes LLM invocation (whether via OpenRouter, local model, or external provider) with a small middleware that records:
   - request timestamp
   - time to first token
   - full response timestamp
   - token count (using `tiktoken` or similar)
   - success / error flag
   Export these as Prometheus metrics (`hermes_latency_seconds`, `hermes_tokens_total`, `hermes_requests_total`, `hermes_errors_total`).

2. **Hook into PR / review workflow** – If Hermes generates code that lands in a repo (via `git commit` or a skill that opens a PR), use a GitHub Action or a Hermes skill that:
   - stamps when the PR is opened
   - stamps when review comments are posted
   - stamps when the PR is merged or closed
   - computes review turn‑around and number of cycles
   - pushes these to the same monitoring stack.

3. **Run automated evaluation suites** – Create a Hermes skill (or cron job) that:
   - pulls a benchmark set of prompts (e.g., HumanEval, MBPP, or internal risk‑management prompts)
   - runs the model (via Hermes) to generate solutions
   - executes unit tests, computes Pass@k, CodeBLEU, execution success, defect density via static analysis tools (Bandit, SonarQube)
   - pushes results to Prometheus/Grafana or writes a markdown summary to the LLm‑wiki (which will be sync‑ed to GBrain via the existing LLm‑wiki → GBrain cron).

4. **Feedback loop for self‑improvement** – For a recursive self‑improvement experiment:
   - Stage 1: Hermes generates code for a task.
   - Stage 2: Run unit tests; collect Pass@k.
   - Stage 3: If Pass@k < threshold, invoke a self‑critique prompt (“How could this code be improved?”) and have Hermes produce a revised version.
   - Stage 4: Log timestamps for each stage; compute pipeline iteration latency.
   - Optionally, feed the revised version back into the model as additional training data (if fine‑tuning is enabled).

5. **Visualization & alerting** – Build a Grafana dashboard that shows:
   - Latency trends (average, p95, TTFT)
   - Throughput and token usage
   - Quality metrics (Pass@k, defect density, alignment score)
   - Review‑cycle metrics
   - QPS and risk‑adjusted velocity over time
   Set alerts when latency regresses > 20 % or defect density rises > 0.6 bugs/KLOC.

6. **Documentation & knowledge sync** – After each benchmark run, write a markdown summary (like this file) to `~/llm-wiki/concepts/` with a timestamp (e.g., `metrics-claude-self-improvement-2026-06-08.md`). The existing LLm‑wiki → GBrain delta sync cron (every 3 h) will push it into GBrain, making it searchable and linkable from other notes.

By instrumenting Hermes in this way, you obtain continuous, quantitative insight into whether the model is truly getting *faster* and *better*—exactly the information needed to gauge the impact of Anthropic’s recursive self‑improvement and to trigger mitigations (e.g., rollback, extra human review, targeted fine‑tuning) before risks accumulate.

---
*Generated via Hermes Agent knowledge synthesis – 2026‑06‑08*
