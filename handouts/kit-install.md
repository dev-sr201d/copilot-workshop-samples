# HVE Core and Spec Kit

Install before the session when possible. All hands-on uses **Local**. No MCP
server, `gh` login, Foundry credentials in files, or cloud deployment is needed.

## HVE Core

1. Command Palette: **Chat: Install Plugin from Source**.
2. Source: `https://github.com/microsoft/hve-core`; scope **User**.
3. Alternatively use Agent Customizations > Plugins > add next to User.
4. Verify the plugin is enabled for Local and **RPI Agent** appears.
5. Do not install the older Marketplace extension for this workshop.

Run the prompt in the lab walkthrough. If an optional researcher requests
Microsoft Docs MCP, keep it disabled and use built-in read/search/web tools.
Do not assume every HVE workflow is MCP-free. Prepared RPI artifacts in
`m4-hve` let you continue without an installation or network connection.

## Spec Kit

```powershell
uv tool install specify-cli
uv tool update-shell
specify --version
```

Open a new terminal if `%USERPROFILE%\.local\bin` was added to PATH.
This installs from public PyPI. If your network blocks it, use your
organization's approved feed instead:

```powershell
uv tool install specify-cli --index-url <approved-pypi-feed>
```

Replace the placeholder; never commit feed credentials.

The session plan tested CLI 1.2.3 on Windows with Python 3.14. Recheck the version
and `specify init --help` on your machine before the workshop.

On a **personal exercise branch** created from `m3-complete`, initialize the current
repository (first check `git status` and commit your work):

```powershell
specify init --here --integration copilot --script ps --non-interactive --force
```

For a separate disposable project:

```powershell
specify init demo --integration copilot --script ps --non-interactive
```

The non-interactive flag avoids agent-terminal input hangs. `--force` is required
to merge into this nonempty repository; use it only on a saved personal branch
from `m3-complete`, before Spec Kit files exist. Do not reinitialize `m5-speckit` or
overwrite your own Spec Kit work. Review generated files before committing.
In a fresh Local chat, discover `/speckit-*` skills.

Run constitution, specify, clarify if needed, plan, tasks, analyze if available,
implement, then converge. Use the prepared artifacts in `m5-speckit` for the
longer steps. Never claim these fallback artifacts were produced by a live agent
run; they are curated workshop examples.

Optional follow-up only: `specify extension add bug`. Inspect extensions and
presets before installation; none is required by these samples.

References: [HVE Core](https://github.com/microsoft/hve-core),
[Spec Kit](https://github.com/github/spec-kit),
[VS Code customization](https://code.visualstudio.com/docs/agent-customization/overview).
