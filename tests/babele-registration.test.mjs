import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { runInNewContext } from "node:vm";

const source = readFileSync(new URL("../scripts/babele-register.js", import.meta.url), "utf8");

for (const [language, expected] of [
    ["es", ["es"]], ["es-ES", ["es-ES", "es"]], ["es-MX", ["es-MX", "es"]],
    ["en", []], ["fr", []], [undefined, []]
]) {
    test(`registration waits for core settings, then uses configured language ${language}`, () => {
        const hooks = new Map();
        let settingsReady = false;
        const calls = [];
        runInNewContext(source, {
            Hooks: { once(event, fn) { hooks.set(event, fn); } },
            game: { i18n: { lang: "en" }, settings: { get(scope, key) {
                if (!settingsReady) throw new Error('"core.language" is not a registered game setting');
                assert.equal(scope, "core"); assert.equal(key, "language"); return language;
            } } },
            console: { log() {}, error(error) { throw error; } }
        });
        hooks.get("babele.init")({ register(config) { calls.push(config.lang); } });
        assert.deepEqual(calls, []);
        assert.equal(typeof hooks.get("setup"), "function");
        settingsReady = true;
        hooks.get("setup")();
        assert.deepEqual(calls, expected);
    });
}

test("activity converter is registered through the Babele bootstrap instance", async () => {
    let callback;
    globalThis.Hooks = { once(event, fn) { assert.equal(event, "babele.init"); callback = fn; } };
    try {
        await import("../scripts/converters.js");
        let converters;
        callback({ registerConverters(value) { converters = value; } });
        assert.equal(typeof converters.activities, "function");
        assert.equal(typeof converters.actorFullById, "function");
    } finally {
        delete globalThis.Hooks;
    }
});
