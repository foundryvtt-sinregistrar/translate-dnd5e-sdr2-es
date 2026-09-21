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

for (const language of ["es", "es-ES", "en", "en-US", "fr"]) {
    test(`converters and sheet fixes are inactive outside Spanish: ${language}`, async () => {
        const hooks = new Map();
        let ready = false;
        globalThis.Hooks = { once(event, fn) { hooks.set(event, fn); } };
        globalThis.game = { settings: { get() {
            if (!ready) throw new Error("Settings not registered");
            return language;
        } } };
        try {
            await import(`../scripts/converters.js?lang=${language}`);
            let converters;
            hooks.get("babele.init")({ registerConverters(value) { converters = value; } });
            assert.equal(converters, undefined);
            ready = true;
            hooks.get("setup")();
            assert.equal(typeof converters?.activities, language.startsWith("es") ? "function" : "undefined");
            const renderHooks = [];
            runInNewContext(readFileSync(new URL("../scripts/runtime-fixes.js", import.meta.url), "utf8"), {
                game: globalThis.game,
                Hooks: { once(event, fn) { assert.equal(event, "setup"); fn(); },
                    on(event) { renderHooks.push(event); } }
            });
            assert.equal(renderHooks.length, language.startsWith("es") ? 4 : 0);
        } finally {
            delete globalThis.Hooks;
            delete globalThis.game;
        }
    });
}
