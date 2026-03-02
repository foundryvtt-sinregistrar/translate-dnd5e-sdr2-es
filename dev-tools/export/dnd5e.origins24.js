(async () => {
    const PACK_ID = "dnd5e.origins24";

    const OPTS = {
        sortFoldersRoot: true,   // ordena folders por nombre (root)
        sortEntriesById: true,   // ordena entries por id
        sortNestedById: false    // ordena sub-bloques (activities/effects/advancement) por id
    };

    const lang = (game?.i18n?.lang ?? "en").toLowerCase();
    const pack = game.packs.get(PACK_ID);
    if (!pack) return ui.notifications.error(`No existe el pack: ${PACK_ID}`);

    // Label real del compendio
    const COMP_LABEL = pack.metadata?.label ?? pack.title ?? PACK_ID;

    // Index para acelerar
    await pack.getIndex({ fields: ["name", "folder"] });

    // ---------- helpers ----------
    const sortObj = (obj, locale) =>
        Object.fromEntries(
            Object.entries(obj).sort(([a], [b]) =>
                locale ? a.localeCompare(b, locale) : a.localeCompare(b)
            )
        );

    const safeStr = (v) => (typeof v === "string" ? v : "");

    const getDescriptionHTML = (doc) => {
        // Items (Origins suele ser Item) => system.description.value
        const v = doc.system?.description?.value ?? doc.system?.description;
        return safeStr(v);
    };

    // Activities: a veces es objeto keyed, a veces colección
    const extractActivities = (doc) => {
        const acts = doc.system?.activities;

        // Caso A: objeto keyed
        if (acts && typeof acts === "object" && !Array.isArray(acts) && !acts.contents) {
            const out = {};
            for (const [id, a] of Object.entries(acts)) {
                if (!id) continue;
                out[id] = { name: safeStr(a?.name) };
            }
            return OPTS.sortNestedById ? sortObj(out) : out;
        }

        // Caso B: colección
        const arr = acts?.contents ?? [];
        if (!Array.isArray(arr) || !arr.length) return {};

        const out = {};
        for (const a of arr) {
            const id = a?._id ?? a?.id;
            if (!id) continue;
            out[id] = { name: safeStr(a?.name) };
        }
        return OPTS.sortNestedById ? sortObj(out) : out;
    };

    const extractEffects = (doc) => {
        const arr = doc.effects?.contents ?? doc.effects ?? [];
        if (!Array.isArray(arr) || !arr.length) return {};

        const out = {};
        for (const e of arr) {
            const id = e?._id ?? e?.id;
            if (!id) continue;

            const patch = { name: safeStr(e?.name) };
            if (typeof e?.description === "string" && e.description.trim()) patch.description = e.description;
            out[id] = patch;
        }
        return OPTS.sortNestedById ? sortObj(out) : out;
    };

    const extractAdvancement = (doc) => {
        const adv = doc.system?.advancement;
        if (!Array.isArray(adv) || !adv.length) return {};

        const out = {};
        for (const a of adv) {
            const id = a?._id ?? a?.id;
            if (!id) continue;

            out[id] = {
                title: safeStr(a?.title),
                hint: safeStr(a?.hint)
            };
        }
        return OPTS.sortNestedById ? sortObj(out) : out;
    };

    // ---------- folders raíz ----------
    const foldersTmp = {};
    const packFolders = pack.folders?.contents ?? pack.folders ?? [];
    for (const f of packFolders) {
        if (f?.name) foldersTmp[f.name] = f.name;
    }

    // ---------- export ----------
    const entriesTmp = {};
    const ids = pack.index.map((e) => e._id);

    let i = 0;
    for (const id of ids) {
        const doc = await pack.getDocument(id);

        const key = doc.id ?? doc._id;
        if (!key) continue;

        const entry = {
            name: safeStr(doc.name),
            description: "",
            activities: {},
            effects: {},
            advancement: {}
        };

        const desc = getDescriptionHTML(doc);
        if (desc) entry.description = desc;

        entry.activities = extractActivities(doc);
        entry.effects = extractEffects(doc);
        entry.advancement = extractAdvancement(doc);

        entriesTmp[key] = entry;

        i++;
        if (i % 200 === 0) console.log(`[${PACK_ID}] ${i}/${ids.length}`);
    }

    const result = {
        label: COMP_LABEL,
        folders: OPTS.sortFoldersRoot ? sortObj(foldersTmp, lang) : foldersTmp,
        entries: OPTS.sortEntriesById ? sortObj(entriesTmp) : entriesTmp
    };

    const filename = `${PACK_ID}.json`;
    saveDataToFile(JSON.stringify(result, null, 2), "application/json", filename);
    ui.notifications.info(`Export OK: ${filename} (${Object.keys(result.entries).length} entries)`);
})();