---
description: "Use when changing Python models, routers, storage or scripts."
applyTo: "**/*.py"
---

# Python conventions

Target Python 3.11+. Add parameter and return annotations to new functions.
Use built-in collection types and `X | None`. Use explicit imports.
Keep HTTP decisions in routers, validation in Pydantic models and storage in
ItemStore. Prefer the existing Annotated dependencies. Avoid unrelated refactors.
Surface errors; do not catch Exception or return success on a failed operation.
Use ruff's configured formatting and lint rules.
