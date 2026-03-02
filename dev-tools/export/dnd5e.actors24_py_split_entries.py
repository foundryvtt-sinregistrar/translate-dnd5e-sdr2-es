#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python split_entries.py entrada.json -o out_entries
# python split_entries.py dnd5e.actors24-en.json -o out_actores_en --wrap
# python split_entries.py dnd5e.actors24-en.json -o out_actores_en --include-key-field

import argparse
import json
import re
from pathlib import Path


def safe_filename(name: str, fallback: str = "entry") -> str:
    """
    Sanitiza nombres para que sean válidos como archivo en Windows.
    """
    if not name:
        name = fallback
    # Quitar caracteres inválidos en Windows: \ / : * ? " < > |
    name = re.sub(r'[\\/:*?"<>|]+', "_", name)
    name = name.strip().strip(".")
    return name or fallback


def main():
    parser = argparse.ArgumentParser(
        description="Divide un JSON y crea un archivo por cada key dentro de entries."
    )
    parser.add_argument("input_json", help="Ruta al JSON de entrada")
    parser.add_argument(
        "-o", "--out",
        default="out_entries",
        help="Carpeta de salida (por defecto: out_entries)"
    )
    parser.add_argument(
        "--wrap",
        action="store_true",
        help='Si se activa, cada archivo tendrá {"<key>": <obj>} en vez de solo <obj>.'
    )
    parser.add_argument(
        "--include-key-field",
        action="store_true",
        help='Si se activa, añade un campo "_entryKey" dentro del objeto exportado.'
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Indentación JSON (por defecto: 2). Usa 0 para minificado."
    )
    args = parser.parse_args()

    in_path = Path(args.input_json)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(in_path.read_text(encoding="utf-8"))

    entries = data.get("entries")
    if not isinstance(entries, dict):
        raise SystemExit('ERROR: El JSON no tiene "entries" como objeto/dict.')

    written = 0
    for entry_key, entry_obj in entries.items():
        if not isinstance(entry_obj, dict):
            # Si alguna entry no es dict, igual la exportamos tal cual
            obj_to_write = entry_obj
        else:
            obj_to_write = dict(entry_obj)  # copia superficial
            if args.include_key_field:
                obj_to_write["_entryKey"] = entry_key

        payload = {entry_key: obj_to_write} if args.wrap else obj_to_write

        filename = safe_filename(entry_key, fallback=f"entry_{written+1}") + ".json"
        out_path = out_dir / filename

        if args.indent == 0:
            out_path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        else:
            out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=args.indent), encoding="utf-8")

        written += 1

    print(f"OK: escritos {written} archivos en: {out_dir.resolve()}")


if __name__ == "__main__":
    main()