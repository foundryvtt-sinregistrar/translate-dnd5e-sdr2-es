# Informe de validación en Foundry VTT 14

## Entorno validado

- Fecha: 20 de agosto de 2026
- Foundry VTT: 14.363
- Sistema D&D 5e: 5.3.3
- Babele: 2.9.1
- Módulo: 1.13.4
- Mundo: `TestModuloLevels`
- Navegador: Google Chrome con sesión de Gamemaster autenticada

## Validación automatizada

Se ejecutó `python dev-tools/pdf-audit/validate_release.py` después de los
cambios. El validador confirmó:

- 12 archivos JSON y 9 paquetes de compendio válidos;
- 188 componentes materiales respaldados por el PDF oficial;
- inventario actualizado de todos los campos de texto visibles;
- ausencia de normalizaciones, duplicados o sincronizaciones pendientes.

También se comprobó la sintaxis de `scripts/runtime-fixes.js` y la ausencia de
errores de espacios o formato mediante `git diff --check`.

## Pruebas funcionales en Foundry

### Carga del módulo

Babele cargó correctamente los nueve paquetes modernos:

- `dnd5e.actors24`
- `dnd5e.classes24`
- `dnd5e.content24`
- `dnd5e.equipment24`
- `dnd5e.feats24`
- `dnd5e.monsterfeatures24`
- `dnd5e.origins24`
- `dnd5e.spells24`
- `dnd5e.tables24`

La consola no mostró errores asociados a `translate-dnd5e-sdr2-es`, sus
conversores ni `scripts/runtime-fixes.js`.

### Actor preparado

Se abrió **Akra (nivel 1)** desde `dnd5e.actors24`. La ficha mostró
`Humanoide` y `Dracónido`; el subtipo inglés `Dragonborn` no estaba presente.
Esto confirma que la corrección en tiempo de ejecución se aplica después de
reiniciar el servidor y volver a cargar el mundo.

### Componentes materiales

Se abrió **Santuario** desde `dnd5e.spells24`. La ficha mostró:

> Materiales: un trozo de vidrio de un espejo

El nombre, la descripción y el componente material aparecen traducidos y el
documento conserva la etiqueta de procedencia `SRD 5.2`.

## Resultado

Las correcciones auditadas superan las validaciones estructurales y las pruebas
visuales seleccionadas en Foundry VTT 14.363. El módulo puede declarar como
verificadas las versiones empleadas en esta ejecución: Foundry 14.363,
D&D 5e 5.3.3 y Babele 2.9.1.

Las incidencias de interfaz y de módulos externos enumeradas en el plan de
acción permanecen fuera del alcance del paquete de traducción SRD 5.2.1.
