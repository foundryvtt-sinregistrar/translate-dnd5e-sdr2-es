#!/usr/bin/env python3
"""Run the non-destructive checks required before testing the module in Foundry."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = Path(__file__).resolve().parent
PACKS = (
    "actors24", "classes24", "content24", "equipment24", "feats24",
    "monsterfeatures24", "origins24", "spells24", "tables24",
)


def run(*arguments: str) -> str:
    result = subprocess.run(
        [sys.executable, str(AUDIT_DIR / arguments[0]), *arguments[1:]],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> None:
    json_files = [ROOT / "module.json", *sorted((ROOT / "lang").glob("*.json"))]
    json_files.extend(ROOT / "compendium" / f"dnd5e.{pack}.json" for pack in PACKS)
    for path in json_files:
        json.loads(path.read_text(encoding="utf-8-sig"))

    spell_pack = json.loads(
        (ROOT / "compendium" / "dnd5e.spells24.json").read_text(encoding="utf-8-sig")
    )
    material_report = json.loads(
        (AUDIT_DIR / "reports" / "spell-materials.json").read_text(encoding="utf-8")
    )
    if spell_pack.get("mapping", {}).get("materials") != "system.materials.value":
        raise SystemExit("spells24 does not map translated material components")
    for document_id, expected in material_report.items():
        entry = spell_pack["entries"].get(document_id, {})
        if entry.get("materials") != expected["spanish"]:
            raise SystemExit(f"missing or stale material translation in spells24: {document_id}")
    if len(material_report) != 188:
        raise SystemExit(f"expected 188 PDF-backed spell materials, found {len(material_report)}")

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as handle:
        visible_report_path = Path(handle.name)
    try:
        run("audit_visible_fields.py", "--output", str(visible_report_path))
        generated_visible_report = json.loads(visible_report_path.read_text(encoding="utf-8"))
        tracked_visible_report = json.loads(
            (AUDIT_DIR / "reports" / "visible-field-inventory.json").read_text(encoding="utf-8")
        )
        if generated_visible_report != tracked_visible_report:
            raise SystemExit("visible field inventory is stale; regenerate it from the complete exports")
    finally:
        visible_report_path.unlink(missing_ok=True)

    with tempfile.TemporaryDirectory(prefix="srd2-audit-") as temporary:
        report = Path(temporary) / "translation-audit.json"
        run("audit_srd_translation.py", "--json", str(report))
        audit = json.loads(report.read_text(encoding="utf-8"))
        for pack, findings in audit["packs"].items():
            structure = findings["structure"]
            if structure["englishEntries"] != structure["spanishEntries"]:
                raise SystemExit(f"entry-count mismatch in {pack}")
            if findings["likelyEnglish"]:
                raise SystemExit(f"likely English text remains in {pack}")
            if findings["mojibake"]:
                raise SystemExit(f"mojibake remains in {pack}")
    pending_checks = (
        ("sync_embedded_translations.py", "replacements"),
        ("normalize_visible_terms.py", "replacementCount"),
        ("repair_actor_duplicates.py", "replacementCount"),
    )
    for script, count_key in pending_checks:
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as handle:
            report = Path(handle.name)
        try:
            run(script, "--report", str(report))
            result = json.loads(report.read_text(encoding="utf-8"))
            if result[count_key]:
                raise SystemExit(f"{script} reports {result[count_key]} pending changes")
        finally:
            report.unlink(missing_ok=True)

    print(f"OK: {len(json_files)} JSON files and {len(PACKS)} compendium packs validated")
    print(f"OK: {len(material_report)} PDF-backed spell material components validated")
    print("OK: visible free-text field inventory matches the complete exports")
    print("OK: no pending normalization, duplicate repair, or embedded sync changes")


if __name__ == "__main__":
    main()
