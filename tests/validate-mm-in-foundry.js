// Run in the Foundry browser console after reloading. Read-only diagnostics.
(async () => {
    if (!game.modules.get("dnd-monster-manual")?.active) {
        throw new Error("Monster Manual must be active.");
    }
    const response = await fetch("modules/translate-dnd5e-sdr2-es/compendium/dnd5e.content24.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`Translation fetch failed: ${response.status}`);
    const text = await response.text();
    JSON.parse(text);
    const uuids = [...new Set(text.match(/Compendium\.dnd-monster-manual\.[A-Za-z0-9_.-]+/g) ?? [])];
    const results = [];
    for (const uuid of uuids) {
        try {
            const page = await fromUuid(uuid);
            results.push({ uuid, name: page?.name, resolved: !!page,
                hasText: !!page?.text?.content?.trim() });
        } catch (error) {
            results.push({ uuid, resolved: false, error: error.message });
        }
    }
    console.table(results);
    console.log("MM integration", { version: game.modules.get("dnd-monster-manual").version,
        checked: results.length, passed: results.filter(r => r.resolved && r.hasText).length });
    return results;
})();
