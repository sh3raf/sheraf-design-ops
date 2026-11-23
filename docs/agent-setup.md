# Set up sdops: instructions for Claude

You are Claude Code, setting up the `sdops` plugin for the person you're working with. Follow the
steps in order. Before each command, say in one line what it does. Run the commands yourself, except
where a step says the person must act. Never ask for, repeat or store a Figma token or password.

## 1. Install the plugin

Run `claude plugin list`. If `sdops@sdops` is already listed, skip to step 2. Otherwise run:

```
claude plugin marketplace add sh3raf/sheraf-design-ops
claude plugin install sdops@sdops
```

If the marketplace can't be reached, tell the person they may need access to the GitHub repository,
and stop.

## 2. Add the official Figma MCP server

Run `claude mcp get figma`. If it isn't found, run:

```
claude mcp add --transport http --scope user figma https://mcp.figma.com/mcp
```

## 3. Sign in to Figma (the person does this)

Run `claude mcp get figma` again. If the status says it needs authentication, tell the person:

> Type `/mcp`, choose **figma → Authenticate** and sign in in the browser with the Figma account
> that can open your files (usually your work account). Tell me when it's done.

Wait for their reply, then run `claude mcp get figma` once more and confirm it's connected.

## 4. Optional: the Figma Desktop Bridge, for large files

Ask once: "Do you also want the Figma Desktop Bridge? It's faster for large files and needs a Figma
personal access token." If they say no, skip to step 5.

If yes, tell them to do these steps themselves, so the token never appears in this chat:

1. In Figma, open **Settings → Security → Personal access tokens** and create a token.
2. In a terminal (not in this chat), run, with their token in place of `figd_...`:
   ```
   claude mcp add figma-console -s user -e FIGMA_ACCESS_TOKEN=figd_... -e ENABLE_MCP_APPS=true -- npx -y figma-console-mcp@latest
   ```
3. In the Figma desktop app, open the file and run
   **Plugins → Development → Figma Desktop Bridge** (setup details:
   [figma-console-mcp](https://github.com/southleft/figma-console-mcp)).

## 5. Restart and check

Tell the person to start a new Claude Code session so the plugin and servers load. In that new
session they ask **"check my Figma setup for sdops"**. The check reports which connectors work, which
account is signed in and whether they can edit the file.

## 6. Finish

Summarise what is installed, what was skipped and the next step, for example:

```
/sdops:ds-ux-patterns Document the onboarding flow of <product> (iOS). Screens: <Figma link>.
```

Guides: [document UX patterns](https://github.com/sh3raf/sheraf-design-ops/blob/main/docs/guides/ds-ux-patterns.md) ·
[fix review notes](https://github.com/sh3raf/sheraf-design-ops/blob/main/docs/guides/ds-fixer.md).
