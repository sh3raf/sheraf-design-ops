---
name: ds-fixer
description: Turns review notes on a Figma screen into fixes that stay on the design system, and reports what is still off-system. Classifies each note as safe, deviation, library bug or owner decision, fixes in the tokens or components library when you can edit it, and writes the client report. Use when a designer says things like "fix these review notes in Figma", "is this a deviation from the design system", "the client flagged R-02 and R-05", "realign this screen with our library" or "add the missing variant and roll it out". For a broad audit of a whole design system with no review notes, use an audit skill instead.
license: MIT
---

# ds-fixer

Turn review notes on a Figma screen into the cleanest fix for each, applied safely, with a report of
what changed and what is still off-system. Works with any design system: discover names, keys and
tokens from the files, never assume them.

## 1. Intake

Collect, and ask only for what is missing:
- **Files:** the product file, the tokens library, the components library. Note which ones the
  designer can edit; that decides whether a fix can happen in the library.
- **Notes:** each review note with the reviewer's own ID (R-02, R-05...). Give unnumbered notes one.
- **Tools:** the Figma Console bridge (`figma_execute`, local, can write any open file) and the
  official Figma MCP (`get_screenshot`, `search_design_system`, cloud). Check which are connected.
  Without the bridge, stop after step 3: deliver the classified plan and the report, change nothing.

## 2. Inspect first (read-only)

For each note, before proposing anything:
- What the screen uses now: components and variants, bound variables, hard-coded values.
- What the library offers: the component's variant options and its description; the tokens
  (`search_design_system` lists library variables with their descriptions).
- What the original or source design did, when there is one: copy its values, don't invent them.

## 3. Classify every note

| Class | Means | Do |
|---|---|---|
| Safe | A library option already does it | Use it. No record needed. |
| Deviation | Only possible as an override in the product file | Do it with tokens, log a D-id |
| Library bug or gap | The library is wrong or missing an option | Editable: fix in the library (step 5). Not: deviation now, log for the library team |
| Owner decision | A judgement call (source of truth, a rule) | Recommend one answer, ask |

Show the table to the designer before writing. Say plainly when something they assumed safe is a
deviation.

## 4. Safety protocol (every write)

- **Version first:** `figma.saveVersionHistoryAsync(title)` in each file before its first write.
- **Name the file:** with several files connected, pass `fileKey` on every call and check
  `figma.root.name` at the top of the script. Null-check every lookup before reading `.id`.
- **Dry run, then one sample:** count what a change will touch, apply it to one node, screenshot,
  then do the rest.
- **Screenshot after:** check the result visually, then delete any temporary frames.
- **Never reset all overrides** on an instance to clear one; it also wipes labels and swaps. Copy
  the main component's value onto the property instead.
- **Library writes need a yes** on the list of changes; publishing is always the designer's click.

## 5. Fix order when the library is editable

1. Change the library: add the variant or token, fix the binding, update the description.
2. Verify inside the library on a temporary instance (content in slots survives a variant switch,
   values reach a fresh instance), then delete it.
3. Draft the publish message; the designer publishes.
4. The designer clicks **Update all** in the product file.
5. Switch instances to the new option, copy the main's values over the old overrides, check again.

Tokens before components: a component bound to a new token needs the tokens library published first.

## 6. Report

Write it with `references/report-template.md`: what was fixed, library updates, decisions, and
deviations with D-ids. End every update to the designer with what is still pending and who it
waits on.

## Look up

- A render, binding, slot, import or screenshot behaves oddly → read `references/figma-gotchas.md`.
- Writing the client report or a publish message → read `references/report-template.md`.
- Airtight (`dsair`) installed → scan before and after and put both scores in the report.
