/**
 * actorFullById
 * - Aplica traducción a Actor + embedded Items + Activities + Effects
 * - NO llama a Babele ni hace deep merge (evita recursión)
 * - Traducciones por _id (robusto)
 */
export function actorFullById(actor, translation) {
    if (!translation) return actor;

    // Si viene como JSON completo con entries
    if (translation.entries) {
        translation = translation.entries[actor._id];
        if (!translation) return actor;
    }

    // --- 1) Actor name
    if (typeof translation.name === "string") actor.name = translation.name;

    // --- 2) Biography
    const bio =
        translation?.system?.details?.biography?.value ??
        translation?.biography ??
        translation?.system?.details?.biography; // por si alguien lo deja como string
    if (typeof bio === "string") {
        actor.system = actor.system ?? {};
        actor.system.details = actor.system.details ?? {};
        actor.system.details.biography = actor.system.details.biography ?? {};
        actor.system.details.biography.value = bio;
    }

    // --- 3) Prototype token name (opcional pero útil)
    const tTokenName = translation?.prototypeToken?.name;
    if (typeof tTokenName === "string") {
        actor.prototypeToken = actor.prototypeToken ?? {};
        actor.prototypeToken.name = tTokenName;
    }

    // --- 4) Actor Active Effects por _id
    mergeEffectsByIdOnDocument(actor, translation.effects);

    // --- 5) Embedded items por _id
    mergeItemsByIdOnActor(actor, translation.items);

    // Babele can run after D&D5e has already copied the race type into the
    // prepared actor data. Synchronize that derived copy as well as the item.
    const items = Array.isArray(actor.items) ? actor.items : (actor.items?.contents ?? []);
    const race = items.find(item => item?.type === "race");
    if (race?.system?.type?.subtype && actor.system?.details?.type) {
        const subtype = race.system.type.subtype;
        if (typeof actor.updateSource === "function") {
            actor.updateSource({ "system.details.type.subtype": subtype });
        } else {
            actor.system.details.type.subtype = subtype;
        }
    }

    return actor;
}

/** Traduce effects del documento (Actor o Item) */
function mergeEffectsByIdOnDocument(doc, tEffects) {
    if (!tEffects) return;

    // Normaliza traducciones: { [id]: {name, description...} }
    const tById = normalizeByIdObject(tEffects);

    const effects = Array.isArray(doc.effects) ? doc.effects : (doc.effects?.contents ?? []);
    for (const ef of effects) {
        const id = ef?._id ?? ef?.id;
        if (!id) continue;
        const t = tById[id];
        if (!t) continue;

        if (typeof t.name === "string") ef.name = t.name;

        // description (si lo quieres)
        const desc = t.description?.value ?? t.description;
        if (typeof desc === "string") {
            ef.description = desc; // en AE suele ser ef.description (string)
        }
    }
}

/** Traduce embedded items del actor, + activities/effects internos */
function mergeItemsByIdOnActor(actor, tItems) {
    if (!tItems) return;

    const tById = normalizeByIdObject(tItems);

    const items = Array.isArray(actor.items) ? actor.items : (actor.items?.contents ?? []);
    for (const it of items) {
        const id = it?._id ?? it?.id;
        if (!id) continue;
        const t = tById[id];
        if (!t) continue;

        // name
        if (typeof t.name === "string") it.name = t.name;

        // Character creature subtype is derived by D&D5e from the embedded
        // race item's system.type object. Localizing only the item name leaves
        // the prepared actor subtitle in English (for example, Dragonborn).
        // The SRD species item name is the authoritative localized subtype.
        if (it.type === "race" && typeof t.name === "string") {
            it.system = it.system ?? {};
            it.system.type = it.system.type ?? {};
            const subtype = t.typeSubtype ?? t.name;
            if (typeof it.updateSource === "function") {
                it.updateSource({ "system.type.subtype": subtype });
            } else {
                it.system.type.subtype = subtype;
            }
        }

        // description.value
        const d =
            t?.system?.description?.value ??
            t?.description?.value ??
            t?.description;
        if (typeof d === "string") {
            it.system = it.system ?? {};
            it.system.description = it.system.description ?? {};
            it.system.description.value = d;
        }

        // activities por _id: it.system.activities.{id}.name
        if (t.activities) {
            const tActById = normalizeByIdObject(t.activities);
            const acts = it.system?.activities ?? {};
            for (const [actId, act] of Object.entries(acts)) {
                const ta = tActById[actId];
                if (!ta) continue;
                if (typeof ta.name === "string") acts[actId].name = ta.name;
            }
        }

        // item effects por _id
        mergeEffectsByIdOnDocument(it, t.effects);
    }
}

/** Acepta array u objeto y devuelve siempre { [id]: obj } */
function normalizeByIdObject(input) {
    if (!input) return {};
    if (Array.isArray(input)) {
        const out = {};
        for (const e of input) {
            const id = e?._id ?? e?.id;
            if (id) out[id] = e;
        }
        return out;
    }
    if (typeof input === "object") return input;
    return {};
}
