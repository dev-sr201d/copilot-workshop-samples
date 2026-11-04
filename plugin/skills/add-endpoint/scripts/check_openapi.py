import argparse
import sys
from pathlib import Path
from typing import Any


def find_root() -> Path:
    # Installed plugins live outside the repository, so search from the terminal cwd.
    for candidate in (Path.cwd(), *Path.cwd().parents):
        if (candidate / "src" / "inventory" / "main.py").is_file():
            return candidate
    raise SystemExit("Run this script from inside the inventory API repository.")


ROOT = find_root()
sys.path.insert(0, str(ROOT / "src"))

from inventory.main import create_app  # noqa: E402


def check_operation(
    schema: dict[str, Any],
    path: str,
    method: str,
    status: int,
    fields: list[str],
) -> list[str]:
    operation = schema["paths"].get(path, {}).get(method.lower())
    if operation is None:
        return [f"{method} {path} is not documented"]
    response = operation.get("responses", {}).get(str(status))
    if response is None:
        return [f"{method} {path} does not document HTTP {status}"]
    if not fields:
        return []
    model = response.get("content", {}).get("application/json", {}).get("schema", {})
    if "$ref" in model:
        reference = model["$ref"]
        if not reference.startswith("#/components/schemas/"):
            return [f"Unsupported response schema reference: {reference}"]
        model = schema["components"]["schemas"][reference.rsplit("/", 1)[-1]]
    properties = model.get("properties", {})
    return [
        f"Response schema has no field {field!r}"
        for field in fields
        if field not in properties
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the local OpenAPI contract.")
    parser.add_argument("path")
    parser.add_argument(
        "--method", choices=["GET", "POST", "PUT", "PATCH", "DELETE"], default="GET"
    )
    parser.add_argument("--status", type=int, default=200)
    parser.add_argument("--field", action="append", default=[])
    args = parser.parse_args()
    errors = check_operation(
        create_app().openapi(), args.path, args.method, args.status, args.field
    )
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    print(f"PASS OpenAPI {args.method} {args.path}: HTTP {args.status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
