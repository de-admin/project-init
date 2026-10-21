# CLAUDE.md – project-init skill

`README.md` describes the project and holds the documentation rules (OKF v0.2). `docs/` holds the
knowledge. This file holds only the procedure for Claude Code sessions. Do not copy README or `docs/`
content into this file.

## Start of a session

1. Read `README.md` and `docs/index.md`.
2. Read `docs/skill/Skill-Open-Items.md`. The "Now" section is the current state.
3. Read `docs/skill/Skill-Overview.md` before you change the skill.

## End of a session

1. Update the "Now" section of the open items file. Close finished items with the date and the reason.
2. Add one entry to `docs/log.md` for each change to `docs/` (actor · owner · reason).
3. Add each new document to the `index.md` of its line.
4. Run the checker and fix every FAIL: `python skill\scripts\check_okf.py docs`

## Commands

```powershell
python tests\test_check_okf.py           # checker tests; compare with Skill-Overview.md section 5
python skill\scripts\check_okf.py docs   # check this project's own bundle
```

## Rules

1. **`skill/` is live.** `~/.claude/skills/project-init` is a junction to it. Every saved edit changes the
   installed skill at once, so keep `skill/` working at each commit.
2. **Keep the four parts consistent.** A change to a feature, a question or a rule must reach every place
   that names it: `SKILL.md` (Step 4 table), `references/features.md`, `references/okf-rules.md`, the
   templates and `check_okf.py`. Feature numbers (F1–F24) and question numbers (Q1–Q12) are never reused.
3. **A template must pass the checker.** After a template change, run the test script; the template
   bundle must show 0 FAIL.
4. **Evidence for a new feature.** Add a feature only with an example from a real project, named in
   `features.md` ("Seen in").
5. **Do not edit the analysed project folders.** The tests and the evidence read them only.

## Environment

- The global preferences in `~/.claude/CLAUDE.md` apply (Windows PowerShell 5.1, commit and push rules).
- Not pushed to any remote.
