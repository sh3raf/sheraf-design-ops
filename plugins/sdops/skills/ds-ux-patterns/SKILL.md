---
name: ds-ux-patterns
description: Builds and maintains a living catalogue of the UX patterns a product uses. Interviews the designer about the product, platform, features and reference screens, detects the patterns, then updates existing catalogue entries, adds missing ones and suggests patterns the product lacks. Use when someone says "document our UX patterns", "what UX patterns does this product need", "update the pattern catalogue with these new screens", "add the onboarding flow to our patterns" or "which patterns are we missing". To check a screen against the design-system libraries, use ds-fixer instead.
license: MIT
---

# ds-ux-patterns

Keep one catalogue of the product's UX patterns, grounded in its real screens, and keep it current.
Reads Figma; writes only the catalogue files.

## 1. Find the catalogue

Look for `ux-patterns/index.md` in the project. Not there: ask where it lives, or offer to create
`ux-patterns/` (one file per pattern plus `index.md`). Read the index and every entry before step 3.

## 2. Interview

Ask only for what is missing, one question at a time, and confirm the summary before going on:
- **Product:** what it does and for whom; the main jobs users come to do.
- **Platform:** web, iOS, Android, desktop; breakpoints; languages and right-to-left.
- **Features and flows:** the ones in scope this run.
- **Reference screens:** Figma links (read with `get_metadata` and `get_screenshot`) or images.
- **Constraints:** accessibility level, design system in use, brand rules.

## 3. Detect

Map features and screens to patterns. Use the catalogue's names first, then
`references/pattern-vocabulary.md`; record other names as aliases. Every pattern needs evidence: the
screen or frame where it appears. No evidence, no entry.

## 4. Propose the changes

Show one table before writing anything:

| Pattern | Change | Evidence | What changes |
|---|---|---|---|
| ... | New / Update / Unchanged / Suggested (missing) / Deprecate | screen link | one line |

- **Update** an existing entry with new examples, platform notes or states; never rewrite its intent
  silently.
- **Suggested** patterns are ones this kind of product usually needs but the screens lack (an empty
  state, an error recovery path). Add them only on a yes, marked `status: proposed`.
- **Never delete.** Mark `status: deprecated` with a reason and a pointer to the replacement.

## 5. Write

Use `references/pattern-template.md`. One file per pattern; update `index.md`; set `last reviewed`
to today and add a changelog line to every entry you touch. Link library components when they are
known (`search_design_system`), so ds-fixer and the catalogue speak the same names.

## 6. Report

What was added, updated, deprecated and declined; entries not reviewed for 6 months or more; open
questions for the designer. Anonymise client names before anything leaves the team.
