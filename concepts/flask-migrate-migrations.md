---
date: 2026-08-02
type: concept
title: Flask Migrate Migrations
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/flask-migrate-migrations
description: Manage Flask-Migrate migrations for Flask/SQLAlchemy apps.
---

# Flask Migrate Migrations

> Manage Flask-Migrate migrations for Flask/SQLAlchemy apps.

## Overview

- **When to Use** — - You need to add, modify, or remove database columns/tables. - You are working with a Flask app that uses Flask-Migrate for migrations (e.g., Dify API). - You want to version-control your database schema and apply changes consistently across environments.
- **Pitfalls** — - **Duplicate column definitions**: If you manually add a column in the model but forget to generate a migration, or generate a migration that adds a column that already exists, you will get errors on upgrade. Always check the generated migration script. - **Forgotten virtual environment**: Running `flask` outside the venv will use a different Flask-Migrate version or fail. Always activate the venv first. - **Multiple heads**: If you see multiple heads after `flask db heads`, you may need to merge heads with `flask db merge` before creating a new migration. - **Downgrades**: To roll back, use
- **Verification** — After running `flask db upgrade`, the output should indicate the migration was applied successfully. You can also check the database schema directly (e.g., using `\d tablename` in psql) to confirm columns were added.

## Further detail

### References

- Flask-Migrate documentation: https://flask-migrate.readthedocs.io/ - Alembic documentation: https://alembic.sqlalchemy.org/

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/flask-migrate-migrations/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
