#!/usr/bin/env python3
"""Reuse exact translated strings from non-actor SRD compendiums in actors24."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
PACKS = (
    "classes24", "content24", "equipment24", "feats24",
    "monsterfeatures24", "origins24", "spells24", "tables24",
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def walk(value: Any, path: tuple[Any, ...] = ()) -> Iterator[tuple[tuple[Any, ...], str]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path + (index,))
    elif isinstance(value, str):
        yield path, value


def get(value: Any, path: tuple[Any, ...]) -> Any:
    try:
        for key in path:
            value = value[key]
        return value
    except (KeyError, IndexError, TypeError):
        return None


def set_value(value: Any, path: tuple[Any, ...], replacement: str) -> None:
    for key in path[:-1]:
        value = value[key]
    value[path[-1]] = replacement


def pack_paths(pack: str) -> tuple[Path, Path]:
    base = f"dnd5e.{pack}"
    source = ROOT / "dev-tools" / "export" / "data" / base / "en" / f"{base}.json"
    translated = ROOT / "compendium" / f"{base}.json"
    return source, translated


def translation_memory() -> tuple[dict[str, str], int]:
    candidates: dict[str, str] = {}
    conflicts: set[str] = set()
    for pack in PACKS:
        source_path, translated_path = pack_paths(pack)
        source = load(source_path)
        translated = load(translated_path)
        for path, english in walk(source):
            spanish = get(translated, path)
            if not isinstance(spanish, str) or spanish == english or len(english) <= 20:
                continue
            if english in candidates and candidates[english] != spanish:
                conflicts.add(english)
            else:
                candidates[english] = spanish
    for english in conflicts:
        candidates.pop(english, None)
    return candidates, len(conflicts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    memory, conflicts = translation_memory()
    source_path, translated_path = pack_paths("actors24")
    source = load(source_path)
    translated = load(translated_path)
    changes: list[dict[str, str]] = []

    for path, english in walk(source):
        current = get(translated, path)
        spanish = memory.get(english)
        if current == english and spanish is not None:
            set_value(translated, path, spanish)
            changes.append({"path": "/".join(map(str, path)), "english": english, "spanish": spanish})

    report = {
        "translationMemoryEntries": len(memory),
        "discardedConflicts": conflicts,
        "replacements": len(changes),
        "changes": changes,
    }
    if args.write:
        translated_path.write_text(
            json.dumps(translated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "changes"}, indent=2))


if __name__ == "__main__":
    main()
