/**
 * Aplica traducciones de JournalEntry:
 * - entry.name
 * - pages[pageId].name
 * - pages[pageId].text.content
 * - pages[pageId].description.value
 * - pages[pageId].description.subclass
 * - pages[pageId].subclassHeader
 *
 * Traducción viene en translations[entry._id]
 */
export function journalPagesById(entity, translation) {
    if (!translation) return entity;

    // Nombre de la entry
    if (typeof translation.name === "string") entity.name = translation.name;

    const tPages = normalizeById(translation.pages);
    const pages = normalizePages(entity.pages);

    for (const page of pages) {
        const pageId = page?._id ?? page?.id;
        const tPage = pageId ? tPages[pageId] : undefined;
        if (!tPage) continue;

        // Nombre de página
        if (typeof tPage.name === "string") page.name = tPage.name;

        // 1) text.content (Foundry)
        if (tPage.text?.content !== undefined) {
            // Foundry v13: page.text es objeto; page.text.content es string
            if (page.text && typeof page.text === "object") {
                page.text.content = tPage.text.content;
            }
            // dnd5e a veces guarda también en system.text
            if (page.system?.text && typeof page.system.text === "object" && "content" in page.system.text) {
                page.system.text.content = tPage.text.content;
            }
        }

        // 2) description.value (dnd5e-style)
        if (tPage.description?.value !== undefined) {
            // si existe system.description.value, úsalo
            if (page.system?.description && typeof page.system.description === "object" && "value" in page.system.description) {
                page.system.description.value = tPage.description.value;
            } else {
                // fallback: crea la ruta mínima
                page.system = page.system ?? {};
                page.system.description = page.system.description ?? {};
                page.system.description.value = tPage.description.value;
            }
        }

        // 3) description.subclass
        if (tPage.description?.subclass !== undefined) {
            page.system = page.system ?? {};
            page.system.description = page.system.description ?? {};
            page.system.description.subclass = tPage.description.subclass;
        }

        // 4) subclassHeader
        if (tPage.subclassHeader !== undefined) {
            page.system = page.system ?? {};
            page.system.subclassHeader = tPage.subclassHeader;
            // algunos esquemas lo guardan en description/subclase; no lo fuerzo más
        }
    }

    return entity;
}

function normalizePages(value) {
    if (!value) return [];
    if (typeof value[Symbol.iterator] === "function") return value;
    if (Array.isArray(value?.contents)) return value.contents;
    if (Array.isArray(value)) return value;
    return typeof value === "object" ? Object.values(value) : [];
}

function normalizeById(value) {
    if (Array.isArray(value)) {
        return Object.fromEntries(value
            .filter(page => page && typeof page === "object" && (page._id ?? page.id))
            .map(page => [page._id ?? page.id, page]));
    }
    return value && typeof value === "object" ? value : {};
}
