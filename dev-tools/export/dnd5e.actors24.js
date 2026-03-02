(async () => {
    const PACK_ID = "dnd5e.actors24";
    const pack = game.packs.get(PACK_ID);
    if (!pack) {
        ui.notifications.error(`No existe el pack: ${PACK_ID}`);
        return;
    }

    // Cargar docs (robusto incluso si pack.index no trae todo)
    const docs = await pack.getDocuments();

    // Carpetas del compendio (si existen)
    const folders = {};
    const folderById = new Map();
    const packFolders = pack.folders?.contents ?? pack.folders ?? [];
    for (const f of packFolders) {
        folderById.set(f._id ?? f.id, f);
        if (f?.name) folders[f.name] = f.name; // EN->EN (tú lo traduces luego)
    }

    // Label real del compendio
    const COMP_LABEL = pack.metadata?.label ?? pack.title ?? PACK_ID;

    const out = {
        label: COMP_LABEL,
        folders,
        entries: {}
    };

    const safeGet = (obj, path, fallback = undefined) => {
        try {
            return path.split(".").reduce((a, k) => (a?.[k]), obj) ?? fallback;
        } catch (_) {
            return fallback;
        }
    };

    for (const a of docs) {
        const actorId = a._id ?? a.id;
        if (!actorId) continue;

        const entry = {
            name: a.name ?? "",
            biography: safeGet(a, "system.details.biography.value", "") ?? "",
            folder: null, // nombre de carpeta (si hay)
            effects: {},
            items: {}
        };

        // Folder -> nombre (si hay)
        const folderId = a.folder?._id ?? a.folder?.id ?? a.folder ?? null;
        if (folderId && folderById.has(folderId)) {
            entry.folder = folderById.get(folderId).name ?? null;
            if (entry.folder && !(entry.folder in out.folders)) out.folders[entry.folder] = entry.folder;
        }

        // Actor effects
        const aEffects = a.effects?.contents ?? a.effects ?? [];
        for (const ef of aEffects) {
            const efId = ef._id ?? ef.id;
            if (!efId) continue;
            entry.effects[efId] = { name: ef.name ?? "" };
        }

        // Embedded items
        const items = a.items?.contents ?? a.items ?? [];
        for (const it of items) {
            const itemId = it._id ?? it.id;
            if (!itemId) continue;

            const tItem = {
                name: it.name ?? "",
                description: safeGet(it, "system.description.value", "") ?? "",
                activities: {},
                effects: {}
            };

            // Activities (obj keyed)
            const acts = safeGet(it, "system.activities", {}) ?? {};
            if (acts && typeof acts === "object") {
                for (const [actId, act] of Object.entries(acts)) {
                    if (!actId) continue;
                    // Algunos activities tienen name vacío en el pack; lo exportamos tal cual.
                    tItem.activities[actId] = { name: act?.name ?? "" };
                }
            }

            // Item effects
            const iEffects = it.effects?.contents ?? it.effects ?? [];
            for (const ef of iEffects) {
                const efId = ef._id ?? ef.id;
                if (!efId) continue;
                tItem.effects[efId] = { name: ef.name ?? "" };
            }

            entry.items[itemId] = tItem;
        }

        out.entries[actorId] = entry;
    }

    const filename = "dnd5e.actors24.json";
    saveDataToFile(JSON.stringify(out, null, 2), "application/json", filename);
    ui.notifications.info(`Export OK: ${filename} (${Object.keys(out.entries).length} entries)`);
})();
