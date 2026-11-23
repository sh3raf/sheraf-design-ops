---
name: figma-safe-write
description: "Safety rules and Plugin API gotchas for changing Figma files and libraries through the official Figma MCP (use_figma) or the Figma Console bridge. Covers saving a version before a write, naming the target file, dry runs and one sample first, small batches, reading back after a dropped or timed-out call, resuming a half-applied script, and the known traps with slots, cloned variants, nested instances, variable modes, text styles, imports and renders. Also runs the setup check (\"check my Figma setup\"): connectors, signed-in account, file access. Use before any script that writes to a Figma file, and whenever a write, binding, slot, import or render behaves unexpectedly. Other sdops skills load it before their first write."
license: MIT
---

# figma-safe-write

Follow these rules for every write to a Figma file. They exist because each one cost real work when
skipped.

## Connect (before the first Figma call of a run)
Check, then tell the designer exactly what to do for anything missing (steps in `references/setup.md`):
- **Connectors:** official MCP (`whoami`) and the bridge (`figma_get_status`, then the open files list).
  Neither answers: give the setup steps, mark the run **blocked on the designer**, and stop.
- **Account:** `whoami` names the signed-in account. If it can't open the file ("not found", "no
  access"), say: "Run `/mcp` → figma → Clear authentication, then sign in with the account that owns
  this file."
- **File:** read the target file once (metadata). On the bridge it must be in the open files list, else
  say: "Open the file in Figma Desktop, then Plugins → Development → Figma Desktop Bridge."
- **Edit rights:** read-only access means plan and report only; say so before step 1, not after.
- **The tool's own guide:** before `use_figma`, load `figma-use` (and `figma-generate-design` before
  visible changes): the Figma plugin's skill if installed, else the MCP resource
  `skill://figma/figma-use/SKILL.md`. With the official MCP, `create_session` on the file key first.

## Before the first write
- **Version first:** `figma.saveVersionHistoryAsync(title)` in each file before its first change;
  name the version in the report so the designer can undo the round. The official MCP's `use_figma`
  can't save versions: use the bridge, or ask the designer to save one, unless the run only adds new
  pages or frames.
- **Name the file:** with several files connected, pass `fileKey` on every call and check
  `figma.root.name` at the top of the script. Null-check every lookup before reading `.id`.
- **Inspect, read-only:** what exists, which libraries the file can use, which fonts the product uses.

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
