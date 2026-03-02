#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merge_lang_dicts_all_in_one.py
==============================

Objetivo
--------
Unificar TODOS los ficheros JSON en carpetas 'en/' y 'es/' (misma ruta relativa),
y generar UN ÚNICO diccionario global de traducción:

    EN entry.name  ->  ES entry.name

Estructura esperada (ejemplo):
    en/dnd5e.backgrounds.json
    es/dnd5e.backgrounds.json

o con subcarpetas:
    en/srd/dnd5e.backgrounds.json
    es/srd/dnd5e.backgrounds.json

Salida
------
- out/_all.dict.json
    {
      "Acolyte": "Acólito",
      "Shelter of the Faithful": "Refugio de los fieles",
      ...
    }

Opcional:
- out/_all.byId.json
    {
      "IgJkSnLiLJOWH7eK": { "en": "Acolyte", "es": "Acólito", "file": "dnd5e.backgrounds.json" },
      ...
    }

- out/_all.report.json
    {
      "counts": {...},
      "missing_pairs": [...],
      "warnings": [...],
      "collisions": [...]
    }

Ejecución (Windows PowerShell)
-----------------------------
1) Coloca este script en la carpeta raíz que contiene 'en\' y 'es\'.
2) Ejecuta:
    py .\merge_lang_dicts_all_in_one.py --en en --es es --out out

Opciones útiles:
- Generar auditoría por ID + reporte:
    py .\merge_lang_dicts_all_in_one.py --en en --es es --out out --by-id --report

- Estrategia ante colisiones (mismo EN name con ES distinto):
    --collision keep-first   (se queda con la primera)
    --collision keep-last    (se queda con la última)  [default]
    --collision error        (falla si ocurre)
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Dict, Any, List, Tuple, Optional


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(path: str, obj: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)

def is_json_file(filename: str) -> bool:
    return filename.lower().endswith(".json")

def norm_key(s: str) -> str:
    return s.lower().strip()

def find_en_jsons(en_root: str) -> List[str]:
    out: List[str] = []
    for root, _, files in os.walk(en_root):
        for fn in files:
            if is_json_file(fn):
                out.append(os.path.join(root, fn))
    out.sort()
    return out

def merge_one_pair(
    rel: str,
    en_data: Dict[str, Any],
    es_data: Dict[str, Any],
    global_dict: Dict[str, str],
    global_by_id: Dict[str, Dict[str, str]],
    warnings: List[str],
    collisions: List[Dict[str, Any]],
    collision_mode: str,
) -> Tuple[int, int, int]:
    """
    Devuelve (en_entries_count, es_entries_count, paired_count)
    """
    en_entries: Dict[str, Any] = (en_data.get("entries") or {})
    es_entries: Dict[str, Any] = (es_data.get("entries") or {})

    paired = 0

    # EN -> ES por ID
    for entry_id, en_entry in en_entries.items():
        es_entry = es_entries.get(entry_id)
        if es_entry is None:
            warnings.append(f"[{rel}] ID existe en EN pero no en ES: {entry_id}")
            continue

        en_name = (en_entry or {}).get("name")
        es_name = (es_entry or {}).get("name")
        if not isinstance(en_name, str) or not en_name.strip():
            warnings.append(f"[{rel}] EN sin 'name' válido en ID: {entry_id}")
            continue
        if not isinstance(es_name, str) or not es_name.strip():
            warnings.append(f"[{rel}] ES sin 'name' válido en ID: {entry_id}")
            continue

        paired += 1

        # Auditoría por ID (opcional)
        if global_by_id is not None:
            global_by_id[entry_id] = {"en": en_name, "es": es_name, "file": rel.replace("\\", "/")}

        # Merge al diccionario global por name
        if en_name in global_dict and global_dict[en_name] != es_name:
            col = {
                "en": en_name,
                "prev_es": global_dict[en_name],
                "new_es": es_name,
                "file": rel.replace("\\", "/"),
                "id": entry_id,
            }
            collisions.append(col)

            if collision_mode == "keep-first":
                # no tocamos el valor existente
                pass
            elif collision_mode == "keep-last":
                global_dict[en_name] = es_name
            elif collision_mode == "error":
                raise ValueError(
                    f"Colisión EN name '{en_name}': '{global_dict[en_name]}' vs '{es_name}' "
                    f"(file={rel}, id={entry_id})"
                )
            else:
                raise ValueError(f"collision_mode inválido: {collision_mode}")
        else:
            global_dict[en_name] = es_name

    # IDs que existen en ES pero no en EN (warning)
    for entry_id in es_entries.keys():
        if entry_id not in en_entries:
            warnings.append(f"[{rel}] ID existe en ES pero no en EN: {entry_id}")

    return (len(en_entries), len(es_entries), paired)


def main():
    ap = argparse.ArgumentParser(description="Genera UN diccionario global EN name -> ES name a partir de carpetas en/es.")
    ap.add_argument("--en", default="en", help="Carpeta raíz EN (default: en)")
    ap.add_argument("--es", default="es", help="Carpeta raíz ES (default: es)")
    ap.add_argument("--out", default="out", help="Carpeta de salida (default: out)")
    ap.add_argument("--by-id", action="store_true", help="Genera también out/_all.byId.json (auditoría por ID)")
    ap.add_argument("--report", action="store_true", help="Genera también out/_all.report.json")
    ap.add_argument(
        "--collision",
        choices=["keep-first", "keep-last", "error"],
        default="keep-last",
        help="Qué hacer si el mismo EN name aparece con ES distinto (default: keep-last)",
    )
    args = ap.parse_args()

    en_root = args.en
    es_root = args.es
    out_root = args.out

    if not os.path.isdir(en_root):
        raise SystemExit(f"❌ No existe carpeta EN: {en_root}")
    if not os.path.isdir(es_root):
        raise SystemExit(f"❌ No existe carpeta ES: {es_root}")

    en_files = find_en_jsons(en_root)
    if not en_files:
        raise SystemExit("⚠ No se encontraron JSONs en la carpeta EN.")

    global_dict: Dict[str, str] = {}
    global_by_id: Optional[Dict[str, Dict[str, str]]] = {} if args.by_id else None

    missing_pairs: List[str] = []
    warnings: List[str] = []
    collisions: List[Dict[str, Any]] = []

    totals = {
        "files_en": 0,
        "files_paired": 0,
        "en_entries": 0,
        "es_entries": 0,
        "paired_entries": 0,
        "dict_size": 0,
        "collisions": 0,
        "warnings": 0,
        "missing_pairs": 0,
    }

    for en_path in en_files:
        totals["files_en"] += 1
        rel = os.path.relpath(en_path, en_root)
        es_path = os.path.join(es_root, rel)

        if not os.path.isfile(es_path):
            missing_pairs.append(rel.replace("\\", "/"))
            continue

        try:
            en_data = load_json(en_path)
            es_data = load_json(es_path)
        except Exception as e:
            warnings.append(f"[{rel}] Error leyendo JSON: {e}")
            continue

        try:
            en_count, es_count, paired = merge_one_pair(
                rel=rel,
                en_data=en_data,
                es_data=es_data,
                global_dict=global_dict,
                global_by_id=global_by_id,
                warnings=warnings,
                collisions=collisions,
                collision_mode=args.collision,
            )
        except Exception as e:
            raise SystemExit(f"❌ Error procesando {rel}: {e}")

        totals["files_paired"] += 1
        totals["en_entries"] += en_count
        totals["es_entries"] += es_count
        totals["paired_entries"] += paired

    # Orden final del diccionario global por clave EN
    global_dict = dict(sorted(global_dict.items(), key=lambda kv: norm_key(kv[0])))

    # Guardar salidas
    out_all = os.path.join(out_root, "_all.dict.json")
    write_json(out_all, global_dict)

    if args.by_id and global_by_id is not None:
        out_by_id = os.path.join(out_root, "_all.byId.json")
        # ordenar por id
        global_by_id = dict(sorted(global_by_id.items(), key=lambda kv: kv[0]))
        write_json(out_by_id, global_by_id)

    totals["dict_size"] = len(global_dict)
    totals["collisions"] = len(collisions)
    totals["warnings"] = len(warnings)
    totals["missing_pairs"] = len(missing_pairs)

    if args.report:
        out_report = os.path.join(out_root, "_all.report.json")
        report = {
            "counts": totals,
            "collision_mode": args.collision,
            "missing_pairs": missing_pairs,
            "collisions": collisions,   # detalles completos
            "warnings": warnings,       # warnings completos
        }
        write_json(out_report, report)

    # Consola (resumen)
    print("✅ Generado diccionario global:")
    print(f"   - {out_all}")
    if args.by_id:
        print(f"   - {os.path.join(out_root, '_all.byId.json')}")
    if args.report:
        print(f"   - {os.path.join(out_root, '_all.report.json')}")
    print("\n--- RESUMEN ---")
    print(f"Ficheros EN encontrados:    {totals['files_en']}")
    print(f"Ficheros EN+ES emparejados: {totals['files_paired']}")
    print(f"Pares entries (por ID):     {totals['paired_entries']}")
    print(f"Tamaño dict EN->ES:         {totals['dict_size']}")
    print(f"Colisiones:                 {totals['collisions']}  (modo: {args.collision})")
    print(f"Warnings:                   {totals['warnings']}")
    print(f"Sin par ES:                 {totals['missing_pairs']}")


if __name__ == "__main__":
    main()