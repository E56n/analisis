"""Lee las fuentes efectivas usando el directorio real de ejecución de TeX."""
from pathlib import Path
import re
import os

INPUT = re.compile(r'\\input\{([^{}]+)\}')


def expand(path, *, directory=None, stack=()):
    path = Path(path).resolve()
    directory = Path(directory or path.parent).resolve()
    if path in stack:
        raise ValueError(f'Inclusión circular: {path}')
    text = path.read_text(encoding='utf-8')

    def include(match):
        name = match.group(1)
        if '\\' in name or '#' in name:
            raise ValueError(f'Inclusión dinámica no soportada en {path}: {name}')
        target = directory / name
        if not target.suffix:
            target = target.with_suffix('.tex')
        return expand(target, directory=directory, stack=(*stack, path))

    return INPUT.sub(include, text)


def check_case(path):
    """Comprueba las grafías reales; no equivale a compilar en Linux."""
    # resolve() en Windows puede corregir las mayusculas y ocultar el error.
    path = Path(os.path.abspath(path))
    current = Path(path.anchor)
    for component in path.parts[1:]:
        names = {entry.name for entry in current.iterdir()}
        if component not in names:
            raise AssertionError(f'Mayúsculas distintas en {current / component}')
        current /= component


def inputs(path, directory):
    path = Path(os.path.abspath(path))
    check_case(path)
    text = path.read_text(encoding='utf-8')
    result = {path}
    for match in INPUT.finditer(text):
        target = Path(directory) / match.group(1)
        if not target.suffix:
            target = target.with_suffix('.tex')
        result.update(inputs(target, directory))
    return result
