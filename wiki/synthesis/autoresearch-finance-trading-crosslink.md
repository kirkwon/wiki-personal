---
created: 2026-08-23
updated: 2026-08-23
---


# Finance / Trading Autoresearch — Cross-Reference with Quant Pipeline

Analysis of all 32 finance/trading entries from awesome-autoresearch, cross-linked to existing quant wiki concepts.

---

## Entry Classification

| Project | Strategy | Backtest Type | Metric | APS Score |
|---------|---------|--------------|--------|-----------|
| atlas-gic | Swarm optimization | Rolling Sharpe | Sharpe | 4 |
| autoresearch-trading (erix) | SPY options | Historical | backtest metrics | 3 |
| autoresearch-trading (dietmarwo) | Generic + optimizer | Walk-forward | composite | 4 |
| binance-trading-karpathy | Crypto multi-asset | Historical | P&L | 3 |
| BTCautoresearch | Bitcoin formula | Walk-forward RMSE | RMSE | 3 |
| autoresearch-skfolio | Portfolio (skfolio) | Out-of-sample | Deflated Sharpe Ratio | 5 |
| AutoHypothesis | Stock selection | Walk-forward | holdout gates | 4 |
| autoresearch-glm | Credit scoring | Fixed benchmark | AUC | 2 |
| SlopePay feature research | Credit underwriting | Feature IV | AUC | 3 |
| autoresearch-markets | Kalshi prediction market | Held-out | val_logloss | 3 |
| Simmer Autoresearch | Prediction market config | Live trading | P&L | 3 |
| Autonomous Trading Strategy | Hyperliquid perps | Historical | score | 4 |
| PolyEdge AutoResearch | Polymarket arbitrage | Paper trading | P&L/fill rate | 3 |
| AutoResearch DEX | Uniswap V3 / Aerodrome | Backtest | composite 0.421→8.176 | 5 |
| Paradigm PM Challenge | Prediction market MM | Evaluation | mean edge | 4 |
| AutoresearchTrading | Crypto strategy | Historical | port_val / max_dd | 3 |
| Investing Autoresearch | Generic strategy | Walk-forward | Sharpe | 4 |
| EMA Crossover Autoresearch | SBIN EMA | Fixed 10yr | Sharpe+return+DD | 3 |
| NSE AutoResearch | Indian stocks | Fixed 10yr | composite | 3 |
| delu-agent | Live crypto trading | Live 24/7 | P&L | 5 |
| investment-autoresearch | Strategy variants | Parallel worktrees | vs buy-hold | 4 |
| autoresearch-crypto | Crypto strategy | Historical | metric gates | 3 |
| Juspay Neurolink PR | Finance infra | Auto experiment | N/A | 2 |
| ml-vs-leadlag-jp-stock | Japanese stocks | Reproducible | Sharpe | 4 |
| autoresearch-backtesting | SPY prediction | Backtest | Sharpe | 4 |
| IPL Odds Multi-Agent | Sports betting | Season-long | Brier score | 3 |
| Clio | Prediction market | Multi-agent Pareto | bankroll | 4 |
| trading-autoresearch | Intraday PatchTST | Overnight iterations | Sharpe CI | 4 |
| quanti-autoresearch | GDP econometrics | 4-phase exploration | RMSE | 2 |
| AutoResearch Trading Strategy Gen | Crypto futures | Simulation | keep/discard | 3 |
| Auto-Quant | FreqTrade crypto | Backtest | composite | 4 |
| noahroboros | BTC/ETH/SOL (Rust) | Backtest | 2.569 composite | 3 |

**APS (Applies to our Stack):** 1-5 scale. 5 = directly applicable.

---

## Top Projects for Our Quant Pipeline

### 1. autoresearch-skfolio — Portfolio Optimization (APS: 5)

**Repo:** https://github.com/CarloNicolini/autoresearch-skfolio
**Pattern:** Edits a single portfolio-research script, runs fixed out-of-sample validation, keeps only Deflated Sharpe Ratio gains.

**Why it fits:**
- Uses `skfolio` (Python portfolio optimization library) — same ecosystem as our mean-variance pipeline
- Deflated Sharpe Ratio is our metric of choice for strategy comparison
- Supports multiple datasets and reversed-return variants for robustness

**Cross-links:**
- [[factors]] — portfolio optimization is factor-based
- [[mean-variance-myopia-under-stochastic-volatility]] — this corrects for the myopia by testing across regimes
- [[asymmetry-hunter]] — Deflated Sharpe is an asymmetric acceptance criterion

### 2. AutoResearch DEX — DEX Strategy Discovery (APS: 5)

**Repo:** https://github.com/darks0l/autoresearch
**Pattern:** Backtests one mutation at a time against real Uniswap V3 and Aerodrome data. Lifted composite score from 0.421 to 8.176 over 230+ experiments.

**Why it fits:**
- Published results with transparent ledger (230 experiments)
- Real on-chain data, not synthetic
- Composite scoring (multi-objective)

**Connection:**
If we ever trade DeFi, this is the reference implementation.

### 3. delu-agent — Live Crypto Trading (APS: 5)

**Repo:** https://github.com/deluagent/delu-agent
**Pattern:** Runs 5 parallel autoresearch loops 24/7 on Base, executing trades via Bankr without human intervention. 9,000+ backtested experiments.

**Why it fits:**
- Fully autonomous 24/7 trading agent
- Self-improving via autoresearch
- Uses Bankr for execution (opinionated but proven)

**Cross-links:**
- Our [[causal-ai-hedge-agent]] project for the agent pattern
- [[market-close-summary]] cron for market awareness

### 4. AutoHypothesis — Stock Selection (APS: 4)

**Repo:** https://github.com/arteemg/AutoHypothesis
**Pattern:** Karpathy-style loop on `agent.py`, iterating on DEV data, keeping only hypotheses that clear one-shot holdback **and** walk-forward gates.

**Why it fits:**
- Multi-gate validation prevents overfitting to test data
- Walk-forward + holdback = rigorous strategy evaluation

**Connection:**
Directly applicable to our factor model validation pipeline.

### 5. ml-vs-leadlag-jp-stock (APS: 4)

**Repo:** https://github.com/kiwiiosaru-jp/ml-vs-leadlag-jp-stock
**Pattern:** Compares ML-driven Sharpe maximization against classical lead-lag PCA strategy.

**Why it fits:**
- Benchmarks ML vs classical quant — exactly our domain
- PCA lead-lag connects to our [[pca-random-matrix-theory-equity-markets]] source

**Connection:**
Empirical validation of the PCA/RMT framework we just added. The lead-lag PCA strategy is a concrete implementation of the eigenportfolio concept.

---

## Cross-Link Summary

| Existing Concept | Connected Finance Entry | Connection |
|---|---|---|
| [[factors]] | autoresearch-skfolio, AutoHypothesis | Portfolio factor optimization |
| [[mean-variance-myopia-under-stochastic-volatility]] | autoresearch-skfolio | Multi-regime validation |
| [[asymmetry-hunter]] | autoresearch-skfolio | Deflated Sharpe as asymmetric gate |
| [[pca-random-matrix-theory-equity-markets]] | ml-vs-leadlag-jp-stock | PCA lead-lag strategy implementation |
| [[causal-ai-hedge-agent]] | delu-agent | Autonomous 24/7 trading agent |
| [[optimal-investment-stochastic-volatility-chiarella-hsiao]] | trading-autoresearch | Overnight iterations with vol-aware gates |

---

## Clusters by Strategy Type

| Strategy Type | Projects | Count |
|---------------|----------|-------|
| Crypto trading (retail) | binance, AutoResearch DEX, AutoQuant, autoresearch-crypto, AutoResearch Gen, noahroboros | 6 |
| Prediction market | autoresearch-markets, Simmer, PolyEdge, Paradigm, Clio | 5 |
| Traditional equity | AutoHypothesis, EMA Crossover, NSE, autoresearch-backtesting, ml-vs-leadlag | 5 |
| Generic/meta | atlas-gic, dietmarwo, Investing Autoresearch, investment-autoresearch, trading-autoresearch | 5 |
| Options/derivatives | autoresearch-trading (erix) | 1 |
| Live/autonomous | delu-agent | 1 |
| Portfolio optimization | autoresearch-skfolio | 1 |
| Credit/fintech | autoresearch-glm, SlopePay | 2 |
| Sports betting | IPL Odds | 1 |
| Economic research | quanti-autoresearch | 1 |
| Infrastructure | Juspay Neurolink PR | 1 |

## Key Takeaways

1. **Most projects are traditional backtesting** — few run live. delu-agent is the exception.
2. **Crypto dominates** (6/32) — easier data access, retail-friendly.
3. **Sharpe is the universal metric** — every project uses some variant of risk-adjusted return.
4. **Walk-forward validation is rare** — most projects use fixed historical splits.
5. **skfolio project is the closest to our pipeline** — same tooling, same metric.

## Next step
Evaluate autoresearch-skfolio for integration: does our mean-variance pipeline benefit from adding autoresearch-style iteration to portfolio parameter discovery?

See also: [[awesome-autoresearch]]
