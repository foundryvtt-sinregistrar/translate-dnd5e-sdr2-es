# 🇬🇧 D&D 5e SRD 2024 -- Spanish Translation (Babele)

![Foundry v13](https://img.shields.io/badge/Foundry-v13-green) ![dnd5e
5.2.x](https://img.shields.io/badge/dnd5e-5.2.x-blue) ![Babele
Required](https://img.shields.io/badge/Babele-required-orange) ![SRD
5.2.1](https://img.shields.io/badge/SRD-5.2.1-lightgrey)

Full Spanish translation of SRD 5.2.x (2024 rules compatible)
compendiums for the dnd5e system in Foundry VTT.

------------------------------------------------------------------------

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

1.  Copy into FoundryVTT/Data/modules/
2.  Enable module
3.  Activate translation in Babele

------------------------------------------------------------------------

## 📜 License

Based exclusively on SRD 5.2.1 content.

Generated on 2026-03-02 10:20:40 UTC
