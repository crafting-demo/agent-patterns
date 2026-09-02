# Install: code review

Do this after the repository root `INSTALL.md`.

Create specialists **before** the manager (the manager references them by name).

From the repository root:

```sh
cs llm agent create cr-quality --shared patterns/code-review/agents/cr-quality.yaml
cs llm agent create cr-logic --shared patterns/code-review/agents/cr-logic.yaml
cs llm agent create cr-sec --shared patterns/code-review/agents/cr-sec.yaml
cs llm agent create cr-manager --shared patterns/code-review/agents/cr-manager.yaml
```

If a name already exists, run the matching `cs llm agent update ... --shared FILE.yaml` instead.

If `--shared` is denied, omit it on every command.

Verify:

```sh
cs llm agent list
cs llm agent show cr-manager --shared
```

You should see `cr-manager` with three sub-agents, and `cr-quality`, `cr-logic`, `cr-sec`.

Then tell the user to start a **new** session, select agent `cr-manager`, and paste the contents of `patterns/code-review/example-prompt.md`.
