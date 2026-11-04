# Workshop Inventory Constitution

Curated workshop example, not the output of a live /speckit-constitution run.

## Core principles

### I. Explicit public contracts

Specify request parsing, response shape, status codes and boundary behavior
before implementation. Preserve all unrelated endpoint contracts. Document
intentional changes and teaching gaps instead of silently repairing them.

### II. Verifiable delivery

Every feature must have isolated HTTP tests for its acceptance criteria and
regressions. A completion claim requires the actual pytest and ruff results;
plans and generated artifacts are not test execution evidence.

### III. Small, local architecture

Use the existing FastAPI/Pydantic stack and per-application ItemStore. No new
dependency, persistent storage, external service, MCP or deployment is allowed
without an explicit change to workshop scope.

### IV. Safe, reviewable workflow

Use personal branches and review diffs. Preserve participant work. Keep normal
terminal approvals, never commit credentials, and treat hooks as trusted code
that must be inspected. Instructions are not a security boundary.

### V. Python compatibility and clarity

Keep Python 3.11+ compatibility, typed new functions and existing repository
patterns. Put HTTP parsing in routers, state operations in the store and
request/response validation in Pydantic models.

## Quality gates

From the repository root, run `uv run pytest -c tests/pytest.ini`,
`uv run ruff check .` and `uv run ruff format --check .`. New query parameters
must appear in OpenAPI. Report failures or unavailable checks explicitly.

## Governance

This constitution governs new feature decisions; AGENTS.md supplies operational
commands and architecture. Amendments require a rationale, version change and
review of affected specs/tests. The unresolved baseline gaps remain out of
scope unless a feature explicitly addresses them.

**Version**: 1.0.0 | **Ratified**: 2026-11-04 | **Last Amended**: 2026-11-04
