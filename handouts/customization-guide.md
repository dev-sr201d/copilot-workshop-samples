# Choose the smallest customization

| Observed problem | Use |
|---|---|
| A one-off requirement was missed | Better task prompt |
| A project convention is repeatedly missed | Always-on instructions |
| A rule concerns only certain files | File-based instructions |
| A multi-step task repeats | Skill with resources |
| A short Local-only task repeats | Prompt file |
| A recurring role needs restricted tools | Custom agent |
| An action must run at a lifecycle event | Hook |
| A team shares a bundle | Plugin |
| An external system needs tools | MCP (disabled in this workshop) |

| Type | Local | Copilot |
|---|---|---|
| Instructions | Yes | Yes |
| Skills | Yes | Yes |
| Prompt files | Yes | No; use a skill |
| Tool sets | Yes | No |
| Custom agents | Yes | Yes; check fields and tool names |
| Hooks | Yes | Yes; different schema/payload |
| Plugins | Yes | Yes; check bundled components |
| MCP | Policy-disabled | Policy-disabled |

User scope is for personal preferences; workspace scope is for shared project
rules. Instructions advise; tools enable actions; hooks run independently of
the model. Instructions are not a security boundary. A formatter hook does not
enforce security policy either.

Keep customizations focused to control context cost. Verify references, debug
logs, frontmatter, globs and the selected harness. A script invoked with normal
terminal approvals can replace an MCP dependency for this workshop.
