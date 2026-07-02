---
type: synthesis
tags: [autoresearch, matrix, technology, domain, cross-reference]
related: [awesome-autoresearch]
---

# awesome-autoresearch — Tech × Domain Matrix

Cross-reference of all 684 entries by technology and application domain, built from category file analysis.

---

## Technology Distribution

| Technology | Entries | Primary Domains |
|-----------|---------|----------------|
| **Python** | ~650 (95%) | All categories — the universal language |
| **PyTorch** | ~180 | Scientific research, GPU optimization, ML training |
| **Claude Code** | ~120 | Infra/skills/forks, software optimization, evaluation |
| **Codex** | ~45 | Infra/skills/forks, research automations |
| **OpenCode** | ~12 | General-purpose agent harnesses |
| **XGBoost/LightGBM** | ~25 | Finance/trading, tabular ML research |
| **Apple Silicon (MPS/MLX)** | ~15 | On-device training, inference optimization |
| **CUDA/GPU** | ~40 | Kernel optimization, LLM training |
| **Rust** | ~8 | Solvers, database kernels (Lance, sudoku) |
| **Go** | ~3 | Helixon, autoresearch-go-ane |
| **Elixir** | ~1 | ExAutoresearch (distributed training) |

---

## Domain × Technique Heatmap

### Scientific Research (68 entries)
| Technique | Count | Representative Projects |
|-----------|-------|----------------------|
| Straight Karpathy fork | 45 | autoresearch-cifar10, OCR, quantum, mol, connect4 |
| Multi-agent | 8 | AutoScientists, bountyhunter, AutoGo |
| Hypothesis tree | 3 | Arbor, AutoMedal |
| Paper-augmented | 2 | Paper Lantern, recursive-org |
| Domain-specific | 10 | Bio-Autoresearch (drug discovery), auto-alphafold3, SciMLx |

### Software/Systems Optimization (52 entries)
| Technique | Count | Representative Projects |
|-----------|-------|----------------------|
| GPU kernel tuning | 5 | autokernel, cublas-sam3, nnmetal+labrat |
| Apple Silicon optimization | 6 | SiliconSwarm, Flash-MoE, lance-autoresearch |
| LLM inference serving | 5 | vllm, helix-inference-opt, WinMoE |
| Database/ETL | 4 | SQLite 588×, Lance, ClickHouse bug finder |
| Search ranking | 3 | idealo LTR, BM25 (×2) |
| Test reliability | 2 | Gumroad flaky tests, pytest speedups |
| Security/WAF | 1 | WAFPlanet (98.4% acc) |
| Compiler/hardware | 2 | arete (Scheme), auto-arch-tournament (RISC-V) |
| Web/app optimization | 2 | Shopify Liquid (53% faster), Google Play ASO |

### Evaluation/Red Teaming (23 entries)
| Technique | Count | Representative Projects |
|-----------|-------|----------------------|
| Attack→Fix→Verify loop | 4 | Claudini, Jailbreak, JustAsk, autovoiceevals |
| Prompt/skill optimization | 5 | Langfuse blog, AutoPrompter, AutoMemory |
| Agent behavior evaluation | 3 | Autoreason (Borda), Trace2Evolve, AutonomousTester |
| Novelty/integrity benchmarks | 4 | Anti-Autoresearch, Novelty Bench, ResearchArena |
| Domain-specific benchmarks | 3 | AutoMedBench, DSBench, ResearchClawBench |

### Finance/Trading (32 entries)
| Technique | Count | Representative Projects |
|-----------|-------|----------------------|
| Crypto backtesting | 6 | binance, DEX, AutoQuant, noahroboros |
| Prediction markets | 5 | Simmer, PolyEdge, Clio, Paradigm Challenge |
| Traditional equity | 5 | AutoHypothesis, EMA Crossover, ml-vs-leadlag |
| Walk-forward validation | 4 | dietmarwo, Investing Autoresearch, AutoHypothesis |
| Live trading | 1 | delu-agent (24/7, 9,000+ experiments) |
| Portfolio optimization | 1 | autoresearch-skfolio (Deflated Sharpe) |

### Infra/Skills/Forks (132 entries)
| Technique | Count | Representative Projects |
|-----------|-------|----------------------|
| Agent plugins (Claude Code) | ~35 | lazy-developer, claude-autoresearch, AutoSkill |
| Skill optimization | ~8 | AutoSkill, EvoSkill, 达尔文.skill, autoimprove-cc |
| Parallel/multi-agent infra | ~15 | CORAL, Litmus, multiautoresearch, community.computer |
| Platform ports | ~10 | macOS fork, Windows, AMD, Tenstorrent, Colab/TPU |
| CLI/Rust tools | ~5 | autorize (Rust CLI), autoresearch CLI (Rust) |
| Cross-agent frameworks | ~12 | helix, GOAL.md, scalar-loop, pi-autoresearch |

---

## Key Cross-Domain Patterns

### Patterns that appear in 3+ domains
- **Git-backed keep/revert** — universal across all 684 entries
- **Single-file mutation** — used in 90%+ of entries (the core Karpathy pattern)
- **Fixed-time budget** — 80%+ of ML/optimization entries
- **Scout-promote funnel** — openroad (chip design), DEX trading, AutoKernel
- **Multi-agent parallel workers** — AutoScientists (science), Litmus (infra), delu-agent (trading), CORAL (general)
- **Evidence gates / falsification** — Vesuvius (science), Anti-Autoresearch (eval), SciTriage (eval)

### Technologies that appear in the most domains
1. **Python** — 100% of entries across all 14 categories
2. **Claude Code** — present in 7/14 categories
3. **PyTorch** — present in 5/14 categories
4. **Git** — implicit in every entry (keep/revert depends on git)
5. **JSONL/TSV logging** — present in 80%+ of entries with published results

---

## Apple Silicon Compatibility Check

Projects confirmed working on macOS (tested in Phase 3):

| Project | Category | Test Result |
|---------|----------|-------------|
| autoresearch-macos (miolini) | Infra fork | ✅ Full train cycle (val_bpb: 1.78) |
| kaggle-autoresearch: Titanic | Software opt | ✅ 5-fold CV, keep/discard decisions |
| kaggle-autoresearch: Housing | Software opt | ✅ RMSE improvement, accepted |
| build-readme.py | Build pipeline | ✅ README regenerates clean |
| update script | Build pipeline | ✅ Syntax valid |

### macOS-compatible but untested
| Project | Category | Why Would Work |
|---------|----------|---------------|
| autospec (Spring Boot) | Software opt | Pure Java/Gradle |
| WAFPlanet (ModSecurity) | Software opt | Python + ModSecurity configs |
| SQLite 588× | ETL optimization | Pure Python |
| HashSmith | Data structure | JVM-based |
| xgboost-autoresearch | Scientific | Pure Python (needs data download) |
