# Try the prepared search feature

```powershell
uv sync --locked
uv run pytest -c tests/pytest.ini
uv run ruff check .
uv run ruff format --check .
uv run uvicorn inventory.main:app --app-dir src --reload
```

Use <http://127.0.0.1:8000/docs> to create Blue Pen quantity 2 and Pencil quantity
5. GET /items with name=pen returns both. Use name=cil to get Pencil only.
Use a query surrounded by spaces to verify trimming. Query for an unmatched
name to get []. Restarting the process clears all data.

For in-process contract checks:

```powershell
uv run python .github/skills/add-endpoint/scripts/check_openapi.py /items
uv run python .github/skills/add-endpoint/scripts/validate_endpoint.py /items
```

These script invocations each create a fresh, empty application; they do not
inspect the running server's data. See README.md in this directory to select
the feature context for generated Spec Kit scripts.
