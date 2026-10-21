# AGENTS.md – {{TITLE}}

Instructions for any coding agent (Claude Code, Codex, IlmuCode). `README.md` describes the project and
holds the documentation rules (OKF v0.2). `docs/` holds the knowledge. Do not copy README or `docs/`
content into this file.

## Start of a session

1. Read `README.md` and `docs/index.md`.
2. Find the line of the task. Read its open items file: `docs/<line>/<Line>-Open-Items.md`.
   The "Now" section is the current state.
3. Read the line's overview before you change anything in its reference material or code.

## End of a session

1. Update the "Now" section of the open items file. Close finished items with the date and the reason.
2. Add one entry to `docs/log.md` for each change to `docs/` (actor · owner · reason). Your actor is
   `<tool>/<model>`, for example `codex/gpt-5` or `claude-code/claude-opus-5-5`.
3. Add each new document to the `index.md` of its line.
4. Run the checker and fix every FAIL:
   `{{CHECKER_COMMAND}}`

<!-- Delete if there are no commands. Copy commands exactly; do not invent them. -->
## Commands

```powershell
{{EXACT_COMMANDS}}
```

<!-- Delete if the project has no external system. -->
## Key identifiers

Copy these exactly. Do not guess them.

| Name | Value |
|---|---|
| {{NAME}} | `{{VALUE}}` |

## Rules

1. **Do not change files in `{{REFERENCE_PATH}}`** – it is the user's source of truth.
2. **Write facts only from evidence** – cite each source in `sources`. Put what you do not know in the
   open items file as a question.
3. **Never add a `human:` verified entry** for a person who did not confirm the document in this session.
4. **Commit at logical checkpoints** (a finished phase, a verified fix). Never push, force-push or rewrite
   history without an instruction from the user.
{{PROJECT_RULES: add only rules with a real reason, as "N. **Rule** – reason".}}

## Environment

- Windows 11. The default shell is Windows PowerShell 5.1: no `&&` or `||`. Quote paths that have spaces
  or parentheses.
{{ENVIRONMENT_NOTES: for example "This folder syncs with OneDrive. A locked file is a sync lock; wait and
retry." Or "Not a git repository." Delete if none.}}
