# Registro de adopción

Proyecto: `translate-dnd5e-sdr2-es`. Rama: `chore/homogeneizacion-documentacion`.

Plantilla inicial: PHB `caf298ee2c8b78c27634c2e2f23baf87e44243fe`; base anterior a esta aplicación en el destino: `2b194f1b0e803f1bcb523268c95c4c527614704f`. Base común ampliada: `4ab392ea3fbe0e3d7eb44f803a07fe631d15916e` (plantilla versión 2; perfiles y SHA-256). La suite común y el constructor proceden de esa revisión; el perfil de cada destino se conserva por separado.

## Archivos y adaptaciones

Documentación bilingüe, DEVELOPER, CHANGELOG, `.editorconfig`, `.gitattributes`, base de `.gitignore`, constructor y suite de 24 pruebas compartida. El perfil versionado conserva alias `translate-dnd5e-sdr2-es.zip`, canal `latest` y variante `standard`. Se mantiene la licencia existente; los avisos de DM/Tomb no sustituyen la decisión pendiente sobre sus aportaciones.

Conservar el identificador `sdr2`, las atribuciones CC BY 4.0 y `scripts/runtime-fixes.js`. Los generadores y auditorías que escriben archivos están en `dev-tools/validation/`, separados de las tres suites Node portables. No ejecutes `build_effects_translation.py` para validar: modifica compendios. Los contadores de descargas siguen versionados pero se excluyen del ZIP.

## Sincronización

Antes de actualizar herramientas comunes, compara la base registrada con la nueva revisión de PHB y revisa las diferencias de cada archivo. Conserva este perfil, las suites propias y los adaptadores. No sobrescribas traducciones ni adaptes una licencia mediante una copia ciega. Los SHA-256 del inventario identifican los bytes de Git sin conversiones LF/CRLF.

## Validación y commits

La comprobación en un clon aislado detectó imports de Babele desde una carpeta hermana. Se conservan esas dos pruebas como integración con carga diferida y omisión visible si falta Babele; las otras 16 pruebas Node son independientes de esa instalación.

El informe global registra los resultados definitivos, omisiones, inventario del ZIP y commits. Consulta `git log --oneline -- dev-tools/homogeneizacion/ADOPCION.md` para localizar la adopción. CI remota, pruebas funcionales en Foundry y publicación se verifican por separado; no se presentan como ejecutadas por una validación local.

La rama incorpora los siete commits remotos de contadores junto al commit local de versión, sin alterar main. Se conserva el identificador sdr2 y el texto original de la licencia al renombrarla a LICENSE.md.
