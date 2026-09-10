---
date: 2026-07-19
type: concept
title: Skill Vetting
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/skill-vetting
description: 'Security vetting for agent skills and repositories. Scans for vulnerabilities
  (68 patterns, 17 categories) before installing. Uses NVIDIA SkillSpector. Gates
  installs on risk score: SAFE (0-20), CAUTION (21-50 requires confirmation), DANGER
  (51+ blocked).'
---

# Skill Vetting

> Security vetting for agent skills and repositories. Scans for vulnerabilities (68 patterns, 17 categories) before installing. Uses NVIDIA SkillSpector. Gates installs on risk score: SAFE (0-20), CAUTION (21-50 requires confirmation), DANGER (51+ blocked).

## Overview

- **Score Interpretation** — | Score | Severity | Exit | Action | |:-----:|----------|:----:|--------| | 0-20 | LOW — SAFE | 0 | Install | | 21-50 | MEDIUM — CAUTION | 1 | Ask user | | 51+ | HIGH/CRITICAL — DANGER | 2 | Block |
- **What It Scans For** — 17 categories: prompt injection, anti-refusal, data exfiltration, privilege escalation, supply chain (unpinned deps, curl-bash, CVEs via OSV.dev), excessive agency, output handling, system prompt leakage, memory poisoning, tool misuse, rogue agent, trigger abuse, behavioral AST (exec/eval/subprocess), taint tracking, YARA malware signatures, MCP least privilege, MCP tool poisoning.
- **Workflow** — 1. Identify target: local dir, git URL, or SKILL.md 2. Run `skill-scan <target>` for structured verdict 3. **SAFE** (exit 0): proceed with install 4. **CAUTION** (exit 1): present findings, ask confirmation 5. **DANGER** (exit 2+): block install, show findings

## Further detail

### MCP Tool

SkillSpector runs as an MCP server registered in Hermes config: `mcp_skillspector__scan_skill(target, use_llm, output_format)`

### Baseline

After first scan, suppress known findings:

### Integration

- **Before repo ingestion**: Run `skill-scan` before `ingest-repo`/`ingest-paper` - **Before skill install**: `ingest-skill` bakes scan into install flow - **Knowledge-metabolism**: Ingest stage includes ingest-skill with safety gate

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/skill-vetting/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
