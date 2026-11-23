![sheraf design ops icon](assets/icon.png)

# sheraf design ops

Design-ops skills for designers working in Figma: turn review notes into fixes that stay on your
design system, and keep a living catalogue of your product's UX patterns.

| Skill | What it does |
|---|---|
| `ds-fixer` | Resolves a round of review notes on a Figma screen against your design-system libraries. It classifies each note (safe, deviation, library bug, owner decision), shows you the plan before changing anything, fixes the library when it is wrong, and reports every deviation with an ID. |
| `ds-ux-patterns` | Asks about the product, finds page, flow and interaction patterns in its real screens, and writes a catalogue in Markdown or as Figma pages, with pattern IDs, a numbered template and a real example. Unknowns stay `TBD` with an open question; nothing is invented. |
| `figma-safe-write` | The safety rules every skill loads before a Figma write: check the connection, save a named version, try one sample, screenshot, then do the rest. |

## Set it up (about 5 minutes, once per computer)

1. **Install the plugin.** In Claude Code:
   ```
   /plugin marketplace add sh3raf/sheraf-design-ops
   /plugin install sdops@sdops
   ```
   On Claude Code 2.1.275 or later, one line does both:
   `/plugin install sdops --marketplace sh3raf/sheraf-design-ops`.
2. **Connect Figma.** Type `/mcp`. If **figma** isn't listed, run
   `claude mcp add --transport http figma https://mcp.figma.com/mcp`, then `/mcp` again. Choose
   **figma → Authenticate** and sign in with the Figma account that can open your files.
3. **Optional, for big files:** install the [Figma Console MCP](https://github.com/southleft/figma-console-mcp),
   open the file in the Figma desktop app and run **Plugins → Development → Figma Desktop Bridge**.
4. **Check it.** Ask Claude "check my Figma setup for sdops". It tells you what's connected, which
   account is signed in and whether you can edit the file.

Full steps, limits and privacy notes: [setup guide](https://github.com/sh3raf/sheraf-design-ops/blob/main/plugins/sdops/skills/figma-safe-write/references/setup.md).

## Use it

Type `/sdops:ds-fixer` with your review notes and a Figma link, or `/sdops:ds-ux-patterns` with the
screens to document. You can also ask in your own words ("document the booking flow as a UX
pattern", "fix these review notes on the dashboard"). Every skill shows you a table and waits for your yes before it
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

## Support

Report a problem or ask a question in [GitHub Issues](https://github.com/sh3raf/sheraf-design-ops/issues).

## License

Released under the [MIT License](https://github.com/sh3raf/sheraf-design-ops/blob/main/LICENSE). Copyright © 2026 sheraf.
