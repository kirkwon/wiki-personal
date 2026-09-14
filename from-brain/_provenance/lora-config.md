---
type: note
title: Lora Config
source: hermes-memory
recency: '2026-07-25T00:00:00.000Z'
frequency: weekly
offloaded: '2026-08-03T00:00:00.000Z'
importance: medium
truthfulness: verified
ingested_via: put_page
ingested_at: '2026-08-03T22:28:15.568Z'
source_kind: put_page
created: 2026-08-03
---
# Single-Layer LoRA

- Architecture: single-layer (arm B, L18, rank 64)
- Config: tools.skill_to_lora.command
- Crons: weekly_lora_retrain (547ffc18c9ae) + lora_heartbeat (016810d7afa0)
- Skill: mlops/lora-skill-integration
