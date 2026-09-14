---
type: note
title: 'Experiment: Evolver vs Solver model size impact on self‑improving agents'
created: 2026-08-10
source: brain/ (retired 2026-09-13)
---
# Experiment: Evolver vs Solver model size impact on self‑improving agents

**Goal:** Test the hypothesis from arXiv:2605.30621 that a smaller, cheaper model can serve as an effective *evolver* (writing updates) while a larger, more capable model serves as the *solver* (using those updates to solve tasks), and that the sweet spot is a mid‑tier solver.

**Related notes**
- [[better-self-improving-agents-need-better-solvers]] – paper summary
- [[metrics-weekly-report-plan]] – weekly speed/quality tracking
- [[self-improving-agent-loop]] – general framework
- [[skill-update-pipeline]] – how Hermes can autonomously generate and test new skills

## Proposed experimental setup

1. **Task suite** – Choose a small, well‑defined benchmark that can be solved via Hermes skills, e.g.:
   - A set of 20 simple coding problems (HumanEval subset).
   - A set of 10 question‑answering prompts requiring multi‑step reasoning.
   - A set of 5 tool‑usage scenarios (e.g., fetch a URL, compute a metric, write a file).

2. **Models** – Use three model tiers available via OpenRouter (or local):
   - **Small**: Qwen3.5‑9B (or similar ~9B parameter model).
   - **Mid**: Claude 3.5 Sonnet (or equivalent mid‑tier).
   - **Large**: Claude Opus 4.6 (or the strongest available).

3. **Roles**
   - **Evolver**: Responsible for generating a *skill update* (e.g., a new Hermes skill that encapsulates a useful prompt pattern, memory entry, or tool wrapper) based on the task description.
   - **Solver**: Responsible for executing the task using the evolver‑generated skill (or the baseline if no skill is provided).

4. **Procedure**
   - For each model pair (evolver, solver):
     a. **Evolver phase**: Prompt the evolver model to produce a skill/update for a given task category (e.g., “Write a Hermes skill that improves solving of array‑manipulation problems by adding a preprocessing step”). The evolver output is saved as a temporary skill file.
     b. **Solver phase**: Load the evolver‑generated skill (or run without it as control) and have the solver model attempt the task suite.
     c. **Metrics**: Record success rate, average latency, token usage, and any review‑cycle metrics (if the skill triggers a PR‑like review).
   - Include a control where evolver and solver are the same model (to isolate the effect of decoupling).

5. **Analysis**
   - Compare solver performance across evolver sizes.
   - Expected pattern per paper:
     - Evolver size has minimal impact on solver performance (small evolver ≈ large evolver).
     - Solver size shows a clear monotonic improvement up to a point, after which gains plateau.
     - The best overall score may come from a small evolver + mid solver, or mid evolver + mid solver, depending on the task difficulty.

6. **Automation with Hermes**
   - Use the `hermes` CLI with per‑call model override (if supported) or create temporary cron jobs that point to different model configurations.
   - Log each run using the existing metrics‑logging pipeline (`simple-metrics-log` skill) to capture latency, token count, success.
   - Store the evolver‑generated skill as a temporary file in `~/.hermes/skills/temp/` and clean up after each iteration.
   - After each model pair run, write a markdown summary to `~/llm-wiki/concepts/experiment-results-<evolver>-<solver>.md` and link it from this note.

7. **Linking to knowledge graph**
   - Each result note will include front‑matter:
     ```yaml
     ---
     title: "Experiment Results – Evolver: Qwen3.5‑9B, Solver: Claude Opus 4.6"
     date: 2026-06-08
     tags: [experiment, evolver-solver, model-size]
     ---
     ```
   - The LLm‑wiki → GBrain delta‑sync cron (every 3 h) will push these notes into GBrain, making them searchable and linkable (e.g., `[[experiment-results-qwen3.5-9b-claude-opus-4.6]]`).

## Next steps

- Verify that Hermes allows specifying a model per invocation (check `hermes --help` or skill context).
- If not, create two separate Hermes profiles (e.g., `hermes-evolver` and `hermes-solver`) with different model configs and switch profiles via `hermes --profile`.
- Implement a small wrapper script that automates the evolver→solver loop and logs results.
- Run a pilot with a handful of tasks to validate the pipeline.
- Expand to the full task suite and analyze.

---

*See also:* [[better-self-improving-agents-need-better-solvers]] for the paper that motivated this experiment.

*Created 2026‑06‑08 as part of testing the evolver/solver hypothesis.*  
*This note will be synced to GBrain via the existing LLm‑wiki → GBrain delta‑sync cron.*
