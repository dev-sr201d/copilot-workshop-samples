# Example rewrites (open after attempting the exercise)

## 1. Input validation

**Goal:** Reject invalid item input before it reaches storage.

**Context:** Read `src/inventory/models.py`, `src/inventory/routers/items.py`
and `tests/unit/test_items.py`. Use FastAPI's existing Pydantic error handling.

**Constraints:** Use Pydantic only. Trim names and require 1-80 characters
after trimming. Quantity must be an integer >= 0; keep its default of 1.
Do not redesign the store or change other endpoint contracts. Ask if a
requirement is ambiguous.

**Done when:** POST /items returns 201 for ordinary valid input, a trimmed
name, zero quantity and omitted quantity; it returns 422 with a field message
for empty/whitespace/81-character names and negative quantity. Add parameterized
tests for each boundary and confirm rejected input was not stored. Run
`uv run pytest -c tests/pytest.ini`, `uv run ruff check .` and
`uv run ruff format --check .`. Report changed files and exact results.

## 2. Add an endpoint

**Goal:** Let a client discover this running API's version.

**Context:** Read `src/inventory/main.py` and the health router for the
registration/response pattern. `create_app()` already defines `app.version`.

**Constraints:** Add GET /version in its own router, registered by `create_app`.
Return `{"version": "<app.version>"}` with HTTP 200 and a documented Pydantic
response model. Read the version from the current app instance, not a second
hard-coded constant. No new dependency or storage changes; preserve every
existing endpoint. Ask if ambiguity remains.

**Done when:** Tests cover status, exact JSON shape, a custom app.version value,
and GET /version's 200 response schema in OpenAPI. All existing tests pass.
Run the same pytest and ruff commands as above. Summarize changed files,
test results and any decisions.
