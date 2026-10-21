---
type: decision
title: Project setup – type and features
description: The project type and the context-file features chosen at initialization, with the answers that decided them and the triggers for a later review
status: draft
tags: [setup, decision]
sources:
  - id: grill
    resource: session:{{YYYY-MM-DD}}-project-init
    title: Answers of the owner to the project-init questions
generated:
  by: claude-code/{{MODEL_ID}}
  at: {{YYYY-MM-DDTHH:MM:SS+08:00}}
decided: {{YYYY-MM-DD}}
decided_by: {{OWNER}}
# When the owner confirmed the fit table in this session, add the next line and set status: stable.
# verified: { by: human:{{OWNER_INITIALS}}, at: {{YYYY-MM-DDTHH:MM:SS+08:00}} }
---

# Project setup – type and features

This record says which context-file features this project uses, and why. The `project-init` skill reads
it in mode `review`. Do not edit an old section; add a new dated section below it.

## {{YYYY-MM-DD}} – initialization

**Type:** `{{TYPE}}` – {{ONE_LINE_REASON}}

### Answers

| Question | Answer | Found or asked |
|---|---|---|
| Q1 Deliverable | {{ANSWER}} | {{found in <file> / asked}} |

### Features

| Feature | Decision | Reason |
|---|---|---|
| F1 Session protocol | {{on / off / later}} | {{THE_ANSWER_THAT_DECIDED_IT}} |

All other features: off, no signal.

<!-- One row for each feature that is on or later, or that the owner asked about, or that has a signal.
     Core features are not listed. -->

### Triggers for a review

<!-- Only the triggers for features that are "later". -->

- [ ] {{EVENT}} → add {{FEATURE}}
