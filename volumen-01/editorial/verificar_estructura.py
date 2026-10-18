"""Comprueba cobertura, etiquetas y referencias del volumen integrado."""
from collections import Counter
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [7, 7, 9, 6, 9, 8, 7, 7, 1, 10, 6, 3, 8, 6, 6, 5,
            7, 7, 7, 7, 8, 6, 4, 7, 0, 8, 5, 4, 8, 6, 7, 10]
chapters = sorted((ROOT / "capitulos").glob("*.tex"))
assert [p.stem for p in chapters] == [f"{i:02}" for i in range(1, 17)]
body = "\n".join(p.read_text() for p in chapters)
files = [ROOT / name for name in ("main.tex", "partes.tex", "cobertura.tex",
                                  "notacion.tex", "referencias.tex")]
text = body + "\n" + "\n".join(p.read_text() for p in files)
labels = re.findall(r"\\label\{([^}]+)\}", text)
duplicates = [key for key, n in Counter(labels).items() if n > 1]
assert not duplicates, duplicates
refs = set(re.findall(r"\\(?:ref|pageref|eqref)\{([^}]+)\}", text))
missing = sorted(refs - set(labels))
assert not missing, missing
expected_labels = {f"ej:lectura-{n}-{k}" for n, count in enumerate(EXPECTED, 1)
                   for k in range(1, count + 1)}
actual_labels = {key for key in labels if key.startswith("ej:lectura-")}
assert actual_labels == expected_labels, (expected_labels - actual_labels,
                                         actual_labels - expected_labels)
assert body.count(r"\begin{ejercicio}") == sum(EXPECTED) == 206
assert body.count(r"\begin{solucion}") == 206
assert body.count(r"\chapter{") == 16
assert (ROOT / "partes.tex").read_text().count(r"\parte{") == 6
for n in range(1, 33):
    assert f"lectura:{n:02}" in labels and f"chap:{n:02}" in labels
for path in chapters:
    source = path.read_text()
    assert Counter(re.findall(r"\\begin\{([^}]+)\}", source)) == Counter(
        re.findall(r"\\end\{([^}]+)\}", source)), path.name
citations = set()
for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text):
    citations.update(group.split(","))
bibkeys = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
assert citations <= bibkeys, citations - bibkeys
result = {
    "partes": 6, "capitulos": 16, "lecturas_originales": 32,
    "ejercicios": 206, "soluciones": 206,
    "entradas_indice": body.count(r"\index{"),
    "etiquetas_duplicadas": duplicates,
    "referencias_internas_faltantes": missing,
    "citas": sorted(citations),
    "palabras_aproximadas_fuentes_latex": len(text.split()),
    "ejercicios_por_capitulo": {
        p.stem: p.read_text().count(r"\begin{ejercicio}") for p in chapters
    },
}
(ROOT / "editorial/verificacion-estructura.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
