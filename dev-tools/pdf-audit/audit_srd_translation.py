#!/usr/bin/env python3
"""Audit SRD compendium translations against their English exports.

The audit is intentionally read-only. It checks structural parity, exact
untranslated visible strings, likely English prose, mojibake, and mutations in
Foundry inline commands and references.
"""

from __future__ import annotations

import argparse
from collections import Counter
import html
import json
from pathlib import Path
import re
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
PACKS = (
    "actors24", "classes24", "content24", "equipment24", "feats24",
    "monsterfeatures24", "origins24", "spells24", "tables24",
)
VISIBLE_KEYS = {"label", "name", "description", "biography", "condition", "alignment"}
ENGLISH_MARKERS = re.compile(
    r"\b(?:the|and|you|your|creature|target|saving throw|damage|spell|attack|"
    r"until|within|each|must|can|when|while|failure|success|takes|makes)\b",
    re.IGNORECASE,
)
MOJIBAKE = re.compile(r"(?:Ã.|Â.|â€|â€™|â€œ|â€�|â€“|â€”|ï¿½|\ufffd)")
FOUNDRY_TOKEN = re.compile(
    r"@(?:UUID|Embed)\[[^\]]+\]|&(?:amp;)?Reference\[[^\]]+\]|\[\[[\s\S]*?\]\]"
)


def canonical_token(token: str) -> str:
    """Discard translatable decoration while preserving executable payloads."""
    token = token.replace("&amp;Reference[", "&Reference[")
    if token.startswith("[[") and "#" in token:
        token = token.split("#", 1)[0].rstrip() + "]]"
    return token


def foundry_tokens(value: str) -> Counter[str]:
    return Counter(canonical_token(token) for token in FOUNDRY_TOKEN.findall(value))


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


def shape(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: shape(child) for key, child in value.items()}
    if isinstance(value, list):
        return [shape(child) for child in value]
    return type(value).__name__


def plain_text(value: str) -> str:
    value = FOUNDRY_TOKEN.sub(" ", value)
    value = re.sub(r"\{[^{}]+\}", " ", value)
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def visible(path: tuple[Any, ...], value: str) -> bool:
    return bool(path and path[-1] in VISIBLE_KEYS and plain_text(value))


def path_text(path: tuple[Any, ...]) -> str:
    return "/".join(map(str, path))


def pack_paths(pack: str) -> tuple[Path, Path]:
    base = f"dnd5e.{pack}"
    source = ROOT / "dev-tools" / "export" / "data" / base / "en" / f"{base}.json"
    translated = ROOT / "compendium" / f"{base}.json"
    return source, translated


def audit_pack(pack: str) -> dict[str, Any]:
    source_path, translated_path = pack_paths(pack)
    source = load(source_path)
    translated = load(translated_path)
    source_entries = source.get("entries", {})
    translated_entries = translated.get("entries", {})
    exact: list[dict[str, str]] = []
    likely_english: list[dict[str, str]] = []
    mojibake: list[dict[str, str]] = []
    token_changes: list[dict[str, Any]] = []

    for path, english in walk(source):
        spanish = get(translated, path)
        if not isinstance(spanish, str):
            continue
        if MOJIBAKE.search(spanish):
            mojibake.append({"path": path_text(path), "value": spanish})
        if not visible(path, english):
            continue
        source_plain = plain_text(english)
        spanish_plain = plain_text(spanish)
        if spanish == english and len(source_plain) >= 4 and re.search(r"[A-Za-z]", source_plain):
            exact.append({"path": path_text(path), "value": english})
        marker_count = len(ENGLISH_MARKERS.findall(spanish_plain))
        if len(spanish_plain) >= 40 and marker_count >= max(2, len(spanish_plain.split()) // 16):
            likely_english.append({"path": path_text(path), "value": spanish})
        source_tokens = foundry_tokens(english)
        spanish_tokens = foundry_tokens(spanish)
        if source_tokens != spanish_tokens:
            token_changes.append({
                "path": path_text(path),
                "missing": list((source_tokens - spanish_tokens).elements()),
                "added": list((spanish_tokens - source_tokens).elements()),
            })

    return {
        "files": {"english": str(source_path.relative_to(ROOT)), "spanish": str(translated_path.relative_to(ROOT))},
        "structure": {
            "englishEntries": len(source_entries),
            "spanishEntries": len(translated_entries),
            "missingEntryIds": sorted(set(source_entries) - set(translated_entries)),
            "extraEntryIds": sorted(set(translated_entries) - set(source_entries)),
            "sameTopLevelShape": shape(source).keys() == shape(translated).keys(),
        },
        "exactUntranslated": exact,
        "likelyEnglish": likely_english,
        "mojibake": mojibake,
        "foundryTokenChanges": token_changes,
    }


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# SRD translation audit",
        "",
        "Generated by `dev-tools/pdf-audit/audit_srd_translation.py`.",
        "",
        "| Pack | EN entries | ES entries | Exact untranslated | Likely English | Mojibake | Foundry token changes |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for pack, result in report["packs"].items():
        structure = result["structure"]
        lines.append(
            f"| {pack} | {structure['englishEntries']} | {structure['spanishEntries']} | "
            f"{len(result['exactUntranslated'])} | {len(result['likelyEnglish'])} | "
            f"{len(result['mojibake'])} | {len(result['foundryTokenChanges'])} |"
        )
    lines.extend(["", "The JSON report contains the complete field-level findings.", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path)
    args = parser.parse_args()
    report = {"packs": {pack: audit_pack(pack) for pack in PACKS}}
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown(report), encoding="utf-8")


if __name__ == "__main__":
    main()
