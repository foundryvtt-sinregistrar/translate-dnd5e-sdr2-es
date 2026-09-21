/** Translate activity text by ID, without merging mechanical data. */
export function activities(source, translation) {
    if (!source || typeof source !== "object" || !translation || typeof translation !== "object") return source;

    const byId = Array.isArray(translation)
        ? Object.fromEntries(translation.filter(t => t && (t._id ?? t.id)).map(t => [t._id ?? t.id, t]))
        : translation;
    const deepClone = globalThis.foundry?.utils?.deepClone ?? structuredClone;
    const out = deepClone(source);

    for (const [key, activity] of Object.entries(out)) {
        if (!activity || typeof activity !== "object") continue;
        const id = activity._id ?? activity.id ?? (Array.isArray(out) ? undefined : key);
        if (!id || !Object.hasOwn(byId, id)) continue;
        const patch = byId[id];
        if (!patch || typeof patch !== "object") continue;

        if (typeof patch.name === "string") activity.name = patch.name;
        // D&D5e 6 stores both text fields inside description.
        for (const field of ["value", "chatFlavor"]) {
            if (typeof patch.description?.[field] !== "string") continue;
            activity.description ??= {};
            activity.description[field] = patch.description[field];
        }
    }
    return out;
}
