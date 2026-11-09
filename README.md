# GitHub Copilot workshop materials

Handouts, lab instructions, prompt exercises and trainer notes for the
GitHub Copilot workshop samples. The application code lives on the checkpoint
branches (`start`, `m2-prompting`, ... `m5-speckit`); this orphan branch shares
no history or files with them.

## Why this branch is separate

Agents search every file in the open workspace. When these materials sat next to
the code, even fast models found the improved prompts, the worked example and the
known baseline gaps, so a vague prompt behaved like a structured one and the
Module 1 and 2 comparisons stopped working. Keep the checkpoint branches free of
lab prompts, answers and acceptance criteria.

Read the materials on GitHub, print them, or use a separate worktree **outside**
the lab folder. Never open it in the same VS Code window (or multi-root
workspace) as the samples, and never merge or check out `materials` into a lab
branch.

```powershell
git worktree add ..\workshop-materials origin/materials
```

## Contents

Participants:

* [Lab walkthrough](handouts/labs.md)
* [Git workflow card](handouts/git-workflow.md)
* [Prompt template](handouts/prompt-template.md)
* [Copilot controls](handouts/copilot-controls.md)
* [Customization decision guide](handouts/customization-guide.md)
* [Files and frontmatter](handouts/file-locations.md)
* [Kit installation](handouts/kit-install.md)
* Module 2 exercise: [weak prompts](exercises/weak-prompts.md) and
  [example rewrites](exercises/improved-prompts.md) (open after attempting)

Trainer:

* [Trainer runbook](trainer/runbook.md)
* [Local formatter hook notes](trainer/hook-notes.md)
