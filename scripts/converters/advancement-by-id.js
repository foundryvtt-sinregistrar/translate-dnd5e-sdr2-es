export function advancementById(source, translation) {
  if (!source || typeof source !== "object" || !translation || typeof translation !== "object") return source;

  const deepClone = globalThis.foundry?.utils?.deepClone ?? structuredClone;
  const out = deepClone(source);
  // DnD5e used arrays for advancements in earlier versions and now stores
  // them in an object keyed by advancement ID.
  const advancements = Array.isArray(out) ? out : Object.values(out);
  const translations = Array.isArray(translation)
    ? Object.fromEntries(translation
      .filter(adv => adv && typeof adv === "object" && (adv._id ?? adv.id))
      .map(adv => [adv._id ?? adv.id, adv]))
    : translation;

  for (const adv of advancements) {
    const id = adv?._id ?? adv?.id;
    if (!id) continue;
    const patch = translations[id];
    if (patch && typeof patch === "object") {
      // Translation must never replace levels, grants, choices or other mechanics.
      if (typeof patch.title === "string") {
        // DnD5e 6 renamed title to name; preserve compatibility with older data.
        adv["name" in adv ? "name" : "title"] = patch.title;
      }
      if (typeof patch.hint === "string") adv.hint = patch.hint;
    }
  }
  return out;
}
