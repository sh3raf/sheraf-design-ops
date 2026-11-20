# sdops skill test, 2026-11-20
Model under test: as configured in tests/run_case.py (not stated in runner output) · Runner: tests/run_case.py · Cases run: 9 of 11 · Cost: about $1.28

## Summary
| Case | Skill | Turns | Pass | Partial | Fail |
|---|---|---|---|---|---|
| fix-no-connection | ds-fixer | 1 | 2 | 1 | 0 |
| fix-trigger-no-slash | ds-fixer | 1 | 1 | 0 | 0 |
| safe-setup-check | figma-safe-write | 1 | 4 | 0 | 0 |
| ux-missing-codename | ds-ux-patterns | 2 | 3 | 1 | 1 |
| ux-designer-skips | ds-ux-patterns | 1 | 4 | 0 | 2 |
| ux-no-connection | ds-ux-patterns | 1 | 2 | 1 | 0 |
| ux-existing-catalogue | ds-ux-patterns | 1 | 4 | 1 | 1 |
| ux-no-evidence | ds-ux-patterns | 2 | 3 | 0 | 0 |
| ux-trigger-no-slash | ds-ux-patterns | 2 | 1 | 0 | 0 |

## Cases
### fix-no-connection
- PASS · Connect check, no connector — "A search for Figma tools found neither the Figma Console bridge (`figma_execute`) nor the official Figma MCP"
- PARTIAL · Setup steps naming /mcp and Desktop Bridge — says "connect the Figma Console bridge or the official Figma MCP", but never names `/mcp` or the Figma Desktop Bridge plugin path.
- PASS · Changes nothing, plan marked not inspected — "Nothing below is a measurement. It's a plan to check once a connection exists." files in work: [].
Transcript: fix-no-connection/turn-*.jsonl

### fix-trigger-no-slash
- PASS · Loads sdops:ds-fixer unprompted — runner shows `skills: ['sdops:ds-fixer']`.
Transcript: fix-trigger-no-slash/turn-*.jsonl

### safe-setup-check
- PASS · Loads figma-safe-write — `skills: ['sdops:figma-safe-write']`.
- PASS · Neither MCP nor Bridge answers — table: "Not available" for both.
- PASS · Plain steps — "Type `/mcp` ... Choose figma → Authenticate", "Plugins → Development → Figma Desktop Bridge".
- PASS · Right account — "sign in with the account that owns your files" (it does not say "the account that can open the client's files").
Transcript: safe-setup-check/turn-*.jsonl

### ux-missing-codename
- PASS · Reads README/notes first — Read, Glob; does not ask product name, platform or screen size.
- PARTIAL · One question at a time, default each, says why — turn 1 ended with three questions in one block (product code, owner/approver, which patterns), with no defaults.
- FAIL · Proposes ID in PROD-PLT-#### shape and asks to confirm — wrote `TBD-IOS-0001`; offered "If the code is `LUM`..." only as a rename hint, and wrote files before any confirmation.
- PASS · No Figma needed — "I skipped the Figma connect step because this run is Markdown only."
- PASS (extra) · Turn 2 changed nothing and kept TBD.
Transcript: ux-missing-codename/turn-*.jsonl

### ux-designer-skips
- PASS · TBD for codename/owner/approver, no invented names — index.md "codename TBD", pattern `owner: TBD`.
- PASS · Status proposed — `status: proposed`.
- PASS · Open questions section — present, lists codename, owner/approver, modules, behaviour gaps.
- PASS · Branch 3a, entry points, exit — "3a payment declined", "Entry points: Home search results, Saved list", "Exit: Confirmation → Trips tab".
- PASS · Does not stop; writes files — ux-patterns/LUM-IOS-0001-book-a-stay.md, index.md.
- FAIL · Proposal table before writing — went straight to Write in turn 1, no table shown.
- FAIL · (implied) ID convention confirmed — `LUM-IOS-####` invented from "Lumen"; flagged only after writing.
Transcript: ux-designer-skips/turn-*.jsonl

### ux-no-connection
- PASS · Notices no connector — "No Figma tools are loaded".
- PASS · Setup steps naming /mcp and Desktop Bridge — both named.
- PARTIAL · Blocked on designer, writes nothing — correct, but the session loaded `sdops:figma-safe-write`, not `ds-ux-patterns`, so the slash command was not honoured as that skill.
Transcript: ux-no-connection/turn-*.jsonl

### ux-existing-catalogue
- PASS · Reads index first, reuses conventions — index shows `codename HALO`, `LUMN-IOS-#### `kept.
- PASS · Numbers LUMN-IOS-0005 — file `LUMN-IOS-0005-saved.md`.
- PASS · No re-ask of owner/approver/modules — owner "Lumen design team" copied.
- FAIL · Proposal table before writing — none shown; wrote directly.
- PARTIAL · Links to 0003/0004 — "Related" cites 0003 and 0001; 0004 (skeleton/states) not linked; frontmatter `uses: []`, "No formal uses/used_by links yet", and the index row's Uses cell is empty.
- PASS · Updates index and Next free ID — "Next free ID: LUMN-IOS-0006".
Transcript: ux-existing-catalogue/turn-*.jsonl

### ux-no-evidence
- PASS · Says no refund screen, asks — "no evidence at all ... I'm not going to infer a refund flow".
- PASS · No refund pattern written — turn 2: "Declined: the refund flow, noted in the index."
- PASS · Checkout treated as booking flow, asks — "I think that's your checkout, but I won't assume it."
Transcript: ux-no-evidence/turn-*.jsonl

### ux-trigger-no-slash
- PASS · Loads sdops:ds-ux-patterns — `skills: ['sdops:ds-ux-patterns']`.
Transcript: ux-trigger-no-slash/turn-*.jsonl

## Other findings
1. Proposal table skipped when the prompt is a slash command (ux-designer-skips, ux-existing-catalogue, ux-missing-codename). In the three non-slash/non-skip runs (ux-trigger-no-slash, ux-no-evidence) a table was shown first. Slash runs show `skills: none` in the runner, so the SKILL's flow (table, confirm) may not be loaded at all; they appear to follow a generic path.
2. Invented ID prefix: `LUM-IOS-####` assumed from "Lumen" and written to files without confirmation (ux-designer-skips; ux-no-evidence and ux-trigger-no-slash asked only after proposing). In ux-no-evidence turn 2 the designer never confirmed the code, yet the session wrote five files with LUM IDs. In ux-trigger-no-slash turn 2 the designer said "skip, I don't know" and the session still wrote ten LUM-IOS files.
3. Over-scope in ux-trigger-no-slash turn 2: wrote 10 patterns (including skeleton, tab bar, carousel, error recovery) when the designer only answered intake. Interaction patterns were proposed in turn 1, and "yes, go ahead" was never given for the table.
4. ux-no-connection routed to figma-safe-write, not ds-ux-patterns, so the pattern-library-specific guidance (read catalogue, evidence rule) was not reached.
5. ux-missing-codename wrote a file named `TBD-IOS-0001-home.md`: a placeholder baked into the filename and ID, so a rename is needed later.
6. ux-existing-catalogue fixture: index links `LUMN-IOS-0001-home.md` but the fixture has no such file (broken link, flagged by the session). Also the session added the Saved row but left its "Uses" cell empty.
7. Wording: fix-no-connection says "connect the Figma Console bridge" without the `/mcp` and Plugins path a designer would follow.
8. Ask-once-then-write habit: ux-existing-catalogue turn 1 ended with a 7-item question list after writing, instead of one question at a time.

## Suggested skill changes
- plugins/sdops/skills/ds-ux-patterns/SKILL.md: make "show the proposal table and wait for yes before any Write" a hard step, including for slash-command runs. Fixes finding 1.
- ds-ux-patterns/SKILL.md: never write an ID prefix that the designer or index has not confirmed; ask once with a default, else stop. Fixes findings 2, 5.
- ds-ux-patterns/SKILL.md: write only the patterns the designer confirmed in the table; list extras as suggestions. Fixes finding 3.
- ds-ux-patterns/SKILL.md: when linking, fill `uses` and the index "Uses" cell for patterns in the catalogue. Fixes ux-existing-catalogue partial.
- ds-ux-patterns/SKILL.md: ask one question per turn with a default and a why. Fixes ux-missing-codename partial and finding 8.
- ds-ux-patterns/SKILL.md (description/triggers): make "Add ... to our Figma pattern library" route to ds-ux-patterns, which then calls the connect check. Fixes finding 4.
- ds-fixer/SKILL.md: add the `/mcp` and Desktop Bridge plugin steps to the no-connection reply, or point to figma-safe-write setup.md. Fixes finding 7.

## Not run
- fix-read-only: needs live-figma (manual).
- fix-library-bug: needs live-figma (manual).

## Re-run after fixes (same day, `tests/results/2026-11-20-rerun/`)
Reviewer check of the findings: the skill *was* loaded in slash runs (verified headless: the session
quoted "## 2. Intake: look first, then ask"); the runner simply couldn't see slash loads (now shown as
"(slash)"). Finding 4 is withdrawn: ds-ux-patterns correctly loaded figma-safe-write for its Connect
step. Root cause of findings 1–3, 5, 8: the skill's "a TBD never blocks the run" read as "write now";
fixed with an ask-then-end-turn rule, a hard table gate, no TBD in IDs or file names, and writing only
approved rows. Fixture index had a broken link (removed).

| Case | Turn 1 now | Result |
|---|---|---|
| ux-missing-codename | Asks one question (product code, default `LUM`, says why), writes nothing | PASS |
| ux-designer-skips | Writes nothing, shows the table, waits; TBDs kept; bundles 3 questions | PASS, minor |
| ux-existing-catalogue | Table first; after "yes" writes 0005–0007 with `uses`/`used_by` both ways, index Uses filled, next ID 0008 | PASS |
| fix-no-connection | Loads figma-safe-write; gives `/mcp` and Desktop Bridge steps word for word; writes nothing | PASS |

Open: ux-designer-skips still bundles three questions in one turn (allowed as one confirmation list,
but not one at a time).
