---
name: figma-safe-write
description: Safety rules and Plugin API gotchas for changing Figma files and libraries through the official Figma MCP (use_figma) or the Figma Console bridge. Covers saving a version before a write, naming the target file, dry runs and one sample first, small batches, reading back after a dropped or timed-out call, resuming a half-applied script, and the known traps with slots, cloned variants, nested instances, variable modes, text styles, imports and renders. Use before any script that writes to a Figma file, and whenever a write, binding, slot, import or render behaves unexpectedly. Other sdops skills load it before their first write.
license: MIT
---

# figma-safe-write

Follow these rules for every write to a Figma file. They exist because each one cost real work when
skipped.

## Before the first write
- **Version first:** `figma.saveVersionHistoryAsync(title)` in each file before its first change;
  name the version in the report so the designer can undo the round. The official MCP's `use_figma`
  can't save versions: use the bridge, or ask the designer to save one, unless the run only adds new
  pages or frames.
- **Name the file:** with several files connected, pass `fileKey` on every call and check
  `figma.root.name` at the top of the script. Null-check every lookup before reading `.id`.
- **Inspect, read-only:** what exists, which libraries the file can use, which fonts the product uses.
- **Load the tool's own guide** when it has one (the official MCP requires `figma-use` before
  `use_figma`, and `figma-generate-design` before visible changes).

## While writing
- **Dry run, then one sample:** count what a change will touch, apply it to one node, screenshot,
  then do the rest.
- **Small batches.** A dropped or timed-out call may still have applied, and may still be running:
  read the state back before retrying.
- **Resume, don't repeat.** On the bridge, a script that fails part-way keeps the steps before the
  failure: re-run only the rest. The official MCP's `use_figma` rolls a failed script back entirely.
  Either way, read the canvas before retrying.
- **Inventories on disk:** save long lists as JSON in the working folder, not in chat.
- **Never reset all overrides** on a live instance to clear one; it also wipes labels and swaps. Copy
  the main component's value onto the property instead.
- **Know the limits:** the official MCP has a daily call cap; the bridge runs one script at a time.
  Never run scripts in parallel on the bridge.

## After writing
- **Screenshot and look.** Check text, overlaps and renders; delete temporary frames.
- **Library writes need a yes** on the list of changes; publishing is always the designer's click.

## Look up
A render, binding, slot, import, text or screenshot behaves oddly → read `references/figma-gotchas.md`.
