# Figma gotchas

Read when a render, binding, slot, import or screenshot behaves unexpectedly. Seen in November 2026;
Figma's Plugin API changes, so re-check an entry that stops matching what you see.

## Colour and effects
- **Translucent fills need an alpha token.** A paint bound to an opaque colour variable loses its
  paint opacity in instances (renders solid). Put the alpha in the token itself (white at 12%),
  bind that, and leave paint opacity at 1. Precedent to look for: hover-overlay tokens.
- **Glass effect styles can render opaque.** A GLASS effect applied through an effect style can
  render as a solid white block on small controls, in exports and cloud screenshots alike. Check
  the render; set the effect directly on the component if the style fails.
- **Read token descriptions against mode names.** "(White)" can be the name of the light mode, not
  the colour. Resolve the value before calling a token wrong.

## Components
- **`clone()` of a variant drops its wiring.** A SLOT becomes a plain FRAME, and text property links
  and boolean references are lost. Fix the slot with `variant.createSlot()`: give it the old frame's
  layout, remove the frame and the default white fill createSlot adds, set
  `componentPropertyReferences = {slotContentId: <existing slot property>}`, then
  `deleteComponentProperty` on the stray property it created. Relink every text and boolean reference.
- **Map cloned layers by name, not index.** Hidden layers shift the order.
- **`clone()` + `swapComponent()` carries the old instance's overrides** (padding, fills). On that
  freshly built instance only, call `resetOverrides()`, then relink the text properties.
- **Variant switches keep fill overrides, and hidden nested overrides.** After `setProperties`, copy
  the new main's fills, strokes and effects onto the instance, and check the result.
- **A nested layer missing from a variant can't be restored by any override.** Classify it as a
  library bug.
- **Some text or boolean layers aren't linked to their property.** Link them, then test that typed-over
  text survives as the property value.
- **Changing a main component's constraints (for example to SCALE) reflows resized instances.** Scan
  for resized instances after the change.
- **Swapping a nested icon drops its colour override.** Recolour after the swap, at every level.
- **Replacing a nested node in a main component loses per-instance swaps** made on it (a row that
  showed $ instead of the default sign reverts). Resize or recolour in place instead.
- **A layer name is not a component.** Several sets can share a name; find sets by their variant
  options.

## Slots
- **`findAll` and `findOne` don't enter slot content.** Walk `children` recursively.
- **`appendChild` into a nested slot returns a new node.** Re-read `slot.children[i]` before each edit.
- **Nested edits in the same call as an append often don't stick.** Do swaps and nested edits in a
  second call.
- **Instances cloned from other screens into a slot carry stale nested ids** ("node does not exist")
  and lose their slot content. Build from a fresh instance of the main component.
- **Moving heavily overridden instances into a slot can drop their children.** Rebuild them inside
  the slot.
- **Direct slot children can't carry boolean property references.** To hide a part, delete the layer
  in the slot.
- **After hiding a nested slot, the parent layout can go stale.** Nudge `itemSpacing` (+1, -1) to
  force a relayout.

## Text
- **A text component set to Fill doesn't wrap.** Set its inner text to Fill and auto height too.
- **Never apply a text style to a glyph-font layer** (currency symbols, icon fonts): it replaces the
  font and the glyph disappears.

## Variables and modes
- **Set modes on the section or page, never on screens or layers.** To clear them, call
  `clearExplicitVariableModeForCollection` on every node, including inside instances. For an
  extension collection, clear via its parent collection; clearing the extension does nothing.
- **Modes resolve per collection.** An alias into a remote collection uses that collection's own mode,
  not the aliasing collection's. A dark section may need modes set on both collections, or the dark
  values must alias primitives directly.
- **REST `variables/local` omits library variables,** so bindings look broken when they aren't.
  Resolve the ids through the Plugin API before reporting.
- **New tokens copy their siblings' naming and scopes,** and go into every layer of the token stack at
  once (component layer and theme layer).

## Libraries and imports
- **A file with no libraries enabled can still import published components by key**
  (`importComponentByKeyAsync`, `importComponentSetByKeyAsync`). Some keys still fail (unpublished
  or restricted): treat each import as optional, report the misses, and never leave an empty section.
- **Reference files can use deprecated components.** Check each component's name and description in
  the library (`-DEPRECATED`, "Instead use ...") and build with the replacement.
- **Library components ship with placeholder text** (`{title}`, `{{description}}`, "Label",
  "Option1"). Replace every one before showing a result; when a text isn't tied to a component
  property, load its font and set `characters` directly.
- **A brand asset can render wrong even with a normal transform** (a mirrored logo in exports and
  cloud screenshots). Check the render; if it's wrong, use another official variant and re-check.
- **The default variant is rarely the screen's variant** (a header with a back arrow on a home
  screen). Read the variant options and pick the one the reference uses.

## Bridge and tools
- **`importComponentByKeyAsync` / `importVariableByKeyAsync` can hang** and keep running after the
  timeout, finishing later. Prefer variables already bound somewhere in the file
  (`getVariableByIdAsync`), import one at a time, and re-read state after any timeout before retrying.
- **The bridge screenshot shoots the active file only.** For another file, use the official MCP
  `get_screenshot` (cloud copy, may lag a few seconds) or `exportAsync` saved to disk.
- **The designer doesn't see a change?** Check they're viewing the right file (branch or main) and the
  right mode in the variable dropdown.
- **Reference images in shared files can be compressed copies.** Fetch originals through REST
  `/v1/files/:key/images` and compare image hashes.
- **Return values flood context.** Don't return base64 images inline; let the tool save oversize
  output to a file and decode it there.
- **Plugin errors show the designer a red toast.** A crashed read-only script changes nothing, but
  say so.
