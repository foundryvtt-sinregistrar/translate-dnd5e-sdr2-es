# dnd5e.content24 · mini correctiva de referencias v6
## Alcance
- Base: `dnd5e.content24.references.mini-correctiva.v5.json`
- Enfoque: **equivalencias externas manuales**
- Salida principal: `dnd5e.content24.references.mini-correctiva.v6.external-mm.json`

## Resultado
- Casos restantes de entrada: **15**
- Cambios aplicados: **18**
  - Retargets local → external MM content: **3**
  - Normalizaciones de sintaxis `@Embed[...]`: **15**
- Rutas tocadas: **8**

## Resolución
Esta v6 **no fuerza equivalencias locales dudosas**. En su lugar:
1. reapunta los 3 casos que aún referenciaban páginas locales inexistentes hacia el pack externo correcto
2. normaliza la sintaxis de los 15 embeds restantes
3. deja el bloque final **condicionalmente resuelto** si está instalado el módulo oficial:

- `dnd-monster-manual`
- pack usado: `Compendium.dnd-monster-manual.content`

## Estado final
- Sin el módulo externo: **15** referencias siguen dependiendo de contenido no instalado
- Con el módulo externo: **0** casos pendientes en este remanente v5

## Casos cubiertos
- Quaggoth
- Quaggoth Thonot
- Pixie
- Pixie Wonderbringer
- Beholder Lairs
- Arch-hag Lairs
- Githzerai Monk
- Githzerai Zerth
- Githzerai Psion
- Adventures with Gith
- Empyrean Iota
- Empyrean
- Demilich Lairs
- Manes
- Manes Vaporspawn

## Archivos incluidos
- `dnd5e.content24.references.mini-correctiva.v6.external-mm.json`
- `module.json.recommended-dnd-monster-manual.v1.json`
- `dnd5e_reference_integrity_mini_correctiva.v6.content24.conditional-external.json`
- `dnd5e_reference_integrity_mini_correctiva.v6.content24.report.json`
