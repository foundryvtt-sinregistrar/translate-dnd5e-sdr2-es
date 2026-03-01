/**
 * Babele registration for this translation module.
 * - Registers for both "es" and "es-ES" style language codes.
 */
Hooks.on("init", () => {
  const babele = game?.babele;
  if (!babele) return;

  const current = game.i18n?.lang ?? "es";
  const base = current.split("-")[0];
  const langs = Array.from(new Set([current, base]));

  for (const lang of langs) {
    try {
      babele.register({
          module: "translate-dnd5e-sdr2-es",
          lang,
          dir: "compendium",
          compendium: {
              "dnd5e.content24": {
                  label: "Reglas",
                  path: "dnd5e.content24.json",
                  converter: "journalEntryFullById"
              },
              "dnd5e.origins24": {
                  label: "Orígenes",
                  path: "dnd5e.origins24.json"
                  // aquí normalmente usarías mapping dentro del JSON, o converter si lo necesitas
              },
              "dnd5e.classes24": {
                  label: "Clases",
                  path: "dnd5e.classes24.json"
              },
              "dnd5e.feats24": {
                  label: "Dotes",
                  path: "dnd5e.feats24.json"
              },
              "dnd5e.spells24": {
                  label: "Conjuros",
                  path: "dnd5e.spells24.json"
              },
              "dnd5e.tables24": {
                  label: "Tablas",
                  path: "dnd5e.tables24.json"
                  // aquí normalmente NO hace falta mapping
              },
              "dnd5e.monsterfeatures24": {
                  label: "Rasgos de monstruos",
                  path: "dnd5e.monsterfeatures24.json"
              },
              "dnd5e.actors24": {
                  label: "Actores",
                  path: "dnd5e.actors24.json",
                  converter: "actorFullById"
              }
          }
      });
        console.log(`[Babele - translate-dnd5e-sdr2-es] Registered for lang="${lang}" (dir=compendium)`);
    } catch (err) {
        console.error(`[Babele - translate-dnd5e-sdr2-es] Failed registering for lang="${lang}"`, err);
    }
  }
});
