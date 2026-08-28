---
type: concept
title: Apple Notes
created: 2026-08-27
updated: 2026-08-27
tags:
  - Skill
  - apple
---

# apple-notes

Read, search, and create Apple Notes via AppleScript and Notes CLI

## Usage

# Apple Notes Integration

Read, search, create, and manage Apple Notes on macOS.

## Usage

### Search Notes
```bash
# Search notes by keyword
osascript -e 'tell application "Notes" to set matching to every note whose body contains "keyword"'

# List all notes with names
osascript -e 'tell application "Notes" to set noteNames to name of every note'
```

### Read Note Content
```bash
# Get note body
osascript -e 'tell application "Notes" to get body of note "Note Name" of folder "Notes" of account "iCloud"'

# Get plain text body
osascript -e 'tell application "Notes" to set noteBody to body of note "Note Name" of folder "Notes" of account "iCloud"'
```

### Create Note
```bash
# Create new note in default folder
osascript -e '
tell application "Notes"
    set newNote to make new note at folder "Notes" of account "iCloud" with properties {name: "Title", body: "Content"}
end tell'
```

### List Folders/Accounts
```bash
# List all accounts
osascript -e 'tell application "Notes" to set accountNames to name of every account'

# List folders in iCloud
osascript -e 'tell application "Notes" to set folderNames to name of every folder of account "iCloud"'
```

## Common Patterns

### Extract notes for GBrain ingest
```bash
osascript -e '
tell application "Notes"
    set output to ""
    repeat with acct in every account
        set acctName to name of acct
        repeat with fldr in every folder of acct
            set fldrName to name of fldr
            repeat with n in every note of fldr
                set output to output & "---" & linefeed & "# " & name of n & linefeed & "Source: " & acctName & "/" & fldrName & linefeed & linefeed & body of n & linefeed
            end repeat
        end repeat
    end repeat
    return output
end tell'
```

## Notes
- Uses AppleScript via `osascript` — requires Accessibility permissions
- Notes body is HTML — strip tags for plain text
- iCloud is the default account name
- Folders are "Notes" by default