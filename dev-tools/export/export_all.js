(async () => {
    const packs = [
        "dnd5e.actors24",
        "dnd5e.classes24",
        "dnd5e.content24",
        "dnd5e.equipment24",
        "dnd5e.feats24",
        "dnd5e.monsterfeatures24",
        "dnd5e.origins24",
        "dnd5e.spells24",
        "dnd5e.tables24"
    ];

    for (const packName of packs) {
        const pack = game.packs.get(packName);
        const docs = await pack.getDocuments();

        const data = docs.map(d => d.toObject());

        const fileName = `${packName}.json`;
        saveDataToFile(
            JSON.stringify(data, null, 2),
            "application/json",
            fileName
        );
    }
})();