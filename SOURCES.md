# Sources

These Crafting patterns follow published agent designs from Anthropic, Google, GitHub, OpenAI, and OWASP. Crafting YAMLs are ours (sandbox join, `cs`, org-shared agents). The *roles*, *read-only reviewers*, *fresh specialist sessions*, and *review output shape* are the parts we interleaved from the sources below.

We do not vendor other vendors’ plugin files. Their production prompts stay internal; these are the public docs and official examples they actually shipped.

## Shared ideas (all patterns)

| Idea | Where it is published |
| --- | --- |
| Specialists in **isolated context**, parent only sees the summary | [Anthropic: Create custom subagents](https://code.claude.com/docs/en/sub-agents) |
| Do not mix implement and review in one session; review the diff in a **fresh** subagent | [Anthropic: Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) |
| Sequential pipeline: write, then review (we do **not** auto-refactor in the reviewer) | [Google ADK SequentialAgent](https://github.com/google/adk-docs/blob/main/docs/agents/workflow-agents/sequential-agents.md) |
| Durable project norms live in-repo (`AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`) | [OpenAI Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md), Anthropic `CLAUDE.md` |

## Code review

Official specialist splits we mapped onto `cr-quality` / `cr-logic` / `cr-sec`:

- Anthropic Claude Code plugin **[pr-review-toolkit](https://github.com/anthropics/claude-code/tree/main/plugins/pr-review-toolkit)** — `code-reviewer`, `pr-test-analyzer`, `silent-failure-hunter`, `type-design-analyzer`, `comment-analyzer`, `code-simplifier`; fan-out via [`review-pr`](https://github.com/anthropics/claude-code/blob/main/plugins/pr-review-toolkit/commands/review-pr.md).
- Anthropic plugin **[code-review](https://github.com/anthropics/claude-code/tree/main/plugins/code-review)** — parallel agents for project-guide compliance, bugs, history, comments; confidence scoring.
- Anthropic docs: read-only **code-reviewer** (`Read`, `Grep`, `Glob`) and **security-reviewer** in [subagents](https://code.claude.com/docs/en/sub-agents) and [best practices](https://code.claude.com/docs/en/best-practices). Crafting has no tool allowlist on `LLMAgent`; we enforce the same contract in instructions (join an existing sandbox, do not write).
- Google ADK **Code Reviewer** criteria: correctness, readability, efficiency, edge cases, best practices — [example](https://github.com/google/adk-docs/blob/main/examples/python/snippets/agents/workflow-agents/sequential_agent_code_development_agent.py).
- GitHub Copilot official **[review-code](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/review-code)** prompt: Critical / Suggestions / Good practices, line refs, constructive tone. Also [Copilot instructions files](https://github.blog/ai-and-ml/github-copilot/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files/).
- OpenAI Codex: put review rules in `AGENTS.md` ([guide](https://developers.openai.com/codex/guides/agents-md)).
- **OWASP Top 10** and **CWE** as the security taxonomy (same approach as public Copilot `security-reviewer` agents).

## Engineering manager

- Google ADK sequential **writer then reviewer** (implement, then QA — we skip their refactorer agent; the manager sends failures back to `em-coding`).
- Anthropic: verification in a **fresh** specialist session that did not write the change.

## Incident commander

- Same read-only contract as Anthropic’s reviewer/security-reviewer: reproduce and report, do not patch.
- Fresh specialist context so diagnosis is not graded by the session that would want to “just fix it.”

## Agent eval

- Isolated trial sessions = Anthropic subagent isolation (each cell is a new context).
- Independent repeats so one lucky run does not decide the ranking (eval hygiene, not a vendor plugin).
