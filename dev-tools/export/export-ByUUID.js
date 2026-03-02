// Pega esto en la consola de Foundry.
// Exporta TODOS los datos del item "Compendium.dnd5e.equipment24.Item.dmgCarrionCrawle"
// en 2 ficheros: JSON completo y JSON "limpio" (sin keys internas ruidosas opcional).
(async () => {
    const UUID = "Compendium.dnd5e.equipment24.Item.dmgCarrionCrawle";

    const OPTS = {
        fileBaseName: "dnd5e.equipment24.Item.dmgCarrionCrawle",
        pretty: 2,

        // Si quieres SOLO el documento completo, deja true/false según prefieras
        exportRaw: true,

        // Un "snapshot" útil (name, system, flags, effects, activities, folder, ownership, etc.)
        exportClean: true,

        // Limpieza opcional de campos muy ruidosos (puedes desactivar)
        strip: {
            _stats: true,
            ownership: false,
            sort: false
        }
    };

    const notify = (m) => ui?.notifications?.info?.(m) ?? console.log(m);

    const deepClone = (x) => foundry?.utils?.deepClone
        ? foundry.utils.deepClone(x)
        : JSON.parse(JSON.stringify(x));

    const stripKeysRecursive = (obj) => {
        if (obj === null || obj === undefined) return obj;
        if (Array.isArray(obj)) return obj.map(stripKeysRecursive);
        if (typeof obj !== "object") return obj;

        const out = {};
        for (const [k, v] of Object.entries(obj)) {
            if (OPTS.strip._stats && k === "_stats") continue;
            if (OPTS.strip.ownership && k === "ownership") continue;
            if (OPTS.strip.sort && k === "sort") continue;
            out[k] = stripKeysRecursive(v);
        }
        return out;
    };

    // 1) Resolve UUID -> Document
    const doc = await fromUuid(UUID);
    if (!doc) return ui.notifications.error(`No se pudo resolver el UUID: ${UUID}`);

    // 2) RAW (documento completo serializado)
    //    En Foundry VTT 11-13: doc.toObject() es el snapshot completo (incluye system, flags, effects, etc.)
    const raw = deepClone(doc.toObject ? doc.toObject() : doc);

    // 3) CLEAN (útil para debugging humano)
    const clean = {
        uuid: UUID,
        id: doc.id,
        name: doc.name,
        type: doc.type,
        img: doc.img,
        folder: doc.folder?.name ?? doc.folder ?? null,
        flags: deepClone(doc.flags ?? {}),
        system: deepClone(doc.system ?? {}),
        activities: deepClone(doc.system?.activities ?? {}),
        effects: (() => {
            const arr = doc.effects?.contents ?? doc.effects ?? [];
            return arr.map(e => {
                const eo = e.toObject ? e.toObject() : deepClone(e);
                return eo;
            });
        })()
    };

    const rawOut = stripKeysRecursive(raw);
    const cleanOut = stripKeysRecursive(clean);

    // 4) Descargar
    if (OPTS.exportRaw) {
        saveDataToFile(
            JSON.stringify(rawOut, null, OPTS.pretty),
            "application/json",
            `${OPTS.fileBaseName}.raw.json`
        );
    }

    if (OPTS.exportClean) {
        saveDataToFile(
            JSON.stringify(cleanOut, null, OPTS.pretty),
            "application/json",
            `${OPTS.fileBaseName}.clean.json`
        );
    }

    notify(`OK: exportado ${doc.name} (${UUID})`);
})();