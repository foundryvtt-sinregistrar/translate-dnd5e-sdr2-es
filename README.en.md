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

### 🔹 Option 1 — Download ZIP

1. Go to the **Releases** section of the repository.
2. Download the `.zip` file for the **latest version** or any **specific version** you want.
3. Extract into:

   FoundryVTT/Data/modules/

4. Enable the module in Foundry.
5. Activate the translation in Babele.

---

### 🔹 Option 2 — Install directly from Foundry (Manifest URL)

1. In Foundry, go to **Add-on Modules → Install Module → Install from Manifest URL**.
2. Use the following URL:

   https://raw.githubusercontent.com/foundryvtt-sinregistrar/translate-dnd5e-sdr2-es/main/module.json

3. Install the module.
4. Enable it and activate the translation via Babele.

------------------------------------------------------------------------

## 📜 License

Based exclusively on SRD 5.2.1 content.

Generated on 2026-03-02 10:20:40 UTC
