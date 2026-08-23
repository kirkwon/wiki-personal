---
date: 2026-07-01
type: architecture
title: Hermes Agent System Architecture — Data Pipelines, Processes & Storage
status: active
tags: [architecture, data-pipeline, process, storage, mermaid]
created: '2026-07-01T00:00:00.000Z'
---

# Hermes Agent System Architecture

Comprehensive architecture covering data pipelines, processes, and data storage. Mermaid diagrams that render in GitHub, Notion, Obsidian, and any Mermaid-compatible viewer.

> **See also:** [[concepts/hermes-agent-stack]] for the cognitive DAG (awareness → analysis → exploration → interaction → interpretation → learning → communication). This document adds the infrastructure layer.

---

## 1. System Context (C4 Level 1)

```mermaid
C4Context
  title System Context — Hermes Agent Ecosystem

  Person(user, "Kirk Won", "Human operator & decision-maker")

  System(hermes, "Hermes Agent", "The agent runtime — skill system, tool loop, MCP client, cron scheduler")

  System_Ext(telegram, "Telegram", "Message delivery & alerts")
  System_Ext(github, "GitHub", "Source repos, skills, tools")
  System_Ext(web, "Web / APIs", "External data sources")

  Boundary(boundary, "Local Infrastructure") {
    SystemQueue(cron, "Cron Jobs", "Scheduled tasks (no_agent + LLM)")
    SystemDb(gbrain, "GBrain", "Semantic memory — 20k+ pages, vector search, entity graph")
    SystemDb(wiki, "Wiki-Personal", "Markdown wiki — raw/papers/prompts/concepts")
    SystemDb(state, "State DB", "Session history — SQLite (state.db)")
    SystemQueue(queue, "Hermes Queue", "Task queue — SQLite-backed")
    System_Ext(mcp, "MCP Servers", "13 MCP tools — Brave, OpenBB, GitHub, etc.")
    System_Ext(ollama, "Ollama", "Local LLM inference — Ornith, Gemma, nomic-embed")
  }

  Rel(user, hermes, "Chats via Telegram / DM")
  Rel(hermes, telegram, "Delivers briefs & alerts")
  Rel(hermes, web, "Web searches, repo clones")
  Rel(hermes, github, "Clones & ingests repos")
  Rel(hermes, cron, "Schedules & runs tasks")
  Rel(cron, hermes, "Triggers agent tasks (LLM mode)")
  Rel(hermes, mcp, "Tool calls via MCP protocol")
  Rel(hermes, gbrain, "Query & store semantic memory")
  Rel(hermes, wiki, "Read & write wiki pages")
  Rel(hermes, state, "Logs session history")
  Rel(hermes, queue, "Enqueue & claim tasks")
  Rel(hermes, ollama, "Local embeddings & inference")

  UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")
```

---

## 2. Data Pipeline — Full DAG

The cognitive stack as a data pipeline, annotated with storage points and data formats.

```mermaid
flowchart LR
  subgraph Awareness["AWARENESS — Context Injection"]
    direction TB
    A1[MEMORY.md] --> A
    A2[memory/YYYY-MM-DD.md] --> A
    A3[USER.md] --> A
    A4[gbrain retrieval] --> A
    A5[quick-recap footer] --> A
    A((Awareness Context))
  end

  subgraph Analysis["ANALYSIS — Reasoning"]
    direction TB
    B1[read-the-damn-docs] --> B
    B2[Super Hermes prisms] --> B
    B3[knowledge-eval.py] --> B
    B4[premortem skill] --> B
    B((Analyzed Intent))
  end

  subgraph Exploration["EXPLORATION — Discovery"]
    direction TB
    C1[web_search / web_extract] --> C
    C2[delegate_task subagents] --> C
    C3[git clone → ingestion] --> C
    C4[knowledge-metabolism gap check] --> C
    C((Discovered Data))
  end

  subgraph Interaction["INTERACTION — Execution"]
    direction TB
    D1[Tool calls / Terminal] --> D
    D2[MCP Server calls] --> D
    D3[File read/write/patch] --> D
    D4[skill_manage] --> D
    D((Action Output))
  end

  subgraph Interpretation["INTERPRETATION — Synthesis"]
    direction TB
    E1[GBrain dream cycle] --> E
    E2[Concept synthesis] --> E
    E3[prism-reflect] --> E
    E4[GraphMind queries] --> E
    E((Synthesized Knowledge))
  end

  subgraph Learning["LEARNING — Growth"]
    direction TB
    F1[MEMORY.md update] --> F
    F2[Skill create/patch] --> F
    F3[Cron consolidation] --> F
    F4[Dojo auto-fix] --> F
    F((Persistent Changes))
  end

  subgraph Communication["COMMUNICATION — Delivery"]
    direction TB
    G1[Telegram brief] --> G
    G2[Text-to-speech] --> G
    G3[Inbox triage] --> G
    G4[quick-recap footer] --> G
    G((User-Facing Output))
  end

  A --> B
  B --> C
  C --> D
  D --> E
  E --> F
  F --> G

  G -.->|user feedback / correction| A

  style A fill:#e1f5fe,stroke:#01579b
  style B fill:#f3e5f5,stroke:#7b1fa2
  style C fill:#e8f5e9,stroke:#1b5e20
  style D fill:#fff3e0,stroke:#e65100
  style E fill:#fce4ec,stroke:#880e4f
  style F fill:#e0f7fa,stroke:#006064
  style G fill:#f1f8e9,stroke:#33691e
```

---

## 3. Processes

### 3.1 Dojo Pipeline — Auto Self-Improvement

```mermaid
flowchart TD
  subgraph Cron["Daily Cron 7:30am"]
    direction LR
    S[d o j o - e v a l . s h] --> M
  end

  subgraph Monitor["Phase 1: Monitor"]
    M[dojo-eval.py] -->|reads| DB[(state.db)]
    M -->|detects| F[Tool failures]
    M -->|detects| C[User corrections]
    M -->|detects| R[Retry loops]
    M -->|detects| G[Skill gaps]
  end

  subgraph Analyze["Phase 2: Analyze"]
    M -->|JSON pipe| A[dojo-analyze.py]
    A -->|classifies| RC[8 root-cause categories]
    A -->|generates| FR[Fix recommendations]
    A -->|maps to| SK[Existing skills]
  end

  subgraph Circuit["Phase 3: Circuit Breakers"]
    M -->|feeds| CB[circuit-breaker.py]
    CB -->|updates| CST[(circuit-breakers.json)]
    CB -->|opens circuits| OPEN[🔴 Blocked tools]
  end

  subgraph Fix["Phase 4: Fix (on-demand)"]
    FR -->|load via| SF[dojo-fix skill]
    SF -->|applies via| SM[skill_manage patch/create]
    SM -->|updates| SKILL[(~/.hermes/skills/)]
  end

  subgraph Report["Output"]
    CB -->|generates| BRIEF[Telegram brief]
    FR --> BRIEF
    M --> BRIEF
  end

  style Monitor fill:#e3f2fd,stroke:#1565c0
  style Analyze fill:#f3e5f5,stroke:#7b1fa2
  style Circuit fill:#fff3e0,stroke:#e65100
  style Fix fill:#e8f5e9,stroke:#1b5e20
  style Report fill:#f1f8e9,stroke:#33691e
```

### 3.2 Ingestion Pipeline — Repo → Wiki → GBrain

```mermaid
flowchart LR
  subgraph Safety["Safety Gate"]
    SC[skill-scan / SkillSpector] -->|score ≤ 20| OK((✅ SAFE))
    SC -->|score 21-50| CAUTION((⚠️ Prompt user))
    SC -->|score 51+| BLOCK((🔴 BLOCKED))
  end

  subgraph Ingest["Ingestion"]
    direction TB
    IG[ingest-skill / ingest-repo / ingest-paper] -->|git clone + copy| RAW[(wiki-personal/raw/repos/)]
    IG -->|convert + structure| CONV[Conversion]
  end

  subgraph Index["Indexing"]
    CONV -->|gbrain sync| GB[(GBrain)]
    CONV -->|GraphMind index| GM[(code graph)]
    CONV -->|embed| OLLAMA[Ollama nomic-embed-text]
    OLLAMA --> GB
  end

  subgraph Maintain["Maintenance"]
    GB -->|dream cycle| E[Entity extraction]
    GB -->|concept synthesis| CS[Auto-concept pages]
    GB -->|orphan scan| OR[Orphan cleanup]
    GB -->|advisor| AD[Health report]
  end

  REPO[GitHub Repo / Paper / Skill] --> Safety
  OK --> Ingest
  CAUTION -->|user approves| Ingest
```

### 3.3 Cron Cascade

```mermaid
flowchart TD
  subgraph Every_180m["Every 180m"]
    L1[LLm-wiki → GBrain delta sync]
    L2[symphony-dispatch + collect]
  end

  subgraph Daily["Daily"]
    D0[GBrain Live Sync - 3:00am]
    D1[GBrain Daily Backup - 3:00am]
    D2[Token Usage Log - 2:00am]
    D3[GBrain Nightly Dream - 2:00am]
    D4[Backup Integrity Verify - 3:05am]
    D5[Project Dashboard Sync - 6:00am]
    D6[SPCX Monitor - 6:30am wkdays]
    D7[Morning Briefing - 7:00am]
    D8[Knowledge Eval - 8:00am]
    D9[Inbox Triage - 7/12/21]
    D10[Market Close Summary - 1:05pm wkdays]
    D30[Dojo Eval - 7:30am]
  end

  subgraph Weekly["Weekly"]
    W1[GBrain Weekly Health - Mon 6am]
    W2[Weekly Maintenance - Mon 2am]
    W3[Weekly Hedge Signal - Mon 9am]
    W4[Weekly Macro Brief - Mon 9am]
    W5[Weekly Questions Scan - Mon]
    W6[Stale Page Watchdog - Mon 10am]
    W7[Memory Tier Demotion - Sun 9am]
    W8[Weekly Review - Sun 6pm]
    W9[Comprehension Debt - Mon 9am]
    W10[IPO Catalyst Scan - Sat 7am]
  end

  subgraph Monthly["Monthly"]
    M1[GBrain Monthly Review - 1st 4am]
    M2[GBrain Quarterly Cleanup - 1st 5am]
    M3[Cron Monthly Audit - 1st 8am]
  end

  Every_180m --> Daily
  Daily --> Weekly
  Weekly --> Monthly

  style Daily fill:#e3f2fd,stroke:#1565c0
  style Weekly fill:#f3e5f5,stroke:#7b1fa2
  style Monthly fill:#fff3e0,stroke:#e65100
```

---

## 4. Data Storage

### 4.1 Storage Map

```mermaid
flowchart LR
  subgraph Local["Local Filesystem"]
    SKILLS[~/.hermes/skills/]:::storage
    SCRIPTS[~/.hermes/scripts/]:::storage
    CONFIG[~/.hermes/config.yaml]:::storage
    WIKI[~/wiki-personal/]:::storage
    CRON[~/.hermes/cron/]:::storage
    LOGS[~/.hermes/logs/]:::storage
  end

  subgraph Databases["Databases"]
    STATE[(~/.hermes/state.db<br/>SQLite — session history)]:::db
    QUEUE[(~/.hermes/queue/messages.db<br/>SQLite — task queue)]:::db
    GRAIN[(PostgreSQL — GBrain<br/>20266 pages, 36389 chunks)]:::db
  end

  subgraph StateFiles["State Files (JSON)"]
    EVAL[~/.hermes/knowledge-eval/history.json<br/>Metric time series]:::state
    DOJO[~/.hermes/dojo-eval/<br/>Analysis + fix plans + thresholds]:::state
    CB[~/.hermes/dojo-eval/circuit-breakers.json<br/>Per-tool circuit states]:::state
    THRESH[~/.hermes/knowledge-eval/thresholds.json<br/>Alert thresholds]:::state
    DEMOTE[~/.hermes/memory/tier-tracker.json<br/>Memory tier state]:::state
  end

  subgraph Memory["Agent Memory"]
    MEM[~/clawd/MEMORY.md<br/>Long-term curated]:::mem
    DAILY[~/clawd/memory/*.md<br/>Daily session logs]:::mem
    USER[~/clawd/USER.md<br/>User profile]:::mem
    SOUL[~/clawd/SOUL.md<br/>Agent identity]:::mem
  end

  subgraph External["External"]
    TG[Telegram — delivery channel]
    GH[GitHub — source repos]
  end

  classDef storage fill:#e8f5e9,stroke:#2e7d32
  classDef db fill:#e3f2fd,stroke:#1565c0
  classDef state fill:#fff3e0,stroke:#e65100
  classDef mem fill:#fce4ec,stroke:#c62828
```

### 4.2 Data Volume & Freshness

```mermaid
flowchart TD
  subgraph Size["Storage Size Estimates"]
    SS10[~2 MB — state.db (SQLite session store)]
    SS11[~50 KB — queue DB]
    SS12[~300 MB — GBrain PostgreSQL (20k pages, 36k chunks, vectors)]
    SS13[~5 MB — wiki-personal markdown files]
    SS14[~100 KB — skills + scripts + config]
  end

  subgraph Freshness["Update Cadence"]
    FR1[state.db — every tool call (continuous)]
    FR2[GBrain — 180m sync + nightly dream cycle]
    FR3[Memory files — per session]
    FR4[Circuit breakers — per dojo eval run (7:30am)]
    FR5[Eval history — daily (8:00am)]
  end

  subgraph Criticality["Backup Status"]
    BK1[GBrain — daily backup script ✓]
    BK2[Wiki — git versioned ✓]
    BK3[state.db — not backed up ⚠️]
    BK4[Config — git versioned ✓]
    BK5[Skills — git versioned ✓]
  end
```

---

## 5. Tool Tiers & Reliability

```mermaid
flowchart TD
  subgraph Critical["🟢 Critical — No Circuit Breaker"]
    T1[read_file, write_file, patch, terminal, search_files, memory, todo, cronjob]
  end

  subgraph Standard["🟡 Standard — 5 fails → 5min open"]
    T2[web_search, web_extract, skill_view, skills_list, skill_manage, session_search, vision_analyze, browser_navigate]
  end

  subgraph NonCritical["🔴 Non-Critical — 3 fails → 10min open"]
    T3[mcp_* tools, browser_*, delegate_task, execute_code, computer_use, text_to_speech, image_generate]
  end

  subgraph Bulkhead["Bulkhead Isolation"]
    direction TB
    B1[Critical tools unaffected by non-critical failures]
    B2[Non-critical tools can be skipped without system impact]
    B3[Circuit state persisted between sessions]
  end

  Critical --> Bulkhead
  Standard --> Bulkhead
  NonCritical --> Bulkhead
```

---

## 6. Related Documents

- [[concepts/hermes-agent-stack]] — Cognitive DAG (awareness → communication)
- [[concepts/knowledge-metabolism]] — 3D cube model for knowledge health
- [[concepts/self-maintaining-knowledge-base]] — KB auto-maintenance
- [[concepts/super-hermes-prisms]] — Analytical prism system
- [dojo-fix skill](~/.hermes/skills/dojo-fix/SKILL.md) — Fix application skill
- [circuit-breaker.py](~/.hermes/scripts/circuit-breaker.py) — Circuit breaker + bulkhead implementation
- [dojo-eval.py](~/.hermes/scripts/dojo-eval.py) — Session failure monitor
- [dojo-analyze.py](~/.hermes/scripts/dojo-analyze.py) — Root cause analysis + fix recommendations
- [GBrain architecture](~/.gbrain/) — Semantic memory system
