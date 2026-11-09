# Trainer runbook

## Before delivery

* Open the samples folder itself. Run `uv sync --locked`, pytest and both ruff
  checks from the README. Check Python 3.11+ on participant machines.
* Participants install from public PyPI. On a network that blocks
  `files.pythonhosted.org`, see
  [Install through an approved mirror](#install-through-an-approved-mirror).
* Publish all eight checkpoint branches and the `materials` branch if
  distributing by Git. This local repository has no remote configured. Do not
  promise a clone URL until hosted. Participant commands use `origin/<branch>`;
  see the [Git workflow card](../handouts/git-workflow.md).
* Share the materials as a GitHub link or printout, never as files inside the
  lab folder. See [Keep answers out of the workspace](#keep-answers-out-of-the-workspace).
* Rehearse UI labels and all customization types in the exact VS Code build.
  Check Local tools, references, hook logs, Foundry models and tool calling.
* Verify HVE plugin and Specify CLI versions. Network-dependent installs are
  separate from the offline Python samples; use approved feeds if required.
* Record backup videos yourself: these samples contain text/code fallbacks, not
  recordings of an agent interaction.
* Prepare clean personal branches/worktrees per demo. Never reset participant
  work to recover a failed demo.

## Keep answers out of the workspace

Agents search the whole open folder before acting, even with fast models.
When the handouts, exercises and this runbook were on the checkpoint branches,
the vague Module 2 prompt found the worked example, the answer card and the
documented validation gap, and produced the structured result. The Module 1
Plan demo likewise found its prompt on the lab card.

The checkpoint branches therefore contain only the application, tests, the
cumulative customizations each lab produces, and a setup README. Lab prompts,
answers, acceptance criteria and known gaps stay on `materials`. Customizations
such as `AGENTS.md` from Lab 3A onward are intended context. Before a delivery,
check that the participant starting points contain no materials:

```powershell
foreach ($b in 'start','m2-prompting','m3-complete') {
  git ls-tree -r --name-only $b | Select-String '^(handouts|exercises|trainer)/'
}
```

No output means clean. Run the demos with only the samples folder open,
not a multi-root workspace that includes the materials worktree.

## Install through an approved mirror

If a network blocks the public file host, `uv sync --locked` fails, typically
with a TLS handshake error. Install the identical locked files from your
organization's approved PyPI mirror instead. The exported requirements carry
the lock's sha256 hashes, so `uv pip sync` rejects any file that differs.
Run once per clone or worktree:

```powershell
uv export --locked --no-emit-project --format requirements.txt -o "$env:TEMP\workshop-requirements.txt"
uv venv
uv pip sync "$env:TEMP\workshop-requirements.txt" --index-url <approved-pypi-mirror>
```

Afterwards `uv sync --locked` finds every package already installed and the
README commands work unchanged. For Spec Kit, add
`--index-url <approved-pypi-mirror>` to `uv tool install specify-cli`.
Never commit a lockfile regenerated against a private mirror: participants
on other networks cannot rely on it.

## Timing and branch map

| Time | Demo / lab | Checkpoint |
|---|---|---|
| 0:10 | Ask -> Plan -> implement description field; models | `start` |
| 0:40 | Vague / structured input validation and two prompt rewrites | `m2-prompting` |
| 1:20 | Lab 3A instructions | `m3-instructions` solution |
| 1:45 | Prompt -> add-endpoint skill | `m3-skills` solution |
| 2:00 | Lab 3B plan, handoff, review | `m3-agents` solution |
| 2:15 | Lab 3C formatter hook and OpenAPI check | `m3-complete` solution |
| 2:55 | HVE RPI low-stock filter | `m4-hve` fallback |
| 3:25 | Spec Kit name search | `m5-speckit` fallback |
| 3:50 | Compare approaches and wrap up | Handouts |

Use the detailed lab card for exact prompts and acceptance criteria.
Module 3's five-minute buffer is catch-up time; skip optional packaging first.
`m4-hve` and `m5-speckit` both build on `m3-complete` and are independent:
the Spec Kit branch contains no HVE artifacts or low-stock filter.
Before Lab 3B, make sure everyone has run the skill sync from the Git card.

## Known baseline observations

* `POST /items` accepts `{"name": " ", "quantity": -1}`: intentional validation gap.
* `GET /items/999` returns `{"error": "Item not found"}`.
* `DELETE /items/999` returns `{"detail": "Item not found"}`.
* Baseline tests omit delete/invalid inputs: green does not mean complete.
* Default quantity is 1; creation uses incrementing IDs starting at 1 per app.
* There is no authentication or persistence. Bind only to localhost.
* README is participant setup, not an architecture/conventions document. It
  does not mention these gaps; `AGENTS.md` documents them from Lab 3A onward.
* `m2-prompting` has the same files as `start`. It stays as the named Module 2
  starting point; the exercise prompts are on `materials`.
* The module branches primarily add customizations, not all possible API fixes.
  Kit branches implement their named features only.

Do not fix all gaps before the labs: they motivate specific customizations.
In Module 2, run both prompts against identical starting code; independent
worktrees are preferable to undoing a large agent edit.

## Optional plugin stretch goal

The reference solution is `plugin/` on `m3-complete` (also on `m4-hve` and
`m5-speckit`). It follows the current
[plugin authoring reference](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference):
Agent Plugins 1.0 `plugin.json` with `$schema`, the portable skill in `skills/`
and the Copilot-specific agents in `com.github.copilot/agents/`. Keep the
working workspace customizations as the primary solution. The plugin bundles
no MCP, instructions or hook: the Local formatter hook assumes the repository
root and plugin hooks use the Copilot hook contract. The packaged skill scripts
find the repository from the terminal's working directory, not from their
install location. `tests/unit/test_plugin.py` checks the manifest, that the
packaged agents and template match the workspace copies, and the scripts.
Rehearse the trial in `plugin/README.md`: install from a local folder into a
disposable worktree without the workspace copies, then test discovery and
handoff before sharing.

## Fallbacks and evidence

Module 4 and 5 files are explicitly **curated examples**, not fabricated logs
of live HVE or Spec Kit agent runs. They include code, acceptance criteria and
tests that can be validated locally. Installation/discovery and live agent
behavior must still be rehearsed in VS Code. No command-line test proves that
the selected editor harness loaded a customization.

## Preparation validation (2026-11-04)

Every checkpoint passed `uv sync --locked`, the supported pytest command and
both ruff checks on Windows with Python 3.14.10 and uv 0.13.7. The preparation
machine could not reach the public file host, so packages were installed
through the approved-mirror path above. The lock was verified with
`uv lock --check`, and every locked file's sha256 matches the file PyPI
publishes. Run `uv sync --locked` once on a machine with public PyPI access
before the workshop.

| Branch | Passing tests |
|---|---:|
| start | 3 |
| m2-prompting | 3 |
| m3-instructions | 3 |
| m3-skills | 10 |
| m3-agents | 10 |
| m3-complete | 36 |
| m4-hve | 46 |
| m5-speckit | 48 |

Also checked every branch's expected file layout, YAML frontmatter, JSON,
relative documentation links, Python 3.11 syntax and absence of MCP configuration.
Runtime tests were on 3.14, not every supported interpreter. The generated Spec
Kit PowerShell prerequisite check resolved the prepared feature successfully.

One upstream Starlette/httpx deprecation warning is present; tests pass.
Live VS Code discovery, references, agent handoffs, hook activation and HVE
installation remain trainer rehearsal steps. These checks do not prove model
output quality or a successful live kit session.
