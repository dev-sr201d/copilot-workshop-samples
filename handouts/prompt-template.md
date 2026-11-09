# Prompt template card

```text
Goal:        What should change and why?
Context:     Relevant files, patterns, background.
Constraints: Libraries, scope limits, what not to touch.
Done when:   Observable behavior, tests, expected output.
```

## Worked example

**Goal:** Reject invalid items so bad data never reaches storage.

**Context:** Read `src/inventory/models.py`, `src/inventory/routers/items.py`
and `tests/unit/test_items.py`. Follow FastAPI's Pydantic error responses.

**Constraints:** Use Pydantic validation only. Trim names; require 1-80 characters
after trimming and integer quantity >= 0. Keep quantity's default of 1.
Do not change other endpoints, add dependencies, or redesign storage.

**Done when:** Valid input returns 201, invalid input returns 422 with a field
message, and tests cover empty/whitespace/too-long names, negative quantity,
zero quantity, omitted quantity and ordinary valid input. Run
`uv run pytest -c tests/pytest.ini`, `uv run ruff check .` and
`uv run ruff format --check .`. Summarize changed files and results.

Start a fresh chat for each comparison. Use the same model, branch and acceptance
criteria. Review the diff, not just the final message. Variance is expected:
structured prompting improves predictability, not guaranteed superiority.
