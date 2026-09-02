# Install: incident commander

Do this after the repository root `INSTALL.md`.

Create specialists **before** the manager (the manager references them by name).

From the repository root:

```sh
cs llm agent create ic-repro --shared patterns/incident-commander/agents/ic-repro.yaml
cs llm agent create ic-cluster --shared patterns/incident-commander/agents/ic-cluster.yaml
cs llm agent create ic-manager --shared patterns/incident-commander/agents/ic-manager.yaml
```

If a name already exists, run the matching `cs llm agent update ... --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

Verify:

```sh
cs llm agent list
cs llm agent show ic-manager --shared
```

You should see `ic-manager` with two sub-agents, and `ic-repro`, `ic-cluster`.

Then tell the user to start a **new** session, select agent `ic-manager`, and paste the contents of `patterns/incident-commander/example-prompt.md`.
