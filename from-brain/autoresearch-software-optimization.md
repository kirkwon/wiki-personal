---
type: note
title: Autoresearch Software Optimization
related:
  - awesome-autoresearch
  - autoresearch-pattern
  - karpathy-autoresearch-loop
ingested_via: put_page
ingested_at: '2026-06-30T06:05:34.728Z'
source_kind: put_page
tags:
  - autoresearch
  - clusters
  - performance
  - software-optimization
created: 2026-06-30
---
# Software / Systems Optimization Autoresearch — Technique Cluster Matrix

Analysis of 52 software/systems optimization entries from awesome-autoresearch, clustered by technique and domain.

---

## Cluster Matrix

| Technique | Projects | Count | Avg Gain | Start Ease |
|-----------|----------|-------|----------|------------|
| GPU kernel optimization | autokernel, cublas-sam3, SiliconSwarm, Flash-MoE, nnmetal+labrat | 5 | ~2-6× speedup | ❌ (needs GPU) |
| LLM inference serving | vllm, helix-inference-opt, inference-opt, Flash-MoE, WinMoE | 5 | 15%-37% | ⚠️ (needs GPU) |
| Apple Silicon (MLX/Metal) | SiliconSwarm, Flash-MoE, autoresearch-go-ane, autoresearch-mamba, liltrAIner, nnmetal+labrat | 6 | ~2-6× | ✅ (native Mac) |
| Database/ETL | SQLite 588x, Lance, auto-data-pipeline, ClickHouse bug | 4 | 11%-588× | ✅ |
| Search ranking | idealo LTR, MSMarco BM25 (×2) | 3 | 37% latency | ✅ |
| Compiler | arete (Scheme), auto-arch-tournament (RISC-V) | 2 | 91.9% CoreMark | ❌ (RTL tools) |
| Security/WAF | WAFPlanet (ModSecurity) | 1 | 98.4% acc, -94.5% FP | ✅ |
| SAT/CP solvers | agent-sat, heuristic CP, sudoku | 3 | beats benchmarks | ✅ |
| Code generation | autospec (Spring Boot), english-app | 2 | pass/fail | ✅ |
| Test reliability | Gumroad flaky tests, pytest speedups | 2 | 295s→71s, 13 fixes | ✅ |
| Browser automation | OpenCLI, browser-use mind2web | 2 | 97% benchmark | ✅ |
| Systems (general) | autooptimization, HashSmith, PolyTrader, autoresearch-function | 4 | 13%-56% | ✅ |
| Web/SEO | Google Play ASO, Liquid template engine | 2 | 53% perf | ✅ |
| Logistics | VRPTW solver | 1 | algorithmic | ⚠️ (Rust) |
| Education app | Türkçe Hoca | 1 | continuous | ✅ |
| Resource forecasting | tsfm-autoresearch | 1 | 200ms budget | ✅ |

---

## Top Optimization Stories by Impact

### 1. 588× Faster SQLite Ingestion
**Source:** https://www.luiscolunga.com/posts/autoresearch-etl-optimization/
**Method:** pi-autoresearch on a Python financial-data ingestion pipeline
**Result:** 397s → 0.675s (588×)
**Why it matters:** Pure Python, no GPU. Demonstrates that dramatic wins are possible on CPU-bound IO pipelines.

### 2. 91.9% CoreMark on a RISC-V Core
**Source:** auto-arch-tournament (https://github.com/FeSens/auto-arch-tournament)
**Method:** Karpathy loop applied to SystemVerilog RTL, verified through riscv-formal + Verilator + FPGA
**Result:** +91.9% CoreMark
**Why it matters:** Extends autoresearch to hardware — shows it's architecture-agnostic.

### 3. Shopify Liquid: 53% Faster, 61% Fewer Allocations
**Source:** Tobi Lütke (https://simonwillison.net/2026/Mar/13/liquid/)
**Method:** 93 automated commits via autoresearch loop on the Liquid template engine
**Result:** Parse+render 53% faster, 61% fewer allocations
**Why it matters:** Production-tested at Shopify scale. Published by the CEO himself.

### 4. 62% Fewer ClickHouse Granule Scans (Hidden 3-Year Bug)
**Source:** PostHog (https://posthog.com/blog/autoresearch-query-bug)
**Method:** pi-autoresearch with lane-structured hypothesis exploration at a team offsite
**Result:** Found a timestamp-wrapping bug hidden for 3 years. Cut granule scans by 62%.
**Why it matters:** Found a real production bug that humans missed for 3 years. Autoresearch as debugging tool.

### 5. WAF: 98.4% Accuracy, 94.5% Fewer False Positives
**Source:** WAFPlanet (https://github.com/wafplanet/autoresearch)
**Method:** 30 autonomous experiments on OWASP ModSecurity CRS configuration
**Result:** 80.8% → 98.4% balanced accuracy, FP cut by 94.5%
**Why it matters:** Security domain. Shows autoresearch works for rule-tuning, not just code.

---

## Clusters by Reusable Technique

### The Benchmark + Correctness Double-Gate
**Used by:** autokernel, lance-autoresearch, nnmetal+labrat
**Pattern:** Every change must pass both a speed benchmark (latency/throughput) AND a correctness test (bit-equivalent, unit tests).
**Why it matters:** Prevents the agent from improving speed by breaking functionality. Essential for production systems.

### The Profile-First Protocol
**Used by:** autooptimization, HashSmith, PolyTrader
**Pattern:** Profile before changing. Only optimize what's measurably slow. Keep only changes backed by stack-level profiling evidence.
**Why it matters:** Prevents premature optimization. The agent doesn't guess where bottlenecks are — it measures.

### The Scout-Promote Funnel
**Used by:** openroad-autoresearch-ibex
**Pattern:** Cheap scout experiments on small data → if promising, promote to full expensive eval.
**Why it matters:** Saves compute for changes that won't pan out. Essential when full eval is expensive (RTL simulation, FPGA place-and-route).

### The Quality Guard
**Used by:** helix-inference-opt
**Pattern:** Accept throughput gains only if output quality stays within a tight bound (e.g., 1% bpb guard).
**Why it matters:** Prevents the agent from sacrificing quality for speed.

---

## macOS-Compatible Projects We Can Test

These require no GPU, no cloud, and no special hardware:

| Project | What It Tests | Setup Time |
|---------|--------------|------------|
| **SQLite 588×** | ETL performance optimization | ~5 min |
| **WAFPlanet** | Security rule optimization | ~10 min |
| **HashSmith** | Data structure optimization | ~5 min |
| **Pytest speedups** | Test suite performance | ~10 min |
| **autoresearch-function** | Arbitrary function optimization | ~3 min |
| **autospec** | Spring Boot service generation | ~15 min (needs Java) |

---

## Cross-Links to Add

- [[autoresearch-pattern]] — the core loop
- [[karpathy-autoresearch-loop]] — the original three-file architecture
- [[performance-optimization]] — if this concept exists
- [[apple-silicon-mlx]] — if this concept exists
