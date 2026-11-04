# Implementation plan: inventory name search

## Technical context

Python 3.11+, FastAPI/Pydantic, per-app in-memory ItemStore; pytest, httpx and
ruff via the existing uv lock. Extend GET /items, not a separate search service.

## Constitution check

* Explicit contract: spec FR-001 through FR-007 covers query semantics.
* Evidence: HTTP tests plus existing regressions and OpenAPI inspection.
* Minimal architecture: no new files in production beyond existing router/store.
* Reviewable: scoped change from m3-complete; all baseline gaps remain out of scope.
* Compatibility: unfiltered GET /items, Item shape and insertion order preserved.

## Implementation

1. Write parameterized HTTP tests in `tests/unit/test_item_search.py` from the
   specification, including blank queries and Unicode casefold.
2. Extend ItemStore.list with optional name. Compute the normalized query once,
   filter without mutating items or changing iteration order.
3. Add the optional string Query parameter in list_items; forward it by keyword.
   Document whitespace and case-insensitive semantics.
4. Run targeted tests, full pytest and both ruff checks. Inspect the OpenAPI
   contract and compare every test group with its FR requirement.

## Dependencies and non-goals

Build on m3-complete. Independent of the HVE low-stock checkpoint. No new
package, database, index, endpoint, authentication, deployment or MCP.

## Verification commands

`uv run pytest -c tests/pytest.ini tests/unit/test_item_search.py`

`uv run pytest -c tests/pytest.ini`

`uv run ruff check .`

`uv run ruff format --check .`
