# Sample: one review round with ds-fixer

A fictional, anonymised example of what `/sdops:ds-fixer` produces. "Lumen" is a made-up analytics
dashboard built on two made-up libraries, **Acme Tokens** (variables) and **Acme Components**. The
designer could edit both libraries.

## 1. The review notes that came in

> R-01 The icons next to the metrics look off.
> R-02 One customer logo is missing from the list.
> R-03 Invert the colours: the container should be grey, the cards inside it white.
> R-04 Status pills should take the colour of their text.
> R-05 The quick-action buttons on the dark header should be glass, as in the original design.
> R-06 Should "View all" links be underlined?

## 2. Classification (shown to the designer before any change)

| Note | What the inspection found | Class | Fix |
|---|---|---|---|
| R-01 | Icon is 24 px in the link colour beside 15 px text; the original design used 16 px in the text colour | Deviation | Resize to the library icon scale (16 px), recolour with `color/text/primary` |
| R-02 | The logo is white on a white card, so it disappears | Deviation | 1 px hairline border with `color/border/divider` |
| R-03 | The container component has no grey option | Library gap | Add `type=subtle` to Container, on `color/surface/subtle` |
| R-04 | Every Pill colour in the library uses the same blue background | Library bug | Bind each colour to its own tint token |
| R-05 | Button has no option for dark backgrounds; screens fake it with a 90 % white fill | Library gap | Add `type=glass` to Button, on two new alpha tokens |
| R-06 | A judgement call | Owner decision | Recommend: keep the library link's underline |

## 3. What changed

**Acme Tokens** (published first)
- New `color/surface/glass-fill` (white 12 %) and `color/surface/glass-stroke` (white 24 %).

**Acme Components** (published second)
- Button: new `type=glass` (enabled and disabled), bound to the glass tokens.
- Pill: each colour now has its own background tint (fixes all-blue backgrounds).
- Container: new `type=subtle` for grey cards that hold white panels.

**Lumen dashboard** (after Update all)
- 212 buttons switched to `type=glass`; their old white fills removed.
- 23 cards switched to `type=subtle`; their grey overrides removed.
- Metric icons resized to 16 px and recoloured; logos given a hairline border.

## 4. Publish messages drafted for the designer

```
Acme Tokens: new color/surface/glass-fill (white 12%) and glass-stroke (white 24%) for glass controls on dark backgrounds.

Acme Components:
• Button: new type=glass for dark or image backgrounds.
• Pill: each colour now has its own background. Green, yellow and red pills change colour after updating.
• Container: new type=subtle (grey) for cards that hold white panels.
```

## 5. The report section

### Review round, 12 March

**Fixed**
- **R-01 metric icons:** 16 px, in the text colour, 4 px before the value.
- **R-02 missing logo:** visible again, with a hairline border.
- **R-03 container colours:** grey containers, white cards inside.
- **R-04 pill colours:** each pill's background matches its text.
- **R-05 glass buttons:** the header actions use the new glass button.

**Decisions**
- **R-06 "View all" underline:** kept as the library draws it. *(Recommended; awaiting confirmation.)*

**Deviations from the libraries**
- **D-01 icon size and colour:** set per use, as the icon component documents.
- **D-02 logo border:** a 1 px `color/border/divider` border so white logos stay visible.

**Library backlog**
- Glass effect style renders small controls as solid white blocks; buttons set the effect directly.

**Pending:** nothing. All library changes are published and the dashboard is updated.
