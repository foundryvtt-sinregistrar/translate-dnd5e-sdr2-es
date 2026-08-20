#!/usr/bin/env python3
"""Extract official Spanish spell material components from the SRD 5.2.1 PDF.

The full Foundry export retains ``system.materials.value`` while the reduced
translation export omits it.  This tool joins the full export to the translated
pack by document ID, finds the corresponding spell entry in the official
Spanish PDF, and emits a deterministic JSON mapping suitable for review or
application to the Babele translation file.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import unicodedata

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / "compendium" / "dnd5e.spells24.json"
FULL_EXPORT = ROOT / "dev-tools" / "export" / "data" / "export_all" / "dnd5e.spells24 (1).json"
SPANISH_PDF = ROOT / "dev-tools" / "sourcesToChatGPT" / "SRD_CC_v5.2.1-es.pdf"

# The existing pack predates the official PDF review. These titles either use
# legacy proper names, differ from the official terminology, contain a typo, or
# are currently assigned to the wrong English spell.
OFFICIAL_TITLE_OVERRIDES = {
    "phbFaithfulHound": "Mastín fiel",
    "phbMagnificentMa": "Mansión magnífica",
    "phbPrivateSanctu": "Sanctasanctórum privado",
    "phbsplBigbysHand": "Mano arcana",
    "phbsplDancingLig": "Luces danzantes",
    "phbsplFlameStrik": "Golpe flamígero",
    "phbsplForesight0": "Presciencia",
    "phbsplHeroesFeas": "Festín de héroes",
    "phbsplLight00000": "Luz",
    "phbsplMagicCircl": "Círculo mágico",
    "phbsplMending000": "Reparar",
    "phbsplMessage000": "Mensaje",
    "phbsplMinorIllus": "Ilusión menor",
    "phbsplSequester0": "Recluir",
    "phbsplShillelagh": "Shillelagh",
    "phbsplTrueStrike": "Impacto certero",
    "phbsplWaterWalk0": "Caminar sobre el agua",
    "phbswdMordenkain": "Espada arcana",
}


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "", value)


def clean_pdf_text(value: str) -> str:
    # PDF line wrapping sometimes inserts a visible non-breaking hyphen with
    # surrounding spaces. It is a layout artifact, not part of the source word.
    value = re.sub(r"\s*[‐‑]\s*\n\s*", "", value)
    return re.sub(r"\s+", " ", value).strip()


def spell_lines() -> list[str]:
    reader = PdfReader(SPANISH_PDF)
    # Spell descriptions occupy this bounded part of the official Spanish SRD.
    return [
        line
        for index in range(115, 194)
        for line in (reader.pages[index].extract_text() or "").splitlines()
    ]


def material_for_title(lines: list[str], title: str) -> str | None:
    wanted = normalized(title)
    for index, line in enumerate(lines):
        if normalized(line.strip()) != wanted:
            continue
        # Flattening the bounded spell section also handles entries whose title
        # or component list falls at the end of one PDF page and continues on
        # the next (notably Message and Invisibility).
        following = "\n".join(lines[index + 1:index + 24])
        match = re.search(r"Componentes:\s*.*?\bM\s*\((.*?)\).*?Duración:", following, re.S)
        if match:
            return clean_pdf_text(match.group(1))
    return None


def build_mapping() -> dict[str, dict[str, str]]:
    pack = json.loads(PACK.read_text(encoding="utf-8-sig"))
    full_export = json.loads(FULL_EXPORT.read_text(encoding="utf-8-sig"))
    english_materials = {
        document["_id"]: document.get("system", {}).get("materials", {}).get("value", "")
        for document in full_export
    }
    lines = spell_lines()
    result: dict[str, dict[str, str]] = {}
    missing: list[str] = []
    for document_id, entry in pack["entries"].items():
        english = english_materials.get(document_id, "")
        if not english:
            continue
        title = OFFICIAL_TITLE_OVERRIDES.get(document_id, entry["name"])
        material = material_for_title(lines, title)
        if material is None:
            missing.append(f"{document_id}: {title}")
            continue
        result[document_id] = {
            "title": title,
            "english": english,
            "spanish": material,
        }
    if missing:
        raise SystemExit("Material components not found:\n" + "\n".join(missing))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="write the mapping as UTF-8 JSON")
    arguments = parser.parse_args()
    mapping = build_mapping()
    payload = json.dumps(mapping, ensure_ascii=False, indent=2) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    print(f"Extracted {len(mapping)} official Spanish material components", file=__import__("sys").stderr)


if __name__ == "__main__":
    main()
