"""Build the effects translation from the installed 6.0.3 inventory (UTF-8)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT / "tests/effects-source.json").read_text(encoding="utf-8"))
abilities = dict(zip("Strength Dexterity Constitution Intelligence Wisdom Charisma".split(),
                     ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]))
skills = dict(zip(["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival", "Initiative"],
                  ["Acrobacias", "Trato con animales", "Conocimiento arcano", "Atletismo", "Engaño", "Historia", "Perspicacia", "Intimidación", "Investigación", "Medicina", "Naturaleza", "Percepción", "Interpretación", "Persuasión", "Religión", "Juego de manos", "Sigilo", "Supervivencia", "Iniciativa"]))
damage = dict(zip("Acid Bludgeoning Cold Fire Force Lightning Necrotic Piercing Poison Psychic Radiant Slashing Thunder".split(),
                  ["ácido", "contundente", "frío", "fuego", "fuerza", "relámpago", "necrótico", "perforante", "veneno", "psíquico", "radiante", "cortante", "trueno"]))
conditions = dict(zip(["Bleeding", "Blinded", "Burning", "Charmed", "Cursed", "Deafened", "Dehydration", "Diseased", "Exhaustion", "Falling", "Frightened", "Grappled", "Incapacitated", "Invisible", "Malnutrition", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Silenced", "Stunned", "Suffocation", "Surprised", "Transformed", "Unconscious"],
                      ["Sangrado", "Cegado", "En llamas", "Hechizado", "Maldito", "Ensordecido", "Deshidratación", "Enfermo", "Agotamiento", "Caída", "Asustado", "Agarrado", "Incapacitado", "Invisible", "Desnutrición", "Paralizado", "Petrificado", "Envenenado", "Derribado", "Apresado", "Silenciado", "Aturdido", "Asfixia", "Sorprendido", "Transformado", "Inconsciente"]))
names = {**conditions, "Aura of Life": "Aura de vida", "Burrow Speed": "Velocidad de excavación", "Climb Speed": "Velocidad de escalada", "Fly Speed": "Velocidad de vuelo", "Swim Speed": "Velocidad de nado", "Conditions": "Estados", "Condition Immunities": "Inmunidades a estados", "Damage Immunities": "Inmunidades al daño", "Damage Resistances": "Resistencias al daño", "Damage Vulnerabilities": "Vulnerabilidades al daño", "Speeds": "Velocidades", "Spells": "Conjuros"}
for en, es in conditions.items():
    names[f"{en} Immunity"] = f"Inmunidad: {es}"
for en, es in {**damage, "Damage": None}.items():
    for suffix, prefix in [("Immunity", "Inmunidad"), ("Resistance", "Resistencia"), ("Vulnerability", "Vulnerabilidad")]:
        names[f"{en} {suffix}"] = f"{prefix} al daño" + (f" {es}" if es else "")
for suffix, prefix in [("Advantage", "Ventaja"), ("Disadvantage", "Desventaja")]:
    for en, es in skills.items():
        names[f"{en} {suffix}"] = f"{prefix} en {es}"
    for en, es in abilities.items():
        for kind, label in [("Check", "pruebas"), ("Save", "tiradas de salvación"), ("Check & Save", "pruebas y tiradas de salvación")]:
            names[f"{en} {kind} {suffix}"] = f"{prefix} en {label} de {es}"
    for kind, label in [("Check", "pruebas de característica"), ("Save", "tiradas de salvación"), ("Check & Save", "pruebas de característica y tiradas de salvación")]:
        names[f"Ability {kind} {suffix}"] = f"{prefix} en {label}"
    names[f"Skill {suffix}"] = f"{prefix} en habilidades"
descriptions = {
    "phbeffAuraLife00": "<p>Mientras estéis dentro del aura, tú y tus aliados tenéis resistencia al daño necrótico y vuestros máximos de puntos de golpe no pueden reducirse. Si un aliado con 0 puntos de golpe comienza su turno dentro del aura, recupera [[/healing 1 type=healing]]{1 punto de golpe}.</p>",
    "phbeffSilenced00": "<p>Cualquier criatura u objeto que esté completamente dentro de la esfera tiene inmunidad al daño de trueno, y las criaturas tienen el estado Ensordecido mientras estén completamente dentro de ella. Allí es imposible lanzar un conjuro que incluya un componente verbal.</p>"
}
output = {"label": "Efectos activos", "mapping": {"name": "name", "description": "description"}, "folders": {}, "entries": {}}
for entry in sorted(source, key=lambda e: e["name"]):
    name = names[entry["name"]]  # Fail if any source name lacks a translation.
    if entry["key"].startswith("!folders!"):
        output["folders"][entry["name"]] = name
    else:
        translated = {"name": name}
        if entry.get("description"):
            translated["description"] = descriptions[entry["_id"]]
        output["entries"][entry["_id"]] = translated
assert len(output["entries"]) == 173
assert len(output["folders"]) == 15
(ROOT / "compendium/dnd5e.effects.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("173 effects and 15 folders translated; 2 descriptions; no mechanical fields included.")
