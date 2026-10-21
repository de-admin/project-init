# project-init – OKF project initialization skill

A Claude Code skill that sets up the context files of a project folder: `README.md`, `CLAUDE.md`, an
optional `AGENTS.md`, and a `docs/` bundle in the Open Knowledge Format (OKF v0.2). Before it writes, it
grills the user to find the project type and the smallest set of features that fit.

Started 21/10/2026 by SW (YTL Data Team, SPYTL).

## Goals

1. One repeatable way to start or adopt a project folder, based on what worked in earlier projects.
2. Documentation that any tool can read (vendor-neutral), with rules that a script can check.

## Lines of work

| Line | Subject | Reference | Documentation |
|---|---|---|---|
| 1 | **Skill** – the skill, its references, templates and checker | [`skills/project-init/`](skills/project-init/) | [`docs/skill/`](docs/skill/) |

## Install

This repository is a Claude Code plugin. It is listed in the de-admin marketplace
([de-admin/claude-tools](https://github.com/de-admin/claude-tools)). The repositories are private: git on
your machine must have access to `de-admin` on GitHub.

```bash
claude plugin marketplace add de-admin/claude-tools
```

```bash
claude plugin install project-init@claude-tools --scope user
```

To update: `claude plugin marketplace update claude-tools`, then `claude plugin update project-init@claude-tools`.

To use it, open a project folder in Claude Code and say "initialize this project", or type
`/project-init`. The skill copies its checker into each project as `tools/check_okf.py`.

### Develop the skill

Do not install the plugin on the machine where you develop it. Link the skill folder instead, so an edit
here changes the installed skill at once. Run in Windows PowerShell (one time per machine):

```powershell
cmd /c mklink /J "$env:USERPROFILE\.claude\skills\project-init" "D:\projects\project-init\skills\project-init"
```

With both the plugin and the junction, the skill loads twice.

## Test

```powershell
python tests\test_check_okf.py
```

The script runs the checker on two real OKF bundles, on an edge-case fixture and on a bundle made from
the templates. It prints results; compare them with the expected results in
`docs/skill/Skill-Overview.md` section 5. It reads two folders under
`D:\Users\ShaoWenChooi\YTL\...\Studies` and writes only to a new temporary folder.

## Folder layout

```
project-init/
├── README.md            this file
├── CLAUDE.md            procedure for Claude Code sessions in this repository
├── CHANGELOG.md         changes for each release of the plugin
├── .claude-plugin/
│   └── plugin.json      plugin name, version, description
├── skills/project-init/ the skill
│   ├── SKILL.md         the procedure: inspect, grill, show the fit, write, check, log
│   ├── references/      features.md (types, features, questions), okf-rules.md (OKF + house rules)
│   ├── templates/       file templates with {{placeholders}}
│   └── scripts/         check_okf.py – the bundle checker (copied into each project as tools/)
├── tests/               test_check_okf.py
└── docs/                documentation bundle (OKF v0.2)
    ├── index.md
    ├── log.md
    ├── Project-Setup.md
    └── skill/
        ├── index.md
        ├── Skill-Overview.md
        └── Skill-Open-Items.md
```

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
7. A reversed decision is not deleted. Set `status: deprecated` and link to the new decision.
