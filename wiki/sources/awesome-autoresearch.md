---
type: source
tags: [autoresearch, curated-list, awesome-list, survey]
related: [autoresearch-pattern, karpathy-autoresearch-loop, experiment-loop]
---

# awesome-autoresearch

A curated awesome list of public autoresearch use cases across industries.

**URL:** https://github.com/yibie/awesome-autoresearch
**Maintainer:** @yibie
**License:** MIT
**Cloned:** 2026-06-29
**Coverage:** 684 entries across 14 category files + 5 open categories

## Structure

### Populated categories
| Category | Entries | Domain |
|----------|---------|--------|
| scientific-research | 68 | science, medicine, lab, ML research |
| software-systems-optimization | 52 | performance, kernels, compilers, code |
| evaluation-red-teaming | 23 | benchmarking, jailbreaking, testing |
| finance-trading | 32 | trading strategies, market analysis |
| personal-knowledge-humanities | 2 | genealogy, personal wikis |
| knowledge-base-rag-preparation | 2 | RAG prep, knowledge curation |
| workflow-automation | 4 | operational loops |
| infra-skills-forks | 132 | engines, harnesses, ports, dashboards |
| related-practices-discussions | 146 | X threads, Reddit, HN |

### Seeding in progress (0 entries)
| Category | Domain |
|----------|--------|
| competitive-intelligence | competitive landscape tracking |
| content-research | content strategy via autoresearch |
| customer-discovery | customer insights via autoresearch |
| lead-generation | lead gen via autoresearch |
| trend-monitoring | trend monitoring via autoresearch |

## Inclusion criteria
- Source must be public and citable
- Directly about autoresearch (explicit mention, Karpathy citation, or modify → verify → keep/discard → repeat loop)
- Summary explains scenario, method, and value in one sentence
- No generic agents, vague commentary, or private claims

## Build pipeline
- `scripts/build-readme.py` — aggregates category files into README.md
- `scripts/update-awesome-autoresearch.sh` — periodic refresh
- `scripts/commit-and-push.sh` — auto publish
- `scripts/install-launchd-job.sh` — macOS launchd integration

## Curation skill
The repo ships its own curation agent skill at `.agents/skills/autoresearch-curation/SKILL.md` — designed for Hermes agents to maintain the list autonomously with strict inclusion rules, promotion workflow, and periodic sweeps.

## Key patterns extracted
### The three-file architecture (Karpathy canonical)
- `prepare.py` — immutable data preparation (chmod 444)
- `train.py` — **only** mutable file; agent edits this
- `eval.py` — fixed evaluator, agent cannot change

### Variants across domains
- **Paired-seed** — two runs per change to filter noise
- **Scout-promote** — cheap scout runs → full eval for strong candidates
- **Multi-agent** — decentralized teams sharing hypothesis pools
- **Paper-augmented** — MCP server with paper corpus to inform proposals
- **Phased strategist** — strategist → researcher → experimenter roles
- **100-round scaffold opt** — optimizing the agent harness itself
- **Self-healing** — autonomous recovery from experiment failures
- **Evidence-gated** — falsification gates before promotion
