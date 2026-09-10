# Secure delivery

Multi-agent demo: `engineering-manager` delegates to `software-engineer`, then `qa-engineer`, then `security-scanner` (lonkero CLI in an exec template). Findings go back to the implementer until clean or blocked.

Agents compile from [crafting-demo/agent-hub](https://github.com/crafting-demo/agent-hub). The scanner is the hub `security-scanner` package (demo-org webscan pattern).

```mermaid
sequenceDiagram
  participant User
  participant EM as engineering-manager
  participant Dev as software-engineer
  participant QA as qa-engineer
  participant Scan as security-scanner
  User->>EM: Change plus template
  EM->>Dev: Implement in sandbox
  Dev-->>EM: Files and endpoints
  EM->>QA: Local QA
  QA-->>EM: Pass or fail
  alt QA failed
    EM->>Dev: Original req plus evidence
  end
  EM->>Scan: Scan reported URLs
  Scan-->>EM: Findings
  alt Findings
    EM->>Dev: Remediate without exploits
  end
```

## Install

```
Set up the secure delivery pattern from https://github.com/crafting-demo/agent-patterns. Create a sandbox from that repo if needed (or git pull if it already exists), open a workspace, follow INSTALL.md without asking for confirmation, and finish by printing the example prompt.
```

After install, start a **new** session, select `engineering-manager`, and paste [example-prompt.md](example-prompt.md).
