# 🇪🇸 D&D 5e SRD 2024 -- Español (Babele)

![Foundry v13](https://img.shields.io/badge/Foundry-v13-green) ![dnd5e
5.2.x](https://img.shields.io/badge/dnd5e-5.2.x-blue) ![Babele
Required](https://img.shields.io/badge/Babele-required-orange) ![SRD
5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

Traducción completa al español de los compendios SRD 5.2.x (2024 rules compatible) del sistema dnd5e para Foundry VTT, implementada mediante Babele y una arquitectura mapping-first + converter-second con normalización semántica avanzada.

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

-   Foundry VTT v13+
-   Sistema dnd5e SRD 5.2.x
-   Babele

------------------------------------------------------------------------

## 🚀 Instalación

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

Contenido basado exclusivamente en SRD 5.2.1.

---

## 📜 Changelog

Consulta: **CHANGELOG.md**

## 👤 Autor

foundryvtt-sinregistrar
