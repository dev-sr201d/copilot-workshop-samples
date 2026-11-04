---
name: add-endpoint
description: "Use when adding a FastAPI API endpoint or route to the inventory service, including its response model, router registration, tests and validation."
argument-hint: "HTTP method, path, response shape and expected status."
---

# Add one endpoint

1. Read AGENTS.md, the application factory and the nearest existing router.
   Clarify method, path, request/response contract and failure behavior.
2. Plan the smallest change. Use [the router template](./templates/router_template.py)
   as a starting pattern, not a generator to copy without adaptation.
3. Add a typed Pydantic response model and handler; register the router in
   create_app. Use existing dependency patterns and no new service.
4. Add TestClient tests with per-test app isolation. Cover status and JSON shape,
   boundaries/invalid input where relevant, and OpenAPI documentation.
5. Run the route smoke check (replace /health, method, status and JSON as needed):
   `uv run python .github/skills/add-endpoint/scripts/validate_endpoint.py /health`.
   Use `--method POST --status 201 --body '{"name":"Pen","quantity":2}'` for
   a POST example; shell quoting differs, so prefer a terminal with known quoting.
6. Run the exact pytest and both ruff checks from AGENTS.md. Report results and
   changed files; do not claim a failed script succeeded.

The script imports the local application and uses an in-process TestClient:
no server, external API, authentication or MCP is required. Each invocation
starts with empty storage. For the OpenAPI contract extension, see Lab 3C.
