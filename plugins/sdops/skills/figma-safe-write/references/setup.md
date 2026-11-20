# Connect Claude to Figma (about 5 minutes)

The sdops skills reach Figma through two connectors. One is enough to start; with both you get the
full workflow. Do this once per computer.

| Connector | What it gives you | Needed for |
|---|---|---|
| **Figma MCP** (official, cloud) | Search your libraries, screenshots of any file, writes | Every skill |
| **Figma Desktop Bridge** (local plugin) | Fast reads and writes in the files you have open, saving versions | Big batches, `ds-fixer` library fixes |

## 1. Figma MCP

1. In Claude Code, type `/mcp`.
2. If **figma** isn't listed, add it: `claude mcp add --transport http figma https://mcp.figma.com/mcp`,
   then `/mcp` again.
3. Choose **figma → Authenticate**. A browser window opens: sign in with the Figma account that can
   open your client's files (usually your **work** account, not a personal one).
4. Back in Claude, ask: "who am I in Figma?" It should answer with that account's name.

**Wrong account?** `/mcp` → figma → **Clear authentication**, then authenticate again with the right one.

## 2. Figma Desktop Bridge (optional, recommended)

1. Install the Figma Console MCP server (follow its README), then restart Claude Code.
2. Open the Figma **desktop app** (not the browser) and the file you want to work on.
3. In the file: **Plugins → Development → Figma Desktop Bridge**. Keep the plugin window open.
4. Repeat step 3 in every file the skill should touch (for example the product file and the library).

The bridge only sees files where the plugin is running. If Claude says it can't see a file, run the
plugin in that file again.

## 3. Check it

Ask Claude: **"check my Figma setup for sdops"**. It answers with:
- which connectors work and which Figma account is signed in;
- which open files the bridge sees;
- whether you can **edit** the target files and libraries (only then can fixes happen in a library).

## Limits to know
- The Figma MCP has a daily call limit; the skills use the bridge for big reads to stay under it.
- The bridge runs one script at a time: don't run two skills on it at once.

## Privacy
- The Figma MCP is a cloud service: what it reads leaves your machine. The bridge works locally.
- Reports and screenshots contain your client's work. The skills anonymise client names in anything
  meant to leave the team.

## Undo
Before its first change in a file, a skill saves a named version (or asks you to). To undo a round:
**File → Show version history**, and restore the version named in the report.
