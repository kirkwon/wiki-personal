---
created: 2026-07-03
updated: 2026-07-03
---
# Using AutoClaw Skills with Hermes

## Overview
You now have **AutoClaw** installed alongside your Hermes agent.  
The skill comparison file is located at:

```
~/.openclaw-autoclaw/workspace/SKILLS-COMPARISON.md
```

This file outlines the 82 AutoClaw skills (vs. 246 Hermes skills) and highlights where each system excels.

## How to Access AutoClaw Skills from Hermes

1. **Activate the AutoClaw environment (if not already):**
   ```bash
   source "$HOME/.openclaw-autoclaw/venv/bin/activate"
   ```

2. **List available AutoClaw skills:**
   ```bash
   autoclaw skills list
   ```

3. **Run a skill directly from the shell:**
   ```bash
   # Example: web search (no Firecrawl needed)
   autoclaw skill run web-search-plus \
       --query "latest LangChain 0.2 release notes" \
       --max-results 5
   ```

4. **Call AutoClaw skills from within Hermes (recommended for pipelines):**
   Use a small Python wrapper inside an `execute_code` block or a delegated task:

   ```python
   from hermes_tools import terminal

   def run_autoclaw(skill: str, args: dict = None):
       cmd = ["autoclaw", "skill", "run", skill]
       if args:
           for k, v in args.items():
               cmd.extend([f"--{k}", str(v)])
       res = terminal(command=" ".join(cmd))
       if res["exit_code"] != 0:
           raise RuntimeError(f"AutoClaw error: {res['output']}")
       return res["output"]

   # Example usage
   output = run_autoclaw(
       "web-search-plus",
       {"query": "2024 Nobel Prize in Physics winners", "max-results": "3"}
   )
   # `output` now contains markdown you can feed to Hermes skills
   ```

5. **Commonly useful AutoClaw skills**
   - `web-search-plus` – enhanced web search (uses crawl4ai/curl)
   - `youtube-watcher` – fetch YouTube metadata
   - `autoglm-generate-image` – text‑to‑image via AutoGLM
   - `markdown-converter` – PDF/HTML → Markdown
   - `backtest-expert` – quick quant back‑test
   - `ffmpeg-video-editor` – simple video edits
   - `notion` / `feishu-cron-reminder` – productivity integrations

## Connecting to Your Personal Knowledge (GBrain)

The wiki‑personal vault (`~/wiki-personal/`) is already wired into your **GBrain** knowledge graph via the standard wiki‑to‑NotebookLM sync workflow.

To make this new note searchable in GBrain:

1. **Ensure the file is saved** (as done above) under `wiki-personal/`.
2. **Run the sync script** (if you have it configured) or manually add the file as a source to your GBrain‑linked NotebookLM notebook:
   ```bash
   # Example using the helper script (adjust paths as needed)
   ./scripts/update-wiki-to-notebooklm.sh \
       "Personal Knowledge Base" \
       pkb \
       "$HOME/wiki-personal" \
       OpenClawUsage.md
   ```
   This will:
   - Strip any YAML frontmatter / wikilinks (if present)
   - Add the cleaned content as a source in the notebook aliased `pkb`
   - Make the content queryable via `nlm notebook query` and usable for AI‑generated outputs (reports, audio, infographics, etc.)

## Quick Reference: Where Each System Shines

| Domain | AutoClaw Strength | Hermes Strength |
|--------|-------------------|-----------------|
| **External access** | Web search, image/audio generation, Notion/1Password/TMUX, FFmpeg, Vercel, weather | Limited to local tools & APIs you expose |
| **Content generation** | Website builder, frontend design, PRD→app, PDF conversions, YouTube factory | Structured output via NotebookLM (reports, mind‑maps, slides, audio) |
| **Channel integrations** | 1Password, Feishu, Notion, YouTube watcher, stock analysis | Deep agent autonomy, dispatcher, evolver, subagent‑driven dev |
| **Finance / Quant** | Basic stock/US‑stock analysis, back‑test expert | Full Bayesian Rogue suite, mean‑variance analyzer, options market, causal modeling |
| **Knowledge & GBrain** | Can ingest history from Claude, Codex, Copilot, Pi, Hermes | gBrain ecosystem, memory‑tier system, wiki governance, cognitive‑biases library |
| **MLOps / AI dev** | AutoGLM image/gen, whisper transcription | DSPy, Guidance, Outlines, MLX local models, NotebookLM pipeline, token optimization |
| **Software craft** | GitHub ops, agentic coding workflows | 40+ dev skills (debugging, scaffolding, testing, review, architecture) |

## Next Steps
- Explore the `SKILLS-COMPARISON.md` file for the full list.
- Try a quick AutoClaw skill (e.g., `web-search-plus`) and pipe its markdown output into a Hermes summarization or NotebookLM query.
- Keep this note under version control (your wiki‑personal repo) so future updates to AutoClaw are documented here.

---
*This page is intended to be ingested into your personal wiki and linked to GBrain via the standard wiki‑to‑NotebookLM synchronization pipeline.*