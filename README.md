# D&D SRD 5.2.1 — Traducción al español

**Versión actual — Foundry v14**

![Foundry v14](https://img.shields.io/badge/Foundry-v14-green)
[![Release v1.14.3](https://img.shields.io/badge/release-v1.14.3-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.14.3)
![dnd5e 6.0.3](https://img.shields.io/badge/dnd5e-6.0.3-blue)
![Babele 2.9.1 required](https://img.shields.io/badge/Babele-2.9.1_required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

[![Downloads v1.14](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/downloads-v14.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases)

**Compatibilidad histórica — Foundry v13**

![Foundry v13](https://img.shields.io/badge/Foundry-v13-green)
[![Release v1.13.4](https://img.shields.io/badge/release-v1.13.4-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.4)
![dnd5e 5.2.x](https://img.shields.io/badge/dnd5e-5.2.x-lightgrey)
![Babele Required](https://img.shields.io/badge/Babele-required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

[![Downloads v1.13](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/downloads-v13.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases)


**Español** | [English](README.en.md)

Traducción para Foundry VTT mediante Babele. Identificador: `translate-dnd5e-sdr2-es`.

## Estado

Versión: **1.14.3**. Traducciones de los compendios SRD del sistema dnd5e, con correcciones de ejecución específicas. El identificador histórico `sdr2` se conserva. Las pruebas automáticas no sustituyen la revisión editorial y funcional en Foundry.

Consulta [CHANGELOG.md](CHANGELOG.md).

Comprobación del 28 de septiembre de 2026 en Foundry 14.368, dnd5e 6.0.3 y Babele 2.9.1: lectura de 2453 documentos en 10 compendios, comprobación de nombres y campos de texto explícitos e importación y revisión visual de una muestra. No es una revisión lingüística ni funcional exhaustiva; permanecen algunas etiquetas inglesas del contenido original.

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
