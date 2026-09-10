---
date: 2026-07-19
type: concept
title: Knowledge Maintenance
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge-management
sources:
- hermes://skill/knowledge-maintenance
description: Perform periodic knowledge maintenance tasks
---

# Knowledge Maintenance

> Perform periodic knowledge maintenance tasks

## Overview

- **Actions** — When invoked, this skill will perform the following maintenance tasks:
- **Important Notes** — - This skill is designed to be run periodically via a cron job, but can also be triggered automatically by the Hermes agent when knowledge maintenance context is detected in conversation. - Each sub-task logs its results for review in the session output. - For best results, run this skill weekly to maintain knowledge base health. - **Performance Note**: This skill can take 20+ minutes to complete due to the comprehensive nature of the checks. Consider running during off-peak hours. - **Delegation Constraint**: In some contexts (such as skill review sessions), the `delegate_task` tool may not b
- **Usage** — This skill is designed to be run periodically via a cron job, but can also be triggered automatically by the Hermes agent when knowledge maintenance context is detected in conversation.

## Further detail

### Notes

- Actions 1 and 2 may take a significant amount of time depending on the size of the knowledge base. - Consider running this skill during off-peak hours. - Review the output logs to verify completion and address any issues. - Consider running this skill during off-peak hours. - Review the output logs to verify completion and address any issues.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/knowledge-maintenance/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
