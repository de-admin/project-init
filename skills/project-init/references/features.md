# Project types, features and the grilling question bank

This file supports Step 2 (grilling) of SKILL.md. Part A names the project types. Part B lists every
feature that earlier projects used, with the signals that make it fit and how it maps to OKF. Part C is
the question bank. Part D is the challenge rules. Part E is the triggers for a later review.

## Part A – Project types

A type is a starting set of features and a set of default answers. The grilling then adds or removes
features one by one. A type is not a rule: the final set is what the answers support.

| Type | Typical project | Starting features | Default answers (not asked unless a signal disagrees) | Seen in |
|---|---|---|---|---|
| `quick-study` | One person, days to a few weeks, one analysis or one workbook; deliverable is a finding, a workbook or a report | Core, F1, F16, F17 | Q6 no · Q9 no · Q10 no · Q12 no | KPI ScoreCard, Non-design KPI Consolidation |
| `tool-study` | One person builds a tool that runs in an external system (Power Automate, n8n, Power Query, PowerShell); many sessions | Core, F1, F4, F6, F18, F24 | Q5 yes · Q6 yes · Q9 no | SP Automation, HR KPI Tracker, Water Rain, Excel Protection |
| `team-study` | More than one person or role; results are checked by others; accuracy must be shown | Core, F1, F7, F12, F13, F14, F22 | Q3 others · Q4 exact | Voon Water Engineering (FPF) |
| `app` | Code with tests, git, users and releases; months of work in phases | Core, F1, F7, F8, F9, F10, F20, F22 | Q2 months · Q5 no (git keeps versions) · Q10 yes | Manhour POC v3, DocuScan, Orchestra |
| `doc-study` | The deliverable is documentation of something that already exists | Core, F1, F16 | Q5 no · Q6 no · Q10 no | Worksheet Improvements |

**Mixed deliverables.** Q1 allows more than one answer (for example documentation of a workbook and a new
prototype). Make each deliverable its own line. Select the type of the main deliverable, and add the
features of the other deliverables one by one. A runnable prototype is a line with its own folder at the
project root (for example `prototype/`), not a folder inside `docs/`.

## Part B – Feature catalogue

Each feature has: what it is, the signals that make it fit, the cost, and where it goes in an OKF project.
"Core" features are always on and are not asked about.

### Core (always on)

| Feature | Files |
|---|---|
| Project description and doc rules | `README.md` |
| Agent procedure | `CLAUDE.md` |
| OKF bundle root | `docs/index.md`, `docs/log.md` |
| One folder per line | `docs/<line>/index.md`, `<Line>-Overview.md`, `<Line>-Open-Items.md` |
| Current state, short form | The "Now" section of each open items file |
| Setup record | `docs/Project-Setup.md` – the answers of the grilling and the features chosen (templates/Project-Setup.md) |
| Checker | `tools/check_okf.py` – a copy of the skill's checker |

### Continuity – resume work across sessions

**F1. Session protocol** – a start-of-session and end-of-session checklist in `CLAUDE.md`.
- Fits: more than one session. On in every type; turn off only when Q2 = one session.
- Cost: none.
- OKF: not in `docs/` (agent procedure).

**F2. Current-state page** – one page that says where the whole project is: goal, state of each line,
task in flight, what is paused. Replaces `CURRENT.md` / `CURRENT-TASK.md`.
- Fits: two or more lines, so one "Now" section per line does not show the whole picture; or a task in
  flight with acceptance checks that spans many sessions.
- Does not fit: one line – the "Now" section is enough.
- Cost: must be rewritten at the end of each session, or it misleads.
- OKF: `docs/Current-State.md` (templates/Current-State.md), `type: status`, with `stale_after` set 14 days
  ahead. The checker warns when it is stale. Rewrite it in place; history goes in `log.md`.

**F3. Session notes** – one note for each working session: what was tried, what was found, where it
stopped. Replaces `docs/sessions/` and `SESSION.md`.
- Fits: long investigations where the path matters (why an approach failed); work that one person hands
  to another between sessions.
- Does not fit: most projects – `log.md` and the open items file hold enough.
- Cost: high. Notes grow fast and are rarely read again.
- OKF: `docs/<line>/sessions/YYMMDD-<slug>.md`, `type: session-note`, append-only.

**F4. Live files register** – a table of the authoritative version of each artifact, and which files are
superseded. From `LIVE-FILES.md`.
- Fits: several versions of the same artifact exist side by side (`-v1`..`-v4`, flow package zips,
  `Version 5`); an agent could edit the wrong one.
- Cost: must be updated when a file is added, replaced or retired.
- OKF: `docs/<line>/<Line>-Live-Files.md`, `type: register`. Columns: artifact, live file, superseded files,
  since (date).

### Knowledge structure

**F5. Context map** – topical subfolders in a line (for example `foundation/`, `features/`, `delivery/`) and
a quick-load table in `CLAUDE.md`: session type → files to read first. From `docs/context/` with C1–C5 or
D1–D5 codes.
- Fits: more than about 15 documents in one line; different kinds of sessions need different files.
- Does not fit: small projects – the line `index.md` is the map. Extracted files (`.pq`, `.json`) are not
  documents and do not count.
- Cost: the table in `CLAUDE.md` must follow the folders.
- OKF: subfolders under `docs/<line>/`, each with its own `index.md`. No phase codes in file names;
  the folder name says the topic.

**F6. Key identifiers** – a table of exact values: site URLs, list GUIDs, connection names, workflow IDs.
- Fits: the work touches an external system; a wrong guess breaks something.
- Cost: low.
- OKF: the values go in `CLAUDE.md` "Key identifiers" (agents need them at once). If other tools also need
  them, put them in `docs/<line>/<Line>-Identifiers.md`, `type: reference-note`, and link from `CLAUDE.md`.

**F7. Decision records** – one file for each decision, kept when reversed.
- Fits: choices that people will question later; more than one person; parameters with a reason.
- Cost: low, if a record is written only for decisions that someone could reverse.
- OKF: `docs/<line>/decisions/<Question-Named>.md`, `type: decision` (templates/Decision.md).

**F8. Lessons learnt** – dated retrospective notes, append-only, for the whole project.
- Fits: long projects (months); a team that repeats similar projects.
- Cost: low; needs a habit at the end of each phase.
- OKF: `docs/lessons/YYMMDD-<slug>.md` (bundle root, not per line), `type: lesson`.

### Delivery

**F9. Execution plans** – a plan with phases and acceptance checks for each larger piece of work.
- Fits: work in phases over many sessions; work that sub-agents do in parallel.
- Cost: medium. A plan that is not updated is worse than none.
- OKF: `docs/<line>/plans/YYMMDD-<slug>.md`, `type: plan`. Its "Status" section is the resume point (it
  replaces a separate `STATE.md`). Reports and audits of a phase: `type: report` in the same folder.

**F10. Release changelog** – a user-facing list of changes for each release. Different from `docs/log.md`,
which records changes to the documentation.
- Fits: an app with users and versions.
- OKF: `CHANGELOG.md` at the project root, outside the bundle (it describes the product, not the docs).

**F11. Reports** – Word or PDF reports with SYTL-RPT codes.
- Fits: the deliverable is a report for management or another department.
- OKF: the `.docx`/`.pdf` in `reports/` at the project root. The report's content in markdown, if kept, is
  a concept: `docs/<line>/reports/<Name>.md`, `type: report`.

**F12. Handover and operator guides** – the entry point for a person who joins or takes over, and the
runbooks for a person who operates or deploys the result.
- Fits: more than one person; the project will be handed to a builder, an operator or another team.
- OKF: `docs/<line>/<Line>-Handover.md` and `docs/<line>/guides/<Task>.md`, `type: guide`. A guide that is
  also given to people outside the team is an external document too (F23).

### Trust

**F13. Checks** – check-value scripts with printed receipts.
- Fits: numbers must be exact and someone else must be able to confirm them.
- Cost: medium; one script for each spec.
- OKF: `docs/<line>/checks/`, `type: Attested Computation` (see okf-rules.md).

**F14. Multi-person rules** – roles in the README, the strict owner policy in `log.md`, `human:` IDs for
each person.
- Fits: more than one person edits or approves `docs/`. Not needed when others only answer questions
  (the Voon pilot logged `owner:unattributed` on most entries and ran well).

**F15. AGENTS.md** – the agent procedure in a file that other agents read.
- Fits: Codex, IlmuCode or another agent will work in the folder.

**F22. Ground truth and acceptance values** – known correct results to compare against: old outputs, a
sample CSV, fixtures, the acceptance values of a spec.
- Fits: the work replaces or rebuilds something that already gives results; a change must not alter the
  numbers. Seen in KPI ScoreCard (450-row comparison CSV), Voon (acceptance values, 36/36), DocuScan
  (fixtures).
- Cost: low; the data must be stored once and never edited.
- OKF: the data files in `fixtures/<line>/` at the project root, read-only after capture. One concept that
  lists them: `docs/<line>/<Line>-Acceptance-Values.md`, `type: register` (file, what it proves, how it was
  captured, date). F13 checks read from it.

### External material

**F23. External documents** – documents that come from or go to another party, or that live outside the
folder.
- Fits: (a) another team's documents that outrank ours ("where it disagrees with our docs, they are
  right"); (b) a living document that is shared online, with a local copy or export to keep the same;
  (c) a guide given to operators outside the team.
- Cost: low for (a); medium for (b), because each change must be synced.
- OKF: (a) verbatim copies in `reference/upstream/<party>/`, read-only, with a README rule that they
  outrank `docs/`. (b) and (c): a register `docs/<line>/<Line>-Shared-Docs.md`, `type: register`, with
  columns: document, where it lives (URL), local copy, sync rule, last synced (date).

**F24. Run evidence** – a lasting record of each run in an external system: logs, CSV results, the
summary email.
- Fits: the tool runs outside the folder (Power Automate, n8n) and each run changes something real.
- OKF: `runs/YYMMDD - <name>/` at the project root, outside the bundle. A rule in `CLAUDE.md`: every run
  leaves a record. Findings from a run go in a `type: report` concept that links to the run folder.

### Folders and tools

| Feature | Fits when | Rule |
|---|---|---|
| F16. `reference/` | The user supplies source material | Read-only |
| F17. `output/` | The project generates files | `output/<yyyy-mm-dd>/<name>_r<N>.<ext>` |
| F18. `_archive/` | Retired versions must be kept | Do not edit |
| F19. `tools/` | Extract or generate scripts exist or are planned | Document each script in the overview. (`tools/` always exists for the checker copy; F19 means the project's own scripts) |
| F20. Git | Code, or a need to undo changes | `git init`, `.gitignore`; commit rules from the global preferences |
| F21. Project skills | A task repeats in this project and needs its own procedure | `.claude/skills/<name>/SKILL.md`. Mirror to `docs/skills/` only if git must track the skills and `.claude/` is ignored |

## Part C – Question bank

Ask only questions whose answer you cannot get from the folder or from the type's defaults. Each answer
turns features on or off. Offer the choices as AskUserQuestion options, with your inference first and
marked "(Recommended)". Q1 is `multiSelect`.

| # | Question | Choices → features |
|---|---|---|
| Q1 | What will the project deliver? (select all) | finding or workbook → F16, F17 · tool in an external system → F4, F6, F18, F24 · app with users → F9, F10, F20 · report → F11 · documentation of something that exists → F16 · prototype → a separate line, F19 |
| Q2 | How long will the project run, and in how many sessions? | one session → F1 off · days or weeks → (core, F1) · months in phases → F8, F9 |
| Q3 | Who works in it? | only me → – · others answer questions → F12 · others edit or approve → F12, F14 · other agents too → F15 |
| Q4 | Will someone else check or rely on the numbers? | no → – · yes, a person reviews → F7 · yes, they must be exact and repeatable → F7, F13, F22 |
| Q5 | Will there be several versions of the same file at the same time? | no → – · yes → F4, F18 |
| Q6 | Does the work change an external system (SharePoint, Power Automate, n8n, a database)? | no → – · yes → F6 · yes, and each run must leave a record → F6, F24 |
| Q7 | How many separate subjects (lines) are there? | one → – · two or more → F2 |
| Q8 | When you return after a break, what do you need first? | the next step → (core "Now") · the whole picture → F2 · what I tried and why it failed → F3 |
| Q9 | Do you expect more than about 15 documents in one line? | no → – · yes → F5 |
| Q10 | Is there code? | no → – · scripts that extract or generate → F19 · code that must be tested before each change → F19, F20, test command in `CLAUDE.md` |
| Q11 | Is there a known correct result to compare against (an old output, sample data, a fixture)? | no → – · yes → F22 |
| Q12 | Does any document come from another team, or live outside this folder (online, shared)? | no → – · another team's docs that outrank ours → F23 (a) · a shared online document → F23 (b) |

**Signal-only features** – turned on by Step 1 signals, not by a question: F16 (reference material found),
F17 (generated files found), F18 (old versions found), F19 (scripts found), F21 (the user asks for a
project skill, or the same procedure is repeated in the folder's notes).

**Order and the 4-question limit.** AskUserQuestion takes at most 4 questions in one call.
1. Round 1: the guessed questions among Q1–Q4 (at most 4). They decide the type.
2. Round 2: the guessed questions among Q5–Q12 that the type's defaults do not answer. Rank them by the
   number of features they can change, and ask the top 4. For a `quick-study`, ask at most 2.
3. Questions that are not asked keep the inferred or default answer. They appear in the fit table, where
   the user can change them.
4. Round 3: only for challenges and conflicts (Part D).

Worst case: 12 questions in 3 rounds. Typical `quick-study`: 4 to 6 questions in 2 rounds.

## Part D – Challenge rules (the "grilling")

The goal is the smallest set of features that the project needs. Push back in both directions, once for
each feature, then accept the user's answer.

1. **A feature with no signal.** If the user asks for a feature that no answer supports, ask what problem
   it solves here. Example: "Session notes cost a note for each session. What do you need from them that
   `log.md` and the open items file do not give?" If there is no answer, leave the feature out and record
   it as "considered, not chosen".
2. **A missing feature with a strong signal.** If an answer strongly supports a feature that the user
   declines, state the risk in one sentence. Example: "Three versions of the flow package exist. Without a
   live files register, an agent can edit the old one." Then accept the user's decision.
3. **Conflicting answers.** If two answers conflict (for example "only me" and "the builders will take it
   over"), ask which one is true now and which one is later. Features for "later" are recorded as
   triggers, not created.
4. **Vague answers.** "Maybe" or "not sure" is a "no" now, recorded with a trigger: "add F7 when the first
   decision is questioned".
5. **Stop rule.** Stop after 3 rounds of questions, or when every feature in Part B is decided. Do not ask
   about core features.

## Part E – Triggers for a later review

Record the triggers that apply in `docs/Project-Setup.md`. When one happens, run the skill in mode
`review`.

- A second person or another agent starts to work in the folder → F12, F14, F15.
- A second line starts → F2.
- A second version of an artifact appears next to the first → F4.
- A number is questioned, or a decision is reversed → F7, F13, F22.
- A line passes about 15 documents → F5.
- Another team sends documents, or a document is shared online → F23.
- The tool starts to run in production → F24.
- The work moves from a study to a product with users → type `app`.
