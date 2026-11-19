# Figma gotchas

Read when a render, binding, slot, import or screenshot behaves unexpectedly.

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
- **Cloning a variant drops its slot.** `clone()` turns a SLOT into a plain FRAME, so instances
  switched to the new variant lose their content. Fix: `variant.createSlot()`, give it the old
  frame's layout, remove the frame, set `componentPropertyReferences = {slotContentId: <existing
  slot property>}`, then `deleteComponentProperty` on the duplicate property createSlot added.
- **Swapping a nested icon drops its colour override.** Recolour after the swap, at every level.
- **Replacing a nested node in a main component loses per-instance swaps** made on it (a row that
  showed $ instead of the default sign reverts). Resize or recolour in place instead.
- **Variant switches keep fill overrides.** After `setProperties`, copy the new main's fills,
  strokes and effects onto the instance.
- **A layer name is not a component.** Several sets can share a name (an icon "Currency" and a
  header "Currency"); find sets by their variant options.

## Bridge and tools
- **`importComponentByKeyAsync` / `importVariableByKeyAsync` can hang** and keep running after the
  timeout, finishing later. Prefer variables already bound somewhere in the file
  (`getVariableByIdAsync`), import one at a time, and re-read state after any timeout before retrying.
- **The bridge screenshot shoots the active file only.** For another file, use the official MCP
  `get_screenshot` (cloud copy, may lag a few seconds) or `exportAsync` saved to disk.
- **Return values flood context.** Don't return base64 images inline; let the tool save oversize
  output to a file and decode it there.
- **Plugin errors show the designer a red toast.** A crashed read-only script changes nothing, but
  say so.
