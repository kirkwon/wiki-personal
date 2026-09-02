---
type: concept
title: Dojo Investigation Workflow
created: 2026-09-01
updated: 2026-09-01
tags:
  - Skill
  - uncategorized
---

# dojo-investigation-workflow

"Investigate dojo findings and apply fixes."

## Usage

# Dojo Investigation Workflow

This skill provides a repeatable process for turning Dojo auto‑heal investigation items into concrete fixes.

## When to use

When the daily dojo run produces `investigate` recommendations (type: investigate) in `latest_analysis.json`.

## Steps

1. **Collect the investigation items**
   - Read `~/.hermes/dojo-eval/latest_analysis.json`
   - Extract items where `"type": "investigate"`
   - For each, note `detail.tool` and `detail.evidence`.

2. **Delegate a focused investigation**
   - For each item, call `delegate_task` with:
     - goal: a concise question derived from the evidence (e.g., "Why does the `process` tool see 'No process with ID 4620'?").
     - context: include the relevant excerpt from latest_analysis.json and any helpful hints (e.g., "look at recent session logs, check classifier patterns").
   - Store the delegation ID.

3. **Review subagent output**
   - Wait for the delegation to complete (or tail the live transcript).
   - Extract the summary and any proposed fix (e.g., regex pattern to add, code change, config update).

4. **Apply the fix**
   - If the fix is a classifier pattern edit:
     - Open `~/.hermes/scripts/dojo-analyze.py`
     - Locate the appropriate pattern list (e.g., `CONTEXT_UNAVAILABLE_PATTERNS` or `MODEL_USAGE_ERROR_PATTERNS`).
     - Add the new regex pattern.
     - Save and run a quick test with `execute_code` to ensure classification works.
   - If the fix is a skill patch:
     - Use `skill_manage(action='patch', name='<skill>', old_string='<...>', new_string='<...>')` targeting the active skill under `~/.hermes/skills/`.
   - If the fix is a config or cron change:
     - Use the appropriate tool (`terminal`, `cronjob`, `hermes config set`).
   - If the fix is to add input validation:
     - Add a check in the relevant tool backend (e.g., `computer_use/cua_backend.py`).

5. **Update documentation**
   - Add a markdown file under `references/` of this skill with:
     - The original investigation goal.
     - The root cause found.
     - The exact fix applied.
     - Any verification steps.
   - Reference the file from SKILL.md.

6. **Verify circuit‑breaker health**
   - Run `python3 ~/.hermes/scripts/circuit-breaker.py --status` to confirm the affected tool’s circuit is closed or improving.

7. **Clean up**
   - Archive duplicate plan files if desired (move older `*.md` plans from `~/.clawd/.hermes/plans/` to `archived-duplicates/`).

## Pitfalls

- Do not patch archived skill copies under `~/.hermes/skills/.archive/`; always target the active skill in `~/.hermes/skills/`.
- Avoid adding overly broad patterns that could misclassify legitimate outputs as errors.
- Remember that some "investigate" items are model‑level retry loops (e.g., repeated `terminal` calls with identical arguments). Those are not fixable by skill patches; instead adjust the classifier to mark them as `won't_fix` or add a note that they are model behavior.
- When editing `dojo-analyze.py`, keep the pa

...(truncated)