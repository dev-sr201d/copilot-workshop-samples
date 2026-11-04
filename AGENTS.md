# Inventory API contributor guide

## Setup and checks

Run commands from this repository root:

```powershell
uv sync --locked
uv run pytest -c tests/pytest.ini
uv run ruff check .
uv run ruff format --check .
uv run uvicorn inventory.main:app --app-dir src --reload
```

`tests/pytest.ini` supplies the source path and test directory. Do not replace
the explicit test command with plain pytest. Dependencies come from public PyPI
and are declared in `pyproject.toml`; commit `uv.lock` with dependency
changes. Python 3.11 is the minimum.

## Architecture

* `src/inventory/main.py`: application factory and router registration.
* `src/inventory/models.py`: Pydantic request/response models.
* `src/inventory/routers/`: HTTP parsing, status codes, response contracts.
* `src/inventory/store.py`: per-application, in-memory item storage.
* `tests/unit/`: isolated FastAPI TestClient tests using the factory fixture.

Use the request's `app.state.store` dependency, not a module-global store.
Register new routers in `create_app()` so test-created apps get the same routes.
The global `app` exists only as the server entry point.

## Teaching boundaries

This repository deliberately has incomplete input validation, inconsistent 404
envelopes and missing tests. Fix a gap only when the task requests it. Preserve
other public behavior, including default quantity 1 and insertion order.
The intended convention for new not-found responses is HTTPException with
`detail="Item not found"`; the old GET envelope remains until explicitly fixed.
Do not add persistence, authentication, deployment or external services.
