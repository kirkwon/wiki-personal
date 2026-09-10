---
date: 2026-07-19
type: concept
title: Wiki Content Quality
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- wiki
- quality
- llm
- stub-generation
- content-audit
- note-taking
sources:
- hermes://skill/wiki-content-quality
description: Audit wiki content quality, identify empty/skeletal pages, and regenerate
  low-quality content using local LLMs (Gemma 4 >> Qwen3 for accuracy).
---

# Wiki Content Quality

> Audit wiki content quality, identify empty/skeletal pages, and regenerate low-quality content using local LLMs (Gemma 4 >> Qwen3 for accuracy).

## Overview

- **When This Skill Activates** — - User asks to "spot check the wiki", "fix stubs", "improve wiki quality" - User reports factual errors or vague content in wiki pages - You need to batch-regenerate low-quality wiki content - You're deciding which local LLM to use for content generation
- **Prerequisites** — - Local Ollama running with models installed: `gemma4` (recommended), `qwen3:8b` (fallback) - Wiki directory: `~/wiki-personal/wiki/concepts/` - Helper scripts: `~/.hermes/scripts/stub-filler.py`, `~/.hermes/scripts/regenerate-stubs-gemma4.py`
- **Model Selection** — | Model | Quality | Speed | Best For | |-------|---------|-------|----------| | **gemma4** (9.6GB) | ✅ Excellent — specific, correct, mentions creators | ~7-15s/call on 16GB Mac | All content generation | | **qwen3:8b** | ❌ Poor — vague, hallucinated (micrograd → "educational program") | ~3-5s/call | NOT recommended for factual content |

## Further detail

### Temperature Settings

| Model | Temperature | Notes | |-------|------------|-------| | gemma4 | **0.7** | Lower temps (0.2) produce empty responses on this model | | qwen3:8b | 0.3 | Works at default temp — but avoid this model |

### Categorization: What's Worth Regenerating

| Category | Includes | Action | |----------|----------|--------| | **A — Empty skeletons** | Frontmatter-only pages for well-known concepts (GTD, Ray Dalio, judgment) | ✅ Regenerate — highest impact | | **B — Important concepts, thin** | bayesian-thinking (1 sentence), interleaving, pareto-principle | ✅ Regenerate | | **C — Culinary/foreign imports** | Sushi terms in Japanese, tea processing in Chinese | ❌ Skip — LLM is weaker here; these serve as searchable stubs | | **D — Short but accurate** | 300-600 char pages with correct content | Lower priority — keep unless user requests expansion |

### Validation

After regeneration, verify:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/note-taking/wiki-content-quality/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
