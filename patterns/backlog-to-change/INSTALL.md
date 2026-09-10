# Install: backlog to reviewed change

Do this after the repository root `INSTALL.md`. Hub compile steps are in `HUB.md`.

Create specialists **before** coordinators.

Agents from the hub, in order:

1. `software-engineer`
2. `qa-engineer`
3. `code-reviewer`
4. `engineering-manager`
5. `product-manager`

If the user named **Jira** or **Linear** (or an org `named_mcp_servers` ref), compile product-manager with that provider:

```sh
python3 scripts/build.py product-manager --provider ticket_board=jira
# or ticket_board=linear
```

Otherwise compile it unbound (works from a pasted backlog; MCP not attached).

`product-manager` and `code-reviewer` emit exec templates (`hub-product-manager`, `hub-code-reviewer`) because they ship skills — create those templates before the agents.

Verify:

```sh
cs llm agent list
cs llm agent show product-manager --shared
cs llm agent show engineering-manager --shared
cs llm agent show code-reviewer --shared
```

Then tell the user to start **new** sessions in order: `product-manager`, then `engineering-manager`, then `code-reviewer`, using `patterns/backlog-to-change/example-prompt.md`.
