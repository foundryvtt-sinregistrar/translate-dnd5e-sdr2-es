#!/usr/bin/env python3
"""Write the current version's CHANGELOG section as GitHub release notes."""
import argparse, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
p = argparse.ArgumentParser(description=__doc__); p.add_argument("--output", type=Path, default=ROOT / "dist" / "release-notes.md")
args = p.parse_args(); version = str(json.loads((ROOT / "module.json").read_text(encoding="utf-8"))["version"])
log = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
start = re.search(rf"^## \[{re.escape(version)}\].*$", log, re.MULTILINE)
if not start: raise SystemExit(f"CHANGELOG.md does not contain version {version}.")
end = re.search(r"^## \[", log[start.end():], re.MULTILINE)
body = log[start.end():start.end() + end.start() if end else len(log)].strip()
if not body: raise SystemExit(f"CHANGELOG.md section for {version} is empty.")
args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(f"## Changes\n\n{body}\n", encoding="utf-8")
print(f"OK: {args.output}")
