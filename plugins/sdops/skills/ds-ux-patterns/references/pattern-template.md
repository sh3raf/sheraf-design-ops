# Pattern template

## Entry: `ux-patterns/<pattern-slug>.md`

```markdown
---
name: <Pattern name>
aliases: [<other names used in the team>]
category: <Navigation | Input | Data display | Feedback | Onboarding | Search and filter | Commerce | Account | Content>
status: active | proposed | deprecated
platforms: [web, ios, android, desktop]
last_reviewed: <YYYY-MM-DD>
---

# <Pattern name>

**Problem it solves:** one sentence, from the user's side.

## When to use
## When not to use (and what to use instead)
## Anatomy
Named parts, in reading order.
## States
Default, empty, loading, error, success, disabled: only those that apply.
## Behaviour
Interaction, keyboard, focus, motion.
## Platform notes
## Accessibility
## Built with
Library components and tokens that make it, by their library names.
## Where it appears
- <screen or frame link>: <what this instance shows>

## Changelog
- <YYYY-MM-DD>: <what changed and why>
```

## Index: `ux-patterns/index.md`

```markdown
# UX patterns: <product>

| Pattern | Category | Status | Platforms | Last reviewed |
|---|---|---|---|---|
| [<name>](<slug>.md) | ... | active | web, ios | YYYY-MM-DD |
```
