# Figma doc kit

A neutral, minimal set of components for pattern documentation. Build it once per pattern-library file
in a section named `Pattern Doc Kit`, then reuse instances. If the team already has a doc template, use
theirs instead.

## Look
- **Neutral:** white page, one grey surface, one hairline, one ink colour, one accent. No gradients,
  no shadows, no brand colours, no logo unless the team asks for one (then use the brand library's
  official logo component and check its render).
- **Type:** the product's font (read it from the reference); fall back to the platform font.
- **Defaults:** ink `#18181B`, muted `#71717A`, surface `#F4F4F5`, hairline `#E4E4E7`, accent `#2563EB`.
  Bind to the library's neutral tokens when it has them.
- **Spacing:** 4-based (8, 12, 16, 24, 32, 40). Radius 8 for chips and rows, 12 for panels.

## Components (all auto layout, text exposed as component properties)

| Component | Contents | Properties |
|---|---|---|
| `Doc/Header` | Library name left, "Pattern Library" right, hairline below | `library` |
| `Doc/TypeTag` | Small outlined pill: "Interaction", "Page template", "Flow" or "Example" | `type` |
| `Doc/StatusTag` | Small filled pill: proposed, active, deprecated | `status` |
| `Doc/PatternId` | Monospaced ID on the surface colour | `id` |
| `Doc/Title` | PatternId on top, the pattern's screen or flow name below (32 px); the same in every frame | `name`, nested `id` |
| `Doc/MetaTable` | Product (codename), Platform, Version, Owner, Last updated | one per column |
| `Doc/IndexRow` | ID, name, type, status, owner, last reviewed, for the Overview | one per column |
| `Doc/OpenQuestion` | A "TBD" tag, the question and who can answer, on the surface colour | `question`, `who` |
| `Doc/RegionBadge` | 24 px accent circle with a number or "3a" | `number` |
| `Doc/RegionRow` | Badge + label, label wraps | `label` |
| `Doc/PropertyRow` | Key (fixed 160 px) + value, hairline below; height hugs | `key`, `value` |
| `Doc/Section` | Section title + body text, for Purpose, Usage, Behaviour, Content, Accessibility | `title`, `body` |
| `Doc/DoDont` | Two cards side by side, each a wireframe **slot** (so sketches can go in instances), a green "Do" or red "Don't" label and a reason | `do`, `dont` |
| `Doc/StateChip` | Small chip naming one state | `state` |
| `Doc/PatternLink` | ID + name of a related pattern | `id`, `name` |

## Overview frame (first on the page)
Header; Title "Pattern catalogue" with the product name; a MetaTable for the catalogue (product and
codename, platforms, library, client modules, owner, approver, next free ID); then one IndexRow per
pattern in ID order. Update it on every run; number new patterns from it.

## Frames per pattern
- **Section** `<ID> · <Name>` holding two frames side by side.
- **Template frame** (1056 wide; 2300 for flows), top to bottom: Header; TypeTag + StatusTag; Title (code on
  top, name below); Purpose; MetaTable; the anatomy panel (wireframe with RegionBadges; flows show step wireframes
  with arrows and a branch card); Anatomy list and Key properties side by side; Usage; Behaviour; States
  (a row of StateChips); Content; Accessibility; Do / Don't; one Section per client module that is on;
  Related (PatternLinks to parents and children); Open questions while anything is `TBD`. Only
  sections the schema calls for.
- **Example frame**: same header block and Title, then the real screen at the platform width on the surface
  colour; flows show each step's screen with a caption `<n> · <step>`.

## Key properties to fill
The type module's fields (`pattern-schema.md`): interaction (trigger, feedback, motion, where it
appears), page (layout, grid, responsive behaviour, visibility rules), flow (entry points, exit,
branches, error recovery, abandon and resume, success measure), plus Variants and Library.
