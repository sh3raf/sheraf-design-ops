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
| `Doc/TypeTag` | Small outlined pill: "Page template", "Flow" or "Example" | `type` |
| `Doc/PatternId` | Monospaced ID on the surface colour | `id` |
| `Doc/MetaTable` | Four columns: Product, Platform, Version, Last updated | `product`, `platform`, `version`, `updated` |
| `Doc/RegionBadge` | 24 px accent circle with a number or "3a" | `number` |
| `Doc/RegionRow` | Badge + label, label wraps | `label` |
| `Doc/PropertyRow` | Key (fixed 160 px) + value, hairline below | `key`, `value` |

## Frames per pattern
- **Section** `<ID> · <Name>` holding two frames side by side.
- **Template frame** (1056 wide, 2300 for flows): Header, TypeTag, PatternId + title, one-sentence
  description, MetaTable, wireframe panel (grey blocks, one RegionBadge per region; flows show step
  wireframes with arrows and a branch card), then Regions (or Steps) and Key properties side by side.
- **Example frame**: same header block, then the real screen at 375 (or the platform width) on the
  surface colour; flows show each step's screen with a caption `<n> · <step>`.

## Key properties to fill
Layout, Platform, Variants, Data states (loading, empty, error), Accessibility, Customisation, Library
(the components used). Flows add Type, Entry points, Exit, Branches and Platform differences.
