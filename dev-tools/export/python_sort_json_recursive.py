#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ordena un JSON recursivamente SOLO bajo las keys indicadas.

Ejemplos:

1) Ordenar solo dentro de "items"
py -3 sort_json_recursive_v02.py .\dnd5e.actors24\en\dnd5e.actors24.json --sort-only-key items

2) Ordenar dentro de "items,effects,activities"
py -3 sort_json_recursive_v02.py actores.json --sort-only-key items,effects,activities

3) Sobrescribir el archivo original
py -3 sort_json_recursive_v02.py actores.json --sort-only-key items --in-place

4) Guardar en un directorio distinto (mantiene nombre por defecto *_sorted.json)
py -3 sort_json_recursive_v02.py actores.json --sort-only-key items --out-dir .\out
py -3 sort_json_recursive_v02.py .\dnd5e.actors24\en\dnd5e.actors24.json --sort-only-key items --out-dir .\dnd5e.actors24\en\dnd5e.actors24-sort.json

5) Guardar con un nombre/ruta exacta
py -3 sort_json_recursive_v02.py actores.json --sort-only-key items -o .\out\actores_ordenado.json

6) Cambiar el sufijo por defecto
py -3 sort_json_recursive_v02.py actores.json --sort-only-key items --suffix _asc
"""

import argparse
import json
from pathlib import Path
from typing import Any, Optional


def parse_keys_csv(value: Optional[str]) -> set[str]:
    if not value:
        return set()
    return {p.strip() for p in value.split(",") if p.strip()}


def sort_dict_by_key_recursively(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: sort_dict_by_key_recursively(obj[k]) for k in sorted(obj.keys())}

    if isinstance(obj, list):
        return [sort_dict_by_key_recursively(x) for x in obj]

    return obj


def selective_sort_under_keys(obj: Any, target_keys: set[str]) -> Any:
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in target_keys and isinstance(v, (dict, list)):
                out[k] = sort_dict_by_key_recursively(v)
            else:
                out[k] = selective_sort_under_keys(v, target_keys)
        return out

    if isinstance(obj, list):
        return [selective_sort_under_keys(x, target_keys) for x in obj]

    return obj


def resolve_output_path(
    in_path: Path,
    in_place: bool,
    output: Optional[str],
    out_dir: Optional[str],
    suffix: str,
) -> Path:
    """
    Reglas (prioridad):
      1) --in-place  => output = input (y NO permite --output/--out-dir)
      2) --output    => output exacto
      3) --out-dir   => directorio destino + nombre por defecto (stem + suffix + .json)
      4) default     => mismo dir + nombre por defecto
    """
    if in_place:
        if output or out_dir:
            raise SystemExit("ERROR: --in-place no puede usarse junto con --output o --out-dir.")
        return in_path

    if output:
        return Path(output)

    filename = f"{in_path.stem}{suffix}.json"

    if out_dir:
        return Path(out_dir) / filename

    return in_path.with_name(filename)


def main():
    parser = argparse.ArgumentParser(
        description="Ordena un JSON recursivamente solo bajo keys específicas."
    )
    parser.add_argument("input_json", help="Ruta al JSON de entrada")
    parser.add_argument(
        "--sort-only-key",
        required=True,
        help='CSV de keys donde ordenar recursivamente. Ej: "items,effects"',
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="Indentación JSON (default 2). Usa 0 para minificado.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Sobrescribe el archivo original.",
    )

    # NUEVO: salida personalizada
    parser.add_argument(
        "-o",
        "--output",
        help="Ruta exacta del fichero de salida. Ej: .\\out\\mi_archivo.json",
    )
    parser.add_argument(
        "--out-dir",
        help="Directorio destino (se mantiene el nombre por defecto). Ej: .\\out",
    )
    parser.add_argument(
        "--suffix",
        default="_sorted",
        help='Sufijo para el nombre por defecto (default "_sorted").',
    )

    args = parser.parse_args()

    in_path = Path(args.input_json)
    if not in_path.is_file():
        raise SystemExit(f"ERROR: No existe el fichero de entrada: {in_path}")

    data = json.loads(in_path.read_text(encoding="utf-8"))

    target_keys = parse_keys_csv(args.sort_only_key)
    if not target_keys:
        raise SystemExit("ERROR: --sort-only-key está vacío. Debe contener al menos 1 key.")

    sorted_data = selective_sort_under_keys(data, target_keys)

    out_path = resolve_output_path(
        in_path=in_path,
        in_place=args.in_place,
        output=args.output,
        out_dir=args.out_dir,
        suffix=args.suffix,
    )

    # Crear directorio destino si no existe
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.indent == 0:
        out_path.write_text(
            json.dumps(sorted_data, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
    else:
        out_path.write_text(
            json.dumps(sorted_data, ensure_ascii=False, indent=args.indent),
            encoding="utf-8",
        )

    print(f"OK: JSON ordenado guardado en {out_path.resolve()}")


if __name__ == "__main__":
    main()