#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comparar dos JSON y detectar diferencias en las keys dentro de "entries".

Uso:
    python compare_entries_keys.py fileA.json fileB.json

    py -3 compare_entries_keys.py ./dnd5e.actors24.json ./dnd5e.actors24-es.json
"""

import json
import argparse
from pathlib import Path


def load_entries(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "entries" not in data:
        raise ValueError(f"El archivo {path} no contiene la key 'entries'")

    return set(data["entries"].keys())


def main():
    parser = argparse.ArgumentParser(
        description="Compara las keys dentro de 'entries' entre dos JSON."
    )
    parser.add_argument("fileA", help="Primer JSON")
    parser.add_argument("fileB", help="Segundo JSON")
    parser.add_argument(
        "--export",
        help="Exportar resultado a archivo JSON",
        default=None
    )

    args = parser.parse_args()

    fileA = Path(args.fileA)
    fileB = Path(args.fileB)

    keysA = load_entries(fileA)
    keysB = load_entries(fileB)

    missing_in_B = sorted(keysA - keysB)
    missing_in_A = sorted(keysB - keysA)

    result = {
        "fileA_total": len(keysA),
        "fileB_total": len(keysB),
        "missing_in_B": missing_in_B,
        "missing_in_A": missing_in_A,
    }

    print("\n=== RESULTADO ===")
    print(f"{fileA.name}: {len(keysA)} entries")
    print(f"{fileB.name}: {len(keysB)} entries")
    print(f"\nFaltan en {fileB.name}: {len(missing_in_B)}")
    print(f"Faltan en {fileA.name}: {len(missing_in_A)}")

    if missing_in_B:
        print("\n--- Keys que faltan en B ---")
        for k in missing_in_B:
            print(k)

    if missing_in_A:
        print("\n--- Keys que faltan en A ---")
        for k in missing_in_A:
            print(k)

    if args.export:
        with open(args.export, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nResultado exportado a: {args.export}")


if __name__ == "__main__":
    main()