(async () => {
    const PACK_ID = "dnd5e.content24";

    const OPTS = {
        sortFoldersRoot: true,
        sortEntriesById: true,
        sortNestedById: true // pages por id
    };

    const TEMPLATE_MODE = false; // true => text="" (plantilla)

    const pack = game.packs.get(PACK_ID);
    if (!pack) return ui.notifications.error(`No existe el pack: ${PACK_ID}`);
    if (pack.documentName !== "JournalEntry") {
        return ui.notifications.error(`El pack ${PACK_ID} no es JournalEntry (es ${pack.documentName}).`);
    }

    const lang = (game?.i18n?.lang ?? "en").toLowerCase();
    const COMP_LABEL = pack.metadata?.label ?? pack.title ?? PACK_ID;

    await pack.getIndex({ fields: ["name", "folder"] });

    // ---------- helpers ----------
    const sortObj = (obj, locale) =>
        Object.fromEntries(
            Object.entries(obj).sort(([a], [b]) =>
                locale ? a.localeCompare(b, locale) : a.localeCompare(b)
            )
        );

    const safeStr = (v) => (typeof v === "string" ? v : "");

    function pick(obj, keys) {
        const out = {};
        for (const k of keys) {
            const v = obj?.[k];
            if (v !== undefined && v !== null && v !== "") out[k] = v;
        }
        return out;
    }

    const EXTRA_KEYS = ["description", "subclassHeader", "subclass", "special", "hint"];

    function pageToExport(p) {
        const t = {
            name: safeStr(p?.name),
            key: safeStr(p?.name) // como tu ejemplo
        };

        // Texto: en content24 normalmente es page.type === "text" y p.text.content
        if (p?.type === "text") {
            const content = safeStr(p?.text?.content);
            t.text = TEMPLATE_MODE ? "" : content;
        }

        // Extras directos en page
        Object.assign(t, pick(p, EXTRA_KEYS));

        // Extras en system (sin inventar)
        if (p?.system) {
            const sysExtra = pick(p.system, EXTRA_KEYS);

            // Caso: system.text es string
            if (typeof p.system.text === "string") {
                t.textString = TEMPLATE_MODE ? "" : p.system.text;
            }

            // Caso: system.text.content
            if (typeof p.system.text === "object" && p.system.text?.content !== undefined) {
                t.systemText = { content: TEMPLATE_MODE ? "" : safeStr(p.system.text.content) };
            }

            Object.assign(t, sysExtra);
        }

        return t;
    }

    // ---------- folders raíz ----------
    // Intentamos sacar folders del propio pack; si no hay, quedan vacías
    const foldersTmp = {};
    const packFolders = pack.folders?.contents ?? pack.folders ?? [];
    for (const f of packFolders) {
        if (f?.name) foldersTmp[f.name] = f.name;
    }

    // ---------- entries ----------
    const entriesTmp = {};
    const ids = pack.index.map((e) => e._id);
    let i = 0;

    for (const id of ids) {
        const doc = await pack.getDocument(id);
        if (!doc) continue;

        const key = doc.id ?? doc._id; // ej: dmgDmsToolbox000
        if (!key) continue;

        // pages: colección iterable
        const pagesArr = doc.pages ? [...doc.pages] : [];
        const pagesTmp = {};

        for (const p of pagesArr) {
            const pid = p?._id ?? p?.id;
            if (!pid) continue;
            pagesTmp[pid] = pageToExport(p);
        }

        const pages = OPTS.sortNestedById ? sortObj(pagesTmp) : pagesTmp;

        entriesTmp[key] = {
            name: safeStr(doc.name),
            pages
        };

        i++;
        if (i % 25 === 0) console.log(`[${PACK_ID}] ${i}/${ids.length}`);
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