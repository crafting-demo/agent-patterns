# Install: vendor contract review

Do this after the repository root `INSTALL.md`. Hub compile steps are in `HUB.md`.

Create specialists **before** the coordinator.

Agents from the hub, in order:

1. `contract-analyst`
2. `compliance-reviewer`
3. `legal-counsel`

Follow `HUB.md` for clone/compile/`cs template create`/`cs llm agent create`.

Verify:

```sh
cs llm agent list
cs llm agent show legal-counsel --shared
```

You should see `legal-counsel` with sub-agents `contract-analyst` and `compliance-reviewer`.

Then tell the user to start a **new** session, select agent `legal-counsel`, and paste `patterns/vendor-contract-review/example-prompt.md`.
