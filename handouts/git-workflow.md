# Git workflow card

Checkpoint branches are read-only references. Work on your own branch and
never commit to a checkpoint. In a clone, checkpoints are `origin/<branch>`;
in the original repository without a remote, drop the `origin/` prefix.
Stop a running server before switching branches.

These handouts are on the separate `materials` branch. Read them on GitHub or in
a worktree outside the lab folder; never merge them into your work.

## Start (before Module 2)

```powershell
git fetch origin
git switch -c my-work origin/m2-prompting
```

## Save work during labs

Labs create new files, so `git commit -am` alone is not enough:

```powershell
git add -A
git commit -m "Lab 3A"
```

## Catch up to a checkpoint

1. Check `git status`. Keep or discard your attempt.
   * Keep it: `git add -A`, then `git commit -m "Lab 3A attempt"`.
   * Discard it: `git restore --staged --worktree .`, then `git clean -fd`.
     `git clean` deletes untracked files; preview with `git clean -nd` first.
2. Continue from the checkpoint on a new personal branch:

| Before | Checkpoint | Catch-up command |
|---|---|---|
| Module 2 exercise | `m2-prompting` | `git switch -c my-work origin/m2-prompting` |
| Lab 3A | `m2-prompting` | `git switch -c my-work-3a origin/m2-prompting` |
| Skill demo (3.3) | `m3-instructions` | `git switch -c my-work-33 origin/m3-instructions` |
| Lab 3B | `m3-skills` | Sync below, or `git switch -c my-work-3b origin/m3-skills` |
| Lab 3C | `m3-agents` | `git switch -c my-work-3c origin/m3-agents` |
| Module 4 (HVE Core) | `m3-complete` | `git switch -c my-work-m4 origin/m3-complete` |
| Module 5 (Spec Kit) | `m3-complete` | `git switch -c my-work-m5 origin/m3-complete` |

If a branch name already exists, pick another one.

## Required sync before Lab 3B

The trainer builds the add-endpoint prompt and skill in the 3.3 demo, and
Lab 3C extends that skill. Everyone needs it. On your own branch, commit your
work first, then copy only the demo files. This avoids conflicts with your own
instruction files:

```powershell
git checkout origin/m3-skills -- .github/skills .github/prompts
git commit -m "Sync add-endpoint skill from m3-skills"
```

Prefer a clean state? Use `git switch -c my-work-3b origin/m3-skills` instead.

## Compare with a solution

```powershell
git diff origin/m3-instructions -- AGENTS.md .github
```

## Modules 4 and 5

Continue on a personal branch. HVE Core writes to `.copilot-tracking/`;
Spec Kit writes to `.specify/`, `specs/` and `.github/skills/speckit-*`.
Commit before running `specify init`.

## Never

* `git reset --hard` or `git checkout -f` to follow the workshop
* Commit to or push a checkpoint branch
* Merge, check out or copy `materials` into your lab workspace
* Switch branches with uncommitted work you want to keep
