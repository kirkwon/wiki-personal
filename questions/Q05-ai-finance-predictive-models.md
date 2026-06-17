---
tags: [permanent-question, research, ai-finance]
created: 2026-05-25
question: "How can modern AI add to predictive models that incorporate: risk (VaR, CVaR), options (greek exposure, implied vol surfaces), volume/order book, cyclical patterns (seasonality, macro cycles), and behavioral/irrational behavior? What's the gap between academic finance ML and practitioner use?"
type: permanent-question
reviewed: 2026-06-12
status: Active - accumulating
---

# Q05: AI + Finance Predictive Models

## Question
*How can modern AI add to predictive models that incorporate: risk (VaR, CVaR), options (greek exposure, implied vol surfaces), volume/order book, cyclical patterns (seasonality, macro cycles), and behavioral/irrational behavior? What's the gap between academic finance ML and practitioner use?*

## Current State of Knowledge

### The Gap: Academic vs. Practitioner
Academic finance ML papers usually:
- Backtest on clean, survivorship-bias-free data
- Ignore transaction costs and slippage
- Use in-sample validation that overfits to noise
- Test on a single asset class or period
- Miss regime changes (2008, 2020)

Practitioners who survive add:
- Strict out-of-sample + walk-forward validation
- Transaction cost modeling from the start
- Regime-aware modeling (hidden Markov, change-point detection)
- Multi-asset, multi-factor context
- Risk overlay on top of alpha model

### Specific Factor Categories

**1. Risk (VaR, CVaR)**
- Traditional: Historical simulation, parametric VaR, Monte Carlo
- ML opportunity: Use deep learning for tail risk modeling (generative models for scenario generation, VAE/GAN for fat-tailed distributions, neural networks for CVaR optimization)
- Key challenge: VaR is not coherent. ML could help bridge to CVaR/ES optimization
- State of art: Jump-diffusion models (Bates model) + DL for calibration

**2. Options (Greeks, IV Surfaces)**
- Implied volatility surface is rich — contains information about forward-looking sentiment, risk appetite
- IV surface dynamics: sticky strike vs sticky delta behavior
- ML opportunity:
  - Volatility surface forecasting (LSTM, Transformer on IV time series)
  - Greeks hedging with ML (learn hedge ratios that adapt to market regime)
  - Arbitrage-free neural SDEs for IV surface modeling (Gentile et al., 2021)
  - Using deep hedging (Buehler et al.) — learn optimal hedging strategies via RL
- Practical: Options flow data (Cboe) — ML for detecting unusual activity

**3. Volume / Order Book**
- Order book dynamics are high-dimensional, non-linear
- ML opportunity:
  - Mid-price prediction from order book imbalance (deep learning on limit order data)
  - Trade classification (aggressive vs passive) using ML
  - Market impact modeling — how does your own trade move the market?
  - VPIN (Volume-synchronized Probability of Informed Trading) — can be ML-enhanced
- Known: simple logistic regression on order flow can predict direction
- State of art: Temporal Convolutional Networks on L2 data

**4. Cyclical Patterns**
- Traditional: ARIMA, seasonal decomposition, Fourier analysis
- ML opportunity:
  - Detect regime transitions (HMM, change-point detection via deep learning)
  - Multi-scale cycle detection (wavelet decomposition + ML)
  - Cross-asset cycle relationships (credit vs equity cycles)
  - Macro regime classification (growth, inflation, risk-off) — often discrete states
- Key: cycles are non-stationary. ML models must adapt.

**5. Behavioral / Irrational Behavior**
- Traditional: Factor models for value/growth, momentum, sentiment
- ML opportunity:
  - Text/sentiment from news, earnings calls, social media (LLM-based)
  - Options market signals for fear/recklessness (IV vs realized vol spread)
  - Retail vs institutional flow detection
  - Anchoring, disposition effect — can we measure these in aggregate?
- Key: Behavioral signals are noisy and short-lived. ML can help but false signals abound.

### Hybrid Approaches That Work

1. **Deep Order Book Models** — Use CNN or Transformer on tick data (LOB representation). Predict mid-price moves.
2. **Attention-Based Time Series** — Temporal Fusion Transformer (TFT) for interpretable multi-horizon forecasting.
3. **Reinforcement Learning for Portfolio** — Learn allocation policies that account for transaction costs and risk constraints.
4. **Generative Models for Scenarios** — Train VAE/GAN on historical returns to generate plausible scenarios for stress testing.
5. **Graph Neural Networks for Market Networks** — Model asset relationships as graphs, predict spillover effects.

### What's NOT Working (Common Pitfalls)
- Transformers on daily price data (too little signal, too much noise)
- LSTM on short time series (overfitting to noise)
- Predicting returns directly (stationarity problems) — predict signals, then convert
- Ignoring regime (training on full history including different regimes)



## Implementation Progress — June 2026

### 1. Causal AI Pipeline (DoWhy + EconML)

The causal ML framework has been operationalized into a production pipeline:

**DoWhy 4-Step Refutation for Factor Models:**
1. **Model** — DAG encoding factor → returns relationships with confounders (market regime, liquidity, risk appetite)
2. **Identify** — do-calculus to verify causal estimand is identifiable from observational data
3. **Estimate** — backdoor adjustment + linear regression for continuous treatment, propensity score matching for binary treatment
4. **Refute** — bootstrap refutation (add random common cause), placebo treatment (replace treatment with random variable), data subset refutation (split by regime)

**EconML CATE for Regime-Dependent Effects:**
- Causal Forest for heterogeneous treatment effects — e.g., does momentum factor alpha differ in high-vol vs low-vol regimes?
- DML (Double Machine Learning) with orthogonalization to debias factor attribution
- Metalearners (S-, T-, X-Learners) for estimating Conditional Average Treatment Effects on individual instruments

**Results so far**: Momentum factor shows significant causal effect only in trending regimes (R² > 0.4); breaks down in choppy / mean-reverting markets. Size factor has weaker causal identifiability (confounded by liquidity). Value factor's causal effect is regime-dependent — positive in recovery phases, negative in late-cycle.

### 2. Self-Harness Enhancement for Financial Scripts

Applied the Self-Harness pattern (CLI wrapper + structured logging + retry + deterministic fallback) to core data pipeline scripts:

- **fetch_yf.py** — Yahoo Finance data fetcher. Added: argparse CLI for ticker/date params, rich-structured logging, exponential backoff retry on API failures, deterministic fallback to cached data
- **pull_macro_data.py** — Macroeconomic data ingestion. Added: same Self-Harness pattern with FRED API retry, stale-data fallback, formatted output tables

Both scripts now pass through a harness layer providing: `--verbose`, `--log-file`, `--max-retries`, `--dry-run` flags; unified error handling; structured JSON logging for downstream pipeline consumption.

### 3. Headroom Compression for Backtesting

Implemented columnar compression on OHLCV time-series data achieving **5-8x compression ratios**:
- Delta encoding on price columns (small changes → small integers)
- Zigzag encoding + varint packing for variable-length integers
- Dictionary encoding on symbol column
- Frame-of-reference (FOR) per trading session

**Impact**: Enables 10-year backtest windows on intraday OHLCV data that previously required subsampling or streaming. Memory footprint for a 10yr 1-min OHLCV universe (500 tickers) reduced from ~18 GB to ~2.8 GB.

### 4. Portfolio Dashboard

Built multi-view dashboard covering:
- **Allocation view** — Current vs target weights, drift tracking, rebalance triggers
- **Concentration view** — Herfindahl-Hirschman Index (HHI), top holding %, sector concentration
- **Tax view** — Realized/unrealized gains, tax-lot tracking, wash sale detection
- Backfilled 30+ tickers with 5yr history from the Self-Harness data pipeline

Dashboard is plotly-based, rendered as HTML static export for daily review.

### 5. Loop Engineering: Critic Separation for Backtest Validation

Introduced a separate **critic model** in the backtest loop to detect:
- Look-ahead bias (future information leaking into signal computation)
- Survivorship bias (stratified by ticker tenure)
- Overfitting indicators (train/test performance divergence, min Sharpe ratio thresholds)
- Regime-shift sensitivity (performance breakdown by volatility regime)

The critic runs *after* each backtest iteration, independent of the strategy loop, and produces a validation report. If the critic flags systematic issues, the backtest is marked as "needs review" rather than accepted. This separation prevents the signal model from optimizing against the validation criteria.

## Causal ML — The Most Underused Addition to Finance ML

The gap between academic and practitioner finance ML is largely causal:

**The problem**: Most ML models find *correlations* in historical data. When markets change
(economic regime, structural change, crisis), these correlations break. A causal model
distinguishes between "this factor causes returns" and "this factor just happens to
correlate with returns in this sample."

**Confounders in finance** — A confounder causes both treatment (factor exposure) and
outcome (returns). Common confounders:
- Market regime (causes both factor attractiveness AND returns)
- Liquidity (affects factor signal AND execution costs)
- Risk appetite (affects both factor popularity and market direction)

**Microsoft DoWhy** (https://www.microsoft.com/en-us/research/project/dowhy/):
The four-step approach:
1. **Model** — Encode your assumptions as a causal graph (DAG)
2. **Identify** — Does the causal effect exist? Use do-calculus to check.
3. **Estimate** — Instrumental variables, matching, stratification
4. **Refute** — Placebo tests, sensitivity analysis

**Example for factor investing**:
- Treatment: High exposure to momentum factor
- Outcome: Risk-adjusted returns
- Confounders: Market regime, liquidity conditions
- DoWhy can tell you: given my causal graph, is the measured effect the true causal effect?

**EconML** — Microsoft's extension for heterogeneous treatment effects:
- Does a strategy work differently in high-vol vs low-vol regimes? Quantify it.
- What is the *average treatment effect* of adding a factor to an existing portfolio?

**Key papers**:
1. Sharma & Kiciman — "DoWhy: An End-to-End Library for Causal Inference" (arXiv:2011.04216)
2. Pearl — "Causality" (2009) — structural causal models, do-calculus
3. Pearl, Glymour, Jewell — "Causal Inference in Statistics: A Primer" (2016)
4. Imbens & Angrist — "Identification and Average Treatment Effects" (1994, LATE theorem)

**The practical test**: Before claiming alpha, use DoWhy's refutation tools:
- Add random confounders — does the effect survive?
- Placebo test — does the "effect" appear in placebo treatments?
- Bootstrap — how sensitive is the effect to perturbations?

## Key Papers / Resources
- Buehler et al. — "Deep Hedging" (2019) — RL for derivatives hedging
- Gentil et al. — "Arbitrage-Free Neural SDEs for IV Surface Modeling" (2021)
- Lim et al. — "Temporal Fusion Transformer" — interpretable multi-horizon forecasting
- López de Prado — *Advances in Financial Machine Learning*
- Filippov et al. — "Deep Order Book Networks" — CNN on LOB data
- Arai — "Deep Learning for Order Flow" — predicting trade direction

## Emerging Methodology

Three-layer model design:
1. **Signal Layer** — Separate models for vol, flow, sentiment, cycles
2. **Combination Layer** — How signals combine (attention, ensemble, meta-learner)
3. **Risk Layer** — Risk overlay that limits drawdowns regardless of alpha forecasts

Key insight: **Predict regimes, not returns.** Regime classification (bull/bear, high/low vol, risk-on/risk-off) is more robust and actionable.

## Connections to Other Questions
- [[Q01]] — foundational skills needed to build these models properly
- [[Q03]] — accelerated learning needed to stay current with rapidly evolving methods
- [[Q04]] — symbolic models may help with interpretability and causality
- [[loop-engineering]] — critic separation and Self-Harness patterns applied to backtest validation
- [[headroom-integration]] — columnar compression enabling long-window backtests

## Last Updated
_2026-06-12_ — Added implementation progress: causal AI pipeline (DoWhy 4-step + EconML CATE), Self-Harness for data scripts, headroom compression (5-8x), portfolio dashboard, critic separation for backtest validation
