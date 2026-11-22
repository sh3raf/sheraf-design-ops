# Changelog

## 0.5.3

- Fixes from the full re-run (`tests/results/2026-11-23/report.md`): people's names only from the
  designer or the catalogue, never from the environment; a fixed product code (first 5 letters of the
  product name); an Update row for an entry with no file says so in the table; ds-fixer asks one
  question per turn and, with no connector, gives only the steps, the notes and at most one question.

## 0.5.2

- `ds-ux-patterns` asks one question per turn, never a numbered list beside the table, and does not
  re-ask skipped items. Client modules are switched on from the screens and confirmed in the summary
  instead of seven questions.

## 0.5.1

- Fixes from the first independent test run (`tests/results/2026-11-20/report.md`):
  `ds-ux-patterns` asks, then ends its turn; shows the proposal table and waits for a yes in every run;
  writes only approved rows; never puts `TBD` in an ID or file name; fills `uses` / `used_by` both ways.
  `ds-ux-patterns` and `ds-fixer` give the setup steps word for word when Figma isn't connected.
- Test kit: `tests/AGENT-TEST.md` (brief for an independent agent), `tests/run_case.py` (one isolated
  headless session per case), fictional fixtures in `tests/fixtures/`.

## 0.5.0

- Shared **Connect** check in `figma-safe-write`, used by every skill: connectors, signed-in account,
  file access, edit rights, and the Figma tool's own guide; plain fix-it steps for the designer
  (`/mcp`, Desktop Bridge plugin). The setup guide moved inside the plugin and was rewritten for designers.
- `ds-ux-patterns` intake: a look-first checklist (product name and codename, ID codes, IDs in use,
  flows and screens in scope, library, catalogue location, owner and approver), one question at a
  time with a default and a reason. Missing answers become `TBD` plus an **Open questions** section,
  never invented and never blocking. Scope stated before the first write.
- Catalogue **Overview** (Markdown index or Figma frame) with the next free ID; patterns move from
  proposed to active only on the approver's yes. Doc kit gains IndexRow and OpenQuestion.
- Designer guides per skill in `docs/guides/`, and prompt-first evals in `evals/`.

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
