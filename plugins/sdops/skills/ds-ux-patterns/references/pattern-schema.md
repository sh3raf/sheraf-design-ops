# Pattern schema

One definition for every pattern, in Markdown and in Figma. A pattern = **core** + its **type module**
+ the **client modules** switched on for this catalogue. Leave out a section only when its module is
off; never leave a core section empty (write "None" and why, or `TBD` with an open question).

## Core (every pattern)

| Section | Contents |
|---|---|
| Identity | ID, name, aliases, type, category, status (proposed / active / deprecated), owner, version, last reviewed |
| Purpose | The user problem it solves and the business goal, one sentence each |
| Usage | When to use; when not to use and what to use instead |
| Anatomy | Numbered parts: regions (page), steps (flow) or elements (interaction) |
| Behaviour | Interactions, rules and edge cases |
| States | Which apply: default, loading, empty, error, success, disabled, offline |
| Content | Labels, tone, microcopy rules, truncation, number and date formats |
| Accessibility | Specific requirements: focus order, labels, contrast, dynamic type, motion |
| Do / Don't | At least one pair: correct use next to a common misuse, each with a one-line reason |
| Related | Parent and child patterns (by ID), library components that build it |
| Evidence | The real screens or frames it comes from |
| Changelog | Date, what changed, why |
| Open questions | Only while something is `TBD`: the question, who can answer, what it blocks |

## Type modules (one per pattern)

Types nest: a **flow** uses page templates; a **page template** uses interaction patterns. Record the
links in Related, both ways.

| Type | Use for | Adds |
|---|---|---|
| Interaction | A behaviour reused across screens: hide balance, pull to refresh, inline validation, empty state | Trigger → feedback, gestures, motion and timing, where it appears |
| Page template | One screen's structure: home, detail, list, settings | Regions, layout grid, responsive behaviour, region visibility rules |
| Flow | A journey across screens: onboarding, transfer, apply | Entry points, exit, steps, branches (3a, 3b), error recovery, abandon and resume, success measure |

## Client modules (switched on at intake, stored in the catalogue index)

| Module | Switch on when | Adds to every pattern |
|---|---|---|
| Regulated | Banking, insurance, health, public sector | Disclosures, consent, mandatory wording, audit trail |
| Security & privacy | Sensitive personal or financial data | Masking, re-authentication, timeouts, screenshot and clipboard rules |
| Localisation & RTL | More than one language, or a right-to-left language | Mirroring rules, text expansion, numerals, currency and date formats |
| Multi-platform | More than one of iOS, Android, web, desktop | Differences per platform and the reason for each |
| Multi-brand | Several brands share the system | What a brand may change, what it may not |
| Analytics | The team tracks product events | Events, funnel steps, KPIs |
| Code link | Developers read the catalogue | Code component names, Code Connect links, API and data states |

## Intake questions that set the modules
1. What industry, and is it regulated? 2. Does the product show sensitive data? 3. Which languages,
and is any right-to-left? 4. Which platforms? 5. More than one brand? 6. Does the team track events?
7. Will developers use the catalogue? Show the resulting section list and confirm it before writing.
