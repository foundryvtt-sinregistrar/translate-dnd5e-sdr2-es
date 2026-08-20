#!/usr/bin/env python3
"""Inventory free-text Foundry fields omitted by the reduced Babele exports."""

from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
FULL = ROOT / "dev-tools" / "export" / "data" / "export_all"

# These leaf fields are rendered as author-provided prose rather than localized
# D&D5e enum codes. They therefore need explicit ownership by a translation.
VISIBLE_FREE_TEXT = {
    "condition": "activity trigger or usage condition",
    "chatFlavor": "activity chat description",
    "special": "custom target, range, sense, or movement text",
    "custom": "custom type, trait, damage, or formula label",
    "subtype": "mixed enum or custom creature/species subtype; review by document type",
    "dimensions": "vehicle or object dimensions",
}


def normalized_path(parts: tuple[str, ...]) -> str:
    return ".".join("*" if re.fullmatch(r"[A-Za-z0-9]{16}", part) else part for part in parts)


def walk(value, parts: tuple[str, ...] = ()):  # noqa: ANN001
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, (*parts, key))
    elif isinstance(value, list):
        for child in value:
            yield from walk(child, (*parts, "[]"))
    elif isinstance(value, str) and value.strip() and parts[-1] in VISIBLE_FREE_TEXT:
        yield normalized_path(parts), value.strip()


def build_report() -> dict:
    packs = {}
    for path in sorted(FULL.glob("dnd5e.*24*.json")):
        documents = json.loads(path.read_text(encoding="utf-8-sig"))
        findings = defaultdict(list)
        for document in documents:
            for field_path, value in walk(document):
                findings[field_path].append({"id": document.get("_id"), "value": value})
        packs[path.name] = {
            field_path: {
                "owner": "review-required" if field_path.endswith(".subtype") else "translate-dnd5e-sdr2-es",
                "reason": VISIBLE_FREE_TEXT[field_path.split(".")[-1]],
                "count": len(values),
                "examples": values[:5],
            }
            for field_path, values in sorted(findings.items())
        }
    return {
        "scope": "Free-text fields in complete modern SRD exports that require translation ownership",
        "classification": {
            "translationOwned": sorted(set(VISIBLE_FREE_TEXT) - {"subtype"}),
            "reviewRequired": ["subtype"],
            "systemOwned": "enum codes, units, damage types, creature types, sizes, abilities, and property identifiers",
            "technical": "IDs, UUIDs, formulas, image paths, source metadata, and numeric values",
        },
        "packs": packs,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    report = build_report()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    paths = sum(len(fields) for fields in report["packs"].values())
    values = sum(field["count"] for fields in report["packs"].values() for field in fields.values())
    print(f"Inventoried {values} visible free-text values across {paths} normalized paths")


if __name__ == "__main__":
    main()
