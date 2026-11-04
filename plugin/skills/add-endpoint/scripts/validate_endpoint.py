import argparse
import json
import sys
from pathlib import Path


def find_root() -> Path:
    # Installed plugins live outside the repository, so search from the terminal cwd.
    for candidate in (Path.cwd(), *Path.cwd().parents):
        if (candidate / "src" / "inventory" / "main.py").is_file():
            return candidate
    raise SystemExit("Run this script from inside the inventory API repository.")


ROOT = find_root()
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402

from inventory.main import create_app  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test a local inventory route.")
    parser.add_argument("path")
    parser.add_argument(
        "--method", choices=["GET", "POST", "PUT", "PATCH", "DELETE"], default="GET"
    )
    parser.add_argument("--status", type=int, default=200)
    parser.add_argument("--body", type=json.loads)
    args = parser.parse_args()
    if not args.path.startswith("/") or args.path.startswith("//"):
        parser.error("path must be an application-relative route beginning with /")
    with TestClient(create_app()) as client:
        response = client.request(args.method, args.path, json=args.body)
    if response.status_code != args.status:
        print(
            f"FAIL {args.method} {args.path}: expected {args.status}, "
            f"got {response.status_code}; {response.text}",
            file=sys.stderr,
        )
        return 1
    print(f"PASS {args.method} {args.path}: {response.status_code}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
