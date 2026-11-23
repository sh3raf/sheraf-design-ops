# Contributing

- **Found a Figma behaviour the skill gets wrong?** Open an issue with what you asked, what happened
  and what you expected. Leave out client names and file links.
- **Changing a skill:** keep `SKILL.md` to what every run needs; put case-specific detail in
  `references/` behind a line saying when to read it. Edit the line that covers an idea rather than
  adding a new one.
- **Once per clone:** `git config core.hooksPath .githooks`. Every push then runs the checks
  (`tests/check.py`, `claude plugin validate`) and blocks any client name listed in
  `.git/info/private-names` (one per line, kept on your machine only).
- **Testing a skill change:** two suites, on the fictional fixtures in `tests/plugin-evals/fixtures/`.
  - First turn, scored with and without the plugin (`claude plugin eval`, about $5 for the full run):
    `tests/plugin-eval.sh` (the cases live in `tests/plugin-evals/`, outside the plugin folder:
    the directory accepts no scripts there)
  - Whole conversations, played by an independent agent: brief it with `tests/AGENT-TEST.md`.
- **Before a pull request:** add a line to `CHANGELOG.md`.
