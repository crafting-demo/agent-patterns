# Install: secure delivery

Do this after the repository root `INSTALL.md`.

These agents are compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout — do not clone or build the hub.

Create the templates **before** the agents that use them, and the specialists **before** the manager.

From the repository root:

```sh
cs template create hub-software-engineer patterns/secure-delivery/templates/hub-software-engineer.yaml
cs template create hub-qa-engineer patterns/secure-delivery/templates/hub-qa-engineer.yaml
cs template create hub-security-scanner patterns/secure-delivery/templates/hub-security-scanner.yaml

cs llm agent create software-engineer --shared patterns/secure-delivery/agents/software-engineer.yaml
cs llm agent create qa-engineer --shared patterns/secure-delivery/agents/qa-engineer.yaml
cs llm agent create security-scanner --shared patterns/secure-delivery/agents/security-scanner.yaml
cs llm agent create engineering-manager --shared patterns/secure-delivery/agents/engineering-manager.yaml
```

If a name already exists, run the matching `cs template update ...` or `cs llm agent update NAME --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

Verify:

```sh
cs llm agent list
cs llm agent show engineering-manager --shared
cs template show hub-security-scanner
```

You should see `engineering-manager` with sub-agents `software-engineer`, `qa-engineer`, and `security-scanner`. The scanner's template plants the lonkero CLI in its sandbox.

Then tell the user to start a **new** session, select agent `engineering-manager`, and paste the contents of `patterns/secure-delivery/example-prompt.md`.
