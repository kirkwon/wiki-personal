---
tags: [permanent-question, research]
created: 2026-05-25
question: "How can modern AI add to predictive models that incorporate: risk (VaR, CVaR), options (greek exposure, implied vol surfaces), volume/order book, cyclical patterns (seasonality, macro cycles), and behavioral/irrational behavior? What's the gap between academic finance ML and practitioner use?"
date: 2026-05-25
type: note
reviewed: 2026-09-02
confidence: 0.95
evidence_count: 181
last_evidence_date: 2026-09-09
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

### 6. Web Extraction Infrastructure — Free Alternative Data Pipelines

Deployed free, local web extraction backends (Crawl4AI + ScrapeGraphAI) via Hermes's pluggable Web Extraction Provider Architecture. This eliminates the Firecrawl credit dependency for extraction, enabling unbounded alternative data collection for predictive models:

| Backend | Speed | Quality | Use Case |
|---------|-------|---------|----------|
| [[entities/crawl4ai]] | ~1-4s/URL | Good (heuristic markdown) | Default extraction — news, filings, earnings transcripts |
| [[entities/scrapegraphai]] | ~30-60s/URL | Best (LLM-filtered) | Quality-sensitive research — sentiment, structured data |

**Impact on Q05 predictive models:**
- Sentiment extraction from earnings calls, news, and social media is now cost-free
- Regulatory filing analysis (SEC EDGAR, international equivalents) — unlimited extraction scale
- Options data provider scraping — alternative sources for IV surfaces and flow data
- Macro data from central bank and government sources — automated ingestion pipelines

See [[concepts/web-extraction-provider-architecture]] for the architecture, [[entities/crawl4ai]] and [[entities/scrapegraphai]] for tool details.

### 7. Game-Theoretic Finance Analysis — Gap Identified and Started

The [[wiki/gaps/game-theory-gaps|Game Theory Gaps]] audit (2026-06-21) identified **GAP-1: No Game-Theoretic Finance Analysis** as the highest-leverage gap across all agent skills:

**Problem identified:** Current finance skills treat markets as optimization or description problems. No skill models: Who are the players? What are their payoffs? What's the equilibrium? What move exploits mispricing?

**Missing capabilities identified:**
- Player belief modeling (what does the other side believe?)
- Payoff matrix construction for market scenarios
- Nash equilibrium computation for competitive dynamics
- Signaling game analysis (what do options flows signal about informed traders?)
- Mechanism design for trade execution (optimal order splitting as a game against predatory strategies)
- Agent-based market simulation to test strategies against adaptive opponents

**Status:** STARTED (2026-06-21). A new `game-theoretic-finance-analysis` skill has been created to operationalize this. The project is in early stage — see the skill for current progress.

**Connection to CWM pattern:** The [[wiki/synthesis/cwm-game-theory-application|CWM Game Theory Application]] synthesis maps the Lehrach et al. CWM pattern to financial decision-making: encode market rules as executable code, then use classical solvers (MCTS, game tree search) rather than direct LLM prediction. This is an architectural template for the game-theoretic finance analysis skill.

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
- [[concepts/web-extraction-provider-architecture]] — free alternative data pipelines for predictive models
- [[entities/crawl4ai]] — fast, free local extraction backend
- [[entities/scrapegraphai]] — LLM-powered extraction for quality-sensitive research
- [[wiki/gaps/game-theory-gaps]] — GAP-1: game-theoretic finance analysis (started)
- [[wiki/synthesis/cwm-game-theory-application]] — CWM pattern mapped to financial strategic decision-making

## Last Updated
_2026-06-24_ — Added: Web extraction infrastructure (free alternative data pipelines via Crawl4AI/ScrapeGraphAI). Added game-theoretic finance analysis (GAP-1, started). Updated Connections with new references.
_2026-06-12_ — Added implementation progress: causal AI pipeline (DoWhy 4-step + EconML CATE), Self-Harness for data scripts, headroom compression (5-8x), portfolio dashboard, critic separation for backtest validation

## Evidence Log

<!-- Weekly scan appends dated evidence blocks below this line.
     Format: ### YYYY-MM-DD: <topic>
             - Finding
             - Source: [[wikilink]] or URL
             - Confidence: High/Medium/Low
-->

### 2026-06-12: Causal ML pipeline — DoWhy refutation catches spurious factors
- DoWhy 4-step (model → identify → estimate → refute) applied to factor investing. EconML DML for CATE: which market conditions does a factor work in, not just whether it works. Practical test: placebo treatment + random confounder refutation before claiming alpha.
- Source: [[DoWhy]] [[EconML]]
- Confidence: High

### 2026-06-21: Game-theoretic finance analysis — GAP-1 identified and started
- No existing skill models markets as games: player beliefs, payoff matrices, Nash equilibria, signaling games, mechanism design for execution. New game-theoretic-finance-analysis skill created to address this highest-leverage gap.
- Source: [[wiki/gaps/game-theory-gaps]]
- Confidence: Medium

### 2026-06-24: Free alternative data pipelines unbound sentiment/flow analysis
- Crawl4AI + ScrapeGraphAI eliminate Firecrawl credit dependency. Earnings call sentiment, SEC filing analysis, options flow scraping, macro data ingestion — all now cost-free at unlimited scale. Transforms predictive model feature engineering.
- Source: [[concepts/web-extraction-provider-architecture]]
- Confidence: High

### 2026-06-16: FinAcumen — τ-gated selective memory for financial reasoning

### 2026-07-03: Parameter-Efficient Quantum-Inspired Fast Weight Programmers for Traffic-Matrix 

### 2025-07-21: Quantitative Risk Management in Volatile Markets with an Expectile-Based

### 2025-08-27: Forecasting Probability Distributions of Financial Returns with Deep

### 2025-09-15: QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading

### 2025-10-03: TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis

### 2026-07-28: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social

### 2025-10-08: A Contextual Quality Reward Model for Reliable and Efficient Best-of-N

### 2025-11-18: Genomic Next-Token Predictors are In-Context Learners

### 2025-12-05: QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory

### 2025-12-11: Towards a Science of Scaling Agent Systems

### 2025-12-11: Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware ROI Pred

### 2025-12-19: Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment with Na

### 2026-02-10: AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents

### 2026-03-18: I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Prob

### 2026-04-02: QuitoBench: A High-Quality Open Time Series Forecasting Benchmark

### 2026-05-15: Nexus : An Agentic Framework for Time Series Forecasting

### 2026-06-03: Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment 

### 2026-07-28: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social

### 2026-08-03: In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous Driving

### 2026-08-03: One Future, Every Robot: Label-Efficient Collective-State Prediction with Decent

### 2026-08-03: ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

### 2026-08-03: N_0-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulatio

### 2026-08-03: SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark fo

### 2026-08-03: Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts 

### 2026-08-03: ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamic

### 2026-08-03: Multi-Head Attention Residuals

### 2026-08-03: Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generati

### 2026-08-04: SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space

### 2026-08-04: ICDAR 2026 Competition on Information Extraction from Atomic Layer Deposition/Et

### 2026-08-04: A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples

### 2026-08-04: DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered Video Diff

### 2026-08-04: GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Ti

### 2026-08-04: 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D Question 

### 2026-08-04: WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning
- HF trending paper (arxiv: 2607.29613). Keywords: regression. Status: pending-review.
- Source: [[papers/2607.29613]] | https://huggingface.co/papers/2607.29613
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01185). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.01185]] | https://huggingface.co/papers/2608.01185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02585). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2608.02585]] | https://huggingface.co/papers/2608.02585
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00486). Keywords: attention, forecast, prediction. Status: pending-review.
- Source: [[papers/2608.00486]] | https://huggingface.co/papers/2608.00486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29122). Keywords: transformer, prediction. Status: pending-review.
- Source: [[papers/2607.29122]] | https://huggingface.co/papers/2607.29122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26848). Keywords: classification. Status: pending-review.
- Source: [[papers/2607.26848]] | https://huggingface.co/papers/2607.26848
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01397). Keywords: forecast, prediction. Status: pending-review.
- Source: [[papers/2608.01397]] | https://huggingface.co/papers/2608.01397
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27372). Keywords: deep learning, prediction. Status: pending-review.
- Source: [[papers/2607.27372]] | https://huggingface.co/papers/2607.27372
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27230). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2607.27230]] | https://huggingface.co/papers/2607.27230
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28362). Keywords: prediction. Status: pending-review.
- Source: [[papers/2607.28362]] | https://huggingface.co/papers/2607.28362
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28308). Keywords: prediction. Status: pending-review.
- Source: [[papers/2607.28308]] | https://huggingface.co/papers/2607.28308
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28996). Keywords: deep learning. Status: pending-review.
- Source: [[papers/2607.28996]] | https://huggingface.co/papers/2607.28996
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23783). Keywords: transformer, prediction. Status: pending-review.
- Source: [[papers/2607.23783]] | https://huggingface.co/papers/2607.23783
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27924). Keywords: prediction. Status: pending-review.
- Source: [[papers/2607.27924]] | https://huggingface.co/papers/2607.27924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28443). Keywords: prediction. Status: pending-review.
- Source: [[papers/2607.28443]] | https://huggingface.co/papers/2607.28443
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.15820). Keywords: trend. Status: pending-review.
- Source: [[papers/2607.15820]] | https://huggingface.co/papers/2607.15820
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23370). Keywords: forecasting, regime detection, sentiment. Status: pending-review.
- Source: [[papers/2607.23370]] | https://huggingface.co/papers/2607.23370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.01770). Keywords: forecasting. Status: pending-review.
- Source: [[papers/2606.01770]] | https://huggingface.co/papers/2606.01770
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.14389). Keywords: forecasting, time series. Status: pending-review.
- Source: [[papers/2605.14389]] | https://huggingface.co/papers/2605.14389
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.26017). Keywords: forecasting, time series. Status: pending-review.
- Source: [[papers/2603.26017]] | https://huggingface.co/papers/2603.26017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.15670). Keywords: factor model. Status: pending-review.
- Source: [[papers/2603.15670]] | https://huggingface.co/papers/2603.15670
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06855). Keywords: forecasting, time series. Status: pending-review.
- Source: [[papers/2602.06855]] | https://huggingface.co/papers/2602.06855
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.11251). Keywords: forecasting, time series. Status: pending-review.
- Source: [[papers/2512.11251]] | https://huggingface.co/papers/2512.11251
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05402). Keywords: time series. Status: pending-review.
- Source: [[papers/2512.05402]] | https://huggingface.co/papers/2512.05402
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.08296). Keywords: predictive model. Status: pending-review.
- Source: [[papers/2512.08296]] | https://huggingface.co/papers/2512.08296
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05049). Keywords: forecasting. Status: pending-review.
- Source: [[papers/2512.05049]] | https://huggingface.co/papers/2512.05049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.12797). Keywords: predictive model. Status: pending-review.
- Source: [[papers/2511.12797]] | https://huggingface.co/papers/2511.12797
- Confidence: Low (auto-matched, not yet reviewed)
  Samplin
- HF trending paper (arxiv: 2510.04087). Keywords: sentiment. Status: pending-review.
- Source: [[papers/2510.04087]] | https://huggingface.co/papers/2510.04087
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23370). Keywords: forecasting, regime detection, sentiment. Status: pending-review.
- Source: [[papers/2607.23370]] | https://huggingface.co/papers/2607.23370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.01538). Keywords: forecasting, time series. Status: pending-review.
- Source: [[papers/2510.01538]] | https://huggingface.co/papers/2510.01538
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.09995). Keywords: sentiment. Status: pending-review.
- Source: [[papers/2509.09995]] | https://huggingface.co/papers/2509.09995
- Confidence: Low (auto-matched, not yet reviewed)
  Neural Ne
- HF trending paper (arxiv: 2508.18921). Keywords: forecasting. Status: pending-review.
- Source: [[papers/2508.18921]] | https://huggingface.co/papers/2508.18921
- Confidence: Low (auto-matched, not yet reviewed)
  Frame
- HF trending paper (arxiv: 2507.13391). Keywords: time series. Status: pending-review.
- Source: [[papers/2507.13391]] | https://huggingface.co/papers/2507.13391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.27821). Keywords: forecasting. Status: pending-review.
- Source: [[papers/2606.27821]] | https://huggingface.co/papers/2606.27821
- Confidence: Low (auto-matched, not yet reviewed)
- Self-evolving experience memory with threshold-gated retrieval. Memory only activates when semantic relevance exceeds calibrated τ — prevents irrelevant memories from degrading performance. Composes with Self-Harness: retrieve relevant experience → verify → execute.
- Source: arXiv:2606.17642
- Confidence: Medium

### 2026-08-05: Applied causal inference (Pearl/DoWhy/EconML) for risk management and portfolio construction, building toward an autonomous causal hedge signal generator.
- Source: [[causal-ai-hedge-agent.md]]
- Confidence: Medium

### 2026-08-05: Loop engineering is the practice of structuring agent improvement as a closed-loop system with a **critic/doer separation** — one component acts, another validates. This separation enables the agent t...
- Source: [[loop-engineering.md]]
- Confidence: Low

### 2026-08-05: Centralized blog draft pipeline: 2 active drafts, 12 verified candidates across 3 tiers, organized into thematic series.

### 2026-08-05: Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-B

### 2026-08-05: MiniWorld: Democratizing the Training of Video World Models from Scratch

### 2026-08-05: LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

### 2026-08-05: ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visua

### 2026-08-05: Quo Vadis, World Modeling?

### 2026-08-05: Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for Streaming Rec

### 2026-08-05: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Lear

### 2026-08-05: Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via Repre

### 2026-08-05: InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthe

### 2026-08-06: SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in Multimodal Large

### 2026-08-06: Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Ear

### 2026-08-06: Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Sele

### 2026-08-06: HelloWorld: Enabling Socially Interactive Characters in Video World Models

### 2026-08-06: ARCHead: Activation-Metric Residual Correction for Large Language Model Output H

### 2026-08-07: Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulu

### 2026-08-07: Task-Conditional Flow Matching for Balanced Multilingual Text Embedding Adaptati

### 2026-08-07: PaDoc: Layout-Grounded Parallel Decoding for Document Parsing

### 2026-08-07: World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Ma

### 2026-08-07: DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for C

### 2026-08-07: Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised Wor

### 2026-08-08: FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channel

### 2026-08-10: FATE: Frame-Level Audio-Visual Temporal Embedding

### 2026-08-10: Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence

### 2026-08-10: Towards Interpretable Foundation Models for Retinal Fundus Images

### 2026-08-10: YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family

### 2026-08-10: SimWAM: A Simple World Action Model for End-to-End Autonomous Driving

### 2026-08-10: Uncertainty-Aware World Model for Aerial Image-Goal Navigation

### 2026-08-10: Modular TTT: Rethinking Test-Time Training as Composable Modules

### 2026-08-10: Skaling: Chinchilla's Exponents Meet Kaplan's Coupling

### 2026-08-10: Addressable Memory for Video World Models

### 2026-08-11: The Loss Does Not See the Basis, but Adam Does

### 2026-08-11: Vision-Language Grounding as Bidirectional Concept Correspondence

### 2026-08-11: OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching

### 2026-08-11: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

### 2026-08-12: Power law graph attention: exact generalization of scaled dot-product attention,

### 2026-08-12: iFAN: Inference-Aware Learning for Plain Mask Transformers

### 2026-08-12: TSDS-Toolbox: A Toolbox for Measuring Time-Series Dataset Similarity

### 2026-08-12: Beyond Pixels: From Video Priors to 4D Worlds

### 2026-08-12: VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model w

### 2026-08-12: Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers

### 2026-08-12: The Loss Does Not See the Basis, but Adam Does

### 2026-08-12: Vision-Language Grounding as Bidirectional Concept Correspondence

### 2026-08-12: OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching

### 2026-08-12: RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance

### 2026-08-13: Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop

### 2026-08-13: Simplex Relaxation for Discrete Diffusion

### 2026-08-13: AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models

### 2026-08-14: Mitigating Gender Bias in English to Romanian Machine Translation

### 2026-08-14: TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation wi

### 2026-08-14: An AI4AI Framework for Visual Token Pruning

### 2026-08-14: UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos

### 2026-08-14: LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time

### 2026-08-14: DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation

### 2026-08-14: Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attent

### 2026-08-14: Full-bandwidth transformer

### 2026-08-14: Alaya-EVOKE: From Linear-Scaling Supervision to Endless World

### 2026-08-14: Intern-S2-Preview: Scientific Agentic Foundation Model

### 2026-08-14: From Atomic Evidence to Logical Composition: Structured Compositional Reasoning 

### 2026-08-14: Gaze Target Estimation Anywhere with Concepts

### 2026-08-15: Maglev: Sliding Recurrent Memory

### 2026-08-17: A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientif

### 2026-08-17: UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Mu

### 2026-08-17: Generation as Auxiliary Supervision: Enhancing Visual Understanding at Zero Infe

### 2026-08-17: Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning

### 2026-08-18: Valid Per-Field Selective Risk Control for Document Extraction: Three Failure Mo

### 2026-08-18: MOSS-VL Technical Report

### 2026-08-18: Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe Ac

### 2026-08-18: HiFi-BRep: High-Fidelity Latent Representation for Robust B-Rep Generation

### 2026-08-18: Drive, Pack, Fly: The Travelling Thief Problem with Drone

### 2026-08-18: Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable

### 2026-08-18: An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models

### 2026-08-18: Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped Tr
- HF trending paper (arxiv: 2608.13987). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2608.13987]] | https://huggingface.co/papers/2608.13987
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16887). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.16887]] | https://huggingface.co/papers/2608.16887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15022). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.15022]] | https://huggingface.co/papers/2608.15022
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16435). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.16435]] | https://huggingface.co/papers/2608.16435
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16485). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.16485]] | https://huggingface.co/papers/2608.16485
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15037). Keywords: regression. Status: pending-review.
- Source: [[papers/2608.15037]] | https://huggingface.co/papers/2608.15037
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15045). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.15045]] | https://huggingface.co/papers/2608.15045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14639). Keywords: regression. Status: pending-review.
- Source: [[papers/2608.14639]] | https://huggingface.co/papers/2608.14639
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14290). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.14290]] | https://huggingface.co/papers/2608.14290
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12209). Keywords: transformer, prediction. Status: pending-review.
- Source: [[papers/2608.12209]] | https://huggingface.co/papers/2608.12209
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10835). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.10835]] | https://huggingface.co/papers/2608.10835
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14075). Keywords: classification. Status: pending-review.
- Source: [[papers/2608.14075]] | https://huggingface.co/papers/2608.14075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02870). Keywords: transformer, attention, prediction. Status: pending-review.
- Source: [[papers/2608.02870]] | https://huggingface.co/papers/2608.02870
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11367). Keywords: transformer, prediction. Status: pending-review.
- Source: [[papers/2608.11367]] | https://huggingface.co/papers/2608.11367
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12836). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.12836]] | https://huggingface.co/papers/2608.12836
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13505). Keywords: forecasting, time series, forecast. Status: pending-review.
- Source: [[papers/2608.13505]] | https://huggingface.co/papers/2608.13505
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13546). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.13546]] | https://huggingface.co/papers/2608.13546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08888). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2608.08888]] | https://huggingface.co/papers/2608.08888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12149). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.12149]] | https://huggingface.co/papers/2608.12149
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13489). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.13489]] | https://huggingface.co/papers/2608.13489
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11745). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2608.11745]] | https://huggingface.co/papers/2608.11745
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11752). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.11752]] | https://huggingface.co/papers/2608.11752
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07193). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.07193]] | https://huggingface.co/papers/2608.07193
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11951). Keywords: deep learning, prediction, anomaly detection, regression. Status: pending-review.
- Source: [[papers/2608.11951]] | https://huggingface.co/papers/2608.11951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08606). Keywords: transformer, classification. Status: pending-review.
- Source: [[papers/2608.08606]] | https://huggingface.co/papers/2608.08606
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06729). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.06729]] | https://huggingface.co/papers/2608.06729
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10615). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.10615]] | https://huggingface.co/papers/2608.10615
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11215). Keywords: prediction, trend. Status: pending-review.
- Source: [[papers/2608.11215]] | https://huggingface.co/papers/2608.11215
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09853). Keywords: attention, prediction, regression. Status: pending-review.
- Source: [[papers/2608.09853]] | https://huggingface.co/papers/2608.09853
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08097). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.08097]] | https://huggingface.co/papers/2608.08097
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07886). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.07886]] | https://huggingface.co/papers/2608.07886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06111). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2608.06111]] | https://huggingface.co/papers/2608.06111
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08477). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.08477]] | https://huggingface.co/papers/2608.08477
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10744). Keywords: transformer, attention, prediction. Status: pending-review.
- Source: [[papers/2608.10744]] | https://huggingface.co/papers/2608.10744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08119). Keywords: forecasting, forecast, classification. Status: pending-review.
- Source: [[papers/2608.08119]] | https://huggingface.co/papers/2608.08119
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03216). Keywords: transformer, prediction. Status: pending-review.
- Source: [[papers/2608.03216]] | https://huggingface.co/papers/2608.03216
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10288). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.10288]] | https://huggingface.co/papers/2608.10288
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09853). Keywords: attention, prediction, regression. Status: pending-review.
- Source: [[papers/2608.09853]] | https://huggingface.co/papers/2608.09853
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08097). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.08097]] | https://huggingface.co/papers/2608.08097
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07886). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.07886]] | https://huggingface.co/papers/2608.07886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07408). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.07408]] | https://huggingface.co/papers/2608.07408
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07222). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.07222]] | https://huggingface.co/papers/2608.07222
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07110). Keywords: sequence model. Status: pending-review.
- Source: [[papers/2608.07110]] | https://huggingface.co/papers/2608.07110
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05597). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.05597]] | https://huggingface.co/papers/2608.05597
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07468). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.07468]] | https://huggingface.co/papers/2608.07468
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07051). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.07051]] | https://huggingface.co/papers/2608.07051
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.18846). Keywords: prediction. Status: pending-review.
- Source: [[papers/2603.18846]] | https://huggingface.co/papers/2603.18846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06756). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.06756]] | https://huggingface.co/papers/2608.06756
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01310). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.01310]] | https://huggingface.co/papers/2608.01310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01049). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.01049]] | https://huggingface.co/papers/2608.01049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04378). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.04378]] | https://huggingface.co/papers/2608.04378
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06374). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.06374]] | https://huggingface.co/papers/2608.06374
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05369). Keywords: forecast, prediction. Status: pending-review.
- Source: [[papers/2608.05369]] | https://huggingface.co/papers/2608.05369
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06146). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.06146]] | https://huggingface.co/papers/2608.06146
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05785). Keywords: classification. Status: pending-review.
- Source: [[papers/2608.05785]] | https://huggingface.co/papers/2608.05785
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01481). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.01481]] | https://huggingface.co/papers/2608.01481
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02703). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.02703]] | https://huggingface.co/papers/2608.02703
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05070). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.05070]] | https://huggingface.co/papers/2608.05070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04349). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.04349]] | https://huggingface.co/papers/2608.04349
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05000). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.05000]] | https://huggingface.co/papers/2608.05000
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04244). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.04244]] | https://huggingface.co/papers/2608.04244
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02437). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.02437]] | https://huggingface.co/papers/2608.02437
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03316). Keywords: regression. Status: pending-review.
- Source: [[papers/2608.03316]] | https://huggingface.co/papers/2608.03316
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01837). Keywords: trend. Status: pending-review.
- Source: [[papers/2608.01837]] | https://huggingface.co/papers/2608.01837
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02738). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.02738]] | https://huggingface.co/papers/2608.02738
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02713). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.02713]] | https://huggingface.co/papers/2608.02713
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28993). Keywords: prediction. Status: pending-review.
- Source: [[papers/2607.28993]] | https://huggingface.co/papers/2607.28993
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03457). Keywords: trend. Status: pending-review.
- Source: [[papers/2608.03457]] | https://huggingface.co/papers/2608.03457
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01127). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.01127]] | https://huggingface.co/papers/2608.01127
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02791). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.02791]] | https://huggingface.co/papers/2608.02791
- Confidence: Low (auto-matched, not yet reviewed)
- Source: [[blog-content-pipeline.md]]
- Confidence: Medium

### 2026-08-19: Conditional causal discovery for rare/tail events (UAI 2026, arXiv:2608.12640)

### 2026-08-19: PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture

### 2026-08-19: CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Represent

### 2026-08-19: V-RAE: Rethinking Video Latent Spaces for Generation

### 2026-08-19: PixRestore: Unified Image Restoration via Pixel Diffusion Transformer

### 2026-08-19: EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing

### 2026-08-19: CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Gu

### 2026-08-19: Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents

### 2026-08-19: Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning

### 2026-08-20: Temporal Multi-Signal Fusion for Token-Level Hallucination Detection

### 2026-08-20: Training Chemical Plausibility-Aware Large Language Models for Single-Step Retro

### 2026-08-20: The Problem Is the Problem: Towards Scalable Mathematical Discovery

### 2026-08-21: Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learne

### 2026-08-21: FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving

### 2026-08-21: 4DAnyone: Create Anyone in 4D from a Casual Monocular Video

### 2026-08-21: WithEveryone: Unified Planning and Identity Grounding for Group Image Generation

### 2026-08-22: TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity

### 2026-08-22: The Embedder's Dilemma: LLMs Are Better, but at What Cost?

### 2026-08-24: UniSpace: Unified Visual Representation and Scalable Multimodal Modeling

### 2026-08-24: Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference

### 2026-08-24: Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Sc

### 2026-08-24: Hadith computational science in the age of large language models: a critical nar

### 2026-08-24: InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter

### 2026-08-25: The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration

### 2026-08-25: WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning

### 2026-08-25: Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated B

### 2026-08-25: RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling

### 2026-08-25: Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selec

### 2026-08-25: Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervisi

### 2026-08-25: ReWorld: An Interactive World Model with Long-Horizon Memory

### 2026-08-25: TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration
- HF trending paper (arxiv: 2608.17336). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.17336]] | https://huggingface.co/papers/2608.17336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23565). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.23565]] | https://huggingface.co/papers/2608.23565
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16812). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.16812]] | https://huggingface.co/papers/2608.16812
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20169). Keywords: classification. Status: pending-review.
- Source: [[papers/2608.20169]] | https://huggingface.co/papers/2608.20169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22849). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.22849]] | https://huggingface.co/papers/2608.22849
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13914). Keywords: classification. Status: pending-review.
- Source: [[papers/2608.13914]] | https://huggingface.co/papers/2608.13914
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22591). Keywords: transformer, sequence model. Status: pending-review.
- Source: [[papers/2608.22591]] | https://huggingface.co/papers/2608.22591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23252). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.23252]] | https://huggingface.co/papers/2608.23252
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20910). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.20910]] | https://huggingface.co/papers/2608.20910
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20364). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.20364]] | https://huggingface.co/papers/2608.20364
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20061). Keywords: attention, regression. Status: pending-review.
- Source: [[papers/2608.20061]] | https://huggingface.co/papers/2608.20061
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20210). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.20210]] | https://huggingface.co/papers/2608.20210
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08676). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.08676]] | https://huggingface.co/papers/2608.08676
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12875). Keywords: classification. Status: pending-review.
- Source: [[papers/2608.12875]] | https://huggingface.co/papers/2608.12875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15767). Keywords: forecasting, attention, forecast. Status: pending-review.
- Source: [[papers/2608.15767]] | https://huggingface.co/papers/2608.15767
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20336). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.20336]] | https://huggingface.co/papers/2608.20336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20335). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.20335]] | https://huggingface.co/papers/2608.20335
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19758). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.19758]] | https://huggingface.co/papers/2608.19758
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19863). Keywords: transformer, attention, prediction. Status: pending-review.
- Source: [[papers/2608.19863]] | https://huggingface.co/papers/2608.19863
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16977). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.16977]] | https://huggingface.co/papers/2608.16977
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18940). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.18940]] | https://huggingface.co/papers/2608.18940
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18115). Keywords: attention, regression. Status: pending-review.
- Source: [[papers/2608.18115]] | https://huggingface.co/papers/2608.18115
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15869). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.15869]] | https://huggingface.co/papers/2608.15869
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15008). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.15008]] | https://huggingface.co/papers/2608.15008
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17566). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.17566]] | https://huggingface.co/papers/2608.17566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18063). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.18063]] | https://huggingface.co/papers/2608.18063
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16793). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.16793]] | https://huggingface.co/papers/2608.16793
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13556). Keywords: predictive model, prediction. Status: pending-review.
- Source: [[papers/2608.13556]] | https://huggingface.co/papers/2608.13556
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12944). Keywords: transformer, prediction, classification. Status: pending-review.
- Source: [[papers/2608.12944]] | https://huggingface.co/papers/2608.12944
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17379). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.17379]] | https://huggingface.co/papers/2608.17379
- Confidence: Low (auto-matched, not yet reviewed)
- Adaptive multilevel splitting estimates a posterior over causal structure conditional on rare events ("this effect is large", "variables co-occur in a tail") — the exact regime of finance joint-tail estimation where copula-style models underprice co-movement (analogous 2.5× underpricing measured for LLM co-failure tails); finance transfer is method-level, not yet validated.
- Source: [[papers/causal-discovery-effect-constraints]]
- Confidence: Medium

### 2026-08-23: Vol- and volume-aware Kelly sizing — accepted decision with resolved estimators

### 2026-08-26: Automata from Agent Traces: Failure and Next-Step Prediction

### 2026-08-26: GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with 

### 2026-08-26: MoTE: Mixture of Task Experts for Multi-Task Video Understanding

### 2026-08-26: WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report

### 2026-08-26: Best Practice Critic Optimization

### 2026-08-26: The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space,

### 2026-08-26: What AstroPT knows about galaxies, and what that can teach us about LLMs

### 2026-08-27: Prefix Sliding for efficient test-time scaling

### 2026-08-27: Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling

### 2026-08-27: LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech De

### 2026-08-27: Real-TurnTurk: A Multimodal Turkish Corpus for Turn-Taking Prediction

### 2026-08-27: Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation

### 2026-08-27: Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models

### 2026-08-27: Gated Recurrent Transformers: Expressive Depth through Recurrent Modulation

### 2026-08-27: StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Mode

### 2026-08-28: TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback

### 2026-08-28: EditaLive! Unified Character Video Editing for Live Streaming

### 2026-08-28: GameWAM: A World Action Model for Video Games

### 2026-08-28: Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Techn

### 2026-08-28: CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehensi

### 2026-08-28: Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task

### 2026-08-28: Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher

### 2026-08-28: What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents

### 2026-08-28: GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Gro

### 2026-08-30: Luce: Relightable Gaussians for 3D Asset Generation

### 2026-08-31: LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in V

### 2026-08-31: LMSM: LLM Security Framework Inspired by Linux Security Modules

### 2026-09-01: SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language Models

### 2026-09-01: Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation a

### 2026-09-01: DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution

### 2026-09-01: SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Mo

### 2026-09-01: LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigatio

### 2026-09-01: Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation

### 2026-09-01: Cross-lingual Functional Vectors for Emotion Detection in Large Language Models

### 2026-09-02: ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-

### 2026-09-02: H3-World: Turning Language Understanding into World Control

### 2026-09-03: Wasserstein-Barycentric Interaction Fields for Spatial Factor Models: Evidence f

### 2026-09-03: NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Eff

### 2026-09-03: ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes

### 2026-09-03: CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivat

### 2026-09-03: EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction

### 2026-09-03: Language Models Can Control Their Own Attention

### 2026-09-03: Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall

### 2026-09-04: Using Grounded Theory for Agent Behavior Analysis at Scale

### 2026-09-04: Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reco

### 2026-09-04: Percolation Dynamics in Optimization : Variance Cascades and Discrete Scale Inva

### 2026-09-04: Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning

### 2026-09-04: Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Hal

### 2026-09-04: Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens

### 2026-09-07: The 2026 PNPL Competition: Word Classification and Efficient Cross-Subject Gener

### 2026-09-07: UniMate: One Unified Model to Animate Diverse Skeletons

### 2026-09-07: One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Edit

### 2026-09-07: Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reason

### 2026-09-07: The Attention Triangle in Audio-Video Models

### 2026-09-07: ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding

### 2026-09-07: Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inf

### 2026-09-08: Unifying Conformal Language Tasks with In-Context Ensembles

### 2026-09-08: Causal Foundation Models

### 2026-09-08: ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation

### 2026-09-08: EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying V
- HF trending paper (arxiv: 2609.01281). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.01281]] | https://huggingface.co/papers/2609.01281
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03756). Keywords: classification. Status: pending-review.
- Source: [[papers/2609.03756]] | https://huggingface.co/papers/2609.03756
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03003). Keywords: neural network. Status: pending-review.
- Source: [[papers/2609.03003]] | https://huggingface.co/papers/2609.03003
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03005). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.03005]] | https://huggingface.co/papers/2609.03005
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05275). Keywords: transformer. Status: pending-review.
- Source: [[papers/2609.05275]] | https://huggingface.co/papers/2609.05275
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02780). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.02780]] | https://huggingface.co/papers/2609.02780
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03586). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.03586]] | https://huggingface.co/papers/2609.03586
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04753). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.04753]] | https://huggingface.co/papers/2609.04753
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04190). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.04190]] | https://huggingface.co/papers/2609.04190
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05415). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2609.05415]] | https://huggingface.co/papers/2609.05415
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03231). Keywords: classification. Status: pending-review.
- Source: [[papers/2609.03231]] | https://huggingface.co/papers/2609.03231
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01936). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.01936]] | https://huggingface.co/papers/2609.01936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04098). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.04098]] | https://huggingface.co/papers/2609.04098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.03430). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.03430]] | https://huggingface.co/papers/2609.03430
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02373). Keywords: neural network. Status: pending-review.
- Source: [[papers/2609.02373]] | https://huggingface.co/papers/2609.02373
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04201). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.04201]] | https://huggingface.co/papers/2609.04201
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30391). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.30391]] | https://huggingface.co/papers/2608.30391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01532). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.01532]] | https://huggingface.co/papers/2609.01532
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02737). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.02737]] | https://huggingface.co/papers/2609.02737
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02783). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.02783]] | https://huggingface.co/papers/2609.02783
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01925). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.01925]] | https://huggingface.co/papers/2609.01925
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01740). Keywords: transformer. Status: pending-review.
- Source: [[papers/2609.01740]] | https://huggingface.co/papers/2609.01740
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01657). Keywords: transformer. Status: pending-review.
- Source: [[papers/2609.01657]] | https://huggingface.co/papers/2609.01657
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29669). Keywords: factor model. Status: pending-review.
- Source: [[papers/2608.29669]] | https://huggingface.co/papers/2608.29669
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01560). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.01560]] | https://huggingface.co/papers/2609.01560
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00188). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.00188]] | https://huggingface.co/papers/2609.00188
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29613). Keywords: attention, classification. Status: pending-review.
- Source: [[papers/2608.29613]] | https://huggingface.co/papers/2608.29613
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24293). Keywords: transformer, prediction. Status: pending-review.
- Source: [[papers/2608.24293]] | https://huggingface.co/papers/2608.24293
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30935). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.30935]] | https://huggingface.co/papers/2608.30935
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29098). Keywords: prediction, classification. Status: pending-review.
- Source: [[papers/2608.29098]] | https://huggingface.co/papers/2608.29098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31106). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.31106]] | https://huggingface.co/papers/2608.31106
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30795). Keywords: forecasting, forecast, prediction. Status: pending-review.
- Source: [[papers/2608.30795]] | https://huggingface.co/papers/2608.30795
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29974). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.29974]] | https://huggingface.co/papers/2608.29974
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25697). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.25697]] | https://huggingface.co/papers/2608.25697
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28460). Keywords: attention, prediction. Status: pending-review.
- Source: [[papers/2608.28460]] | https://huggingface.co/papers/2608.28460
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23943). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.23943]] | https://huggingface.co/papers/2608.23943
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21832). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.21832]] | https://huggingface.co/papers/2608.21832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27260). Keywords: trend. Status: pending-review.
- Source: [[papers/2608.27260]] | https://huggingface.co/papers/2608.27260
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26872). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.26872]] | https://huggingface.co/papers/2608.26872
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26103). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.26103]] | https://huggingface.co/papers/2608.26103
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23172). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.23172]] | https://huggingface.co/papers/2608.23172
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15763). Keywords: regression. Status: pending-review.
- Source: [[papers/2608.15763]] | https://huggingface.co/papers/2608.15763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26200). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.26200]] | https://huggingface.co/papers/2608.26200
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27123). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.27123]] | https://huggingface.co/papers/2608.27123
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25798). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.25798]] | https://huggingface.co/papers/2608.25798
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26067). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.26067]] | https://huggingface.co/papers/2608.26067
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15062). Keywords: neural network, transformer. Status: pending-review.
- Source: [[papers/2608.15062]] | https://huggingface.co/papers/2608.15062
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19556). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.19556]] | https://huggingface.co/papers/2608.19556
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24138). Keywords: regression. Status: pending-review.
- Source: [[papers/2608.24138]] | https://huggingface.co/papers/2608.24138
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22071). Keywords: prediction, classification. Status: pending-review.
- Source: [[papers/2608.22071]] | https://huggingface.co/papers/2608.22071
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25204). Keywords: deep learning, classification. Status: pending-review.
- Source: [[papers/2608.25204]] | https://huggingface.co/papers/2608.25204
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14652). Keywords: forecasting, forecast. Status: pending-review.
- Source: [[papers/2608.14652]] | https://huggingface.co/papers/2608.14652
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26070). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.26070]] | https://huggingface.co/papers/2608.26070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22614). Keywords: transformer. Status: pending-review.
- Source: [[papers/2608.22614]] | https://huggingface.co/papers/2608.22614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22876). Keywords: attention, sequence model. Status: pending-review.
- Source: [[papers/2608.22876]] | https://huggingface.co/papers/2608.22876
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23566). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.23566]] | https://huggingface.co/papers/2608.23566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24053). Keywords: classification. Status: pending-review.
- Source: [[papers/2608.24053]] | https://huggingface.co/papers/2608.24053
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24763). Keywords: forecasting, transformer, forecast, prediction. Status: pending-review.
- Source: [[papers/2608.24763]] | https://huggingface.co/papers/2608.24763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15875). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.15875]] | https://huggingface.co/papers/2608.15875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23670). Keywords: prediction. Status: pending-review.
- Source: [[papers/2608.23670]] | https://huggingface.co/papers/2608.23670
- Confidence: Low (auto-matched, not yet reviewed)
- Volatility enters Kelly directly (f* = mu/sigma^2; double forecast vol -> quarter size; HAR-RV chosen over GARCH(1,1) for sigma^2 forecasting, GARCH kept as sanity check); volume enters via estimation quality, edge erosion (Amihud), and regime staleness; operating rule: volume > 2x trailing 20-day median -> half-Kelly until 5 sessions re-price
- Source: [[wiki/decisions/vol-volume-aware-kelly-2026-08-23]]
- Confidence: High

### 2026-09-09: Certified portfolio risk bounds without cross-asset covariances
- Firm-level distributional characteristics (Qwen3-Embedding-8B news representations) + Wasserstein-2 dispersion yield a sharp UPPER bound on systematic portfolio variance and an implementable allocation rule needing only marginal vols — 52-firm panel 2018–2022, allocation lands in 0.69th–1.33rd in-sample variance percentile vs equal-risk's 21st–28th
- Source: [[2608.29692]]
- Confidence: High

### 2026-09-09: Wasserstein-barycentric interaction fields for spatial factor models

### 2026-09-09: Graph Machine: Towards Better Pretraining via Edges

### 2026-09-09: RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives

### 2026-09-09: Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Serie

### 2026-09-09: SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions

### 2026-09-09: ReactVAU: A Slow-Fast Decoupled Framework for Streaming Video Anomaly Understand

### 2026-09-09: CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs

### 2026-09-09: AuK Technical Report: An Open-Source Foundational Model for Speech Generation an

### 2026-09-09: TransNormal-2: Geometry-Grounded Rectified Flow with Edge-Aware Decoding for Pre

### 2026-09-09: BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Lar

### 2026-09-09: Reason Through the Latent! Making Latent Visual Reasoning Necessary

### 2026-09-09: Steering Geometry: Validating Human Value Geometry in LLM Steering Space

### 2026-09-09: Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context R

### 2026-09-09: Kalman Delta Networks: Uncertainty-aware Associative Memory

### 2026-09-09: VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes

### 2026-09-09: What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale

### 2026-09-10: OracleZoom: On-Policy Self-Distillation Inspired Reference-Constrained Recursive

### 2026-09-10: Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning

### 2026-09-10: WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data

### 2026-09-10: RESCUE-BENCH: Towards Relation-Aware Multi-Party Emotional Support Conversation 

### 2026-09-11: Memory as Plans: World-Action Modeling with Memory-Grounded Planning

### 2026-09-11: FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation

### 2026-09-11: DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning fo

### 2026-09-11: HyQuant: Hybrid-Precision Quantization for LLM Attention

### 2026-09-11: SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacki

### 2026-09-12: Memory as Plans: World-Action Modeling with Memory-Grounded Planning

### 2026-09-12: FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation

### 2026-09-12: DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning fo

### 2026-09-12: HyQuant: Hybrid-Precision Quantization for LLM Attention

### 2026-09-12: SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacki

### 2026-09-12: World in World: Explore the World with World Models

### 2026-09-12: CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary
- HF trending paper (arxiv: 2609.06931). Keywords: classification. Status: pending-review.
- Source: [[papers/2609.06931]] | https://huggingface.co/papers/2609.06931
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11548). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.11548]] | https://huggingface.co/papers/2609.11548
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07064). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.07064]] | https://huggingface.co/papers/2609.07064
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27875). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.27875]] | https://huggingface.co/papers/2608.27875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11155). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.11155]] | https://huggingface.co/papers/2609.11155
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11486). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2609.11486]] | https://huggingface.co/papers/2609.11486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11561). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.11561]] | https://huggingface.co/papers/2609.11561
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07064). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.07064]] | https://huggingface.co/papers/2609.07064
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27875). Keywords: attention. Status: pending-review.
- Source: [[papers/2608.27875]] | https://huggingface.co/papers/2608.27875
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11155). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.11155]] | https://huggingface.co/papers/2609.11155
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11486). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2609.11486]] | https://huggingface.co/papers/2609.11486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.11561). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.11561]] | https://huggingface.co/papers/2609.11561
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.09657). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.09657]] | https://huggingface.co/papers/2609.09657
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05405). Keywords: time series. Status: pending-review.
- Source: [[papers/2609.05405]] | https://huggingface.co/papers/2609.05405
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06806). Keywords: classification. Status: pending-review.
- Source: [[papers/2609.06806]] | https://huggingface.co/papers/2609.06806
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06490). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.06490]] | https://huggingface.co/papers/2609.06490
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05663). Keywords: regression. Status: pending-review.
- Source: [[papers/2609.05663]] | https://huggingface.co/papers/2609.05663
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06652). Keywords: alternative data. Status: pending-review.
- Source: [[papers/2609.06652]] | https://huggingface.co/papers/2609.06652
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07816). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.07816]] | https://huggingface.co/papers/2609.07816
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07108). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.07108]] | https://huggingface.co/papers/2609.07108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06289). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.06289]] | https://huggingface.co/papers/2609.06289
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06746). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.06746]] | https://huggingface.co/papers/2609.06746
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.04971). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.04971]] | https://huggingface.co/papers/2609.04971
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06665). Keywords: prediction. Status: pending-review.
- Source: [[papers/2609.06665]] | https://huggingface.co/papers/2609.06665
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08936). Keywords: transformer. Status: pending-review.
- Source: [[papers/2609.08936]] | https://huggingface.co/papers/2609.08936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.08345). Keywords: attention. Status: pending-review.
- Source: [[papers/2609.08345]] | https://huggingface.co/papers/2609.08345
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.07941). Keywords: anomaly detection. Status: pending-review.
- Source: [[papers/2609.07941]] | https://huggingface.co/papers/2609.07941
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.08999). Keywords: neural network. Status: pending-review.
- Source: [[papers/2510.08999]] | https://huggingface.co/papers/2510.08999
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.06008). Keywords: time series, forecast, prediction. Status: pending-review.
- Source: [[papers/2609.06008]] | https://huggingface.co/papers/2609.06008
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.05738). Keywords: transformer, attention. Status: pending-review.
- Source: [[papers/2609.05738]] | https://huggingface.co/papers/2609.05738
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02881). Keywords: transformer. Status: pending-review.
- Source: [[papers/2609.02881]] | https://huggingface.co/papers/2609.02881
- Confidence: Low (auto-matched, not yet reviewed)
- Companion paper: builds spatial factor structure from language-model representation geometry — an alternative to return-based factor estimation when return histories are short/high-dimensional
- Source: [[2608.29669]]
- Confidence: Medium
