# Changelog

## 0.4.0

- `ds-ux-patterns` follows one pattern schema (`references/pattern-schema.md`) in Markdown and Figma:
  core sections for every pattern (identity with status and owner, purpose, usage, anatomy,
  behaviour, states, content, accessibility, do / don't, related, evidence, changelog), a type module
  (new **interaction** type, page template, flow; types nest), and client modules switched on at
  intake (regulated, security & privacy, localisation & RTL, multi-platform, multi-brand, analytics,
  code link).
- Figma doc kit gains StatusTag, Section, DoDont, StateChip and PatternLink, and the template frame
  shows only the sections the schema calls for.

## 0.3.0

- `ds-ux-patterns` writes Figma pattern pages as well as Markdown: a neutral doc kit, a team-set ID
  convention (default PROD-PLT-####), page and flow types, a numbered template and a real example per
  pattern, and a deprecated-component check on the reference.
- New shared skill `figma-safe-write`: the safety protocol and gotchas, loaded by every write skill.
  `ds-fixer` now loads it; the gotchas moved there and gained a Libraries and imports section.

## 0.2.0

- New skill `ds-ux-patterns`: interviews the designer, detects UX patterns from the product's screens
  and keeps a living catalogue (update, add, suggest, deprecate; never delete).
- `ds-fixer`: conventions and branch checks at intake, usage check before changing a main component,
  library-wins rule for reference values, A/B/C library proposals, small batches and read-back after
  timeouts, consumer-file spot check, undo, worklog and measured claims; `use_figma` as a write path;
  plan-only mode with no write connector.
- Gotchas: new Slots, Text, and Variables and modes sections; clone, override and bridge entries
  extended; dated.
- Docs: setup guide, privacy and limits, planned skills.

## 0.1.0

- First release: the `sdops` plugin with `ds-fixer`, the Figma gotchas reference, the report
  template and an anonymised sample review round.
