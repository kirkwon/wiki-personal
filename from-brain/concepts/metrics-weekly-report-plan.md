---
type: note
title: Weekly Metrics Report Plan for Hermes (Speed & Quality)
created: 2026-08-10
---
# Weekly Metrics Report Plan for Hermes (Speed & Quality)

## Goal
Automatically capture **interaction‑time (speed)** and **quality** metrics from Hermes each week, summarize them in a markdown note, and store the note in the LLm‑wiki (`~/llm-wiki/concepts/`) so it becomes searchable via GBrain and can be reviewed for trends, regressions, and improvement opportunities.

## Frequency
- **Cron schedule:** `0 9 * * 1` (Every Monday at 09:00 local time) – produces a report for the previous week (Sun‑Sat).

## Data Sources
| Metric Category | Source | Query / Collection Method |
|-----------------|--------|---------------------------|
| **API‑level latency** (avg, p95, TTFT) | Prometheus (or local TimescaleDB) – metrics exported by Hermes middleware: `hermes_latency_seconds{quantile="0.5"}`, `hermes_latency_seconds{quantile="0.95"}`, `hermes_ttft_seconds` | `avg_over_time(hermes_latency_seconds[7d])`, `quantile_over_time(0.95, hermes_latency_seconds[7d])`, `avg_over_time(hermes_ttft_seconds[7d])` |
| **Throughput** (tokens/sec) | Prometheus counter: `hermes_tokens_total` | `rate(hermes_tokens_total[7d])` |
| **Review turn‑around** | GitHub webhook logs → Hermes‑review skill timestamps stored in a small SQLite table (`hermes_review_events`) or exported via a Hermes skill that writes to Prometheus (`hermes_review_duration_seconds`) | `avg_over_time(hermes_review_duration_seconds[7d])` |
| **Number of review cycles** | Same table – count of `review_opened` → `review_closed` → `review_reopened` sequences per PR | Custom query: count distinct PRs where `review_state` changed >1 time in the week |
| **Pipeline iteration latency** (self‑improvement loop) | Logs from Hermes self‑improvement skill: timestamps for `gen_start`, `test_end`, `critique_start`, `next_gen_start` | Compute stage deltas and average over week |
| **Pass@k** (code generation) | Evaluation skill output: JSON file `eval/pass_at_k.json` generated weekly | Read file, extract `pass@1`, `pass@10` |
| **CodeBLEU / ROUGE‑L** | Same evaluation script; outputs `codebleu.json`, `rougeL.json` |
| **Execution Success Rate** | Evaluation script: fraction of snippets that run without error | `exec_success_rate` |
| **Defect Density** | Static analysis (Bandit, SonarQube) run on repo after Hermes‑generated code is merged; output `defect_density.json` (bugs/KLOC) |
| **Test‑Coverage Increase** | Coverage tool (coverage.py, JaCoCo) diff between baseline and week‑end | `coverage_diff_percent` |
| **Alignment / Safety Score** | Reward model or human‑rating aggregation; stored as `hermes_alignment_score` gauge | `avg_over_time(hermes_alignment_score[7d])` |
| **Hallucination Rate** | Sampled fact‑checking job; output `hallucination_rate.json` |
| **Code Review Severity Distribution** | GitHub review labels (critical, major, minor, info) aggregated via GitHub API or webhook logs | Compute percentages |
| **Technical Debt Ratio** | Time‑tracking logs (e.g., Toggl) or Jira issue types; ratio of refactoring effort vs. feature effort | `debt_ratio` |
| **User‑perceived Quality** | In‑chat rating widget (thumbs‑up/down or 1‑5) stored in `hermes_user_rating` gauge | `avg_over_time(hermes_user_rating[7d])` |

> **Note:** If a particular metric source is not yet instrumented, the weekly job can gracefully skip it and note “data not available” in the report.

## Implementation Steps
1. **Instrument Hermes (if not already done)**
   - Wrap LLM call in middleware that emits:
     - `hermes_latency_seconds` (histogram with quantiles)
     - `hermes_ttft_seconds` (gauge)
     - `hermes_tokens_total` (counter)
     - `hermes_errors_total` (counter)
     - `hermes_alignment_score` (gauge)
     - `hermes_user_rating` (gauge)
   - Export via Prometheus endpoint (`/metrics`) scrapeable by the existing monitoring stack.

2. **Add Review‑Event Tracking**
   - Create a Hermes skill `hermes-review-tracker` that:
     - Listens to GitHub webhook events (PR opened, review submitted, PR closed/merged).
     - Writes a row to a local SQLite DB (`~/.hermes/review_events.db`) with columns: `pr_id`, `event_type`, `timestamp`, `actor`, `review_state`.
   - Alternatively, push events to Prometheus as a histogram `hermes_review_duration_seconds`.

3. **Weekly Evaluation Skill**
   - Create a Hermes skill `hermes-weekly-eval` that:
     - Pulls a fixed benchmark set (e.g., 200 HumanEval prompts + internal risk‑management prompts).
     - Runs the current Hermes model to generate solutions.
     - Executes unit tests, computes Pass@k, CodeBLEU, ROUGE‑L, execution success.
     - Runs static analysis (Bandit/SonarQube) on the generated code to get defect density.
     - Runs coverage diff vs. baseline.
     - Writes results to JSON files under `~/.hermes/eval/weekly/`.
   - This skill can be triggered by the cron job or run on‑demand.

4. **Cron Job Definition**
   - Use Hermes’ built‑in cron management:
     ```yaml
     # ~/.hermes/cron/weekly-metrics.yaml
     - name: weekly-metrics-report
       schedule: "0 9 * * 1"
       prompt: |
         You are a metrics‑gathering assistant. Using the available data sources (Prometheus, local SQLite, eval JSON files), produce a concise markdown weekly report covering:
         1. Speed metrics (average latency, p95 latency, TTFT, throughput, review turn‑around, review cycles, pipeline iteration latency).
         2. Quality metrics (Pass@k, CodeBLEU, ROUGE‑L, execution success, defect density, test‑coverage delta, alignment score, hallucination rate, review severity distribution, technical debt ratio, user rating).
         3. Trend commentary: compare each metric to the previous week (Δ%).
         4. Action items: highlight any regressions (>10% degradation) or notable improvements.
         Output the report as markdown ready to be saved to ~/llm-wiki/concepts/ with a filename like metrics-weekly-YYYY-WW.md.
       skills:
         - hermes-metrics-weekly-report   # the skill that implements the logic above
       deliver: origin   # send back to this chat for verification, then we can move to wiki
     ```
   - The skill `hermes-metrics-weekly-report` will:
     - Query Prometheus (via `curl` to `http://localhost:9090/api/v1/query`) for each latency/throughput metric.
     - Read the SQLite review DB for review metrics.
     - Load the latest eval JSON files.
     - Compute deltas versus the previous week’s report (stored in `~/hermes/metrics/history/`).
     - Render a markdown template.
     - Write the file to `~/llm-wiki/concepts/metrics-weekly-YYYY-WW.md`.
     - Optionally, also copy a copy to `~/hermes/metrics/history/` for archival.

5. **Knowledge Sync**
   - The existing LLm‑wiki → GBrain delta‑sync cron (every 3 h) will automatically pull the newly created markdown file into GBrain, making it searchable and linkable from other notes.
   - Tag the file with front‑matter for easy filtering:
     ```yaml
     ---
     title: "Weekly Metrics Report – Week 24, 2026"
     date: 2026-06-10
     tags: [metrics, weekly, speed, quality]
     ---
     ```

6. **Alerting & Feedback Loop**
   - Add a Prometheus alert rule that fires if:
     - `avg_over_time(hermes_latency_seconds[7d]) > baseline_latency * 1.2` (20% regression)
     - `avg_over_time(hermes_defect_density[7d]) > 0.6 bugs/KLOC`
   - Alerts can be routed to a Hermes‑managed Slack/Telegram channel or to the weekly report as a “⚠️ Alerts” section.

## Example Markdown Output (template)
```markdown
# Weekly Metrics Report – Week 24, 2026 (2026‑06‑03 → 2026‑06‑09)

*Generated by Hermes metrics‑weekly‑report skill – 2026‑06‑10 09:00*

## Speed Metrics
| Metric | This Week | Prev Week | Δ% | Target |
|--------|-----------|-----------|----|--------|
| Avg Latency (ms) | 182 | 200 | -9% | ≤200 |
| 95‑pct Latency (ms) | 410 | 460 | -11% | ≤500 |
| TTFT (ms) | 48 | 55 | -13% | ≤50 |
| Throughput (tok/s) | 1 240 | 1 100 | +13% | ≥2×baseline |
| Review Turn‑Around (h) | 1.9 | 2.3 | -17% | ≤2.0 |
| Review Cycles / PR | 1.1 | 1.3 | -15% | ≤1.2 |
| Pipeline Iteration Latency (min) | 28 | 34 | -18% | ≤30 |

## Quality Metrics
| Metric | This Week | Prev Week | Δ% | Target |
|--------|-----------|-----------|----|--------|
| Pass@1 | 0.73 | 0.68 | +7pp | ≥0.70 |
| Pass@10 | 0.92 | 0.88 | +4pp | ≥0.90 |
| CodeBLEU | 0.48 | 0.44 | +9pp | ≥0.45 |
| ROUGE‑L | 0.51 | 0.48 | +6pp | ≥0.45 |
| Execution Success (%) | 96.5 | 94.2 | +2.3pp | ≥95 |
| Defect Density (bugs/KLOC) | 0.38 | 0.45 | -16pp | ≤0.5 |
| Test‑Coverage Δ (%) | +12% | +8% | +4pp | ≥+10% |
| Alignment Score | 0.91 | 0.89 | +2pp | ≥0.90 |
| Hallucination Rate (%) | 1.4 | 1.8 | -0.4pp | ≤2 |
| Review Severity – Critical (%) | 3.2 | 4.5 | -1.3pp | ≤5 |
| Technical Debt Ratio | 0.12 | 0.15 | -0.03 | ≤0.15 |
| User Rating (1‑5) | 4.3 | 4.1 | +0.2 | ≥4.2 |

## Trend Commentary
- Latency improved across the board, driven by the new token‑streaming middleware.
- Review turn‑around dropped below the 2 h target for the first time.
- Defect density continues its downward trend, suggesting the static‑analysis gate in the PR workflow is effective.
- Alignment score remains safely above the 0.90 threshold.

## Action Items
- ✅ No regressions >10% detected.
- ⚠️ Monitor the slight increase in hallucination rate; consider adding a fact‑checking prompt for high‑risk topics.
- 📈 Plan to increase the benchmark set size next week to capture more edge‑cases.

---
*Sources: Prometheus (hermes_* metrics), SQLite review DB, eval JSON files (Pass@k, CodeBLEU, etc.), static analysis reports.*
```

## Next Steps / Checklist
- [ ] Verify Hermes middleware emits latency/token metrics.
- [ ] Deploy `hermes-review-tracker` skill and confirm SQLite logs.
- [ ] Create `hermes-weekly-eval` skill and test on a small prompt set.
- [ ] Add the cron job definition (`~/.hermes/cron/weekly-metrics.yaml`).
- [ ] Create the skill `hermes-metrics-weekly-report` that implements the markdown generation.
- [ ] Run a dry‑run (`hermes cron run weekly-metrics-report`) to validate output.
- [ ] Once satisfied, enable the cron and let it run automatically.
- [ ] Review the first generated note in LLm‑wiki and adjust the template as needed.

---

*Prepared for Hermes – 2026‑06‑08*  
*This plan can be saved as a LLm‑wiki concept (as done above) and linked from other notes via `[[metrics-weekly-report-plan]]`.*
