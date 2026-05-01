"""Cornice workflow D · 45-route + anon-probe smoke walk + frozen-sibling probe.

Run from project root:
    python factory/reports/scorecard/cornice-workflowD-release-decision/_smoke.py
"""
import os
import sys
import pathlib
import django

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketweb.settings')
django.setup()

from django.test import Client  # noqa: E402
from django.contrib.auth import get_user_model  # noqa: E402

U = get_user_model()
u = U.objects.get(username='cornice_review')
c = Client()
c.force_login(u)

LOCALES = ['it', 'en', 'fr', 'es', 'ar']
PAGES = ['', 'studio/', 'servizi/', 'progetti/', 'contatti/']
CASES = [
    'biblioteca-pietrasanta-concorso',
    'via-volpe-roma-residenziale',
    'palazzo-lignari-bologna-restauro',
    'cornice-fronte-minore-saggio',
]
base = '/templates/business/cornice-architettura/preview/'

ok = fails = 0
fail_lines = []
for loc in LOCALES:
    for p in PAGES:
        url = (f'{base}{p}?preview=1' if loc == 'it'
               else f'{base}{p}?lang={loc}&preview=1')
        s = c.get(url).status_code
        if s == 200:
            ok += 1
        else:
            fails += 1
            fail_lines.append(f'FAIL {s} {url}')
    for slug in CASES:
        url = (f'{base}progetti/{slug}/?preview=1' if loc == 'it'
               else f'{base}progetti/{slug}/?lang={loc}&preview=1')
        s = c.get(url).status_code
        if s == 200:
            ok += 1
        else:
            fails += 1
            fail_lines.append(f'FAIL {s} {url}')

print(f'cornice staff routes: ok={ok} fails={fails}')
for ln in fail_lines:
    print(ln)

# Anonymous tier-gate probes
ca = Client()
print('anon catalog list:        ', ca.get('/templates/business/').status_code)
print('anon cornice preview:     ', ca.get(base).status_code)
print('anon cornice preview ?p:  ', ca.get(base + '?preview=1').status_code)
text = ca.get('/templates/business/').content.decode('utf-8', 'ignore')
print('cornice-architettura in anon catalog HTML (expected False):',
      'cornice-architettura' in text)

# Frozen-sibling regression probes (anon — must remain 200 in IT/EN/FR/ES/AR)
SIBLINGS = [
    'pragma-corporate-suite',
    'fiscus-commercialista',
    'solaria-coaching',
    'continua-stewardship',
]
print('frozen siblings (anon, 5 locales each):')
sib_ok = sib_fails = 0
for slug in SIBLINGS:
    row = []
    for loc in LOCALES:
        url = (f'/templates/business/{slug}/preview/' if loc == 'it'
               else f'/templates/business/{slug}/preview/?lang={loc}')
        s = ca.get(url).status_code
        row.append(f'{loc}={s}')
        if s == 200:
            sib_ok += 1
        else:
            sib_fails += 1
    print(f'  {slug:32s} ' + '  '.join(row))
print(f'frozen-sibling totals: ok={sib_ok} fails={sib_fails}')
