import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { activities } from "../scripts/converters/activities.js";
import { actorFullById } from "../scripts/converters/actorFullById.js";

const source = {
    attack: {
        _id: "attack", name: "Attack", type: "attack",
        description: { value: "Original", chatFlavor: "Attack roll" },
        damage: { parts: [{ formula: "2d6 + @mod", types: ["fire"] }] },
        target: { affects: { count: "1", type: "creature" } },
        consumption: { targets: [{ value: "1" }] }
    },
    other: { _id: "other", name: "Attack" }
};

test("translates only allowed text by ID, preserving source and mechanics", () => {
    const original = structuredClone(source);
    const result = activities(source, {
        attack: { name: "Ataque", description: { value: "<p>[[/r 2d6]]</p>", chatFlavor: "Tirada" },
            _id: "changed", type: "heal", damage: {}, target: {}, consumption: {} },
        Attack: { name: "Must not match by name" },
        missing: { name: "Must not insert" }
    });
    const expected = structuredClone(source);
    expected.attack.name = "Ataque";
    expected.attack.description = { value: "<p>[[/r 2d6]]</p>", chatFlavor: "Tirada" };
    assert.deepEqual(result, expected);
    assert.deepEqual(source, original);
});

test("accepts arrays, empty text and absent translations", () => {
    const result = activities([source.attack], [{ _id: "attack", name: "", description: { value: "", chatFlavor: 12 } }]);
    assert.equal(result[0].name, "");
    assert.equal(result[0].description.value, "");
    assert.equal(result[0].description.chatFlavor, "Attack roll");
    assert.equal(activities(source, null), source);
    assert.deepEqual(activities(source, { attack: { name: null } }), source);
});

test("actor converter uses the same text-only activity translation", () => {
    const actor = { items: [{ _id: "item", system: { activities: structuredClone(source) } }] };
    actorFullById(actor, { items: { item: { activities: { attack: { name: "Ataque", damage: {} } } } } });
    assert.equal(actor.items[0].system.activities.attack.name, "Ataque");
    assert.deepEqual(actor.items[0].system.activities.attack.damage, source.attack.damage);
});

test("all activity-bearing item packs and embedded actor items have mappings", () => {
    const read = name => JSON.parse(readFileSync(new URL(`../compendium/dnd5e.${name}.json`, import.meta.url)));
    for (const name of ["classes24", "equipment24", "monsterfeatures24", "origins24", "spells24", "feats24"]) {
        assert.deepEqual(read(name).mapping.activities, { path: "system.activities", converter: "activities" });
    }
    const items = read("actors24").mapping.items;
    assert.equal(items.converter, "document");
    assert.equal(items.documentType, "Item");
    assert.deepEqual(items.mapping.activities, { path: "system.activities", converter: "activities" });
});
