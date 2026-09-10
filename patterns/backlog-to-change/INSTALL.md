# Install: backlog to reviewed change

Do this after the repository root `INSTALL.md`.

These agents are compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout — do not clone or build the hub.

Create the templates **before** the agents that use them, and the specialists **before** the manager.

From the repository root:

```sh
cs template create hub-product-manager patterns/backlog-to-change/templates/hub-product-manager.yaml
cs template create hub-software-engineer patterns/backlog-to-change/templates/hub-software-engineer.yaml
cs template create hub-qa-engineer patterns/backlog-to-change/templates/hub-qa-engineer.yaml
cs template create hub-security-scanner patterns/backlog-to-change/templates/hub-security-scanner.yaml
cs template create hub-code-reviewer patterns/backlog-to-change/templates/hub-code-reviewer.yaml

cs llm agent create software-engineer --shared patterns/backlog-to-change/agents/software-engineer.yaml
cs llm agent create qa-engineer --shared patterns/backlog-to-change/agents/qa-engineer.yaml
cs llm agent create security-scanner --shared patterns/backlog-to-change/agents/security-scanner.yaml
cs llm agent create engineering-manager --shared patterns/backlog-to-change/agents/engineering-manager.yaml
cs llm agent create code-reviewer --shared patterns/backlog-to-change/agents/code-reviewer.yaml
cs llm agent create product-manager --shared patterns/backlog-to-change/agents/product-manager.yaml
```

`engineering-manager` declares `software-engineer`, `qa-engineer`, and `security-scanner` as sub-agents, so all three exist before it is created even though this pattern's example task never asks for a scan.

If a name already exists, run the matching `cs template update ...` or `cs llm agent update NAME --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

`product-manager` is vendored with no ticket board bound, so it works from a pasted backlog. If the user asked for **Jira** or **Linear**, say that binding a board means re-vendoring that package from the hub with `--provider ticket_board=jira` (see [HUB.md](../../HUB.md)); do not hand-edit the compiled file during install.

Verify:

```sh
cs llm agent list
cs llm agent show product-manager --shared
cs llm agent show engineering-manager --shared
cs llm agent show code-reviewer --shared
```

Then tell the user to start **new** sessions in order — `product-manager`, then `engineering-manager`, then `code-reviewer` — using `patterns/backlog-to-change/example-prompt.md`.
