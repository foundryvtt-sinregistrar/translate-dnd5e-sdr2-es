#!/usr/bin/env python3
"""Repair truncated actor fields from better translations of identical source text."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
BASE = "dnd5e.actors24"
SOURCE = ROOT / "dev-tools" / "export" / "data" / BASE / "en" / f"{BASE}.json"
TARGET = ROOT / "compendium" / f"{BASE}.json"
TOKEN = re.compile(r"@(?:UUID|Embed)\[[^\]]+\]|&(?:amp;)?Reference\[[^\]]+\]|\[\[[\s\S]*?\]\]")


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


def tokens(value: str) -> Counter[str]:
    return Counter(token.replace("&amp;Reference[", "&Reference[") for token in TOKEN.findall(value))


def retained(source: str, translated: str) -> int:
    return sum((tokens(source) & tokens(translated)).values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    source = json.loads(SOURCE.read_text(encoding="utf-8-sig"))
    translated = json.loads(TARGET.read_text(encoding="utf-8-sig"))
    groups: dict[tuple[str, str], list[tuple[tuple[Any, ...], str]]] = defaultdict(list)
    for path, english in walk(source):
        spanish = get(translated, path)
        if (
            isinstance(spanish, str)
            and len(english) >= 40
            and len(path) >= 5
            and path[-3] == "items"
            and path[-1] == "description"
        ):
            groups[(english, str(path[-2]))].append((path, spanish))

    changes: list[dict[str, Any]] = []
    for (english, _item_id), occurrences in groups.items():
        if len(occurrences) < 2:
            continue
        scores = [(retained(english, spanish), len(spanish), spanish) for _, spanish in occurrences]
        best_score, best_length = max((score, length) for score, length, _ in scores)
        best_texts = {
            spanish for score, length, spanish in scores
            if (score, length) == (best_score, best_length)
        }
        if len(best_texts) != 1:
            continue
        best = best_texts.pop()
        for path, spanish in occurrences:
            score = retained(english, spanish)
            materially_shorter = len(spanish) < best_length * 0.5 or spanish.strip().endswith("...")
            if (score >= best_score and not materially_shorter) or spanish == best:
                continue
            set_value(translated, path, best)
            changes.append({
                "path": "/".join(map(str, path)),
                "retainedTokensBefore": score,
                "retainedTokensAfter": best_score,
            })

    report = {"replacementCount": len(changes), "changes": changes}
    if args.write and changes:
        TARGET.write_text(json.dumps(translated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"duplicate actor repairs: {len(changes)}")


if __name__ == "__main__":
    main()
