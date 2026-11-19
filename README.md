# sheraf design ops

Claude Code skills for design-system work in Figma, packaged as the `sdops` plugin.

| Skill | What it does |
|---|---|
| `/sdops:ds-fixer` | Checks, fixes and reports a Figma screen against its design-system libraries: classifies each review note as safe, deviation, library bug or owner decision, fixes in the library when you can edit it, and writes the report. |

## Install

```
/plugin marketplace add sh3raf/sheraf-design-ops
/plugin install sdops@sdops
```

From a local clone: `/plugin marketplace add ./sheraf-design-ops` instead of the first line.

## Needs

- Figma Desktop with the Figma Console bridge plugin, for writes.
- The official Figma MCP, for library search and screenshots of other files.
- Edit access to the libraries, if you want fixes made there instead of logged as deviations.
