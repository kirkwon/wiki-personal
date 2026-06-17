---
type: concept
title: Karpathy‑Enhanced Self‑Harness
created: 2026-06-11
updated: 2026-06-11
tags: [concept, self-harness, karpathy, methodology, causal-discovery]
sources: []
---

# Karpathy‑Enhanced Self‑Harness

Applying Andrej Karpathy’s \"build it yourself\" methodology to the Self‑Harness framework yields a tighter improvement loop for LLM‑based agents.

## Weakness Mined

When attempting to rebuild the data‑fetch and macro‑assembly scripts from scratch, the following gaps were revealed:

- **fetch_yf.py**: Hard‑coded tickers, date ranges, and output paths; no retry logic; plain `print` statements; no CLI.
- **pull_macro_data.py**: Monolithic script; hard‑coded FRED key handling; no modularity; placeholder random numbers for fallback; no logging.

These weaknesses made the scripts brittle, non‑reusable, and hard to validate.

## Harness Proposed

A minimal, focused harness was built around each weakness:

1. **Added CLI** – argparse for ticker, dates, output directory, `--no‑save`, verbosity.
2. **Logging** – replaced `print` with the `logging` module (INFO/DEBUG).
3. **Retry mechanism** – exponential backoff (max 3 attempts) for Yahoo‑Finance and FRED requests.
4. **Deterministic fallback** – when FRED is unavailable, realized‑vol proxies replace missing series (no random numbers).
5. **Modular functions** – separated data loading, macro construction, regime building, and treatment/outcome computation.
6. **Type hints** – Python 3.8‑compatible annotations using `typing.Tuple`, `Optional`, etc.
7. **Dependency guards** – optional imports of `pandas_datareader` and `fredapi`; the script degrades gracefully.

## Validation Results

- Both scripts compile cleanly with `python3 -m py_compile`.
- Running with a short date range (2024‑12‑01 to 2024‑12‑31) produces:
  - `fetch_yf.py`: downloads SPY and TLT data, writes `price_data.csv` and `volume_data.csv`.
  - `pull_macro_data.py`: builds regime variables from price/volume alone (no FRED key) and outputs `real_data.csv` with the expected columns.
- The SHA‑256 hashes of the improved files are:
  - `fetch_yf.py`: `902be4cc999390d64b178880b3cc5ade5f1aab21570c12833924eb7032e28fb0`
  - `pull_macro_data.py`: `6b03966007b0f4de01bffa646cd859e9a7f678c18b17bfc5cf3448e1e607f7ee`

## Documentation & Reflection

Writing this page (the “explain it simply” step) clarified that the core insight is to treat the *script* as the harness to be improved: each iteration of the loop makes the harness more configurable, observable, and resilient.

## Related Concepts

- [[self-harness]] – the base paradigm being enhanced.
- [[karpathy-methodology]] – the build‑it‑yourself approach (see [[micrograd]], [[nanoGPT]], [[llm.c]]).
- [[causal-portfolio-analysis]] – the domain where the improved scripts are applied.
- [[llm-workflows]] – how LLM‑agents can orchestrate such data pipelines.
- [[personal-knowledge-management]] – the broader second‑brain context in which this improvement lives.
- [[methodology-loop]] – three‑layered improvement system (inner Self‑Harness loop, validation gate, meta‑loop to refine the inner loop)

## Applications

The enhanced harness can be reused for any financial‑data pipeline that needs:
- Configurable data sources
- Robust error handling
- Clear logging and auditability
- Easy integration into larger causal‑discovery or portfolio‑construction workflows.

---
