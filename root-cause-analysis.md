---
type: concept
title: Root Cause Analysis
created: 2026-09-03
updated: 2026-09-03
tags:
  - Skill
  - devops
---

# root-cause-analysis

>-

## Usage

# Root Cause Analysis Toolkit

## When to Use

Triggered by: system failures, cron job errors, outages, recurring bugs,
performance degradation, or any incident requiring post-mortem.

## The 10 RCA Methods

Each method has a sweet spot. Using the wrong one wastes time.

| Method | Best For | Effort | Output |
|--------|----------|--------|--------|
| **Brainstorming** | Unknown territory, need to surface all possibilities | Low | Idea list (unprioritized) |
| **Fishbone (Ishikawa)** | Multi-factor problems with clear categories | Medium | Categorized cause tree |
| **5 Whys** | Simple, linear cause-effect chains | Low | Single root cause |
| **Cause Mapping** | Events with multiple interconnected causes | Medium | Relationship graph |
| **Fault Tree Analysis (FTA)** | Complex systems, safety-critical, probabilistic | High | Boolean logic tree with failure probabilities |
| **Process Mapping** | Workflow failures, bottleneck identification | Medium | Step-by-step flow diagram |
| **FMEA** | Proactive — anticipate failures before they happen | High | Risk priority numbers (RPN) |
| **Pareto Analysis** | Prioritizing which of many causes to fix first | Low | 80/20 ranked list |
| **Scatter Diagram** | Correlation analysis between variables | Low | Visual correlation plot |
| **Barrier Analysis** | Safety incidents — what controls failed? | Medium | Failed/prevented barrier list |

## Decision Framework: Which Method When?

```
Is the problem NEW or RECURRING?
├── NEW → Is it complex (multiple systems)?
│   ├── YES → FTA or Cause Mapping
│   └── NO → 5 Whys
└── RECURRING → Pareto Analysis (which cause accounts for 80%?)
    └── Then apply the method suited to the top cause

Is the problem in a WORKFLOW/PROCESS?
├── YES → Process Mapping + Fishbone
└── NO → Is it a SAFETY incident?
    ├── YES → Barrier Analysis + FTA
    └── NO → Is data available for correlation?
        ├── YES → Scatter Diagram + Pareto
        └── NO → Brainstorming → Fishbone

Proactive (before failure)?
└── FMEA
```

## The Hopper Protocol — Cron-Specific RCA

For cron job failures, use this streamlined 5-step protocol:

### Step 1: Capture the Error Signature
```bash
# Get the exact error, exit code, and timestamp
hermes cron logs <job_id> --last 5
```

### Step 2: Environment Diff
The #1 cause of cron failures is environment mismatch (PATH, env vars,
working directory). Check ALL of these:

| Check | Interactive Shell | Cron Environment |
|-------|------------------|------------------|
| PATH | Full user PATH | Minimal `/usr/bin:/bin` |
| Working dir | User's CWD | Usually `/` or user home |
| Env vars | All loaded | Only CRON_* prefixed |
| Shell | User's shell (zsh/bash) | `/bin/sh` (POSIX) |
| Python | venv/uv activated | System python only |

### Step 3: Dependency Trace
```bash
# Check every binary the script calls
grep -oP '(?:^|\s)([a-zA-Z_][a-zA-Z0-9_]*)' script.sh | sort -u | while read cmd; do
  which "$cmd" 2>/dev/null || echo "MISSING: $cmd"
done
```

### Step 4:

...(truncated)