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
