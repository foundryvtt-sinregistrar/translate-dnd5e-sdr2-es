# Plan de trabajo para la validación en Foundry 14

## Objetivo

Completar la cobertura de traducción del SRD 5.2.1 y verificar formalmente el
módulo con Foundry VTT 14.363, D&D 5e 5.3.3 y Babele 2.9.1, sin confundir los
compendios modernos (`*24`) con los compendios heredados del SRD 5.1.

## Estado comprobado

- El módulo 1.13.4 está activo y Babele carga correctamente sus nueve paquetes.
- Los nueve JSON de compendio conservan paridad estructural con sus exportaciones
  inglesas.
- No se observaron errores de carga de este módulo ni de sus conversores.
- Las fichas modernas muestran nombres, descripciones, actividades, efectos y
  elementos embebidos traducidos.
- La ficha del actor Akra y sus elementos se abren correctamente en Foundry 14.
- La validación final está documentada en `foundry14-validation.md` y confirma
  la ejecución con Foundry 14.363, D&D 5e 5.3.3 y Babele 2.9.1.

## Trabajo prioritario

### 1. Traducir los componentes materiales de los conjuros

**Estado: completado.** Se extrajeron y validaron 188 componentes materiales
del PDF oficial; la ficha de Santuario se verificó también en Foundry.

**Problema:** `system.materials.value` no forma parte de la exportación ni del
mapeo actual. Por ello, una ficha como **Santuario** muestra el componente
`a shard of glass from a mirror` en inglés.

**Proceso:**

1. Incorporar `system.materials.value` al esquema de exportación de
   `dnd5e.spells24`.
2. Extraer todos los componentes materiales del paquete fuente.
3. Obtener la redacción oficial española del PDF SRD 5.2.1 y relacionarla por ID
   de conjuro, no únicamente por nombre.
4. Añadir un campo estable, por ejemplo `materials`, al mapeo y a cada entrada
   que lo necesite.
5. Extender el auditor para detectar componentes vacíos, idénticos al inglés o
   con indicios de texto inglés.
6. Validar una muestra de conjuros con componentes normales, consumibles y con
   coste indicado.

**Criterio de aceptación:** ninguna ficha de `dnd5e.spells24` muestra texto
inglés en «Materiales», y el auditor incluye este campo en sus resultados.

### 2. Revisar campos visibles omitidos por los exportadores

**Estado: completado.** El inventario contiene 1.603 valores agrupados en 46
rutas normalizadas y forma parte de la validación de publicación.

**Problema:** la auditoría actual comprueba los campos exportados, pero Foundry
puede mostrar otros valores de `system`, como materiales, textos especiales,
condiciones de activación o etiquetas derivadas.

**Proceso:**

1. Comparar las exportaciones completas de `dev-tools/export/data/export_all`
   con los nueve archivos reducidos usados por Babele.
2. Crear un inventario de cadenas visibles que no tengan ruta de traducción.
3. Clasificar cada ruta como traducible, dato técnico, valor localizado por
   D&D 5e o valor derivado en tiempo de ejecución.
4. Incorporar al mapeo únicamente las rutas traducibles y añadirlas al auditor.

**Criterio de aceptación:** todas las cadenas visibles de los paquetes modernos
tienen propietario documentado: módulo SRD, localización de D&D 5e o Babele.

### 3. Investigar el subtipo derivado de los actores

**Estado: completado.** El valor preparado por D&D 5e se corrige al renderizar
la ficha. Akra muestra `Dracónido` y ya no muestra `Dragonborn`.

**Problema:** Akra muestra `Dragonborn` junto al objeto de especie traducido como
`Dracónido`. El valor parece derivarse de la especie o de datos preparados por
el sistema, y no aparece en la exportación reducida del actor.

**Proceso:**

1. Identificar la ruta o función de D&D 5e 5.3.3 que genera el subtipo visible.
2. Comprobar si el valor se corrige al importar el actor al mundo.
3. Determinar si debe corregirse mediante el conversor `actorFullById`, mediante
   un campo adicional o en la localización española del sistema.
4. Probar otras especies y tipos de criatura para evitar una solución específica
   solo para `Dragonborn`.

**Criterio de aceptación:** los actores muestran la especie o subtipo en español,
o el informe identifica de forma reproducible que es una incidencia externa.

## Pruebas de regresión

Después de cada lote de cambios:

1. Ejecutar `python dev-tools/pdf-audit/validate_release.py`.
2. Confirmar que `.gitignore` y otros cambios del usuario no entren en el commit.
3. Crear un commit descriptivo en inglés por unidad lógica.
4. Recargar el mundo con `Ctrl+F5`, ya que Babele mantiene las traducciones en
   memoria durante la sesión.
5. Comprobar un documento de cada paquete moderno:
   `actors24`, `classes24`, `content24`, `equipment24`, `feats24`,
   `monsterfeatures24`, `origins24`, `spells24` y `tables24`.
6. Ejecutar al menos una actividad de ataque, salvación, daño y curación.
7. Abrir referencias, documentos embebidos y efectos enlazados.
8. Revisar la consola filtrando por `translate-dnd5e-sdr2-es`, `Babele` y los
   nombres de los conversores propios.

## Incidencias externas o separadas

- Las etiquetas `Description`, `Details`, `Activities` y `Effects` pertenecen a
  la localización de la interfaz de D&D 5e, no a los compendios de este módulo.
- Las claves visibles `DND5E.DeathSaveSuccessLabelN.other` y equivalentes son
  incidencias de la traducción del sistema D&D 5e.
- Los avisos de Babele sobre conversores `range` y `activities` proceden de una
  traducción heredada activa y deben resolverse en ese módulo, no aquí.
- Los compendios del SRD 5.1 deben excluirse de esta campaña de pruebas; el
  objetivo de este módulo son los paquetes modernos `dnd5e.*24`.

## Cierre y compatibilidad

Solo después de superar todas las pruebas se debe actualizar `module.json` para
declarar Foundry 14.363, D&D 5e 5.3.3 y Babele 2.9.1 como versiones verificadas.
La actualización de compatibilidad debe constituir un commit independiente y
estar respaldada por el informe de ejecución final.

**Estado: autorizado por la validación final.** Las pruebas se completaron el
20 de agosto de 2026 y permiten realizar el commit independiente de
compatibilidad.
