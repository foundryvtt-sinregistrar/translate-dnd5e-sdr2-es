export function advancementById(source, translation) {
  if (!Array.isArray(source) || !translation || typeof translation !== "object") return source;

  const deepClone = globalThis.foundry?.utils?.deepClone ?? structuredClone;
  const out = source.map(a => deepClone(a));

  for (const adv of out) {
    const id = adv?._id ?? adv?.id;
    if (!id) continue;
    const patch = translation[id];
    if (patch && typeof patch === "object") {
      // Translation must never replace levels, grants, choices or other mechanics.
      for (const field of ["title", "hint"]) {
        if (typeof patch[field] === "string") adv[field] = patch[field];
      }
    }
  }
  return out;
}
