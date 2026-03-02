(async () => {
    const PACK_ID = "dnd5e.equipment24";

    const OPTS = {
        sortFoldersRoot: true,
        sortEntriesById: true,
        sortNestedById: false
    };

    const lang = (game?.i18n?.lang ?? "en").toLowerCase();
    const pack = game.packs.get(PACK_ID);
    if (!pack) return ui.notifications.error(`No existe el pack: ${PACK_ID}`);

    const COMP_LABEL = pack.metadata?.label ?? pack.title ?? PACK_ID;
    await pack.getIndex({ fields: ["name", "folder"] });

    const sortObj = (obj, locale) =>
        Object.fromEntries(
            Object.entries(obj).sort(([a], [b]) =>
                locale ? a.localeCompare(b, locale) : a.localeCompare(b)
            )
        );

    const getDescriptionHTML = (doc) => {
        if (typeof doc.system?.description?.value === "string") return doc.system.description.value;
        if (typeof doc.system?.description === "string") return doc.system.description;
        return "";
    };

    const extractEffects = (doc) => {
        const arr = doc.effects?.contents ?? doc.effects ?? [];
        if (!arr.length) return undefined;

        const out = {};
        for (const e of arr) {
            const id = e._id ?? e.id;
            if (!id) continue;

            const patch = { name: e.name ?? "" };
            if (typeof e.description === "string" && e.description.trim()) patch.description = e.description;
            out[id] = patch;
        }
        return OPTS.sortNestedById ? sortObj(out) : out;
    };

    // folders raíz
    const foldersTmp = {};
    const packFolders = pack.folders?.contents ?? pack.folders ?? [];
    for (const f of packFolders) if (f?.name) foldersTmp[f.name] = f.name;

    // entries
    const entriesTmp = {};
    const ids = pack.index.map(e => e._id);
    let i = 0;

    for (const id of ids) {
        const doc = await pack.getDocument(id);
        const key = doc.id;
        if (!key) continue;

        const entry = { name: doc.name ?? "" };

        const desc = getDescriptionHTML(doc);
        if (desc) entry.description = desc;

        const effs = extractEffects(doc);
        if (effs) entry.effects = effs;

        entriesTmp[key] = entry;

        i++;
        if (i % 200 === 0) console.log(`[${PACK_ID}] ${i}/${ids.length}`);
    }

    const result = {
        label: COMP_LABEL,
        folders: OPTS.sortFoldersRoot ? sortObj(foldersTmp, lang) : foldersTmp,
        entries: OPTS.sortEntriesById ? sortObj(entriesTmp) : entriesTmp
    };

    // const filename = `${PACK_ID}-${lang}.json`;
    const filename = `${PACK_ID}.json`;
    saveDataToFile(JSON.stringify(result, null, 2), "application/json", filename);
    ui.notifications.info(`Export OK: ${filename} (${Object.keys(result.entries).length} entries)`);
})();