

# Hermes Queue — SQLite-Backed Task Orchestration

The Hermes queue was built from squad's SQLite-as-bus pattern — adapted for Hermes subagent workflows with lease-based ownership, role routing, and full operator visibility.

## Why It Exists

Previous approaches to subagent orchestration were invisible:
- **delegate_task** — spawns subagents in the background, results pop back silently
- **Kanban** — visual but poll-based, no blocking read
- **Cron jobs** — fire-and-forget, no task lifecycle

The queue solves this by storing every task in a SQLite file you can inspect at any time: `sqlite3 ~/.hermes/queue/messages.db "SELECT * FROM tasks WHERE status='acked'"`

## Architecture

```
~/.hermes/queue/
├── queue.py          # Python library (open_queue, QueueDB)
├── __main__.py       # CLI (run via `queue` command)
├── queue             # bash wrapper
├── messages.db       # SQLite database (auto-created)
└── tests/test_queue.py  # 44 unit tests
```

### Schema (3 Tables)

**agents** — `(id, role, joined_at, last_seen, status, metadata)` — workers register here with auto-ID suffixing and archived-agent reactivation.

**tasks** — `(id, title, body, created_by, assigned_to, status, priority, tags, session_id, source_skill, lease_owner, lease_expires_at, result_summary, created_at, updated_at, completed_at)` — the queue itself.

**messages** — `(id, from_agent, to_agent, content, task_id, kind, created_at, read)` — peer-to-peer messaging between agents.

### Task Lifecycle

```
enqueue → [queued] → claim → [acked + 15m lease] → complete → [completed]
                        ↓                              ↓
                    skip (re-queued)              cancel (terminal)
```

- **Lease**: 15-minute TTL prevents lost tasks on worker crash
- **Priority**: Higher = more urgent; sorted `priority DESC, created_at ASC`
- **Role routing**: `--to worker` targets role; `--role worker` claims by role

## Key Patterns Worth Noting

### Transactional Read+Mark
Messages are fetched and marked read in the same SQLite transaction — no race conditions:
```python
tx.execute("SELECT ... WHERE read=0 AND to_agent=?")  
tx.execute("UPDATE messages SET read=1 WHERE id IN (...)")  
# atomic
```

### Lease-Based Ownership
```python
# Claim sets lease
UPDATE tasks SET status='acked', lease_owner=?, lease_expires_at=?
WHERE id=? AND status='queued'

# Only lease holder can complete
UPDATE tasks SET status='completed' WHERE id=? AND lease_owner=?
```

### SQLite WAL Mode
Writes don't block reads. `PRAGMA busy_timeout=5000` handles concurrent access gracefully.

## Commands

| Command | Purpose |
|---------|---------|
| `queue count` | Show task counts by status |
| `queue list [--status]` | List tasks (filtered) |
| `queue get <id>` | Show task details |
| `queue enqueue <title>` | Add a task |
| `queue claim <agent>` | Claim highest-priority task |
| `queue complete <id>` | Complete claimed task |
| `queue skip <id>` | Release back to queue |
| `queue cancel <id>` | Cancel entirely |
| `queue requeue <id>` | Reset to queued |
| `queue clean-stale` | Re-queue expired leases |
| `queue register <agent>` | Register a worker |
| `queue agents` | List registered agents |
| `queue send/receive` | Message between agents |

## Stale Lease Cron

Job `queue-stale-lease-cleanup` runs hourly, re-queuing any tasks with expired 15-minute leases. This prevents work from being lost when a subagent crashes mid-task.

## Comparison: Queue vs delegate_task vs Kanban

| Feature | Queue | delegate_task | Kanban |
|---------|-------|---------------|--------|
| Visibility | 🟢 Full SQLite | 🔴 Invisible | 🟡 Poll-based |
| Task lifecycle | 🟢 queued→acked→completed | 🟡 spawned→returned | 🟢 columns |
| Blocking read | 🟢 claim locks | 🟡 no | 🔴 poll only |
| Worker crash safety | 🟢 lease TTL | 🔴 lost | 🔴 lost |
| Cross-CLI agents | 🟢 any CLI | 🔴 Hermes only | 🔴 Hermes only |
| Priority | 🟢 integer | 🟡 none | 🟡 column order |

Sources: [[smart-money-concepts-ict-python]]

See also: [[hermes-queue]]

See also: [[mean-variance-myopia-under-stochastic-volatility]]
