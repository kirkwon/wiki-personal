---
type: concept
title: Hermes Autoclaw Bridge
created: 2026-09-12
updated: 2026-09-12
tags:
  - Skill
  - uncategorized
---

# hermes-autoclaw-bridge

Bridge for invoking AutoClaw skills from within Hermes Agent workflows

## Usage

# Hermes to AutoClaw Bridge

This skill provides patterns and tools for integrating AutoClaw skills with Hermes Agent workflows, enabling you to leverage AutoClaw's external access capabilities (web search, media processing, integrations) within Hermes' reasoning and knowledge management framework.

## Overview

AutoClaw and Hermes are complementary systems:
- **AutoClaw**: Optimized for reaching outward (web, media, integrations, content generation)
- **Hermes**: Optimized for thinking inward (strategy, knowledge, code quality, agent autonomy)

This bridge enables you to combine both strengths in your workflows.

## Environment Setup

Before using AutoClaw skills from Hermes, ensure the AutoClaw environment is activated:

```bash
source "$HOME/.openclaw-autoclaw/venv/bin/activate"
```

You can verify the CLI is working with:
```bash
autoclaw skills list
```

## Direct Shell Invocation

## Direct Shell Invocation

```bash
# Example: web search
autoclaw skill run web-search-plus \
    --query "latest LangChain 0.2 release notes" \
    --max-results 5

# Example: YouTube metadata
autoclaw skill run youtube-watcher \
    --channel-id UCXuqSBlHAE6Xw-yeJA0Tunw \
    --max-results 3 \
    --format json

# Example: Image generation
autoclaw skill run autoglm-generate-image \
    --prompt "a cyberpunk fox reading a scroll, ultra-detail, 8k" \
    --width 1024 --height 1024 \
    --out /tmp/fox.png
```

## Direct Script Invocation (when CLI not available)

Some AutoClaw skills expose a standalone script (e.g., `scripts/search.py` for web-search-plus) that can be run directly when the `autoclaw` CLI is not installed or when you need fine‑grained control over provider selection and API keys.

```bash
# Example: run the web-search-plus script directly
cd ~/.openclaw-autoclaw/skills/web-search-plus/scripts
export TAVILY_API_KEY="your-key-here"   # or SERPER_API_KEY, etc.
python search.py --query "LangChain 0.2 release notes" --max-results 3 --provider tavily
```

The script returns JSON (or markdown if you add `--raw‑content`‑style flags) that you can capture and feed into Hermes skills just like the wrapper:

```python
import subprocess
def run_autoclaw_script(script_path, args=None):
    cmd = ["python", script_path]
    if args:
        for k, v in args.items():
            cmd.extend([f"--{k}", str(v)])
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout  # adjust parsing as needed
```

Remember to export any required API keys as environment variables before invoking the script; the script will fall back through its providers if one fails.

### Using the Tavily Helper Script

A convenience script `tavily-search` is available at `/Users/kirkwon/.openclaw-autoclaw/workspace/scripts/tavily-search`. It wraps the Tavily API and expects the environment variable `TAVILY_API_KEY` to be set.

```bash
# Basic usage
tavily-search \"your query\"             # default 5 results
tavily-search \"query\" -n 10            

...(truncated)