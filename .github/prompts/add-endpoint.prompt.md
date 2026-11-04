---
description: "Add one FastAPI endpoint with tests and an OpenAPI response contract."
agent: agent
argument-hint: "Describe the method, path, purpose and response shape."
---

Add the endpoint described in the user's message. If method, path, status,
response shape or invalid-input behavior is missing, clarify before editing.

Read [the contributor guide](../../AGENTS.md) and existing routers. Reuse models
and dependencies. Register the router in create_app, add isolated tests, and
preserve unrelated contracts. Do not add a dependency.

Run `uv run pytest -c tests/pytest.ini`, `uv run ruff check .` and
`uv run ruff format --check .`. Report changed files and exact results.
This prompt is a Local-only shortcut; the add-endpoint skill works in both
harnesses.
