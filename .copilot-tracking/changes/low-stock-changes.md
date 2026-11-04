# Implementation record: low-stock filtering

Prepared implementation, not a transcript of an HVE agent run.

* `src/inventory/routers/items.py`: optional annotated query, ge=0 validation.
* `src/inventory/store.py`: inclusive, non-mutating optional filter.
* `tests/unit/test_low_stock.py`: acceptance and regression tests.

Reproduce verification from the repository root:

```powershell
uv run pytest -c tests/pytest.ini
uv run ruff check .
uv run ruff format --check .
```

Inspect the feature-only difference with
`git diff m3-complete..m4-hve -- src tests/unit/test_low_stock.py`.
Do not treat this Markdown document as evidence that a command ran locally.
