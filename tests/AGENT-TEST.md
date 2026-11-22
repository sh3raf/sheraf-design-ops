# Full skill test: brief for an independent agent

You test the `sdops` skills as an outsider. You did not write them; judge only what the sessions do.
Every case runs in a **fresh, isolated Claude Code session** that has only the sdops plugin, no Figma
connection, no user memory and a folder copied from a fictional fixture. You play the designer.

## Rules
- Run sessions only through `tests/run_case.py`. Never run the skills yourself, never connect Figma,
  never edit `plugins/`, `evals/` or `plugins/sdops/evals/fixtures/`.
- Play the designer from the fixture's `designer.md` only. Answer briefly, only what is asked. Never
  volunteer facts, never coach the session, never mention the expectations.
- At most **4 turns per case**. Stop earlier when the session finishes, blocks or repeats itself.
- Cases with `"needs": "live-figma"` are listed as **not run** (manual).
- Grade only from evidence: quote the session's words or name the file it wrote. No evidence = FAIL.

## Steps
1. `python3 tests/check.py` must print `ok`. Read `evals/*.json` for the cases.
2. Results folder: `tests/results/<YYYY-MM-DD>/` (transcripts there are git-ignored).
3. For each case that can run:
   - `python3 tests/run_case.py <id> --out tests/results/<date>`
   - Read the printed reply. If it asks the designer something, answer from `designer.md`:
     `python3 tests/run_case.py <id> --out tests/results/<date> --reply "<answer>"`
   - When it ends, read any files it wrote in `tests/results/<date>/<id>/work/`.
   - Grade each expectation PASS / FAIL / PARTIAL with one line of evidence.
4. Look across cases for problems no expectation names: invented facts, questions the files already
   answered, wrong IDs, written files with a broken structure, unclear wording a designer wouldn't
   follow, client or real-company names, a person's name taken from the environment (account, git
   user, folder paths), more than one question in a turn, anything unsafe. The report is committed:
   describe a leaked name, never quote it.
5. Write `tests/results/<date>/report.md`:

```markdown
# sdops skill test, <date>
Model under test: <model> · Runner: tests/run_case.py · Cases run: N of M · Cost: $X

## Summary
| Case | Skill | Turns | Pass | Partial | Fail |
|---|---|---|---|---|---|

## Cases
### <id>
- PASS · <expectation> — "<quote>" / <file>
- FAIL · <expectation> — <what happened instead>
Transcript: <id>/turn-*.jsonl

## Other findings
<ranked, most serious first; each with the case and evidence>

## Suggested skill changes
<one line each: file, the change, the finding it fixes>

## Not run
<live-figma cases and why>
```

6. Reply with the summary table, the top three findings and the report path. Change nothing else.
