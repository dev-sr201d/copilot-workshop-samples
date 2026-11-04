import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
PLUGIN = ROOT / "plugin"
WORKSPACE_SKILL = ROOT / ".github" / "skills" / "add-endpoint"
PLUGIN_SKILL = PLUGIN / "skills" / "add-endpoint"


def run_plugin_script(
    name: str, *args: str, cwd: Path = ROOT
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PLUGIN_SKILL / "scripts" / name), *args],
        cwd=cwd,
        env={**os.environ, "PYTHONUTF8": "1"},
        capture_output=True,
        text=True,
        check=False,
    )


def test_manifest_declares_agent_plugins_schema() -> None:
    manifest = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    assert manifest["$schema"] == (
        "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    )
    assert manifest["name"] == "inventory-workshop"
    assert not (PLUGIN / "mcp.json").exists()


@pytest.mark.parametrize(
    "relative",
    [
        "com.github.copilot/agents/planner.agent.md",
        "com.github.copilot/agents/reviewer.agent.md",
        "skills/add-endpoint/templates/router_template.py",
    ],
)
def test_packaged_copy_matches_workspace(relative: str) -> None:
    source = (
        ROOT / ".github" / "agents" / Path(relative).name
        if "agents" in relative
        else WORKSPACE_SKILL / "templates" / Path(relative).name
    )
    assert (PLUGIN / relative).read_bytes() == source.read_bytes()


def test_skill_name_matches_folder() -> None:
    text = (PLUGIN_SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert text.startswith("---\nname: add-endpoint\n")


@pytest.mark.parametrize(
    ("script", "args"),
    [
        ("validate_endpoint.py", ("/health",)),
        (
            "check_openapi.py",
            ("/items", "--method", "POST", "--status", "201", "--field", "id"),
        ),
    ],
    ids=["route", "openapi"],
)
def test_plugin_scripts_find_repository_from_cwd(
    script: str, args: tuple[str, ...]
) -> None:
    result = run_plugin_script(script, *args, cwd=ROOT / "tests")
    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS" in result.stdout


def test_plugin_scripts_fail_outside_repository(tmp_path: Path) -> None:
    result = run_plugin_script("check_openapi.py", "/health", cwd=tmp_path)
    assert result.returncode == 1
    assert "inside the inventory API repository" in result.stderr
