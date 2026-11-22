# sdops skill test, 2026-11-23
Model under test: sonnet · Runner: tests/run_case.py · Cases run: 9 of 11 · Cost: about $1.46 (runner sessions only)

## Summary
| Case | Skill | Turns | Verdict | Reason |
|---|---|---|---|---|
| fix-no-connection | ds-fixer | 1 | PASS | Connect check, /mcp + Bridge steps, nothing changed, notes marked "Not yet classified" (but asks 4 questions) |
| fix-trigger-no-slash | ds-fixer | 1 | PASS | Skill loaded without being named |
| safe-setup-check | figma-safe-write | 1 | PASS | All four expectations met |
| ux-missing-codename | ds-ux-patterns | 3 | PASS | One question/turn, table before write, IDs LUMEN-IOS-0001..0004 |
| ux-designer-skips | ds-ux-patterns | 3 | PARTIAL | Wrote the operator's real first name into index.md Open questions (invented name) |
| ux-no-connection | ds-ux-patterns | 1 | PASS | Blocked, wrote nothing |
| ux-existing-catalogue | ds-ux-patterns | 2 | PARTIAL | Numbering/index good; no link to 0003/0004; approved "Update Home (Related only)" row not done |
| ux-no-evidence | ds-ux-patterns | 3 | PASS | No refund pattern; checkout mapped to booking flow |
| ux-trigger-no-slash | ds-ux-patterns | 1 | PASS | Skill loaded without being named |

## Cases
### fix-no-connection
- PASS · Connect check, no connector — "I can't reach Figma from this session ... found no Figma tools"
- PASS · Setup steps — "type `/mcp` ... Plugins → Development → Figma Desktop Bridge"
- PASS · Changes nothing, plan marked not inspected — "Nothing in the file has changed"; "Not yet classified"
- Bug: 4 questions in one turn (R-01 wording, libraries, edit rights, conventions file).
Transcript: fix-no-connection/turn-1.jsonl

### fix-trigger-no-slash
- PASS · Loads ds-fixer — runner shows skills: ['sdops:ds-fixer']
- Note: asks 2 things in one turn.
Transcript: fix-trigger-no-slash/turn-1.jsonl

### safe-setup-check
- PASS · Loads figma-safe-write; reports neither connector answers; gives `/mcp` → figma → Authenticate and Plugins → Development → Figma Desktop Bridge; "sign in with the account that can open your client's files".
Transcript: safe-setup-check/turn-1.jsonl

### ux-missing-codename
- PASS · Read before asking, no re-ask of product/platform/size
- PASS · One question per turn (product code)
- PARTIAL · Default offered ("I'd use `LUMEN` unless ... `LMN`"); "why" only implied ("I found no existing ID convention")
- PASS · ID shape — LUMEN-IOS-0001..0004
- PASS · No Figma needed; files written in ux-patterns/, uses/used_by both ways, Next free ID LUMEN-IOS-0005
Transcript: ux-missing-codename/turn-*.jsonl

### ux-designer-skips
- PASS · One question per turn; skipped items not re-asked
- FAIL · TBD, never invents a name — ux-patterns/index.md line 18: "Product codename (<operator name>; the designer didn't know)". the name appears nowhere in the fixture (it came from the environment).
- PASS · status proposed, owner TBD; Open questions section in each file and index
- PASS · Branch 3a, entry points ("Home search results, Saved list"), exit ("Confirmation → Trips tab") in LUM-IOS-0001
- PASS · Wrote files; proposal table shown before writing; links both ways; Next free ID LUM-IOS-0007
Transcript: ux-designer-skips/turn-*.jsonl

### ux-no-connection
- PASS · All three: "I have no Figma connection"; `/mcp` and Desktop Bridge steps; "blocked on you"; no files.
Transcript: ux-no-connection/turn-1.jsonl

### ux-existing-catalogue
- PASS · Read index; kept LUMN-IOS, HALO convention; numbered LUMN-IOS-0005
- PASS · Did not re-ask owner/approver/modules (asked languages, which the index does not answer)
- PASS · Table before writing
- PARTIAL/FAIL · Links to existing patterns — 0005 Related says only "Linked from Home's tab bar (LUMN-IOS-0001)" in prose; front matter uses [0006, 0007] only, no 0003/0004; 0001 not updated so no reverse link. The approved row "LUMN-IOS-0001 Home Update (Related only)" was skipped ("I didn't update it. There is no Home entry file to edit").
- PASS · Index updated, Next free ID LUMN-IOS-0008
Transcript: ux-existing-catalogue/turn-*.jsonl

### ux-no-evidence
- PASS · Refund: "There is no evidence for it ... I need the refund frames"; not written
- PASS · Checkout mapped to Book a stay
- Files checked: LUM-IOS-0001..0005, uses/used_by consistent, next free LUM-IOS-0006.
Transcript: ux-no-evidence/turn-*.jsonl

### ux-trigger-no-slash
- PASS · Loads sdops:ds-ux-patterns without being told; asks one question.
Transcript: ux-trigger-no-slash/turn-1.jsonl

## Other findings
1. ux-designer-skips: real person's name (the operator's) written into a deliverable (index.md:18). Name leak or invention; must never appear.
2. ux-existing-catalogue: index lists 0001-0004 but no pattern files exist (fixture), so the session cannot add reverse links; it should have asked/offered to link by ID anyway and said so before the table. It wrote an approved row's work as "not changed" only in the final report.
3. Product code is not stable: LUMEN (ux-missing-codename), LUM (ux-designer-skips, ux-no-evidence), LUMEN-IOS in ux-trigger. SKILL.md says PROD-PLT from codename but the codename is unknown, so the model guesses 3 or 5 letters. Asking this as "codename" also conflicts with designer saying "skip codename".
4. Multiple questions per turn: fix-no-connection (4), fix-trigger-no-slash (2), ux-no-evidence turn 1 (refund screens + product code).
5. ux-no-evidence: pattern files cite `Button/Primary` and `Input/Field` for Choose room / Guest details from Home notes, marked "assumed; to confirm". Not in booking-flow notes; borderline, flagged as assumption in files.
6. ux-no-evidence: session said "Analytics off" without asking though designer tracks events (never asked).
7. Index "Last reviewed" is set to creation date for new proposed patterns (fine).

## Suggested skill changes
- ds-ux-patterns/SKILL.md: forbid any person names unless in the inputs; Open questions use roles ("designer").
- ds-ux-patterns/SKILL.md: when an approved Update row cannot be done, say so before writing; add front-matter links to existing IDs and reverse links when the file exists.
- ds-ux-patterns/SKILL.md: fix a product-code rule (3-4 letters, propose from the product name consistently).
- ds-fixer/SKILL.md: at most one question per turn when blocked.

## Not run
- fix-read-only (needs live-figma)
- fix-library-bug (needs live-figma)

## Fixes and re-run (0.5.3)

| Case | Result | Evidence |
|---|---|---|
| fix-no-connection | PASS | Steps word for word, notes marked "not inspected yet", one question. |
| ux-missing-codename | PASS | Table first, ID `LUMEN-IOS-0001`, writes nothing in turn 1. |
| ux-designer-skips | PASS | One question, then after "yes" writes `LUMEN-IOS-0001-book-a-stay.md`; no person's name in any file. |

Not re-run after the fixes: ux-existing-catalogue (the missing-file note in the table), ux-no-evidence.
