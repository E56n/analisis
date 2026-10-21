"""Pruebas de aceptacion en copias desechables, sin modificar los originales.

python herramientas/probar_compilacion.py --referencia RUTA --salida INFORME.json
Requiere las herramientas de compilacion y las bibliotecas de auditar_pdf.py.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time

from auditar_pdf import compare, log_summary, save
from fuentes import inputs, check_case
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DOCS = [f'volumen-{n:02}/{name}' for n in range(1, 5) for name in ('main', 'solucionario')]


def snapshot(folder):
    shutil.copytree(ROOT, folder, ignore=shutil.ignore_patterns(
        '.git', 'tmp', '__pycache__', 'build', 'main.pdf', 'solucionario.pdf', '*.pyc'))
    for volume in ROOT.glob('volumen-*'):
        marker = volume / 'build/.gitkeep'
        if marker.exists():
            target = folder / volume.name / 'build/.gitkeep'
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(marker, target)


def run(folder, arguments, log):
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open('w', encoding='utf-8') as stream:
        result = subprocess.run(['latexmk', '-interaction=nonstopmode', '-halt-on-error', *arguments],
                                cwd=folder, stdout=stream, stderr=subprocess.STDOUT, text=True)
    assert result.returncode == 0, f'Compilacion fallida; consultar {log}'


def hashes(folder):
    return {path.relative_to(folder).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in folder.glob('volumen-*/*.pdf')}


def stamps(folder):
    return {path.relative_to(folder).as_posix(): path.stat().st_mtime_ns
            for pattern in ('volumen-*/*.pdf', 'volumen-*/build/*.log')
            for path in folder.glob(pattern)}


def check(folder, expected, reference, work, base_logs):
    assert set(hashes(folder)) == {f'{doc}.pdf' for doc in expected}, 'Se construyeron objetivos ajenos'
    assert {p.relative_to(folder).as_posix() for p in folder.rglob('*.pdf')} == {
        *(f'{doc}.pdf' for doc in expected),
        'comun/assets/escudo-esfm.pdf'}, 'Hay PDF generados fuera de las rutas previstas'
    results = {}
    readers = {doc: PdfReader(folder / f'{doc}.pdf') for doc in expected}
    names = {doc: reader.named_destinations for doc, reader in readers.items()}
    for doc in expected:
        volume, name = doc.split('/')
        for source in ('main.tex', 'solucionario.tex'):
            inputs(folder / volume / source, folder / volume)
        check_case(folder/'comun/assets/escudo-esfm.pdf')
        assert not list((folder / volume).glob('*.aux'))
        assert not list((folder / volume).glob('*.xdv'))
        logs = log_summary(folder / volume / 'build' / f'{name}.log')
        for key in ('errors', 'undefined', 'duplicate_labels', 'missing_glyphs', 'missing_fonts', 'overfull'):
            assert logs[key] == 0, (doc, logs)
        if base_logs:
            assert logs == base_logs[doc]['log'], (doc, 'Avisos distintos', logs)
        for page in readers[doc].pages:
            for ref in page.get('/Annots', []):
                link = ref.get_object()
                action = link.get('/A')
                if not action:
                    continue
                action = action.get_object()
                if action.get('/S') == '/GoToR':
                    assert action.get('/F') == 'main.pdf', action
                    assert action['/D'] in names[f'{volume}/main'], action
                elif action.get('/S') == '/GoTo' and isinstance(action.get('/D'), str):
                    assert action['/D'] in names[doc], action
        result = {'log': logs, 'pages': len(readers[doc].pages)}
        if reference:
            result['editorial'] = compare(reference / f'{doc}.pdf', folder / f'{doc}.pdf', work / 'diferencias' / doc)
            assert all(result['editorial']['checks'].values()), (doc, result['editorial'])
        results[doc] = result
    return results


def case(name, volume, kind, args, work, reference, base_logs):
    folder = work / name
    snapshot(folder)
    run(folder / volume, args, work / f'{name}.log')
    expected = [f'{volume}/main']
    if kind != 'main':
        expected.append(f'{volume}/solucionario')
    results = check(folder, expected, reference, work / name, base_logs)
    print(f'PASS {name}', flush=True)
    return name, results


def refresh_test(folder, work):
    volume = folder / 'volumen-01'
    chapter = volume / 'capitulos/01.tex'
    aux = volume / 'build/main.aux'
    copied = (volume / 'ejercicios-soluciones.tex').read_text(encoding='utf-8')
    old_aux = aux.read_text(encoding='utf-8')
    labels = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', copied)
    selected = None
    for label in labels:
        pattern = r'\\newlabel\{' + re.escape(label) + r'\}\{\{(1\.\d+)\}\{[^}]*\}\{[^}]*\}\{(teorema\.1\.\d+)\}'
        match = re.search(pattern, old_aux)
        if match:
            selected = label
            break
    assert selected, 'No se encontro una referencia teorica de prueba'
    original = chapter.read_text(encoding='utf-8')
    # La primera linea es la apertura de capitulo; se altera solo esta copia.
    first, rest = original.split('\n', 1)
    chapter.write_text(first+'\n\\setcounter{teorema}{20}\n'+rest, encoding='utf-8')
    before = stamps(folder)
    time.sleep(1.1) # Evita la resolucion de un segundo de algunas herramientas TeX.
    run(volume, ['solucionario.tex'], work / 'actualizacion-etiquetas.log')
    current_aux = aux.read_text(encoding='utf-8')
    updated = re.search(r'\\newlabel\{'+re.escape(selected)+r'\}\{\{([^}]+)\}\{[^}]*\}\{[^}]*\}\{([^}]+)\}', current_aux)
    assert updated and updated[1] != match[1]
    reader = PdfReader(volume / 'solucionario.pdf')
    remote = [a.get_object()['/A'].get_object().get('/D') for page in reader.pages
              for a in page.get('/Annots', []) if a.get_object().get('/A') and
              a.get_object()['/A'].get_object().get('/S') == '/GoToR']
    assert updated[2] in remote, 'El solucionario conservo un destino obsoleto'
    after = stamps(folder)
    assert after['volumen-01/main.pdf'] != before['volumen-01/main.pdf']
    assert after['volumen-01/solucionario.pdf'] != before['volumen-01/solucionario.pdf']
    assert all(after[key] == stamp for key, stamp in before.items() if not key.startswith('volumen-01/'))
    chapter.write_text(original, encoding='utf-8')
    run(volume, ['solucionario.tex'], work / 'restauracion-etiquetas.log')
    return {'label': selected, 'before': match[1], 'after': updated[1],
            'new_destination_in_solution': updated[2], 'other_volumes_unchanged': True,
            'test_source_restored': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--referencia', type=Path)
    parser.add_argument('--avisos-base', type=Path)
    parser.add_argument('--salida', type=Path, required=True)
    parser.add_argument('--trabajo', type=Path)
    args = parser.parse_args()
    reference = args.referencia.resolve() if args.referencia else None
    work = (args.trabajo or ROOT/'tmp'/f'aceptacion-{time.time_ns()}').resolve()
    work.mkdir(parents=True, exist_ok=False)
    base_logs = json.loads(args.avisos_base.read_text(encoding='utf-8')) if args.avisos_base else None
    matrix = {}
    jobs = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for n in range(1, 5):
            volume = f'volumen-{n:02}'
            for kind, command in (('main', ['main.tex']), ('solucionario', ['solucionario.tex']), ('pareja', [])):
                name = f'{volume}-{kind}'
                jobs.append(pool.submit(case, name, volume, kind, command, work, reference, base_logs))
        for job in as_completed(jobs):
            name, results = job.result()
            matrix[name] = results
            save(args.salida, {'matrix': matrix, 'complete': False})
    root_selection = {}
    for n in range(1, 5):
        folder = work / f'volumen-{n:02}-pareja'
        before = stamps(folder)
        for targets in ([f'volumen-{n:02}/main.tex'], [f'volumen-{n:02}/solucionario.tex'],
                        [f'volumen-{n:02}/main.tex', f'volumen-{n:02}/solucionario.tex']):
            run(folder, targets, work / f'seleccion-raiz-{n}-{len(targets)}-{Path(targets[0]).stem}.log')
            assert stamps(folder) == before, 'Seleccion desde raiz reconstruyo PDF al dia'
        root_selection[f'volumen-{n:02}'] = 'apuntes, solucionario y pareja: sin reconstrucciones ajenas'
    collection = work / 'coleccion'
    snapshot(collection)
    run(collection, [], work/'coleccion.log')
    matrix['coleccion'] = check(collection, DOCS, reference, work/'coleccion', base_logs)
    before = stamps(collection)
    run(collection, [], work/'sin-cambios.log')
    assert before == stamps(collection), 'Se reconstruyeron PDF sin cambios'
    before_hash = hashes(collection)
    run(collection, ['-c'], work/'limpieza.log')
    assert before_hash == hashes(collection), 'La limpieza modifico los PDF'
    assert not list(collection.glob('volumen-*/build/*.aux'))
    run(collection, [], work/'reconstruccion.log')
    matrix['reconstruccion'] = check(collection, DOCS, reference, work/'reconstruccion', base_logs)
    refresh = refresh_test(collection, work)
    matrix['restauracion'] = check(collection, DOCS, reference, work/'restauracion', base_logs)
    save(args.salida, {'complete': True, 'matrix': matrix, 'root_selection': root_selection,
                      'no_op_preserves_pdf_mtimes': True,
                      'clean_preserves_pdfs': True, 'reference_update': refresh,
                      'case_sensitive_os_tested': False,
                      'case_sensitive_limitation': 'WSL/Linux no disponible; se comprobaron las grafias de las rutas con los nombres reales.',
                      'temporary_directory': str(work)})
    print(f'PASS matriz completa, limpieza, reconstruccion y actualizacion de referencias: {args.salida}', flush=True)


if __name__ == '__main__':
    main()
