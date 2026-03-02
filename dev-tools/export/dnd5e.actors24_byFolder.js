(async () => {
    // ===== CONFIG =====
    const PACK_ID = "dnd5e.actors24";
    const OUT_LABEL = "Actores ES";
    const TEMPLATE_MODE = false; // true => vacía strings (plantilla); false => exporta el contenido actual
    const MAKE_ALL_FILE = false; // también genera un dnd5e.actors24.json combinado
    const BASE_NAME = "dnd5e.actors24"; // nombres de ficheros: dnd5e.actors24.<folder>.json
    // ==================

    const pack = game.packs.get(PACK_ID);
    if (!pack) return ui.notifications.error(`No existe el pack: ${PACK_ID}`);

    const actors = await pack.getDocuments();
    ui.notifications.info(`Exportando ${actors.length} actores (por carpeta)...`);

    // Folder map (id -> name)
    const folderById = new Map();
    const packFolders = pack.folders?.contents ?? pack.folders ?? [];
    for (const f of packFolders) {
        const id = f?._id ?? f?.id;
        if (id && f?.name) folderById.set(id, f.name);
    }

    const safeStr = (v) => (typeof v === "string" ? v : "");
    const toArray = (maybe) => {
        if (!maybe) return [];
        if (Array.isArray(maybe)) return maybe;
        if (Array.isArray(maybe.contents)) return maybe.contents;
        if (typeof maybe[Symbol.iterator] === "function") return [...maybe];
        if (typeof maybe === "object") return Object.values(maybe);
        return [];
    };

    // Normaliza nombre para filename
    const slug = (s) =>
        String(s ?? "NoFolder")
            .trim()
            .replace(/[\/\\:*?"<>|]/g, "-")
            .replace(/\s+/g, "_")
            .slice(0, 80) || "NoFolder";

    // Builder de entry traducible
    const buildEntry = (a) => {
        const entry = {
            name: safeStr(a.name),
            biography: safeStr(a.system?.details?.biography?.value),
            effects: {},
            items: {}
        };

        // Actor effects
        for (const ef of toArray(a.effects)) {
            const efId = ef?._id ?? ef?.id;
            if (!efId) continue;
            entry.effects[efId] = { name: safeStr(ef.name) };
            if (TEMPLATE_MODE) entry.effects[efId].name = "";
        }

        // Embedded items
        for (const it of toArray(a.items)) {
            const itemId = it?._id ?? it?.id;
            if (!itemId) continue;

            const tItem = {
                name: safeStr(it.name),
                description: safeStr(it.system?.description?.value),
                activities: {},
                effects: {}
            };

            // Activities (system.activities es objeto por id)
            const acts = it.system?.activities ?? {};
            if (acts && typeof acts === "object") {
                for (const [actId, act] of Object.entries(acts)) {
                    if (!actId) continue;
                    tItem.activities[actId] = { name: safeStr(act?.name) };
                    if (TEMPLATE_MODE) tItem.activities[actId].name = "";
                }
            }

            // Item effects
            for (const ef of toArray(it.effects)) {
                const efId = ef?._id ?? ef?.id;
                if (!efId) continue;
                tItem.effects[efId] = { name: safeStr(ef.name) };
                if (TEMPLATE_MODE) tItem.effects[efId].name = "";
            }

            if (TEMPLATE_MODE) {
                tItem.name = "";
                tItem.description = "";
            }

            entry.items[itemId] = tItem;
        }

        if (TEMPLATE_MODE) {
            entry.name = "";
            entry.biography = "";
        }

        return entry;
    };

    // Agrupar por folderName
    const groups = new Map(); // folderName -> entries obj
    const allEntries = {};

    for (const a of actors) {
        const actorId = a?._id ?? a?.id;
        if (!actorId) continue;

        const folderId = a.folder?._id ?? a.folder?.id ?? a.folder ?? null;
        const folderName = folderId ? (folderById.get(folderId) ?? "NoFolder") : "NoFolder";

        const entry = buildEntry(a);

        if (!groups.has(folderName)) groups.set(folderName, {});
        groups.get(folderName)[actorId] = entry;

        allEntries[actorId] = entry;
    }

    // Descarga múltiples
    const download = async (obj, filename) => {
        const json = JSON.stringify(obj, null, 2);
        const blob = new Blob([json], { type: "application/json;charset=utf-8" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(() => URL.revokeObjectURL(url), 1500);
        // pequeño delay para no bloquear el navegador con muchas descargas
        await new Promise((r) => setTimeout(r, 250));
    };

    // Export por folder
    const foldersMap = {};
    for (const folderName of groups.keys()) foldersMap[folderName] = folderName;

    let n = 0;
    for (const [folderName, entries] of groups.entries()) {
        const out = {
            label: OUT_LABEL,
            folders: { [folderName]: folderName },
            entries
        };
        const fn = `${BASE_NAME}.${slug(folderName)}.json`;
        console.log(`[actors24] descargando ${fn} (${Object.keys(entries).length} entries)`);
        await download(out, fn);
        n++;
    }

    // Export ALL (opcional)
    if (MAKE_ALL_FILE) {
        const outAll = {
            label: OUT_LABEL,
            folders: foldersMap,
            entries: allEntries
        };
        const fnAll = `${BASE_NAME}.json`;
        console.log(`[actors24] descargando ${fnAll} (${Object.keys(allEntries).length} entries)`);
        await download(outAll, fnAll);
    }

    ui.notifications.info(`Export completado: ${n} ficheros por carpeta${MAKE_ALL_FILE ? " + ALL" : ""}`);
})();