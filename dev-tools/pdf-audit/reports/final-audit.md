# Final SRD translation review

The Spanish SRD 5.2.1 translation was reviewed against the English exports and
the Spanish and English reference PDFs in `dev-tools/sourcesToChatGPT`.

## Automated result

- All nine compendium files have the same top-level entry counts as their
  English exports.
- All module, language, and compendium JSON files parse successfully.
- No likely English prose or mojibake remains in visible translated fields.
- Foundry inline-command and reference differences were reviewed; they are
  localized redirects, deliberate additions, or repairs of defective source
  markup rather than accidental translation loss.
- The normalization, duplicate-repair, and embedded-translation checks report
  no pending changes.

Run the complete non-destructive validation with:

```powershell
python dev-tools/pdf-audit/validate_release.py
```

Exact English/Spanish matches that remain are proper names, abbreviations, or
terms that are written identically in both languages. Foundry-token differences
remaining in the detailed report are intentional localized links, redirected
embeds, additional rule references, or corrections to source defects.

## Foundry smoke test

The module is ready for an interactive smoke test from this Data directory:

1. Start Foundry and open a disposable D&D 5e world with Babele enabled.
2. Enable **D&D 5e SRD 2024 Spanish Translation (Babele)** and reload the world.
3. Open one document from each translated compendium and confirm its name,
   description, activities, effects, and embedded links are in Spanish.
4. Test representative actors, spells, equipment, class features, and monster
   features; roll at least one attack, save, damage, and healing activity.
5. Confirm rule references and compendium embeds open the intended documents and
   that the browser console contains no converter or Babele errors.

The manifest currently declares Foundry VTT 13 (verified 13.351), D&D 5e 5.2.x,
and Babele 2.7.5. The local host directory is for Foundry 14.363-B, so a successful
manual test there must not be interpreted as declared v14 compatibility until
the whole smoke test passes and the manifest is deliberately updated.
