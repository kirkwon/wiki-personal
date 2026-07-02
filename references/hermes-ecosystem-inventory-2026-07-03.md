# Hermes Skill Ecosystem — Complete Inventory

> Generated 2026-07-03
> Purpose: Document the full skill ecosystem for gbrain ingestion and wiki archival
> Masters: 6 · Skills: 244 · Categories: 20

## Architecture

The system uses a **two-layer routing** architecture to solve the "too many tools" problem:

```
User Request → Dispatcher → Meta-Master → Sub-Skill → Execution
```

The dispatcher classifies intent from keywords and routes to the right master. Each master owns a bounded set of sub-skills (10-38). No agent ever sees all 244 skills at once — only the sub-skills of the matched master.

## Meta-Masters

### 1. knowledge-master (38 sub-skills)
Pipeline for the knowledge lifecycle: Phase 1 (Discover) + Phase 2 (Assimilate).
- **Discover**: arxiv, blogwatcher, web-researcher, last30days, youtube-video-ingestion, academic-graph-import
- **Assimilate**: analyze-paper, extract-wisdom, research-agent, storm-research, research-paper-writing, autoresearch, knowledge-ecosystem-ops, knowledge-health, architecture-documentation, cognitive-biases-library
- **Store**: gbrain-content-ops, gbrain-minions, gbrain-skillify, gbrain-to-notebooklm, gbrain-graph-enrichment, gbrain-health-dashboard, gbrain-ops, knowledge-metabolism, memory-tier-system, llm-wiki, obsidian-vault-management, wiki-okf-compliance, wiki-stub-generation, wiki-vault-access, defrag, permanent-questions, media-pipeline-architecture-recap, user-preferences, knowledge-operations, notebooklm-cli, notebooklm-downloader, notebooklm-research-pipeline
- **Web extraction**: crawl4ai (local, free, default)

### 2. learning-master (14 sub-skills)
Phase 3 (Retain) of the GTD-aligned pipeline.
- memory-tier-system, knowledge-metabolism, defrag, gbrain-health-dashboard, knowledge-ecosystem-ops, architecture-documentation, llm-wiki, obsidian-vault-management, user-preferences, notebooklm-cli, notebooklm-downloader, notebooklm-research-pipeline, permanent-questions, cognitive-biases-library

### 3. finance-master (10 sub-skills)
Toolkit for financial analysis — each skill is a different analytical lens.
- portfolio-dashboard, portfolio-analyzer, options-market-analysis, mean-variance-analyzer, causal-modeling, game-theoretic-finance-analysis, optionality-valuer, catalyst-calendar, options-market-analysis/scripts, unified-book-library-management

### 4. productivity-master (24 sub-skills)
Workspace for daily operations — email, documents, notes, calendar, Apple ecosystem, Office.
- **Email**: gmail, inbox-triage, email-sending
- **Documents**: google-workspace, nano-pdf, ocr-and-documents, unify-document-formats, docx, xlsx, pptx, pdf, markitdown
- **Notes**: session-logging, apple-notes, conversation-logging-review
- **Apple**: apple-notes, apple-reminders, imessage, findmy
- **Communication**: one-three-one-rule, conversation-patterns-visualization, social-media

### 5. creativity-master (15 sub-skills)
Studio for generating — diagrams, writing, media, ideation.
- **Diagrams**: mermaid-diagrams, cli-anything-mermaid, cli-anything-drawio, excalidraw, architecture-diagram, diagramming
- **Writing**: improve-writing, creative-ideation, design-md, multi-perspective-essay
- **Media**: youtube-content, gif-search, tts-setup, spotify, gifs

### 6. software-development-master (38 sub-skills)
Workflow engine for software development — plan, implement, test, debug, review, ship.
- **Design**: brainstorming, archify-diagramming, multi-option-architecture-planning
- **Plan**: writing-plans, plan, spike, project-scaffolding
- **Implement**: subagent-driven-development, executing-plans, structured-execution, self-harness, dispatching-parallel-agents, delegate-task-protocol
- **Test**: test-driven-development, unit-testing, ab-test-framework
- **Debug**: systematic-debugging, python-debugpy, node-inspect-debugger, debugging-hermes-tui-commands
- **Review**: verification-before-completion, critical-review, meta-critic, requesting-code-review, receiving-code-review, simplify-code, grill-me, finishing-development-branch
- **Git**: using-git-worktrees, git-changelog
- **Docs**: understand-anything, explain-code, archify-diagramming, architecture-documentation
- **Ship**: dogfood, verification-before-completion, finishing-development-branch

## Governance Layer

- **skill-scorer.py** — Quarterly scoring (recency 40% / frequency 35% / quality 25%)
- **skill-archiver.py** — Archive workflow with consolidation support
- **quarterly-skill-score** cron — Runs Oct 1
- **A/B test protocol** — Documented in each master for overlap pairs
- **Mistake recovery protocol** — Learned from 159-skill deletion incident

## Infrastructure

- **CAO server**: Port 51954, healthy
- **crawl4ai**: Default web extraction (local, free)
- **gbrain**: 36K chunks, 19K pages (local, Ollama embeddings)
- **Memory tiers**: HOT (tool) → WARM (MEMORY.md) → COOL (skills) → COLD (gbrain/wiki)
- **Dispatcher**: Zeroeth-level router, parallel multi-master dispatch
- **Obra Superpowers**: 14 matching skills mapped, methodology integrated
- **anthropics/skills**: docx, xlsx, pptx, pdf ported
- **microsoft/markitdown**: Universal document→markdown converter

## Full Skill Count: 244

### By Category
- Autonomous AI Agents: 10
- Communication: 1
- Creative: 10
- Data Engineering: 2
- Data Science: 2
- Decision: 1
- DevOps: 14
- Finance: 10
- GBrain: 1
- GitHub: 6
- Knowledge: 9
- Knowledge Management: 5
- MCP: 4
- Media: 5
- MLOps: 10
- Note-taking: 6
- Productivity: 11
- Research: 16
- Software Development: 28
- Strategy: 5
- Uncategorized/Freestanding: 88

### Top Skills by Usage (scored Jul 1)
- systematic-debugging: 9
- verification-before-completion: 9
- memory-tier-system: 9
- mermaid-diagrams: 9
- gmail: 9
- google-workspace: 9
- portfolio-dashboard: 8
- options-market-analysis: 8
- mean-variance-analyzer: 8
- research-agent: 8
- storm-research: 8
- knowledge-ecosystem-ops: 8
- gbrain-content-ops: 8
- gbrain-to-notebooklm: 8
- memory-tier-system: 8
- improve-writing: 8
- test-driven-development: 8
- writing-plans: 8
- subagent-driven-development: 8
- delegate-task-protocol: 8
- hermes-skill-development-workflow: 8
- markitdown: 8
- archify-diagramming: 8

## Key Insight from MCP Design Patterns Paper

The Rohan Paul tweet references a paper on MCP server design: LLMs get confused when shown too many tools or vague tools. Our architecture addresses this by:

1. **Intent-based routing** — Dispatcher classifies before showing tools
2. **Bounded contexts** — Each master shows ≤38 skills (avg 23)
3. **Pipeline gating** — software-development-master hides later phases until earlier ones complete
4. **Lens-based design** — finance-master shows different tools vs creativity-master
5. **Quarterly pruning** — scorer archives unused skills (≤3.0 threshold)

This is a significant improvement over a flat skill list of 244 items.
