# Research: low-stock filtering

Prepared evidence, not a live researcher transcript.

## User problem

Warehouse staff need to find items at or below a restocking threshold without
fetching and filtering the entire inventory themselves.

## Repository evidence

* `src/inventory/main.py:create_app` supplies one ItemStore per application.
* `src/inventory/routers/items.py:list_items` exposes GET /items with list[Item].
* `src/inventory/store.py:ItemStore` keeps insertion order in a dict.
* `src/inventory/models.py:Item.quantity` is an integer; baseline create validation
  is intentionally unfinished and is outside this feature.
* `tests/unit/conftest.py:client` isolates state per test.
* `tests/pytest.ini` is necessary for the supported import/test configuration.

## Options

1. A separate /items/low-stock route: extra API surface for a simple filter.
2. Optional max_quantity query on GET /items: preserves default behavior,
   documents validation in OpenAPI and composes with future filters.

Choose option 2. Use FastAPI Query(ge=0); inclusive comparison in the store.
No external research, MCP, new dependency or persistence is needed.
