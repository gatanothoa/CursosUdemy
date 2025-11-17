#!/usr/bin/env python3
"""update_readmes.py

Generador básico de resúmenes automáticos e inserción entre marcadores.

Uso:
  python scripts/update_readmes.py --dry-run
  python scripts/update_readmes.py --push

El script busca los marcadores <!-- AUTO_SUMMARIES_START --> y <!-- AUTO_SUMMARIES_END -->
en los README y reemplaza el contenido entre ellos con resúmenes generados.
"""
import os
import re
import subprocess
from datetime import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
COURSES = ['Python', 'JavaScript', 'SQL']
MEMORIA = os.path.join(ROOT, 'MEMORIA UDEMY.md')

def find_last_day(course):
    """Encuentra la última carpeta 'Día ...' dentro de un curso.
    Soporta carpetas con número (Día 1, Día 2) o con nombre (Día Uno, Día cuatro).
    Prioriza carpetas que contienen un número; si no hay números usa la fecha
    de modificación más reciente.
    Devuelve el nombre de la carpeta encontrada o None.
    """
    path = os.path.join(ROOT, course)
    if not os.path.isdir(path):
        return None
    candidates = []
    for name in os.listdir(path):
        if re.match(r"^D[ií]a\b", name, re.IGNORECASE):
            mnum = re.search(r"(\d+)", name)
            num = int(mnum.group(1)) if mnum else None
            full = os.path.join(path, name)
            try:
                mtime = os.path.getmtime(full)
            except Exception:
                mtime = 0
            candidates.append((num, mtime, name))
    if not candidates:
        return None
    # Si hay candidatos con número, escoger el mayor número
    numeric = [c for c in candidates if c[0] is not None]
    if numeric:
        numeric.sort(key=lambda x: x[0])
        return numeric[-1][2]
    # Si no hay números, escoger por fecha de modificación
    candidates.sort(key=lambda x: x[1])
    return candidates[-1][2]

def build_block():
    t = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    blocks = []
    for c in COURSES:
        last = find_last_day(c)
        if last:
            # evitar duplicar 'Día' si la carpeta ya contiene la palabra
            low = last.lower()
            if low.startswith('día') or low.startswith('dia'):
                display = last
            else:
                display = f"Día {last}"
            blocks.append(f"### {c} — {display}\n\nResumen automático para {c} {display}.")
    if not blocks:
        return "(No se detectaron días en los cursos)"
    return '\n\n'.join(blocks)

def replace_between_markers(text, start_marker, end_marker, new_block):
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start == -1 or end == -1 or end < start:
        return None
    before = text[:start+len(start_marker)]
    after = text[end:]
    return before + '\n' + new_block + '\n' + after

def process_file(path, new_block, dry_run=False):
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        txt = fh.read()
    start = '<!-- AUTO_SUMMARIES_START -->'
    end = '<!-- AUTO_SUMMARIES_END -->'
    new = replace_between_markers(txt, start, end, new_block)
    if new is None:
        print(f'Marcadores no encontrados en {path}')
        return False
    if dry_run:
        print(f'--- Preview for {path} ---\n')
        print(new[new.find(start):new.find(end)+len(end)])
        return True
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(new)
    print(f'Actualizado {path}')
    return True

def git_commit_push(do_push=False):
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f"Auto: actualizar resúmenes {datetime.utcnow().date()}"], check=True)
        if do_push:
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
        return True, ''
    except subprocess.CalledProcessError as e:
        return False, str(e)

def main(dry_run=False, push=False):
    new_block = build_block()
    # process root README
    root_readme = os.path.join(ROOT, 'README.md')
    process_file(root_readme, new_block, dry_run=dry_run)
    # process language readmes
    for c in COURSES:
        lang_readme = os.path.join(ROOT, c, 'README.md')
        if os.path.exists(lang_readme):
            process_file(lang_readme, f"### {c} summary\n\n" + new_block, dry_run=dry_run)
    if dry_run:
        print('Dry-run completado. No se hicieron commits.')
        return 0
    ok, err = git_commit_push(do_push=push)
    if not ok:
        print('Git error:', err)
        return 2
    print('Commit realizado y push (si se solicitó) completado.')
    return 0

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--push', action='store_true')
    args = p.parse_args()
    exit(main(dry_run=args.dry_run, push=args.push))
