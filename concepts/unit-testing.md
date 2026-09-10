---
date: 2026-07-19
type: concept
title: Unit Testing
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/unit-testing
description: Write, run, and debug unit tests. Use this skill whenever the user needs
  to create test files, run pytest or unittest, write assertions, set up fixtures,
  mock dependencies, measure coverage, or fix failing tests. Covers pytest (preferred),
  unittest (stdlib), fixtures, parametrization, mocking, async tests, coverage reporting,
  and test organization by convention. Trigger on phrases like "write tests", "run
  pytest", "unit test this", "add test coverage", "test this function", "mock this",
  "test fixture", "pytest mark", "test is failing", "increase test coverage", "test-driven",
  "TDD", "integration test", "assert".
---

# Unit Testing

> Write, run, and debug unit tests. Use this skill whenever the user needs to create test files, run pytest or unittest, write assertions, set up fixtures, mock dependencies, measure coverage, or fix failing tests. Covers pytest (preferred), unittest (stdlib), fixtures, parametrization, mocking, async tests, coverage reporting, and test organization by convention. Trigger on phrases like "write tests", "run pytest", "unit test this", "add test coverage", "test this function", "mock this", "test fixture", "pytest mark", "test is failing", "increase test coverage", "test-driven", "TDD", "integration test", "assert".

## Overview

- **Project Convention** — This project uses: - **pytest** as the test runner - Tests in `tests/` directories alongside source - `conftest.py` for shared fixtures - Test files named `test_*.py`, functions named `test_*`
- **6. First Aid for Failing Tests** — | Symptom | Likely Cause | Fix | |---------|-------------|------| | `AssertionError` | Wrong expected value | Check actual output | | `ModuleNotFoundError` | Missing import | Fix import path | | `AttributeError` | Mock not set up | Check mock path matches import site | | `TimeoutError` | Test hangs | Add `@pytest.mark.timeout(10)` | | `FixtureNotFound` | Missing fixture | Add to conftest.py | | Flaky test | Shared state / ordering | Use fresh data per test |
- **7. Best Practices** — 1. **One assertion per test** where practical 2. **Descriptive names** — `test_cannot_delete_others_post` not `test_delete` 3. **Arrange-Act-Assert** — separate setup, execution, verification 4. **Test behavior, not implementation** — refactoring shouldn't break tests 5. **Mock external services** in unit tests; integration tests in CI 6. **Coverage target: 80%+** on business logic 7. **Order independence** — no shared mutable state between tests

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/unit-testing/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
