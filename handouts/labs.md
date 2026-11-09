# Participant labs

Use Local, your preferred Copilot or Foundry tool-calling model, and a fresh
chat for each task. Keep normal terminal approvals. Save work on a personal
branch before moving to a solution checkpoint. Each section names its
checkpoint and the one-line catch-up command; see the
[Git workflow card](git-workflow.md) for keeping or discarding an attempt first.

Keep this card and the other materials outside your lab workspace. Agents read
every file in the open folder, so a copy there lets them read the answers and
hides the difference between a vague and a structured prompt.

## Module 1: orient yourself (trainer demo, Copilot harness)

Start at `start`. Ask: "Explain the create-item request path and where state is
stored. Do not edit." Then Plan mode: "Add an optional description field to items,
default null. Preserve existing responses apart from the new field; test omitted
and supplied values." Review the plan before implementing.
Switch models, show Auto/thinking effort and Manage Language Models. This demo
does not change the prepared branches.

## Module 2: rewrite prompts (10 minutes)

Start: `m2-prompting`. Catch up: `git switch -c my-work origin/m2-prompting`.
Open [the weak prompts](../exercises/weak-prompts.md) from the materials, not
from your workspace; write your own improved prompts before opening
[the example rewrites](../exercises/improved-prompts.md). Apply the four-part
template. Run weak and improved versions in separate chats on separate personal
branches/worktrees from the same checkpoint. Run tests and inspect scope/diffs.
Compare with a neighbor; a reasonable weak-prompt result is still possible.

## Lab 3A: instructions (15 minutes including explanation)

Start: `m2-prompting`. Solution: `m3-instructions`.
Catch up: `git switch -c my-work-3a origin/m2-prompting`.

1. Ask `/init` to draft project instructions. Read the API and config first.
2. Keep setup and architecture in `AGENTS.md`; keep shared behavioral rules in
   `.github/copilot-instructions.md`, without duplicating paragraphs.
3. Add Python instructions and pytest-specific instructions with scoped globs.
4. Include the exact pytest command, per-app fixture isolation, and the intended
   `{"detail": "Item not found"}` 404 convention. Do not silently rewrite the
   deliberately inconsistent baseline.
5. Ask for a missing-item test. Check response references/debug context for
   repository instructions and the test-scoped file. Verify pytest and ruff.

## Demo: prompt to skill (15 minutes)

Start: `m3-instructions`. Solution: `m3-skills`.
Catch up: `git switch -c my-work-33 origin/m3-instructions`.

Create `/add-endpoint` as a Local prompt, then as a skill with a router template
and route validator. Task: "Add GET /version returning the app version. No new
dependency; no storage change. Cover status and JSON shape."
Inspect the template rather than blindly copying it. Verify the script against
`/health` first; a nonexistent path must fail. Confirm automatic skill discovery
in a fresh session and distinguish the prompt/skill entries in the slash menu.

## Lab 3B: agents (15 minutes including explanation)

Start: `m3-skills`. Solution: `m3-agents`.

**Required sync first:** Lab 3C extends the skill from the trainer demo, so
everyone brings it into their work. On your own branch, commit, then run:

```powershell
git checkout origin/m3-skills -- .github/skills .github/prompts
git commit -m "Sync add-endpoint skill from m3-skills"
```

Or start clean: `git switch -c my-work-3b origin/m3-skills`.

Create a planner and reviewer with only read/search tools. Planner output must
name files, acceptance criteria, test strategy and risks; add an unsubmitted
handoff to built-in Agent. Plan GET /version, review the plan, hand off and
implement. Select reviewer and review the result. It must report evidence and
must not edit files or claim to run tests without execution tools.

## Lab 3C: hook and script (15 minutes including explanation)

Start: `m3-agents`. Solution: `m3-complete`.
Catch up: `git switch -c my-work-3c origin/m3-agents`.

1. Review the Local `PostToolUse` hook and Python formatter script before enabling.
2. Ask Agent to make an intentionally unformatted small Python edit. Check the
   hook diagnostic in the session log and the resulting diff.
3. Confirm read-only calls do not format and an unrelated Python file stays
   unchanged. Hook failures must be visible.
4. Extend the skill with `check_openapi.py`: test GET /health's documented 200
   response and POST /items' documented 201 response. Wrong paths/methods/statuses
   must exit nonzero. Run the new script tests, pytest and ruff.

Hooks are harness-specific. This solution targets Local; do not copy it unchanged
into Copilot. A passing script test alone does not prove editor hook activation.

## Stretch: package as a plugin (Module 3 buffer)

Optional. Package the add-endpoint skill and the planner/reviewer agents as a
local plugin. Reference solution: `plugin/` on `m3-complete`; its README shows
how to try it in a disposable worktree without loading duplicate copies.

## Module 4: HVE Core (hands-on research/plan)

Start: `m3-complete`. Prepared solution: `m4-hve`.
Catch up: `git switch -c my-work-m4 origin/m3-complete`.

Select RPI Agent after installing the plugin. Prompt:

> Add optional max_quantity filtering to GET /items so warehouse staff can
> find low-stock items. Inclusive threshold, integer >= 0, missing means all
> items, empty results return [], preserve insertion order and all existing
> endpoint contracts. No dependency or persistence changes. Research and plan
> first; include tests for 0, equality, invalid input and empty results. Use no MCP.

Participants stop after research/plan. Trainer implements and reviews, or opens
the curated `.copilot-tracking/` fallback artifacts. Compare tests with criteria.

## Module 5: Spec Kit (optional follow-along)

Start: `m3-complete`. Prepared solution: `m5-speckit` (independent of `m4-hve`).
Catch up: `git switch -c my-work-m5 origin/m3-complete`.
Initialize only on a personal branch; follow the kit installation card.

* `/speckit-constitution`: preserve public contracts; tests prove changes; no
  services/dependencies; memory-only application; normal approval boundaries.
* `/speckit-specify`: optional case-insensitive substring name search on GET /items;
  trim query whitespace, empty query means no filter, preserve order, return []
  when unmatched.
* `/speckit-clarify`: explicitly choose Unicode casefold behavior.
* `/speckit-plan`: FastAPI/Pydantic, existing store, pytest and ruff.
* Inspect prepared tasks and implementation to save time. Compare specification,
  tests and implementation; use `/speckit-converge` if available.

Do not enable MCP or install extra extensions for these labs.

## Wrap-up

Pick the smallest useful customization to take home. HVE provides a broad RPI
workflow; Spec Kit starts from explicit intent. Both reuse Module 3 primitives.
Review the reference links on the kit card and keep your own lab commits.
