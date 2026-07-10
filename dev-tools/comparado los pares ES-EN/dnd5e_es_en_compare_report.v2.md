# Informe comparativo ES vs EN

Generado: 2026-03-25T22:28:25.488246+00:00

## Alcance
- Comparados 9 pares ES/EN.
- Ya no quedan pares pendientes dentro del bloque actual.

## dnd5e.classes24.json ↔ dnd5e.classes24-en.json
- Entradas: ES 282 / EN 282
- Diferencia top-level: ES=['label', 'mapping', 'folders', 'entries'] / EN=['label', 'folders', 'entries']
- Cadenas probablemente sin traducir en ES: 1 (entradas afectadas: 1)
  - `phbinvOnewithSha` · `/entries/phbinvOnewithSha/effects/9svfDetqjhsFP3ey/name` → `Invisible`

## dnd5e.actors24.json ↔ dnd5e.actors24-en.json
- Entradas: ES 441 / EN 441
- Entradas con campos anidados faltantes en ES: 14 — ejemplos: `mmPlanetar000000`(51), `mmAdultBrassDrag`(30), `mmAdultBlackDrag`(23), `mmAdultBlueDrago`(22), `mmCouatl00000000`(19)
- `folder` posiblemente sin traducir en ES: 7 — ejemplos: `MorthosLv1100000`→Level 11, `AkraLv0500000000`→Level 5, `QuillatheLv11000`→Level 11, `MerricLv17000000`→Level 17, `MerricLv11000000`→Level 11
- Cadenas probablemente sin traducir en ES: 87 (entradas afectadas: 54)
  - `AkraLv0500000000` · `/entries/AkraLv0500000000/folder` → `Level 5`
  - `AothLv0500000000` · `/entries/AothLv0500000000/items/dwMaTtPq9jnWmVLG/effects/Oy8fnNNzPmehxXio/name` → `Shillelagh (1d10)`
  - `AothLv0500000000` · `/entries/AothLv0500000000/items/dwMaTtPq9jnWmVLG/effects/QPsqj6jfS0iXSrTs/name` → `Shillelagh (1d8)`

## dnd5e.equipment24.json ↔ dnd5e.equipment24-en.json
- Entradas: ES 634 / EN 635
- Diferencia top-level: ES=['label', 'mapping', 'folders', 'entries'] / EN=['label', 'folders', 'entries']
- Entradas presentes solo en EN: `dmgManualOfGolem`
- Entradas con campos anidados faltantes en ES: 2 — ejemplos: `dmgCarrionCrawle`(1), `phbagBallBearing`(1)
- Cadenas probablemente sin traducir en ES: 7 (entradas afectadas: 7)
  - `dmgDustOfDisappe` · `/entries/dmgDustOfDisappe/effects/MC5GAZMrAc4wSvAS/name` → `Invisible`
  - `dmgEarthRingOfEl` · `/entries/dmgEarthRingOfEl/effects/cN85nWiTzfGzWR7D/name` → `Charmed`
  - `dmgFireRingOfEle` · `/entries/dmgFireRingOfEle/effects/cN85nWiTzfGzWR7D/name` → `Charmed`

## dnd5e.feats24.json ↔ dnd5e.feats24-en.json
- Entradas: ES 17 / EN 17
- Diferencia top-level: ES=['label', 'mapping', 'folders', 'entries'] / EN=['label', 'folders', 'entries']
- Cadenas probablemente sin traducir en ES: 0 (entradas afectadas: 0)

## dnd5e.content24.json ↔ dnd5e.content24-en.json
- Entradas: ES 53 / EN 53
- Cadenas probablemente sin traducir en ES: 59 (entradas afectadas: 8)
  - `dmgMagicItemList` · `/entries/dmgMagicItemList/pages/72JPQib8zeo3bhZJ/name` → `K-O`
  - `dmgMagicItemList` · `/entries/dmgMagicItemList/pages/IT9XH2oNs3kN5fG5/name` → `A-B`
  - `dmgMagicItemList` · `/entries/dmgMagicItemList/pages/QkZq96gbQRbKYqaE/name` → `F-J`

## dnd5e.monsterfeatures24.json ↔ dnd5e.monsterfeatures24.en.json
- Entradas: ES 390 / EN 391
- Diferencia top-level: ES=['label', 'mapping', 'folders', 'entries'] / EN=['label', 'folders', 'entries']
- Entradas presentes solo en EN: `mmEarthGlide0000`
- Entradas con campos anidados faltantes en ES: 124 — ejemplos: `mmLoathsomeLimbs`(6), `mmRoar0000000000`(3), `mmCrush000000000`(2), `mmParalyzingBrea`(2), `mmPetrifyingBite`(2)
- Cadenas probablemente sin traducir en ES: 4 (entradas afectadas: 4)
  - `mmMindInvasion00` · `/entries/mmMindInvasion00/activities/SxaXUPLBRHtYL9As/name` → `Mind Spike`
  - `mmMindJolt000000` · `/entries/mmMindJolt000000/activities/f3Q5Cky4bKFVdOT2/name` → `Mind Spike`
  - `mmMistyStep00000` · `/entries/mmMistyStep00000/activities/sstmyMnemXbXqI5Y/name` → `Misty Step`

## dnd5e.origins24.json ↔ dnd5e.origins24-en.json
- Entradas: ES 54 / EN 54
- Diferencia top-level: ES=['label', 'mapping', 'folders', 'entries'] / EN=['label', 'folders', 'entries']
- Entradas con campos anidados faltantes en ES: 2 — ejemplos: `phbsptGnomishCun`(1), `phbsptLargeForm0`(1)
- Cadenas probablemente sin traducir en ES: 3 (entradas afectadas: 3)
  - `phbbgCriminal000` · `/entries/phbbgCriminal000/name` → `Criminal`
  - `phbspInfernalTie` · `/entries/phbspInfernalTie/name` → `Tiefling, Infernal`
  - `phbsptTrance0000` · `/entries/phbsptTrance0000/name` → `Trance`
- Nota de consistencia: `/folders/Tiefling` → `Tiflin`, pero en varias entries/textos sigue apareciendo `Tiefling`/`tiefling`.

## dnd5e.spells24.json ↔ dnd5e.spells24-en.json
- Entradas: ES 341 / EN 341
- Cadenas probablemente sin traducir en ES: 7 (entradas afectadas: 4)
  - `phbsplGreaterInv` · `/entries/phbsplGreaterInv/effects/NDpw6r63ZdEgks1a/name` → `Invisible`
  - `phbsplInvisibili` · `/entries/phbsplInvisibili/effects/9svfDetqjhsFP3ey/name` → `Invisible`
  - `phbsplMislead000` · `/entries/phbsplMislead000/effects/3mTWrCYjgS8jIDRU/name` → `Invisible`

## dnd5e.tables24.json ↔ dnd5e.tables24-en.json
- Entradas: ES 66 / EN 66
- Cadenas probablemente sin traducir en ES: 1 (entradas afectadas: 1)
  - `phbFiendishLegac` · `/entries/phbFiendishLegac/results/3-3` → `Tiefling, Infernal`
