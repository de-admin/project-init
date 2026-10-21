# {{TITLE}}

{{ONE_PARAGRAPH: what the project is, who it is for, and what it delivers.}}

Started {{DD/MM/YYYY}} by {{OWNER_INITIALS}} ({{TEAM}}).

## Goals

1. {{GOAL_1}}
2. {{GOAL_2}}

## Lines of work

Each line is one separate subject, with its own reference material and its own documentation.

| Line | Subject | Reference | Documentation |
|---|---|---|---|
| 1 | **{{LINE_TITLE}}** – {{ONE_LINE_DESCRIPTION}} | [`{{REFERENCE_PATH}}`](<{{REFERENCE_PATH}}>) | [`docs/{{LINE_SLUG}}/`](docs/{{LINE_SLUG}}/) |

<!-- Multi-person only: delete this section otherwise. -->
## People and roles

| ID | Role |
|---|---|
| `human:{{OWNER_INITIALS}}` | {{ROLE}} |

<!-- Delete this section if there is nothing to run. -->
## How to run

{{EXACT_STEPS_OR_COMMANDS}}

## Folder layout

```
{{FOLDER_NAME}}/
├── README.md        this file
├── CLAUDE.md        procedure for Claude Code sessions
├── {{REFERENCE_PATH}}   line 1 reference material (read-only)
└── docs/            documentation bundle (OKF v0.2)
    ├── index.md     root index: the lines
    ├── log.md       change log
    └── {{LINE_SLUG}}/
        ├── index.md
        ├── {{LINE_FILE}}-Overview.md
        └── {{LINE_FILE}}-Open-Items.md
```

<!-- Keep only the rows for folders that exist. -->
## Folder conventions

- `reference/` holds the source material from the user. Do not change, move or rename a file in it.
- `output/<yyyy-mm-dd>/<name>_r<N>.<ext>` holds generated files. A new revision gets a new `_r<N>`.
- `reports/` holds Word or PDF reports, named with the SYTL-RPT document code.
- `_archive/` holds retired versions. Do not edit a file in it.
- `reference/upstream/<party>/` holds verbatim documents from another team. Where they disagree with
  `docs/`, they are right.
- `fixtures/<line>/` holds known correct results (old outputs, sample data). Read-only after capture.
- `runs/YYMMDD - <name>/` holds the record of each run in an external system (logs, CSV results, summary).

## Documentation rules (OKF)

The `docs/` folder follows the Open Knowledge Format (OKF), spec v0.2:
<https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md>

1. `index.md` and `log.md` are reserved names. Do not use them for a document.
2. Only the root `docs/index.md` has frontmatter, and it holds only `okf_version: "0.2"`. Each other
   `index.md` is a list of bullets: `* [Title](link) - description`.
3. Every other `.md` file in `docs/` starts with YAML frontmatter. `type` is required. Also give `title`,
   `description`, `sources`, `generated` (`by`, `at`) and, for a draft, `status: draft`.
4. When a person reviews a document, add a `verified` entry `{ by: human:<id>, at: <ISO time with offset> }`
   and set `status: stable`. A document with no `verified` key is unverified. An agent never adds a
   `human:` entry for a person who did not confirm.
5. Each change to `docs/` gets one entry in `docs/log.md`, newest first, with actor, owner and reason.
   If the owner is not known, write `owner:unattributed`. Do not guess an owner.
6. Put a document in the folder of its line, and add it to that line's `index.md`. Put open questions,
   unfinished work and the current state in the line's open items file, not in a new file.
7. A new line gets its own subfolder in `docs/`, a section in `docs/index.md` and a row in the table above.
8. A reversed decision is not deleted. Set `status: deprecated` and link to the new decision.
