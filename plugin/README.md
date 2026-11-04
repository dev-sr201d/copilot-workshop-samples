# Inventory workshop plugin (optional stretch goal)

Reference solution for the Module 3 packaging stretch goal. It uses the
[Agent Plugins 1.0 layout](https://code.visualstudio.com/docs/agents/reference/agent-plugin-reference):

```text
plugin/
  plugin.json                       manifest with the Agent Plugins $schema
  skills/add-endpoint/              portable skill, template and scripts
  com.github.copilot/agents/        Copilot-specific planner and reviewer agents
```

## What is packaged and what is not

| Customization | Packaged | Reason |
|---|---|---|
| add-endpoint skill (Lab 3C version) | Yes | Portable; scripts find the repository from the terminal's current directory |
| planner and reviewer agents (Lab 3B) | Yes | Identical copies of `.github/agents/` |
| Instructions (Lab 3A) | No | Repository-specific; they stay in `AGENTS.md` and `.github/` |
| Formatter hook (Lab 3C) | No | Uses the Local hook schema and assumes the repository root; plugin hooks use the Copilot hook contract |
| MCP servers | No | Disabled by policy in this workshop |

## Try it

1. Use a disposable worktree so the workspace copies do not load twice:

   ```powershell
   git worktree add ..\plugin-trial -b my-plugin-trial origin/m3-complete
   cd ..\plugin-trial
   git rm -r -q .github/skills/add-endpoint .github/agents
   ```

   Without a remote, use `m3-complete` instead of `origin/m3-complete`.
2. Open `..\plugin-trial` in VS Code. In the Agent Customizations editor, select
   **Plugins**, select add (`+`) next to **Workspace**, and enter the full path
   of this `plugin` folder (or run **Chat: Install Plugin from Source**).
3. Check that the plugin is enabled for Local and that `add-endpoint`, `planner`
   and `reviewer` appear once each.
4. In a fresh Local chat, select `planner`, plan GET /version, hand off and let
   the add-endpoint skill run its scripts. Then review with `reviewer`.
5. Uninstall the plugin and remove the worktree when finished.

Review every file before installing a plugin; installed skills and agents are
trusted customizations. Keep the workspace files as the primary lab solution.
