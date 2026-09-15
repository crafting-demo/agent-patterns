# Install: incident commander

Do this after the repository root `INSTALL.md`.

This agent is compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout; do not clone or build the hub.

This agent needs no sandbox template; its skill is compiled into the agent's instructions.

From the repository root:

```sh
cs llm agent create incident-commander --shared patterns/incident-commander/agents/incident-commander.yaml
```

If the name already exists, run `cs llm agent update incident-commander --shared FILE.yaml` instead.

If `--shared` is denied, omit it.

Verify:

```sh
cs llm agent list
cs llm agent show incident-commander --shared
```

Then tell the user to start a **new** session, select agent `incident-commander`, and paste the contents of `patterns/incident-commander/example-prompt.md`.
