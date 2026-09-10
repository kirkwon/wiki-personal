---
date: 2026-07-19
type: concept
title: Blogwatcher
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- RSS
- Blogs
- Feed-Reader
- Monitoring
- research
sources:
- hermes://skill/blogwatcher
description: Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.
---

# Blogwatcher

> Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.

## Overview

- **Installation** — Pick one method:
- **Environment Variables** — All flags can be set via environment variables with the `BLOGWATCHER_` prefix:
- **Notes** — - Auto-discovers RSS/Atom feeds from blog homepages when no `--feed-url` is provided. - Falls back to HTML scraping if RSS fails and `--scrape-selector` is configured. - Categories from RSS/Atom feeds are stored and can be used to filter articles. - Import blogs in bulk from OPML files exported by Feedly, Inoreader, NewsBlur, etc. - Database stored at `~/.blogwatcher-cli/blogwatcher-cli.db` by default (override with `--db` or `BLOGWATCHER_DB`). - Use `blogwatcher-cli <command> --help` to discover all flags and options.

## Further detail

### Google Workspace Integration

After running `blogwatcher-cli scan` and collecting new unread articles, deliver a digest of new items via Gmail. This is especially useful for cron-triggered scans where the results need to reach the inbox. Use the shared helper library:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/blogwatcher/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
