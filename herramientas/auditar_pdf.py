"""Huella editorial de un PDF y comparación renderizada de todas sus páginas.

Requiere pypdf, pypdfium2 y Pillow. No usa fechas ni identificadores internos
para decidir si dos PDF son editorialmente equivalentes.
"""
from pathlib import Path
import hashlib
import json
import re
from functools import wraps
from threading import RLock

from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import ImageChops

# PDFium no permite llamadas concurrentes desde varios hilos de un proceso.
_PDFIUM_LOCK = RLock()


def serialized(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        with _PDFIUM_LOCK:
            return function(*args, **kwargs)
    return wrapper


def digest(data):
    return hashlib.sha256(data).hexdigest()


@serialized
def measure(path):
    path = Path(path)
    reader = PdfReader(path)
    page_ids = {page.indirect_reference.idnum: i for i, page in enumerate(reader.pages)}

    def destination(value):
        if isinstance(value, (str, int, float)) or value is None:
            return value
        if isinstance(value, (list, tuple)):
            return [({'page': page_ids[v.idnum]} if hasattr(v, 'idnum') and v.idnum in page_ids
                     else str(v)) for v in value]
        return str(value)

    def outline(items):
        result = []
        for item in items:
            if isinstance(item, list):
                result.append(outline(item))
            else:
                result.append({'title': item.title,
                               'page': reader.get_destination_page_number(item),
                               'destination': destination(item.dest_array[1:])})
        return result

    texts, annotations = [], []
    for page in reader.pages:
        texts.append(page.extract_text() or '')
        links = []
        for reference in page.get('/Annots', []):
            item = reference.get_object()
            if item.get('/Subtype') != '/Link':
                continue
            link = {'rect': [str(n) for n in item['/Rect']]}
            if '/Dest' in item:
                link['destination'] = destination(item['/Dest'])
            if '/A' in item:
                action = item['/A'].get_object()
                link['action'] = {key: destination(action.get(key))
                                  for key in ('/S', '/D', '/F', '/URI') if key in action}
            links.append(link)
        annotations.append(links)
    named = {name: {'page': reader.get_destination_page_number(dest),
                    'destination': destination(dest.dest_array[1:])}
             for name, dest in reader.named_destinations.items()}
    metadata = {key: str(value) for key, value in (reader.metadata or {}).items()
                if key not in ('/CreationDate', '/ModDate')}
    render = pdfium.PdfDocument(str(path))
    pixels = []
    for index in range(len(render)):
        page = render[index]
        bitmap = page.render(scale=1).to_pil().convert('RGB')
        pixels.append({'size': list(bitmap.size), 'sha256': digest(bitmap.tobytes())})
        page.close()
    render.close()
    return {'sha256': digest(path.read_bytes()), 'pages': len(reader.pages),
            'text': texts, 'metadata': metadata, 'outline': outline(reader.outline),
            'destinations': named, 'links': annotations, 'render': pixels}


@serialized
def compare(reference_pdf, candidate_pdf, differences_dir):
    reference_pdf = Path(reference_pdf)
    cache = reference_pdf.with_suffix('.json')
    before = json.loads(cache.read_text(encoding='utf-8')) if cache.exists() else measure(reference_pdf)
    assert before['sha256'] == digest(reference_pdf.read_bytes()), 'La referencia cambió'
    after = measure(candidate_pdf)
    checks = {key: before[key] == after[key] for key in
              ('pages', 'text', 'metadata', 'outline', 'destinations', 'links', 'render')}
    changed = [i for i, (a, b) in enumerate(zip(before['render'], after['render'])) if a != b]
    if changed:
        folder = Path(differences_dir)
        folder.mkdir(parents=True, exist_ok=True)
        left, right = pdfium.PdfDocument(str(reference_pdf)), pdfium.PdfDocument(str(candidate_pdf))
        for index in changed:
            a = left[index].render(scale=1).to_pil().convert('RGB')
            b = right[index].render(scale=1).to_pil().convert('RGB')
            a.save(folder / f'{index+1:03}-antes.png')
            b.save(folder / f'{index+1:03}-despues.png')
            if a.size == b.size:
                ImageChops.difference(a, b).save(folder / f'{index+1:03}-diferencia.png')
        left.close()
        right.close()
    return {'checks': checks, 'changed_pages': [i+1 for i in changed],
            'reference_sha256': before['sha256'], 'candidate_sha256': after['sha256'],
            'pages': after['pages']}


def log_summary(path):
    text = Path(path).read_text(encoding='utf-8', errors='replace')
    patterns = {
        'errors': r'^!', 'undefined': r'undefined', 'duplicate_labels': r'multiply defined',
        'missing_glyphs': r'Missing character', 'missing_fonts': r'font.*not found',
        'overfull': r'Overfull', 'underfull': r'Underfull',
        'remote_page_warning': r'Invalid page number',
    }
    return {key: len(re.findall(pattern, text, re.M | re.I)) for key, pattern in patterns.items()}


def save(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
