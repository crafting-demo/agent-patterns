# Install: code review

Do this after the repository root `INSTALL.md`.

This agent is compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout; do not clone or build the hub.

This agent needs no sandbox template; its skill is compiled into the agent's instructions.

From the repository root:

```sh
cs llm agent create code-reviewer --shared patterns/code-review/agents/code-reviewer.yaml
```

If the name already exists, run `cs llm agent update code-reviewer --shared FILE.yaml` instead.

If `--shared` is denied, omit it.

Verify:

```sh
cs llm agent list
cs llm agent show code-reviewer --shared
```

Then tell the user to start a **new** session, select agent `code-reviewer`, and paste the contents of `patterns/code-review/example-prompt.md`.
