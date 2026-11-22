![sheraf design ops icon](assets/icon.png)

# sheraf design ops

Design-ops skills for designers working in Figma: turn review notes into fixes that stay on your
design system, and keep a living catalogue of your product's UX patterns.

| Skill | What it does |
|---|---|
| `ds-fixer` | Resolves a round of review notes on a Figma screen against your design-system libraries. It classifies each note (safe, deviation, library bug, owner decision), shows you the plan before changing anything, fixes the library when it is wrong, and reports every deviation with an ID. |
| `ds-ux-patterns` | Asks about the product, finds page, flow and interaction patterns in its real screens, and writes a catalogue in Markdown or as Figma pages, with pattern IDs, a numbered template and a real example. Unknowns stay `TBD` with an open question; nothing is invented. |
| `figma-safe-write` | The safety rules every skill loads before a Figma write: check the connection, save a named version, try one sample, screenshot, then do the rest. |

## Use it

Type `/sdops:ds-fixer` with your review notes and a Figma link, or `/sdops:ds-ux-patterns` with the
screens to document. You can also ask in your own words ("document the booking flow as a UX
pattern", "fix these review notes on the dashboard"). To check your Figma connection first, ask
"check my Figma setup for sdops". Every skill shows you a table and waits for your yes before it
writes anything, and it never publishes a library: that stays your click.

Step-by-step guides: [ds-fixer](https://github.com/sh3raf/sheraf-design-ops/blob/main/docs/guides/ds-fixer.md),
[ds-ux-patterns](https://github.com/sh3raf/sheraf-design-ops/blob/main/docs/guides/ds-ux-patterns.md).

## What it needs

A Figma connection you set up yourself: the official Figma MCP server (Claude's Figma connector), or
the Figma Console MCP server with its Desktop Bridge plugin for writes in the Figma desktop app.
Without either, the skills plan and report but change nothing. Markdown catalogues need no Figma
connection.

## Data

The plugin contains only instructions; it runs no code, starts no server and stores nothing. It reads
and writes your Figma files only through the Figma connection you have already authorised, and writes
Markdown files only in the folder you work in. It sends nothing to any other service.

## Licence

MIT. Issues and questions: [github.com/sh3raf/sheraf-design-ops/issues](https://github.com/sh3raf/sheraf-design-ops/issues).
