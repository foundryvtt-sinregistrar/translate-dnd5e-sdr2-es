# 🇬🇧 D&D 5e SRD 2024 – Spanish Translation (Babele)

![Foundry v13](https://img.shields.io/badge/Foundry-v13-green)
![dnd5e 5.2.x](https://img.shields.io/badge/dnd5e-5.2.x-blue)
![Babele Required](https://img.shields.io/badge/Babele-required-orange)
![SRD 5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

### This module is not affiliated with Wizards of the Coast.
### This module does not include non-SRD content.

This module contains translations of material released under the  
**Creative Commons Attribution 4.0 International License (CC-BY 4.0).**

Dungeons & Dragons SRD 5.2.1 © Wizards of the Coast LLC.

------------------------------------------------------------------------
## 📦 Description

Spanish translation of the official **D&D 5e SRD 5.2.x (2024 rules compatible)**  
compendiums for the Foundry VTT **dnd5e** system.

Implemented using **Babele** with architecture:

Mapping First → Converter Second → Normalization Layer

---

## 📦 Module Contents

Structured translations for:

-   Classes
-   Spells
-   Feats
-   Equipment
-   Monster Features
-   Actors (Monsters, NPCs, Premades)
-   Origins
-   Tables
-   Rules (Journal Entries)

------------------------------------------------------------------------

## 🧠 Technical Architecture

Mapping First → Converter Second → Normalization Layer

### Converters

-   activities
-   mergeEffects
-   advancementById

### Normalization v7

-   Canonical EN → ES glossary
-   Macro protection (@UUID, &Reference, @Embed, \[\[/r ...\]\])
-   Table and heading block protection
-   Semantic Spanish Title Case policy for structured fields

------------------------------------------------------------------------

## 📂 Structure
```
translate-dnd5e-sdr2-es/ 
├── module.json 
├── scripts/ 
├── compendiums/
└── normalization/
```
------------------------------------------------------------------------

## ⚙️ Requirements

-   Foundry VTT v13+
-   dnd5e SRD 5.2.x
-   Babele

------------------------------------------------------------------------

## 🚀 Installation

### Option 1 — Download ZIP

1. Go to the repository **Releases** page.
2. Download the `.zip` for the **latest** release or a **specific** version.
3. Extract to:

```
FoundryVTT/Data/modules/
```

4. Enable the module in Foundry.
5. Enable the translation via Babele.

---

### Option 2 — Install from Foundry (Manifest URL)

1. In Foundry → **Add-on Modules → Install Module → Install from Manifest URL**
2. Paste this URL:

```
https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/module.json
```

3. Install the module.
4. Enable it and activate the translation in Babele.

---

## 📜 License

This project contains only material released under  
**Creative Commons Attribution 4.0 (CC-BY 4.0).**

No proprietary or non-SRD content is included.

---

## 📜 Changelog

See: **CHANGELOG.md**

---

## 👤 Author

foundryvtt-sinregistrar
