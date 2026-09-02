---
type: concept
title: Information Effectiveness Evaluator V2
created: 2026-09-01
updated: 2026-09-01
tags:
  - Skill
  - uncategorized
---

# information-effectiveness-evaluator-v2

"Assesses agent info effectiveness: gather, retain, apply."

## Usage

# Information Effectiveness Evaluator v2
Assesses agent info effectiveness: gather, retain, apply with GraphWork compliance.
Evaluates whether an agent system is gathering and using information effectively, with focus on retaining important insights and connecting knowledge to actionable behaviors. Includes specific checks for GraphWork methodology compliance.

## When to Use
- Assessing if research insights are being retained in long-term knowledge systems
- Evaluating whether gathered information translates to improved system behavior
- Checking if knowledge storage mechanisms are being actively used in decision-making
- Reviewing if there's a gap between information collection and behavioral application
- Verifying GraphWork methodology compliance in projects

## Prerequisites
- Access to agent's memory systems (gbrain, MEMORY.md, daily logs)
- Access to agent's configuration and workflow documentation (SOUL.md, AGENTS.md, USER.md)
- Ability to search through past conversations and session history
- Familiarity with the agent's current projects and active workflows
- Knowledge of GraphWork methodology requirements

## How to Run
Invoke through the `execute_code` tool with a Python script that:
1. Reads key documentation files (SOUL.md, AGENTS.md, USER.md, MEMORY.md)
2. Searches for recent learning imports and knowledge retention evidence
3. Evaluates alignment between gathered information and active project work
4. Checks GraphWork compliance in projects
5. Generates a structured assessment report

## Quick Reference
- read_file: SOUL.md, AGENTS.md, USER.md, MEMORY.md
- search_files: "gbrain", "research", "academic-graph-import", "GRAPH.md", "graph_runner.py"
- session_search: Review recent conversations for learning applications and past conversations for learning applications
- web_search: Verify if important papers have been processed
- execute_code: Run evaluation logic and generate report

## Procedure
1. **Review Core Operating Principles**
   - Read `SOUL.md` to understand agent's information philosophy
   - Read `AGENTS.md` to check for mandated information practices
   - Read `USER.md` to understand user-specific information preferences
   - Check for GraphWork-scaffolded projects (GRAPH.md, AGENTS.md, decisions/ folders)

2. **Assess Knowledge Retention Systems**
   - Read `MEMORY.md` to see curated long-term knowledge
   - Search for evidence of gbrain operations and research imports
   - Check for recent entries in `memory/YYYY-MM-DD.md` files showing learning capture
   - Verify if GraphWork projects have memory/ directories being used

3. **Evaluate Information-to-Behavior Connection**
   - Search recent conversations where learning was applied
   - Look for `graph_runner.py`, `GRAPH.md` files to see behavior mapping efforts
   - Check for explicit connections between imported papers and active project work
   - Review decisions/decision-log.md for insights leading to specific decisions
   - Verify ACTIVITY.md shows application o

...(truncated)