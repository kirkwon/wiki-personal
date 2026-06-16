---
tags: [analysis, comparison, agent-eval]
created: 2026-06-16
type: comparison
---

# Mimo vs Gemma 4: Technical Task Categorization

## Context

Comparison run on 2026-06-16 to evaluate when to use **Mimo** (autonomous coding agent, API-based) vs **Gemma 4** (local LLM, 9.6GB, Ollama) for different technical task categories.

## Task Categories Tested

### 1. Code Generation

**Task:** Add a `POST /api/batch-merge` endpoint to an existing Flask app (gbrain orphan resolver).

| Aspect | Mimo | Gemma 4 |
|---|---|---|
| Context awareness | ✅ Read actual `app.py`, detected existing endpoint, produced replacement | ❌ Generated standalone with mock helpers — needs manual integration |
| Style consistency | ✅ Used `@app.route()`, followed project patterns | ⚠️ Would add unnecessary imports |
| Correctness | ✅ Used `run_gbrain()`, `get_db()` correctly | ⚠️ Valid logic but wouldn't work in real app |
| Speed | ~15s | ~27s |

### 2. Code Review

**Task:** Find bugs in a deliberately flawed Python function (command injection, file leaks, SQL issues).

| Aspect | Mimo | Gemma 4 |
|---|---|---|
| Issues found | **8** (3 HIGH, 3 MEDIUM, 2 LOW) | **4** (2 HIGH, 1 MEDIUM) |
| Specificity | Named exact lines, gave patched version | Descriptions without line numbers |
| Misses | — | Missed deprecated `os.popen`, `range(len())` anti-pattern |

### 3. Data Transformation

**Task:** Group JSON array by first letter of slug, count types, output compact JSON.

| Aspect | Mimo | Gemma 4 |
|---|---|---|
| Result | ✅ `{"a":{"concept":2,"stub":1},...}` | ❌ Empty response consistently |

Gemma 4 consistently failed to produce structured JSON output from data transformation prompts (temperature 0.2–0.7, various phrasings). This appears to be a systematic weakness.

### 4. Technical Explanation

**Task:** Explain database indexes with SQL example, under 200 words.

| Aspect | Mimo | Gemma 4 |
|---|---|---|
| Output | Wrote `docs/database-index-explanation.md` (156 words) | Inline response, book-analogy style |
| Quality | Technical, file-based | Natural prose, explanatory |

### 5. Stub Generation (prior session)

| Aspect | Mimo | Gemma 4 |
|---|---|---|
| Result | N/A | ✅ 74 stubs regenerated, ~600-700 chars each, accurate content |

### 6. Empty Skeleton Filling (prior session)

| Aspect | Mimo | Gemma 4 |
|---|---|---|
| Result | N/A | ✅ 14 empty pages → substantive content |

## Decision Matrix

| Task Type | Recommended | Rationale |
|---|---|---|
| Write new code | **Mimo** | File-aware, context-correct, follows project conventions |
| Code review | **Mimo** | More thorough (8 vs 4 issues), locates exact lines |
| Data transformation | **Mimo** | Gemma 4 consistently blanked on structured JSON output |
| Refactoring | **Mimo** | Understands existing project, produces surgical changes |
| Concept explanations | **Gemma 4** | Better prose, natural flow, no side effects |
| Wiki/stub content | **Gemma 4** | Purpose-built — good structured content at ~600-700 chars |
| Documentation | **Gemma 4** | Stronger writing quality, file-creation via script |
| Quick one-shot code | **Mimo** | Faster (15s vs 27s), immediately usable output |

## Key Insight

They are **complementary**, not competitive:

- **Mimo** is an autonomous **agent** — explores files, understands projects, acts with intent. Use for anything needing project context.
- **Gemma 4** is a **language model** — strong at prose, explanations, structured content. Use for wiki, docs, conceptual writing.
- **Weakest match:** Gemma 4 struggled with pure structured data transformation. Mimo handled it instantly.
- **Strongest overlap:** Both explained concepts competently, just differently (Mima: technical/file-based, Gemma 4: explanatory/prose).

## Architecture Implication

The current Symphony system dispatches coding tasks to Gemini CLI (API). Mimo could replace Gemini CLI for code-gen-heavy tasks with comparable project-awareness. Gemma 4 (local, free) handles prose-heavy tasks that currently go through API calls.

| Current | Proposed | Monthly Savings |
|---|---|---|
| Gemini CLI (API) → coding | Mimo (API) → coding | Cost-neutral |
| GPT-4o-mini → batch summaries | Gemma 4 (local) → summaries | ~$3-5 |
| OpenAI embed → gbrain | Keep (no local alternative) | ~$0.50-2 |

---

*Tested 2026-06-16 on 16GB Mac, Mimo v0.1.0, Gemma 4 via Ollama*
