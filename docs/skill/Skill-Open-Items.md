---
type: open-items
title: project-init skill – Open Items
description: Running tracker for line 1 – current state, questions for the owner, gaps found, and decisions pending
status: draft
tags: [line-1, skill, tracker]
sources:
  - id: skill
    resource: ../../skills/project-init/SKILL.md
    title: The skill, as installed on 21/10/2026
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-10-21T11:05:00+08:00
---

# project-init skill – Open Items

Use this file for the current state, unfinished work and open questions on line 1. Do not make a new
file for them. Mark an item `[x]` when it closes, and write the date and the reason. Never reuse a number.

## Now

- State: the skill is drafted, audited twice, and installed through a junction (21/10/2026). Plugin 0.1.0
  is pushed to the private repository `de-admin/project-init`. The marketplace entry waits in PR #1 of
  `de-admin/claude-tools` (<https://github.com/de-admin/claude-tools/pull/1>). The skill has not been run
  from start to end on a real folder.
- Next step: merge PR #1; run `/project-init` on a real study folder, then record what went wrong here.

## Questions for the owner

- [ ] Q1. Is this setup record (`docs/Project-Setup.md`) correct? It was inferred, not grilled. Confirm it,
      and the agent can add your `verified` entry.
- [ ] Q2. Share the skill through the de-admin marketplace (`de-admin/claude-tools`)? SW asked on
      21/10/2026 to prepare it. Done locally: `.claude-plugin/plugin.json`, `skills/project-init/`, the
      checker copied into each project as `tools/check_okf.py`, `CHANGELOG.md`, and the marketplace entry
      committed in `D:\projects\claude-tools`. Done 21/10/2026: private repository `de-admin/project-init`
      created (`de-admin` is a user account, not an organization) and `main` pushed; the `claude-tools`
      entry pushed on branch `add-project-init`, PR #1. Open: merge PR #1. Close this item then.

## Gaps found (21/10/2026)

- [ ] G1. No end-to-end run with a real user. The grilling rounds, the fit table and the templates have
      been checked only by reading and by the checker.
- [ ] G2. The dry run on four projects (77% of feature decisions matched) used the catalogue before F22–F24
      and the 4-question rule were added. It has not been run again.
- [ ] G3. Without PyYAML, the checker does not check the shape of `sources` and `verified` lists.
- [ ] G4. The checker does not check the bullet form of `index.md` (`* [Title](link) - description`).
- [ ] G5. The test script prints results; it does not compare them with the expected results
      automatically.

## Decisions pending

- [ ] D1. `verified: []` with a comment (Voon pilot) or no key (the skill now). The skill warns on
      `verified: []`.
- [ ] D2. `type: overview` for every subject (the skill now) or narrower types such as `app-overview`
      (Worksheet Improvements).
- [ ] D3. Convert the Voon pilot and the Worksheet bundle to the skill's rules with mode `adopt`/`review`,
      or leave them as they are.

## Closed

<!-- Move closed items here: - [x] Q1. ... – closed DD/MM/YYYY: <reason> -->
