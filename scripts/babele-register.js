/**
 * Babele registration for this translation module.
 * - Registers only for Spanish ("es" and variants such as "es-ES").
 */
Hooks.once("babele.init", (babele) => {
  if (!babele) return;

  // Foundry 14 has not registered core.language during babele.init.
  // setup runs after core settings exist and before Babele loads its session
  // in ready. Keep converter registration in babele.init.
  Hooks.once("setup", () => registerSpanishCompendiums(babele));
});

function registerSpanishCompendiums(babele) {
  // Match the language Babele uses for its translation session.
  const current = game.settings.get("core", "language");
  if (typeof current !== "string") return;

  const base = current.split("-")[0].toLowerCase();
  if (base !== "es") return;

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
              "dnd5e.equipment24": {
                  label: "Equipo",
                  path: "dnd5e.equipment24.json"
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
}
