# Guide: fix review notes on the design system

`/sdops:ds-fixer` takes the notes a reviewer left on a Figma screen and, for each one, fixes it the
on-system way, fixes the library when the library is wrong, or logs it as a deviation. You get a
report the client can read.

## Before you start (once)
Connect Claude to Figma: [setup guide](../../plugins/sdops/skills/figma-safe-write/references/setup.md).
Then ask "check my Figma setup for sdops".

## 1. Start it
```
/sdops:ds-fixer Fix the client's notes on the dashboard: <Figma link to the screen>.
R-01 the icons next to the amounts look off. R-02 the container should be grey, cards white.
Libraries: <tokens file link>, <components file link>.
```
No IDs on the notes? It numbers them for you.

## 2. Answer a few questions
Only what it can't find: the library files, whether you can edit them, and the branch to work on.

## 3. Approve the plan
For each note you see one of four answers:

| Answer | Means |
|---|---|
| Safe | The library already does it: it switches the option |
| Deviation | Only possible as an override: done, and logged with an ID (D-01...) |
| Library bug or gap | Fixed in the library, if you can edit it |
| Your decision | A judgement call: it recommends one answer and waits |

Nothing changes before you say yes.

## 4. While it works
It saves a named version first, tries one sample, shows you a screenshot, then does the rest. If it
changed a library, it gives you the publish message: **publishing is always your click**. After you
publish, say "done" and it updates the screens.

## 5. What you get
A report: what was fixed, library updates, decisions, deviations with IDs, and what is still open.
See [a sample](../../examples/sample-review-round.md).

## If something goes wrong
| You see | Do |
|---|---|
| "Can't see the file" | Open it in Figma Desktop and run **Plugins → Development → Figma Desktop Bridge** |
| "Read-only" | It can still deliver the plan and the report; ask the file owner for edit access to fix |
| A change you don't want | **File → Show version history**, restore the version named in the report |
