---
type: open-items
title: {{LINE_TITLE}} – Open Items
description: Running tracker for line {{N}} – current state, questions for the owner, gaps found, and decisions pending
status: draft
tags: [line-{{N}}, {{LINE_SLUG}}, tracker]
sources:
  - id: {{SHORT_ID}}
    resource: {{RELATIVE_PATH_TO_FILE}}
    title: {{WHAT_WAS_READ}}, read on {{DD/MM/YYYY}}
generated:
  by: claude-code/{{MODEL_ID}}
  at: {{YYYY-MM-DDTHH:MM:SS+08:00}}
---

# {{LINE_TITLE}} – Open Items

Use this file for the current state, unfinished work and open questions on line {{N}}. Do not make a new
file for them. Mark an item `[x]` when it closes, and write the date and the reason. Never reuse a number.

## Now

- State: {{ONE_OR_TWO_LINES: where the work is today}}
- Next step: {{THE_NEXT_ACTION}}

## Questions for the owner

- [ ] Q1. {{A_REAL_QUESTION_FROM_THE_EVIDENCE}}

## Gaps found ({{DD/MM/YYYY}})

- [ ] G1. {{A_GAP_OR_RISK_FOUND_IN_THE_MATERIAL}}

## Decisions pending

- [ ] D1. {{A_DECISION_THAT_BLOCKS_WORK}}

## Closed

<!-- Move closed items here: - [x] Q1. ... – closed DD/MM/YYYY: <reason> -->
