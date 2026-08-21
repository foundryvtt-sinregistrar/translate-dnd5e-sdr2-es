# Changelog

All notable changes to this project will be documented in this file.
The format is based on **Keep a Changelog**, and this project follows a custom versioning scheme:

**MAJOR.FOUNDRY.PATCH**

- **MAJOR** → Breaking structural changes
- **FOUNDRY** → Foundry VTT major compatibility version
- **PATCH** → Improvements, fixes, and incremental updates

---

## [Unreleased]

### Added
- —

### Changed
- —

### Fixed
- —

---

## [1.14.1] - 2026-08-21

### Changed
- Actualizado el parche de mantenimiento de la versión compatible con Foundry VTT 14.
- Ajustada la versión del módulo a `1.14.1`.

### Fixed
- Correcciones menores posteriores a la publicación de `1.14.0`.

---

## [1.14.0] - 2026-08-21

### Changed
- Actualizada la compatibilidad principal del módulo a Foundry VTT 14.
- Actualizada la convención de versión a `1.14.0`.

---

## [1.13.5] - 2026-08-20

### Added
- Official Spanish material components for all 188 SRD 5.2.1 spells that use them.
- Runtime localization for prepared character species subtitles in Foundry VTT 14.

### Changed
- Verified compatibility with Foundry VTT 14.363, D&D 5e 5.3.3, and Babele 2.9.1.
- Improved visible terminology, actor biographies, embedded content, effects, and activity labels using the official Spanish SRD as the reference.

### Fixed
- Restored missing internal rule links, conditions, target lookups, spellcasting lists, and duplicated actor descriptions.
- Corrected residual English text in actors, equipment, monster features, origins, and spells.
- Localized the prepared `Dragonborn` subtype shown on premade character sheets as `Dracónido`.

---

## [1.13.4] - 2026-03-31

### Added
- Spanish vs English consolidation pass (*integración fina v1*) producing a module-ready package per compendium.
- Optional recommendation for `dnd-monster-manual` to resolve remaining external embeds referenced from `dnd5e.content24`.
- Release workflow improvements:
    - Releases are generated as **Draft** by default to allow validation before publication.
    - Automated module packaging using `dev-tools/buildScripts/build_release.py` (git archive–based build).
    - Release asset uploads `dist/translate-dnd5e-sdr2-es.zip`.
    - Explicit `permissions: contents: write` to prevent GitHub Actions permission failures.

### Changed
- Final compendium files consolidated to best-available integrated outputs:
    - `dnd5e.content24.json` ← `dnd5e.content24.es.integracion-fina.v1.json`
        - ES base: `dnd5e.content24.es.mini-correctiva.v2.1.no-key-translation.json`
        - reference overlay: `dnd5e.content24.references.mini-correctiva.v6.external-mm.json`
        - reference paths applied: **135**
        - mismatches: **0**
        - note: `key` values have **not** been translated (by design).
        - note: retains **15** intentional external embeds to `dnd-monster-manual.content` (optional dependency).
    - `dnd5e.actors24.json` ← `dnd5e.actors24.es.integracion-fina.v1.json`
        - ES base: `dnd5e.actors24.es.mini-correctiva.v2.json`
        - overlay references: `dnd5e.actors24.references.mini-correctiva.v2.json`
        - reference paths applied: **28**
        - mismatches: **0**
    - `dnd5e.classes24.json` ← `dnd5e.classes24.es.integracion-fina.v1.json`
        - ES base: `dnd5e.classes24.es.mini-correctiva.v2.json`
        - references overlay: `dnd5e.classes24.references.mini-correctiva.v1.json`
        - reference paths applied: **1**
        - mismatches: **0**
    - `dnd5e.equipment24.json` ← `dnd5e.equipment24.es.mini-correctiva.v2.json`
    - `dnd5e.feats24.json` ← `dnd5e.feats24.es.mini-correctiva.v2.json`
    - `dnd5e.monsterfeatures24.json` ← `dnd5e.monsterfeatures24.es.mini-correctiva.v2.json`
    - `dnd5e.origins24.json` ← `dnd5e.origins24.es.mini-correctiva.v2.json`
    - `dnd5e.spells24.json` ← `dnd5e.spells24.es.mini-correctiva.v2.json`
    - `dnd5e.tables24.json` ← `dnd5e.tables24.es.mini-correctiva.v2.json`
- Babele support:
    - Added/confirmed registration for `dnd5e.equipment24` in the Babele register script (module integration support).

### Fixed
- Final integrity checks after consolidation:
    - `content24`: changes to `key` fields: **0**
    - `content24`: external embeds in `dnd-monster-manual.content`: **15**
    - `actors24`: obsolete references to `phbmobZombie0000`: **0**
    - `actors24`: obsolete references to `phbmobSkeleton00`: **0**
    - `classes24`: obsolete reference to `mh3akteBDiLegqFK`: **0**

### Notes
- `content24` is integrated with the strongest reference fixes available, but retains **15 deliberate external embeds**
  to `dnd-monster-manual.content`; these are intentional and covered via an optional recommendation.

---

## [1.13.3] - 2026-03-02

### Added
- Added Version Links to CHANGELOG.md.

### Changed
- Updated version comparison references to point to v1.13

---
## [1.13.2] - 2026-03-02

### Added
- Added CC-BY 4.0 compliant `LICENSE`.
- Added explicit marketplace legal disclaimers.
- Added non-affiliation statement with Wizards of the Coast.
- Added explicit confirmation that no non-SRD content is included.

### Changed
- Cleaned and normalized `README.md` and `README.en.md` (UTF-8 encoding fix).
- Marketplace-ready documentation structure.
- Updated module version to 1.13.3.

### Fixed
- Fixed UTF-8 encoding issues causing corrupted characters in README.
---

## [1.13.1] - 2026-03-02
### Added
- Added module i18n support via `lang/en.json` and `lang/es.json`.
- Added `languages` section to `module.json` so Foundry can load translations.

### Changed
- `title` and `description` now use localization keys (`TDSRD2.module.name`, `TDSRD2.module.description`).
---

## [1.13.0] - 2026-03-02

### Compatibility
- Foundry VTT v13.x
- dnd5e SRD 5.2.x (2024 rules compatible)

### Added
- Dual installation methods (ZIP + Manifest URL).
- Bilingual README (ES / EN).
- Developer documentation.
- Normalization core v7 structural policy (semantic Spanish Title Case).

### Improved
- Stabilized *mapping-first + converter-second* architecture.
- Full macro preservation (`@UUID`, `&Reference`, `@Embed`, inline rolls).
- Protection of `<table>` blocks and heading elements during normalization.

### Technical
- Converters: `activities`, `mergeEffects`, `advancementById`.
- Forward-compatible structure for future dnd5e system updates.

---

## Version Links

[Unreleased]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/compare/v1.14.1...HEAD
[1.14.1]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.14.1
[1.14.0]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.14.0
[1.13.5]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.5
