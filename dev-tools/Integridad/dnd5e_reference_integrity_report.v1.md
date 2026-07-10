# Informe de integridad de referencias dnd5e

Generado: 2026-03-26T16:13:19.938382+00:00

## Alcance y método
- Se han recorrido todos los strings de los JSON dnd5e.* suministrados.
- Se han validado @UUID[...] y @Embed[...] contra los ids presentes en los packs del dataset actual.
- Se han validado referencias relativas como @UUID[.pageId] y [[/item .itemId]] cuando el contexto permitía resolverlas.
- Las referencias a packs externos se separan en: dependencia externa no declarada y pack auxiliar del sistema no incluido en este dataset.
- Una referencia marcada como 'external' no implica necesariamente rotura en runtime, pero sí requiere revisión de dependencia/alcance.

## Resumen global
- Referencias analizadas: **6530**
- Referencias internas válidas: **6120**
- Roturas internas detectadas: **108**
- Referencias externas: **302**
  - Dependencia externa no declarada: **217**
  - Packs auxiliares del sistema no incluidos en este dataset: **85**

### Mejoras globales prioritarias
- **Registrar dnd5e.equipment24 en Babele** (high) — Los enlaces @UUID hacia equipment24 pueden abrir contenido sin traducir aunque el JSON exista.
- **Declarar o eliminar la dependencia dnd-monster-manual.content** (high) — Si el pack externo no está instalado, los embeds de lore/appendix fallarán.
- **Corregir la sintaxis de @Embed en content24.systemText.content** (high) — Foundry puede no parsear correctamente esos embeds.

## dnd5e.origins24 — Orígenes
- Severidad: **baja**
- Total refs: **100**
- Válidas internas: **98**
- Roturas internas: **0**
- Externas: **2**
  - Packs auxiliares del sistema no incluidos aquí: **2**
- Mejoras propuestas:
  - Mantener, pero revisar las 2 referencias heredadas a dnd5e.items y migrarlas a dnd5e.equipment24 si existe equivalente 2024.

## dnd5e.feats24 — Dotes
- Severidad: **limpia**
- Total refs: **3**
- Válidas internas: **3**
- Roturas internas: **0**
- Externas: **0**
- Mejoras propuestas:
  - Sin roturas detectadas en el dataset suministrado. Solo conviene mantener una pasada de preflight en cada release.

## dnd5e.monsterfeatures24 — Rasgos de monstruos
- Severidad: **limpia**
- Total refs: **71**
- Válidas internas: **71**
- Roturas internas: **0**
- Externas: **0**
- Mejoras propuestas:
  - Sin roturas detectadas. Mantener preflight de @UUID/@Embed antes de publicar.

## dnd5e.tables24 — Tablas
- Severidad: **limpia**
- Total refs: **147**
- Válidas internas: **147**
- Roturas internas: **0**
- Externas: **0**
- Mejoras propuestas:
  - Sin roturas detectadas. Mantener validación específica de rutas Item.ActiveEffect porque el pack depende mucho de ellas.

## dnd5e.classes24 — Clases
- Severidad: **media**
- Total refs: **327**
- Válidas internas: **324**
- Roturas internas: **1**
- Externas: **2**
  - Packs auxiliares del sistema no incluidos aquí: **2**
- Objetivos rotos principales:
  - `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` × 1
- Ejemplos:
  - `entries.phbwlkPactMagic0.description` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` (missing_nested)
- Mejoras propuestas:
  - Corregir la referencia rota a JournalEntryPage mh3akteBDiLegqFK. El candidato más probable en el dataset actual es phbSpells0000000 → iBFe4NyaCUinDoz3 ('Lanzar conjuros').
  - Revisar las 2 referencias heredadas a dnd5e.items y migrarlas a equipment24 cuando exista equivalente 2024.

## dnd5e.spells24 — Conjuros
- Severidad: **baja**
- Total refs: **84**
- Válidas internas: **78**
- Roturas internas: **0**
- Externas: **6**
  - Packs auxiliares del sistema no incluidos aquí: **6**
- Mejoras propuestas:
  - Las 6 referencias a dnd5e.monsters parecen dependencias de packs auxiliares del sistema. Decidir si se mantienen como dependencia explícita o se migran a actors24.

## dnd5e.equipment24 — Equipo
- Severidad: **baja**
- Total refs: **701**
- Válidas internas: **691**
- Roturas internas: **0**
- Externas: **10**
  - Packs auxiliares del sistema no incluidos aquí: **10**
- Mejoras propuestas:
  - Registrar este pack en babele-register.js; ahora mismo el JSON existe pero no se carga en Babele.
  - Revisar las 10 referencias a dnd5e.items y migrarlas a equipment24 si ya hay versión 2024 equivalente.

## dnd5e.content24 — Reglas / Journal Entries
- Severidad: **alta**
- Total refs: **1893**
- Válidas internas: **1579**
- Roturas internas: **68**
- Externas: **246**
  - Dependencia externa no declarada: **217**
  - Packs auxiliares del sistema no incluidos aquí: **29**
- Sintaxis sospechosa de macros: **208**
- Objetivos rotos principales:
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.4EtOTIaHnhnS9jA5` × 2
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.sTeJ3Fyus2oyLaRk` × 2
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.85wfFNgms1hLuQ0m` × 1
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.2w4jxh9j1P9Lr9d1` × 1
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.KJkoHa6ASqqSjrFX` × 1
- Ejemplos:
  - `entries.mmMonstersAtoZ00.pages.09MGKnX2pmlDjmdl.systemText.content` → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.85wfFNgms1hLuQ0m` (missing_nested)
  - `entries.mmMonstersAtoZ00.pages.09MGKnX2pmlDjmdl.systemText.content` → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.2w4jxh9j1P9Lr9d1` (missing_nested)
  - `entries.mmMonstersAtoZ00.pages.0B3uI9PTzjAVI0vv.systemText.content` → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.KJkoHa6ASqqSjrFX` (missing_nested)
  - `entries.mmMonstersAtoZ00.pages.0B3uI9PTzjAVI0vv.systemText.content` → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.rOTJWyJC8aZdsngw` (missing_nested)
  - `entries.mmMonstersAtoZ00.pages.1Atgt2aMSTqlG5eB.systemText.content` → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.1x1Q6MFjBz5OV6We` (missing_nested)
- Mejoras propuestas:
  - Reparar los 208 embeds con sintaxis '@Embed[...] caption=false ...' y mover todas las opciones dentro de los corchetes.
  - Resolver 68 referencias internas rotas a páginas de mmMonstersAtoZ00; parecen ids obsoletos dentro de systemText.content.
  - Resolver o declarar la dependencia externa dnd-monster-manual.content (217 refs).
  - Revisar las 29 referencias a dnd5e.monsters para decidir si siguen siendo válidas en la línea 2024 o deben migrarse a actors24.
  - Seguir preservando la clave key sin traducir; no es un fallo de referencia pero evita romper índices internos.

## dnd5e.actors24 — Actores
- Severidad: **alta**
- Total refs: **3204**
- Válidas internas: **3129**
- Roturas internas: **39**
- Externas: **36**
  - Packs auxiliares del sistema no incluidos aquí: **36**
- Objetivos rotos principales:
  - `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` × 4
  - `Compendium.dnd5e.actors24.Actor.phbmobZombie0000` × 3
  - `Compendium.dnd5e.actors24.Actor.phbmobSkeleton00` × 2
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.HxHIj9RZWeGNXKxV` × 1
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.f6FP49T1ELv3aASd` × 1
- Ejemplos:
  - `entries.SefrisLv01000000.items.LGqdCjSUGKny0Jz2.description` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` (missing_nested)
  - `entries.SefrisLv05000000.items.LGqdCjSUGKny0Jz2.description` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` (missing_nested)
  - `entries.SefrisLv11000000.items.LGqdCjSUGKny0Jz2.description` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` (missing_nested)
  - `entries.SefrisLv17000000.items.LGqdCjSUGKny0Jz2.description` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` (missing_nested)
  - `entries.mmAncientGreenDr.biography` → `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.HxHIj9RZWeGNXKxV` (missing_nested)
- Mejoras propuestas:
  - Corregir las referencias rotas a Actor.phbmobZombie0000 y Actor.phbmobSkeleton00. En el dataset actual los candidatos son mmZombie00000000 y mmSkeleton000000.
  - Corregir las 30 referencias rotas a páginas de content24 (sobre todo mmAppendixMonste y la página de 'Lanzar conjuros').
  - Revisar las 36 referencias heredadas a dnd5e.items/dnd5e.monsters y decidir si se migran a equipment24/actors24.
  - Mantener el uso de referencias relativas [[/item .itemId]]; la validación local las encontró correctas.
