---
name: ds-ux-patterns
description: Builds and maintains a living catalogue of the UX patterns a product uses, as Markdown files or as Figma documentation pages. Interviews the designer about the product, platform, features and reference screens, detects page and flow patterns from the real screens, then updates existing entries, adds missing ones and suggests patterns the product lacks. In Figma it builds a neutral doc kit and documents each pattern with an ID, a numbered template and a real example. Use when someone says "document our UX patterns", "create a pattern library", "document this flow as a pattern", "update the pattern catalogue with these new screens" or "which patterns are we missing". To check a screen against the design-system libraries, use ds-fixer instead.
license: MIT
---

# ds-ux-patterns

Keep one catalogue of the product's UX patterns, grounded in its real screens, and keep it current.

## 1. Find the catalogue and its conventions

Ask where it lives, and read it fully before step 4:
- **Markdown:** `ux-patterns/index.md` plus one file per pattern (`references/pattern-template.md`).
- **Figma:** a pattern-library file with one section per pattern (`references/figma-doc-kit.md`).

Confirm the **ID convention** (default `PROD-PLT-####`, for example `APP-IOS-0001`: product code,
platform code, sequence), the product and platform codes, and whether the team has a doc template.
Read the catalogue's **client modules** from its index; a new catalogue sets them in step 2.

## 2. Interview

Ask only for what is missing, one question at a time, and confirm the summary:
- **Product:** what it does and for whom; the main jobs users come to do.
- **Platform:** web, iOS, Android, desktop; breakpoints; languages and right-to-left.
- **Features and flows** in scope, and the **reference screens** (Figma links or images).
- **Library:** which component library the examples must use.
- **Constraints:** accessibility level, brand rules.
- **Client modules:** ask the seven intake questions in `references/pattern-schema.md`, show the
  resulting section list, confirm it, and store it in the catalogue index.

## 3. Read the reference

For each reference screen or flow: screenshot it, list its regions top to bottom (or its steps, entry
points, branches and exit), and inventory its components. Check each component against the library:
deprecated ones are documented with their replacement. Every pattern needs evidence: no screen, no
entry.

## 4. Classify and propose

Three types (`references/pattern-schema.md`): **interaction** (a reused behaviour), **page template**
(one screen, numbered regions) and **flow** (steps, branches, entry and exit). Record how they nest:
flows use page templates, page templates use interaction patterns. Use the catalogue's names first, then `references/pattern-vocabulary.md`. Show one table before
writing:

| ID | Pattern | Type | Change | Evidence |
|---|---|---|---|---|
| ... | ... | Page / Flow | New / Update / Unchanged / Suggested / Deprecate | screen link |

Suggested patterns (common for this product type, missing from the screens) are added only on a yes,
as `proposed`. Never delete: deprecate with a reason and the replacement.

## 5. Write

Every pattern gets the core sections, its type module and the catalogue's client modules
(`references/pattern-schema.md`). Do / Don't uses annotated wireframes unless the designer provides a
real misuse.
- **Markdown:** one file per pattern from the template; update the index; set `last reviewed` and add
  a changelog line to every entry you touch.
- **Figma:** before the first write, load `sdops:figma-safe-write`. Build or reuse the doc kit, then
  per pattern a **Template** frame (the schema's sections, laid out as in the kit) and an **Example** frame (the real screen or screens). Build examples from library
  instances with realistic content; when that can't be done in time, place renders of the real screens
  and label the frame "renders, not live components".

## 6. Report

Added, updated, deprecated and declined; deprecated components found in the reference; placeholders or
gaps left in examples; entries not reviewed for 6 months. Anonymise client names before anything leaves
the team.
