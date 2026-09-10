# Install: secure delivery

Do this after the repository root `INSTALL.md`. Hub compile steps are in `HUB.md`.

Create specialists **before** the manager.

Agents from the hub, in order:

1. `software-engineer`
2. `qa-engineer`
3. `security-scanner` (creates template `hub-security-scanner`)
4. `engineering-manager`

Follow `HUB.md`. `security-scanner` must have its template created **before** the agent.

Verify:

```sh
cs llm agent list
cs llm agent show engineering-manager --shared
cs template show hub-security-scanner
```

You should see `engineering-manager` with sub-agents `software-engineer`, `qa-engineer`, and `security-scanner`.

Then tell the user to start a **new** session, select agent `engineering-manager`, and paste `patterns/secure-delivery/example-prompt.md`.
