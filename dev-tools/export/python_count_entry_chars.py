#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contar caracteres por cada entry dentro de "entries" y exportar un JSON {entryId: count}.

Uso (Windows PowerShell / CMD):
  py count_entry_chars.py dnd5e.actors24-en_sorted.json -o out_counts.json

Opcional:
  py count_entry_chars.py input.json --pretty
"""

import argparse
import json
from pathlib import Path


def count_chars_of_entry(entry_obj) -> int:
    """
    Cuenta caracteres del entry serializándolo a JSON compacto.
    - ensure_ascii=False para contar caracteres reales (á, ñ, etc.)
    - separators=(',', ':') para que no meta espacios
    """
    s = json.dumps(entry_obj, ensure_ascii=False, separators=(",", ":"))
    return len(s)


def main():
    ap = argparse.ArgumentParser(
        description="Cuenta caracteres del contenido de cada clave dentro de entries."
    )
    ap.add_argument("input", help="Ruta del JSON de entrada")
    ap.add_argument(
        "-o",
        "--output",
        default=None,
        help="Ruta del JSON de salida (por defecto: <input>.entry-char-counts.json)",
    )
    ap.add_argument(
        "--pretty",
        action="store_true",
        help="Salida JSON con indentación (más legible).",
    )
    args = ap.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        raise SystemExit(f"ERROR: No existe el fichero: {in_path}")

    out_path = Path(args.output) if args.output else in_path.with_suffix(".entry-char-counts.json")

    with in_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries")
    if not isinstance(entries, dict):
        raise SystemExit("ERROR: El JSON no tiene un objeto 'entries' (o no es dict).")

    result = {}
    for entry_id, entry_obj in entries.items():
        result[entry_id] = count_chars_of_entry(entry_obj)

    with out_path.open("w", encoding="utf-8") as f:
        if args.pretty:
            json.dump(result, f, ensure_ascii=False, indent=2)
        else:
            json.dump(result, f, ensure_ascii=False, separators=(",", ":"))

    print(f"OK: generado {out_path} ({len(result)} entries)")


if __name__ == "__main__":
    main()