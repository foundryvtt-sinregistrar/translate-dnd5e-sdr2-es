# D&D SRD 5.2.1 — Traducción al español

**Español** | [English](README.en.md)

Traducción para Foundry VTT mediante Babele. Identificador: `translate-dnd5e-sdr2-es`.

## Estado

Versión: **1.14.2**. Traducciones de los compendios SRD del sistema dnd5e, con correcciones de ejecución específicas. El identificador histórico `sdr2` se conserva. Las pruebas automáticas no sustituyen la revisión editorial y funcional en Foundry.

Consulta [CHANGELOG.md](CHANGELOG.md).

## Requisitos

Versiones declaradas en el manifiesto; «—» indica que no se declara ese límite.

| Dependencia | Mínima | Verificada |
|---|---|---|
| Foundry VTT | 14.367 | 14.368 |
| dnd5e | 6.0.0 | 6.0.3 |
| babele | 2.9.1 | 2.9.1 |

Instala y activa las dependencias, adquiriendo por separado los productos oficiales cuando sean necesarios.

El módulo oficial Monster Manual es una recomendación opcional del manifiesto para resolver referencias externas; no es una dependencia obligatoria de la traducción SRD.

## Instalación

En la configuración de Foundry, abre **Add-on Modules → Install Module** y utiliza este manifiesto:

```text
https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/latest/download/module.json
```

Para instalar manualmente, descarga `translate-dnd5e-sdr2-es.zip` de las [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases). Con Foundry detenido, extrae la carpeta `translate-dnd5e-sdr2-es` en `Data/modules/`; el manifiesto debe quedar en `Data/modules/translate-dnd5e-sdr2-es/module.json`.

## Activación

1. Abre un mundo dnd5e.
2. Activa Babele, sus dependencias, los productos oficiales requeridos y esta traducción.
3. Selecciona **Español** y recarga el mundo.
4. Abre un compendio traducido para comprobar el resultado.

El registro es automático para `es` y sus variantes regionales. Otros idiomas no activan la traducción española.

## Actualización

Actualiza desde Foundry o sustituye la carpeta con el ZIP publicado y Foundry detenido. Recarga el mundo. Las copias ya importadas no se sincronizan automáticamente: revisa las diferencias antes de sustituir documentos con cambios propios.

## Contenido incluido

- `dnd5e.actors24.json`.
- `dnd5e.classes24.json`.
- `dnd5e.content24.json`.
- `dnd5e.effects.json`.
- `dnd5e.equipment24.json`.
- `dnd5e.feats24.json`.
- `dnd5e.monsterfeatures24.json`.
- `dnd5e.origins24.json`.
- `dnd5e.spells24.json`.
- `dnd5e.tables24.json`.

## Limitaciones

La cobertura textual y las pruebas automáticas no acreditan todas las automatizaciones de una partida. Conserva las limitaciones indicadas en Estado. Las copias importadas no se actualizan automáticamente. Las nuevas URLs de release necesitan una publicación con sus adjuntos; mientras no estén disponibles, utiliza un ZIP validado. No se distribuyen fuentes privadas, PDF, OCR ni exportaciones oficiales completas.

## Soporte y contribuciones

Comunica errores en las [incidencias](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/issues), indicando versiones, compendio/documento afectado, pasos, resultado esperado y observado, y si se trata de una copia importada.

## Desarrollo

La [guía de desarrollo](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/blob/main/DEVELOPER.md) está disponible en el repositorio y se excluye del ZIP instalable.

## Licencia y créditos

Consulta la licencia y sus condiciones en [LICENSE.md](LICENSE.md). Este proyecto incorpora material del System Reference Document 5.2.1 de Wizards of the Coast LLC, bajo Creative Commons Attribution 4.0 (CC BY 4.0). Dungeons & Dragons SRD 5.2.1 © Wizards of the Coast LLC. Se conserva la atribución completa en el archivo de licencia.

Traducción no oficial, sin afiliación con Wizards of the Coast ni Foundry VTT. Los materiales del producto oficial pertenecen a sus respectivos titulares. Autor del módulo: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).
