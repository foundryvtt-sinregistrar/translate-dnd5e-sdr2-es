import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync, existsSync } from "node:fs";
import { advancementById } from "../scripts/converters/advancement-by-id.js";

const structuredURL = new URL("../../babele/script/converter/structured-data-converter.js", import.meta.url);
const mappingURL = new URL("../../babele/script/mapping/field-mapping.js", import.meta.url);

const pack = name => JSON.parse(readFileSync(new URL(`../compendium/dnd5e.${name}.json`, import.meta.url)));

test("advancements translate text by ID while preserving mechanics and original data", () => {
    const source = [{ _id: "one", title: "Ability Score", hint: "Choose", level: 4,
        configuration: { points: 2 }, value: { chosen: ["str"] } }];
    const original = structuredClone(source);
    const result = advancementById(source, { one: { title: "Característica", hint: "",
        level: 20, configuration: { points: 99 }, value: {} }, missing: { title: "Extra" } });
    assert.deepEqual(result, [{ ...original[0], title: "Característica", hint: "" }]);
    assert.deepEqual(source, original);
});

test("Babele integration: actor biography mapping applies the actual translation field", {
    skip: !existsSync(mappingURL)
}, async () => {
    const { FieldMapping } = await import(mappingURL.href);
    const data = { system: { details: { biography: { value: "Original" } } } };
    const entry = Object.values(pack("actors24").entries).find(e => e.biography);
    const mapping = new FieldMapping("biography", pack("actors24").mapping.biography);
    assert.deepEqual(mapping.map(data, entry), { system: { details: { biography: { value: entry.biography } } } });
});

test("Babele integration: structured converter applies journal text and preserves unmapped fields", {
    skip: !existsSync(structuredURL)
}, async () => {
    const { StructuredDataConverter } = await import(structuredURL.href);
    // These page payloads contain flat string fields; emulate Foundry's non-mutating merge.
    globalThis.foundry = { utils: { mergeObject: (source, patch) => ({ ...structuredClone(source), ...patch }) } };
    try {
        const mappings = pack("content24").mapping.pages.mapping;
        for (const field of ["systemText", "description"]) {
            const params = mappings[field];
            const source = Object.fromEntries(Object.keys(params.mapping).map(k => [k, "Original"]));
            source.untouched = 42;
            const translation = Object.fromEntries(Object.keys(params.mapping).map(k => [k, "Texto traducido"]));
            translation.untouched = 99;
            const result = new StructuredDataConverter().translate({ value: source, translation,
                params, field, path: params.path, runtime: {} });
            assert.deepEqual(result, { ...translation, untouched: 42 });
            assert.equal(source.untouched, 42);
            assert.equal(source[Object.keys(params.mapping)[0]], "Original");
        }
    } finally { delete globalThis.foundry; }
});
