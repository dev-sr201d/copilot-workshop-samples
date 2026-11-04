# Plan: low-stock filtering

Curated plan for the workshop; user review would precede a real implementation.

## Acceptance criteria

* GET /items without a filter is unchanged.
* max_quantity is an optional integer >= 0; invalid values return 422.
* Include items with quantity <= threshold, including zero and equality.
* Return [] when no items match; preserve insertion order and stored state.
* Other routes and their known baseline behavior remain unchanged.

## Steps

1. Extend ItemStore.list with an optional max_quantity argument; do not mutate.
2. Parse/validate the optional query parameter in list_items and pass it through.
3. Add parameterized API tests for omitted/zero/equality/all/invalid thresholds,
   empty stores, no matches, non-mutation and OpenAPI's documented minimum.
4. Run pytest and ruff, inspect the diff against m3-complete, and review criteria.

## Test strategy and risks

`tests/unit/test_low_stock.py` exercises behavior through HTTP, including insertion
order. Existing tests protect create/get/list and customization helpers. Negative
stored quantities are still possible due to the intentionally incomplete create
validation; this feature does not silently change that contract.

Commands: `uv run pytest -c tests/pytest.ini`, `uv run ruff check .`,
`uv run ruff format --check .`. These are planned commands, not claimed execution.
