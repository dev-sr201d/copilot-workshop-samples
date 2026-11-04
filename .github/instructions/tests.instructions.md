---
description: "Use when writing or reviewing pytest tests for the inventory API."
applyTo: "tests/**/*.py"
---

# Pytest conventions

Run `uv run pytest -c tests/pytest.ini` from the repository root.
Use the `client` fixture in `tests/unit/conftest.py`; it creates a fresh app
per test. Never import the global server app to share mutable state.
Type new generator fixtures with `Iterator[TestClient]`.

Name tests `test_<observable_behavior>`. Assert the HTTP status before the body,
then verify the relevant JSON contract. Parameterize boundary cases with clear
IDs. For a new endpoint, cover success, invalid input and documented OpenAPI
response where relevant. Include empty results and missing resources when
applicable. Do not depend on test ordering, network access or fixed filesystem
paths. Test rejected mutations leave storage unchanged.
