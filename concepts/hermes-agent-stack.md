---
date: 2026-07-01
type: concept
title: Hermes Agent Cognitive Stack — Directed Graph
status: active
tags: [architecture, cognition, agent-design, stack, directed-graph]
created: '2026-07-01T00:00:00.000Z'
---

# Hermes Agent Cognitive Stack

A directed graph mapping how the agent moves from raw awareness to effective communication. Each stage feeds forward into the next, with learning loops feeding back into earlier stages.

```
AWARENESS ──► ANALYSIS ──► EXPLORATION ──► INTERACTION ──► INTERPRETATION ──► LEARNING ──► COMMUNICATION
    ▲                                                                                         │
    └───────────────────────────────── feedback loop ─────────────────────────────────────────┘
```

---

## Stage 1: Awareness

**What makes the agent know what's happening.**

The agent doesn't start from zero — it wakes up into a pre-loaded context of persistent memory, session logs, and environmental signals.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| `read-the-damn-docs` skill | Web-search API docs before guessing | → Analysis (grounds reasoning in facts) |
| GBrain retrieval | Semantic search over 20k+ pages at session start | → Analysis, Exploration |
| Memory injection | `MEMORY.md`, `memory/YYYY-MM-DD.md`, `USER.md` auto-loaded | → All downstream stages |
| `quick-recap` convention | Status footer in every response (🟢/🟡/🔴) | → Communication (user sees status) |
| Cron failure watchdog | `cron-failure-watchdog.sh` every 30min on Telegram | → Communication (user alerted) |
| Session_search | FTS5 retrieval over past conversations | → Analysis (learn from history) |
| `gbrain` retrieval-reflex | Zero-LLM entity resolution when a named entity appears | → Analysis (immediate grounding) |

**Directed edges:**
```
Awareness → Analysis:    Grounds reasoning in retrieved context
Awareness → Exploration: Triggers search when context is insufficient
Awareness → Learning:    Memory persistence updates across sessions
```

---

## Stage 2: Analysis

**How the agent processes and understands what it knows.**

Analysis is the bridge between raw data and actionable insight. It includes both structured evaluation and creative reasoning.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| Super Hermes prisms | `prism-scan`, `prism-full`, `prism-3way`, `prism-discover`, `prism-reflect` — self-written analytical lenses | → Interpretation, Learning |
| `knowledge-eval.py` | Passive 3-memory health metrics + trend tracking | → Communication (reports breaches) |
| `premortem` skill | Decision analysis: 5-step failure pre-mortem | → Communication (Telegram brief) |
| GBrain advisor | Health scoring: brain_score (80/100), orphan ratio, sync freshness | → Awareness (doctor runs) |
| Trend computation | Δ between consecutive snapshots (↑ improvement / ↓ regression) | → Learning (identifies decay) |
| Socratic questioning | Divergent-to-convergent funnel from SOUL.md | → Interaction (narrows intent) |

**Directed edges:**
```
Analysis → Exploration:  Identifies knowledge gaps → triggers search/ingest
Analysis → Interpretation: Feeds structured data into synthesis
Analysis → Learning:      Evaluates what worked → adjusts approach
Analysis → Communication: Generates health reports and briefs
```

---

## Stage 3: Exploration

**How the agent discovers new information.**

Exploration is the divergent phase — parallel research, repository ingestion, web searches, and gap detection.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| `delegate_task` | Parallel subagents for research/code review | → Interaction (parallel tool use) |
| `web_search` / `web_extract` | External knowledge retrieval (curl, browser) | → Awareness, Interpretation |
| Repo ingestion | `git clone` → `wiki-personal/raw/repos/` | → Learning (semiosphere growth) |
| Browser navigation | `browser_navigate` for dynamic page interaction | → Interaction |
| `knowledge-metabolism` skill | `check-gaps`, `suggest-pipeline`, `link-eval` commands | → Analysis (gap quantification) |
| GBrain dream cycle | Entity extraction, concept synthesis, link resolution | → Interpretation (concept formation) |
| GraphMind CLI | Symbol graph analysis over codebases (2451 symbols, 874 edges in clawd) | → Interpretation (architectural insight) |

**Directed edges:**
```
Exploration → Interpretation: Raw data → synthesized concepts (GBrain dream)
Exploration → Learning:        New pages → wiki growth → skill updates
Exploration → Awareness:       Search results enrich context for next turn
```

---

## Stage 4: Interaction

**How the agent engages with tools, systems, and the user.**

Interaction is the execution layer — where analysis and exploration translate into tool calls, file operations, and human dialogue.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| Hermes agent loop | Tool calls, subprocess execution, file ops | → All stages (the runtime) |
| Skill system | `skill_manage`, `skill_view`, `skills_list` | → Learning (skill creation/patches) |
| Terminal tool | Shell commands, builds, git, cron management | → All stages |
| File tools | `read_file`, `write_file`, `patch`, `search_files` | → All stages |
| Computer use | `computer_use` for desktop GUI interaction | → Awareness (captures screen state) |
| Telegram delivery | Sends briefs, alerts, and reports | → Communication |
| Voice stories | `text_to_speech` for engaging delivery | → Communication |
| Socratic funnel | 3-phase interaction: Explore → Sieve → Exploit | → Analysis (narrows intent) |

**Directed edges:**
```
Interaction → Communication: Tool outputs → formatted delivery to user
Interaction → Learning:      User corrections → skill patches
Interaction → Analysis:      Mid-turn steering refocuses analysis
```

---

## Stage 5: Interpretation

**How the agent synthesizes meaning from structured and unstructured data.**

Interpretation is where raw information becomes understanding — concepts are formed, connections are drawn, and insights emerge.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| GBrain concept synthesis | Auto-generates concept pages from entity link clusters | → Learning (wiki growth) |
| Super Hermes `prism-reflect` | Constraint transparency: what it knows it missed | → Learning (growth loop) |
| `knowledge-metabolism` link-eval | Evaluates connection density between skills and concepts | → Analysis (gap report) |
| GBrain `ask` / `query` | Hybrid search with RRF + expansion | → Awareness (context enrichment) |
| GraphMind queries | `graph-query` for symbol-level architectural analysis | → Exploration (targeted search) |
| Entity extraction | Facts, takes, atoms from page content | → Learning (semiosphere growth) |

**Directed edges:**
```
Interpretation → Learning:     Synthesized concepts → wiki pages → skill updates
Interpretation → Communication: Insights → formatted briefs/reports
Interpretation → Awareness:     Enriched context for future sessions
```

---

## Stage 6: Learning

**How the agent improves over time.**

Learning is the growth layer — memory persistence, skill refinement, cron tuning, and semiosphere expansion that compound session over session.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| MEMORY.md | Long-term curated memory (episodic + procedural) | → Awareness (injected every turn) |
| `memory/YYYY-MM-DD.md` | Daily session logs | → Awareness, Analysis |
| Skill creation/patches | `skill_manage create/patch` after successful workflows | → Interaction (future sessions) |
| Cron consolidation | Merging/removing redundant cron jobs | → Communication (reduced noise) |
| GBrain semiosphere | 20k+ wiki pages growing with each ingested repo | → Awareness (richer retrieval) |
| `knowledge-eval.py` history | 365-day rolling metrics with trend analysis | → Analysis (identifies decay) |
| (Future) Dojo auto-fix | Monitor state.db → classify → auto-patch skills | → Interaction (self-healing) |

**Directed edges:**
```
Learning → Awareness:     Updated memory → different initial context next session
Learning → Analysis:      Historical trends inform new evaluations
Learning → Communication: Less noise, higher signal over time
```

---

## Stage 7: Communication

**How the agent reports, collaborates, and delivers value.**

Communication is the output layer — the user-facing interface of the entire stack.

| Component | Mechanism | Integrates With |
|-----------|-----------|-----------------|
| Telegram delivery | Cron alerts, briefings, summaries | → User (the ultimate sink) |
| Emoji tone matching | 0-2 emojis, mirroring user energy (SOUL.md) | → User (natural interaction) |
| `text_to_speech` | Voice stories, engaging delivery | → User |
| Inbox triage | Summarized email/alerts with escalation | → Awareness (feeds back) |
| `knowledge-metabolism` run-health | Structured health reports | → User |
| `quick-recap` footer | 🟢/🟡/🔴 status on every response | → User |
| Cron Failure Watchdog | `cron-failure-watchdog.sh` every 30min | → User (error visibility) |

**Directed edges:**
```
Communication → Awareness: User feedback (corrections, steering) → memory updates
Communication → Learning:  User's "remember this" → skill/memory persistence
Communication → Analysis:  User's "check X" → triggers new eval
```

---

## Full Directed Graph (DAG)

```
                    ┌─────────────┐
                    │  AWARENESS  │ ◄────────────────────────────┐
                    │  (context)  │                              │
                    └──────┬──────┘                              │
                           │                                      │
                           ▼                                      │
                    ┌─────────────┐                              │
                    │  ANALYSIS   │                              │
                    │  (understand)│                              │
                    └──────┬──────┘                              │
                           │                                      │
                     ┌─────┴──────┐                              │
                     ▼            ▼                              │
              ┌──────────┐  ┌───────────┐                       │
              │EXPLORATION│  │INTERACTION│                       │
              │(discover) │  │  (act)    │                       │
              └─────┬─────┘  └─────┬─────┘                      │
                    │              │                              │
                    └──────┬──────┘                              │
                           ▼                                      │
                    ┌──────────────┐                             │
                    │INTERPRETATION│                             │
                    │  (synthesize)│                             │
                    └──────┬──────┘                             │
                           │                                      │
                           ▼                                      │
                    ┌───────────┐                               │
                    │  LEARNING │                               │
                    │  (grow)   │                               │
                    └─────┬─────┘                               │
                          │                                       │
                          ▼                                       │
                    ┌──────────────┐                            │
                    │COMMUNICATION │─────────────────────────────┘
                    │   (deliver)  │  user feedback → memory update
                    └──────────────┘
```

**Feedback loops:**
1. **Communication → Awareness**: User corrections → memory updates → different context next session
2. **Learning → Awareness**: Persistent memory → injected into every session start
3. **Exploration → Awareness**: Search results enrich immediate context
4. **Interaction → Learning**: User steering → skill patches

---

## Layer Mapping to SOUL.md Principles

| SOUL.md Principle | Stack Stage | Manifestation |
|-------------------|-------------|---------------|
| Bayesian Rogue | Analysis | Mean-variance thinking, leverage-seeking |
| Socratic Architect | Interaction | Divergent→Convergent funnel |
| Lucky Bias | Exploration | High-entropy Gittins wildcards |
| Black Swan Protocol | Analysis | "One thing that breaks this" check |
| Closed-System Pivot | Analysis | Immediate fix mode for broken systems |
| Data Integrity | Awareness | "I don't know" > guessing |
| Id-forward Explorer | Exploration | Curiosity-driven discovery |
| Strategic Leverager | All | Asymmetric upside, bounded downside |

---

## Related Pages

- [[SOUL.md]] — Agent identity and principles
- [[knowledge-metabolism]] — 3D cube model for knowledge health
- [[self-maintaining-knowledge-base]] — Knowledge base auto-maintenance
- [[hermes-agent-skills]] — Full skill inventory
- [[gbrain-ecosystem]] — GBrain integration architecture
- [[premortem-skill]] — Decision analysis skill
- [[super-hermes-prisms]] — Analytical prism system
- [[architecture/hermes-system-overview]] — Data pipelines, processes, storage (Mermaid diagrams)

---

## Domain Master Extensions (2026-07-15)

The core 7-stage stack integrates with four Domain Master layers and two Loop Engine layers:

### Domain Masters
| Master | Integration Points |
|:-------|:-------------------|
| [[documentation-master]] | Awareness, Learning |
| [[decision-master]] | Analysis, Learning |
| [[productivity-master]] | Interaction, Learning |
| [[knowledge-master]] | Awareness, Exploration, Learning |

### Loop Layers
| Layer | Function |
|:------|:---------|
| [[learning-loop]] | Three-tier improvement (Execution/Harness/Meta) |
| [[self-health-loop]] | Continuous system monitoring and repair |

See [[sources/p6-hermes-architecture-layers-domain-masters.md]] for full architectural extension specification.
