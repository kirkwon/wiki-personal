---
created: 2026-08-23
updated: 2026-08-23
---


# Karpathy Autoresearch Loop

The original autoresearch implementation by Andrej Karpathy, published February 2026. The canonical reference for the pattern that spawned hundreds of forks and adaptations across ML subfields.

**Repo:** https://github.com/karpathy/autoresearch

## Three-file architecture

- **`prepare.py`** — data preparation (immutable, chmod 444 after first run). Agent cannot modify.
- **`train.py`** — **the only mutable file**. The agent reads it, proposes a change, edits it, then runs the experiment.
- **`eval.py`** — fixed evaluator (also immutable). Measures `val_bpb` (validation bits-per-byte) on the nanoGPT GPT-2 small model.

## Workflow
1. Agent runs `prepare.py` to establish baseline data and metrics
2. Agent reads `train.py` and proposes a single change
3. Agent runs training with a fixed time budget (e.g. 5 minutes)
4. `eval.py` runs automatically and logs `val_bpb` to `results.tsv`
5. If `val_bpb` improved → `git commit` the change
6. If not → `git checkout -- train.py` to revert
7. Loop back to step 2

## Impact
- Launched a wave of hundreds of forks and adaptations
- Proven effective across: nanoGPT, CIFAR-10, YOLO, medical imaging, Connect Four, XGBoost, OCR, PDE solving, SAT solvers, chip design, atomic design, quantum experiments
- Ornith (Deep Reinforce AI) proved scaffold optimization via the same loop — 2× improvement on Terminal-Bench (43.1 vs 21.3) with a model 4× smaller than Qwen3.5-35B on SWE-bench (69.4)
- The pattern demonstrated that **optimizing the agent harness itself** (prompts, tool configs, search strategies) can be more impactful than optimizing model weights

## Why it works
- **Bounded experiments** — each run is 2-15 minutes; the cost of a failure is one experiment cycle
- **Empirical gate** — no theoretical justification is accepted; only measured improvement passes
- **Emergent serendipity** — the agent discovers improvements a human would never think to try because it doesn't need to justify them, only measure them
- **Git discipline** — clean commit history means every accepted change is reviewed and reproducible

See also: [[awesome-autoresearch]]

See also: [[autoresearch-pattern]]
