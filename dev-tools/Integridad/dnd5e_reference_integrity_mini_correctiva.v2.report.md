# dnd5e — Mini correctiva automática de referencias v2
Generado: `2026-03-26T23:39:36.952123+00:00`
## Alcance
- `dnd5e.content24.json`
- `dnd5e.actors24.json` (embeds rotos a `mmAppendixMonste`)
- arrastre de las correcciones inequívocas de v1 en `actors24` (`Zombie` / `Skeleton`)

## Resumen ejecutivo
- **content24**: 128 cambios automáticos.
  - 89 retargets de embeds de `mmMonstersAtoZ00`
    - 68 desde `dnd-monster-manual.content` a `dnd5e.content24`
    - 21 desde ids internos antiguos de `mmMonstersAtoZ00` a ids actuales
  - 39 referencias relativas locales convertidas a absolutas
  - Integridad global aproximada: **1579 / 1893** → **1668 / 1893**
- **actors24**: 35 cambios automáticos.
  - 30 embeds rotos a `mmAppendixMonste` resueltos
  - 5 arrastres de v1 (`phbmobZombie0000`×3 y `phbmobSkeleton00`×2)
  - En los 30 casos de `mmAppendixMonste`, el destino final ha sido `mmMonstersAtoZ00` porque no hay una página actual de apéndice equivalente en este dataset.
  - Integridad global aproximada: **3128 / 3204** → **3163 / 3204**

## content24 — criterio aplicado
1. Si un embed antiguo tenía un encabezado HTML inmediatamente anterior (`<h2>...`), se intentó resolver por `key`/`name` de la página actual.
2. Si el embed era el primero del bloque y no había encabezado previo, se usó la `key` de la propia página origen.
3. Si la referencia era relativa (`@UUID[.pageId]`) y la página existía dentro del mismo JournalEntry, se expandió a ruta absoluta.
4. Si la página objetivo no existe en el dataset actual, no se forzó corrección.

### Ejemplos de cambios en content24
- `entries.mmMonstersAtoZ00.pages.0B3uI9PTzjAVI0vv.systemText.content`
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.KJkoHa6ASqqSjrFX`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.0B3uI9PTzjAVI0vv`
  - base: **source_page / key_exact / Gelatinous Cube**
- `entries.mmMonstersAtoZ00.pages.2bADxJuWILSLbKnL.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.Tg5WKzTIgNAHo1Wq`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.2bADxJuWILSLbKnL`
  - base: **source_page / key_exact / Lemure**
- `entries.mmMonstersAtoZ00.pages.2DfEnIm8DZ3RUXYD.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.BK2fFx2HQtSJinWc`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.2DfEnIm8DZ3RUXYD`
  - base: **source_page / key_exact / Planetar**
- `entries.mmMonstersAtoZ00.pages.39KwfdzA13BzHkac.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.6RdlNz0OFdYqFwgH`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.39KwfdzA13BzHkac`
  - base: **source_page / key_exact / Fungi**
- `entries.mmMonstersAtoZ00.pages.3aopi18MGbDzmWZ5.systemText.content`
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.DMYEpWr3wvK4RLih`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.3aopi18MGbDzmWZ5`
  - base: **source_page / key_exact / Red Dragons**
- `entries.mmMonstersAtoZ00.pages.3jj30B8y8b0KajI2.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.B5wMYkbLXefYyuOS`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.3jj30B8y8b0KajI2`
  - base: **source_page / key_exact / Clay Golem**
- `entries.mmMonstersAtoZ00.pages.65CntoJ7zvQIx01s.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.XSbY1pakVSOrMX5q`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.65CntoJ7zvQIx01s`
  - base: **source_page / key_exact / Bearded Devil**
- `entries.mmMonstersAtoZ00.pages.6uMySCQYSC9akp91.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.OZ4pczqo9wAgj4CD`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.6uMySCQYSC9akp91`
  - base: **source_page / key_exact / Nightmare**
- `entries.mmMonstersAtoZ00.pages.6Xu0DgMDkEhIlqgg.systemText.content`
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.SYPUI0R76sVilXaV`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.6Xu0DgMDkEhIlqgg`
  - base: **source_page / key_exact / Sprite**
- `entries.mmMonstersAtoZ00.pages.75LcKiIsCIrohlPV.systemText.content`
  - `Compendium.dnd-monster-manual.content.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.Tnu6KW8hvlaLqaV3`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.75LcKiIsCIrohlPV`
  - base: **source_page / key_exact / Rust Monster**
- `entries.mmMonstersAtoZ00.pages.80kEKa3Nic5cGn3f.systemText.content`
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.l9Nak3iZRRAfQo0B`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.80kEKa3Nic5cGn3f`
  - base: **source_page / key_exact / Zombies**
- `entries.mmMonstersAtoZ00.pages.9Ek1sZ0PfUSb0o6k.systemText.content`
  - `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.4EtOTIaHnhnS9jA5`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.9Ek1sZ0PfUSb0o6k`
  - base: **source_page / key_exact / Vampires**

### Lo que sigue pendiente en content24
- Quedan **196** embeds viejos/externos de `mmMonstersAtoZ00` sin resolver automáticamente.
- El patrón dominante es que el bloque referencia páginas que **no existen** en este dataset SRD actual, por ejemplo:
  - `Lizardfolk Geomancer` desde `Magos`
  - `Lizardfolk Sovereign` desde `Magos`
  - `Gargoyle Ambushes` desde `Cubo gelatinoso`
  - `Brass Dragon Wyrmling` desde `Dragones de bronce`
  - `Young Brass Dragon` desde `Dragones de bronce`
  - `Adult Brass Dragon` desde `Dragones de bronce`
  - `Ancient Brass Dragon` desde `Dragones de bronce`
  - `Brass Dragon Lairs` desde `Dragones de bronce`
  - `Quaggoth` desde `Cuásit`
  - `Quaggoth Thonot` desde `Cuásit`
  - `Larva` desde `Lemur`
  - `Swarm of Larvae` desde `Lemur`
  - `Pixie` desde `Planetar`
  - `Pixie Wonderbringer` desde `Planetar`
  - `Beholder Lairs` desde `Bersérkeres`

## actors24 — criterio aplicado para `mmAppendixMonste`
1. Intento por encabezado previo del bloque (`<h1>` / `<h2>`) hacia una página actual de `mmAppendixMonste`.
2. Si no existe, fallback a `mmMonstersAtoZ00` por `key`/`name`.
3. Si sigue sin resolverse, fallback inverso por actor: se localiza la página actual de `mmMonstersAtoZ00` cuyo `text` ya embebe ese actor.

### Ejemplos de cambios en actors24
- `entries.mmAncientGreenDr.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.HxHIj9RZWeGNXKxV`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.zNzVq7B6Yt1dcY0z`
  - base: **heading_mmaz_name_fallback / Dragones verdes**
- `entries.mmAncientGreenDr.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.f6FP49T1ELv3aASd`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.zNzVq7B6Yt1dcY0z`
  - base: **actor_embed_reverse_fallback / Green Dragons**
- `entries.mmAncientGreenDr.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.kjE0Ff31hZsDdeye`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.zNzVq7B6Yt1dcY0z`
  - base: **actor_embed_reverse_fallback / Green Dragons**
- `entries.mmBalor000000000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.dstDspmI7LdrCsxy`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.mWcROUZcRLMN8Hxl`
  - base: **heading_mmaz_key_fallback / Balor**
- `entries.mmBarbedDevil000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.95Oeqtw6UgtSLiO1`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.Vzpho8zJkNsHQU7y`
  - base: **actor_embed_reverse_fallback / Barbed Devil**
- `entries.mmBeardedDevil00.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.PTpNAXCUpaUdNbcx`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.65CntoJ7zvQIx01s`
  - base: **actor_embed_reverse_fallback / Bearded Devil**
- `entries.mmBoneDevil00000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.LhlUSSOMbbHHTi5e`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.WK7w7PlQ02LoGhOb`
  - base: **heading_mmaz_name_fallback / Diablo óseo**
- `entries.mmChainDevil0000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.ZshK0GnbqU7TpaWe`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.Z6lIT7pPpdBRIMP0`
  - base: **actor_embed_reverse_fallback / Chain Devil**
- `entries.mmDretch00000000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.Tp3r2uMnilo9SUIu`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.ld6ImmsNezopmAiG`
  - base: **actor_embed_reverse_fallback / Dretch**
- `entries.mmDretch00000000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.YeZoNZxhdDHR3iC2`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.ld6ImmsNezopmAiG`
  - base: **heading_mmaz_key_fallback / Dretch**
- `entries.mmErinyes0000000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.YXZP2A00UrCViGCe`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.Ci0k7DXfjeh9FjN3`
  - base: **actor_embed_reverse_fallback / Erinyes**
- `entries.mmGlabrezu000000.biography`
  - `Compendium.dnd5e.content24.JournalEntry.mmAppendixMonste.JournalEntryPage.ywxoKSaj2hlvewVQ`
  - → `Compendium.dnd5e.content24.JournalEntry.mmMonstersAtoZ00.JournalEntryPage.BY9PswYVqCcQbMAx`
  - base: **heading_mmaz_key_fallback / Glabrezu**

### Estado tras la v2 en actors24
- Quedan **0** referencias rotas a `mmAppendixMonste`.
- Quedan **41** referencias rotas totales en `actors24`, pero ya no pertenecen al bloque `mmAppendixMonste` tratado en esta v2.

## Archivos generados
- `dnd5e.content24.references.mini-correctiva.v2.json`
- `dnd5e.actors24.references.mini-correctiva.v2.json`
- `dnd5e_reference_integrity_mini_correctiva.v2.report.md`
- `dnd5e_reference_integrity_mini_correctiva.v2.report.json`
