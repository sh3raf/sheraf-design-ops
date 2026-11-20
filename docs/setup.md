# Setup (about 5 minutes)

The sdops skills read and change Figma files through two connectors. You need at least one; with
both you get the full workflow.

| Connector | Needed for | How to add it |
|---|---|---|
| **Official Figma MCP** | Library search, screenshots of any file, writes with `use_figma` | In Claude Code run `/mcp`, add the Figma server (`https://mcp.figma.com/mcp`) and sign in with Figma. |
| **Figma Console MCP** + Desktop Bridge plugin | Fast local reads and writes in open files, bulk work | Install the Figma Console MCP server, then in Figma Desktop run **Plugins → Development → Figma Desktop Bridge** in each file you work on. |

## Check it

Ask Claude: "check my Figma setup for sdops". It should confirm:
1. Which connectors answer.
2. Which open files the bridge can see (it lists their names).
3. Whether you can edit the libraries (only then can fixes happen in the library).

## Limits to know

- The official MCP has a daily call limit. The skills use the bridge for bulk reads to stay under it.
- The bridge runs one script at a time. Don't run two skills on it at once.

## Privacy

- The official MCP is a cloud service: what it reads leaves your machine. The bridge works locally.
- Reports and screenshots contain your client's work. Anonymise client names before sharing anything
  outside the team; the skills do this by default for anything marked as shareable.

## Undo

Before its first change in a file, `ds-fixer` saves a named version. To undo a round, open
**File → Show version history** and restore the version named in the report.
