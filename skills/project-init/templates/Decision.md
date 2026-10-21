---
type: decision
title: {{QUESTION_THAT_WAS_DECIDED}}
description: {{ONE_SENTENCE: the decision}}
status: draft
tags: [line-{{N}}, {{LINE_SLUG}}, decision]
sources:
  - id: {{SHORT_ID}}
    resource: {{WHERE_THE_DECISION_WAS_MADE: file, meeting note, or email subject}}
generated:
  by: claude-code/{{MODEL_ID}}
  at: {{YYYY-MM-DDTHH:MM:SS+08:00}}
decided: {{YYYY-MM-DD}}
decided_by: human:{{ID}}
---

# {{QUESTION_THAT_WAS_DECIDED}}

## Decision

{{What was decided, in one or two sentences.}}

## Reason

{{Why. The constraint or the evidence that drove it.}}

## Options considered

| Option | Why not |
|---|---|
| {{OPTION}} | {{REASON}} |

## Effect

{{What changes because of this decision: files, rules, open items closed.}}

<!-- When this decision replaces an older one, add the frontmatter key
     `supersedes: <relative path of the old record>`.
     When this decision is reversed: set status: deprecated, add a line
     "Superseded by [new decision](new-file.md) on DD/MM/YYYY", and keep this file. -->
