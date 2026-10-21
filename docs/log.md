# Change log

One entry for each change to `docs/`, newest first. Each entry names the **actor** (what wrote the change),
the **owner** (who is accountable for it) and the **reason**. Actors use the OKF forms:
`<producer>/<version>`, `human:<id>`, `process:<id>`. If the owner is not known, write
`owner:unattributed`. Do not guess an owner.

## 2026-10-21

- **Update** — `skill/Skill-Open-Items.md` "Now" and Q2: the repository `de-admin/project-init` is created
  and pushed; the marketplace entry is in PR #1 of `de-admin/claude-tools`
  actor:claude-code/claude-opus-5-5 · owner:human:SW · reason: SW approved the repository, the push and
  the PR
- **Update** — prepared as a plugin for the de-admin marketplace: the skill moved from `skill/` to
  `skills/project-init/`; source paths in `skill/Skill-Overview.md`, `skill/Skill-Open-Items.md`,
  `index.md` and `skill/index.md` changed to match. Overview: the checker copy (`tools/check_okf.py`) and the
  plugin install. Open items: "Now" and Q2 updated. `Project-Setup.md`: new review section (F10 on)
  actor:claude-code/claude-opus-5-5 · owner:human:SW · reason: SW asked to prepare project-init for the
  de-admin marketplace
- **Update** — `skill/Skill-Open-Items.md` Q2 now names the de-admin marketplace (`de-admin/claude-tools`)
  and the changes that sharing through it needs
  actor:claude-code/claude-opus-5-5 · owner:human:SW · reason: SW asked if the skill must be added to the
  de-admin marketplace
- **Creation** — `docs/` created as an OKF v0.2 bundle with 1 line: line 1 `skill/` (the project-init
  skill, reference `skill/`), with an `index.md`, an overview and an open items file. Root `index.md`,
  `Project-Setup.md`, this log, the project `README.md` and `CLAUDE.md` added. The skill was drafted,
  audited twice and dry-run in an earlier part of the same session
  actor:claude-code/claude-opus-5-5 · owner:human:SW · reason: SW asked to install the skill and make it
  its own project folder under D:\projects
