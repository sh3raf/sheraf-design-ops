# Report template

Add one section per review round to the client report. Plain sentences, no internal node IDs.

```markdown
## Review round, <date>

### Fixed
- **<Note, with the reviewer's ID>:** what it looks like now, and the token or component it uses.

### Library updates made for this round
- **<Components library>:** new variants or fixes, one clause each.
- **<Tokens library>:** new or changed tokens, with what they are for.

### Decisions
- **<ID>, <topic>:** the answer, in one sentence. Mark any the designer has not confirmed.

### Deviations from the libraries
- **D-01, <short name>:** what is overridden, the token used, and why the library can't do it yet.
```

## Publish message

One line per change, said as the outcome a library user will see. Flag anything that changes
existing screens in other files:

```
<Component>: new type=<x> for <when to use it>.
<Component>: <what was wrong> fixed. <What looks different after updating>.
New tokens: <Token> (<value>) for <use>.
```

## Library backlog

List findings for the library teams separately from deviations: bugs found, missing options,
misleading descriptions. One line each, with the component or token name.
