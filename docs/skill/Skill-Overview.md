---
type: overview
title: project-init skill – Overview
description: What the project-init skill does, its parts, the evidence from earlier projects that shaped it, the main design choices, and the tests with their expected results
status: draft
tags: [line-1, skill, claude-code-skill]
resource: ../../skill/
sources:
  - id: skill
    resource: ../../skill/SKILL.md
    title: The skill procedure (Steps 1–6, modes new, adopt, extend, review)
  - id: features
    resource: ../../skill/references/features.md
    title: Project types, features F1–F24, questions Q1–Q12, challenge rules, triggers
  - id: rules
    resource: ../../skill/references/okf-rules.md
    title: OKF v0.2 summary and house adaptations
  - id: checker
    resource: ../../skill/scripts/check_okf.py
    title: Bundle checker
  - id: tests
    resource: ../../tests/test_check_okf.py
    title: Checker test script
  - id: spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format, spec v0.2, read on 21/10/2026
  - id: worksheet
    resource: D:\Users\ShaoWenChooi\YTL\Digital Engineering (SPYTL) - Repository\Studies\(2026.10.21) SW - Worksheet Improvements - App\docs
    title: First hand-made OKF bundle; the reference output
  - id: voon
    resource: D:\Users\ShaoWenChooi\YTL\Digital Engineering (SPYTL) - Repository\Studies\(2026.10.06) Voon - Water Engineering\docs
    title: OKF pilot agreed 08/10/2026 (multi-person, check scripts)
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-10-21T11:05:00+08:00
---

# project-init skill – Overview

**Line 1 of 1.** This line documents the skill in [`skill/`](../../skill/).

## 1. Purpose

The skill gives one repeatable way to start or adopt a project folder. It writes the context files that
earlier projects made by hand, in different ways each time. It uses the Open Knowledge Format (OKF v0.2)
for `docs/`, so that tools other than Claude Code (for example IlmuCode) can read the documentation and a
script can check it[^spec].

## 2. How it works

| Part | What it does |
|---|---|
| `SKILL.md` | Step 1 inspects the folder; Step 2 grills the user; Step 3 shows the fit and the plan for one confirmation; Step 4 writes the files; Step 5 runs the checker; Step 6 logs and reports. Modes: `new`, `adopt`, `extend`, `review`[^skill] |
| `references/features.md` | 5 project types, 24 features (F1–F24), 12 questions (Q1–Q12), challenge rules, triggers for a review[^features] |
| `references/okf-rules.md` | The OKF v0.2 rules, the house adaptations, the `type` vocabulary and the body shape of each type[^rules] |
| `templates/` | 11 file templates with `{{placeholders}}` |
| `scripts/check_okf.py` | Checks a bundle: FAIL for a break of OKF conformance, WARN for a house rule. Standard library; uses PyYAML when it is installed[^checker] |

The files that the skill always writes: `README.md` (description and doc rules), `CLAUDE.md` (agent
procedure only), `docs/index.md`, `docs/log.md`, `docs/Project-Setup.md`, and for each line an `index.md`,
an overview and an open items file. Other files come only from features that the grilling turns on.

## 3. Evidence base

The skill was built on 21/10/2026 from an analysis of about 20 context files in 14 projects:

- **OKF bundles:** Worksheet Improvements[^worksheet] (spec-literal, one folder per line, rules in README)
  and the Voon pilot[^voon] (frontmatter on reports and decisions only, check scripts with receipts, rules
  in `CLAUDE.md`).
- **Small studies:** Excel Protection, Claude vs Codex demo, Water Rain, HR KPI Tracker, OCR Skill, KPI
  ScoreCard, Non-design KPI Consolidation, SP Automation, Agent MCP (all under
  `D:\Users\ShaoWenChooi\YTL\Digital Engineering (SPYTL) - Repository\Studies\`).
- **Apps:** Manhour POC v3, Design App (Digital Design Management), DocuScan, Orchestra.

Main findings that shaped the skill:

1. `CLAUDE.md`, `AGENTS.md` and `README.md` held the same text in the larger projects, and the copies
   drifted (Manhour and Design App). → One fact in one place; `AGENTS.md` is imported by `CLAUDE.md`.
2. Some `CLAUDE.md` files grew to about 490 lines with dated state blocks (DocuScan). → `CLAUDE.md` holds
   only procedure; state goes in the open items "Now" section or the current-state page.
3. The Voon pilot needed rules that other agents read, but kept them in `CLAUDE.md`. → The doc rules go in
   `README.md`.
4. Studies differ from apps: 8 of 10 have no git, sources are often binary files, and deliverables are
   documents. → Project types, and features chosen by fit.

Analysis and review were done with orchestra jobs (GLM reader and auditor profiles): three readers for
the analysis, two audits of the skill (15 and 11 findings, all fixed), and one dry run of the grilling on
four projects.

## 4. Design choices

| Choice | Reason |
|---|---|
| Rules in `README.md`, procedure in `CLAUDE.md` | Other tools read README; Claude-only steps stay out of the shared rules |
| Strict OKF v0.2 in `docs/`, with house additions that do not break it | Bundles stay valid for any OKF consumer |
| Features chosen by grilling, not by habit | Each feature costs upkeep; small studies stay small |
| No `verified: []`; no key means unverified | OKF trust tiers read the key; an empty list says nothing more (open item D1) |
| `type: overview`, not `app-overview` | One type for every kind of subject; the kind goes in `tags` (open item D2) |
| `/`-rooted paths mean the bundle root | As the OKF spec says; files outside `docs/` use relative paths |
| Installed through a junction | One source; no copy to keep in step |

## 5. Tests and expected results

Run `python tests\test_check_okf.py`[^tests]. Expected on 21/10/2026:

| Case | Expected |
|---|---|
| Worksheet Improvements bundle, with and without PyYAML | `PASS: 4 concepts, 0 FAIL, 0 WARN` both times |
| Voon pilot bundle, with and without PyYAML | `FAIL: 17 concepts, 11 FAIL, 25 WARN` both times (11 specs without frontmatter, uppercase `INDEX.md`, `verified: []`, `/`-rooted source paths) |
| Edge-case fixture, PyYAML | 4 FAIL (invalid YAML, `sources[0]` without `resource`, `verified[0]` without `by`, `## Notes` in the log), 4 WARN |
| Edge-case fixture, no PyYAML | 2 FAIL, 4 WARN (the list-shape checks need PyYAML) |
| Template bundle (placeholders replaced with `x`) | `PASS`, 0 FAIL; WARN lines only for `x` paths, the stale test page and pages not listed in an index |

The Voon numbers change when that project changes its docs. A change there is not a failure of the skill.

[^skill]: `skill/SKILL.md`
[^features]: `skill/references/features.md`
[^rules]: `skill/references/okf-rules.md`
[^checker]: `skill/scripts/check_okf.py`
[^tests]: `tests/test_check_okf.py`
[^spec]: OKF spec v0.2
[^worksheet]: Worksheet Improvements `docs/`
[^voon]: Voon Water Engineering `docs/`
