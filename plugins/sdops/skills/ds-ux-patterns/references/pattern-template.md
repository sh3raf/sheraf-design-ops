# Pattern template

Sections come from `pattern-schema.md`: keep the core, the pattern's type module, and the client
modules listed in the index. Delete module headings that are off.

## Entry: `ux-patterns/<id>-<slug>.md`

```markdown
---
id: <PROD-PLT-####>
name: <Pattern name>
aliases: []
type: interaction | page | flow
category: <from pattern-vocabulary.md>
status: proposed | active | deprecated
owner: <team or person>
version: 1.0
platforms: []
last_reviewed: <YYYY-MM-DD>
uses: [<IDs of child patterns>]
used_by: [<IDs of parent patterns>]
---

# <ID> · <Pattern name>

**Purpose:** <user problem>. <business goal>.

## Usage
- Use when: ...
- Don't use when: ... Use <ID or component> instead.

## Anatomy
1. <region, step or element>

## Behaviour
## States
## Content
## Accessibility
## Do / Don't
- Do: <what> (<why>)
- Don't: <what> (<why>)

## <Type module>
<!-- interaction: trigger → feedback, gestures, motion, where it appears
     page: regions, grid, responsive behaviour, visibility rules
     flow: entry points, exit, steps, branches, error recovery, abandon and resume, success measure -->

## <Client modules>
<!-- one heading per module that is on: Regulated, Security & privacy, Localisation & RTL,
     Multi-platform, Multi-brand, Analytics, Code link -->

## Related
- Patterns: <IDs>
- Components: <library names>

## Evidence
- <screen or frame link>: <what it shows>

## Changelog
- <YYYY-MM-DD>: <what changed and why>

## Open questions
<!-- only while something is TBD -->
- <question> (who can answer; what it blocks)
```

## Index: `ux-patterns/index.md`

```markdown
# UX patterns: <product>

Product: <name> (codename <codename>) · Platforms: <...> · Library: <link>
Owner: <team> · Approver: <person who moves proposed → active>
Client modules: <Regulated, Security & privacy, ...>
ID convention: <PROD-PLT-####> · Next free ID: <PROD-PLT-0005>

| ID | Pattern | Type | Status | Uses | Last reviewed |
|---|---|---|---|---|---|
| <ID> | [<name>](<id>-<slug>.md) | page | active | <IDs> | YYYY-MM-DD |
```
