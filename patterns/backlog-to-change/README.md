# Backlog to reviewed change

Multi-agent demo across **sessions**: `product-manager` grooms or specs work from a ticket board (Jira or Linear chosen at install), `engineering-manager` delivers with `software-engineer` + `qa-engineer`, then `code-reviewer` gates the diff.

Agents compile from [crafting-demo/agent-hub](https://github.com/crafting-demo/agent-hub).

```mermaid
sequenceDiagram
  participant User
  participant PM as product-manager
  participant EM as engineering-manager
  participant Dev as software-engineer
  participant QA as qa-engineer
  participant CR as code-reviewer
  User->>PM: Goal plus board
  PM-->>User: Spec or sprint slice
  User->>EM: Spec plus template
  EM->>Dev: Implement
  EM->>QA: Verify
  User->>CR: Review the sandbox diff
  CR-->>User: Critical / Suggestions / Good practices
```

## Install

```
Set up the backlog to reviewed change pattern from https://github.com/crafting-demo/agent-patterns. Create a sandbox from that repo if needed (or git pull if it already exists), open a workspace, follow INSTALL.md without asking for confirmation, and finish by printing the example prompt.
```

After install, run **three** new sessions in order: `product-manager` → `engineering-manager` → `code-reviewer`. Prompts: [example-prompt.md](example-prompt.md).
