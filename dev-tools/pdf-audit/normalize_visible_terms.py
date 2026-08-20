#!/usr/bin/env python3
"""Apply reviewed terminology fixes to exact visible field values."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PACKS = ("actors24", "classes24", "content24", "equipment24", "monsterfeatures24", "origins24", "spells24")
VISIBLE_KEYS = {"label", "name", "condition", "alignment"}
REPLACEMENTS = {
    "Blinded & Deafened": "Cegado y ensordecido",
    "Concentration Disadvantage": "Desventaja en Concentración",
    "Dominated": "Dominado",
    "Exalted Restoration": "Restablecimiento exaltado",
    "Exhaustion 1": "Agotamiento 1",
    "Exhaustion 2": "Agotamiento 2",
    "Exhaustion 3": "Agotamiento 3",
    "Exhaustion 4": "Agotamiento 4",
    "Exhaustion 5": "Agotamiento 5",
    "Exhaustion Dead": "Muerte por agotamiento",
    "Failure: 1/2 Speed": "Fallo: mitad de Velocidad",
    "Gnomish Cunning": "Astucia gnómica",
    "Poisoned and Paralyzed": "Envenenado y paralizado",
    "Spell Changes": "Cambios de conjuro",
    "Tail Swipe": "Coletazo",
    "Tripped": "Derribado",
}


def replace(value: Any, path: tuple[Any, ...], changes: list[dict[str, str]]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = path + (key,)
            if key in VISIBLE_KEYS and isinstance(child, str) and child in REPLACEMENTS:
                value[key] = REPLACEMENTS[child]
                changes.append({
                    "path": "/".join(map(str, child_path)),
                    "english": child,
                    "spanish": value[key],
                })
            else:
                replace(child, child_path, changes)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            replace(child, path + (index,), changes)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report: dict[str, Any] = {"changes": []}
    for pack in PACKS:
        path = ROOT / "compendium" / f"dnd5e.{pack}.json"
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        changes: list[dict[str, str]] = []
        replace(data, (), changes)
        for change in changes:
            change["pack"] = pack
        report["changes"].extend(changes)
        if args.write and changes:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report["replacementCount"] = len(report["changes"])
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"reviewed visible-term replacements: {report['replacementCount']}")


if __name__ == "__main__":
    main()
