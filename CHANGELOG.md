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

[Unreleased]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/compare/v1.13.2...HEAD
[1.13.2]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.2
[1.13.1]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.1
[1.13.0]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.0
