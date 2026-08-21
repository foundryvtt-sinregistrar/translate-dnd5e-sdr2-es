# 🇪🇸 D&D 5e SRD 2024 -- Español (Babele)

![Foundry v13](https://img.shields.io/badge/Foundry-v13-green)
[![Release v1.13.4](https://img.shields.io/badge/release-v1.13.4-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.4)
![dnd5e 5.2.x](https://img.shields.io/badge/dnd5e-5.2.x-lightgrey)
![Babele Required](https://img.shields.io/badge/Babele-required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

![Foundry v14](https://img.shields.io/badge/Foundry-v14-green)
[![Release v1.14.1](https://img.shields.io/badge/release-v1.14.1-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.14.1)
![dnd5e 5.3.x](https://img.shields.io/badge/dnd5e-5.3.x-blue)
![Babele Required](https://img.shields.io/badge/Babele-required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

[![Downloads v1.13](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/downloads-v13.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases)
[![Downloads v1.14](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/downloads-v14.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases)

### Este módulo no está afiliado a Wizards of the Coast.
### Este módulo no incluye contenido fuera del SRD.

Este módulo contiene traducciones de material publicado bajo la licencia **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**.

Dungeons & Dragons SRD 5.2.1 © Wizards of the Coast LLC.

---

## 📦 Descripción

Traducción al español de los compendios oficiales del **SRD 5.2.x (compatible con reglas 2024)** del sistema **dnd5e** para Foundry VTT.

Implementado mediante **Babele** con arquitectura:

Mapping First → Converter Second → Normalization Layer

------------------------------------------------------------------------

## 📦 Contenido del Módulo

Este módulo proporciona traducciones estructuradas para los siguientes compendios del sistema dnd5e:

| Compendio |   Estado   |
|----------|:----------:|
| Clases   |     ✅      |
| Conjuros    |     ✅      |
| Dotes    |     ✅      |
| Equipo    |     ✅      |
| Rasgos de monstruos    |     ✅      |
| Actores (Monstruos, PNJ, Premades)    |     ✅      |
| Orígenes    |     ✅      |
| Tablas    |     ✅      |
| Reglas (Journal Entries)    |     ✅      |

------------------------------------------------------------------------

## 🧠 Arquitectura Técnica

Mapping First → Converter Second → Normalization Layer

### Convertidores

-   activities
-   mergeEffects
-   advancementById

### Normalización v7

-   Glosario EN→ES canónico
-   Protección de macros (@UUID, &Reference, @Embed, \[\[/r ...\]\])
-   Protección de
    ```{=html}
    <table>
    ```
    y `<h1-6>`{=html}
-   Title Case semántico en campos estructurales

------------------------------------------------------------------------

## 📂 Estructura
```
translate-dnd5e-sdr2-es/ 
├── module.json
├── scripts/
├── compendiums/
└── normalization/
```

------------------------------------------------------------------------

## ⚙️ Requisitos

-   Foundry VTT v13 o v14
-   Sistema dnd5e SRD 5.2.x
-   Babele

------------------------------------------------------------------------

## 🚀 Instalación

Descarga la versión correspondiente a tu versión de Foundry VTT:

- Foundry VTT v13: versión `1.13.4` o posterior compatible con v13.
- Foundry VTT v14: versión `1.14.0` o posterior

### 🔹 Opción 1 — Descargar ZIP

1. Ir a la sección **Releases** del repositorio.
2. Descargar el fichero `.zip` de la **última versión** o de la **versión deseada**.
3. Descomprimir en:

   FoundryVTT/Data/modules/

4. Activar el módulo desde Foundry.
5. Activar la traducción desde Babele.

---

### 🔹 Opción 2 — Instalación directa desde Foundry (URL)

1. En Foundry, ir a **Add-on Modules → Install Module → Install from Manifest URL**.
2. Introducir la siguiente URL:

   https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/module.json

4. Instalar el módulo.
4. Activarlo y habilitar la traducción desde Babele.

------------------------------------------------------------------------

## 📜 Licencia

Este proyecto contiene exclusivamente material publicado bajo **Creative Commons Attribution 4.0 (CC-BY 4.0)**.

No incluye contenido propietario fuera del SRD.

---

## 📜 Changelog

Consulta: **CHANGELOG.md**

## 👤 Autor

foundryvtt-sinregistrar
