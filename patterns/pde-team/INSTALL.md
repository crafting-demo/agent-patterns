# Install: PDE team

Do this after the repository root `INSTALL.md`.

Create specialists **before** the lead.

From the repository root:

```sh
cs llm agent create pe-pm --shared patterns/pde-team/agents/pe-pm.yaml
cs llm agent create pe-design --shared patterns/pde-team/agents/pe-design.yaml
cs llm agent create pe-em --shared patterns/pde-team/agents/pe-em.yaml
cs llm agent create pe-notify --shared patterns/pde-team/agents/pe-notify.yaml
cs llm agent create pe-lead --shared patterns/pde-team/agents/pe-lead.yaml
```

If a name already exists, `cs llm agent update ... --shared FILE.yaml` instead. Omit `--shared` if you are not an org admin.

`pe-notify` is always installed. It no-ops unless coworker-bot or Slack tools are present. Optional: create a sandbox from [crafting-demo/coworker-bot](https://github.com/crafting-demo/coworker-bot) if this org should get Slack pings.

Verify:

```sh
cs llm agent list
cs llm agent show pe-lead --shared
```

You should see `pe-lead` with four sub-agents.

Then tell the user to start a **new** session, select agent `pe-lead`, and paste `patterns/pde-team/example-prompt.md`.
