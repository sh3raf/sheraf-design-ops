"""Run one eval turn in a fresh, isolated Claude Code session that has only the sdops plugin.

First turn:  python3 tests/run_case.py <case-id> --out <results-dir>
Next turns:  python3 tests/run_case.py <case-id> --out <results-dir> --reply "designer's answer"

Isolation: no MCP servers (--strict-mcp-config), only project settings, a work folder copied from
the case's fixture (never designer.md), so no Figma access, no user memory, no other plugins' state.
Writes each turn's stream to <out>/<case>/turn-N.jsonl and prints the reply, skills and tools used.
"""
import argparse, json, pathlib, shutil, subprocess, sys

root = pathlib.Path(__file__).resolve().parent.parent
p = argparse.ArgumentParser()
p.add_argument("case"); p.add_argument("--out", required=True); p.add_argument("--reply")
p.add_argument("--model", default="sonnet"); p.add_argument("--budget", default="1.0")
a = p.parse_args()

case = next((c for f in sorted((root / "evals").glob("*.json"))
             for c in json.loads(f.read_text())["cases"] if c["id"] == a.case), None)
if not case: sys.exit(f"no case {a.case}")
if case.get("needs") == "live-figma": sys.exit(f"{a.case} needs live Figma: run it by hand")

case_dir = pathlib.Path(a.out).resolve() / a.case
work = case_dir / "work"
turns = sorted(case_dir.glob("turn-*.jsonl"))
if not turns:
    if a.reply: sys.exit("first turn takes no --reply")
    shutil.copytree(root / "tests/fixtures" / case["fixture"], work,
                    ignore=shutil.ignore_patterns("designer.md", ".keep"))
    (case_dir / "empty-mcp.json").write_text('{"mcpServers":{}}')
    prompt, resume = case["prompt"], []
else:
    if not a.reply: sys.exit("later turns need --reply")
    sid = json.loads((case_dir / "session.json").read_text())["session_id"]
    prompt, resume = a.reply, ["--resume", sid]

cmd = ["claude", "-p", prompt, *resume, "--setting-sources", "project", "--strict-mcp-config",
       "--mcp-config", str(case_dir / "empty-mcp.json"), "--plugin-dir", str(root / "plugins/sdops"), "--add-dir", str(root / "plugins/sdops"),
       "--model", a.model, "--max-budget-usd", a.budget, "--permission-mode", "acceptEdits",
       "--disallowed-tools", "Bash", "WebFetch", "WebSearch",
       "--output-format", "stream-json", "--verbose"]
out = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=900)
log = case_dir / f"turn-{len(turns) + 1}.jsonl"
log.write_text(out.stdout)

skills, tools, result = [], [], None
if not turns and prompt.startswith("/sdops:"):
    skills.append(prompt.split()[0][1:] + " (slash)")
for line in out.stdout.splitlines():
    try: ev = json.loads(line)
    except ValueError: continue
    if ev.get("type") == "assistant":
        for b in ev["message"].get("content", []):
            if b.get("type") == "tool_use":
                tools.append(b["name"])
                if b["name"] == "Skill": skills.append(b["input"].get("skill"))
    if ev.get("type") == "result":
        result = ev
        (case_dir / "session.json").write_text(json.dumps({"session_id": ev["session_id"]}))

print(f"== {a.case} turn {len(turns) + 1} ({log})")
print("skills:", skills or "none", "| tools:", ", ".join(dict.fromkeys(tools)) or "none")
print("files in work:", sorted(str(f.relative_to(work)) for f in work.rglob("*") if f.is_file()))
if result:
    print(f"cost ${result.get('total_cost_usd', 0):.3f}")
    print(result.get("result") or result.get("subtype"))
else:
    print("no result; stderr:", out.stderr[-2000:])
