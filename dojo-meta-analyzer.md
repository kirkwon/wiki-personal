---
type: concept
title: Dojo Meta Analyzer
created: 2026-09-11
updated: 2026-09-11
tags:
  - Skill
  - meta-learning
---

# dojo-meta-analyzer

"Analyzes patterns in dojo-eval outputs over time to suggest skill improvements and systemic fixes, implementing a meta-learning approach inspired by ALMA's reflection loops."

## Usage

# Dojo Meta Analyzer

A meta-skill that analyzes historical dojo-eval outputs to identify patterns, co-failure patterns, and systemic issues that suggest skill improvements or architectural changes.

## How It Works

1. **Collects** historical dojo-eval outputs from cron logs
2. **Analyzes** patterns in failure types, retry loops, and skill gaps over time
3. **Identifies** systemic issues vs. transient problems
4. **Suggests** targeted skill improvements or configuration changes
5. **Logs** findings for review and potential auto-application

## Key Features

- Pattern-based analysis rather than reactive fixing
- Focus on co-failure patterns (multiple related failures pointing to one root cause)
- Differentiates between transient issues and systemic problems
- Leverages existing dojo-eval infrastructure and classification systems
- Outputs actionable insights for skill maintenance

## Usage

Run the analyzer:

```bash
# Analyze last 7 days of dojo-eval data
python3 ~/.hermes/skills/dojo-meta-analyzer/scripts/analyze_patterns.py

# Analyze specific time window
python3 ~/.hermes/skills/dojo-meta-analyzer/scripts/analyze_patterns.py --days 30

# Generate report for review
python3 ~/.hermes/skills/dojo-meta-analyzer/scripts/analyze_patterns.py --report
```

## Output

The skill generates:

- Pattern analysis report in `~/.hermes/skills/dojo-meta-analyzer/logs/`
- Suggested skill improvements with confidence scores
- Identification of co-failure patterns
- Recommendations for configuration or architectural changes

## Integration with Hermes

This skill works alongside the existing dojo-eval system:

1. Standard dojo-eval runs continue to provide immediate feedback
2. This meta-skill runs periodically (e.g., weekly) to analyze trends
3. Insights feed into skill improvement decisions
4. High-confidence suggestions can be auto-applied or queued for review

## Safety Features

- Analysis-only mode by default (no automatic changes)
- Requires explicit opt-in for auto-application of suggestions
- All suggestions include confidence scores and reasoning
- Integrates with existing decision logging and verification systems

## References

- Inspired by ALMA's reflection loops and meta-learning approach
- Builds on existing dojo-eval infrastructure (`dojo-eval.py`, `dojo-analyze.py`)
- Uses Hermes session logging and skill versioning systems

## Scripts

The skill includes:

- `analyze_patterns.py`: Main analysis script
- `pattern_detector.py`: Utilities for detecting failure patterns
- `suggestion_generator.py`: Generates improvement suggestions from patterns
- `confidence_scorer.py`: Scores confidence in suggested improvements

## Example Analysis

The meta-skill might identify patterns like:

- \"Web search failures consistently occur when Camofox is unavailable, suggesting need for better fallback handling\"
- \"Repeated vision_analyze failures with small images indicate need for image preprocessing in the skill\"
- \"CLI tool failures spike after system upd

...(truncated)