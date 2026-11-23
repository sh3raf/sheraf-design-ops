---
name: ds-ux-patterns
description: "Builds and maintains a living catalogue of the UX patterns a product uses, as Markdown files or as Figma documentation pages. Interviews the designer about the product, platform, features and reference screens, detects page and flow patterns from the real screens, then updates existing entries, adds missing ones and suggests patterns the product lacks. In Figma it builds a neutral doc kit and documents each pattern with an ID, a numbered template and a real example. Use when someone says \"document our UX patterns\", \"create a pattern library\", \"document this flow as a pattern\", \"update the pattern catalogue with these new screens\" or \"which patterns are we missing\". To check a screen against the design-system libraries, use ds-fixer instead."
license: MIT
---

# ds-ux-patterns

Keep one catalogue of the product's UX patterns, grounded in its real screens, and keep it current.

## 1. Connect

For Figma (reading reference screens or writing pages), run the **Connect** check in
`sdops:figma-safe-write` first. Markdown-only runs from images skip it.

## 2. Intake: look first, then ask

Fill this list before step 3. For each item, look where the second column says; ask only for what
you can't find. **One question per turn:** the most blocking unknown first (the product code), with
what you found as the default and why you ask ("Product code for the IDs: APPX? It goes in every
pattern ID."). Never number or list a second question in that turn, even beside the step 4 table;
items the designer skipped are not asked again. **Ask, then end your turn and wait for the
answer**; never write files in the same turn as a question. Items with a default are not asked:
confirm them all in one summary.

| Item | Look first in | Default if still unknown |
|---|---|---|
| Product name, codename | File, page and cover names; the catalogue; docs the designer points to (Notion, Jira, README) | ask; else `TBD` |
| ID convention, product and platform codes | Existing IDs in the catalogue | `PROD-PLT-####`: PROD is the first 5 letters of the product name in capitals (Lumen → `LUMEN`), confirmed |
| IDs already used, next free number | The catalogue index or Figma overview | `0001` |
| Platforms, breakpoints, languages, right-to-left | Frame sizes, page names, text on the screens | ask |
| Flows and screens in scope, with a link each | Page and section names, prototype flows | list what you found, ask to confirm |
| Component library (file link) | Libraries the file uses, instances on the screens | ask |
| Catalogue location | An existing `ux-patterns/` folder or pattern page | propose a new page in the product file |
| Owner, approver, version | The catalogue index | `TBD`, version 1.0 |
| Client modules | The catalogue index; the screens (payments, languages, platforms) | switched on from that evidence by the rules in `references/pattern-schema.md`, confirmed in the summary |
| Constraints: accessibility level, brand rules | Conventions file | WCAG 2.2 AA |

An existing catalogue is read in full before step 4: its names, IDs and modules win.

**Missing information.** Never invent a name, code, rule or number. People's names come only from the
designer or the catalogue, never from the environment (account, git user, folder paths). What is still unknown after
asking (the designer says "skip" or doesn't know) is written as `TBD`, keeps the pattern `proposed`,
goes into the pattern's **Open questions**, and is listed in the report. A `TBD` never blocks the run,
but it never replaces asking: ask first. IDs and file names are never `TBD`: propose a product code
from the product name; it stands once the designer accepts it or approves the table (an unconfirmed
code is listed in Open questions). Stop only without evidence (no reference screen for a pattern) and
say what is needed.

**Scope.** Before the first write, state the patterns you will document and what "done" means for
each (sections filled, example built). Don't widen it silently.

## 3. Read the reference

For each reference screen or flow: screenshot it, list its regions top to bottom (or its steps, entry
points, branches and exit), and inventory its components. Check each component against the library:
deprecated ones are documented with their replacement. Every pattern needs evidence: no screen, no
entry.

## 4. Classify and propose

Three types (`references/pattern-schema.md`): **interaction** (a reused behaviour), **page template**
(one screen, numbered regions) and **flow** (steps, branches, entry and exit). Record how they nest:
flows use page templates, page templates use interaction patterns. Use the catalogue's names first, then `references/pattern-vocabulary.md`. Show one table before
writing, then **end your turn and wait for a yes**. This gate holds in every run, slash command or
not:

| ID | Pattern | Type | Change | Evidence |
|---|---|---|---|---|
| ... | ... | Page / Flow | New / Update / Unchanged / Suggested / Deprecate | screen link |

An Update row whose entry has no file says so in the table. Write only the rows the designer approved. Suggested patterns (common for this product type,
missing from the screens) are added only on a yes, as `proposed`. Never delete: deprecate with a reason and the replacement.

## 5. Write

Every pattern gets the core sections, its type module and the catalogue's client modules
(`references/pattern-schema.md`). Fill Related both ways: `uses` / `used_by` in each touched pattern
and the index's Uses column. Do / Don't uses annotated wireframes unless the designer provides a
real misuse.
- **Markdown:** one file per pattern from `references/pattern-template.md`; update the index; set `last reviewed` and add
  a changelog line to every entry you touch.
- **Catalogue overview:** keep one index current on every run, the source for the next free ID: the
  Markdown `index.md`, or in Figma an **Overview** frame first on the page (product, codename,
  platforms, library, client modules, owner, approver, then one row per pattern: ID, name, type,
  status, owner, last reviewed).
- **Status:** new patterns are `proposed`. Set `active` only on the approver's yes, and note who and
  when in the Changelog.
- **Figma:** before the first write, load `sdops:figma-safe-write`. Build or reuse the doc kit (`references/figma-doc-kit.md`), then
  per pattern a **Template** frame (the schema's sections, laid out as in the kit) and an **Example** frame (the real screen or screens). Build examples from library
  instances with realistic content; when that can't be done in time, place renders of the real screens
  and label the frame "renders, not live components".

## 6. Report

Added, updated, deprecated and declined; every `TBD` with the question that resolves it and who can
answer; deprecated components found in the reference; places where
the live example contradicts the documented rule (a library or product gap to raise); placeholders or
gaps left in examples; entries not reviewed for 6 months. Anonymise client names before anything leaves
the team.
