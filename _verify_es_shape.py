import os; os.environ['DJANGO_SETTINGS_MODULE']='marketweb.settings'
import django; django.setup()
from apps.catalog.template_content_albergo import ALBERGO_CONTENT_IT as IT
from apps.catalog.template_content_albergo_es import ALBERGO_CONTENT_ES as ES
def paths(o, p='', out=None):
    if out is None: out = []
    if isinstance(o, dict):
        for k, v in o.items(): paths(v, f'{p}.{k}' if p else k, out)
    elif isinstance(o, list) and o:
        e = o[0]
        if isinstance(e, dict):
            for k in e: out.append(f'{p}[0].{k}')
        elif isinstance(e, tuple):
            out.append(f'{p}[0]:tuple{len(e)}')
        else: out.append(f'{p}[0]:scalar')
    else: out.append(p)
    return out
ip = set(paths(IT)); ep = set(paths(ES))
print('IT paths:', len(ip), 'ES paths:', len(ep))
print('MISSING:', sorted(ip - ep))
print('EXTRA:', sorted(ep - ip))
assert ip == ep
print('SHAPE PARITY OK')

# Count anchor occurrences
import json
def walk_text(o, acc):
    if isinstance(o, str):
        acc.append(o)
    elif isinstance(o, dict):
        for v in o.values(): walk_text(v, acc)
    elif isinstance(o, (list, tuple)):
        for v in o: walk_text(v, acc)
texts = []
walk_text(ES, texts)
big = '\n'.join(texts).lower()
print('hospitalidad de borgo count:', big.count('hospitalidad de borgo'))
