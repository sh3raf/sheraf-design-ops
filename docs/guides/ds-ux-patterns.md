# Guide: document your UX patterns

`/sdops:ds-ux-patterns` writes one page per UX pattern of your product (a screen layout, a flow or a
reused behaviour), each with an ID, a numbered template and a real example. It keeps the catalogue
current when the screens change.

## Before you start (once)
Connect Claude to Figma: [setup guide](../../plugins/sdops/skills/figma-safe-write/references/setup.md).
Then ask "check my Figma setup for sdops".

## 1. Start it
Paste a link to the screens and say what you want:

```
/sdops:ds-ux-patterns Document the home screen and the transfer flow of our banking app (iOS).
Screens: <Figma link>. Write the pages in: <Figma link to the pattern file>.
```

## 2. Answer a few questions
Claude looks in your files first and only asks what it can't find, one question at a time, with its
best guess. Press enter on the guess if it's right. It may ask:

| Question | Why |
|---|---|
| Product name and codename | Shown on every page |
| Product and platform code (e.g. `APPX-IOS`) | Builds the pattern IDs: `APPX-IOS-0001` |
| Which flows and screens are in scope | So it documents only what you want |
| Which component library | Examples are built from real library parts |
| Owner and approver | Who keeps it current, who moves a pattern from proposed to active |
| Seven yes/no questions (regulated? sensitive data? languages? platforms? brands? analytics? developers?) | Adds the extra sections your product needs, such as security or right-to-left |

**Don't know an answer?** Say "skip". It writes `TBD`, keeps the pattern as *proposed* and lists the
question on the page and in the report, so someone can answer later. It never makes up a name or a
rule.

## 3. Approve the plan
You get one table: each pattern, its ID, its type, and whether it's new, updated or suggested. Say yes,
or change it. Nothing is written before this.

## 4. What you get
- An **Overview** frame listing every pattern, its status and the next free ID.
- Per pattern, a **Template** frame (purpose, anatomy with numbered regions, behaviour, states,
  content, accessibility, do / don't, related patterns) and an **Example** frame with the real screen.
- A short report: what was added, open questions, and places where the product contradicts its own
  rule.

## Next time
Run it again with new screens: it updates the existing pages, never deletes (it deprecates with a
reason), and numbers new patterns from the overview.

## If something goes wrong
| You see | Do |
|---|---|
| "Can't see the file" | Open it in Figma Desktop and run **Plugins → Development → Figma Desktop Bridge** |
| "No access" or the wrong account | `/mcp` → figma → Clear authentication, sign in with your work account |
| A change you don't want | **File → Show version history**, restore the version named in the report |
