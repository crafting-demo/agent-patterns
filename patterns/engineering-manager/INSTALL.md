# Install: engineering manager

Do this after the repository root `INSTALL.md`.

These agents are compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout; do not clone or build the hub.

Create the templates **before** the agents that use them, and the specialists **before** the manager (it references them by name).

From the repository root:

```sh
cs template create hub-software-engineer patterns/engineering-manager/templates/hub-software-engineer.yaml
cs template create hub-qa-engineer patterns/engineering-manager/templates/hub-qa-engineer.yaml
cs template create hub-security-scanner patterns/engineering-manager/templates/hub-security-scanner.yaml

cs llm agent create software-engineer --shared patterns/engineering-manager/agents/software-engineer.yaml
cs llm agent create qa-engineer --shared patterns/engineering-manager/agents/qa-engineer.yaml
cs llm agent create security-scanner --shared patterns/engineering-manager/agents/security-scanner.yaml
cs llm agent create engineering-manager --shared patterns/engineering-manager/agents/engineering-manager.yaml
```

`engineering-manager` names `security-scanner` as a sub-agent, so it is created even though this pattern's example task never asks for a scan.

If a name already exists, run the matching `cs template update ...` or `cs llm agent update NAME --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

Verify:

```sh
cs llm agent list
cs llm agent show engineering-manager --shared
```

You should see `engineering-manager` with sub-agents `software-engineer`, `qa-engineer`, and `security-scanner`.

Then tell the user to start a **new** session, select agent `engineering-manager`, and paste the contents of `patterns/engineering-manager/example-prompt.md`.
