# Shared working rules

Read [AGENTS.md](../AGENTS.md) for architecture, commands and teaching boundaries.
Keep changes limited to the requested behavior and its tests/documentation.
Do not silently repair deliberate baseline gaps.

* Inspect existing patterns before editing. Ask about ambiguous behavior.
* Preserve endpoint contracts outside the requested change.
* Use Pydantic for request validation and FastAPI HTTPException for new HTTP
  errors; keep validation errors as 422, not success-shaped JSON.
* Do not add a dependency when the existing stack suffices.
* Run the explicit pytest command and both ruff checks before reporting success.
  If a command cannot run, report that limitation rather than claiming it passed.
* Never commit credentials or enable MCP for these workshop exercises.
