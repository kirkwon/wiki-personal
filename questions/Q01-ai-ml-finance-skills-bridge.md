---
tags: [permanent-question, research]
created: 2026-05-25
question: "What are the foundational skills and knowledge that most leverage the intersection of AI/ML and Finance? Work from basics — what does one actually need to master?"
date: 2026-05-25
type: permanent-question
reviewed: 2026-09-02
confidence: 0.95
evidence_count: 283
last_evidence_date: 2026-09-01
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

## Evidence Log

<!-- Weekly scan appends dated evidence blocks below this line.
     Format: ### YYYY-MM-DD: <topic>
             - Finding
             - Source: [[wikilink]] or URL
             - Confidence: High/Medium/Low
-->

### 2026-06-13: Causal AI pipeline deployed — DoWhy 4-step + EconML DML
- Deployed DoWhy causal graph models on portfolio factors. Refutation step (placebo, random common cause) catches spurious factors standard backtesting misses. EconML DML is now standard for CATE estimation.
- Source: [[DoWhy]] [[EconML]]
- Confidence: High

### 2026-06-24: Web extraction infrastructure — free alternative data pipelines
- Crawl4AI (62k stars, ~1-4s/URL) + ScrapeGraphAI (23k stars, LLM-powered via Ollama gemma4) replace Firecrawl credit dependency. Alternative data collection now cost-free and unbounded.
- Source: [[entities/crawl4ai]] [[entities/scrapegraphai]]
- Confidence: High

### 2026-06-27: PCA + Random Matrix Theory for factor models
- S&P 500's 125,250 covariance entries collapse to 5-15 real eigenportfolios via Marchenko-Pastur screening. Everything else is noise. Principled factor count selection vs arbitrary thresholds.
- Source: [[sources/pca-random-matrix-theory-equity-markets]]
- Confidence: High

### 2026-06-30: Mean-variance myopia under stochastic volatility

### 2026-07-30: CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Ac

### 2026-07-30: Parallel Decoding Distillation for Fast Image and Video Generation

### 2026-07-03: Parameter-Efficient Quantum-Inspired Fast Weight Programmers for Traffic-Matrix 

### 2025-07-11: Machine Bullshit: Characterizing the Emergent Disregard for Truth in

### 2025-07-21: Quantitative Risk Management in Volatile Markets with an Expectile-Based

### 2026-07-08: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Paramete

### 2025-08-19: Ovis2.5 Technical Report

### 2026-07-10: CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

### 2025-08-27: Forecasting Probability Distributions of Financial Returns with Deep

### 2026-07-16: Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

### 2025-09-03: VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use

### 2025-09-10: From Noise to Narrative: Tracing the Origins of Hallucinations in

### 2025-09-15: QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading

### 2026-07-20: Understanding Reasoning from Pretraining to Post-Training

### 2025-09-18: Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation

### 2025-09-26: UserRL: Training Interactive User-Centric Agent via Reinforcement

### 2025-09-29: Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive

### 2025-09-29: WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level

### 2026-07-24: NVIDIA-labs OO Agents: Native Python Object-Oriented Agents

### 2025-10-02: CurES: From Gradient Analysis to Efficient Curriculum Learning for

### 2025-10-03: StockBench: Can LLM Agents Trade Stocks Profitably In Real-world

### 2025-10-03: TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis

### 2026-07-28: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social

### 2025-10-06: Free Lunch Alignment of Text-to-Image Diffusion Models without

### 2025-10-07: AdvEvo-MARL: Shaping Internalized Safety through Adversarial

### 2025-10-08: A Contextual Quality Reward Model for Reliable and Efficient Best-of-N

### 2025-10-14: Self-Improving LLM Agents at Test-Time

### 2025-10-15: Tensor Logic: The Language of AI

### 2025-10-21: Enterprise Deep Research: Steerable Multi-Agent Deep Research for

### 2025-10-22: AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement

### 2025-11-06: LiveTradeBench: Seeking Real-World Alpha with Large Language Models

### 2025-11-07: Scaling Agent Learning via Experience Synthesis

### 2025-12-05: SIMA 2: A Generalist Embodied Agent for Virtual Worlds

### 2025-12-05: QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory

### 2025-12-10: TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion Models

### 2025-12-11: Towards a Science of Scaling Agent Systems

### 2025-12-11: Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware ROI Pred

### 2025-12-19: Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment with Na

### 2026-01-23: From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantific

### 2026-01-27: Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability

### 2026-01-30: Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs v

### 2026-02-04: Scaling Small Agents Through Strategy Auctions

### 2026-02-06: PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling

### 2026-02-10: QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining

### 2026-02-10: Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Langua

### 2026-02-13: The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving

### 2026-02-13: Budget-Constrained Agentic Large Language Models: Intention-Based Planning for C

### 2026-02-20: Discovering Multiagent Learning Algorithms with Large Language Models

### 2026-03-03: Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-tra

### 2026-03-11: SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive

### 2026-03-12: Meissa: Multi-modal Medical Agentic Intelligence

### 2026-03-18: FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use

### 2026-03-18: I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Prob

### 2026-04-02: QuitoBench: A High-Quality Open Time Series Forecasting Benchmark

### 2026-04-03: Brainstacks: Cross-Domain Cognitive Capabilities via Frozen MoE-LoRA Stacks for 

### 2026-04-09: Qualixar OS: A Universal Operating System for AI Agent Orchestration

### 2026-04-14: Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge Graphs and

### 2026-05-07: OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

### 2026-05-11: InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search

### 2026-05-12: G-Zero: Self-Play for Open-Ended Generation from Zero Data

### 2026-05-12: AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Syst

### 2026-05-15: Nexus : An Agentic Framework for Time Series Forecasting

### 2026-05-19: Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces

### 2026-05-20: CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization

### 2026-05-26: Foundation Protocol: A Coordination Layer for Agentic Society

### 2026-05-29: Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Ge

### 2026-06-03: Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment 

### 2026-06-05: Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM 

### 2026-06-09: DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and R

### 2026-06-11: EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agent

### 2026-06-16: Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Mo

### 2026-06-18: STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Sta

### 2026-06-26: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents

### 2026-07-08: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Paramete

### 2026-07-10: CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

### 2026-07-28: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social

### 2026-07-31: INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models

### 2026-07-31: Can Large Language Models Execute Parent Orders?

### 2026-07-31: Beacon: Knowing When and How to Perform Agentic Visual Reasoning

### 2026-08-03: Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a Longitudina

### 2026-08-03: Mental World Modeling

### 2026-08-03: ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow

### 2026-08-03: SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark fo

### 2026-08-03: Meshy T2: Fast Native Mesh Generation with Flow Matching

### 2026-08-03: AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

### 2026-08-03: β-OPSD: Deriving with Policy Optimization, Training with Self-Distillation

### 2026-08-03: Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts 

### 2026-08-03: Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential A

### 2026-08-03: Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainabil

### 2026-08-03: Pedestrian Archetypes Extension -- More Pedestrian Models for Autonomous Vehicle

### 2026-08-03: Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions

### 2026-08-03: AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emot

### 2026-08-03: BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms

### 2026-08-04: A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples

### 2026-08-04: GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Ti

### 2026-08-04: Relax Within, Balance Across: Geometry-Guided Load Balancing for Vision-Language

### 2026-08-04: Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis
- HF trending paper (arxiv: 2608.00440). Keywords: var. Status: pending-review.
- Source: [[papers/2608.00440]] | https://huggingface.co/papers/2608.00440
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00574). Keywords: var. Status: pending-review.
- Source: [[papers/2608.00574]] | https://huggingface.co/papers/2608.00574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02585). Keywords: var. Status: pending-review.
- Source: [[papers/2608.02585]] | https://huggingface.co/papers/2608.02585
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29122). Keywords: var. Status: pending-review.
- Source: [[papers/2607.29122]] | https://huggingface.co/papers/2607.29122
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26497). Keywords: var. Status: pending-review.
- Source: [[papers/2607.26497]] | https://huggingface.co/papers/2607.26497
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25289). Keywords: var. Status: pending-review.
- Source: [[papers/2607.25289]] | https://huggingface.co/papers/2607.25289
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.20891). Keywords: option. Status: pending-review.
- Source: [[papers/2607.20891]] | https://huggingface.co/papers/2607.20891
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16922). Keywords: option. Status: pending-review.
- Source: [[papers/2607.16922]] | https://huggingface.co/papers/2607.16922
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26637). Keywords: var. Status: pending-review.
- Source: [[papers/2607.26637]] | https://huggingface.co/papers/2607.26637
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28319). Keywords: var. Status: pending-review.
- Source: [[papers/2607.28319]] | https://huggingface.co/papers/2607.28319
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28308). Keywords: quant. Status: pending-review.
- Source: [[papers/2607.28308]] | https://huggingface.co/papers/2607.28308
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28582). Keywords: var. Status: pending-review.
- Source: [[papers/2607.28582]] | https://huggingface.co/papers/2607.28582
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28617). Keywords: var. Status: pending-review.
- Source: [[papers/2607.28617]] | https://huggingface.co/papers/2607.28617
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28675). Keywords: quant. Status: pending-review.
- Source: [[papers/2607.28675]] | https://huggingface.co/papers/2607.28675
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28996). Keywords: option. Status: pending-review.
- Source: [[papers/2607.28996]] | https://huggingface.co/papers/2607.28996
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27924). Keywords: var. Status: pending-review.
- Source: [[papers/2607.27924]] | https://huggingface.co/papers/2607.27924
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27201). Keywords: var. Status: pending-review.
- Source: [[papers/2607.27201]] | https://huggingface.co/papers/2607.27201
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.27851). Keywords: risk. Status: pending-review.
- Source: [[papers/2607.27851]] | https://huggingface.co/papers/2607.27851
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28595). Keywords: quant. Status: pending-review.
- Source: [[papers/2607.28595]] | https://huggingface.co/papers/2607.28595
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.28410). Keywords: finance, trading, market. Status: pending-review.
- Source: [[papers/2607.28410]] | https://huggingface.co/papers/2607.28410
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26056). Keywords: option. Status: pending-review.
- Source: [[papers/2607.26056]] | https://huggingface.co/papers/2607.26056
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23370). Keywords: finance, market, volatility. Status: pending-review.
- Source: [[papers/2607.23370]] | https://huggingface.co/papers/2607.23370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.08093). Keywords: risk, quant, option. Status: pending-review.
- Source: [[papers/2607.08093]] | https://huggingface.co/papers/2607.08093
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.01232). Keywords: quant. Status: pending-review.
- Source: [[papers/2607.01232]] | https://huggingface.co/papers/2607.01232
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.26080). Keywords: quant, option. Status: pending-review.
- Source: [[papers/2606.26080]] | https://huggingface.co/papers/2606.26080
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.19236). Keywords: quant. Status: pending-review.
- Source: [[papers/2606.19236]] | https://huggingface.co/papers/2606.19236
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.15007). Keywords: quant. Status: pending-review.
- Source: [[papers/2606.15007]] | https://huggingface.co/papers/2606.15007
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.03108). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2606.03108]] | https://huggingface.co/papers/2606.03108
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.07299). Keywords: risk. Status: pending-review.
- Source: [[papers/2606.07299]] | https://huggingface.co/papers/2606.07299
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.01886). Keywords: finance, trading, portfolio, market. Status: pending-review.
- Sour
### 2026-08-05: Centralized blog draft pipeline: 2 active drafts, 12 verified candidates across 3 tiers, organized into thematic series.
- Source: [[blog-content-pipeline.md]]
- Confidence: Medium

### 2026-08-05: 13 MCP servers configured across Hermes, providing tools for search, code, finance, data, and automation. n8n deployed as visual automation layer. Docker infrastructure running.
- Source: [[mcp-infrastructure.md]]
- Confidence: High

### 2026-08-05: Loop engineering is the practice of structuring agent improvement as a closed-loop system with a **critic/doer separation** — one component acts, another validates. This separation enables the agent t...
- Source: [[loop-engineering.md]]
- Confidence: Low

### 2026-08-05: Three interconnected skill systems: (1) **Book Skills Dashboard** — interactive HTML visualization of 303 skills/concepts from 33 books with D3.js network graphs, (2) **Hermes Skills Library** — 320 i...
- Source: [[skills-ecosystem.md]]
- Confidence: Low

### 2026-08-05: Designing self-running agent loops: heartbeat, SKILL.md, state files, verifiers, worktrees, MCP — transitioning from prompting to engineering autonomous systems.
- Source: [[loop-engineering.md]]
- Confidence: High

### 2026-08-05: Applied causal inference (Pearl/DoWhy/EconML) for risk management and portfolio construction, building toward an autonomous causal hedge signal generator.
- Source: [[causal-ai-hedge-agent.md]]
- Confidence: Medium

### 2026-08-05: Live portfolio dashboard (port 5001) with allocation, concentration, tax-loss harvesting, and performance views.
- Source: [[portfolio-dashboard.md]]
- Confidence: Medium

### 2026-08-05: Centralized blog draft pipeline: 2 active drafts, 12 verified candidates across 3 tiers, organized into thematic series.
- Source: [[blog-content-pipeline.md]]
- Confidence: Medium

### 2026-08-05: Loop engineering is the practice of structuring agent improvement as a closed-loop system with a **critic/doer separation** — one component acts, anot...
- Source: [[loop-engineering.md]]
- Confidence: Low

### 2026-08-05: Three interconnected skill systems: (1) **Book Skills Dashboard** — interactive HTML visualization of 303 skills/concepts from 33 books with D3.js net...
- Source: [[skills-ecosystem.md]]
- Confidence: Low

### 2026-08-05: Designing self-running agent loops: heartbeat, SKILL.md, state files, verifiers, worktrees, MCP — transitioning from prompting to engineering autonomo...
- Source: [[loop-engineering.md]]
- Confidence: High

### 2026-08-05: Tracking SpaceX (SPCX) IPO mechanics, Nasdaq-100 inclusion catalyst (Jul 7), and Anthropic/OpenAI IPO pipelines with automated monitoring.
- Source: [[mega-ipo-tracking.md]]
- Confidence: Medium

### 2026-08-05: Applied causal inference (Pearl/DoWhy/EconML) for risk management and portfolio construction, building toward an autonomous causal hedge signal genera...
- Source: [[causal-ai-hedge-agent.md]]
- Confidence: Medium

### 2026-08-05: Core Hermes workspace (`~/clawd/`): AGENTS.md, SOUL.md, MEMORY.md, heartbeat, memory files, and supporting tooling.
- Source: [[clawd-workspace.md]]
- Confidence: Medium

### 2026-08-05: > Auto-generated 2026-08-04 06:00 | 14 projects
- Source: [[DASHBOARD.md]]
- Confidence: Medium

### 2026-08-05: Live portfolio dashboard (port 5001) with allocation, concentration, tax-loss harvesting, and performance views.

### 2026-08-05: ChronoLens: Measuring Language Change Across Time, Languages, and Linguistic Lev

### 2026-08-05: Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-B

### 2026-08-05: ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?

### 2026-08-05: PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diver

### 2026-08-05: LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

### 2026-08-05: When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, a

### 2026-08-05: Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

### 2026-08-05: Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains and Sur

### 2026-08-05: ExplainBench: Evaluating Code Explanations from Agents

### 2026-08-05: PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Lear

### 2026-08-05: CAPEval: A Decoupled Caption Evaluation across Understanding and Generation

### 2026-08-05: SkillJack: Persistent Skill Backdoors in Self-Evolving Agents

### 2026-08-05: UniWorld-Design: From Pixel Generation to Layer-Native Design

### 2026-08-05: AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming Tasks?

### 2026-08-06: SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in Multimodal Large

### 2026-08-06: GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks

### 2026-08-06: Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from A

### 2026-08-06: NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the English-Korea

### 2026-08-06: HelloWorld: Enabling Socially Interactive Characters in Video World Models

### 2026-08-06: TriGlue: a Biology-Inspired Generative Model for Generating Molecular Glue-Induc

### 2026-08-06: ARCHead: Activation-Metric Residual Correction for Large Language Model Output H

### 2026-08-07: DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous 

### 2026-08-07: Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulu

### 2026-08-07: MameLoshnLM: Yiddish Language Model and Evaluation Benchmark

### 2026-08-07: From Economic Agents to Agentic Economies: A Systems Blueprint for Economic Worl

### 2026-08-07: PaDoc: Layout-Grounded Parallel Decoding for Document Parsing

### 2026-08-07: SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding

### 2026-08-07: On-Policy Delta Distillation for Multilingual Math Reasoning

### 2026-08-07: HarnessOpt-Bench: Evaluating LLMs at Harness Optimization

### 2026-08-07: Helping Music Co-Creation Agents 'Listen' Well: Hierarchical Self-Supervised Wor

### 2026-08-10: Efficient Knowledge Distillation for LLMs: Offline Top-K Logits and a Fused Chun

### 2026-08-10: Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence

### 2026-08-10: Towards Interpretable Foundation Models for Retinal Fundus Images

### 2026-08-10: SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task L

### 2026-08-10: StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming 

### 2026-08-10: Modular TTT: Rethinking Test-Time Training as Composable Modules

### 2026-08-11: The Loss Does Not See the Basis, but Adam Does

### 2026-08-11: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaborat

### 2026-08-11: A^2E : An End-to-End Agent Auditing Engine

### 2026-08-12: Power law graph attention: exact generalization of scaled dot-product attention,

### 2026-08-12: Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness

### 2026-08-12: AdvFD: Boosting Visual Generation via Adversarial Fr'echet Distance Loss

### 2026-08-12: SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Pe

### 2026-08-12: Beyond Pixels: From Video Priors to 4D Worlds

### 2026-08-12: VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model w

### 2026-08-12: Business Arena: Benchmarking LLM Agents in a Realistic Marketplace

### 2026-08-12: Omega-S: A Functional Resilience Index for LLM Fine-Tuning

### 2026-08-12: The Loss Does Not See the Basis, but Adam Does

### 2026-08-12: WeClawArena: An Auditable Sandbox and Benchmark for Cross-User Agents Collaborat

### 2026-08-12: A^2E : An End-to-End Agent Auditing Engine

### 2026-08-13: SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Librari

### 2026-08-13: Parameter Exploration for RLVR via Variational Learning

### 2026-08-13: Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop

### 2026-08-13: Simplex Relaxation for Discrete Diffusion

### 2026-08-13: OpenART: Scaling Agent Red Teaming via Open-Ended Environment Evolution

### 2026-08-13: From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-

### 2026-08-14: Context-Matched Distillation: Teacher Causality for Autoregressive Video Distill

### 2026-08-14: Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing

### 2026-08-14: AVA-Encoder: Towards Agent-Native Video Representation Learning

### 2026-08-14: TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation wi

### 2026-08-14: Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and 

### 2026-08-14: Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

### 2026-08-14: DarwinX: Evolving Agent Harnesses Through Natural Selection

### 2026-08-14: LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-

### 2026-08-14: How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity in 

### 2026-08-14: From Atomic Evidence to Logical Composition: Structured Compositional Reasoning 

### 2026-08-14: ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Fr

### 2026-08-17: Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models

### 2026-08-17: Agents Catching Agents: Shortcut Cascades and Benchmark Gaming in Clinical Multi

### 2026-08-17: A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientif

### 2026-08-17: UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Mu

### 2026-08-17: CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Im

### 2026-08-17: Verifier-Induced Support Reshaping in On-Policy Optimization

### 2026-08-17: Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A 

### 2026-08-17: Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Resea

### 2026-08-18: Valid Per-Field Selective Risk Control for Document Extraction: Three Failure Mo

### 2026-08-18: Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search

### 2026-08-18: TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation

### 2026-08-18: WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Ri

### 2026-08-18: DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs

### 2026-08-18: Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable

### 2026-08-18: Improving the matrix multiplication exponent with modern optimization and AlphaE

### 2026-08-18: UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrati

### 2026-08-18: Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs

### 2026-08-19: V-RAE: Rethinking Video Latent Spaces for Generation

### 2026-08-19: PixRestore: Unified Image Restoration via Pixel Diffusion Transformer

### 2026-08-19: Demystifying Agent Skills: Why They Work-Until They Don't

### 2026-08-19: Cross-Model Memory Transfer via Target-Side Reader Adaptation

### 2026-08-19: EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing

### 2026-08-19: HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety

### 2026-08-19: From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Gen

### 2026-08-19: GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation

### 2026-08-19: StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End

### 2026-08-19: From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

### 2026-08-19: Accuracy and Order Sensitivity Diverge Under Label-Free Strategies

### 2026-08-20: Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditi

### 2026-08-20: SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deforma

### 2026-08-20: Training Leaves Traces: Centered Residual Signatures for Language Model Lineage 

### 2026-08-20: Looped Language Models Improve Compositional Tool Calling

### 2026-08-20: FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents

### 2026-08-21: Towards Quantifying Benchmark Optimization in ASR Models

### 2026-08-21: FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving

### 2026-08-21: ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World

### 2026-08-21: PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-C

### 2026-08-21: Towards Real-Time and Adaptable LiDAR Scene Completion

### 2026-08-21: Bounded Agents: Delegation Security for Multi-Agent AI Systems

### 2026-08-22: TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity

### 2026-08-24: Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but No R

### 2026-08-24: ParaTempo: Efficient Parallel Reasoning via Temporal Confidence

### 2026-08-24: FlavourBench: Ranking Frontier Language Models with Executable Culinary Ground T

### 2026-08-24: EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking

### 2026-08-24: Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Dist

### 2026-08-24: OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs

### 2026-08-24: AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Sce

### 2026-08-25: The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration

### 2026-08-25: Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit 

### 2026-08-25: EXPL-FR: Explaining Face Recognition Models via Vision-Language Alignment

### 2026-08-25: Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated B

### 2026-08-25: Towards a Densing Law for User Representation Learning at Billion-Scale Capacity

### 2026-08-25: EchoWM: Open and Enterable Omnimodal World Models

### 2026-08-25: One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommender

### 2026-08-25: Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selec

### 2026-08-25: TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration

### 2026-08-25: Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Chu

### 2026-08-25: Apodex 1.1: Scaling Agentic Intelligence for Complex Work

### 2026-08-25: RISE: Adaptive Imagination for World Action Models

### 2026-08-25: TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming

### 2026-08-26: Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment

### 2026-08-26: AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace

### 2026-08-26: Latent Action as Intention Enables Efficient Future Imagination for World Action

### 2026-08-26: WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report

### 2026-08-26: Best Practice Critic Optimization

### 2026-08-26: Meta^n: Recursive Self-Improvement through Emergent Depth

### 2026-08-26: The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space,

### 2026-08-26: What AstroPT knows about galaxies, and what that can teach us about LLMs

### 2026-08-27: Skill Issue: Are Skills Language-Invariant in LLMs?

### 2026-08-27: Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling

### 2026-08-27: LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech De

### 2026-08-27: RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieva

### 2026-08-27: Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worl

### 2026-08-27: Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models

### 2026-08-27: Gated Recurrent Transformers: Expressive Depth through Recurrent Modulation

### 2026-08-27: WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploratio

### 2026-08-27: FrontierChallenge: Evaluating Scientific Workflow Completion

### 2026-08-27: Agent-G^2: Gaussian Guidance for Agentic Reinforcement Learning

### 2026-08-27: MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-T

### 2026-08-27: MARS: Multi-Specialist LLM Relay System for Competitive Programming

### 2026-08-27: When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows

### 2026-08-28: CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval

### 2026-08-28: Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Techn

### 2026-08-28: Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher

### 2026-08-28: What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents

### 2026-08-30: Luce: Relightable Gaussians for 3D Asset Generation

### 2026-08-30: CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model 

### 2026-08-31: Language Chain in Alignment: Cross-lingual Ranking Preference Optimization

### 2026-08-31: Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090

### 2026-08-31: StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environmen

### 2026-08-31: StepGuard: Learning Step-Level Guardrails with Scalable Supervision and Safety-U

### 2026-09-01: Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Pref

### 2026-09-01: Uncertainty-Aware End-to-End AI Weather Forecasting: Disentangling Observation a

### 2026-09-01: Super Library Agent: Joint Generation and Maintenance of Multiple Applications B

### 2026-09-01: SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Mo

### 2026-09-01: LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigatio

### 2026-09-01: Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation

### 2026-09-01: SHAPE of Chain-of-Thought in Math Reasoning

### 2026-09-01: Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superinte

### 2026-09-02: From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers

### 2026-09-02: Recursive Criticality of AI Self-Improvement

### 2026-09-02: E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Oper

### 2026-09-02: Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone

### 2026-09-02: ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Trans

### 2026-09-03: Debias-SparseGPT: Bias-Aware Pruning for Large Language Models

### 2026-09-03: Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional Fie

### 2026-09-03: NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Eff

### 2026-09-03: Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Qu

### 2026-09-03: A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss

### 2026-09-03: HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

### 2026-09-03: ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrie

### 2026-09-03: RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Reques
- HF trending paper (arxiv: 2608.27831). Keywords: var. Status: pending-review.
- Source: [[papers/2608.27831]] | https://huggingface.co/papers/2608.27831
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01865). Keywords: var. Status: pending-review.
- Source: [[papers/2609.01865]] | https://huggingface.co/papers/2609.01865
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01437). Keywords: var. Status: pending-review.
- Source: [[papers/2609.01437]] | https://huggingface.co/papers/2609.01437
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00591). Keywords: var. Status: pending-review.
- Source: [[papers/2609.00591]] | https://huggingface.co/papers/2609.00591
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21450). Keywords: var. Status: pending-review.
- Source: [[papers/2608.21450]] | https://huggingface.co/papers/2608.21450
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01657). Keywords: quant. Status: pending-review.
- Source: [[papers/2609.01657]] | https://huggingface.co/papers/2609.01657
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29692). Keywords: portfolio, risk, volatility, var. Status: pending-review.
- Source: [[papers/2608.29692]] | https://huggingface.co/papers/2608.29692
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.02496). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2609.02496]] | https://huggingface.co/papers/2609.02496
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00968). Keywords: var. Status: pending-review.
- Source: [[papers/2609.00968]] | https://huggingface.co/papers/2609.00968
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01404). Keywords: var. Status: pending-review.
- Source: [[papers/2609.01404]] | https://huggingface.co/papers/2609.01404
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30730). Keywords: market. Status: pending-review.
- Source: [[papers/2608.30730]] | https://huggingface.co/papers/2608.30730
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.00137). Keywords: quant. Status: pending-review.
- Source: [[papers/2609.00137]] | https://huggingface.co/papers/2609.00137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2609.01572). Keywords: option. Status: pending-review.
- Source: [[papers/2609.01572]] | https://huggingface.co/papers/2609.01572
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.31075). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.31075]] | https://huggingface.co/papers/2608.31075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.28600). Keywords: var. Status: pending-review.
- Source: [[papers/2608.28600]] | https://huggingface.co/papers/2608.28600
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24293). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.24293]] | https://huggingface.co/papers/2608.24293
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30935). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.30935]] | https://huggingface.co/papers/2608.30935
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29098). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.29098]] | https://huggingface.co/papers/2608.29098
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29310). Keywords: portfolio. Status: pending-review.
- Source: [[papers/2608.29310]] | https://huggingface.co/papers/2608.29310
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.30795). Keywords: var, monte carlo. Status: pending-review.
- Source: [[papers/2608.30795]] | https://huggingface.co/papers/2608.30795
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.29464). Keywords: option, var. Status: pending-review.
- Source: [[papers/2608.29464]] | https://huggingface.co/papers/2608.29464
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24777). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.24777]] | https://huggingface.co/papers/2608.24777
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24804). Keywords: finance. Status: pending-review.
- Source: [[papers/2608.24804]] | https://huggingface.co/papers/2608.24804
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27370). Keywords: var. Status: pending-review.
- Source: [[papers/2608.27370]] | https://huggingface.co/papers/2608.27370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23149). Keywords: var. Status: pending-review.
- Source: [[papers/2608.23149]] | https://huggingface.co/papers/2608.23149
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27455). Keywords: var. Status: pending-review.
- Source: [[papers/2608.27455]] | https://huggingface.co/papers/2608.27455
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23943). Keywords: option, var. Status: pending-review.
- Source: [[papers/2608.23943]] | https://huggingface.co/papers/2608.23943
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.27260). Keywords: option, var. Status: pending-review.
- Source: [[papers/2608.27260]] | https://huggingface.co/papers/2608.27260
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.26872). Keywords: var. Status: pending-review.
- Source: [[papers/2608.26872]] | https://huggingface.co/papers/2608.26872
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15763). Keywords: market, var. Status: pending-review.
- Source: [[papers/2608.15763]] | https://huggingface.co/papers/2608.15763
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25500). Keywords: option. Status: pending-review.
- Source: [[papers/2608.25500]] | https://huggingface.co/papers/2608.25500
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24569). Keywords: var. Status: pending-review.
- Source: [[papers/2608.24569]] | https://huggingface.co/papers/2608.24569
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23918). Keywords: var. Status: pending-review.
- Source: [[papers/2608.23918]] | https://huggingface.co/papers/2608.23918
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24189). Keywords: var. Status: pending-review.
- Source: [[papers/2608.24189]] | https://huggingface.co/papers/2608.24189
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23318). Keywords: var. Status: pending-review.
- Source: [[papers/2608.23318]] | https://huggingface.co/papers/2608.23318
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24979). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.24979]] | https://huggingface.co/papers/2608.24979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24479). Keywords: var. Status: pending-review.
- Source: [[papers/2608.24479]] | https://huggingface.co/papers/2608.24479
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15062). Keywords: trading. Status: pending-review.
- Source: [[papers/2608.15062]] | https://huggingface.co/papers/2608.15062
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19556). Keywords: var. Status: pending-review.
- Source: [[papers/2608.19556]] | https://huggingface.co/papers/2608.19556
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23383). Keywords: var. Status: pending-review.
- Source: [[papers/2608.23383]] | https://huggingface.co/papers/2608.23383
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25625). Keywords: finance, var. Status: pending-review.
- Source: [[papers/2608.25625]] | https://huggingface.co/papers/2608.25625
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25204). Keywords: option. Status: pending-review.
- Source: [[papers/2608.25204]] | https://huggingface.co/papers/2608.25204
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14652). Keywords: var. Status: pending-review.
- Source: [[papers/2608.14652]] | https://huggingface.co/papers/2608.14652
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.25832). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.25832]] | https://huggingface.co/papers/2608.25832
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22614). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.22614]] | https://huggingface.co/papers/2608.22614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22876). Keywords: var. Status: pending-review.
- Source: [[papers/2608.22876]] | https://huggingface.co/papers/2608.22876
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24735). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2608.24735]] | https://huggingface.co/papers/2608.24735
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23566). Keywords: monte carlo. Status: pending-review.
- Source: [[papers/2608.23566]] | https://huggingface.co/papers/2608.23566
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24053). Keywords: var. Status: pending-review.
- Source: [[papers/2608.24053]] | https://huggingface.co/papers/2608.24053
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.24882). Keywords: var. Status: pending-review.
- Source: [[papers/2608.24882]] | https://huggingface.co/papers/2608.24882
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23740). Keywords: var. Status: pending-review.
- Source: [[papers/2608.23740]] | https://huggingface.co/papers/2608.23740
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23691). Keywords: alpha. Status: pending-review.
- Source: [[papers/2608.23691]] | https://huggingface.co/papers/2608.23691
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20958). Keywords: var. Status: pending-review.
- Source: [[papers/2608.20958]] | https://huggingface.co/papers/2608.20958
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20430). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.20430]] | https://huggingface.co/papers/2608.20430
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23283). Keywords: finance. Status: pending-review.
- Source: [[papers/2608.23283]] | https://huggingface.co/papers/2608.23283
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.22856). Keywords: var. Status: pending-review.
- Source: [[papers/2608.22856]] | https://huggingface.co/papers/2608.22856
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17336). Keywords: var. Status: pending-review.
- Source: [[papers/2608.17336]] | https://huggingface.co/papers/2608.17336
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20169). Keywords: var. Status: pending-review.
- Source: [[papers/2608.20169]] | https://huggingface.co/papers/2608.20169
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.13610). Keywords: risk, var. Status: pending-review.
- Source: [[papers/2606.13610]] | https://huggingface.co/papers/2606.13610
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23189). Keywords: var. Status: pending-review.
- Source: [[papers/2608.23189]] | https://huggingface.co/papers/2608.23189
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23392). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.23392]] | https://huggingface.co/papers/2608.23392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13914). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.13914]] | https://huggingface.co/papers/2608.13914
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21486). Keywords: var. Status: pending-review.
- Source: [[papers/2608.21486]] | https://huggingface.co/papers/2608.21486
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20953). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.20953]] | https://huggingface.co/papers/2608.20953
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.23252). Keywords: portfolio. Status: pending-review.
- Source: [[papers/2608.23252]] | https://huggingface.co/papers/2608.23252
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20634). Keywords: var. Status: pending-review.
- Source: [[papers/2608.20634]] | https://huggingface.co/papers/2608.20634
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.21360). Keywords: var. Status: pending-review.
- Source: [[papers/2608.21360]] | https://huggingface.co/papers/2608.21360
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16647). Keywords: var. Status: pending-review.
- Source: [[papers/2608.16647]] | https://huggingface.co/papers/2608.16647
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20886). Keywords: option. Status: pending-review.
- Source: [[papers/2608.20886]] | https://huggingface.co/papers/2608.20886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20574). Keywords: portfolio. Status: pending-review.
- Source: [[papers/2608.20574]] | https://huggingface.co/papers/2608.20574
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16425). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.16425]] | https://huggingface.co/papers/2608.16425
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.20438). Keywords: stress test, var. Status: pending-review.
- Source: [[papers/2608.20438]] | https://huggingface.co/papers/2608.20438
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15767). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.15767]] | https://huggingface.co/papers/2608.15767
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15888). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.15888]] | https://huggingface.co/papers/2608.15888
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16490). Keywords: var. Status: pending-review.
- Source: [[papers/2608.16490]] | https://huggingface.co/papers/2608.16490
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19861). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.19861]] | https://huggingface.co/papers/2608.19861
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14022). Keywords: option. Status: pending-review.
- Source: [[papers/2608.14022]] | https://huggingface.co/papers/2608.14022
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19758). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.19758]] | https://huggingface.co/papers/2608.19758
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.19936). Keywords: risk, quant, var. Status: pending-review.
- Source: [[papers/2608.19936]] | https://huggingface.co/papers/2608.19936
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18423). Keywords: market. Status: pending-review.
- Source: [[papers/2608.18423]] | https://huggingface.co/papers/2608.18423
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18171). Keywords: var. Status: pending-review.
- Source: [[papers/2608.18171]] | https://huggingface.co/papers/2608.18171
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14929). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.14929]] | https://huggingface.co/papers/2608.14929
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18701). Keywords: var. Status: pending-review.
- Source: [[papers/2608.18701]] | https://huggingface.co/papers/2608.18701
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18746). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.18746]] | https://huggingface.co/papers/2608.18746
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11947). Keywords: option. Status: pending-review.
- Source: [[papers/2608.11947]] | https://huggingface.co/papers/2608.11947
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16002). Keywords: risk, quant. Status: pending-review.
- Source: [[papers/2608.16002]] | https://huggingface.co/papers/2608.16002
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17800). Keywords: market, option. Status: pending-review.
- Source: [[papers/2608.17800]] | https://huggingface.co/papers/2608.17800
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17988). Keywords: var. Status: pending-review.
- Source: [[papers/2608.17988]] | https://huggingface.co/papers/2608.17988
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18076). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.18076]] | https://huggingface.co/papers/2608.18076
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17597). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.17597]] | https://huggingface.co/papers/2608.17597
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.18063). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2608.18063]] | https://huggingface.co/papers/2608.18063
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.17050). Keywords: option. Status: pending-review.
- Source: [[papers/2608.17050]] | https://huggingface.co/papers/2608.17050
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14036). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.14036]] | https://huggingface.co/papers/2608.14036
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16793). Keywords: var. Status: pending-review.
- Source: [[papers/2608.16793]] | https://huggingface.co/papers/2608.16793
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13556). Keywords: var. Status: pending-review.
- Source: [[papers/2608.13556]] | https://huggingface.co/papers/2608.13556
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16391). Keywords: var. Status: pending-review.
- Source: [[papers/2608.16391]] | https://huggingface.co/papers/2608.16391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15930). Keywords: var. Status: pending-review.
- Source: [[papers/2608.15930]] | https://huggingface.co/papers/2608.15930
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16884). Keywords: alpha. Status: pending-review.
- Source: [[papers/2608.16884]] | https://huggingface.co/papers/2608.16884
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15022). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.15022]] | https://huggingface.co/papers/2608.15022
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14614). Keywords: market, quant. Status: pending-review.
- Source: [[papers/2608.14614]] | https://huggingface.co/papers/2608.14614
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15659). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.15659]] | https://huggingface.co/papers/2608.15659
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.16765). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.16765]] | https://huggingface.co/papers/2608.16765
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.15669). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.15669]] | https://huggingface.co/papers/2608.15669
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14639). Keywords: risk, alpha, var. Status: pending-review.
- Source: [[papers/2608.14639]] | https://huggingface.co/papers/2608.14639
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13417). Keywords: var. Status: pending-review.
- Source: [[papers/2608.13417]] | https://huggingface.co/papers/2608.13417
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14391). Keywords: risk, var. Status: pending-review.
- Source: [[papers/2608.14391]] | https://huggingface.co/papers/2608.14391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00220). Keywords: var. Status: pending-review.
- Source: [[papers/2608.00220]] | https://huggingface.co/papers/2608.00220
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14546). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.14546]] | https://huggingface.co/papers/2608.14546
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10835). Keywords: var. Status: pending-review.
- Source: [[papers/2608.10835]] | https://huggingface.co/papers/2608.10835
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.14075). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.14075]] | https://huggingface.co/papers/2608.14075
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03744). Keywords: option. Status: pending-review.
- Source: [[papers/2608.03744]] | https://huggingface.co/papers/2608.03744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13760). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.13760]] | https://huggingface.co/papers/2608.13760
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11045). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.11045]] | https://huggingface.co/papers/2608.11045
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12836). Keywords: option. Status: pending-review.
- Source: [[papers/2608.12836]] | https://huggingface.co/papers/2608.12836
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08975). Keywords: var. Status: pending-review.
- Source: [[papers/2608.08975]] | https://huggingface.co/papers/2608.08975
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12990). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.12990]] | https://huggingface.co/papers/2608.12990
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07545). Keywords: var. Status: pending-review.
- Source: [[papers/2608.07545]] | https://huggingface.co/papers/2608.07545
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.29211). Keywords: risk. Status: pending-review.
- Source: [[papers/2607.29211]] | https://huggingface.co/papers/2607.29211
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13430). Keywords: var. Status: pending-review.
- Source: [[papers/2608.13430]] | https://huggingface.co/papers/2608.13430
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11951). Keywords: var. Status: pending-review.
- Source: [[papers/2608.11951]] | https://huggingface.co/papers/2608.11951
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.12313). Keywords: option. Status: pending-review.
- Source: [[papers/2608.12313]] | https://huggingface.co/papers/2608.12313
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11660). Keywords: var. Status: pending-review.
- Source: [[papers/2608.11660]] | https://huggingface.co/papers/2608.11660
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.13391). Keywords: var. Status: pending-review.
- Source: [[papers/2608.13391]] | https://huggingface.co/papers/2608.13391
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11562). Keywords: var. Status: pending-review.
- Source: [[papers/2608.11562]] | https://huggingface.co/papers/2608.11562
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00677). Keywords: risk, var. Status: pending-review.
- Source: [[papers/2608.00677]] | https://huggingface.co/papers/2608.00677
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10615). Keywords: var. Status: pending-review.
- Source: [[papers/2608.10615]] | https://huggingface.co/papers/2608.10615
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11215). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.11215]] | https://huggingface.co/papers/2608.11215
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09805). Keywords: var. Status: pending-review.
- Source: [[papers/2608.09805]] | https://huggingface.co/papers/2608.09805
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05604). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.05604]] | https://huggingface.co/papers/2608.05604
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07346). Keywords: var. Status: pending-review.
- Source: [[papers/2608.07346]] | https://huggingface.co/papers/2608.07346
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03499). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03499]] | https://huggingface.co/papers/2608.03499
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: var. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03887). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.03887]] | https://huggingface.co/papers/2608.03887
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08621). Keywords: trading, market. Status: pending-review.
- Source: [[papers/2608.08621]] | https://huggingface.co/papers/2608.08621
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.08477). Keywords: volatility, var. Status: pending-review.
- Source: [[papers/2608.08477]] | https://huggingface.co/papers/2608.08477
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10744). Keywords: var. Status: pending-review.
- Source: [[papers/2608.10744]] | https://huggingface.co/papers/2608.10744
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10692). Keywords: var. Status: pending-review.
- Source: [[papers/2608.10692]] | https://huggingface.co/papers/2608.10692
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.11205). Keywords: var. Status: pending-review.
- Source: [[papers/2608.11205]] | https://huggingface.co/papers/2608.11205
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.09900). Keywords: stress test. Status: pending-review.
- Source: [[papers/2608.09900]] | https://huggingface.co/papers/2608.09900
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.10288). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.10288]] | https://huggingface.co/papers/2608.10288
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07346). Keywords: var. Status: pending-review.
- Source: [[papers/2608.07346]] | https://huggingface.co/papers/2608.07346
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03499). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03499]] | https://huggingface.co/papers/2608.03499
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05136). Keywords: var. Status: pending-review.
- Source: [[papers/2608.05136]] | https://huggingface.co/papers/2608.05136
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.07110). Keywords: var. Status: pending-review.
- Source: [[papers/2608.07110]] | https://huggingface.co/papers/2608.07110
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05703). Keywords: option. Status: pending-review.
- Source: [[papers/2608.05703]] | https://huggingface.co/papers/2608.05703
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03573). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03573]] | https://huggingface.co/papers/2608.03573
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.18846). Keywords: var. Status: pending-review.
- Source: [[papers/2603.18846]] | https://huggingface.co/papers/2603.18846
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06756). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.06756]] | https://huggingface.co/papers/2608.06756
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03796). Keywords: option. Status: pending-review.
- Source: [[papers/2608.03796]] | https://huggingface.co/papers/2608.03796
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04378). Keywords: var. Status: pending-review.
- Source: [[papers/2608.04378]] | https://huggingface.co/papers/2608.04378
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06301). Keywords: var. Status: pending-review.
- Source: [[papers/2608.06301]] | https://huggingface.co/papers/2608.06301
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05802). Keywords: var. Status: pending-review.
- Source: [[papers/2608.05802]] | https://huggingface.co/papers/2608.05802
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05137). Keywords: var. Status: pending-review.
- Source: [[papers/2608.05137]] | https://huggingface.co/papers/2608.05137
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06146). Keywords: var. Status: pending-review.
- Source: [[papers/2608.06146]] | https://huggingface.co/papers/2608.06146
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.06020). Keywords: market. Status: pending-review.
- Source: [[papers/2608.06020]] | https://huggingface.co/papers/2608.06020
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05850). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.05850]] | https://huggingface.co/papers/2608.05850
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01481). Keywords: risk, quant. Status: pending-review.
- Source: [[papers/2608.01481]] | https://huggingface.co/papers/2608.01481
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03451). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03451]] | https://huggingface.co/papers/2608.03451
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02703). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.02703]] | https://huggingface.co/papers/2608.02703
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.22143). Keywords: var. Status: pending-review.
- Source: [[papers/2607.22143]] | https://huggingface.co/papers/2607.22143
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.05070). Keywords: var. Status: pending-review.
- Source: [[papers/2608.05070]] | https://huggingface.co/papers/2608.05070
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04397). Keywords: sharpe, var. Status: pending-review.
- Source: [[papers/2608.04397]] | https://huggingface.co/papers/2608.04397
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00782). Keywords: var. Status: pending-review.
- Source: [[papers/2608.00782]] | https://huggingface.co/papers/2608.00782
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03764). Keywords: finance. Status: pending-review.
- Source: [[papers/2608.03764]] | https://huggingface.co/papers/2608.03764
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.04244). Keywords: var. Status: pending-review.
- Source: [[papers/2608.04244]] | https://huggingface.co/papers/2608.04244
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00155). Keywords: var. Status: pending-review.
- Source: [[papers/2608.00155]] | https://huggingface.co/papers/2608.00155
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03971). Keywords: alpha. Status: pending-review.
- Source: [[papers/2608.03971]] | https://huggingface.co/papers/2608.03971
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03509). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.03509]] | https://huggingface.co/papers/2608.03509
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02589). Keywords: quant, var. Status: pending-review.
- Source: [[papers/2608.02589]] | https://huggingface.co/papers/2608.02589
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.01837). Keywords: var. Status: pending-review.
- Source: [[papers/2608.01837]] | https://huggingface.co/papers/2608.01837
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26451). Keywords: quant, option. Status: pending-review.
- Source: [[papers/2607.26451]] | https://huggingface.co/papers/2607.26451
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.00730). Keywords: risk, var. Status: pending-review.
- Source: [[papers/2608.00730]] | https://huggingface.co/papers/2608.00730
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03979). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03979]] | https://huggingface.co/papers/2608.03979
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03700). Keywords: risk. Status: pending-review.
- Source: [[papers/2608.03700]] | https://huggingface.co/papers/2608.03700
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03457). Keywords: quant. Status: pending-review.
- Source: [[papers/2608.03457]] | https://huggingface.co/papers/2608.03457
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02218). Keywords: var. Status: pending-review.
- Source: [[papers/2608.02218]] | https://huggingface.co/papers/2608.02218
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03874). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03874]] | https://huggingface.co/papers/2608.03874
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.02791). Keywords: option. Status: pending-review.
- Source: [[papers/2608.02791]] | https://huggingface.co/papers/2608.02791
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2608.03507). Keywords: var. Status: pending-review.
- Source: [[papers/2608.03507]] | https://huggingface.co/papers/2608.03507
- Confidence: Low (auto-matched, not yet reviewed)
- Source: [[portfolio-dashboard.md]]
- Confidence: Medium
ce: [[papers/2606.01886]] | https://huggingface.co/papers/2606.01886
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.01770). Keywords: market. Status: pending-review.
- Source: [[papers/2606.01770]] | https://huggingface.co/papers/2606.01770
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.28424). Keywords: risk. Status: pending-review.
- Source: [[papers/2605.28424]] | https://huggingface.co/papers/2605.28424
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.23218). Keywords: option. Status: pending-review.
- Source: [[papers/2605.23218]] | https://huggingface.co/papers/2605.23218
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.19436). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2605.19436]] | https://huggingface.co/papers/2605.19436
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.17698). Keywords: market, risk, volatility. Status: pending-review.
- Source: [[papers/2605.17698]] | https://huggingface.co/papers/2605.17698
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.14389). Keywords: market. Status: pending-review.
- Source: [[papers/2605.14389]] | https://huggingface.co/papers/2605.14389
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.08715). Keywords: risk, sharpe. Status: pending-review.
- Source: [[papers/2605.08715]] | https://huggingface.co/papers/2605.08715
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.09959). Keywords: quant. Status: pending-review.
- Source: [[papers/2605.09959]] | https://huggingface.co/papers/2605.09959
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.07510). Keywords: alpha. Status: pending-review.
- Source: [[papers/2605.07510]] | https://huggingface.co/papers/2605.07510
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2605.05185). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2605.05185]] | https://huggingface.co/papers/2605.05185
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.11544). Keywords: volatility. Status: pending-review.
- Source: [[papers/2604.11544]] | https://huggingface.co/papers/2604.11544
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.06392). Keywords: market. Status: pending-review.
- Source: [[papers/2604.06392]] | https://huggingface.co/papers/2604.06392
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2604.01152). Keywords: quant. Status: pending-review.
- Source: [[papers/2604.01152]] | https://huggingface.co/papers/2604.01152
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.26017). Keywords: finance. Status: pending-review.
- Source: [[papers/2603.26017]] | https://huggingface.co/papers/2603.26017
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.15670). Keywords: quant. Status: pending-review.
- Source: [[papers/2603.15670]] | https://huggingface.co/papers/2603.15670
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.08262). Keywords: finance, volatility. Status: pending-review.
- Source: [[papers/2603.08262]] | https://huggingface.co/papers/2603.08262
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.09018). Keywords: risk. Status: pending-review.
- Source: [[papers/2603.09018]] | https://huggingface.co/papers/2603.09018
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.06333). Keywords: risk, quant. Status: pending-review.
- Source: [[papers/2603.06333]] | https://huggingface.co/papers/2603.06333
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2603.02208). Keywords: option. Status: pending-review.
- Source: [[papers/2603.02208]] | https://huggingface.co/papers/2603.02208
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.16928). Keywords: alpha, volatility. Status: pending-review.
- Source: [[papers/2602.16928]] | https://huggingface.co/papers/2602.16928
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.11541). Keywords: market, risk. Status: pending-review.
- Source: [[papers/2602.11541]] | https://huggingface.co/papers/2602.11541
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.09877). Keywords: risk. Status: pending-review.
- Source: [[papers/2602.09877]] | https://huggingface.co/papers/2602.09877
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.08004). Keywords: market, risk, quant, option. Status: pending-review.
- Source: [[papers/2602.08004]] | https://huggingface.co/papers/2602.08004
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.07085). Keywords: market, alpha, quant. Status: pending-review.
- Source: [[papers/2602.07085]] | https://huggingface.co/papers/2602.07085
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.06030). Keywords: finance. Status: pending-review.
- Source: [[papers/2602.06030]] | https://huggingface.co/papers/2602.06030
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2602.02751). Keywords: market. Status: pending-review.
- Source: [[papers/2602.02751]] | https://huggingface.co/papers/2602.02751
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.21590). Keywords: sharpe, option. Status: pending-review.
- Source: [[papers/2601.21590]] | https://huggingface.co/papers/2601.21590
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.18778). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2601.18778]] | https://huggingface.co/papers/2601.18778
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2601.15690). Keywords: quant. Status: pending-review.
- Source: [[papers/2601.15690]] | https://huggingface.co/papers/2601.15690
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.11251). Keywords: finance. Status: pending-review.
- Source: [[papers/2512.11251]] | https://huggingface.co/papers/2512.11251
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05402). Keywords: market, risk. Status: pending-review.
- Source: [[papers/2512.05402]] | https://huggingface.co/papers/2512.05402
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.08296). Keywords: finance, quant, option. Status: pending-review.
- Source: [[papers/2512.08296]] | https://huggingface.co/papers/2512.08296
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.08153). Keywords: option. Status: pending-review.
- Source: [[papers/2512.08153]] | https://huggingface.co/papers/2512.08153
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.05049). Keywords: quant. Status: pending-review.
- Source: [[papers/2512.05049]] | https://huggingface.co/papers/2512.05049
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2512.04797). Keywords: portfolio. Status: pending-review.
- Source: [[papers/2512.04797]] | https://huggingface.co/papers/2512.04797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.03773). Keywords: option. Status: pending-review.
- Source: [[papers/2511.03773]] | https://huggingface.co/papers/2511.03773
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2511.03628). Keywords: trading, portfolio, market, risk. Status: pending-review.
- Source: [[papers/2511.03628]] | https://huggingface.co/papers/2511.03628
- Confidence: Low (auto-matched, not yet reviewed)
  Learning F
- HF trending paper (arxiv: 2510.14264). Keywords: trading, market, alpha, quant. Status: pending-review.
- Source: [[papers/2510.14264]] | https://huggingface.co/papers/2510.14264
- Confidence: Low (auto-matched, not yet reviewed)
  Enterprise A
- HF trending paper (arxiv: 2510.17797). Keywords: option. Status: pending-review.
- Source: [[papers/2510.17797]] | https://huggingface.co/papers/2510.17797
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.12269). Keywords: option. Status: pending-review.
- Source: [[papers/2510.12269]] | https://huggingface.co/papers/2510.12269
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.07841). Keywords: quant. Status: pending-review.
- Source: [[papers/2510.07841]] | https://huggingface.co/papers/2510.07841
- Confidence: Low (auto-matched, not yet reviewed)
  Samplin
- HF trending paper (arxiv: 2510.04087). Keywords: risk, option. Status: pending-review.
- Source: [[papers/2510.04087]] | https://huggingface.co/papers/2510.04087
- Confidence: Low (auto-matched, not yet reviewed)
  Co-Evolution in M
- HF trending paper (arxiv: 2510.01586). Keywords: risk. Status: pending-review.
- Source: [[papers/2510.01586]] | https://huggingface.co/papers/2510.01586
- Confidence: Low (auto-matched, not yet reviewed)
  Preference Imag
- HF trending paper (arxiv: 2509.25771). Keywords: quant. Status: pending-review.
- Source: [[papers/2509.25771]] | https://huggingface.co/papers/2509.25771
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.23370). Keywords: finance, market, volatility. Status: pending-review.
- Source: [[papers/2607.23370]] | https://huggingface.co/papers/2607.23370
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2510.01538). Keywords: finance. Status: pending-review.
- Source: [[papers/2510.01538]] | https://huggingface.co/papers/2510.01538
- Confidence: Low (auto-matched, not yet reviewed)
  Markets?
- HF trending paper (arxiv: 2510.02209). Keywords: finance, trading, market, risk. Status: pending-review.
- Source: [[papers/2510.02209]] | https://huggingface.co/papers/2510.02209
- Confidence: Low (auto-matched, not yet reviewed)
  Reasoning L
- HF trending paper (arxiv: 2510.01037). Keywords: quant. Status: pending-review.
- Source: [[papers/2510.01037]] | https://huggingface.co/papers/2510.01037
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.20709). Keywords: option. Status: pending-review.
- Source: [[papers/2607.20709]] | https://huggingface.co/papers/2607.20709
- Confidence: Low (auto-matched, not yet reviewed)
  Feedba
- HF trending paper (arxiv: 2509.22644). Keywords: quant. Status: pending-review.
- Source: [[papers/2509.22644]] | https://huggingface.co/papers/2509.22644
- Confidence: Low (auto-matched, not yet reviewed)
  Explorat
- HF trending paper (arxiv: 2509.22601). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2509.22601]] | https://huggingface.co/papers/2509.22601
- Confidence: Low (auto-matched, not yet reviewed)
  Learning
- HF trending paper (arxiv: 2509.19736). Keywords: option. Status: pending-review.
- Source: [[papers/2509.19736]] | https://huggingface.co/papers/2509.19736
- Confidence: Low (auto-matched, not yet reviewed)
  Framewo
- HF trending paper (arxiv: 2509.14180). Keywords: finance, risk. Status: pending-review.
- Source: [[papers/2509.14180]] | https://huggingface.co/papers/2509.14180
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.16097). Keywords: quant, sharpe. Status: pending-review.
- Source: [[papers/2607.16097]] | https://huggingface.co/papers/2607.16097
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.09995). Keywords: trading, market, risk, quant. Status: pending-review.
- Source: [[papers/2509.09995]] | https://huggingface.co/papers/2509.09995
- Confidence: Low (auto-matched, not yet reviewed)
  Transformers
- HF trending paper (arxiv: 2509.06938). Keywords: risk, quant, option, volatility. Status: pending-review.
- Source: [[papers/2509.06938]] | https://huggingface.co/papers/2509.06938
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2509.01055). Keywords: option. Status: pending-review.
- Source: [[papers/2509.01055]] | https://huggingface.co/papers/2509.01055
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.12395). Keywords: sharpe. Status: pending-review.
- Source: [[papers/2607.12395]] | https://huggingface.co/papers/2607.12395
- Confidence: Low (auto-matched, not yet reviewed)
  Neural Ne
- HF trending paper (arxiv: 2508.18921). Keywords: portfolio, risk. Status: pending-review.
- Source: [[papers/2508.18921]] | https://huggingface.co/papers/2508.18921
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.08093). Keywords: risk, quant, option. Status: pending-review.
- Source: [[papers/2607.08093]] | https://huggingface.co/papers/2607.08093
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2508.11737). Keywords: option. Status: pending-review.
- Source: [[papers/2508.11737]] | https://huggingface.co/papers/2508.11737
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.01232). Keywords: quant. Status: pending-review.
- Source: [[papers/2607.01232]] | https://huggingface.co/papers/2607.01232
- Confidence: Low (auto-matched, not yet reviewed)
  Frame
- HF trending paper (arxiv: 2507.13391). Keywords: portfolio, market, risk, quant. Status: pending-review.
- Source: [[papers/2507.13391]] | https://huggingface.co/papers/2507.13391
- Confidence: Low (auto-matched, not yet reviewed)
  Large Lan
- HF trending paper (arxiv: 2507.07484). Keywords: market, quant. Status: pending-review.
- Source: [[papers/2507.07484]] | https://huggingface.co/papers/2507.07484
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2606.27821). Keywords: quant. Status: pending-review.
- Source: [[papers/2606.27821]] | https://huggingface.co/papers/2606.27821
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.26004). Keywords: derivative. Status: pending-review.
- Source: [[papers/2607.26004]] | https://huggingface.co/papers/2607.26004
- Confidence: Low (auto-matched, not yet reviewed)
- HF trending paper (arxiv: 2607.25294). Keywords: finance. Status: pending-review.
- Source: [[papers/2607.25294]] | https://huggingface.co/papers/2607.25294
- Confidence: Low (auto-matched, not yet reviewed)
- Static M-V frontier is the myopic case of full intertemporal portfolio problem. Under SV (Heston, Stein/Stein), optimal demand = myopic M-V + intertemporal hedging term. mean-variance-analyzer underestimates hedging demand for horizons > 1 month.
- Source: [[concepts/mean-variance-myopia-under-stochastic-volatility]]
- Confidence: High
