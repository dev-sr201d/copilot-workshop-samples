# Harness, agent, mode, model

| Choice | Meaning | Workshop options |
|---|---|---|
| Harness | Runtime executing the agent loop | Local; Copilot |
| Agent | Role and allowed tools | Ask; Agent; Plan (Local); custom |
| Mode | How the task proceeds | Interactive; Plan; Autopilot (Copilot) |
| Model | Reasoning engine | Copilot models / Auto; Foundry BYOK |

* Inline suggestions and next edit suggestions: while typing.
* Inline chat: Ctrl+I. Chat view: Ctrl+Alt+I.
* Agents window: follow sessions and inspect diffs.
* Copilot harness: choose Plan mode or `/plan`, review, then Implement Plan.
  Approve Plan Only lets you change models before implementation.
* Local harness: choose the Plan agent. All hands-on work uses Local.
* Add selected code, file references, problems or terminal output deliberately.
* Manual approvals are the starting point. Assisted uses model judgment;
  Allow all skips confirmations. Neither substitutes for sandboxing or review.
* Autopilot is a Copilot mode but a Local permission level; use only in a
  trusted workspace with understood approvals.
* BYOK changes model access, not the harness. Check tool calling. The Copilot
  harness may need `chat.agentHost.byokModels.enabled` in the workshop build.
* Manage models with **Chat: Manage Language Models**. Do not paste API keys into
  prompts or commit them. Inline suggestions still use the Copilot service.
* One task per chat. Start fresh when context drifts.

UI and preview flags are build-dependent. See
[VS Code agents](https://code.visualstudio.com/docs/agents/concepts/agents).
