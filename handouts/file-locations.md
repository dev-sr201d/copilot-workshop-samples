# Files and frontmatter

Paths are relative to the repository root.

| File | Purpose / essential fields |
|---|---|
| `AGENTS.md` | Setup and architecture; plain Markdown |
| `.github/copilot-instructions.md` | Always-on project conventions |
| `.github/instructions/python.instructions.md` | `description`, `applyTo: "**/*.py"` |
| `.github/instructions/tests.instructions.md` | `description`, `applyTo: "tests/**/*.py"` |
| `.github/prompts/add-endpoint.prompt.md` | `description`, `agent: agent`; Local only |
| `.github/skills/add-endpoint/SKILL.md` | `name: add-endpoint`, `description` |
| `.github/agents/planner.agent.md` | `description`, `tools`, `handoffs` |
| `.github/agents/reviewer.agent.md` | `description`, `tools: [read, search]` |
| `.github/hooks/format-after-edit.json` | Local `PostToolUse` command hook |
| `plugin/plugin.json` | Optional stretch goal: Agent Plugins `$schema`, `name` |
| `plugin/skills/add-endpoint/` | Packaged skill; scripts find the repo from the cwd |
| `plugin/com.github.copilot/agents/` | Packaged planner and reviewer agents |

Example file-based instruction:

```yaml
---
description: "Use when adding pytest tests for the inventory API."
applyTo: "tests/**/*.py"
---
```

Skill names must match their directory. Quote descriptions containing colons.
Use spaces, not tabs. Agent tools are a real restriction: the reviewer has no
edit or terminal tools. Do not pin a model unavailable to participants.

The add-endpoint prompt and skill share a slash name: select the correct entry
in the `/` menu. The skill also supports automatic discovery by description.
Skills bundle resources; prompt files are single saved tasks.

Spec Kit adds `.github/skills/speckit-*/SKILL.md` and `.specify/`.
HVE Core's RPI workflow records artifacts under `.copilot-tracking/`.
The optional plugin reference solution is in `plugin/` on `m3-complete`;
installing both plugin and workspace copies can load duplicate customizations.
