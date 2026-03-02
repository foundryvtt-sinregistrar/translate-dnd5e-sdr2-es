#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merge_lang_dicts.py
===================

Objetivo
--------
Unificar ficheros JSON del mismo "pack" en dos idiomas (EN y ES), ubicados en carpetas distintas,
y generar diccionarios de traducción.

Estructura esperada (ejemplo):
    en/dnd5e.backgrounds.json
    es/dnd5e.backgrounds.json

O con subcarpetas:
    en/srd/dnd5e.backgrounds.json
    es/srd/dnd5e.backgrounds.json

Qué genera
----------
Por cada pareja encontrada (mismo nombre y ruta relativa):

1) out/<ruta_relativa>.dict.json
   Diccionario plano EN->ES:
      {
        "Acolyte": "Acólito",
        "Folk Hero": "Héroe del Pueblo",
        ...
      }

2) (Opcional) out/<ruta_relativa>.byId.json
   Diccionario por ID:
      {
        "IgJkSnLiLJOWH7eK": { "en": "Acolyte", "es": "Acólito" },
        ...
      }

3) (Opcional) out/<ruta_relativa>.report.json
   Reporte (warnings y métricas) para detectar problemas:
      {
        "file": "dnd5e.backgrounds.json",
        "counts": { "en_entries": 42, "es_entries": 42, "paired": 42 },
        "warnings": [...]
      }

Emparejado robusto
------------------
- Empareja por el ID de entries (la clave dentro de "entries")
- Usa entry["name"] como texto EN/ES
- Si faltan IDs o "name", se anotan warnings

Uso rápido (Windows PowerShell)
-------------------------------
1) Coloca este script en la carpeta raíz donde tengas las carpetas "en" y "es".

2) Ejecuta:
    py .\merge_lang_dicts.py --en en --es es --out out

3) Para generar también salida por ID y reportes:
    py .\merge_lang_dicts.py --en en --es es --out out --by-id --report

4) Para procesar solo un fichero concreto:
    py .\merge_lang_dicts.py --en en --es es --out out --only dnd5e.backgrounds.json

Ejemplo de salida
-----------------
Entrada EN:
    entries:
      "IgJkSnLiLJOWH7eK": { "name": "Acolyte", ... }

Entrada ES:
    entries:
      "IgJkSnLiLJOWH7eK": { "name": "Acólito", ... }

Salida (dict):
    { "Acolyte": "Acólito" }

Notas
-----
- No modifica tus ficheros originales.
- Es ideal para construir diccionarios de traducción/normalización.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from typing import Dict, Any, Tuple, List, Optional


# -----------------------------
# Helpers IO
# -----------------------------

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


# -----------------------------
# Core logic
# -----------------------------

@dataclass
class MergeResult:
    dict_name: Dict[str, str]
    dict_by_id: Dict[str, Dict[str, str]]
    report: Dict[str, Any]


def build_dictionaries(en_data: Dict[str, Any], es_data: Dict[str, Any], rel_file: str) -> MergeResult:
    warnings: List[str] = []

    en_entries: Dict[str, Any] = (en_data.get("entries") or {})
    es_entries: Dict[str, Any] = (es_data.get("entries") or {})

    dict_name: Dict[str, str] = {}
    dict_by_id: Dict[str, Dict[str, str]] = {}

    # Emparejamos por ID (clave dentro de entries)
    paired = 0
    for entry_id, en_entry in en_entries.items():
        es_entry = es_entries.get(entry_id)

        if es_entry is None:
            warnings.append(f"ID existe en EN pero no en ES: {entry_id}")
            continue

        en_name = (en_entry or {}).get("name")
        es_name = (es_entry or {}).get("name")

        if not isinstance(en_name, str) or not en_name.strip():
            warnings.append(f"EN sin 'name' válido en ID: {entry_id}")
            continue
        if not isinstance(es_name, str) or not es_name.strip():
            warnings.append(f"ES sin 'name' válido en ID: {entry_id}")
            continue

        paired += 1
        dict_by_id[entry_id] = {"en": en_name, "es": es_name}

        # Diccionario plano EN->ES por name
        # Detectamos colisiones: mismo EN name aparece con dos traducciones distintas
        if en_name in dict_name and dict_name[en_name] != es_name:
            warnings.append(
                f"Colisión EN name '{en_name}': '{dict_name[en_name]}' vs '{es_name}' (ID {entry_id})"
            )
        dict_name[en_name] = es_name

    # También detectamos IDs que existen en ES pero no en EN
    for entry_id in es_entries.keys():
        if entry_id not in en_entries:
            warnings.append(f"ID existe en ES pero no en EN: {entry_id}")

    # Ordenamos por clave EN (dict_name) de forma estable
    dict_name = dict(sorted(dict_name.items(), key=lambda kv: norm_key(kv[0])))

    # Ordenamos dict_by_id por ID
    dict_by_id = dict(sorted(dict_by_id.items(), key=lambda kv: kv[0]))

    report = {
        "file": rel_file.replace("\\", "/"),
        "counts": {
            "en_entries": len(en_entries),
            "es_entries": len(es_entries),
            "paired": paired,
            "dict_name_size": len(dict_name),
            "dict_by_id_size": len(dict_by_id),
        },
        "warnings": warnings,
    }

    return MergeResult(dict_name=dict_name, dict_by_id=dict_by_id, report=report)


def find_pairs(en_root: str, es_root: str, only: Optional[str] = None) -> List[Tuple[str, str, str]]:
    """
    Devuelve lista de tuplas: (rel_path, en_path, es_path)
    Si only se especifica, busca solo ese fichero (por nombre) dentro de en_root.
    """
    pairs: List[Tuple[str, str, str]] = []

    for root, _, files in os.walk(en_root):
        for fn in files:
            if not is_json_file(fn):
                continue
            if only and fn != only:
                continue

            en_path = os.path.join(root, fn)
            rel = os.path.relpath(en_path, en_root)  # subruta dentro de en/
            es_path = os.path.join(es_root, rel)

            if not os.path.isfile(es_path):
                # Si estás en modo --only, esto es importante; si no, sólo avisamos luego
                pairs.append((rel, en_path, ""))  # es_path vacío => no existe
                continue

            pairs.append((rel, en_path, es_path))

    return pairs


# -----------------------------
# CLI
# -----------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Unifica pares en/<file>.json y es/<file>.json generando diccionarios EN name -> ES name."
    )
    ap.add_argument("--en", default="en", help="Carpeta raíz EN (default: en)")
    ap.add_argument("--es", default="es", help="Carpeta raíz ES (default: es)")
    ap.add_argument("--out", default="out", help="Carpeta de salida (default: out)")
    ap.add_argument("--only", default=None, help="Procesa solo este fichero (por nombre), ej: dnd5e.backgrounds.json")
    ap.add_argument("--by-id", action="store_true", help="Genera también salida por ID (out/<file>.byId.json)")
    ap.add_argument("--report", action="store_true", help="Genera también reporte (out/<file>.report.json)")
    args = ap.parse_args()

    en_root = args.en
    es_root = args.es
    out_root = args.out

    if not os.path.isdir(en_root):
        raise SystemExit(f"❌ No existe carpeta EN: {en_root}")
    if not os.path.isdir(es_root):
        raise SystemExit(f"❌ No existe carpeta ES: {es_root}")

    pairs = find_pairs(en_root, es_root, only=args.only)
    if not pairs:
        raise SystemExit("⚠ No se encontraron JSONs en EN con los criterios indicados.")

    processed = 0
    missing_es = 0

    for rel, en_path, es_path in pairs:
        if not es_path:
            print(f"⚠ No existe el par ES para: {rel}")
            missing_es += 1
            continue

        try:
            en_data = load_json(en_path)
            es_data = load_json(es_path)
        except Exception as e:
            print(f"❌ Error leyendo JSON '{rel}': {e}")
            continue

        res = build_dictionaries(en_data, es_data, rel_file=rel)

        # Output: diccionario plano EN->ES
        out_dict_path = os.path.join(out_root, rel).replace(".json", ".dict.json")
        write_json(out_dict_path, res.dict_name)

        # Opcional: por ID
        if args.by_id:
            out_by_id_path = os.path.join(out_root, rel).replace(".json", ".byId.json")
            write_json(out_by_id_path, res.dict_by_id)

        # Opcional: reporte
        if args.report:
            out_report_path = os.path.join(out_root, rel).replace(".json", ".report.json")
            write_json(out_report_path, res.report)

        processed += 1

        # Resumen en consola + warnings (limitados para no spamear)
        print(f"✅ {rel} -> {out_dict_path}  (pares: {res.report['counts']['paired']}, dict: {len(res.dict_name)})")
        if res.report["warnings"]:
            # imprime hasta 8 warnings por fichero
            for w in res.report["warnings"][:8]:
                print(f"   ⚠ {w}")
            if len(res.report["warnings"]) > 8:
                print(f"   ⚠ ... {len(res.report['warnings']) - 8} warnings más (usa --report para verlos todos)")

    print("\n--- RESUMEN ---")
    print(f"Procesados: {processed}")
    print(f"Sin par ES: {missing_es}")
    print(f"Salida en: {out_root}")

    if processed == 0:
        raise SystemExit("⚠ No se generó ninguna salida. Revisa nombres y estructura de carpetas.")


if __name__ == "__main__":
    main()