"""Verifica la separación sin interpretar el contenido matemático.

Uso: python verificar_solucionarios.py [1|2|3|4]
Solo requiere la biblioteca estándar de Python y no modifica archivos.
"""
from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
EXPECTED = {1: (16, 226), 2: (16, 160), 3: (18, 198), 4: (16, 99)}
EXERCISE = re.compile(r"\\begin\{ejercicio\}.*?\\end\{ejercicio\}", re.S)
SOLUTION = re.compile(r"\\begin\{solucion\}.*?\\end\{solucion\}", re.S)
read = lambda path: path.read_text(encoding="utf-8")


def labels(text):
    return re.findall(r"\\label\{([^}]+)\}", text)


def references(text):
    return set(re.findall(r"\\(?:ref|pageref|eqref)\*?\{([^}]+)\}", text))


def verify(number):
    volume = ROOT / f"volumen-{number:02}"
    chapter_count, exercise_count = EXPECTED[number]
    chapters = sorted((volume / "capitulos").glob("*.tex"))
    assert [p.stem for p in chapters] == [f"{n:02}" for n in range(1, chapter_count + 1)]
    sources = [read(path) for path in chapters]
    notes_body = "\n".join(sources)
    solution_body = read(volume / "ejercicios-soluciones.tex")
    solution_chapters = re.split(r"(?m)(?=^\\chapter\{)", solution_body)[1:]
    assert len(solution_chapters) == chapter_count
    assert not SOLUTION.search(notes_body), "Los apuntes aún contienen soluciones"
    assert len(EXERCISE.findall(notes_body)) == exercise_count
    assert len(SOLUTION.findall(solution_body)) == exercise_count
    for path, source, solution_chapter in zip(chapters, sources, solution_chapters):
        statements = EXERCISE.findall(source)
        assert statements == EXERCISE.findall(solution_chapter), f"Enunciados distintos: {path}"
        assert len(statements) == len(SOLUTION.findall(solution_chapter)), path
    shared = "\n".join(read(volume / name) for name in
                       ("preambulo.tex", "referencias.tex"))
    notes = notes_body + "\n" + shared + "\n" + "\n".join(
        read(volume / name) for name in
        ("main.tex", "partes.tex", "cobertura.tex", "notacion.tex"))
    presentation = volume / "presentacion.tex"
    if presentation.exists():
        notes += "\n" + read(presentation)
    solutions = solution_body + "\n" + shared
    note_labels, sol_labels = labels(notes), labels(solutions)
    for document, document_labels in (("apuntes", note_labels), ("solucionario", sol_labels)):
        duplicate = [key for key, count in Counter(document_labels).items() if count > 1]
        assert not duplicate, (volume.name, document, "etiquetas duplicadas", duplicate)
    assert not (references(notes) - set(note_labels)), references(notes) - set(note_labels)
    assert not (references(solutions) - set(note_labels) - set(sol_labels)), (
        references(solutions) - set(note_labels) - set(sol_labels))
    for text in (notes, solutions):
        citations = {key for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text)
                     for key in group.split(",")}
        bibliography = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
        assert citations <= bibliography, citations - bibliography
    for source in sources + solution_chapters:
        assert Counter(re.findall(r"\\begin\{([^}]+)\}", source)) == Counter(
            re.findall(r"\\end\{([^}]+)\}", source)), "Entornos desequilibrados"
    style = read(volume / "estilo-esfm.tex")
    assert style.index(r"\ifsolucionario") < style.index(r"\tcolorboxenvironment{ejercicio}")
    assert r"\solucionariofalse" in read(volume / "main.tex")
    assert r"\solucionariotrue" in read(volume / "solucionario.tex")
    print(f"{volume.name}: {chapter_count} capítulos; {exercise_count} enunciados idénticos; "
          f"{exercise_count} soluciones solo en el solucionario; referencias y citas completas")


if __name__ == "__main__":
    for number in ([int(sys.argv[1])] if len(sys.argv) > 1 else EXPECTED):
        verify(number)
