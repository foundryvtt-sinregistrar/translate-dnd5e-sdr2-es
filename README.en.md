# D&D SRD 5.2.1 — Spanish Translation

**Current version — Foundry v14**

![Foundry v14](https://img.shields.io/badge/Foundry-v14-green)
[![Release v1.14.4](https://img.shields.io/badge/release-v1.14.4-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.14.4)
![dnd5e 6.0.3](https://img.shields.io/badge/dnd5e-6.0.3-blue)
![Babele 2.9.1 required](https://img.shields.io/badge/Babele-2.9.1_required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

**Historical compatibility — Foundry v13**

![Foundry v13](https://img.shields.io/badge/Foundry-v13-green)
[![Release v1.13.4](https://img.shields.io/badge/release-v1.13.4-blue)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/tag/v1.13.4)
![dnd5e 5.2.x](https://img.shields.io/badge/dnd5e-5.2.x-lightgrey)
![Babele Required](https://img.shields.io/badge/Babele-required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

[![Downloads v1.13](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/downloads-v13.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases)
[![Downloads v1.14](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/downloads-v14.json)](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases)

[Español](README.md) | **English**

Translation for Foundry VTT using Babele. Module ID: `translate-dnd5e-sdr2-es`.

## Status

Version: **1.14.4**. Translations of the dnd5e system SRD compendiums, including specific runtime fixes. The historical `sdr2` identifier is preserved. Automated tests do not replace editorial and functional review in Foundry.

See [CHANGELOG.md](CHANGELOG.md).

Checked on September 28, 2026 with Foundry 14.368, dnd5e 6.0.3 and Babele 2.9.1: loaded 2453 documents across 10 compendiums, checked names and explicit text fields, and imported and visually reviewed one sample. This is not an exhaustive linguistic or functional review; some English labels from the original content remain.

## Requirements

Versions declared in the manifest; “—” means that the corresponding limit is not declared.

| Dependency | Minimum | Verified |
|---|---|---|
| Foundry VTT | 14.367 | 14.368 |
| dnd5e | 6.0.0 | 6.0.3 |
| babele | 2.9.1 | 2.9.1 |

Install and enable the dependencies, purchasing official products separately when required.

The official Monster Manual module is an optional manifest recommendation for resolving external references; it is not a required dependency of the SRD translation.

## Installation

In Foundry's Setup screen, open **Add-on Modules → Install Module** and use this manifest:

```text
https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases/latest/download/module.json
```

For manual installation, download `translate-dnd5e-sdr2-es.zip` from [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/releases). With Foundry stopped, extract the `translate-dnd5e-sdr2-es` folder into `Data/modules/`; the manifest must be at `Data/modules/translate-dnd5e-sdr2-es/module.json`.

## Activation

1. Open a dnd5e world.
2. Enable Babele, its dependencies, the required official products and this translation.
3. Select **Spanish** and reload the world.
4. Open a translated compendium to check the result.

Registration is automatic for `es` and its regional variants. Other languages do not enable the Spanish translation.

## Updating

Update through Foundry or replace the folder with the published ZIP while Foundry is stopped. Reload the world. Previously imported copies do not synchronize automatically: review differences before replacing documents with your own changes.

## Included content

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

## Limitations

Text coverage and automated tests do not establish that every gameplay automation works. Observe the limitations listed under Status. Imported copies do not update automatically. New release URLs require a publication containing their assets; until available, use a validated ZIP. Private sources, PDFs, OCR and complete official exports are not distributed.

## Support and contributions

Report problems in [issues](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/issues), including versions, affected compendium/document, steps, expected and observed results, and whether it is an imported copy.

## Development

The [development guide](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/blob/main/DEVELOPER.md) is available in the repository and excluded from the installable ZIP.

## License and credits

See the license and its terms in [LICENSE.md](LICENSE.md). This project incorporates material from the System Reference Document 5.2.1 by Wizards of the Coast LLC, under Creative Commons Attribution 4.0 (CC BY 4.0). Dungeons & Dragons SRD 5.2.1 © Wizards of the Coast LLC. The license file preserves the full attribution.

Unofficial translation, not affiliated with Wizards of the Coast or Foundry VTT. Official product materials belong to their respective owners. Module author: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).
