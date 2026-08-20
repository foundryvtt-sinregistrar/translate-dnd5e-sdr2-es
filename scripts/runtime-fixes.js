/** Runtime localization fixes for D&D5e prepared values outside Babele data. */

function localizeCharacterSpeciesSubtype(_application, element) {
    const root = element instanceof HTMLElement ? element : element?.[0];
    if (!root) return;

    // D&D5e renders details.type.subtype as raw text, after deriving it from
    // the source race item. Babele localizes the item name but cannot reliably
    // replace this prepared copy because the system rebuilds it afterwards.
    const subtype = root.querySelector(".pill-lg.texture.type .subtitle");
    const species = root.querySelector(".pill-lg.texture.race .title");
    const localizedName = species?.textContent?.trim();
    if (subtype && localizedName) subtype.textContent = localizedName;
}

// ApplicationV2 uses the concrete application-class render hook. Keep the
// generic hooks for alternate sheets and compatibility with nearby releases.
Hooks.on("renderCharacterActorSheet", localizeCharacterSpeciesSubtype);
Hooks.on("renderActorSheetV2", localizeCharacterSpeciesSubtype);
Hooks.on("renderApplicationV2", localizeCharacterSpeciesSubtype);
Hooks.on("renderActorSheet", localizeCharacterSpeciesSubtype);
