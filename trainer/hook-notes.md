# Local formatter hook

Review `.github/hooks/format-after-edit.json` and `format_after_edit.py`.
The hook consumes **Local** snake_case `tool_name`/`tool_input` events, supports
the listed edit tools, and formats only their edited `.py` files inside the
repository. Read tools, non-Python files, hidden environments and outside paths
are ignored. The event's `cwd` is not trusted as the workspace root.
Unknown edit payloads and formatter failures are visible errors, not success.

Run:

```powershell
uv run pytest -c tests/pytest.ini tests/unit/test_format_hook.py tests/unit/test_skill_scripts.py
uv run python .github/skills/add-endpoint/scripts/check_openapi.py /items --method POST --status 201 --field id --field name
```

In Local, inspect the actual edit tool's arguments in the agent debug view. If
the build uses a different tool name or payload, adapt the narrow dispatch and
add a fixture test before the workshop. Do not silently run a repo-wide format
as a fallback: it would modify unrelated participant files.

Ask Agent to edit a Python file and inspect the formatter's diagnostic and diff.
CLI tests verify the script, not that VS Code discovered the hook.
Do not install a duplicate plugin hook. Hook code is ordinary trusted code that
can itself be changed; this formatter is not a security boundary.

The shared Copilot runtime uses a different documented event contract, e.g.
`postToolUse` / `toolName` / `toolArgs` and `timeoutSec`. This sample deliberately
uses the Local schema required by the workshop, not a purported universal hook.
See the
[Local reference](https://code.visualstudio.com/docs/agents/reference/hooks-reference)
and [migration guide](https://code.visualstudio.com/docs/agent-customization/migrate-customizations).
