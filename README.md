# GitHub Copilot workshop samples

One small Python inventory API, customized step by step. Use **Local** for all
labs. Only the Module 1 harness demo uses Copilot. No sample requires MCP, cloud
credentials, a database, or an external service.

## Before the workshop

Install Git, Python 3.11+, and [uv](https://docs.astral.sh/uv/). Open this folder
as the VS Code workspace (not its parent). Sign into GitHub Copilot and check
that your preconfigured Foundry model supports tool calling.

```powershell
uv sync --locked
uv run pytest -c tests/pytest.ini
uv run ruff check .
uv run ruff format --check .
uv run uvicorn inventory.main:app --app-dir src --reload
```

Open <http://127.0.0.1:8000/docs> for interactive API documentation.
Stop the server with Ctrl+C before changing checkpoints.

Dependencies come from public PyPI (`pypi.org` and `files.pythonhosted.org`).
`uv.lock` pins exact versions and sha256 hashes, and no feed credentials are
stored. If your network blocks public PyPI, ask the trainer; do not change the
index and commit a regenerated lockfile.

The explicit pytest config is intentional: it supplies the `src` import path
and test location. Plain `pytest` is not the supported workshop command.
All application data is **in memory**, isolated per application instance and
lost on restart. This is a local teaching app, not a production service.

## Checkpoints

Checkpoints are read-only Git branches. In your clone they exist as
`origin/<branch>`; never commit to them. If publishing this repository, push
all branches, not just the current branch.

| Branch | Builds on | Prepared result |
|---|---|---|
| `start` | | Working API, intentionally no agent customizations |
| `m2-prompting` | `start` | Module 2 starting point (same code as `start`) |
| `m3-instructions` | `m2-prompting` | Lab 3A: repository and file-based instructions |
| `m3-skills` | `m3-instructions` | Add-endpoint prompt, skill, template and route validator |
| `m3-agents` | `m3-skills` | Lab 3B: read-only planner/reviewer and implementation handoff |
| `m3-complete` | `m3-agents` | Lab 3C: formatter hook, OpenAPI checker and optional plugin |
| `m4-hve` | `m3-complete` | Module 4 trainer fallback (HVE Core) |
| `m5-speckit` | `m3-complete` | Module 5 trainer fallback (Spec Kit) |

Work on a personal branch created from a checkpoint and commit with `git add -A`
before switching. Never use a hard reset or forced checkout to follow the
workshop. The Git workflow card from your trainer has the commands for each lab.

```powershell
git switch -c my-work origin/m2-prompting
```

For an independent comparison, use a second clean worktree:

```powershell
git worktree add ..\workshop-comparison -b my-comparison origin/m2-prompting
```

In the original repository without a remote, drop the `origin/` prefix.

Run `uv sync --locked` in each worktree. Stop any running server first; existing
Python processes do not reload modules just because Git changed branches.

## Workshop materials

Lab instructions and handouts come from your trainer and are deliberately not
part of this repository's checkpoints. Keep them out of this folder: agents
read every file in the open workspace.

Preview UI labels, hook schemas and kit commands can change; rehearse with the
workshop VS Code build.
