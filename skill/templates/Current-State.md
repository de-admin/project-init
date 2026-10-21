---
type: status
title: {{TITLE}} – Current state
description: Where the whole project is today – goal, state of each line, task in flight, next step, and what is paused
tags: [status]
sources:
  - resource: {{LINE_SLUG}}/{{LINE_FILE}}-Open-Items.md
    title: Open items of line {{N}} (one entry for each line)
generated:
  by: claude-code/{{MODEL_ID}}
  at: {{YYYY-MM-DDTHH:MM:SS+08:00}}
stale_after: {{YYYY-MM-DDTHH:MM:SS+08:00, 14 days after generated.at}}
---

# {{TITLE}} – Current state

Rewrite this page at the end of each session, and move `stale_after` 14 days ahead. History goes in
[log.md](log.md), not here. Details of each line are in its open items file.

## Goal

{{GOAL_IN_ONE_OR_TWO_LINES}}

## Lines

| Line | State | Next step | Open items |
|---|---|---|---|
| {{N}} {{LINE_TITLE}} | {{STATE}} | {{NEXT_STEP}} | [{{LINE_FILE}}-Open-Items.md]({{LINE_SLUG}}/{{LINE_FILE}}-Open-Items.md) |

## Task in flight

- Task: {{TASK}}
- Acceptance checks: {{CHECKS}}

## Paused

- {{WHAT_IS_PAUSED_AND_WHY, or "Nothing"}}
