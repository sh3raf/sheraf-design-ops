<div align="center">

<img src="plugins/sdops/assets/icon.png" alt="sheraf design ops" width="96">

# sheraf design ops

**Claude Code skills that turn Figma review notes into fixes that stay on your design system,
and keep a living catalogue of your product's UX patterns.**

[![License: MIT](https://img.shields.io/badge/license-MIT-2F6B4F.svg)](LICENSE)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-16181A.svg)](https://docs.anthropic.com/en/docs/claude-code/plugins)
[![Figma](https://img.shields.io/badge/works%20with-Figma-16181A.svg)](https://www.figma.com)

[Installation](#installation) · [Quick start](#quick-start) · [Guides](#guides) ·
[Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

</div>

## Overview

`sdops` is a Claude Code plugin for designers and design-system teams who work in Figma. A reviewer
writes "the pills are the wrong colour" or "make the container grey", and for each note someone has to
decide: can the library already do this, is it an off-system override, or is the library itself
wrong? `sdops` makes that call, shows you the plan, fixes the right layer and records every exception.

| Skill | What it does |
|---|---|
| [`/sdops:ds-fixer`](docs/guides/ds-fixer.md) | Resolves a round of review notes on a Figma screen against your design-system libraries, fixes the libraries when they are wrong, and reports every deviation with an ID. |
| [`/sdops:ds-ux-patterns`](docs/guides/ds-ux-patterns.md) | Finds page, flow and interaction patterns in your real screens and keeps a living catalogue, in Markdown or as Figma pages, with pattern IDs, a numbered template and a real example. |
| `/sdops:figma-safe-write` | The safety rules and Figma gotchas every skill loads before it writes to a file. |

## Installation

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and a Figma account
that can open your files. Edit access to the libraries lets `ds-fixer` fix them at the source.

### Let Claude set it up

Paste this into Claude Code:

```
Set up sdops for me by following https://github.com/sh3raf/sheraf-design-ops/blob/main/docs/agent-setup.md
```

Claude installs the plugin and adds the Figma connection, then asks you to sign in to Figma in your
browser, the one step only you can do. The [instructions it follows](docs/agent-setup.md) are short
and readable. It never asks for your Figma token.

### Manual setup

1. **Install the plugin** from Claude Code:

   ```
   /plugin marketplace add sh3raf/sheraf-design-ops
   /plugin install sdops@sdops
   ```

2. **Connect Figma.** Type `/mcp`. If `figma` isn't listed, add the official Figma MCP server, then
   choose **figma → Authenticate**:

   ```
   claude mcp add --transport http figma https://mcp.figma.com/mcp
   ```

3. **Optional, for large files:** add the [Figma Console MCP](https://github.com/southleft/figma-console-mcp)
   and run its **Desktop Bridge** plugin in the Figma desktop app for fast local reads and writes.

4. **Check the setup.** Ask Claude *"check my Figma setup for sdops"*. It reports which connectors
   work, which account is signed in and whether you can edit the file.

The [setup guide](plugins/sdops/skills/figma-safe-write/references/setup.md) covers each step,
the limits of each connector and how to switch accounts.

## Quick start

Resolve a round of review notes:

```
/sdops:ds-fixer Here are the client's notes on the dashboard: R-01 the icons next to the metrics
look off, R-02 the container should be grey and the cards white, R-03 status pills should match
their text colour.
```

Start a UX pattern catalogue:

```
/sdops:ds-ux-patterns Document the UX patterns of our booking app (iOS and web). Reference screens
are on the "Flows" page of this Figma file.
```

Every skill shows you a table and waits for your approval before it writes anything.

## How `ds-fixer` works

1. **Inspects, read-only:** what the screen uses, what the libraries offer, what the original design did.
2. **Classifies every note** and shows you the plan:

   | Class | Meaning |
   |---|---|
   | Safe | A library option already does it |
   | Deviation | Only possible as an override; logged with an ID |
   | Library bug or gap | Fixed in the tokens or components library, when you can edit it |
   | Owner decision | A judgement call; it recommends one answer and asks |

3. **Applies safely:** saves a named version in every file, dry-runs, changes one sample, checks a
   screenshot, then does the rest.
4. **Fixes at the source:** adds the missing variant or token to the library and drafts the publish
   message. After you publish, it swaps every instance and removes the old overrides.
5. **Reports** what was fixed, the library updates, the decisions, the remaining deviations and
   what is still pending.

See an anonymised end-to-end run in [`examples/sample-review-round.md`](examples/sample-review-round.md).

## Results

From one real client review round (client details withheld):

| Measure | Result |
|---|---|
| Review notes resolved | 5 fixes and 4 owner decisions |
| Fixed at the source | 3 components (25 variants added or fixed) and 2 new tokens |
| Instances updated | 216 buttons, 115 currency signs, 23 cards and every flag |
| Status chips checked against their label | 887 (4 had the wrong colour) |
| Deviations left | 3, each with an ID and a reason |
| Safety | A broken variant was caught on the first of 23 cards and reverted with no content lost |

That is about 1,250 instance edits that would otherwise have been made by hand.

## Guides

- [Fix review notes with `ds-fixer`](docs/guides/ds-fixer.md)
- [Document your UX patterns with `ds-ux-patterns`](docs/guides/ds-ux-patterns.md)
- [Connect Claude to Figma](plugins/sdops/skills/figma-safe-write/references/setup.md)

## Safety and privacy

- **Never publishes a library.** Publishing stays your click; the skill drafts the message.
- **Never writes without a saved version.** Every file gets a named version before its first change,
  so any round can be undone from **File → Show version history**.
- **Never changes a library without your approval** of the list of changes.
- **Never resets all overrides** on an instance, which would wipe labels and swaps.
- **Runs no code of its own.** The plugin is instructions only and sends nothing to any service
  besides the Figma connection you authorise. The official Figma MCP is a cloud service; the Desktop
  Bridge works locally. Client names are anonymised in anything meant to leave the team.

Without a write connection, the skills still plan and report, and change nothing.

## How it differs from audit tools

Audit tools scan a whole design system for problems. `ds-fixer` starts from a reviewer's notes on one
screen, decides which fixes are on-system, fixes the libraries when they are wrong and keeps a record
of every deviation. Use an audit tool to find problems; use `ds-fixer` to resolve a review round.

## Roadmap

Planned skills, not built yet:

- **ds-hygiene:** naming, descriptions, text styles and unused parts across a component library.
- **ds-theme-match:** make a theme or mode match reference colours, with contrast checks.
- **ds-branch-merge:** prepare, merge and verify a Figma library branch.
- **ds-screen-build:** build screens from a reference using only your library, then measure the result.

## Contributing

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how to set up the
checks and test a skill change. Please leave client names and file links out of issues.

## License

Released under the [MIT License](LICENSE). Copyright © 2026 sheraf.
