

# Optimal Investment Strategies under Stochastic Volatility – Estimation and Applications

A comprehensive study of how stochastic volatility affects long-term optimal investment strategies, comparing three SV models with Extended Kalman Filter estimation.

## Core Framework

Three stochastic volatility models are compared for optimal portfolio construction:

| Model | Volatility Process | Key Feature |
|-------|-------------------|-------------|
| **Extended Stein/Stein** | Gaussian (Ornstein-Uhlenbeck) | Volatility follows mean-reverting Gaussian process |
| **Heston** | Square-root (CIR) | Variance follows mean-reverting square-root process |
| **Extended Heston + CEV** | CEV variance process | Constant Elasticity Variance — σ(V) = V^γ, nests Heston (γ=0.5) |

## Key Contributions

### 1. Partial Information Problem
- Volatility is **not directly observable** — must be filtered from returns
- **Extended Kalman Filter (EKF)** adopted for state-space estimation of latent volatility
- Maximum likelihood estimation via the EKF prediction error decomposition

### 2. Optimal Strategies
- All three SV strategies produce a **positive intertemporal hedging term** beyond the static mean-variance portfolio (Merton's myopic demand)
- The hedging demand reflects investors' desire to hedge against adverse shifts in the investment opportunity set
- **Implication**: static M-V underestimates optimal hedging demand under SV

### 3. CEV Sensitivity
- Investment strategies are **highly sensitive to the CEV parameter γ**
- When γ ≠ 0.5 (non-Heston), analytical solutions break down → requires **Backward Markov Chain approximation** (Rust, 1996)

### 4. Empirical Result
- **Heston model favored as more parsimonious** than the other two models
- The square-root variance process (CIR) provides the best fit-to-complexity trade-off

## Methodological Toolkit

- **Extended Kalman Filter** — state-space estimation of latent volatility from equity returns alone
- **Backward Markov Chain approximation** — numerical DP for the CEV case where closed-form solutions are unavailable
- **ODE system for value function** — Riccati-style equations from the HJB framework (following Liu, 2007)

## Connection to Existing Work

- **Directly extends mean-variance-analyzer** — shows that static M-V is the myopic case; under SV you need intertemporal hedging demand
- **Informs causal-portfolio-research** — stochastic volatility regime dynamics are a confounder in bond-hedging causal models; the EKF approach provides a principled way to estimate latent vol states
- **Heston model** is also the foundation used in options-market-analysis for IV skew / term structure analysis
- The **CEV sensitivity finding** echoes the "regime matters" conclusion from our causal portfolio work

## References Cited

- Heston (1993) — closed-form SV option pricing
- Stein & Stein (1991) — Gaussian SV process
- Liu (2007) — portfolio selection in stochastic environments
- Merton (1971, 1973) — intertemporal CAPM and continuous-time portfolio theory
- Cox, Ingersoll & Ross (1985) — CIR process theory
- Rust (1996) — numerical DP via Markov chain approximation

See also: [[factors]]

See also: [[factor-investing]]
