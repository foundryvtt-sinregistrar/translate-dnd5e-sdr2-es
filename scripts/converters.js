import { mergeEffects } from "./converters/merge-effects.js";
import { activities } from "./converters/activities.js";
import { advancementById } from "./converters/advancement-by-id.js";
import { journalPagesById } from "./converters/journalPagesById.js";
import { journalEntryFullById } from "./converters/journalEntryFullById.js";
import { actorFullById } from "./converters/actorFullById.js";
import { tableResultsByRange } from "./converters/table-results.js";

Hooks.once("babele.init", (babele) => {
    if (!babele?.registerConverters) return;

    babele.registerConverters({
        activities,
        mergeEffects,
        advancementById,
        journalPagesById,
        journalEntryFullById,
        actorFullById,
        tableResultsByRange
    });

    console.log(
        "[Babele - translate-dnd5e-sdr2-es] Converters registered:",
        Object.keys(babele.converters ?? {})
    );
});