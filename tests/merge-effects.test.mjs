import assert from "node:assert/strict";
import { test } from "node:test";
import { mergeEffects } from "../scripts/converters/merge-effects.js";

test("effects accept legacy arrays and ID-indexed objects without changing mechanics", () => {
    const source = {
        effectOne: { _id: "effectOne", name: "Blessed", description: "Original", changes: [{ key: "x", value: "1" }] },
        effectTwo: { _id: "effectTwo", name: "Unchanged", disabled: true }
    };
    const original = structuredClone(source);
    const result = mergeEffects(source, [{ _id: "effectOne", name: "Bendecido", description: "Traducido", changes: [] }]);

    assert.deepEqual(result, {
        effectOne: { ...source.effectOne, name: "Bendecido", description: "Traducido" },
        effectTwo: source.effectTwo
    });
    assert.deepEqual(source, original);
});

test("effects preserve an array container and ignore non-text patches", () => {
    const source = [{ _id: "effectOne", name: "Blessed", description: "Original", changes: [{ key: "x" }] }];
    const result = mergeEffects(source, { effectOne: { name: 1, description: { value: "No" } } });

    assert.ok(Array.isArray(result));
    assert.deepEqual(result, source);
    assert.notEqual(result, source);
});
