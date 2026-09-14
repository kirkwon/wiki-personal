---
type: concept
title: Hermes Buzz Integration
ingested_via: put_page
ingested_at: '2026-08-01T02:57:09.453Z'
source_kind: put_page
created: 2026-08-01
---
---
type: concept
title: Hermes Agent Integration with Buzz (Nostr Workspace)
---

# Hermes Agent Integration with Buzz (Nostr Workspace)

Source: MarkTechPost article (2026-07-31)
URL: https://www.marktechpost.com/2026/07/31/nous-research-ships-three-integration-paths-for-hermes-agent-and-buzz-blocks-open-source-nostr-workspace-for-humans-and-agents/

## Three Integration Paths

1. **Buzz Desktop managed runtime**:
   - Buzz spawns Hermes locally as a preset harness
   - Discoverable via `hermes-acp` launcher in `~/.local/bin`
   - Inbound: ACP over stdio
   - Zero configuration for solo developers/small teams

2. **Relay bridge**:
   - Transport integration (not a second install)
   - Buzz’s `buzz-acp` harness bridges a channel to `hermes acp` over stdio
   - Reaches relay via WebSocket
   - Subprocess shares same config, credentials, memory, skills, state as local Hermes

3. **Native gateway platform**:
   - Bundled `buzz` plugin makes Buzz a normal Hermes messaging platform
   - Covers channels, DMs, mention gating, threaded replies, reactions, images, cron delivery
   - Hermes keeps its own approvals, memory, session management
   - Setup: `hermes gateway setup`

## Key Resilience & Reliability Features

- **Identity per agent**: Each agent gets its own keypair, channel memberships, and audit trail (removes bot-token model)
- **Signed events**: Every message is a signed event on a user-owned relay (Nostr)
- **Persistent authenticated transport**:
  - Inbound: NIP-42-authenticated Nostr WebSocket with BIP-340 signing
  - Fallback: CLI polling every 4 seconds (configurable)
  - Outbound: Always via Buzz CLI
- **Event deduplication**: By event ID against per-channel high-water mark
- **Message filtering**: Agent’s own messages filtered by pubkey to prevent echo loops
- **Private-by-default defaults**:
  - `require_mention: true` (agent answers only when addressed in channels)
  - `allow_all_users: false` (restricts access to listed npubs/hex pubkeys)
  - `interim_assistant_messages: false` and `tool_progress: off` (keeps tool log out of channel)
- **Infrastructure control**: Relay runs on Postgres, Redis, S3/MinIO (self-hostable)

## Operational Benefits for Resilience

- **Incident memory**: Channel history provides immutable audit trail for debugging
- **Branch-as-room workflows**: Enables isolated environments for code review, testing
- **Agent-drafted artifacts**: Release notes, reports generated within trusted channel context
- **Cron-delivered reports**: Reliable scheduled output via Buzz’s delivery system
- **No vendor lock-in**: Self-hostable Apache-2.0 licensed Buzz

## Risks & Trade-offs

- Desktop runtime auto-approves tool permissions → security risk if not owner-only
- Mobile clients and workflow approval gates still under development (per article)
- Enterprises should treat as pilot until mobile/workflow features mature

## Connection to Hermes Resilience Goals

This integration provides:
1. Cryptographic audit trail (via Nostr signatures) for forensic analysis
2. Transport redundancy (WebSocket + polling fallback)
3. Identity-based message filtering to reduce noise and prevent loops
4. Self-hostable infrastructure control
5. Structured channels for isolating failure domains (e.g., dev vs prod agents)

Suggested builds to leverage this for resilience:
- Sync Hermes decision logs to Buzz as signed events for immutable audit trail
- Use Buzz channels for health checks, circuit breaker status, and self-diagnostics
- Implement config drift detection by comparing Hermes state to Blob stored in Buzz
- Create agent-specific channels for sandboxed experimentation with rollback via event history
- Leverage deduplication and pubkey filtering to build resilient internal messaging

