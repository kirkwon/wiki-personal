---
type: concept
title: Macos Bsd Shell Portability
created: 2026-09-10
updated: 2026-09-10
tags:
  - Skill
  - uncategorized
---

# macos-bsd-shell-portability

"Use when writing or debugging bash scripts on macOS."

## Usage

# macOS / BSD Shell Portability Traps

macOS ships BSD userland, not GNU coreutils. Scripts written against GNU
assumptions often **succeed wrongly or fail silently** — worse than a hard
error, because a cron job wrapping them reports `ok` while producing garbage.

This is about the userland, not bash itself. For bash-semantics traps (e.g.
`set -e` + `((var++))`), see the separate bash-trap skill.

## Always-on rules

1. **Never assume GNU flag semantics.** Before using a flag learned on Linux,
   confirm it on this machine (`mktemp --help`, `man date`, or just run it). BSD
   tools commonly accept the same flag with a *different meaning* (`sed -i`),
   or reject it outright.
2. **A pattern that "works once" is untested.** Re-run any temp-file,
   in-place-edit, or filename-generating pattern 2–3 times in a row before
   trusting it. Several BSD traps only manifest on the *second* invocation.
3. **Verify under cron-like conditions, not your interactive shell:**
   `env -i HOME="$HOME" PATH=/usr/bin:/bin bash script.sh`. Cron's PATH omits
   `/opt/homebrew/bin`, so a Homebrew-provided binary that works interactively
   can be absent in cron.
4. **Prefer the portable form when two exist.** `${TMPDIR:-/tmp}` not a bare
   `/tmp`; trailing-X `mktemp` templates; `sed -i ''` rather than assuming GNU
   `sed -i`.

## The traps

### `mktemp` — the X's must be TRAILING (verified by reproduction)

BSD `mktemp` does **not** substitute `X`s when a suffix follows them:

```bash
mktemp /tmp/x-XXXXXX.md    # BAD — creates a LITERAL file /tmp/x-XXXXXX.md
mktemp /tmp/x-XXXXXX       # GOOD — substitutes, e.g. /tmp/x-Ab3dEf
mktemp -t prefix           # GOOD on macOS — creates inside $TMPDIR
```

**Mechanism:** the first call *succeeds* by creating a file literally named
`...XXXXXX.md`. Every later call then fails with
`mkstemp failed ... File exists`. So the bug is invisible in a single test and
permanent in production.

**Why it is nasty:** if the temp file sits on a *fallback* path, the failure is
swallowed and the job reports something misleading ("no data", "zero items
added") instead of a temp-file error — sending you to debug the wrong layer.

**Fix:** `TEMP=$(mktemp "${TMPDIR:-/tmp}/x-XXXXXX")` (works on BSD and GNU), or
`mktemp -t x` on macOS.

### `sed -i` requires an explicit (empty) backup suffix

```bash
sed -i 's/a/b/' f      # GNU. On macOS: sed: 1: "...": invalid command code
sed -i '' 's/a/b/' f   # macOS — note the empty '' argument
```

### `date` arithmetic has a different flag

```bash
date -d '1 day ago'    # GNU
date -v-1d             # BSD / macOS
```

### `readlink -f` and `stat -c` are not portable

Both are GNU forms absent/different on BSD. Use a Python one-liner for
realpath, and BSD `stat -f` for formatted stat:

```bash
python3 -c 'import os,sys; print(os.path.realpath(sys.argv[1]))' "$path"
```

### `grep -P` (PCRE) is unavailable

BSD `grep` has no `-P`. Use `grep -E`, or `perl`/`python3` for lookaround.

## Verification recipe

```b

...(truncated)