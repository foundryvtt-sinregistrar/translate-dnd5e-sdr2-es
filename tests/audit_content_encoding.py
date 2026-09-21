"""Repair confirmed encoding damage and report possible untranslated prose."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "compendium/dnd5e.content24.json"
source = FILE.read_text(encoding="utf-8")
data = json.loads(source)
words = """Más agitación bárbaro bárbaros cólera conexión emoción espíritu está están expresión líderes más maraña protección también ánimo Creación aún alegría artística bárdica caídos canción clásicas cobró coreografías demás dramáticos héroes hazañas interpretación laúd música melodías monólogos público pérdida podrías románticas sombrías través""".split()
pages = data["entries"]["phbAppendixClass"]["pages"]
for pid in ("phbbrbBarbarian0", "phbbrdBard000000"):
    old = pages[pid]["text"]
    new = old
    for word in sorted(words, key=len, reverse=True):
        damaged = "".join(c if ord(c) < 128 else "?" for c in word)
        new = re.sub(r"(?<!\w)" + re.escape(damaged) + r"(?!\w)", lambda _: word, new)
    new = re.sub(r"(?<=[> ])\?(?=[A-ZÁÉÍÓÚ])", "¿", new)
    assert re.findall(r"<[^>]+>", old) == re.findall(r"<[^>]+>", new)
    if new != old:
        encoded = json.dumps(old, ensure_ascii=False)
        assert source.count(encoded) == 1
        source = source.replace(encoded, json.dumps(new, ensure_ascii=False), 1)
        pages[pid]["text"] = new
assert json.loads(source) == data
assert not re.search(r"\w\?\w", source)
assert "\ufffd" not in source
FILE.write_text(source, encoding="utf-8", newline="\n")

rows = []
def scan(value, path):
    if isinstance(value, dict):
        for key, child in value.items():
            if key not in ("key", "_id", "id"):
                scan(child, path + [key])
    elif isinstance(value, str):
        text = re.sub(r"<[^>]*>|@(?:UUID|Embed)\[[^\]]*\]|&(?:amp;)?Reference\[[^\]]*\]", " ", value)
        text = re.sub(r"\s+", " ", text).strip()
        hits = re.findall(r"\b(?:the|with|from|their|this|that|these|which|your|when|are|have|each)\b", text, re.I)
        if len(hits) >= 3:
            rows.append({"path": ".".join(path), "english_markers": len(hits), "excerpt": text[:350]})
scan(data, [])
report = ROOT / "tests/content-english-audit.json"
report.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Encoding repaired and validated. {len(rows)} fields flagged for English review.")
