# Agent patterns

Reusable Crafting Agent UI patterns. Each pattern is a set of custom agents (and, for eval, a sandbox template) you install on your own org.

These examples are not tied to a particular product, template, or site. After install, you point the engineering manager, incident commander, and code review team at *your* templates and sandboxes, and the eval matrix at *your* org’s LLM catalog.

Roles and isolation follow published designs from Anthropic, Google, GitHub, OpenAI, and OWASP. See [SOURCES.md](SOURCES.md).

To install, start a **new session** in Crafting Agent UI with the default agent (do not pick a custom agent). Paste that pattern’s install prompt as the entire message. The default agent checks out this repository, follows [INSTALL.md](INSTALL.md), and prints what to run next. You need permission to create org-shared agents (`cs llm agent create --shared`); if you are not an org admin, install still works as personal agents.

## Engineering manager

A coordinator (`em-manager`) that does **not** write code. It plans, delegates, and checks work. Specialists (`em-coding`, `em-qa`, `em-integ`) each get a self-contained task in their own session, so the manager’s context stays small.

Use this when a change needs implementation plus verification, and you want the coordinator to loop on evidence instead of accumulating a huge coding transcript.

```mermaid
sequenceDiagram
  participant User
  participant Manager as em-manager
  participant Coding as em-coding
  participant QA as em-qa
  participant Integ as em-integ
  User->>Manager: Issue plus template name
  Manager->>Coding: Implement in sandbox
  Coding-->>Manager: Sandbox id plus what changed
  Manager->>QA: Verify locally in that sandbox
  QA-->>Manager: Pass or fail evidence
  alt QA failed
    Manager->>Coding: Original req plus QA evidence
  end
  Manager->>Integ: Verify via intercept if plan exists
  Integ-->>Manager: Pass or fail evidence
```

```
Set up the engineering manager pattern from https://github.com/crafting-demo/agent-patterns. Create a sandbox from that repo if needed (or git pull if it already exists), open a workspace, follow INSTALL.md without asking for confirmation, and finish by printing the example prompt.
```

After install, start a **new** session, select agent `em-manager`, and paste [patterns/engineering-manager/example-prompt.md](patterns/engineering-manager/example-prompt.md) — or your own issue plus a template name from your org. The manager lists templates if you do not name one.

More detail: [patterns/engineering-manager/README.md](patterns/engineering-manager/README.md)

## Incident commander

A coordinator (`ic-manager`) that does **not** patch. It plans, delegates reproduction, and optional cluster checks. Specialists (`ic-repro`, `ic-cluster`) each get a self-contained task in their own session. The output is a diagnosis and a recommended next step, not a pull request.

Use this when the question is “what broke and where,” not “implement this issue.”

```mermaid
sequenceDiagram
  participant User
  participant Manager as ic-manager
  participant Repro as ic-repro
  participant Cluster as ic-cluster
  User->>Manager: Symptom plus template name
  Manager->>Repro: Reproduce in sandbox
  Repro-->>Manager: Local evidence plus sandbox id
  alt Template has intercept plan
    Manager->>Cluster: Same flow via intercept
    Cluster-->>Manager: Cluster evidence
  else No intercept plan
    Manager-->>User: Skip cluster and say why
  end
  Manager-->>User: Diagnosis and recommended next step
```

```
Set up the incident commander pattern from https://github.com/crafting-demo/agent-patterns. Create a sandbox from that repo if needed (or git pull if it already exists), open a workspace, follow INSTALL.md without asking for confirmation, and finish by printing the example prompt.
```

After install, start a **new** session, select agent `ic-manager`, and paste [patterns/incident-commander/example-prompt.md](patterns/incident-commander/example-prompt.md) — or your own symptom plus a template name from your org. The manager lists templates if you do not name one.

More detail: [patterns/incident-commander/README.md](patterns/incident-commander/README.md)

## Code review

A coordinator (`cr-manager`) that does **not** patch. It fans the same diff out to quality, logic, and security specialists. Each specialist is instruction-enforced read-only (Crafting has no tool allowlist). The output is one review, not a PR.

Use this when a change already exists and you want a gate.

```mermaid
sequenceDiagram
  participant User
  participant Manager as cr-manager
  participant Quality as cr-quality
  participant Logic as cr-logic
  participant Sec as cr-sec
  User->>Manager: Sandbox plus diff to review
  Manager->>Quality: Norms and quality (read-only)
  Manager->>Logic: Correctness (read-only)
  Manager->>Sec: Security (read-only)
  Quality-->>Manager: Critical / Suggestions / Good
  Logic-->>Manager: Critical / Suggestions / Good
  Sec-->>Manager: Critical / Suggestions / Good
  Manager-->>User: Merged review
```

```
Set up the code review pattern from https://github.com/crafting-demo/agent-patterns. Create a sandbox from that repo if needed (or git pull if it already exists), open a workspace, follow INSTALL.md without asking for confirmation, and finish by printing the example prompt.
```

After install, start a **new** session, select agent `cr-manager`, and paste [patterns/code-review/example-prompt.md](patterns/code-review/example-prompt.md) — or name a sandbox that already has the change.

More detail: [patterns/code-review/README.md](patterns/code-review/README.md)

## Agent eval

Compare **prompt × model** variants of the same coding agent on a fixed kata. The orchestrator (`eval-manager`) does not implement the task. Each candidate is a sub-agent with its own `model:` (`provider:name`) and prompt. Each trial is a new session with a fresh sandbox from template `eval-kata`.

Use this when you want to try models **before** assigning org purposes like CODING or FAST. Point slot A and slot B at any two models already in your org catalog.

```mermaid
flowchart TD
  EvalMgr[eval-manager]
  subgraph matrix [Prompt x model slots]
    MinA[ev-min-a]
    MinB[ev-min-b]
    ThrA[ev-thr-a]
    ThrB[ev-thr-b]
  end
  EvalMgr -->|"N trials each, same task"| MinA
  EvalMgr -->|"N trials each, same task"| MinB
  EvalMgr -->|"N trials each, same task"| ThrA
  EvalMgr -->|"N trials each, same task"| ThrB
  MinA --> S1[Fresh eval-kata sandbox per trial]
  MinB --> S1
  ThrA --> S1
  ThrB --> S1
  S1 -->|artifact per trial| EvalMgr
```

```
Set up the agent eval pattern from https://github.com/crafting-demo/agent-patterns. Create a sandbox from that repo if needed (or git pull if it already exists), open a workspace, follow INSTALL.md without asking for confirmation, and finish by printing the example prompt.
```

After install, start a **new** session, select agent `eval-manager`, and paste [patterns/agent-eval/example-prompt.md](patterns/agent-eval/example-prompt.md). Do **not** set a session model override, or every cell can collapse to one model.

A ranking is valid only if **both** slots produced implementation artifacts. Provider 5xx / RPC errors are incomplete trials: `eval-manager` retries, then rebinds the dead slot to another catalog model and re-runs those cells.

More detail: [patterns/agent-eval/README.md](patterns/agent-eval/README.md)
