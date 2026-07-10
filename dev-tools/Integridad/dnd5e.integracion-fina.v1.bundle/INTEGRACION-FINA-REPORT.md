# dnd5e · integración fina v1

Esta entrega consolida la mejor versión disponible por archivo y deja un paquete listo para integrar en el módulo.

## Archivos finales por compendio

- `dnd5e.content24.json` ← `dnd5e.content24.es.integracion-fina.v1.json`
  - base ES: `dnd5e.content24.es.mini-correctiva.v2.1.no-key-translation.json`
  - overlay referencias: `dnd5e.content24.references.mini-correctiva.v6.external-mm.json`
  - paths aplicados: **135**
  - mismatches: **0**
  - nota: No se han traducido valores de clave key.
  - nota: Mantiene 15 embeds externos a dnd-monster-manual.content como dependencia opcional.
- `dnd5e.actors24.json` ← `dnd5e.actors24.es.integracion-fina.v1.json`
  - base ES: `dnd5e.actors24.es.mini-correctiva.v2.json`
  - overlay referencias: `dnd5e.actors24.references.mini-correctiva.v2.json`
  - paths aplicados: **28**
  - mismatches: **0**
- `dnd5e.classes24.json` ← `dnd5e.classes24.es.integracion-fina.v1.json`
  - base ES: `dnd5e.classes24.es.mini-correctiva.v2.json`
  - overlay referencias: `dnd5e.classes24.references.mini-correctiva.v1.json`
  - paths aplicados: **1**
  - mismatches: **0**
- `dnd5e.equipment24.json` ← `dnd5e.equipment24.es.mini-correctiva.v2.json`
  - base final: `dnd5e.equipment24.es.mini-correctiva.v2.json`
- `dnd5e.feats24.json` ← `dnd5e.feats24.es.mini-correctiva.v2.json`
  - base final: `dnd5e.feats24.es.mini-correctiva.v2.json`
- `dnd5e.monsterfeatures24.json` ← `dnd5e.monsterfeatures24.es.mini-correctiva.v2.json`
  - base final: `dnd5e.monsterfeatures24.es.mini-correctiva.v2.json`
- `dnd5e.origins24.json` ← `dnd5e.origins24.es.mini-correctiva.v2.json`
  - base final: `dnd5e.origins24.es.mini-correctiva.v2.json`
- `dnd5e.spells24.json` ← `dnd5e.spells24.es.mini-correctiva.v2.json`
  - base final: `dnd5e.spells24.es.mini-correctiva.v2.json`
- `dnd5e.tables24.json` ← `dnd5e.tables24.es.mini-correctiva.v2.json`
  - base final: `dnd5e.tables24.es.mini-correctiva.v2.json`

## Comprobaciones de cierre

- `content24`: cambios en claves `key`: **0**
- `content24`: embeds externos a `dnd-monster-manual.content`: **15**
- `actors24`: referencias antiguas a `phbmobZombie0000`: **0**
- `actors24`: referencias antiguas a `phbmobSkeleton00`: **0**
- `classes24`: referencia antigua a `mh3akteBDiLegqFK`: **0**

## Ficheros de soporte recomendados

- `babele-register.integracion-fina.v1.js`: añade registro de `dnd5e.equipment24`.
- `module.integracion-fina.v1.recommended-mm.json`: añade `dnd-monster-manual` como recomendación opcional para resolver los 15 embeds externos restantes de `content24`.

## Observación

`content24` queda integrado con las correcciones de referencias más fuertes disponibles. Aun así, mantiene 15 embeds externos deliberados a `dnd-monster-manual.content`; no son un fallo del JSON integrado, sino una dependencia opcional para completar esos casos.