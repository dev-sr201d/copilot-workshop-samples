# Prepared Spec Kit fallback

Specify CLI **1.2.3** actually generated this checkpoint's `.specify/` and
`speckit-*` skills with:

```powershell
uv tool run --from specify-cli specify init --here --integration copilot --script ps --non-interactive --force
```

Behind a network that blocks public PyPI, add `--index-url <approved-pypi-mirror>`.

The constitution, feature documents and code are curated workshop examples,
**not** a transcript of live slash-command execution. The installed skill
resources remain the CLI-generated versions.

Read [specification](spec.md), [plan](plan.md), [tasks](tasks.md),
[research](research.md), [data model](data-model.md),
[contract](contracts/items.md), [quickstart](quickstart.md) and
[requirements checklist](checklists/requirements.md). Tasks describe the
already implemented result; start a new personal branch from `m3-complete` for
live constitution/specify work.

## Resolve the prepared feature

The workshop checkpoint name is not a feature ID. For prerequisite scripts or
follow-up skills on this branch, set the explicit feature directory in the
terminal the agent will use:

```powershell
$env:SPECIFY_FEATURE = "001-item-search"
$env:SPECIFY_FEATURE_DIRECTORY = "specs\001-item-search"
.\.specify\scripts\powershell\check-prerequisites.ps1 -Json -RequireSpec -RequireTasks -IncludeTasks
```

Tell the agent these values as well; terminals/sessions may not share environment
variables. `.specify/feature.json` is ignored runtime state, not a required
committed machine-specific path. Do not initialize again on this branch.
