# sheraf design ops

**Turn design review notes into fixes that stay on your design system, and a report the client can read.**

Claude Code skills for designers working in Figma, packaged as the `sdops` plugin.

## Who it's for

Designers and design-system teams who get review notes on a Figma screen ("the pills are the wrong
colour", "make the container grey") and need to know, for each one: can the library already do this,
is it an off-system override, or is the library itself wrong?

## What `/sdops:ds-fixer` does

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

## Quick start

```
/plugin marketplace add sh3raf/sheraf-design-ops
/plugin install sdops@sdops
```

Open the Figma file, then:

```
/sdops:ds-fixer Here are the client's notes on the dashboard: R-01 the icons next to the metrics look off,
R-02 the container should be grey and the cards white, R-03 status pills should match their text colour.
```

## Needs

- **Figma Console MCP** with its Desktop Bridge plugin running in Figma, to read and write files.
  Without it the skill stops after the classification and delivers the plan and the report, changing nothing.
- **Official Figma MCP**, to search your libraries' tokens and components and to screenshot other files.
- **Edit access to the libraries**, if you want library bugs and gaps fixed at the source instead of logged as deviations.

## What it never does

- **Publish a library.** Publishing is always your click; it drafts the message.
- **Write without a saved version.** Every file gets a named version before its first change.
- **Change a library without your yes** on the list of changes.
- **Reset all overrides** on an instance (that would wipe labels and swaps).

## Differences from design-system audit tools

Audit skills scan a whole design system for problems. `ds-fixer` starts from a reviewer's notes on one
screen, decides which fixes are on-system, fixes the libraries when they're wrong, and leaves a record of
every deviation. Use an audit tool to find problems; use `ds-fixer` to resolve a round of review notes.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

[MIT](LICENSE) © sheraf. If you use or adapt these skills, a mention of
[sheraf](https://github.com/sh3raf) and a link back to this repo is appreciated.
