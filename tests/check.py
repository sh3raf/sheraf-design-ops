"""Checks the manifests parse, versions agree, and every file a skill points to exists."""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

market = json.loads((root / ".claude-plugin/marketplace.json").read_text())
for entry in market["plugins"]:
    plugin_dir = root / entry["source"]
    manifest = json.loads((plugin_dir / ".claude-plugin/plugin.json").read_text())
    if manifest["name"] != entry["name"]:
        errors.append(f"{entry['name']}: plugin.json name is {manifest['name']}")
    for skill in sorted((plugin_dir / "skills").glob("*/SKILL.md")):
        text = skill.read_text()
        front = re.match(r"---\n(.*?)\n---", text, re.S)
        if not front or "\nname:" not in "\n" + front.group(1) or "description:" not in front.group(1):
            errors.append(f"{skill}: frontmatter needs name and description")
        for ref in set(re.findall(r"`(references/[\w./-]+)`", text)):
            if not (skill.parent / ref).exists():
                errors.append(f"{skill}: missing {ref}")

for ev in sorted((root / "evals").glob("*.json")):
    data = json.loads(ev.read_text())
    if not any((root / e["source"] / "skills" / data["skill"]).is_dir() for e in market["plugins"]):
        errors.append(f"{ev.name}: no skill {data['skill']}")
    for case in data["cases"]:
        if not case.get("prompt") or not case.get("expect"):
            errors.append(f"{ev.name}: {case.get('id')} needs prompt and expect")
        if case.get("needs") != "live-figma" and not (root / "tests/plugin-evals/fixtures" / case.get("fixture", "?")).is_dir():
            errors.append(f"{ev.name}: {case.get('id')} has no fixture folder")

for case in sorted((root / "tests/plugin-evals").glob("*/prompt.md")):
    if not list((case.parent / "graders").glob("*.md")):
        errors.append(f"{case.parent.name}: native eval case has no grader")

for doc in sorted(root.rglob("*.md")):
    if any(p in doc.parts for p in (".git", "results")):
        continue
    for link in re.findall(r"\]\(([^)#:\s]+)\)", doc.read_text()):
        if "<" not in link and not (doc.parent / link).exists():  # <id>-<slug>.md is a template placeholder
            errors.append(f"{doc.relative_to(root)}: broken link {link}")

# The directory takes only these file types from organizations it hasn't verified.
allowed = {".md", ".txt", ".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"}
for entry in market["plugins"]:
    for f in (root / entry["source"]).rglob("*"):
        if f.is_file() and (f.suffix.lower() not in allowed or f.read_bytes()[:2] == b"#!"):
            errors.append(f"{f.relative_to(root)}: the plugin directory rejects this file type")

changelog = (root / "CHANGELOG.md").read_text()
for entry in market["plugins"]:
    version = json.loads((root / entry["source"] / ".claude-plugin/plugin.json").read_text())["version"]
    if f"## {version}" not in changelog:
        errors.append(f"CHANGELOG.md has no entry for {version}")

print("\n".join(errors) or "ok")
sys.exit(1 if errors else 0)
