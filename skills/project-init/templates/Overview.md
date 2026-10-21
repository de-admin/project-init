---
type: overview
title: {{LINE_TITLE}} – Overview
description: {{ONE_SENTENCE: what the subject is and what this document explains}}
status: draft
tags: [line-{{N}}, {{LINE_SLUG}}]
resource: {{RELATIVE_PATH_TO_REFERENCE}}
sources:
  - id: {{SHORT_ID}}
    resource: {{RELATIVE_PATH_TO_FILE}}
    title: {{WHAT_THE_FILE_IS}}
generated:
  by: claude-code/{{MODEL_ID}}
  at: {{YYYY-MM-DDTHH:MM:SS+08:00}}
---

# {{LINE_TITLE}} – Overview

**Line {{N}} of {{TOTAL}}.** This line documents {{SUBJECT}} in
[`{{REFERENCE_PATH}}`](<{{RELATIVE_PATH_TO_REFERENCE}}>).

## 1. Purpose

{{Who uses it, for what, and what problem it solves.}}

## 2. How it works

{{The parts, the tools, the flow from input to output. A table or a short list.}}

## 3. Data and storage

{{Where the data comes from, where it is kept, and the identifiers that matter.}}

## 4. Inputs and outputs

{{Inputs, outputs, and their formats.}}

<!-- Add numbered sections for what this subject needs: calculations, rules, screens, steps. Cite each
     statement that comes from a file with a footnote, for example: ... 154 lines[^{{SHORT_ID}}] -->

[^{{SHORT_ID}}]: `{{FILE_NAME}}`
