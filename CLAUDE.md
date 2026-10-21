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
4. Run the checker and fix every FAIL: `python skills\project-init\scripts\check_okf.py docs`

## Commands

```powershell
python tests\test_check_okf.py                          # checker tests; compare with Skill-Overview.md section 5
python skills\project-init\scripts\check_okf.py docs    # check this project's own bundle
claude plugin validate .                                # check the plugin manifest
```

## Rules

1. **`skills/project-init/` is live.** On this machine, `~/.claude/skills/project-init` is a junction to it.
   Every saved edit changes the installed skill at once, so keep it working at each commit.
2. **Keep the four parts consistent.** A change to a feature, a question or a rule must reach every place
   that names it: `SKILL.md` (Step 4 table), `references/features.md`, `references/okf-rules.md`, the
   templates and `check_okf.py`. Feature numbers (F1–F24) and question numbers (Q1–Q12) are never reused.
3. **A template must pass the checker.** After a template change, run the test script; the template
   bundle must show 0 FAIL.
4. **A checker change raises its `VERSION`.** Projects hold a copy in `tools/check_okf.py`; the skill
   refreshes an older copy by its version.
5. **A release raises the version in `.claude-plugin/plugin.json`** and gets an entry in `CHANGELOG.md`.
   Team members get it only after a push and `claude plugin update`.
6. **Evidence for a new feature.** Add a feature only with an example from a real project, named in
   `features.md` ("Seen in").
7. **Do not edit the analysed project folders.** The tests and the evidence read them only.

## Environment

- The global preferences in `~/.claude/CLAUDE.md` apply (Windows PowerShell 5.1, commit and push rules).
- The remote is planned as `de-admin/project-init` (private). Do not push without an instruction.
