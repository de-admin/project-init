---
type: decision
title: Project setup – type and features
description: The project type and the context-file features chosen for the project-init repository, with the reasons and the triggers for a later review
status: draft
tags: [setup, decision]
sources:
  - id: grill
    resource: session:2026-10-21-project-init
    title: Inferred by the agent from the folder and the session; not grilled with the owner
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-10-21T11:05:00+08:00
decided: 2026-10-21
decided_by: claude-code/claude-opus-5-5
---

# Project setup – type and features

This record says which context-file features this project uses, and why. The `project-init` skill reads
it in mode `review`. Do not edit an old section; add a new dated section below it.

The skill did not grill the owner for this setup. The agent inferred the answers from the folder and the
session that built the skill. The owner has not confirmed them, so this record has `status: draft`.

## 2026-10-21 – initialization

**Type:** `tool-study` – one person builds a tool (a skill and a script) used by an external system
(Claude Code), over many sessions.

### Answers

| Question | Answer | Found or asked |
|---|---|---|
| Q1 Deliverable | Tool in an external system (Claude Code skill) | found: `skill/SKILL.md` |
| Q2 Duration | Weeks, many sessions | inferred |
| Q3 People | Only SW | found: session owner |
| Q4 Numbers checked | Yes, the checker results must be repeatable | found: `tests/test_check_okf.py` |
| Q5 Versions side by side | No (git keeps versions) | found |
| Q6 Changes an external system | Yes – the installed skill changes at each save (junction) | found |
| Q7 Lines | One | found |
| Q10 Code | Scripts with a test script | found: `skill/scripts/`, `tests/` |
| Q11 Known correct result | Yes – the Worksheet Improvements bundle must pass with 0 WARN | found |

### Features

| Feature | Decision | Reason |
|---|---|---|
| F1 Session protocol | on | Many sessions |
| F4 Live files register | off | Git keeps versions; the type default does not apply |
| F6 Key identifiers | off | No identifiers; the junction path is in README "Install" |
| F7 Decision records | later | Add when a design choice is questioned (see open items D1, D2) |
| F18 `_archive/` | off | Git keeps old versions |
| F19 `tools/` | on, as `skill/scripts/` and `tests/` | Scripts exist |
| F20 Git | on | Code and tests |
| F22 Ground truth | on, as the expected results in `Skill-Overview.md` section 5 | Q11 |
| F24 Run evidence | off | A run of the skill leaves its own record in the target project's `log.md` |

All other features: off, no signal.

### Triggers for a review

- [ ] Another person or agent starts to change the skill → F14, F15
- [ ] A design choice is questioned or reversed → F7
- [ ] The skill is shared with the team (a plugin or a shared repository) → F10 release changelog
