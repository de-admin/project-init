# OKF v0.2 rules and house adaptations

Source: Open Knowledge Format, spec v0.2 (Google Cloud Platform),
<https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md>. Summary read on 21/10/2026.
Part A is the spec. Part B is what this team adds. Part B never breaks Part A.

## Part A – the spec

### Bundle

- A bundle is a folder tree of UTF-8 markdown files. Here, the bundle is `docs/`.
- `index.md` and `log.md` are **reserved names** at every level. They must not be used for a document.
- Every other `.md` file is a **concept**. Its concept ID is its path in the bundle without `.md`.
- A file that is not `.md` (HTML, PNG, PY, XLSX) can sit in the bundle. It is not a concept. Link to it
  from a concept.

### Concept frontmatter

A YAML block between two `---` lines at the top of the file. Then a markdown body.

| Key | Need | Notes |
|---|---|---|
| `type` | **Required** | Non-empty string. The only key that is always required |
| `title` | Recommended | Display name |
| `description` | Recommended | One sentence |
| `resource` | Recommended | Path or URL of the thing the concept describes. Omit for an abstract concept |
| `tags` | Recommended | List of short strings |
| `sources` | Optional | List of `{ resource (required), id, title, author, last_modified, usage_count }` |
| `generated` | Optional | `{ by (required), at }`. `at` = the last meaningful change |
| `verified` | Optional | List of `{ by, at }`. A bare mapping counts as a list of one |
| `status` | Optional | `draft`, `stable` or `deprecated`. Absent = `stable` |
| `stale_after` | Optional | ISO 8601 instant. The concept is stale when now ≥ this time |

- Extra keys are allowed. Tools must keep unknown keys and must not reject a file because of them.
- Timestamps are ISO 8601 with an offset: `2026-10-21T10:00:00+08:00`.
- To cite a source for one statement, use a footnote whose label is the `sources[].id`:
  `... 1,686 lines[^js]` and `[^js]: script.js`.

### Trust tiers (derived from `verified`)

1. **Unverified** – no `verified` key.
2. **Machine-confirmed** – `verified` holds only actors that do not start with `human:`.
3. **Human-reviewed** – `verified` holds at least one `human:<id>` actor.

### Actors

- Agent or tool: `<producer>/<version>` – for example `claude-code/claude-opus-5-5`.
- Person: `human:<id>` – for example `human:SW`.
- Automated process: `process:<id>` – for example `process:nightly-refresh`.

### Links

- Normal markdown links. Bundle-absolute (`/design-database/index.md`) or relative (`./other.md`).
- A broken link must not make a tool reject the bundle.
- House rule: a `/`-rooted path means the bundle root (`docs/`), not the project root. For a file outside
  `docs/` (reference material, code), use a relative path such as `../../reference/book.xlsx`.

### index.md

- No frontmatter. Exception: the root `docs/index.md` can have `okf_version: "0.2"`, and nothing else.
- Body: `#` or `##` headings, each followed by bullets: `* [Title](link) - description`.

### log.md

- Date headings `## YYYY-MM-DD`, newest first. Entries are prose bullets. The log is a flat list: every
  `##` heading must be a date. Put the explanation of the log above the first date heading, as prose.
- A bold keyword at the start is the convention: `**Creation**`, `**Update**`, `**Deprecation**`.

### Attested Computation (`type: Attested Computation`)

A concept that names a sanctioned computation that an agent must run, not write.
Keys: `runtime` (required, for example `python`), `parameters` (list of `{ name, type, required }`),
`computation` (path to the script, or a `# Computation` fenced block in the body),
`executor: { resource, receipt }` (`receipt` = the fields a run must return),
`attester: { resource }` (deterministic code, no LLM).
An agent can supply parameter values only. It must not edit the computation. Receipts are runtime
output and are not stored in the bundle.

Example (`docs/<line>/checks/Check-Rainfall.md`):

```yaml
---
type: Attested Computation
title: Rainfall check values
description: Recomputes the rainfall acceptance values from the site workbook and prints a receipt
runtime: python
computation: check-rainfall.py
parameters:
  - { name: site, type: string, required: true }
executor:
  resource: check-rainfall.py
  receipt: [script_hash, input_hashes, parameters, verdict]
attester:
  resource: check-rainfall.py
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-10-21T10:00:00+08:00
---
```

### Bundle conformance

1. Every non-reserved `.md` file has frontmatter that YAML can parse.
2. Every frontmatter has a non-empty `type`.
3. `index.md` and `log.md` follow the rules above.

## Part B – house adaptations

These come from the Voon Water Engineering pilot (agreed 08/10/2026) and the Worksheet Improvements
bundle (21/10/2026).

1. **Root index declares the version.** `docs/index.md` has `okf_version: "0.2"`. The name is lowercase
   `index.md`, not `INDEX.md`.
2. **Full frontmatter on every concept.** Give `type`, `title`, `description`, `sources` and `generated`.
   Give `status: draft` to every document that an agent writes and no person has reviewed.
3. **`verified` is for real reviews only.** An agent never writes a `human:` verified entry for a person
   who did not confirm the document in that session. When the person confirms, add
   `{ by: human:<id>, at: <now> }` and change `status` to `stable`. No `verified` key = unverified.
   Do not write `verified: []`.
4. **Log entry format.** Each change to `docs/` gets one bullet under today's date heading:

   ```
   - **Update** — <what changed, which files> 
     actor:<actor> · owner:<actor or owner:unattributed> · reason: <why, in a few words>
   ```

   The owner is the person accountable for the change. Do not guess an owner. If it is not known, write
   `owner:unattributed`. When only the date of an event is known, use midnight of that date.
5. **Lines of work.** Each line has its own folder in `docs/` with `index.md`, an overview and an open
   items file. Put a document in the folder of its line and list it in that line's `index.md`.
6. **Open items, not new files.** Open questions, gaps, pending decisions and the current state go in
   the open items file of the line. Mark an item `[x]` when it closes, with the date and the reason.
   Never reuse an item number.
7. **Decisions are not deleted.** When a decision is reversed, set `status: deprecated` on the old record,
   link it to the new record, and keep the file.
8. **Rules live in README.md.** The documentation rules go in the project `README.md`, so that tools other
   than Claude Code read them. `CLAUDE.md` links to them and does not copy them.
9. **Machine-checkable accuracy.** When numbers must be exact, write a check script and an
   `Attested Computation` concept (see Part A). A check that passes in a session can be recorded as a
   machine-confirmed `verified` entry with the actor `process:<script-name>`.

## Type vocabulary

Use these `type` values so that documents stay consistent across projects. Add a new value only when
none of these fits, and add it to this list.

| `type` | Use for |
|---|---|
| `overview` | What a line is, how it works, how it is built. Put the kind of subject in `tags` (`web-app`, `workbook`, `flow`). The Worksheet Improvements bundle used `app-overview`; new bundles use `overview` |
| `open-items` | The tracker of a line: Now, questions, gaps, decisions pending, closed items |
| `decision` | One decision record |
| `spec` | A specification of a step, a calculation or a workflow |
| `report` | An analysis or a finding at one point in time |
| `plan` | An execution plan with phases |
| `guide` | How to do a task (run, deploy, restore, hand over) |
| `reference-note` | Notes on an external system, a data source or a standard |
| `Attested Computation` | A sanctioned check script (spec-defined type; keep this exact spelling) |
| `status` | The current-state page (feature F2). Always has `stale_after` |
| `session-note` | One working session: what was tried, found, and where it stopped (feature F3) |
| `register` | A table that is kept current, for example the live files register (feature F4) |
| `lesson` | A dated retrospective note (feature F8) |

Every type uses the common frontmatter (`type`, `title`, `description`, `status`, `tags`, `sources`,
`generated`) from `templates/Overview.md`. The body shapes that have no template:

- `plan` – file `plans/YYMMDD-<slug>.md`. Sections: Goal, Phases (a numbered list, each with its acceptance
  check), Status (one line for each phase: not started, in progress, done on DD/MM/YYYY), Risks.
- `spec` – sections: Purpose, Inputs, Steps or Formula, Outputs, Acceptance checks (with the expected values).
- `report` – sections: Question, Method, Findings (each with its source footnote), Conclusion.
- `guide` – sections: When to use, Before you start, Steps (numbered), Check the result.
- `reference-note` – sections: What it is, Identifiers, How this project uses it, Limits.
- `status` – use `templates/Current-State.md`.
- `session-note` – file `sessions/YYMMDD-<slug>.md`. Sections: Goal of the session, What was tried, What
  was found, Where it stopped. Append-only: do not edit an old note.
- `register` – one table with a "since" date column, and a sentence that says when to update it.
- `lesson` – file `lessons/YYMMDD-<slug>.md`. Sections: What happened, Why, What to do next time.
