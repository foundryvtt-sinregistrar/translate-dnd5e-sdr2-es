/**
 * Traduce resultados de RollTable por rango.
 *
 * Foundry VTT 14 + dnd5e 6.x
 *
 * Texto simple:
 *   -> name
 *
 * Texto enriquecido / HTML:
 *   -> description
 *
 * Evita:
 *   - duplicados name + description
 *   - HTML escapado dentro de name
 */
export function tableResultsByRange(source, translation) {
    if (!source || !translation || typeof translation !== "object") {
        return source;
    }

    const deepClone =
        globalThis.foundry?.utils?.deepClone ??
        globalThis.structuredClone;

    let results;

    if (Array.isArray(source)) {
        results = source;
    } else if (Array.isArray(source?.contents)) {
        results = source.contents;
    } else if (typeof source?.[Symbol.iterator] === "function") {
        results = Array.from(source);
    } else {
        return source;
    }

    return results.map(result => {
        const out =
            typeof result?.toObject === "function"
                ? result.toObject()
                : deepClone(result);

        const range = out?.range ?? result?.range;

        if (!Array.isArray(range) || range.length < 2) {
            return out;
        }

        const key = `${range[0]}-${range[1]}`;
        const translated = translation[key];

        if (typeof translated !== "string") {
            return out;
        }

        /*
         * Determina si el contenido necesita ser tratado
         * como contenido enriquecido.
         */
        const rich =
            /<\/?[a-z][\s\S]*?>/i.test(translated) ||
            translated.includes("[[") ||
            translated.includes("@UUID[") ||
            translated.includes("&Reference[");

        if (rich) {
            /*
             * Contenido enriquecido:
             * se muestra únicamente en description.
             *
             * name debe quedar vacío para:
             * - no mostrar HTML escapado
             * - no duplicar el resultado
             */
            if ("name" in out) {
                out.name = "";
            }

            if ("description" in out) {
                out.description = translated;
            }

            /*
             * Compatibilidad legacy únicamente si
             * TableResult todavía posee text.
             */
            if (
                "text" in out &&
                !("description" in out)
            ) {
                out.text = translated;
            }
        } else {
            /*
             * Texto simple:
             * se muestra únicamente como name.
             */
            if ("name" in out) {
                out.name = translated;
            }

            if ("description" in out) {
                out.description = "";
            }

            if (
                "text" in out &&
                !("name" in out)
            ) {
                out.text = translated;
            }
        }

        return out;
    });
}