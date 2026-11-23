<img src="plugins/sdops/assets/icon.png" alt="" width="96">

# sheraf design ops

**Turn design review notes into fixes that stay on your design system, and a report the client can read.**

Claude Code skills for designers working in Figma, packaged as the `sdops` plugin.

| Skill | What it does |
|---|---|
| `/sdops:ds-fixer` | Resolves a round of review notes on a Figma screen against your design-system libraries, fixes the libraries when they're wrong, and reports every deviation. |
| `/sdops:ds-ux-patterns` | Interviews you about the product, detects page and flow patterns in its real screens, and keeps a living catalogue in Markdown or as Figma pages (neutral doc kit, pattern IDs, numbered template and real example). |
| `/sdops:figma-safe-write` | The shared safety rules and Figma gotchas every sdops skill loads before writing to a file. |

## Who it's for

Designers and design-system teams who get review notes on a Figma screen ("the pills are the wrong
colour", "make the container grey") and need to know, for each one: can the library already do this,
is it an off-system override, or is the library itself wrong?

## What `/sdops:ds-fixer` does in detail

1. **Inspects first, read-only:** what the screen uses, what the libraries offer, what the original design did.
2. **Classifies every note** and shows you the table before touching anything:

   | Class | Means |
   |---|---|
   | Safe | A library option already does it |
   | Deviation | Only possible as an override, logged with a D-id |
   | Library bug or gap | Fixed in the tokens or components library when you can edit it |
   | Owner decision | A judgement call: it recommends one answer and asks |

3. **Fixes safely:** saves a named version in every file first, dry-runs, applies to one sample,
   screenshots, then does the rest.
4. **Fixes at the source when it can:** adds the missing variant or token in the library, drafts the
   publish message, and after you publish and update, switches every instance and removes the old overrides.
5. **Reports:** what was fixed, library updates, decisions, deviations with IDs, and what is still pending.

See a full, anonymised run in [`examples/sample-review-round.md`](examples/sample-review-round.md).

## Field results

Measured on one real client review round (client details withheld):

| | |
|---|---|
| Review notes resolved | 5 fixes and 4 owner decisions |
| Fixed at the source, in the libraries | 3 components (25 variants added or fixed) and 2 new tokens |
| Instances updated in the product file | 216 buttons, 115 currency signs, 23 cards and every flag |
| Status chips checked against their label | 887 (4 had the wrong colour) |
| Deviations left at the end | 3, each with an ID and a reason |
| Safety | A broken variant was caught on the first of 23 cards and reverted, with no content lost; a named version was saved before every write session |

Estimate: about 1,250 instance edits that would otherwise have been done by hand (the sum of the
counts above, not a time figure).

## Quick start

```
/plugin marketplace add sh3raf/sheraf-design-ops
/plugin install sdops@sdops
```

Connect Figma: type `/mcp`; if **figma** isn't listed, run
`claude mcp add --transport http figma https://mcp.figma.com/mcp`, then choose **figma → Authenticate**
(full steps in the [setup guide](plugins/sdops/skills/figma-safe-write/references/setup.md)). Ask
"check my Figma setup for sdops" to confirm. Then open the Figma file and:

```
/sdops:ds-fixer Here are the client's notes on the dashboard: R-01 the icons next to the metrics look off,
R-02 the container should be grey and the cards white, R-03 status pills should match their text colour.
```

Or start a pattern catalogue:

```
/sdops:ds-ux-patterns Document the UX patterns of our booking app (iOS and web). Reference screens are on
the "Flows" page of this Figma file.
```

## Guides

Step by step, with the questions each skill asks and what you get:
[document your UX patterns](docs/guides/ds-ux-patterns.md) ·
[fix review notes](docs/guides/ds-fixer.md).

## Needs

Setup takes about 5 minutes: see the [setup guide](plugins/sdops/skills/figma-safe-write/references/setup.md). Then ask Claude "check my Figma setup for sdops".

- **Official Figma MCP** (`use_figma`), to search your libraries, screenshot any file and write.
- **Figma Console MCP** with its Desktop Bridge plugin, for fast local reads and writes in open files.
- **Edit access to the libraries**, if you want library bugs and gaps fixed at the source instead of
  logged as deviations.

Without any write connector, `ds-fixer` stops after the classification and delivers the plan and the
report, changing nothing. The official MCP has a daily call limit and the bridge runs one script at a
time; the skills plan around both.

## Privacy

The official Figma MCP is a cloud service, so what it reads leaves your machine; the bridge works
locally. Reports contain your client's work: the skills anonymise client names in anything meant to
leave the team.

## What it never does

- **Publish a library.** Publishing is always your click; it drafts the message.
- **Write without a saved version.** Every file gets a named version before its first change.
- **Change a library without your yes** on the list of changes.
- **Reset all overrides** on an instance (that would wipe labels and swaps).

## Differences from design-system audit tools

Audit skills scan a whole design system for problems. `ds-fixer` starts from a reviewer's notes on one
screen, decides which fixes are on-system, fixes the libraries when they're wrong, and leaves a record of
every deviation. Use an audit tool to find problems; use `ds-fixer` to resolve a round of review notes.

## Planned skills

Not built yet; each will join `sdops` when it is.

- **ds-hygiene:** "Run a naming, descriptions, text-style or unused-parts pass across this component
  library." Fixes broken sets before renames, traces nested parts up to published components before
  calling them unused, relinks detached copies instead of deprecating, and writes descriptions as
  what it is / when to use / when not to use.
- **ds-theme-match:** "Make this theme or mode match the reference colours across these screens."
  Traces alias chains, fills missing component tokens and audits contrast, confirming text on images
  in a screenshot.
- **ds-branch-merge:** "Prepare, merge and check this Figma library branch." Accepts pending library
  updates in the branch first (or the merge reverts them), writes the merge message, and diffs main
  after the merge.
- **ds-screen-build:** "Build these screens from the reference using only our library." Spec from the
  reference, approved element mapping, build, measure (±2 px geometry, 100% text), overlay review.
  Never inspects network traffic on signed-in pages; redacts captures before sharing.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE) © sheraf. If you use or adapt these skills, a mention of
[sheraf](https://github.com/sh3raf) and a link back to this repo is appreciated.
