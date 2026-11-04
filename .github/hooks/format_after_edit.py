import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

EDIT_TOOLS = {
    "apply_patch",
    "create_file",
    "insert_edit_into_file",
    "replace_string_in_file",
    "multi_replace_string_in_file",
}


def edited_paths(event: dict[str, Any]) -> list[str]:
    tool = event.get("tool_name")
    if not isinstance(tool, str):
        raise ValueError("Expected a Local hook event with tool_name.")
    if tool not in EDIT_TOOLS:
        return []
    arguments = event.get("tool_input")
    if not isinstance(arguments, dict):
        raise ValueError("An edit event must contain a tool_input object.")
    if tool == "apply_patch":
        patch = arguments.get("input", arguments.get("patch"))
        if not isinstance(patch, str):
            raise ValueError("apply_patch must provide an input or patch string.")
        return re.findall(
            r"^\*\*\* (?:Add File|Update File|Move to): (.+)$", patch, re.MULTILINE
        )
    edits = arguments.get("replacements", [arguments])
    if not isinstance(edits, list) or not edits:
        raise ValueError("Expected one edit or a nonempty replacements list.")
    paths = []
    for edit in edits:
        if not isinstance(edit, dict):
            raise ValueError("Each replacement must be an object.")
        path = edit.get("filePath", edit.get("file_path"))
        if not isinstance(path, str):
            raise ValueError("Each edit must identify filePath or file_path.")
        paths.append(path)
    return paths


def format_event(event: dict[str, Any], root: Path) -> int:
    root = root.resolve()
    targets: set[Path] = set()
    for raw_path in edited_paths(event):
        path = (root / raw_path).resolve()
        if not path.is_relative_to(root) or path.suffix != ".py":
            continue
        relative = path.relative_to(root)
        if any(part.startswith(".") for part in relative.parts if part != ".github"):
            continue
        if not path.is_file():
            raise FileNotFoundError(f"Edited Python file does not exist: {path}")
        targets.add(path)
    if not targets:
        print("{}")
        return 0
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "format", *map(str, sorted(targets))],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.stdout:
        print(result.stdout.strip(), file=sys.stderr)
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    if result.returncode:
        print("Formatter hook failed; inspect the edited file.", file=sys.stderr)
        return result.returncode
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": f"ruff format checked {len(targets)} edited "
                    "Python file(s).",
                }
            }
        )
    )
    return 0


def main() -> int:
    event = json.load(sys.stdin)
    if not isinstance(event, dict):
        raise ValueError("Hook stdin must be a JSON object.")
    return format_event(event, Path(__file__).resolve().parents[2])


if __name__ == "__main__":
    raise SystemExit(main())
