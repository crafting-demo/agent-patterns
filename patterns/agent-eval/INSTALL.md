# Install: agent eval

Do this after the repository root `INSTALL.md`.

## 1. Template

```sh
cs template create eval-kata patterns/agent-eval/template/eval-kata.yaml
```

If it already exists:

```sh
cs template update eval-kata patterns/agent-eval/template/eval-kata.yaml
```

## 2. Bind two models (slots A and B)

List what this org already has:

```sh
cs llm config providers list
cs llm config models list
```

(Some sites expose aliases `cs llm provider list` / `cs llm model list`. If those fail, use the `cs llm config …` forms above.)

Choose two distinct `provider:name` selectors that can actually run a chat/coding session:

- If the user named two models in their install message, use those — but only if they appear in the model list.
- Prefer two different providers when the catalog has them.
- Skip FIM / instruct-only models (purpose `CODING_FIM`, or a name like `*-instruct`).
- Prefer a generally available chat model over a `preview` / experimental id when another provider already has a stable chat model. A preview model that never answers is not a second model in the matrix.
- Do **not** assign CODING or FAST purposes. Do **not** invent a model that is not in the catalog.
- If they asked for a model that is missing, stop and tell them how to add it (official OpenAI provider, or OpenAI-compatible `base_url` for a router such as OpenRouter), then wait. Do not remap purposes as a workaround.

Write the two selectors into **every** `REPLACE_SLOT_A` and `REPLACE_SLOT_B` in:

- `patterns/agent-eval/agents/ev-min-a.yaml`
- `patterns/agent-eval/agents/ev-min-b.yaml`
- `patterns/agent-eval/agents/ev-thr-a.yaml`
- `patterns/agent-eval/agents/ev-thr-b.yaml`

Copy those four files to a working directory first if you should not dirty the checkout; replace placeholders in the copies. `eval-manager.yaml` has no model field — do not add one.

## 3. Create candidates, then the manager

```sh
cs llm agent create ev-min-a --shared path/to/ev-min-a.yaml
cs llm agent create ev-min-b --shared path/to/ev-min-b.yaml
cs llm agent create ev-thr-a --shared path/to/ev-thr-a.yaml
cs llm agent create ev-thr-b --shared path/to/ev-thr-b.yaml
cs llm agent create eval-manager --shared patterns/agent-eval/agents/eval-manager.yaml
```

If a name exists, `cs llm agent update NAME --shared FILE.yaml` instead. Omit `--shared` when you are not an org admin.

## 4. Verify

```sh
cs llm agent list
cs llm agent show eval-manager --shared
cs template show eval-kata
```

`eval-manager` must list four sub-agents. Each candidate `show` must display the real `model:` you bound, not the placeholder.

Tell the user to start a **new** session, select agent `eval-manager`, **not** set a session model override, and paste `patterns/agent-eval/example-prompt.md`.
