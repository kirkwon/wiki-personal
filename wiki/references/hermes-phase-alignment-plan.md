---
date: 2026-07-02
type: source
title: Hermes Skill Phase Alignment Plan
description: "Complete alignment of all skills to the three-phase delegation model (Explore → Sieve → Execute) with cross-master coordination, I/O contracts, and skill queue mapping."
created: 2026-07-02
updated: 2026-07-02
tags:
- reference
- skills
- architecture
- hermes
---

# Hermes Skill Phase Alignment Plan

## The Model

Every skill is classified into one of three phases, which determines the delegation discipline:

| Phase | Name | Input | Output | Contract |
|-------|------|-------|--------|----------|
| **P1** | Explore | Fuzzy topic, open question | Candidates[], findings, options | None — wide aperture. Surprising outputs are wins. |
| **P2** | Sieve | Candidates[] from P1 | Ranked[1] with trade-offs | Light — must declare ranking criteria |
| **P3** | Execute | Specific plan/spec | Verified artifact | Strict — input schema + output schema + DAG position |

## Cross-Master Coordination Map

Masters are NOT isolated silos. Work frequently crosses boundaries. These are the documented edges:

```
                              ┌─────────────────┐
                              │  DISPATCHER     │  ← Zeroeth level: routes ambiguous requests
                              │  (P0 router)    │
                              └────────┬────────┘
                                       │
              ┌────────────────────────┼────────────────────────┐
              │                        │                        │
              ▼                        ▼                        ▼
   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
   │ SOFTWARE-DEV     │   │ KNOWLEDGE        │   │ PRODUCTIVITY     │
   │ Master           │   │ Master           │   │ Master           │
   │ P1→P2→P3         │   │ P1→P2 pipeline   │   │ P3 toolkit       │
   │ Build & ship     │   │ Discover→Digest  │   │ Digital life ops │
   └────────┬─────────┘   └────────┬─────────┘   └────────┬─────────┘
            │                      │                      │
            │  Diagrams ▼          │  Storage ▲           │  Storage ▲
            │  ┌──────────┐        │  ┌──────────┐        │  ┌──────────┐
            ├──► CREATIVE │        ├──► LEARNING │        ├──► KNOWLEDGE│
            │  │ Master   │        │  │ Master   │        │  │ Master   │
            │  │ P3 output│        │  │ P3 retain│        │  │ P3 store │
            │  └──────────┘        │  └──────────┘        │  └──────────┘
            │                      │                      │
            │  ┌──────────┐        │  ┌──────────┐        │  ┌──────────┐
            └──► FINANCE  │        └──► FINANCE  │        └──► FINANCE  │
               │ Master   │           │ Master   │           │ Master   │
               │ P1→P2→P3 │           │ Quant    │           │ Portfolio│
               └──────────┘           │ analysis │           │ dash     │
                                      └──────────┘           └──────────┘
```

### Coordination Contracts (Master-to-Master Edges)

| Edge | Trigger | Data Shape | Output Consumed By |
|------|---------|------------|-------------------|
| **SD → Creative** | "Draw a diagram of this architecture" | `{system_description, diagram_type}` → `{file_path, format}` | SD master includes in docs |
| **Knowledge → Learning** | "Retain this concept" | `{concept, source, key_insights}` → `{memory_tier, next_review}` | Learning master tier system |
| **Knowledge → Finance** | "Research impact of rates on portfolio" | `{topic, depth}` → `{findings[], citations[]}` | Finance master feeds to quant models |
| **Productivity → Knowledge** | "Save this email thread" | `{content, tags}` → `{gbrain_slug, wiki_links[]}` | Knowledge master stores & links |
| **Creative → Knowledge** | "Store this diagram" | `{file_path, description}` → `{gbrain_slug}` | Knowledge master archives output |
| **Finance → Knowledge** | "Save this analysis" | `{analysis_report, metrics}` → `{gbrain_slug}` | Knowledge master cross-links |
| **Finance → Creative** | "Chart this portfolio" | `{data_series[], chart_type}` → `{html_file}` | Creative master renders |
| **SD → Finance** | "Model this trade" | `{trade_spec, parameters}` → `{expected_value, risk}` | Finance master quant models |

---

## Phase 1 — Explore Skills (Wide Aperture, No Contract)

### software-development-master (P1)

| Skill | Input | Output | Surprise Value |
|-------|-------|--------|----------------|
| `brainstorming` | Topic/question | Design options[] | Often produces unexpected approaches |
| `spike` | Hypothesis | Validation findings | May prove assumptions wrong |
| `understand-anything` | Code/System reference | Explanation | Surprising connections in unfamiliar code |
| `explain-code` | Code fragment | Beginner-friendly breakdown | May reveal hidden complexity |

### knowledge-master (P1 — Discover)

| Skill | Input | Output | Surprise Value |
|-------|-------|--------|----------------|
| `arxiv` | Topic/query | Paper candidates[] | Often surfaces unknown research areas |
| `blogwatcher` | Feed URL | New posts[] | Serendipitous discovery of emerging topics |
| `web-researcher` | Topic | Structured findings[] | Cross-source connections not obvious from single angle |
| `last30days` | Topic | Social+news+github pulse | Reveals what people *actually say* vs official narrative |
| `youtube-video-ingestion` | Watch Later | Transcripts[] | Unexpected insights from peripheral content |
| `academic-graph-import` | Paper graph | Paper dataset | May reveal unexpected citation clusters |

### finance-master (P1)

| Skill | Input | Output | Surprise Value |
|-------|-------|--------|----------------|
| `catalyst-calendar` | Portfolio | Upcoming events[] | Often surfaces catalysts user wasn't tracking |

### creativity-master (P1)

| Skill | Input | Output | Surprise Value |
|-------|-------|--------|----------------|
| `creative-ideation` | Problem | Idea candidates[] | Structured methods produce non-obvious directions |
| `multi-perspective-essay` | Topic | Essay with N lenses | Cross-domain perspectives user hadn't considered |

### learning-master (P1 — Reflection)

| Skill | Input | Output | Surprise Value |
|-------|-------|--------|----------------|
| `permanent-questions` | Current focus | Evergreen Q scan | Surfaces stale questions that need revisiting |

### Standalone P1 Skills

| Skill | Input | Output | Surprise Value |
|-------|-------|--------|----------------|
| `research-agent` | Topic | Multi-agent synthesis | 4-agent crew produces divergent perspectives |
| `storm-research` | Topic | Multi-perspective report | Expert-role debates reveal hidden assumptions |
| `autoresearch` | Topic | Propose→test→ratchet | Self-improving research loop |
| `batch-entity-web-scanner` | Entity list | Signal report | Uncovers signals from unexpected sources |

---

## Phase 2 — Sieve Skills (Light Contract: Ranking Criteria)

### software-development-master (P2)

| Skill | Input | Output | Contract |
|-------|-------|--------|----------|
| `writing-plans` | Design options[] | Implementation plan | Must rank by risk/time/complexity |
| `multi-option-architecture-planning` | Architecture approaches[] | Recommended approach | Must compare N approaches on explicit criteria |
| `plan` | Task description | Task list with DAG | Must define dependency order |
| `grill-me` | Plan/design | Stress-test findings | Must rank risks by severity |
| `critical-review` | Artifact | Revision suggestions | Must rank issues by impact |
| `meta-critic` | Artifact + context | Optimal critique dimensions | RL policy selects critique lens |
| `requesting-code-review` | Code + PR | Review report | Must categorize by security/quality/bug |
| `receiving-code-review` | Review feedback | Iteration plan | Must rank by blocker/important/nice-to-have |
| `verify-before-completion-horizon` | Claims[] + evidence[] | Verification report | Must flag unverified claims |
| `project-scaffolding` | Project spec | Directory structure + configs | Must define structure OR skip if already used workspace |

### finance-master (P2)

| Skill | Input | Output | Contract |
|-------|-------|--------|----------|
| `mean-variance-analyzer` | Options[] + probabilities[] | Efficient frontier + recommendation | Must rank by Sharpe ratio, personal risk tolerance |
| `options-market-analysis` | Symbol | P/C ratios, IV skew, term structure | Must rank signals by conviction level |
| `optionality-valuer` | Choice + scenarios[] | Option value + recommendation | Must rank options by flexibility value |
| `socratic-sieve` | Candidates[] | Ranked[1] | Must articulate trade-off criteria |

### productivity-master (P2)

| Skill | Input | Output | Contract |
|-------|-------|--------|----------|
| `inbox-triage` | Inbox items[] | Categorized + filed | Must rank by urgency/importance |
| `session-logging` | Session context | Structured log | Must extract: trials, errors, adaptations, policies |
| `conversation-logging-review` | Session logs | Compressed summary | Must rank patterns by frequency/impact |

### strategy/ (P2)

| Skill | Input | Output | Contract |
|-------|-------|--------|----------|
| `socratic-sieve` | Options[] | Ranked[1] | Must state criteria, top choice, and why others lost |
| `premortem` | Plan | Failure modes ranked | Must rank by probability × impact |
| `kelly-sizer` | Opportunity | Optimal allocation % | Must state p, b, edge, fractional Kelly choice |

---

## Phase 3 — Execute Skills (Strict Contract: I/O Schema + DAG)

### software-development-master (P3)

| Skill | Input Schema | Output Schema | DAG Position | Verification |
|-------|-------------|---------------|-------------|-------------|
| `test-driven-development` | `{spec, code_so_far}` | `{tests_passing, coverage}` | Plan→**TDD**→Implement | Tests must pass |
| `unit-testing` | `{code}` | `{test_file, results}` | Code→**Test**→Review | `pytest --exitfirst` |
| `systematic-debugging` | `{error, context, stacktrace}` | `{root_cause, fix, verified}` | Bug→**Debug**→Ship | Error no longer reproduces |
| `structured-execution` | `{plan, constraints}` | `{artifact, log, issues}` | Design→**Execute**→Review | Artifact matches spec |
| `subagent-driven-development` | `{plan, tasks[]}` | `{subagent_outputs[]}` | Plan→**Dispatch**→Review | Each subagent returns verified output |
| `project-scaffolding` | `{project_type, name, dir}` | `{directory_tree, config_files, readme}` | Design→**Scaffold**→Implement | `tree` command verifies structure |
| `self-harness` | `{weakness, iterations}` | `{harness_improvements[]}` | Observe→**Improve**→Verify | Loop shows CI reduction |
| `verification-before-completion` | `{claims, evidence_gathered}` | `{verified, failing_claims[]}` | Any→**Verify**→Ship | Zero unverified claims |
| `git-operations` | `{action, branch, files}` | `{success, commit_hash}` | Work→**Git**→Push | `git log` shows commit |
| `git-changelog` | `{from_sha, to_sha}` | `{changelog_text}` | Release→**Changelog**→Publish | Diff covers all changes |
| `github-pr-workflow` | `{branch, target, body}` | `{pr_url}` | Done→**PR**→Review | PR link opens correctly |
| `dogfood` | `{app_url, test_cases[]}` | `{bugs[], evidence}` | Build→**QA**→Fix | Each bug has reproduction steps |
| `archify-diagramming` | `{system_description, diagram_type}` | `{html_file, png_clipboard}` | Document→**Diagram**→Include | File opens in browser |
| `hermes-skill-development-workflow` | `{skill_name, description, fallback[]}` | `{SKILL.md, verified}` | Idea→**Create**→Deploy | `skill_manage` loads it |
| `prompt-architecture-operations` | `{system_prompt_current, audit_goal}` | `{audited_prompt, improvement_findings}` | Build→**Audit**→Improve | Prompt compiles |

### finance-master (P3)

| Skill | Input Schema | Output Schema | DAG Position | Verification |
|-------|-------------|---------------|-------------|-------------|
| `portfolio-dashboard` | `{holdings[]}` | `{var_95, sharpe, allocation, pnl}` | Data→**Dashboard**→Report | Flask serves `/api/risk` |
| `portfolio-analyzer` | `{positions[]}` | `{evaluation_report}` | Data→**Analyze**→Decide | Report has all positions |
| `causal-modeling` | `{data, treatment, outcome}` | `{ate, ci_lower, ci_upper, regime_cate}` | Question→**Model**→Interpret | CI captures true effect |
| `game-theoretic-finance-analysis` | `{market_event, agent_types[]}` | `{dominant_strategies, probability_distributions}` | Event→**Simulate**→Strategize | Monte Carlo shows convergence |

### productivity-master (P3)

| Skill | Input Schema | Output Schema | DAG Position | Verification |
|-------|-------------|---------------|-------------|-------------|
| `gmail` | `{action, query, limit}` | `{emails[], success}` | Inbox→**Read**→Act | Content matches query |
| `email-sending` | `{to, subject, body}` | `{sent, message_id}` | Compose→**Send**→Confirm | Recipient confirms receipt |
| `google-workspace` | `{service, action, params}` | `{result}` | Task→**GWS**→Save | Data appears in sheet/doc |
| `docx` | `{content, template, output_path}` | `{file_path, lines, sections}` | Draft→**Doc**→Distribute | `file_path` has expected content |
| `xlsx` | `{headers[], rows[], output_path}` | `{file_path, sheet_names}` | Data→**Sheet**→Analyze | Formulas render correctly |
| `pptx` | `{slides[], output_path}` | `{file_path, slide_count}` | Outline→**Deck**→Present | Slides open in PowerPoint |
| `pdf` | `{action, files[], output}` | `{file_path, page_count}` | Docs→**PDF**→Share | Actions succeed without error |
| `markitdown` | `{input_path, format}` | `{markdown_string, file_path}` | Doc→**Convert**→Ingest | Content preserved in markdown |
| `apple-notes` | `{action, title, body}` | `{success, note_id}` | Idea→**Note**→Reference | Note appears in Apple Notes |
| `apple-reminders` | `{action, list, title, due}` | `{success, reminder_id}` | Task→**Remind**→Done | Reminder appears in app |
| `findmy` | `{action, device}` | `{location, success}` | Locate→**Find**→Alert | Location is current |

### creativity-master (P3)

| Skill | Input Schema | Output Schema | DAG Position | Verification |
|-------|-------------|---------------|-------------|-------------|
| `mermaid-diagrams` | `{diagram_type, description}` | `{svg_or_png, file_path}` | Design→**Diagram**→Document | mmdc renders without error |
| `architecture-diagram` | `{system, components[], relationships[]}` | `{html_file}` | Spec→**Diagram**→Include | File opens in browser |
| `excalidraw` | `{elements[], description}` | `{excalidraw_json, file_path}` | Sketch→**Diagram**→Iterate | JSON loads in Excalidraw |
| `cli-anything-drawio` | `{command, params}` | `{file_path, output}` | Model→**Diagram**→Export | File exists at path |
| `cli-anything-mermaid` | `{command, params}` | `{file_path, url}` | Model→**Diagram**→Share | URL loads diagram |
| `improve-writing` | `{text, tone, goals}` | `{improved_text, changes[]}` | Draft→**Polish**→Publish | Changes are improvements |
| `design-md` | `{spec_content}` | `{DESIGN.md, valid}` | Design→**Document**→Review | DESIGN.md passes validation |
| `archify-diagramming` | `{description, diagram_type}` | `{html_file, png}` | Describe→**Diagram**→Present | File includes all elements |

### learning-master (P3)

| Skill | Input Schema | Output Schema | DAG Position | Verification |
|-------|-------------|---------------|-------------|-------------|
| `memory-tier-system` | `{action, item, target_tier}` | `{success, current_tiers}` | Reflect→**Tier**→Review | Item visible in new tier |
| `defrag` | `{vault_path}` | `{broken_links[], fixes_applied}` | Audit→**Fix**→Report | Broken links count reduces |
| `knowledge-ecosystem-ops` | `{action, params}` | `{result, graph_state}` | Operate→**Maintain**→Verify | Orphans decrease |
| `gbrain-health-dashboard` | `{source}` | `{html_dashboard, metrics}` | Monitor→**Dashboard**→Review | Dashboard loads |

### Research/Academic Pipeline (P3)

| Skill | Input Schema | Output Schema | DAG Position | Verification |
|-------|-------------|---------------|-------------|-------------|
| `analyze-paper` | `{paper_url_or_text}` | `{methodology, findings, limitations, integration}` | Paper→**Analyze**→Store | All 4 sections populated |
| `extract-wisdom` | `{text}` | `{insights, quotes, principles}` | Read→**Extract**→Apply | Insights are novel, not repetition |
| `research-paper-writing` | `{topic, outline}` | `{paper_draft}` | Research→**Write**→Publish | Citations are verified |
| `gbrain-content-ops` | `{slug, content, links[]}` | `{gbrain_response}` | Prepare→**Store**→Verify | `gbrain get slug` returns it |
| `gbrain-minions` | `{queue_items[]}` | `{completed_count}` | Batch→**Process**→Report | Queue drains to 0 |
| `gbrain-graph-enrichment` | `{source_slug, target_slug, relationship}` | `{edge_created}` | Link→**Enrich**→Query | Edge visible in gbrain query |
| `gbrain-to-notebooklm` | `{gbrain_slugs[]}` | `{notebook_id, sources[]}` | Select→**Migrate**→Synthesize | NotebookLM has sources |
| `notebooklm-cli` | `{command, params}` | `{result}` | Operate→**NLM**→Output | nlm query returns results |
| `notebooklm-research-pipeline` | `{topic, sources[]}` | `{notebook, artifacts[]}` | Research→**NLM**→Multi-modal | Artifacts generated |
| `arxiv` | `{query, limit}` | `{papers[]}` | Search→**Fetch**→Read | Results match query |


## Wiki Skill Queue — Candidates for Entry

The following wiki concepts are tagged `skill-candidate` and exist in the wiki but have no active Hermes skill. They are queued for potential entry into the skill system.

### Finance Candidates

| Wiki Concept | Size | Tags | Why It's Queued |
|-------------|------|------|-----------------|
| `leverage-risk-analysis` | 1.1KB | finance, risk-management, real-estate | Risk thresholds (LTV/DSCR) are executable logic |
| `value-at-risk-var` | 1.4KB | finance, risk-management, quantitative | Already implemented in portfolio-dashboard; companion concept |
| `leverage-risk-real-estate` | 892B | finance, real-estate, risk-management | Real estate leverage calculator could be built from this |
| `cash-flow-stress-testing` | 1.3KB | finance, real-estate, risk-management | Scenario engine — rent decline, vacancy, rate hikes |
| `single-property-analysis` | 2.5KB | finance, real-estate | Full analysis template — could automate cap rate/cash-on-cash |
| `1031-exchange-strategy` | 13.8KB | finance, real-estate, tax | Full exchange mechanics — eligible for 1031 calculator skill |
| `retirement-planning` | 14.3KB | finance, retirement | 4% rule, allocation by age, RMD planning |
| `retirement-account-types` | 1.8KB | finance, retirement, tax | Account decision framework (Roth vs Traditional) |
| `required-minimum-distributions-rmds` | 4.2KB | finance, retirement, tax | RMD calculation formula — direct executable logic |
| `low-cost-index-funds` | 1.4KB | finance, investing | Fund comparison + fee impact calculator |
| `low-volatility-factor` | 1.3KB | finance, factors | Factor screen logic |
| `cross-sectional-momentum` | 817B | finance, factors | Momentum ranking logic |
| `net-operating-income` | 1.2KB | finance, real-estate | NOI formula — dependency for single-property-analysis |
| `concentration-risk` | 2.1KB | finance, risk-management, portfolio | HHI calculation — feeds portfolio-dashboard |
| `diversification` | 2.7KB | finance, risk-management, portfolio | Allocation framework |
| `risk-assessment-framework` | 5.6KB | finance, risk-management, real-estate | Master framework — could become risk-assessment skill |
| `tail-risk-and-extreme-outcomes` | 410B | finance, risk-management | Companion to VaR/CVaR |
| `illiquidity-risk` | 2.2KB | finance, risk-management | Liquidity assessment for alternatives |
| `factor-investing` | 3.3KB | finance, factors | Factor model reference for game-theoretic-finance-analysis |
| `market-microstructure-and-options` | 7.8KB | finance, game-theory | Direct input to game-theoretic-finance-analysis |
| `institutional-flow-mechanics` | 8.2KB | finance, game-theory | Agent behavior specs for game-theoretic-finance-analysis |

### Strategy/Decision Candidates

| Wiki Concept | Size | Tags | Why It's Queued |
|-------------|------|------|-----------------|
| `game-theory` | 419B | strategy, finance | Core concept — already referenced by game-theoretic-finance-analysis |
| `game-theory-in-life` | 491B | strategy, finance | Practical applications |
| `game-mental-model` | 2.9KB | strategy, finance, risk-management | Taleb + Sinek — risk alignment principle |
| `pre-mortem-analysis` | 1.7KB | strategy, decision-making | Already has `premortem` skill; complementary concept |
| `inversion-thinking` | 1.8KB | strategy, decision-making | Already referenced by premortem skill |
| `noise` | 2.4KB | strategy, decision-making, finance | Signal-to-noise for portfolio-dashboard |
| `coordination-problems` | 413B | strategy, decision-making | Game theory complement |
| `strategic-sequence` | 2.2KB | strategy, decision-making | Blue Ocean validation framework |
| `skin` | 1.5KB | strategy, finance, risk-management | Taleb's skin-in-the-game — ethical governor for leverage-executor |
| `agent-based-modeling` | 2.5KB | finance, research, strategy | Methodology for game-theoretic-finance-analysis |

## Implementation Order

Priority based on current working skills + user leverage:

**Phase 1 (immediate):** Add phase annotations + I/O contracts to master SKILL.md files
- software-development-master: 46 sub-skills across 7 workflows
- knowledge-master: Pipeline already documented, add phase per skill
- creativity-master: Add phase per skill
- learning-master: Add phase per skill
- productivity-master: Add phase per skill

**Phase 2 (this session):** Create wiki concept pages for the skill queue
- Start with finance candidates that have direct cron/skill connections
- Tag as `skill-candidate`

**Phase 3 (next session):** Create active skills from queued concepts
- Highest leverage: real-estate-analyzer (leverage-risk + single-property + 1031)
- Second: retirement-calculator (4% rule + RMD + account types)
- Third: risk-assessment skill (risk-assessment-framework + concentration + diversification)

---

*Part of the Hermes Skill Ecosystem plan. Phase alignment governance: skill-governance skill.*
