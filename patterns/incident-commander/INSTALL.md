# Install: incident commander

Do this after the repository root `INSTALL.md`.

This agent is compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout; do not clone or build the hub.

Create the template **before** the agent that uses it.

From the repository root:

```sh
cs template create hub-incident-commander patterns/incident-commander/templates/hub-incident-commander.yaml
cs llm agent create incident-commander --shared patterns/incident-commander/agents/incident-commander.yaml
```

If a name already exists, run `cs template update ...` or `cs llm agent update incident-commander --shared FILE.yaml` instead.

If `--shared` is denied, omit it.

Verify:

```sh
cs llm agent list
cs llm agent show incident-commander --shared
```

Then tell the user to start a **new** session, select agent `incident-commander`, and paste the contents of `patterns/incident-commander/example-prompt.md`.
