# Install: engineering manager

Do this after the repository root `INSTALL.md`.

Create specialists **before** the manager (the manager references them by name).

From the repository root:

```sh
cs llm agent create em-coding --shared patterns/engineering-manager/agents/em-coding.yaml
cs llm agent create em-qa --shared patterns/engineering-manager/agents/em-qa.yaml
cs llm agent create em-integ --shared patterns/engineering-manager/agents/em-integ.yaml
cs llm agent create em-manager --shared patterns/engineering-manager/agents/em-manager.yaml
```

If a name already exists, run the matching `cs llm agent update ... --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

Verify:

```sh
cs llm agent list
cs llm agent show em-manager --shared
```

You should see `em-manager` with three sub-agents, and `em-coding`, `em-qa`, `em-integ`.

Then tell the user to start a **new** session, select agent `em-manager`, and paste the contents of `patterns/engineering-manager/example-prompt.md`.
