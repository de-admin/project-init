---
name: project-init
description: Initialize, adopt or review a project folder with context files that follow the Open Knowledge Format (OKF v0.2) — README.md, CLAUDE.md, optional AGENTS.md, and a docs/ bundle with index.md, log.md, one subfolder per line of work, an overview and an open items tracker. It grills the user to find the project type and the features that fit (session protocol, current-state page, session notes, live files register, context map, decision records, execution plans, checks). Use this when the user says "initialize this project", "set up the folder", "set up the docs context", "start a new study", "add OKF docs", "make a CLAUDE.md for this folder", "add a line", or "review the project setup". Works for small studies (Excel, Power Query, Power Automate, static web apps, often no git) and for code projects with git. Prefer this over the built-in /init when the user wants the OKF docs bundle, not only a CLAUDE.md.
---

# Project initialization (OKF v0.2)

This skill sets up the context files of a project folder. The result is:

- `README.md` – for people and for any tool. It describes the project and holds the documentation rules.
- `CLAUDE.md` – for Claude Code sessions. It holds only the session procedure, commands and hard rules.
- `AGENTS.md` – optional, for other agents (Codex, IlmuCode).
- `docs/` – an OKF v0.2 bundle: the knowledge about the project.

Reference files:

- `references/features.md` – project types, the feature catalogue (F1–F24), the question bank and the
  challenge rules. Read it before Step 2.
- `references/okf-rules.md` – the OKF rules and the house adaptations. Read it before you write in `docs/`.
- `templates/` – the file templates. `scripts/check_okf.py` – the checker.

## Principles (from the analysis of 14 earlier projects)

1. **Fit, not habit.** Each feature costs upkeep. Create a feature only when an answer in Step 2 supports
   it. Record the features that were considered and not chosen, with the trigger that would add them.
2. **One fact in one place.** README owns the description and the doc rules. CLAUDE.md owns the agent
   procedure. `docs/` owns the knowledge. Link to a fact. Do not copy it. (Earlier projects drifted when
   CLAUDE.md, AGENTS.md and README held the same text.)
3. **CLAUDE.md stays short** – about 80 lines or fewer. Current state, task lists and history do not go in
   CLAUDE.md. Current state goes in the "Now" section of the open items file, or in the current-state
   page (F2). History goes in `docs/log.md`.
4. **Do not repeat the global preferences** (`~/.claude/CLAUDE.md`: PowerShell 5.1, commit and push rules).
   Write one line that says they apply. Write a project rule only if it adds to or changes them.
5. **Evidence only.** Each statement about a file, a system or a number comes from something you read.
   Cite it in `sources`. If you do not know, write an open question. Do not guess.
6. **Never overwrite** an existing context file without the user's approval. Never move or change files
   in a reference folder.

## Step 1 – Inspect the folder

Do this before you ask anything. Each fact you find here answers a question that you then do not ask.

1. Confirm the target folder. It is the working directory unless the user names another folder.
2. List the top two levels (skip `node_modules`, `.git`, `.venv`, `.pytest_cache`, `__pycache__`).
3. Find existing context files: `CLAUDE.md`, `AGENTS.md`, `README.md`, `docs/`, `docs/index.md`,
   `docs/INDEX.md`, `docs/log.md`, `docs/Project-Setup.md`, `CHANGELOG.md`, `CURRENT*.md`, `SESSION.md`,
   `LIVE-FILES.md`, `docs/sessions/`, `docs/context/`, `.claude/skills/`.
4. Check for git (`git rev-parse --is-inside-work-tree`) and for a OneDrive or SharePoint path
   (the path contains `OneDrive` or `YTL\`). A synced folder can lock files; note it in CLAUDE.md.
5. Parse the folder name. A study folder has the form `(YYYY.MM.DD) <Initials> - <Topic> - <Tool>`.
   From it, take the start date, the owner initials, the title and the main tool.
6. Find candidate **lines of work**. A line is one separate subject with its own reference material:
   one app, one workflow, one workbook set, one site. Each top-level folder of user-supplied material
   (`reference/`, `Version 5/`, an app folder, a workbook) is a candidate line.
7. Collect the **signals** for Step 2 (see `references/features.md` Part C): scripts, code and tests,
   several versions of one file, old outputs or sample data to compare against, external system
   identifiers, run logs, documents from another team, number of documents, people named in the files.

Then select the mode:

| Mode | When | What you do |
|---|---|---|
| `new` | The folder is empty or holds only reference material | Grill, then create the file set |
| `adopt` | The folder has content but no OKF bundle | Grill, then create the file set around the content. Do not move or rename existing files |
| `extend` | `docs/index.md` with `okf_version` exists, and the user wants to add a line or a document type | Run the checker first, then add. No full grilling |
| `review` | The user asks to review the setup, or a trigger in `docs/Project-Setup.md` has happened | Read `docs/Project-Setup.md`, grill only on the changed facts, then add or retire features |

If the folder has an older docs layout (`docs/context/`, `docs/INDEX.md`, `CURRENT.md`, `docs/sessions/`),
do not convert it in silence. Map each old file to a feature in `references/features.md` Part B, propose
the conversion as a separate step, and ask.

## Step 2 – Grill for fit

The goal: the smallest set of features that this project needs. Use `references/features.md`.

1. **Infer first.** From the Step 1 signals, give each question in Part C a provisional answer. Mark each
   answer as *found* (evidence in the folder) or *guessed*. Turn on the signal-only features.
2. **Round 1 – the type.** One AskUserQuestion call with the questions among Q1–Q4 that are still guessed
   (at most 4; Q1 is multiSelect). Put your inference first, marked "(Recommended)", and say in the option
   description what it turns on. From the answers, select the project type in Part A. If Q1 has more than
   one answer, follow "Mixed deliverables" in Part A.
3. **Round 2 – the open features.** One AskUserQuestion call with at most 4 of the guessed questions among
   Q5–Q12 that the type's defaults do not answer, ranked as Part C "Order" says (at most 2 for a
   `quick-study`). If the user's message did not give the goal, it takes one of the 4 places (offer 2–3
   goals inferred from the material). Questions not asked keep their inferred or default answer.
4. **Challenge.** Apply Part D. If the user asks for a feature with no signal, or declines one with a
   strong signal, push back once in one sentence. Use a Round 3 only for the challenges and conflicts.
   Never more than 3 rounds.

Owner: use the initials from the folder name as `human:<initials>` (for example `human:SW`). If the folder
name has no initials and the user does not say, write `owner:unattributed`.

## Step 3 – Show the fit and the plan (one confirmation)

Before you write any file, show both of these in one message, and ask the user once to confirm or change:

1. **The fit table.** The type, then each feature that is **on** or **later (trigger)**, and each feature
   that the user asked about or that has a signal, with the answer that decided it. Close with one line:
   "All other features: off, no signal." Include the answers that were not asked (inferred or default),
   so the user can correct them.
2. **The plan.** A short tree of the files you will create and the files you will leave alone. For each
   existing `CLAUDE.md`, `AGENTS.md` or `README.md`, say what you will do: keep, add a section, or replace.

After the confirmation, you can create the new files without a further question. Ask again only before
you replace or edit an existing context file, if the plan did not name that change.

## Step 4 – Write the files

Use the templates in `templates/`. Replace every `{{...}}` placeholder. Delete a template section that does
not apply, and delete the `<!-- -->` instruction comments. Do not leave an empty heading or a placeholder.

Placeholders that need a definition:

| Placeholder | Value |
|---|---|
| `{{REFERENCE_PATH}}` | Path of the line's reference material, relative to the **project root** (`Version 5/Version 5/`) |
| `{{RELATIVE_PATH_TO_REFERENCE}}`, `{{RELATIVE_PATH_TO_FILE}}` | The same kind of path, relative to the **concept file** (`../../Version 5/Version 5/`). Use relative paths, not `/`-rooted paths, for files outside `docs/` |
| `{{TEAM}}` | From the folder path (`Digital Engineering (SPYTL)`, `Data Team (SPYTL)`), or ask |
| `{{MODEL_ID}}` | The model ID of this session, for example `claude-opus-5-5` |
| `{{CHECKER_COMMAND}}` | `python "$env:USERPROFILE\.claude\skills\project-init\scripts\check_okf.py" docs` when the skill is installed for the user; otherwise the real path of `scripts/check_okf.py` |
| `{{N}}`, `{{TOTAL}}` | The number of the line, and the number of lines |

For more than one line, repeat the line section in `docs/index.md` and the row in the README table.

### Core file set (every project)

```
<project>/
├── README.md                     templates/README.md
├── CLAUDE.md                     templates/CLAUDE.md
└── docs/                         OKF v0.2 bundle
    ├── index.md                  templates/docs-index.md     (root: okf_version only)
    ├── log.md                    templates/docs-log.md
    ├── Project-Setup.md          templates/Project-Setup.md  (type: decision – the fit from Step 2)
    └── <line-slug>/              one folder for each line
        ├── index.md              templates/line-index.md
        ├── <Line>-Overview.md    templates/Overview.md       (type: overview)
        └── <Line>-Open-Items.md  templates/Open-Items.md     (type: open-items)
```

- A project with **one line** still gets a line folder. A second line is then easy to add.
- `<line-slug>` is lowercase with hyphens (`worksheet-kpi`). `<Line>` in file names is Title-Case with
  hyphens (`Worksheet-KPI`). The prefix keeps file names unique when files are shared or exported.
- Write the overview from the reference material: purpose, how it works, data and storage, inputs and
  outputs, and numbers you can show from the source. Cite each source.
- Seed the open items file with real questions and gaps that you found. Do not invent filler questions.
- Write `docs/Project-Setup.md` from the confirmed fit table: the type, the answers, the features in the
  table, the line "All other features: off, no signal", and the triggers. Because the user confirmed this
  content in this session, add `verified: { by: human:<owner>, at: <now> }` and set `status: stable`. If
  the user changed the table without a final confirmation, keep `status: draft` and no `verified`.

### Features that are on

For each feature that is **on**, create what `references/features.md` Part B says, at the path it gives.
Create a folder only when its first file exists (for example `decisions/` with the first decision), except
`reference/`, `output/` and `reports/`, which the user fills. Add each feature's rule to the right place:

| Feature | Goes in |
|---|---|
| Feature | Create | Add to |
|---|---|---|
| F1 session protocol | – | `CLAUDE.md` "Start of a session" / "End of a session" (in the template) |
| F2 current-state page | `docs/Current-State.md` | Root `index.md`; start of a session: "Read it"; end: "Rewrite it, move `stale_after`" |
| F3 session notes | the first note, when the first session ends | Line `index.md`; end of a session: "Write a session note" |
| F4 live files register | `docs/<line>/<Line>-Live-Files.md` | Line `index.md`; start of a session: "Read it before you edit a file" |
| F5 context map | topical subfolders under `docs/<line>/`, each with an `index.md` | `CLAUDE.md` "Quick load" table: session type → files to read first |
| F6 key identifiers | – | `CLAUDE.md` "Key identifiers" |
| F7 decision records | `decisions/` with the first decision | Line `index.md` |
| F8 lessons learnt | `docs/lessons/` with the first lesson | Root `index.md`; end of a phase: "Write a lesson" |
| F9 execution plans | `plans/` with the first plan | Line `index.md`; `CLAUDE.md`: plan location, "update the plan Status at the end of a session" |
| F10 release changelog | `CHANGELOG.md` at the project root | `CLAUDE.md`: "update it for each change that users see" |
| F11 reports | `reports/` | README "Folder conventions" (SYTL-RPT names) |
| F12 handover and guides | `<Line>-Handover.md` when a handover is planned | Line `index.md` |
| F13 checks | see below | Line `index.md` |
| F14 multi-person | – | Roles table in `README.md`; owner policy line in `docs/log.md` |
| F15 AGENTS.md | see below | – |
| F16–F19 folders | the folders | README "Folder conventions" |
| F20 git | `git init`, a `.gitignore` for the tool | Commit after Step 5 |
| F21 project skills | `.claude/skills/<name>/SKILL.md` when the procedure is known | `CLAUDE.md`: one line for each skill and when to use it |
| F22 ground truth | `fixtures/<line>/`, `docs/<line>/<Line>-Acceptance-Values.md` | Line `index.md`; README rule: fixtures are read-only after capture |
| F23 external documents | `reference/upstream/<party>/` (a) or `docs/<line>/<Line>-Shared-Docs.md` (b, c) | README rule: upstream docs outrank `docs/`; end of a session: "Sync each changed shared document" |
| F24 run evidence | `runs/` | `CLAUDE.md` rule: every run leaves a record in `runs/YYMMDD - <name>/` |

For tested code (Q10), copy the exact install, run and test commands from the package files into
`CLAUDE.md` "Commands", and add the test command to run before a commit. If the repository has a remote,
add the rule: merge to `main` only through a PR.

**AGENTS.md (F15)** – write the agent procedure in `AGENTS.md` (templates/AGENTS.md) instead of
`CLAUDE.md`. Then `CLAUDE.md` holds only the import line and the Claude-only lines:

```markdown
@AGENTS.md

## Claude Code only

- The global preferences in `~/.claude/CLAUDE.md` apply.
```

One source, no drift.

**Checks (F13)** – `docs/<line>/checks/check-<subject>.py`. One script for each spec. It recomputes the
acceptance values, prints one PASS or FAIL line for each check, then a JSON receipt (script hash, input
hashes, parameters, verdict). The receipt is printed, not stored in `docs/`. Describe each check in a
concept with `type: Attested Computation` (see `references/okf-rules.md`).

## Step 5 – Check

Run the checker on the bundle and fix every FAIL:

```bash
python "<skill-dir>/scripts/check_okf.py" docs
```

`<skill-dir>` is the folder of this SKILL.md. Fix WARN lines when the fix is clear. Report the others.
The checker uses PyYAML when it is installed. Without it, the frontmatter checks are approximate.

## Step 6 – Log and report

1. Add the initialization entry to `docs/log.md` (the template has it). Actor: `claude-code/<model-id>`.
   Owner: from Step 2. Reason: the user's request in a few words.
2. If the folder is a git repository, commit the new files as one commit (`docs: initialize OKF context
   files`), following the global commit rules. Do not push.
3. Tell the user: the type, the features on and the triggers for later, the tree that you created, the
   open questions that you seeded, and the checker result.

## Mode `extend`

Add a line:

1. Create `docs/<slug>/` with `index.md`, `<Line>-Overview.md` and `<Line>-Open-Items.md`.
2. Add a section for the line to `docs/index.md`.
3. Add a row to the "Lines of work" table in `README.md`.
4. If this is the second line, check the trigger for F2 (current-state page) in `docs/Project-Setup.md`.
5. Add a `log.md` entry. Run the checker.

Add a document type or a single feature (for example the first decision record):

1. Find the feature in `references/features.md` Part B. If it is "off" in `docs/Project-Setup.md`, this is a
   change of setup: use mode `review` instead.
2. Create the file and the places to add it from the Step 4 table.
3. Add a `log.md` entry. Run the checker.

## Mode `review` – change the features

1. Read `docs/Project-Setup.md`. List the triggers that have happened, with the evidence.
2. Ask only the questions in `references/features.md` Part C whose answers changed. Apply Part D.
3. Show the new fit table (changes only). After the user confirms, add the new features and retire the
   unused ones. To retire a document in `docs/`, set `status: deprecated`; do not delete it. To retire a
   rule in `CLAUDE.md` or a root file (for example `CHANGELOG.md`), remove the section, and record the
   removal in `log.md` and `Project-Setup.md`.
4. Update `docs/Project-Setup.md` (a new dated section; keep the old one), add a `log.md` entry, and run
   the checker.

## Writing style

- Follow the output style of the session. This user uses ASD-STE100 Simplified Technical English: short
  sentences, active voice, one word for one meaning, "must" for a requirement.
- Dates in prose: `DD/MM/YYYY`. Timestamps in frontmatter: ISO 8601 with the offset
  (`2026-10-21T10:00:00+08:00`). Log headings: the date only (`## 2026-10-21`).
- Expand each abbreviation at its first use in a document.

Intentional differences from the Worksheet Improvements bundle (the first hand-made example): the open
items file has a "Now" section and a "Closed" section; the README has a "Goals" section; the overview uses
`type: overview`, not `type: app-overview`; the bundle has a `Project-Setup.md` record.
