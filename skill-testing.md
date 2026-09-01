---
type: concept
title: Skill Testing
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - uncategorized
---

# skill-testing

"Use when verifying that a model (local Ollama, remote API, or any Hermes provider) behaves correctly for a specific structured task before relying on it in production. Always test responsiveness and output quality prior to production workflows."

## Usage

# Skill Testing and Validation for Hermes Agent

**When to use this skill:** When verifying that a model (local Ollama, remote API, or any Hermes provider) behaves correctly for a specific structured task before using it in production. Always test responsiveness and output quality *prior* to relying on a model for a workflow.

**This skill emerged from:** B4 LLM stub enrichment session (2026-08-23), where ornith-9b was assumed ready without testing, and the test revealed timeout/latency issues that would have wasted a full batch run.

---

## Core Principle

**Never assume a model is ready. Always test before you trust.**

This applies especially to:
- Local Ollama models (per-session availability varies, context length limits real)
- Models you haven't used for *this specific task* before
- Structured output tasks (JSON, specific schema) — unstructured chat success doesn't predict structured output reliability

---

## Testing Protocol

### Step 1: Verify the model is reachable

```bash
curl -s --max-time 5 http://localhost:11434/api/tags | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'OK: {len(d[\"models\"])} models')"
```

If this fails, the model isn't available — stop here, don't proceed with testing.

### Step 2: Test with the EXACT task format you'll use in production

Use a minimal batch (3-5 items) that mirrors the production prompt structure exactly. Don't test with a simplified prompt — the failure mode is often in the interaction between prompt complexity and model capability.

Key elements to test:
- **Batch size**: Start at 3, then 5, then 10. Don't jump to production batch size.
- **Prompt structure**: Use the same instructions, same output format requirement, same examples.
- **Timeout**: Set a generous timeout (120s+ for local models) and actually measure elapsed time.
- **Output parsing**: Test your JSON extraction logic against the real output, not a hand-crafted example.

### Step 3: Evaluate the results

For structured JSON tasks:
- Did the model produce valid JSON? (parseable as `json.loads()`)
- Did it follow the schema? (array of batches, each batch an array of `{target, reason}`)
- Are the suggested targets valid? (exist in the slug index — for wiki tasks)
- How many suggestions per page? (quality vs quantity tradeoff)

For unstructured tasks:
- Is the output coherent and on-topic?
- Does it follow the requested format/length?

### Step 4: Decide based on test results

| Result | Action |
|--------|--------|
| Valid JSON, good targets, fast (<60s/batch) | Proceed to production with that model + batch size |
| Valid JSON but slow (>90s/batch) | Note the latency; consider smaller batches or a different model |
| Invalid JSON, but extractable with fallback | Document the fallback; proceed with caution |
| Invalid JSON, not extractable | Don't use this model for this task. Try a different model or simplify the task. |
| Timeout with no output | Model may be overloaded or unsuitable. Try another model. |

---

#

...(truncated)