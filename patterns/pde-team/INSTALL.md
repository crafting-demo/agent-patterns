# Install: PDE team

Do this after the repository root `INSTALL.md`.

These agents are compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout; do not clone or build the hub.

Create the template **before** the agent that uses it, and the specialists **before** the coordinators. `pde-lead` delegates to `engineering-manager`, and `engineering-manager` in turn names three specialists of its own, so all seven agents are created here. Only `security-scanner` needs a template.

From the repository root:

```sh
cs template create hub-security-scanner patterns/pde-team/templates/hub-security-scanner.yaml

cs llm agent create software-engineer --shared patterns/pde-team/agents/software-engineer.yaml
cs llm agent create qa-engineer --shared patterns/pde-team/agents/qa-engineer.yaml
cs llm agent create security-scanner --shared patterns/pde-team/agents/security-scanner.yaml
cs llm agent create product-manager --shared patterns/pde-team/agents/product-manager.yaml
cs llm agent create design-lead --shared patterns/pde-team/agents/design-lead.yaml
cs llm agent create engineering-manager --shared patterns/pde-team/agents/engineering-manager.yaml
cs llm agent create pde-lead --shared patterns/pde-team/agents/pde-lead.yaml
```

If a name already exists, run the matching `cs template update ...` or `cs llm agent update NAME --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

`product-manager` is vendored with no ticket board bound; the definition phase does not need one. See [HUB.md](../../HUB.md) if the user wants Jira or Linear attached.

Verify:

```sh
cs llm agent list
cs llm agent show pde-lead --shared
cs llm agent show engineering-manager --shared
```

You should see `pde-lead` with sub-agents `product-manager`, `design-lead`, and `engineering-manager`, and `engineering-manager` with `software-engineer`, `qa-engineer`, and `security-scanner`.

Then tell the user to start a **new** session, select agent `pde-lead`, and paste `patterns/pde-team/example-prompt.md`.
