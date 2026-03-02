(async () => {
    const PACK_ID = "dnd5e.tables24";

    const OPTS = {
        sortFoldersRoot: true,   // ordena folders por nombre
        sortEntriesById: true,   // ordena entries por id
        sortResultsByRange: false // ordena results por rango "1-50", "51-51", etc.
    };

    const lang = (game?.i18n?.lang ?? "en").toLowerCase();
    const pack = game.packs.get(PACK_ID);
    if (!pack) return ui.notifications.error(`No existe el pack: ${PACK_ID}`);

    const COMP_LABEL = pack.metadata?.label ?? pack.title ?? PACK_ID;

    await pack.getIndex({ fields: ["name", "folder"] });

    // ---------- helpers ----------
    const safeStr = (v) => (typeof v === "string" ? v : "");

    const sortObjAlpha = (obj, locale) =>
        Object.fromEntries(
            Object.entries(obj).sort(([a], [b]) =>
                locale ? a.localeCompare(b, locale) : a.localeCompare(b)
            )
        );

    // Para keys tipo "1-50" "100-100"
    const parseRangeKey = (k) => {
        const m = String(k).match(/^(\d+)\s*-\s*(\d+)$/);
        if (!m) return { a: Number.POSITIVE_INFINITY, b: Number.POSITIVE_INFINITY, raw: String(k) };
        return { a: parseInt(m[1], 10), b: parseInt(m[2], 10), raw: String(k) };
    };

    const sortResultsRanges = (resultsObj) => {
        const entries = Object.entries(resultsObj ?? {});
        entries.sort(([ka], [kb]) => {
            const ra = parseRangeKey(ka);
            const rb = parseRangeKey(kb);
            if (ra.a !== rb.a) return ra.a - rb.a;
            if (ra.b !== rb.b) return ra.b - rb.b;
            return ra.raw.localeCompare(rb.raw);
        });
        return Object.fromEntries(entries);
    };

    // Extrae resultados desde TableResult (RollTable)
    const extractResults = (doc) => {
        const out = {};

        // RollTable: doc.results suele ser una colección
        const arr =
            doc.results?.contents ??
            doc.results ??
            doc.data?.results?.contents ??
            [];

        if (!Array.isArray(arr) || !arr.length) return {};

        for (const r of arr) {
            // En rolltables de Foundry, el rango suele venir como range: [min,max]
            const range = r?.range;
            let key = "";

            if (Array.isArray(range) && range.length === 2) {
                key = `${range[0]}-${range[1]}`;
            } else if (typeof r?.range === "string") {
                key = r.range;
            } else if (r?.min != null && r?.max != null) {
                key = `${r.min}-${r.max}`;
            } else {
                // fallback estable: si no hay rango claro
                key = safeStr(r?._id ?? r?.id ?? "");
                if (!key) continue;
            }

            // Texto: RollTableResult puede usar text o documentCollection/documentId.
            // Tu export usa strings que ya incluyen @UUID cuando aplica, así que priorizamos r.text.
            const text = safeStr(r?.text);

            out[key] = text;
        }

        return OPTS.sortResultsByRange ? sortResultsRanges(out) : out;
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
            results: extractResults(doc)
        };

        entriesTmp[key] = entry;

        i++;
        if (i % 200 === 0) console.log(`[${PACK_ID}] ${i}/${ids.length}`);
    }

    const result = {
        label: COMP_LABEL,
        folders: OPTS.sortFoldersRoot ? sortObjAlpha(foldersTmp, lang) : foldersTmp,
        entries: OPTS.sortEntriesById ? sortObjAlpha(entriesTmp) : entriesTmp
    };

    const filename = `${PACK_ID}.json`;
    saveDataToFile(JSON.stringify(result, null, 2), "application/json", filename);
    ui.notifications.info(`Export OK: ${filename} (${Object.keys(result.entries).length} entries)`);
})();