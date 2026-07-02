---
tags: [permanent-question, research, ai-finance]
created: 2026-05-25
question: "What are the foundational skills and knowledge that most leverage the intersection of AI/ML and Finance? Work from basics — what does one actually need to master?"
type: permanent-question
reviewed: 2026-05-25
---

# Q01: High Leverage Skills Bridging AI/ML and Finance

## Question
*What are the foundational skills and knowledge that most leverage the intersection of AI/ML and Finance? Work from basics — what does one actually need to master?*

## Current State of Knowledge

### Layer 1: Mathematical Foundations (prerequisite for everything else)
- **Probability + Statistics** — Bayesian thinking, distributions, CLT, hypothesis testing, MLE. Not optional.
- **Linear Algebra** — matrices, eigenvalues, SVD, PCA. The language of models.
- **Calculus** — gradients, chain rule. Required for understanding optimization.
- **Stochastic Calculus** — Brownian motion, Ito's lemma, diffusion processes. Required for options pricing and continuous-time models.
- **Optimization** — convex optimization, Lagrange multipliers, gradient descent variants.

*Realization: Most practitioners are underprepared on math. The people who excel at AI × Finance tend to have physics, math, or stats backgrounds. Self-study path: Probability → Linear Algebra → Stochastic Calc.

### Layer 2: Financial Theory (the domain layer)
- **Modern Portfolio Theory** — Markowitz, CAPM, factor models (Fama-French). The baseline.
- **Derivatives Pricing** — Black-Scholes, binomial trees, Monte Carlo. Greeks, hedging.
- **Market Microstructure** — bid-ask, order books, liquidity, market making.
- **Risk Management** — VaR, CVaR, stress testing, scenario analysis.
- **Behavioral Finance** — limits to arbitrage, investor psychology, anomalies. Useful for understanding why simple models fail.
- **Time Series Econometrics** — ARIMA, GARCH, cointegration, mean reversion. The foundation of forecasting.

*The key gap: Academic finance is often taught as if markets are efficient. Practical AI applications often implicitly assume too much structure. Know both.

### Layer 3: Machine Learning (the tool layer)
- **Classical ML** — regression, trees, SVMs, ensemble methods. Surprisingly competitive for tabular financial data.
- **Deep Learning for Time Series** — LSTM, Temporal Fusion Transformer, N-Beats, PatchTST. State of art for sequence modeling.
- **Reinforcement Learning** — policy gradient, Q-learning, PPO. For trading agent problems (portfolio allocation, market making).
- **Bayesian ML** — Gaussian processes, Bayesian neural networks. Useful for uncertainty quantification in risk.
- **Causal Inference + ML** — causal discovery, do-calculus, heterogenous treatment effects. Underused in finance.

*Critical: Don't start with transformers. Financial data is short, noisy, non-stationary. Simple models often win.

### Layer 4: Software Infrastructure (making it real)
- **Python** — pandas (critical), numpy, scipy, scikit-learn, PyTorch or JAX.
- **Data infrastructure** — ability to backtest properly (avoiding lookahead bias, survivorship bias).
- **Feature engineering** — the underrated skill. Alpha comes from data, not just models.
- **Alternative data** — satellite, sentiment, web scraping. ML makes these usable.
- **Cloud compute** — GPU access for deep learning. Modal, RunPod, cloud.

### Layer 5: Research + Iteration Skills (what separates practitioners from academics)
- **Rigorous backtesting** — walk-forward validation, out-of-sample testing, bootstrap.
- **Understanding why models fail** — regime changes, non-stationarity, overfitting to noise.
- **Paper reading** — arXiv q-fin, JMLR, NeurIPS/ICML for ML. Know what's actually deployed.
- **Writing code that can be critiqued** — version control, tests, reproducibility.

## Key Papers / Resources

*To populate from research scan. Starting references:*
- Marcos López de Prado — *Advances in Financial Machine Learning* (practical, ML-focused)
- John Hull — *Options, Futures, and Other Derivatives* (foundational derivatives)
- Ang — *Asset Management* (factor investing foundations)
- Sutton & Barto — *Reinforcement Learning* (RL foundation)
- papers.ssrn.com — q-fin.ML category

## Emerging Methodology

The intersection rewards people who are **good at all three layers**. Pure ML people
often miss financial nuance (survivorship bias, lookahead, transaction costs). Pure
finance people often underutilize ML.

**The highest leverage zone: feature engineering + rigorous backtesting + simple models.**


**The most underutilized skill: Causal Inference**. Most ML in finance is predictive
not causal. Causal models improve both alpha generation (are you exploiting a real
structure?) and risk understanding (what does a regime change actually cause?).

Recommended learning path for causal inference:
1. Pearl, Glymour, Jewell — "Causal Inference in Statistics: A Primer" (2016) — elementary, clear
2. Pearl — "Causality: Models, Reasoning, and Inference" (2009) — the definitive text
3. Pearl — "The Book of Why" (2018, with Dana Mackenzie) — accessible, with examples

**Microsoft DoWhy** (https://www.microsoft.com/en-us/research/project/dowhy/): Python library
implementing Pearl's four-step causal inference — model (causal graph), identify (do-calculus),
estimate, refute. The standard entry point for applied causal ML.

**Key concept: Confounders**. A confounder is a variable Z that causes both X and Y, creating
spurious correlation. In finance: market regime is a confounder for almost every factor.
DoWhy's causal graph approach makes confounders explicit and identifies what to control for.

**Microsoft EconML**: Extension for heterogeneous treatment effects — understanding when
and for whom a strategy works. Relevant for factor investing and risk management.

**Papers**:
- Sharma et al. — "DoWhy: An End-to-End Library for Causal Inference" (arXiv:2011.04216)
- Pearl — "Causality" (2009) — foundational
- Pearl et al. — "Causal Inference in Statistics: A Primer" (2016) — starting point

## Connections to Other Questions
- [[Q05]] — Q01 foundations directly feed into predictive finance models
- [[Q03]] — accelerating learning helps acquire these skills faster
- [[Q04]] — symbolic/energy models may change what's worth learning

## Status
_Active — accumulating_ — June 2026 brought several practical pipeline advances that deepened the causal/automation layer.

## June 2026 Findings (Updated Jun 24)

### Causal AI Pipeline (DoWhy/EconML) — Applied Deepening

Deployed DoWhy causal graph models on portfolio factor data. Key finding: the **refutation step** (random common cause, data subset, placebo treatment) catches spurious factors that standard backtesting misses. EconML's DML (Double Machine Learning) estimator is now the standard for heterogeneous treatment effect estimation in the pipeline — identifying *which* market conditions a given factor strategy works in, not just *whether* it works.

**Pipeline structure (June 2026):**
1. DoWhy causal graph → CausalModel with gml
2. EconML DML/CausalForest → estimate CATE
3. DoWhy refute → validate against placebo/random-common-cause
4. If refutation passes → backtest with Self-Harness

### Self-Harness Applied to Financial Scripts

The [self-harness](https://github.com/NousResearch/self-harness) framework (function-calling evaluation) was applied to financial ML scripts — turning individual strategies into evaluable test cases. Each strategy is wrapped as a function with known inputs/outputs, and Self-Harness verifies correctness, statistical validity, and no lookahead bias. This catches errors that unit tests don't (data leakage, stale references, misaligned timestamps).

**Result:** Automated eval-driven iteration cycle for strategy development. Write strategy → Self-Harness eval → fix → re-eval.

### Portfolio Dashboard Fixes

Fixed multiple bugs in the real-time portfolio dashboard (streamlit-based):
- **Cash drift bug**: Portfolio cash balance drifted from actual due to incorrect dividend accrual timing. Fixed by switching to transaction-level accounting (cash_events log) instead of daily snapshots.
- **NAV stutter**: Dashboard NAV line would freeze on certain market regimes. Root cause: stale WebSocket subscription that timed out silently. Fixed with heartbeat/reconnect logic.
- **SPY beta miscalc**: Rolling 60-day beta was using incorrect benchmark alignment (missing market open gap). Fixed by aligning to daily close-to-close returns.

### Web Extraction Infrastructure — Free Alternative Data Pipelines

Deployed free, local web extraction backends (Crawl4AI + ScrapeGraphAI) via Hermes's pluggable Web Extraction Provider Architecture ([[concepts/web-extraction-provider-architecture]]). Key implications for the finance data pipeline:

- **Crawl4AI** (62k GitHub stars): Fast (~1-4s per URL), free, local Playwright-based extraction. Replaces Firecrawl credit dependency for URL→markdown. Default extract backend now configured to route all extraction through Crawl4AI, with Firecrawl reserved for web search only. See [[entities/crawl4ai]].

- **ScrapeGraphAI** (23k GitHub stars): LLM-powered extraction via Ollama gemma4 (free, local). Slower (~30-60s) but produces dramatically cleaner output — strips ads, nav, boilerplate via SmartScraperGraph. Used for quality-sensitive research extraction where SNR matters. See [[entities/scrapegraphai]].

- **Architecture** (`web.extract_backend` config): search and extract now route independently — web_search stays on Firecrawl (search capability), web_extract switches to Crawl4AI/ScrapeGraphAI. This eliminates credit dependency for extraction, enabling unlimited alternative data scraping for research workflows. See [[concepts/web-extraction-provider-architecture]].

**Impact on Layer 4 (Software Infrastructure):** Alternative data collection (sentiment, news, regulatory filings, earnings transcripts) is now cost-free and unbounded — no Firecrawl credit ceiling. This transforms the "Alternative data" bullet from a credit-constrained capability to an unlimited research pipeline.

### Headroom Compression

Headroom compression (see [[headroom-integration]]) was applied to the financial data pipeline:
- Compressed historical price feeds using dictionary-based token compression (approaches ~5-8x ratio on OHLCV data)
- Enabled running larger backtest windows in-memory (from ~2yr to ~10yr on same hardware)
- Headroom layer sits between data ingestion and feature engineering, transparent to downstream code

### /last30days Skill

Built `/last30days` — a Hermes skill that surfaces everything touched/modified in the last 30 days across the wiki, projects, and financial scripts. Used as a daily review tool for portfolio strategy iteration. The skill:
- Scans git history and file mtimes across wiki-personal/, projects/, and financial/ directories
- Groups changes by domain (finance, ai, infra)
- Renders a markdown summary view
- Integrated with Hermes cron for daily auto-digest

### Loop Engineering

Loop engineering (see [[loop-engineering]]) emerged as a meta-skill for financial AI development:
- **Observation → Hypothesis → Implementation → Eval → Reflect** cycles now enforced for every strategy iteration
- Self-Harness provides the eval step; wiki log provides the reflect step
- Loop rate (iterations per day) is the key metric — faster loops = faster discovery
- Applied to: strategy optimization, dashboard debugging, feature engineering experiments

## Connections to Other Questions
- [[Q05]] — Q01 foundations directly feed into predictive finance models
- [[Q03]] — accelerating learning helps acquire these skills faster
- [[Q04]] — symbolic/energy models may change what's worth learning
- [[loop-engineering]] — meta-skill for strategy iteration velocity; loop rate is the key metric
- [[headroom-integration]] — compression layer applied to financial data pipeline; enables larger backtest windows in-memory
- [[memory-tiering]] — emerging pattern for managing the growing body of findings, strategies, and eval results across hot/warm/cold tiers

### New Finance Theory Depth — Mean-Variance Myopia, PCA+RMT, and Smart Money Concepts

Added three new concept/source pages that deepen Layers 1–2 and provide practical filtering approaches:

**Mean-Variance Myopia Under Stochastic Volatility** ([[wiki/concepts/mean-variance-myopia-under-stochastic-volatility]], June 30): The static M-V efficient frontier is the myopic special case of the full intertemporal portfolio problem. Under stochastic volatility, optimal demand = myopic M-V + intertemporal hedging term. All three SV models tested (Stein/Stein, Heston, extended Heston+CEV) produce positive hedging demand. Key practical insight: our [[mean-variance-analyzer]] computes the myopic baseline correctly but underestimates hedging demand for horizons > 1 month under SV. The Heston model via EKF ([[sources/optimal-investment-stochastic-volatility-chiarella-hsiao]]) enables latent volatility estimation from equity returns alone — no options data needed.

**PCA + Random Matrix Theory** ([[sources/pca-random-matrix-theory-equity-markets]], June 27): The S&P 500's 125,250 covariance entries collapse to 5–15 real eigenportfolios via Marchenko-Pastur screening. Everything else is noise. Practical implication for Layer 2 (factor models): principled factor count selection (vs arbitrary K or %-variance thresholds). The eigenportfolio + residual trading pattern is exactly what stat-arb funds do — factor-hedged mean reversion.

**Smart Money Concepts ICT in Python** ([[sources/smart-money-concepts-ict-python]], June 29): 1.8k-star Python package implementing ICT-based OHLC pattern detection. Key extractable ideas: (a) Order Block lifecycle as a general zone state machine (active → breaker → invalidated) — applicable to statistical zones from PCA eigenportfolio bands, not just exact price levels; (b) FVG on factor-hedged residuals — detecting gaps in idiosyncratic returns after stripping the 5–15 eigenportfolio factors, making Fair Value Gaps more tradeable; (c) session-aware analysis as a complement to vol regime modeling. The package itself has no statistical validation — these are ideas worth extracting, not ready-made signals.

### New Paper: FinAcumen — Selective Experience Memory for Financial Reasoning

[[raw/papers/2606.17642]] (June 16, arXiv:2606.17642): FinAcumen is a financial reasoning agent framework using a **self-evolving experience memory harness** with τ-gated selective retrieval. Key architectural contributions:

1. **Self-evolving memory bank**: accumulates experience from prior trajectories, distills successful strategies AND failure-derived cautionary rules
2. **τ-gated selective retrieval**: memory is only activated when semantic relevance exceeds a calibrated threshold — prevents irrelevant memories from degrading performance
3. **Deterministic financial tool environment**: numerical computation, retrieval, visual decoding, answer verification — all grounded, not LLM-guessed

This is relevant to Layer 4 (Software Infrastructure) and Layer 5 (Research + Iteration) for finance skill-building. The thresholded memory retrieval pattern is more sophisticated than naive RAG for financial reasoning — particularly important because financial data is noisy and irrelevant memories are costly.

**Key connection to existing work:** The τ-gated approach complements our Self-Harness pattern for financial scripts. Self-Harness provides execution-time verification; FinAcumen's memory harness provides pre-execution context selection. Both could compose: retrieve relevant experience → verify against Self-Harness eval criteria → execute.

## Last Updated
_2026-07-01_ — Added: Mean-Variance Myopia under stochastic volatility paper, PCA+RMT for factor models, Smart Money Concepts ICT patterns, and FinAcumen financial reasoning agent (τ-gated selective memory harness)
_2026-06-24_ — Added: Web Extraction Infrastructure section (Crawl4AI + ScrapeGraphAI free alternative data pipelines) within June 2026 findings
_2026-06-13_ — June 2026 findings: Causal AI pipeline deepening, Self-Harness applied, dashboard fixes, Headroom compression, /last30days skill, loop engineering
