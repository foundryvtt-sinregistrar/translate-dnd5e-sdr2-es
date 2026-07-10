# Mini correctiva automática de referencias v1
## Alcance
- Se han aplicado solo correcciones exactas y seguras.
- No se ha tocado `dnd5e.content24.json` porque sus roturas principales requieren un mapeo de ids antiguos a ids actuales que no es inequívoco con el dataset disponible.

## Resumen global
- Archivos procesados: **2**
- Archivos modificados: **2**
- Reemplazos totales aplicados: **10**

## Correcciones aplicadas

### dnd5e.actors24.json
- Archivo generado: `dnd5e.actors24.references.mini-correctiva.v1.json`
- Reemplazos aplicados: **9**
  - `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.iBFe4NyaCUinDoz3` × **4**
    - Motivo: Página válida actual en content24: 'Lanzar conjuros'
  - `Compendium.dnd5e.actors24.Actor.phbmobZombie0000` → `Compendium.dnd5e.actors24.Actor.mmZombie00000000` × **3**
    - Motivo: Actor válido actual en actors24: 'Zombi'
  - `Compendium.dnd5e.actors24.Actor.phbmobSkeleton00` → `Compendium.dnd5e.actors24.Actor.mmSkeleton000000` × **2**
    - Motivo: Actor válido actual en actors24: 'Esqueleto'

### dnd5e.classes24.json
- Archivo generado: `dnd5e.classes24.references.mini-correctiva.v1.json`
- Reemplazos aplicados: **1**
  - `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.mh3akteBDiLegqFK` → `Compendium.dnd5e.content24.JournalEntry.phbSpells0000000.JournalEntryPage.iBFe4NyaCUinDoz3` × **1**
    - Motivo: Página válida actual en content24: 'Lanzar conjuros'

## Pendiente para una v2 más agresiva
- Referencias rotas masivas a páginas obsoletas dentro de dnd5e.content24.json
- Embeds de actors24 hacia mmAppendixMonste sin correspondencia inequívoca
- Referencias externas a dnd-monster-manual.content
- Referencias heredadas a dnd5e.items y dnd5e.monsters
