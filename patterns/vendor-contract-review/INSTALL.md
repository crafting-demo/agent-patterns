# Install: vendor contract review

Do this after the repository root `INSTALL.md`.

These agents are compiled from the Crafting Agent Hub and committed to this repo ([HUB.md](../../HUB.md)). Everything you need is in this checkout — do not clone or build the hub.

Create the templates **before** the agents that use them, and the specialists **before** the coordinator.

From the repository root:

```sh
cs template create hub-contract-analyst patterns/vendor-contract-review/templates/hub-contract-analyst.yaml
cs template create hub-compliance-reviewer patterns/vendor-contract-review/templates/hub-compliance-reviewer.yaml

cs llm agent create contract-analyst --shared patterns/vendor-contract-review/agents/contract-analyst.yaml
cs llm agent create compliance-reviewer --shared patterns/vendor-contract-review/agents/compliance-reviewer.yaml
cs llm agent create legal-counsel --shared patterns/vendor-contract-review/agents/legal-counsel.yaml
```

If a name already exists, run the matching `cs template update ...` or `cs llm agent update NAME --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

Verify:

```sh
cs llm agent list
cs llm agent show legal-counsel --shared
cs template show hub-contract-analyst
```

You should see `legal-counsel` with sub-agents `contract-analyst` and `compliance-reviewer`.

The demo contract and playbook are in `patterns/vendor-contract-review/fixtures/`, already present in this sandbox. Tell the user that path.

Then tell the user to start a **new** session, select agent `legal-counsel`, and paste the contents of `patterns/vendor-contract-review/example-prompt.md`.
