import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / ".github" / "skills" / "add-endpoint" / "scripts"


def run_script(name: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *args],
        cwd=ROOT,
        env={**os.environ, "PYTHONUTF8": "1"},
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize(
    ("args", "expected_code"),
    [
        (("/health",), 0),
        (("/missing",), 1),
        (("/health", "--method", "POST"), 1),
        (("/health", "--status", "201"), 1),
        (
            (
                "/items",
                "--method",
                "POST",
                "--status",
                "201",
                "--body",
                '{"name":"Pen"}',
            ),
            0,
        ),
        (("https://example.invalid",), 2),
        (("/items", "--body", "not-json"), 2),
    ],
    ids=["health", "missing", "method", "status", "create", "external-url", "bad-json"],
)
def test_route_smoke_check(args: tuple[str, ...], expected_code: int) -> None:
    result = run_script("validate_endpoint.py", *args)
    assert result.returncode == expected_code, result.stdout + result.stderr
    if expected_code == 0:
        assert "PASS" in result.stdout
    else:
        assert result.stderr


@pytest.mark.parametrize(
    ("args", "expected_code"),
    [
        (("/health",), 0),
        (("/missing",), 1),
        (("/health", "--method", "POST"), 1),
        (("/health", "--status", "201"), 1),
        (("/items", "--method", "POST", "--status", "201", "--field", "id"), 0),
        (("/items", "--method", "POST", "--status", "201", "--field", "missing"), 1),
        (("/items/{item_id}", "--method", "DELETE", "--status", "204"), 0),
    ],
    ids=[
        "health",
        "missing",
        "method",
        "status",
        "schema",
        "missing-field",
        "no-content",
    ],
)
def test_openapi_check(args: tuple[str, ...], expected_code: int) -> None:
    result = run_script("check_openapi.py", *args)
    assert result.returncode == expected_code, result.stdout + result.stderr
    if expected_code == 0:
        assert "PASS OpenAPI" in result.stdout
    else:
        assert "FAIL" in result.stderr
