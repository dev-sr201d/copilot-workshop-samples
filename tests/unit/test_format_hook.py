import json
import runpy
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
HOOK = ROOT / ".github" / "hooks" / "format_after_edit.py"
FORMAT_EVENT = runpy.run_path(str(HOOK))["format_event"]


def test_hook_formats_only_edited_python_file(tmp_path: Path) -> None:
    edited = tmp_path / "edited.py"
    unrelated = tmp_path / "unrelated.py"
    edited.write_text("answer= 42\n", encoding="utf-8")
    unrelated.write_text("other= 7\n", encoding="utf-8")
    code = FORMAT_EVENT(
        {"tool_name": "create_file", "tool_input": {"filePath": str(edited)}},
        tmp_path,
    )
    assert code == 0
    assert edited.read_text(encoding="utf-8") == "answer = 42\n"
    assert unrelated.read_text(encoding="utf-8") == "other= 7\n"


def test_hook_ignores_read_calls(tmp_path: Path) -> None:
    edited = tmp_path / "edited.py"
    edited.write_text("answer= 42\n", encoding="utf-8")
    assert (
        FORMAT_EVENT(
            {"tool_name": "read_file", "tool_input": {"filePath": str(edited)}},
            tmp_path,
        )
        == 0
    )
    assert edited.read_text(encoding="utf-8") == "answer= 42\n"


def test_hook_does_not_format_outside_workspace(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    outside = tmp_path / "outside.py"
    outside.write_text("answer= 42\n", encoding="utf-8")
    assert (
        FORMAT_EVENT(
            {"tool_name": "create_file", "tool_input": {"filePath": str(outside)}},
            workspace,
        )
        == 0
    )
    assert outside.read_text(encoding="utf-8") == "answer= 42\n"


@pytest.mark.parametrize("tool", ["apply_patch", "multi_replace_string_in_file"])
def test_hook_supports_batch_edits(tool: str, tmp_path: Path) -> None:
    edited = tmp_path / "edited.py"
    edited.write_text("answer= 42\n", encoding="utf-8")
    arguments = (
        {"input": "*** Begin Patch\n*** Update File: edited.py\n*** End Patch"}
        if tool == "apply_patch"
        else {"replacements": [{"filePath": str(edited)}]}
    )
    assert FORMAT_EVENT({"tool_name": tool, "tool_input": arguments}, tmp_path) == 0
    assert edited.read_text(encoding="utf-8") == "answer = 42\n"


def test_hook_formatter_failure_is_nonzero(tmp_path: Path) -> None:
    edited = tmp_path / "broken.py"
    edited.write_text("def (\n", encoding="utf-8")
    assert (
        FORMAT_EVENT(
            {"tool_name": "create_file", "tool_input": {"filePath": str(edited)}},
            tmp_path,
        )
        != 0
    )


def test_hook_rejects_malformed_edit_payload(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="filePath"):
        FORMAT_EVENT({"tool_name": "create_file", "tool_input": {}}, tmp_path)


def test_hook_stdin_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps({"tool_name": "read_file", "tool_input": {}}),
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == {}


def test_hook_formats_moved_patch_destination(tmp_path: Path) -> None:
    moved = tmp_path / "moved.py"
    moved.write_text("answer= 42\n", encoding="utf-8")
    event = {
        "tool_name": "apply_patch",
        "tool_input": {
            "input": "*** Begin Patch\n*** Update File: old.py\n"
            "*** Move to: moved.py\n*** End Patch"
        },
    }
    assert FORMAT_EVENT(event, tmp_path) == 0
    assert moved.read_text(encoding="utf-8") == "answer = 42\n"


def test_hook_does_not_format_hidden_environments(tmp_path: Path) -> None:
    environment = tmp_path / ".venv"
    environment.mkdir()
    edited = environment / "package.py"
    edited.write_text("answer= 42\n", encoding="utf-8")
    assert (
        FORMAT_EVENT(
            {"tool_name": "create_file", "tool_input": {"filePath": str(edited)}},
            tmp_path,
        )
        == 0
    )
    assert edited.read_text(encoding="utf-8") == "answer= 42\n"


def test_hook_rejects_malformed_stdin() -> None:
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        input="not-json",
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "JSONDecodeError" in result.stderr
